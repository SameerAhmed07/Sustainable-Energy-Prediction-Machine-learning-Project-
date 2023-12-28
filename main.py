import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import random

# Load solar energy data
solar_data = pd.read_csv("solar_energy_production_30_years.csv")
# Train a linear regression model for solar energy prediction
solar_model = LinearRegression()
solar_model.fit(solar_data[['Year']], solar_data['Solar Energy Produced (MW)'])

# Load wind energy data
wind_data = pd.read_csv("wind_energy_production_30_years.csv")
# Train a linear regression model for wind energy prediction
wind_model = LinearRegression()
wind_model.fit(wind_data[['Year']], wind_data['Wind Energy Produced (MW)'])

quotes = [
    "The best time to plant a tree was 20 years ago. The second best time is now. -Chinese Proverb",
    "The future of energy is sustainable. Let's build it together.",
    "Renewable energy is the key to a cleaner, greener planet.",
    "Sustainability is not a choice; it's a responsibility.",
    "The sun is an infinite source of clean energy. Let's harness its power for a better future."
]

# Streamlit web app
st.set_page_config(
    page_title="Energy Prediction App",
    layout="wide"
)

# Sidebar for user input
current_year = datetime.now().year
selected_year = st.sidebar.slider("Select a future year", current_year + 1, current_year + 10)
selected_page = st.sidebar.radio("Select a prediction", ("Solar Energy", "Wind Energy"))


st.title("Future Energy Prediction")

if selected_page == "Solar Energy":
    # Predict energy production for solar
    predicted_solar_energy = solar_model.predict([[selected_year]])
    st.subheader("Predicted Solar Energy")
    st.markdown(
        f"<div style='font-size:18px; font-weight: bold; color: green; border: 2px solid green; padding: 10px; border-radius: 5px;'>{predicted_solar_energy[0]:.2f} MW</div>",
        unsafe_allow_html=True)

    # Plot solar energy data
    st.subheader("Solar Energy Production Over the Years")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x='Year', y='Solar Energy Produced (MW)', data=solar_data, color='orange', ax=ax)
    ax.scatter([selected_year], [predicted_solar_energy[0]], marker='*', color='red', s=200, zorder=5)
    plt.title('Solar Energy Production Over the Years', fontsize=16, fontweight='bold')
    st.pyplot(fig)

    # Calculate estimated carbon emissions avoided
    carbon_emissions_avoided_solar = predicted_solar_energy[0] * 0.5
    st.subheader(" * Pollution Reduced by Produced Solar Energy")
    st.markdown(
        f"By producing {predicted_solar_energy[0]:.2f} MW of solar energy, you've potentially avoided "
        f"{carbon_emissions_avoided_solar:.2f} tons of carbon emissions. This is equivalent to planting "
        f"{int(carbon_emissions_avoided_solar / 0.02)} trees annually."
    )

elif selected_page == "Wind Energy":
    # Predict energy production for wind
    predicted_wind_energy = wind_model.predict([[selected_year]])
    st.subheader("Predicted Wind Energy")
    st.markdown(
        f"<div style='font-size:18px; font-weight: bold; color: green; border: 2px solid green; padding: 10px; border-radius: 5px;'>{predicted_wind_energy[0]:.2f} MW</div>",
        unsafe_allow_html=True)

    # Plot wind energy data
    st.subheader("Wind Energy Production Over the Years")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x='Year', y='Wind Energy Produced (MW)', data=wind_data, color='blue', ax=ax)
    ax.scatter([selected_year], [predicted_wind_energy[0]], marker='*', color='red', s=200, zorder=5)

    plt.title('Wind Energy Production Over the Years', fontsize=16, fontweight='bold')
    st.pyplot(fig)

    # Calculate estimated carbon emissions avoided
    carbon_emissions_avoided_wind = predicted_wind_energy[0] * 0.7
    st.subheader(" * Pollution Reduced by Produced Wind Energy")
    st.markdown(
        f"By producing {predicted_wind_energy[0]:.2f} MW of wind energy, you've potentially avoided "
        f"{carbon_emissions_avoided_wind:.2f} tons of carbon emissions. This is equivalent to planting "
        f"{int(carbon_emissions_avoided_wind / 0.02)} trees annually."
    )
#This section specifys the Random quote to be displayed
st.markdown("---")
quote = random.choice(quotes)
st.markdown(f"<div style='font-size:24px; font-weight: bold; color: green;'>{quote}</div>", unsafe_allow_html=True)
