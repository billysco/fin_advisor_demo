from newsapi import NewsApiClient
import os

class NewsService:
    def __init__(self):
        self.api = NewsApiClient(api_key=os.environ.get('NEWS_API_KEY'))
        
    def get_stock_news(self, symbol: str, limit: int = 5) -> list:
        """Get news articles for a specific stock"""
        try:
            news = self.api.get_everything(
                q=symbol,
                language='en',
                sort_by='publishedAt',
                page_size=limit
            )
            return news.get('articles', [])
        except Exception as e:
            raise Exception(f"Failed to fetch news for {symbol}: {e}")
    
    def get_market_news(self, limit: int = 10) -> list:
        """Get general market news"""
        try:
            news = self.api.get_top_headlines(
                category='business',
                language='en',
                country='us',
                page_size=limit
            )
            return news.get('articles', [])
        except Exception as e:
            raise Exception(f"Failed to fetch market news: {e}")
    
    def search_news(self, query: str, limit: int = 10) -> list:
        """Search news articles by query"""
        try:
            news = self.api.get_everything(
                q=query,
                language='en',
                sort_by='relevancy',
                page_size=limit
            )
            return news.get('articles', [])
        except Exception as e:
            raise Exception(f"Failed to search news: {e}")
