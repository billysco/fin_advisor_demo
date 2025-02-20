import streamlit as st
from components import portfolio, news, charts
from services.stock_service import StockService
from services.news_service import NewsService
from services.ai_service import AIService

st.set_page_config(
    page_title="AI Financial Advisor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("AI Financial Advisor 📈")

    # Initialize services
    stock_service = StockService()
    ai_service = AIService()

    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select a page",
        ["Portfolio Dashboard", "News Tracker", "AI Insights"]
    )

    if page == "Portfolio Dashboard":
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Portfolio Overview")
            portfolio.display_portfolio_summary()

            st.subheader("Performance Charts")
            charts.plot_portfolio_performance()

        with col2:
            st.subheader("Quick Actions")
            portfolio.display_quick_actions()

            st.subheader("Market Summary")
            portfolio.display_market_summary()

    elif page == "News Tracker":
        news.display_news_dashboard()

    else:  # AI Insights
        st.subheader("AI-Powered Insights")

        # Get sample portfolio data for AI analysis
        sample_portfolio = {
            'holdings': [
                {'symbol': 'AAPL', 'quantity': 10, 'value': 1750.00},
                {'symbol': 'GOOGL', 'quantity': 5, 'value': 3250.00},
                {'symbol': 'MSFT', 'quantity': 8, 'value': 2800.00}
            ],
            'total_value': 7800.00,
            'daily_change': 120.50
        }

        portfolio_analysis = ai_service.get_portfolio_insights(sample_portfolio)
        st.write(portfolio_analysis)

        # Get news for sentiment analysis
        news_service = NewsService()
        market_news = news_service.get_market_news(limit=5)
        sentiment = ai_service.get_market_sentiment(market_news)

        st.subheader("Market Sentiment Analysis")
        st.write(sentiment)

if __name__ == "__main__":
    main()