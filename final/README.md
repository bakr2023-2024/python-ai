# California Housing Price Prediction

This project aimed to predict California housing prices using **linear regression**, focusing on key features such as **median income**, **location**, and **household characteristics**.

## 📊 Data Preprocessing

- Handled missing values
- Encoded categorical variables (e.g., `ocean_proximity`)

## 🔍 Exploratory Data Analysis (EDA)

- **Median income** showed the strongest positive correlation with house prices (**correlation coefficient = 0.69**)
- Features like number of rooms and household size had weaker correlations
- Insights suggest that income plays a major role in determining housing costs

## 📈 Model Performance

- **Model:** Linear Regression
- **R² Score:** 64.88% – indicates the model explains a significant portion of the variance
- **Mean Squared Error (MSE):** ~4.8 billion – large error due to wide property value range

## ✅ Conclusion

The analysis confirms that **income** is a critical driver of housing prices in California. While the linear model provides a solid baseline, incorporating additional features and more sophisticated models could yield better results.
