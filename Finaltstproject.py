import streamlit as st
import pickle

# Load the trained model
with open(r"C:\Users\GOWRI SANKAR\OneDrive\Desktop\frontend\finalmodel.pkl", "rb") as file:
    Regressor = pickle.load(file)

# Page Configuration
st.set_page_config(page_title="Air Quality Predictor", layout="centered", page_icon="🌤️")

# Apply custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            color: #333333;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 0.5em 1em;
            border: none;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center;'>🌍 Air Quality Index (AQI) Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter the gas concentrations to predict the air quality index and determine the pollution level.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input Section
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("🚗 CO (Carbon Monoxide) in ppm", min_value=0.0)
        b = st.number_input("☁️ Ozone (O₃) in ppm", min_value=0.0)
        c = st.number_input("🚛 NO₂ (Nitrogen Dioxide) in ppm", min_value=0.0)
    with col2:
        d = st.number_input("🔥 SO₂ (Sulfur Dioxide) in ppm", min_value=0.0)
        e = st.number_input("🌫️ PM2.5 (µg/m³)", min_value=0.0)
        f = st.number_input("🌁 PM10 (µg/m³)", min_value=0.0)

# Prediction Logic
if st.button("📊 Predict AQI"):
    result = Regressor.predict([[a, b, c, d, e, f]])
    predicted_aqi = result[0]
    st.success(f"✅ Predicted AQI: {predicted_aqi:.2f}")

    # AQI Interpretation
    if predicted_aqi < 50:
        st.markdown("🟢 **Air Quality: Good** – Air quality is considered satisfactory.")
    elif 50 <= predicted_aqi < 100:
        st.markdown("🟡 **Air Quality: Moderate** – Acceptable, but there may be concerns for sensitive individuals.")
    elif 100 <= predicted_aqi < 150:
        st.markdown("🟠 **Unhealthy for Sensitive Groups** – Members of sensitive groups may experience health effects.")
    elif 150 <= predicted_aqi < 200:
        st.markdown("🔴 **Unhealthy** – Everyone may begin to experience health effects.")
    elif 200 <= predicted_aqi < 300:
        st.markdown("🟣 **Very Unhealthy** – Health alert: everyone may experience more serious health effects.")
    else:
        st.markdown("⚫ **Hazardous** – Health warnings of emergency conditions.")

# Footer
st.markdown("---")
