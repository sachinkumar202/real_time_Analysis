import requests
from textblob import TextBlob
import matplotlib.pyplot as plt

# Function to fetch real-time news using NewsAPI
def fetch_news(api_key, query, language='en', page_size=10):
    url = f'https://newsapi.org/v2/everything?q={query}&language={language}&pageSize={page_size}&apiKey={api_key}'
    response = requests.get(url)
    return response.json()

# Function to analyze the sentiment of the news articles
def analyze_sentiment(articles):
    sentiment_data = {'Positive': 0, 'Neutral': 0, 'Negative': 0}
    for article in articles:
        text = article['title'] + " " + article.get('description', '')
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            sentiment_data['Positive'] += 1
        elif analysis.sentiment.polarity == 0:
            sentiment_data['Neutral'] += 1
        else:
            sentiment_data['Negative'] += 1
    return sentiment_data

# Function to visualize the sentiment analysis
def plot_sentiment(sentiment_data):
    labels = sentiment_data.keys()
    sizes = sentiment_data.values()
    colors = ['green', 'gold', 'red']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Sentiment Analysis of News Articles')
    plt.show()

# Main function
def main():
    api_key = 'ab3cf51728974c2a871576a9c99cd252'  # Replace with your NewsAPI key
    query = input("Enter the topic you want to search news for: ")
    
    # Fetch news articles
    news_data = fetch_news(api_key, query)
    
    if news_data['status'] == 'ok':
        articles = news_data['articles']
        print(f"Fetched {len(articles)} articles about {query}.")

        # Analyze sentiment
        sentiment_data = analyze_sentiment(articles)
        
        # Display results
        print(f"Sentiment Data: {sentiment_data}")

        # Visualize sentiment analysis
        plot_sentiment(sentiment_data)
    else:
        print("Failed to fetch news articles. Please check your API key or query.")

if __name__ == '__main__':
    main()
