import streamlit as st
import pandas as pd
from services.stock_service import StockService
from utils.data_utils import format_currency, format_percentage, calculate_portfolio_metrics

def display_portfolio_summary():
    """Display portfolio summary section"""
    # Sample portfolio data (in real app, this would come from a database)
    portfolio = {
        'AAPL': 10,
        'GOOGL': 5,
        'MSFT': 8
    }
    
    performance = StockService.get_portfolio_performance(portfolio)
    metrics = calculate_portfolio_metrics(performance)
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Total Value",
            format_currency(metrics['total_value']),
            format_percentage(metrics['daily_return'])
        )
    
    with col2:
        st.metric(
            "YTD Return",
            format_percentage(metrics['ytd_return'])
        )
    
    with col3:
        st.metric(
            "Diversification Score",
            format_percentage(metrics['risk_metrics']['diversification_score'] * 100)
        )
    
    # Display holdings table
    st.subheader("Holdings")
    holdings_df = pd.DataFrame(performance['holdings'])
    st.dataframe(
        holdings_df.style.format({
            'value': lambda x: format_currency(x),
            'daily_change': lambda x: format_currency(x)
        })
    )

def display_quick_actions():
    """Display quick actions section"""
    st.text_input("Add Stock Symbol", placeholder="e.g., AAPL")
    col1, col2 = st.columns(2)
    
    with col1:
        st.number_input("Quantity", min_value=1, value=1)
    
    with col2:
        st.button("Add to Portfolio")
    
    st.button("Rebalance Portfolio")

def display_market_summary():
    """Display market summary section"""
    market_data = StockService.get_market_summary()
    
    for index, data in market_data.items():
        st.metric(
            data['name'],
            format_currency(data['price']),
            format_percentage(data['change'])
        )
