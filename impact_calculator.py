import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
import os


class ImpactCalculator:
    def __init__(self, model_dir='models'):
        self.model_carbon = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_split=5, random_state=42)
        self.model_energy = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_split=5, random_state=42)
        self.model_water = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_split=5, random_state=42)
        self.scaler = StandardScaler()
        self.label_encoder_location = LabelEncoder()
        self.label_encoder_technology = LabelEncoder()

        # Define paths for model persistence
        self.model_dir = model_dir
        self.model_file_carbon = os.path.join(model_dir, 'carbon_model.pkl')
        self.model_file_energy = os.path.join(model_dir, 'energy_model.pkl')
        self.model_file_water = os.path.join(model_dir, 'water_model.pkl')
        self.scaler_file = os.path.join(model_dir, 'scaler.pkl')

        # Categories for classification
        self.categories = [
            'Renewable Energy', 'Recycling', 'Emission Control', 'Water Conservation',
            'Reforestation', 'Sustainable Agriculture', 'Clean Transportation',
            'Waste Management', 'Green Technology', 'Ocean Conservation'
        ]

        # Location & Technology Encoding
        self.label_encoder_location.fit([
            'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
            'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
            'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
            'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
        ])
        self.label_encoder_technology.fit(['Solar', 'Wind', 'Hydro', 'Organic', 'Mechanical', 'Chemical', 'Biofuel', 'EV', 'Manual', 'AI'])

        self.load_or_train_model()

    def load_or_train_model(self):
        """ Load existing models or train new ones if not found. """
        try:
            if all(os.path.exists(f) for f in [self.model_file_carbon, self.model_file_energy, self.model_file_water, self.scaler_file]):
                print("Loading pre-trained models and scaler...")
                with open(self.model_file_carbon, 'rb') as f:
                    self.model_carbon = pickle.load(f)
                with open(self.model_file_energy, 'rb') as f:
                    self.model_energy = pickle.load(f)
                with open(self.model_file_water, 'rb') as f:
                    self.model_water = pickle.load(f)
                with open(self.scaler_file, 'rb') as f:
                    self.scaler = pickle.load(f)
                print("Models and scaler loaded successfully.")
            else:
                print("Model files missing. Training new models...")
                self.train_model()
        except Exception as e:
            print(f"Failed to load models: {e}. Training new models...")
            self.train_model()

    def train_model(self):
        """ Train RandomForest models and save them. """
        X = np.array([
            [500000, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 5, 0, 0],  
            [100000, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 3, 0, 0],  
            [10000, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 0, 0],    
        ])

        y_carbon = np.array([750, 500, 150])
        y_energy = np.array([1000, 600, 200])
        y_water = np.array([50, 30, 0])

        # Transform features
        X[:, 0] = np.log1p(X[:, 0])  # Apply log transformation for scaling
        self.scaler.fit(X)
        X_transformed = self.scaler.transform(X)

        # Train models
        self.model_carbon.fit(X_transformed, y_carbon)
        self.model_energy.fit(X_transformed, y_energy)
        self.model_water.fit(X_transformed, y_water)

        # Save models
        os.makedirs(self.model_dir, exist_ok=True)
        with open(self.model_file_carbon, 'wb') as f:
            pickle.dump(self.model_carbon, f)
        with open(self.model_file_energy, 'wb') as f:
            pickle.dump(self.model_energy, f)
        with open(self.model_file_water, 'wb') as f:
            pickle.dump(self.model_water, f)
        with open(self.scaler_file, 'wb') as f:
            pickle.dump(self.scaler, f)

    def predict_impact(self, investment_amount, category_names, project_duration_months=12, project_scale=1, location='Uttar Pradesh', technology_type='Manual'):
        investment_amount = float(investment_amount)
        location_encoded = self.label_encoder_location.transform([location])[0] if location in self.label_encoder_location.classes_ else 0
        technology_encoded = self.label_encoder_technology.transform([technology_type])[0] if technology_type in self.label_encoder_technology.classes_ else 0

        category_vector = [1 if cat in category_names else 0 for cat in self.categories]
        interaction_term = investment_amount * project_duration_months

        X = np.array([[investment_amount, interaction_term] + category_vector + [project_duration_months, project_scale, location_encoded, technology_encoded]])
        X[:, 0] = np.log1p(X[:, 0])  # Apply log transformation
        X[:, 1] = np.log1p(X[:, 1])  

        X_transformed = self.scaler.transform(X)

        carbon_reduced = max(0, self.model_carbon.predict(X_transformed)[0])
        energy_saved = max(0, self.model_energy.predict(X_transformed)[0])
        water_conserved = max(0, self.model_water.predict(X_transformed)[0])

        return carbon_reduced, energy_saved, water_conserved


def main():
    calc = ImpactCalculator()
    investment = float(input("Enter investment amount (₹): "))
    category = input("Enter category (e.g., 'Renewable Energy'): ")
    tech = input("Enter technology (e.g., 'Solar'): ")
    location = input("Enter location (e.g., 'Uttar Pradesh'): ")

    carbon, energy, water = calc.predict_impact(investment, [category], location=location, technology_type=tech)
    
    print(f"\nResults for {category}:")
    print(f"  Amount Invested: ₹{investment:.2f}")
    print(f"  Carbon Reduced: {carbon:.0f} kg")
    print(f"  Energy Saved: {energy:.0f} kWh")
    print(f"  Water Conserved: {water:.0f} L")


if __name__ == "__main__":
    main()