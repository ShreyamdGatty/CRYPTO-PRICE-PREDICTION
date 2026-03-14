import matplotlib.pyplot as plt

def volatility_analysis(df):

    df["returns"] = df["price"].pct_change()

    plt.hist(df["returns"].dropna(), bins=50)
    plt.title("Volatility Distribution")
    plt.show()
