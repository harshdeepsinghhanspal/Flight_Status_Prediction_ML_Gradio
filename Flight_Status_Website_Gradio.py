import gradio as gr
import numpy as np
import pickle

# Load the trained model
with open('flight_status_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the scaler
with open('flight_status_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Prediction function
def predict_flight_status(wind_speed, temperature, humidity):
    new_data = np.array([[wind_speed, temperature, humidity]])
    new_data_scaled = scaler.transform(new_data)
    prediction = model.predict(new_data_scaled)

    result = "✅ Flight Status: Fly" if prediction[0] == 1 else "❌ Flight Status: Don't Fly"
    
    return result, new_data.tolist(), new_data_scaled.tolist(), prediction.tolist()

# Gradio interface
demo = gr.Interface(
    fn=predict_flight_status,
    inputs=[
        gr.Slider(0, 100, value=20, label="Wind Speed (km/h)"),
        gr.Slider(-10, 50, value=25, label="Temperature (°C)"),
        gr.Slider(0, 100, value=50, label="Humidity (%)"),
    ],
    outputs=[
        gr.Text(label="Prediction"),
        gr.JSON(label="Raw Input"),
        gr.JSON(label="Scaled Input"),
        gr.JSON(label="Prediction Output"),
    ],
    title="Flight Status Predictor ✈️",
    description="Predict whether it's safe to fly based on wind speed, temperature, and humidity."
)

demo.launch()