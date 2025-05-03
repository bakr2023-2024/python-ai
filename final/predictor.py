import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#load and clean data
data = pd.read_csv("housing.csv")
data.dropna(inplace=True)
#encode categorical columns
data = pd.get_dummies(data, columns=["ocean_proximity"], drop_first=True)
#setup x and y data
X = data.drop("median_house_value", axis=1)
y = data["median_house_value"]
#setup heatmap to determine variables that correlate positively with 'median house value'
heatmap = sns.heatmap(data.corr(), annot=True)
plt.title("Feature Correlation with House Value")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
#confirm that 'median income'(from heatmap) has highest positive correlation with 'median house value'
scatter = plt.scatter(data["median_income"], data["median_house_value"], s=10)
plt.xlabel("Median Income")
plt.ylabel("House Value ($)")
plt.title("Income vs. House Value")
plt.tight_layout()
plt.show()

# train-test split and model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2 * 100:.2f}%")