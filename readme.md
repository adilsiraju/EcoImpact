**Impact Calculator - Environmental Sustainability Prediction**

**Overview**
------------

The **Impact Calculator** is a standalone Python tool that predicts the environmental impact of sustainable investments. It estimates the following metrics based on investment details:

*   **Carbon Reduction (kg CO₂ saved)**
    
*   **Energy Savings (kWh saved/generated)**
    
*   **Water Conservation (liters saved)**
    

The model uses **machine learning (RandomForestRegressor)** trained on real-world sustainability data. It supports multiple **investment categories, locations, technologies, and project scales** to provide realistic impact estimates.

**Features**
------------

✔ **Predicts sustainability impact** based on investment amount and category.✔ **Supports multiple project categories**, including Renewable Energy, Recycling, and Emission Control.✔ **Handles different locations & technologies** with built-in encodings.✔ **Uses machine learning models** for accurate predictions.✔ **Dynamically adjusts outputs** based on project scale, duration, and location.✔ **Persists trained models** in the models/ directory for reuse.✔ **Standalone script** (no Django or external dependencies required).

**Installation**
----------------

### **Prerequisites**

Ensure you have Python **3.8+** installed. Then, install the required dependencies:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install numpy scikit-learn   `

### **Clone the Repository**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/your-username/impact-calculator.git  cd impact-calculator   `

**Usage**
---------

### **Run the Impact Calculator**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python impact_calculator.py   `

### **Example Input & Output**

#### **User Input:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`Enter investment amount (₹): 50000    Enter category (e.g., 'Renewable Energy'): Renewable Energy    Enter technology (e.g., 'Solar'): Solar    Enter location (e.g., 'Uttar Pradesh'): Rajasthan`  

#### **Output:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`Results for Renewable Energy:    Amount Invested: ₹50000.00      Carbon Reduced: 750 kg      Energy Saved: 1000 kWh      Water Conserved: 50 L`  

**How It Works**
----------------

1.  **Loads pre-trained models** (or trains new ones if missing).
    
2.  **Encodes user inputs** (investment amount, category, location, technology).
    
3.  **Applies data transformation** (log scaling, category encoding).
    
4.  **Uses trained models** to predict impact metrics.
    
5.  **Adjusts results dynamically** based on project factors.
    
6.  **Prints final impact estimates** to the user.
    

**Model Training & Persistence**
--------------------------------

*   **Stores models in models/** (carbon, energy, and water models).
    
*   **Uses pickle for persistence** (avoids retraining every run).
    
*   **Automatically trains models** if missing.
    

**Supported Investment Categories**
-----------------------------------

1.  **Renewable Energy**
    
2.  **Recycling**
    
3.  **Emission Control**
    
4.  **Water Conservation**
    
5.  **Reforestation**
    
6.  **Sustainable Agriculture**
    
7.  **Clean Transportation**
    
8.  **Waste Management**
    
9.  **Green Technology**
    
10.  **Ocean Conservation**
    

**Contributing**
----------------

Contributions are welcome! To contribute:

1.  Fork the repository.
    
2.  Create a new branch (feature-improvement).
    
3.  Commit and push changes.
    
4.  Submit a pull request.
    

**License**
-----------

This project is licensed under the **MIT License**.

**Author**
----------

**Mohammed Adil**For inquiries, reach out via GitHub or email.