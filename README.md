# Real-Time Stock Visualizer

# 🇬🇧 English Version

## Objective
This Streamlit web application allows users to visualize real-time stock market data with technical indicators such as SMA, EMA, RSI, Bollinger Bands, and MACD.  
The project combines financial market analysis and data visualization to provide an interactive and dynamic overview of stock price movements.

## Requirements

- Python 3.10 or higher  
- Compatible with macOS, Linux, and Windows  
- Internet connection (data retrieved using `yfinance`)  
- Optional: API key for alternative data sources (e.g., AlphaVantage, Finnhub)
 
## Installation

    ```bash
    # 1. Clone the repository
    git clone https://github.com/Pooranan11/Real-Time-Stock-Visualizer.git
    cd Real-Time-Stock-Visualizer

    # 2. Create a virtual environment
    python -m venv .venv
    # macOS/Linux
    source .venv/bin/activate
    # Windows (PowerShell)
    # .venv\Scripts\Activate.ps1

    # 3. Install dependencies
    pip install --upgrade pip
    pip install -r requirements.txt
    # If the file does not exist:
    # pip install streamlit yfinance pandas numpy plotly ta
    ```

### Running the Application
    
    ```bash
    streamlit run main.py
    ```

The app will automatically open in your browser at http://localhost:8501.

### Project Structure

.
├── main.py              # Streamlit entry point
├── requirements.txt     # Dependencies
└── README.md            # Documentation

You can later refactor your code as follows:
data_loader.py for data loading
indicators.py for indicator calculations
ui_components.py for Streamlit interface elements

Features
1. **Data Loading**

    Source: Yahoo Finance (yfinance)
    Available periods: 1mo, 3mo, 6mo, 1y, 5y
    Intervals: 5m, 15m, 30m, 1h, 1d
    Automatic price adjustment

2. **Technical Indicators**

    SMA (Simple Moving Average)
    EMA (Exponential Moving Average)
    RSI (Relative Strength Index)
    Bollinger Bands
    MACD (optional)

3. **Streamlit Interface**

    Sidebar controls for ticker, period, and interval
    Checkboxes for indicator selection
    Interactive Plotly charts
    Auto-refresh slider (0–300 seconds)

### Deployment

Streamlit Cloud
Push the repository to GitHub (with requirements.txt).
Log into https://share.streamlit.io.
Connect your GitHub account and select main.py as the entry file.
Deploy and retrieve your public link.


### Author

    V. Pooranan
    Software Engineer | Data and Finance Enthusiast
    GitHub: Pooranan11
