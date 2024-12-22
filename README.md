# Dissertation title
National Net-Zero Targets: Are they achievable? Assessing the funding sufficiency for developing economies to achieve climate goals

# About repository
This repository contains the python code used in the dissertation to calculate the energy output in Terra watt hours (TWh) using Multiple Linear Regression (MLR) Model to calculate the projected energy requirement in India in the year 2050

# Inputs
1.	GDP (Annual percent change)
•	Historical data from 1980 to 2023
•	Future projections assumed at 6.5% constant growth from 2024 to 2050

2.	Population 
•	Historical data from 1980 to 2023
•	Projected population numbers until 2050 based on demographic forecasts

3.	Per Capita Energy Consumption (kWh) 
•	Historical data from 1980 to 2023
•	Future projections following historical growth patterns
•	Used 5.38% growth rate to fill historical gaps
•	Post-2023 projections based on anticipated consumption patterns

# Data Split
•	Training Data: 1980-2023 (43 years of historical data)
•	Prediction Period: 2024-2050 (27 years of forecasting)

# Assumptions
On top of assumptions made by the model, this case study also considers the data related assumptions. For Per capital consumption of electricity in India, the Central Electricity Authority of India does not provide forecasted figures for years between 2025 and 2050. To overcome this situation, the model uses the conversative approach by applying pre-covid average growth in per capital consumption until year 2017. For GDP, IMF only provides forecast until 2029. To be able to get the forecast until 2050, the model assumes the 6.5% GDP growth which was provided by IMF as forecast from year 2025 and until 2029. The population growth forecast does not have any adjustments in the model and is completely adapted as it was provided by the World Bank.

# Output
Model Performance (R-squared = 0.9990):
•	The R² value of 0.9990 (99.90%) indicates the model explains almost all the variation in electricity demand
•	This extremely high value suggests a very strong fit, though it might indicate potential overfitting
Feature Coefficients (how each variable affects the prediction):
•	GDP: 562,719,328.8027 kWh (0.56 TWh) increase for each 1% increase in GDP
•	Population: -658.5875 kWh decrease for each additional person (this negative coefficient is counterintuitive and might indicate multicollinearity)
•	Per Capita Energy: 1.96 TWh increase for each 1 kWh increase in per capita consumption

# Year-wise Predictions of energy required in TWh:
•	2025: 2,155.56 TWh
•	2030: 2,978.31 TWh (38% increase from 2025)
•	2035: 4,064.66 TWh (36% increase from 2030)
•	2040: 5,478.58 TWh (35% increase from 2035)
•	2045: 7,347.86 TWh (34% increase from 2040)
•	2050: 9,810.66 TWh (33% increase from 2045)

# Key Observations:
•	The demand shows a consistent upward trend
•	Growth rate slightly decreases over time (from 38% to 33% per 5-year period)
•	Total demand is predicted to increase by about 4.5 times from 2025 to 2050

# Potential Concerns:
•	The negative population coefficient is counterintuitive
•	The remarkably high R² might indicate overfitting
•	The growth rates seem quite high and should be validated against other forecasts
