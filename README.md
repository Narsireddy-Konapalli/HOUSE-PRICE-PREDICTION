# 🏡 House Price Prediction

## 📖 Project Overview

This project focuses on predicting house prices using a **Gradient Boosting Regressor** model. The model is trained on a comprehensive dataset containing various features of houses, such as the number of bedrooms, bathrooms, and square footage, to accurately forecast prices. 

The Gradient Boosting Regressor is a powerful ensemble learning technique that builds a series of decision trees, with each tree correcting the errors of the previous one. To further enhance the model's performance, **hyperparameter tuning** was conducted using **GridSearchCV**.

## 📊 Features Used

The model uses the following features from the dataset:
- **bedrooms**: Number of bedrooms
- **bathrooms**: Number of bathrooms
- **sqft_living**: Living area in square feet
- **sqft_lot**: Lot size in square feet
- **floors**: Number of floors
- **waterfront**: Whether the house has a waterfront view (binary)
- **view**: Quality of the view (rating)
- **condition**: Overall condition of the house
- **grade**: Grade based on the construction and design quality
- **sqft_above**: Square footage of the house above ground
- **sqft_basement**: Square footage of the basement
- **yr_built**: Year the house was built
- **yr_renovated**: Year the house was renovated
- **lat**: Latitude coordinate
- **long**: Longitude coordinate
- **sqft_living15**: Living area of the nearest 15 neighbors
- **sqft_lot15**: Lot size of the nearest 15 neighbors
- **years**: The age of the house

Additionally, **feature engineering** was performed to create new features from the existing data, capturing hidden relationships and boosting the model's predictive power.

## 🔧 Model Training & Hyperparameter Tuning

The Gradient Boosting Regressor was fine-tuned using **GridSearchCV** to identify the optimal hyperparameters. The key hyperparameters tuned include:
- **n_estimators**: Number of boosting stages
- **learning_rate**: Shrinks the contribution of each tree
- **max_depth**: Maximum depth of each tree
- **min_samples_split**: Minimum samples required to split a node
- **min_samples_leaf**: Minimum samples required at each leaf node

The best model achieved:
- **R-squared (R²)**: 0.90
- **Root Mean Squared Error (RMSE)**: 121,494
- **Mean Absolute Error (MAE)**: 66,474

## 🎨 Streamlit App

A user-friendly **Streamlit** web application was built to allow users to input house features and receive real-time price predictions. The app displays the predicted price instantly and features an intuitive, clean design.

## 🚀 Deployment

The model and web app have been deployed on **Hugging Face Spaces** for public access:

👉 [Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/Narsireddy-Konapalli/house-price-prediction)

## 📦 Installation

Clone the repository and install dependencies:

```bash
# Clone the repo
git clone https://github.com/Narsireddy-Konapalli/house-price-prediction.git

# Change directory
cd house-price-prediction

# Install required libraries
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## 📁 Project Structure

```
.
├── data/                        # Dataset
├── models/                      # Saved model files
├── app.py                       # Streamlit app
├── train_model.py               # Model training script
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
```

## 🌟 Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

## 📧 Contact

For any inquiries, please reach out via:
- **Email**: [konapallinarsireddy@gmail.com](mailto:konapallinarsireddy@gmail.com)
- **LinkedIn**: [Narsireddy-Konapalli](https://www.linkedin.com/in/narsireddyk/)

---

Thank you for visiting the project! 🙌
