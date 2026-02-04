import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("house_price.csv")

# Features and target
X = data[['sqft', 'rooms', 'bathrooms']]
y = data['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction function
def predict_price(sqft, rooms, bathrooms):
    return model.predict([[sqft, rooms, bathrooms]])[0]
