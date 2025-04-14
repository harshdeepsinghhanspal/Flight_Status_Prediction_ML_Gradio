---
## ✈️ Flight Status Prediction with Gradio

This project utilizes machine learning to predict flight statuses—specifically, whether a flight will be on-time or delayed. 

The model is deployed using Gradio, providing an interactive web interface for users to input flight details and receive real-time predictions.​

---

## 🚀 Features
Machine Learning Model: Trained to classify flights as on-time or delayed based on input features.​

Interactive Interface: User-friendly web application built with Gradio.​

Preprocessing Tools: Includes a scaler for feature normalization.​

Deployment Ready: Easily deployable as a standalone web app.​

---

## 🧠 Model Overview
The model is trained on a dataset containing various flight attributes. Key steps in the model development include:​

Data Preprocessing: Cleaning and preparing the dataset for training.​

Feature Engineering: Selecting and transforming relevant features.​

Model Training: Using classification algorithms to train the model.​

Evaluation: Assessing model performance using appropriate metrics.​

---

## 🗂️ Repository Structure

The repository contains the following files:​

Flight_Status.ipynb: Jupyter Notebook detailing the data analysis and model training process.​

Flight_Status_Website_Gradio.py: Python script to launch the Gradio web application.​

flight_status_model.pkl: Serialized machine learning model.​

flight_status_scaler.pkl: Serialized scaler for input feature normalization.​

Flight_Status.txt: Additional documentation or notes.​

---

## ⚙️ Installation and Usage

Clone the Repository:

```
git clone https://github.com/harshdeepsinghhanspal/Flight_Status_Prediction_ML_Gradio.git
cd Flight_Status_Prediction_ML_Gradio
```

Install Dependencies:

Ensure you have Python installed. Then, install the required packages:

```
pip install numpy pandas scikit-learn gradio seaborn matplotlib
```

Run the Gradio App:

```
python Flight_Status_Website_Gradio.py
```

After running the script, a local URL will be provided. Open it in your web browser to access the application.

🖥️ Application Interface
The Gradio interface allows users to input flight details through a simple form. Upon submission, the application processes the inputs and displays the predicted flight status.​

---

## 📈 Model Performance

Accuracy: 98%​

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.​

