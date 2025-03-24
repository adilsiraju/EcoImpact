Impact Calculator
-----------------

An ML model to predict environmental impacts (carbon reduced, energy saved, water conserved) based on investment amounts in various sustainability categories.

**Installation**

1\. Clone or download this repository:

git clone [https://github.com/adilsiraju/EcoImpact.git](https://github.com/adilsiraju/EcoImpact.git)

cd impact\_calculator

2\. Install dependencies:

pip install -r requirements.txt

3\. Run the script:

python impact\_calculator.py

**Usage**

Run the script and input:

\- Investment amount (in ₹)

\- Category (e.g., "Renewable Energy", "Water Conservation")

\- Technology (e.g., "Solar", "Manual")

**Example:**

Enter investment amount (₹): 15000

Enter category (e.g., 'Renewable Energy'): Renewable Energy

Enter technology (e.g., 'Solar'): Solar

Results for Renewable Energy:

Amount Invested: ₹15000.00

Carbon Reduced: 2000 kg

Energy Saved: 4000 kWh

Water Conserved: 0 L

**Categories**

\- Renewable Energy

\- Recycling

\- Emission Control

\- Water Conservation

\- Reforestation

\- Sustainable Agriculture

\- Clean Transportation

\- Waste Management

\- Green Technology

\- Ocean Conservation

**Technologies**

\- Solar, Wind, Hydro, Organic, Mechanical, Chemical, Biofuel, EV, Manual, AI

**Notes**

\- Models are trained on synthetic data and saved to \`models/\`.

\- Impacts scale linearly with investment, capped by category-specific limits.

\- For custom use, modify \`ImpactCalculator\` class or training data in \`train\_model()\`.

**Credits**

Developed with assistance from xAI's Grok 3.
