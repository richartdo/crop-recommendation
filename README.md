# 🌱 Crop Recommendation System

## 📌 Overview  
This project uses **Machine Learning** to recommend the most suitable crop to grow based on **soil nutrients (N, P, K), pH, rainfall, temperature, and humidity**.  
The model was trained and evaluated on the **[Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)**.  

## ✨ Features  
- Preprocessing with **Label Encoding** and **StandardScaler**  
- Multiple ML models tested (Decision Tree, Random Forest, Logistic Regression, etc.)  
- Best-performing model saved for deployment  
- Ready for deployment with **Flask / FastAPI** + **Render**  
- Jupyter Notebook included for reproducibility  

## 📂 Project Structure  
├── notebooks/
│   └── crop_recommendation.ipynb   # Training notebook
├── models/
│   ├── best_model.pkl              # Saved trained model
│   ├── scaler.pkl                  # StandardScaler object
│   └── label_encoder.pkl           # LabelEncoder object
├── app.py                          # API for deployment (to be added)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation

