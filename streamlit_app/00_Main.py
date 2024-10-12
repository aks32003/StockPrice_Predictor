import streamlit as st

st.set_page_config(
    page_title="Stock Price Prediction Dashboard",
    page_icon="📊",
)

st.markdown(
    """# 📈 **Stock Price Prediction Dashboard**
### **Accurately Forecast Stock Prices with Machine Learning**

**The Stock Price Prediction Dashboard** is an advanced app built with Python and Streamlit, designed to help investors forecast stock prices using cutting-edge machine learning models. It leverages historical data to generate insightful predictions, making it easier for users to make informed investment decisions.

## **How It Works**

The Stock Price Prediction Dashboard operates through the following key steps:

1. **Stock Selection**: Users begin by selecting a stock ticker symbol of their choice.
2. **Real-Time Data Fetching**: The app retrieves historical stock price data directly from Yahoo Finance, using the YFinance library.
3. **Model Training**: An ARIMA time series forecasting model is trained on the fetched historical data, allowing for robust, statistical predictions.
4. **Price Prediction**: Once trained, the model generates multi-day price forecasts for the selected stock.
5. **Interactive Visualizations**: Using Plotly, the app presents interactive, detailed charts that show both historical price data and future forecasts, providing users with a clear visual understanding of potential trends.

## **Key Features**

- **Live Data**: Access up-to-date stock prices and financial metrics for accurate forecasting.
- **Interactive Charts**: Visualize historical stock performance and future projections with interactive, dynamic Plotly charts.
- **ARIMA Model**: Use the ARIMA model, a well-established technique for time series forecasting, to make informed predictions.
- **Backtesting Functionality**: Assess the accuracy of the model’s predictions by comparing forecasts to real historical performance.
- **User-Friendly Design**: The dashboard is designed to be responsive, offering an intuitive experience across all devices, including desktops, tablets, and smartphones.

## **Technologies Used**

Stock Price Prediction Dashboard is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Plotly** - To create interactive financial charts

## **Future Enhancements**

Some potential features for future releases:

- **More advanced forecasting models like LSTM**
- **Quantitative trading strategies**
- **Portfolio optimization and tracking**
- **Additional fundamental data**
- **User account system**

## **Disclaimer**

This app is for educational purposes and should not be considered financial advice. Users are encouraged to conduct their own research and consult with financial professionals before making any investment decisions. Predictions are based on historical data and statistical models, and there is no guarantee of future performance.
"""
)
