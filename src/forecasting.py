import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


# -------------------------------
# PROPHET FORECASTING
# -------------------------------

def prophet_forecasting(df, periods=30):

    prophet_df = df.rename(columns={
        "date": "ds",
        "price": "y"
    })

    model = Prophet()

    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=periods)

    forecast = model.predict(future)

    return forecast


# -------------------------------
# ARIMA FORECASTING
# -------------------------------

def arima_forecasting(df, steps=30):

    series = df["price"]

    model = ARIMA(series, order=(5,1,0))

    model_fit = model.fit()

    forecast = model_fit.forecast(steps=steps)

    return forecast


# -------------------------------
# LSTM FORECASTING
# -------------------------------

def lstm_forecasting(df):

    data = df["price"].values
    data = data.reshape(-1,1)

    scaler = MinMaxScaler()

    data_scaled = scaler.fit_transform(data)

    X = []
    y = []

    for i in range(60, len(data_scaled)):
        X.append(data_scaled[i-60:i,0])
        y.append(data_scaled[i,0])

    X = np.array(X)
    y = np.array(y)

    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    model = Sequential()

    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1],1)))
    model.add(LSTM(50))
    model.add(Dense(1))

    model.compile(
        optimizer="adam",
        loss="mean_squared_error"
    )

    model.fit(X, y, epochs=5, batch_size=32)

    return model
