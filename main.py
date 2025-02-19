import streamlit as st
from components import portfolio, news, charts
from services import stock_service, news_service, ai_service

st.set_page_config(
    page_title="AI Financial Advisor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("AI Financial Advisor 📈")
    
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
        portfolio_analysis = ai_service.get_portfolio_insights()
        st.write(portfolio_analysis)
        
        st.subheader("Market Sentiment Analysis")
        sentiment = ai_service.get_market_sentiment()
        st.write(sentiment)

if __name__ == "__main__":
    main()
