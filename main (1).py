import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="AI Stock Analyzer", page_icon="📈", layout="wide")

st.title("📈 AI Stock Analyzer")

stock = st.text_input("Enter Stock Symbol", "RELIANCE.NS")

if st.button("Analyze"):
    data = yf.download(stock, period="1y", progress=False, auto_adjust=False)

    if data.empty:
        st.error("Invalid Stock Symbol")
        st.stop()

    open_price = data["Open"].squeeze()
    high_price = data["High"].squeeze()
    low_price = data["Low"].squeeze()
    close_price = data["Close"].squeeze()
    volume = data["Volume"].squeeze()

    ma20 = close_price.rolling(20).mean()
    ma50 = close_price.rolling(50).mean()

    current_price = float(close_price.iloc[-1])
    high52 = float(high_price.max())
    low52 = float(low_price.min())

    st.success(f"Showing data for {stock}")

    c1, c2, c3 = st.columns(3)
    c1.metric("Current Price", f"₹{current_price:.2f}")
    c2.metric("52 Week High", f"₹{high52:.2f}")
    c3.metric("52 Week Low", f"₹{low52:.2f}")

    st.subheader("Recent Data")
    st.dataframe(data.tail())

    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=data.index,
        open=open_price,
        high=high_price,
        low=low_price,
        close=close_price,
        name="Price"
    ))

    fig.add_trace(go.Scatter(
        x=data.index,
        y=ma20,
        mode="lines",
        name="MA20"
    ))

    fig.add_trace(go.Scatter(
        x=data.index,
        y=ma50,
        mode="lines",
        name="MA50"
    ))

    fig.update_layout(
        template="plotly_dark",
        height=700,
        title=f"{stock} Candlestick Chart",
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Volume")

    volume_fig = go.Figure()
    volume_fig.add_trace(go.Bar(
        x=data.index,
        y=volume,
        name="Volume"
    ))

    volume_fig.update_layout(
        template="plotly_dark",
        height=300
    )

    st.plotly_chart(volume_fig, use_container_width=True)
