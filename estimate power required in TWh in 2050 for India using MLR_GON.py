import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

def read_excel_data(filename):
    """
    Read data from three sheets of an Excel workbook
    
    Parameters:
    filename (str): Path to the Excel file
    
    Returns:
    tuple: (years, gdp_values, population_values, per_capita_energy)
    """
    try:
        # Read data from each sheet
        gdp_df = pd.read_excel(filename, sheet_name='GDP')
        population_df = pd.read_excel(filename, sheet_name='Population')
        energy_df = pd.read_excel(filename, sheet_name='Per_Capita_Energy')
        
        # Assuming each sheet has 'Year' and 'Value' columns
        years = gdp_df['Year'].values
        gdp_values = gdp_df['Value'].values
        population_values = population_df['Value'].values
        per_capita_energy = energy_df['Value'].values
        
        return years, gdp_values, population_values, per_capita_energy
    
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        raise

def predict_electricity_demand(data):
    """
    Predict electricity demand using GDP, population, and per capita energy consumption
    """
    # Prepare features (X) and target (y)
    X = data[['GDP', 'Population', 'Per_Capita_Energy']]
    y = data['Total_Energy'] = data['Population'] * data['Per_Capita_Energy']
    
    # Split data into training and testing sets
    train_mask = data['Year'] <= 2023
    X_train = X[train_mask]
    y_train = y[train_mask]
    X_future = X[~train_mask]
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred_train = model.predict(X_train)
    y_pred_future = model.predict(X_future)
    
    # Calculate R-squared for training data
    r2 = r2_score(y_train, y_pred_train)
    
    # Create predictions DataFrame
    predictions = pd.DataFrame({
        'Year': data['Year'],
        'Actual': y,
        'Predicted_kWh': np.concatenate([y_pred_train, y_pred_future])
    })
    
    # Add TWh column
    predictions['Predicted_TWh'] = predictions['Predicted_kWh'] / 1e9
    
    return model, predictions, r2

def main():
    # Read data from Excel file
    try:
        years, gdp_values, population_values, per_capita_energy = read_excel_data(r"C:\Users\nbvso1\Downloads\Data inputs GON.xlsx")
        
        # Create DataFrame
        data = pd.DataFrame({
            'Year': years,
            'GDP': gdp_values,
            'Population': population_values,
            'Per_Capita_Energy': per_capita_energy
        })
        
        # Run the model
        model, predictions, r2 = predict_electricity_demand(data)
        
        # Print model performance
        print(f"Model R-squared: {r2:.4f}")
        print("\nFeature coefficients:")
        for feature, coef in zip(['GDP', 'Population', 'Per_Capita_Energy'], model.coef_):
            print(f"{feature}: {coef:.4f}")
        
        # Create and display future predictions table (2025-2050)
        future_predictions = predictions[predictions['Year'] >= 2025].copy()
        future_predictions = future_predictions[['Year', 'Predicted_kWh', 'Predicted_TWh']]
        
        print("\nYear-wise Predictions for Total Energy Demand (2025-2050):")
        print("\nYear      Predicted Total Energy Demand (TWh)")
        print("-" * 30)
        for _, row in future_predictions.iterrows():
            print(f"{int(row['Year'])}      {row['Predicted_TWh']:,.2f}")
        
        # Plot results
        plt.figure(figsize=(12, 6))
        plt.plot(predictions['Year'], predictions['Actual']/1e9, label='Actual', marker='o')
        plt.plot(predictions['Year'], predictions['Predicted_TWh'], label='Predicted', marker='x')
        plt.axvline(x=2023, color='r', linestyle='--', label='Training Cutoff')
        plt.title('Total Energy Demand Prediction')
        plt.xlabel('Year')
        plt.ylabel('Total Energy Demand (TWh)')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    except Exception as e:
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
