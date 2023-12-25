1. SUSTAINABLE ENERGY PREDICTION WEB APP

   This is a web app built using Streamlit that predicts future energy production based on linear regression models trained on historical data for solar and wind energy.

2. DATA SOURCES USED
   
   The app uses the following datasets for training the models:
   - [Solar Energy Production Data (30 Years)](solar_energy_production_30_years.csv)
   - [Wind Energy Production Data (30 Years)](wind_energy_production_30_years.csv)
  
3.MODEL TRAINING WITH SCIKIT-LEARN
     The Energy Prediction App utilizes the powerful machine learning library Scikit-Learn, to train linear regression models for forecasting both solar and wind energy production.
    -Linear regression is a statistical method that models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.
    -Linear regression is chosen for its simplicity and interpretability, making it a suitable choice for predicting energy production based on historical trends.
    The models aim to capture the linear relationship between the 'Year' (independent variable) and the corresponding 'Solar Energy Produced' or 'Wind Energy Produced' (dependent variable) over the provided 30- 
    year datasets.
   
4.STEPS IN MODEL TRAINING
  
  4.1 DATA LOADING:
      Historical data for both solar and wind energy production is loaded from the provided datasets ('solar_energy_production_30_years.csv') and ('wind_energy_production_30_years.csv').
  
  4.2 MODEL INITIALIZATION:
      Separate instances of the Linear Regression model are created for solar and wind energy prediction.
  
  4.3 MODEL FITTING:
      The linear regression models are trained on the historical data using the fit method, which estimates the coefficients of the linear equation.
  
  4.4 PREDICTION:
  
      After training, the models are capable of predicting future energy production for a specified year using the predict method.
      - # Predict energy production for solar
        predicted_solar_energy = solar_model.predict([[selected_year]])
      - # Predict energy production for wind
        predicted_wind_energy = wind_model.predict([[selected_year]])
  These trained models enable the Energy Prediction App to provide insights into the expected solar and wind energy production for a user-selected future year.
  The simplicity and effectiveness of linear regression, coupled with Scikit-Learn's user-friendly implementation, contribute to the accuracy and reliability of the energy predictions presented by the app.
  
5.SIDE BAR:
  
  Here i created a sidebar to select a future year and the type of energy prediction (Solar or Wind).
  
6.RESULTS:
  
  6.1 Solar Energy Prediction:
  
      -The app predicts the solar energy production in megawatts for the selected future year.
      -It visualizes the historical solar energy production over the years and marks the predicted value on the plot.
      -It calculates the estimated carbon emissions avoided by the solar energy production.
  
  6.2 Wind Energy Prediction:
  
     -The app predicts the wind energy production in megawatts for the selected future year.
     -It visualizes the historical wind energy production over the years and marks the predicted value on the plot.
     -It calculates the estimated carbon emissions avoided by the wind energy production.
  
  6.3 Random Quote:
  
      At the end of each prediction, a random inspirational quote related to renewable energy is displayed.

   
