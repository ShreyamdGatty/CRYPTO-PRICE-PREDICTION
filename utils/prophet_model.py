from prophet import Prophet

def prophet_forecast(df):

    df = df.rename(columns={
        "date":"ds",
        "price":"y"
    })

    model = Prophet()

    model.fit(df)

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    return forecast
