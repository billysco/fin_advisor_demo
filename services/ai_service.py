import os
from openai import OpenAI
import json

class AIService:
    def __init__(self):
        # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model = "gpt-4o"
    
    def get_portfolio_insights(self, portfolio_data: dict) -> dict:
        """Generate AI insights for portfolio"""
        try:
            prompt = f"""Analyze this portfolio data and provide insights:
            {json.dumps(portfolio_data)}
            
            Provide analysis in JSON format with the following structure:
            {
                "summary": "overall portfolio assessment",
                "risks": ["list of potential risks"],
                "opportunities": ["list of potential opportunities"],
                "recommendations": ["list of actionable recommendations"]
            }
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            raise Exception(f"Failed to generate portfolio insights: {e}")
    
    def get_market_sentiment(self, news_articles: list) -> dict:
        """Analyze market sentiment from news"""
        try:
            prompt = f"""Analyze these news articles and provide market sentiment:
            {json.dumps(news_articles)}
            
            Provide analysis in JSON format with the following structure:
            {
                "overall_sentiment": "bullish/bearish/neutral",
                "confidence": 0.0-1.0,
                "key_factors": ["list of key factors"],
                "market_outlook": "brief outlook description"
            }
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            raise Exception(f"Failed to analyze market sentiment: {e}")
