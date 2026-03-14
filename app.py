import streamlit as st
import plotly.express as px
from src.data_collection import get_crypto_data
from src.preprocessing import clean_data
from src.sentiment_analysis import sentiment_analysis
from src.volatility_analysis import volatility_analysis
from models.prophet_model import prophet_forecast

# Page Configuration
st.set_page_config(
    page_title="Crypto AI Dashboard",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    font-size:40px;
    font-weight:700;
    text-align:center;
    background: -webkit-linear-gradient(#00F5A0, #00D9F5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.card {
    background-color:#1c1f26;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.4);
}

.metric {
    font-size:22px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)


# Title
st.markdown('<p class="title">🚀 Cryptocurrency Price Analysis Dashboard</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ Dashboard Settings")

coin = st.sidebar.selectbox(
    "Select Cryptocurrency",
    ["bitcoin", "ethereum", "dogecoin"]
)

st.sidebar.info("AI powered crypto analytics dashboard")


# Fetch Data
data = get_crypto_data(coin)
data = clean_data(data)

# Layout columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Latest Price", f"${data['price'].iloc[-1]:.2f}")

with col2:
    st.metric("Highest Price", f"${data['price'].max():.2f}")

with col3:
    st.metric("Lowest Price", f"${data['price'].min():.2f}")


# Raw Data Section
st.markdown("### 📊 Latest Data")
st.dataframe(data.tail(), use_container_width=True)


# Price Trend Graph
st.markdown("### 📈 Price Trend")

fig = px.line(
    data,
    x="date",
    y="price",
    title=f"{coin.capitalize()} Price Trend",
    template="plotly_dark"
)

fig.update_layout(
    title_x=0.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)


# Volatility Analysis
# st.markdown("### 📉 Volatility Analysis")
# volatility_analysis(data)


# # Sentiment Analysis
# st.markdown("### 🧠 Market Sentiment")
# sentiment_analysis(coin)


# Forecast Section
st.markdown("### 🔮 AI Price Forecast")

forecast = prophet_forecast(data)

st.success("Forecast completed successfully!")