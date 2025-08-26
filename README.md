# 🌱 Crop Recommendation System  

## 📌 Overview  
This project leverages **Machine Learning** to recommend the most suitable crop to grow based on key agricultural factors:  
- **Soil nutrients:** Nitrogen (N), Phosphorus (P), Potassium (K)  
- **Environmental conditions:** pH, Rainfall, Temperature, Humidity  

The model was trained and evaluated on the **[Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)** and deployed as an API using **Flask** on **Render**.  

---

## ✨ Features  
- ✅ Data preprocessing with **Label Encoding** and **StandardScaler**  
- ✅ Multiple ML models tested (Decision Tree, Random Forest, Logistic Regression, etc.)  
- ✅ **XGBoost** chosen as the best-performing model  
- ✅ Saved trained model + scaler + label encoder for reproducibility  
- ✅ REST API built with **Flask** for deployment  
- ✅ Hosted live on **Render**  

---

## 📂 Project Structure  



---

## 🚀 Live API  
- **Base URL:** [https://crop-recommendation-2-u8wx.onrender.com](https://crop-recommendation-2-u8wx.onrender.com)  
- **Health Check:** `/` → Returns a JSON welcome message  
- **Prediction Endpoint:** `/predict`  

### 🔧 Usage  

#### Endpoint: `/predict`  
- **Method:** `POST`  
- **Headers:**  
  `Content-Type: application/json`  

#### Example Request  
```json
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.5,
  "humidity": 80,
  "ph": 6.5,
  "rainfall": 200
}

