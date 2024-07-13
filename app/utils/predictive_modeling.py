from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def predict_stock_prices(data):
    data = data[['Close']]
    data['Prediction'] = data['Close'].shift(-30)

    X = np.array(data.drop(['Prediction'], 1))[:-30]
    y = np.array(data['Prediction'])[:-30]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    lr = LinearRegression().fit(X_train, y_train)
    lr_prediction = lr.predict(X_test)
    
    dt = DecisionTreeRegressor().fit(X_train, y_train)
    dt_prediction = dt.predict(X_test)
    
    rf = RandomForestRegressor().fit(X_train, y_train)
    rf_prediction = rf.predict(X_test)
    
    return {
        'Linear Regression': lr_prediction,
        'Decision Tree': dt_prediction,
        'Random Forest': rf_prediction
    }
