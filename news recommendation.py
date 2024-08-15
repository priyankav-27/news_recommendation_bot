import streamlit as st
import requests

# Function to fetch news articles for a list of categories
def fetch_news(categories, country='in'):
    api_key = 'b47c7727443a44e3a0a3a1666f7a456d'  # Replace with your NewsAPI key
    url = 'https://newsapi.org/v2/top-headlines'
    all_articles = {}
    
    for category in categories:
        parameters = {
            'country': country,
            'category': category,
            'apiKey': api_key
        }
        response = requests.get(url, params=parameters)
        
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            all_articles[category] = articles
        else:
            st.error(f"Failed to fetch news articles for category {category}: {response.status_code}")
    
    return all_articles

# Function to summarize top headlines
def summarize_headlines(articles, max_lines=10):
    summary = ""
    for article in articles:
        if len(summary.splitlines()) >= max_lines:
            break
        summary += f"{article.get('title', 'No Title')}: {article.get('description', 'No Description')}\n"
    return summary.strip()

# Streamlit app interface
st.title("News Recommendation Bot")

# Multi-select for category selection
categories = st.multiselect(
    "Select news categories:",
    ["General","Business", "Entertainment", "Health", "Science", "Sports", "Technology"],
)

# Button to fetch news
if st.button("Get News"):
    if categories:
        all_articles = fetch_news(categories)
        
        # Display category summaries
        st.subheader("Category Summaries")
        for category in categories:
            articles = all_articles.get(category, [])
            summary = summarize_headlines(articles)
            st.text_area(f"{category.capitalize()} Summary", summary, height=150, max_chars=None, key=category)
        
        st.subheader("Top News from Selected Categories")
        
        if all_articles:
            for category, articles in all_articles.items():
                st.write(f"**{category.capitalize()}**")
                if articles:
                    for i, article in enumerate(articles[:10]):  # Display top 5 articles
                        st.write(f"**{i+1}. {article['title']}**")
                        st.write(f"Source: {article['source']['name']}")
                        st.write(f"[Read more]({article['url']})")
                        st.write("\n")
                else:
                    st.write(f"No articles found for {category}.")
                st.write("\n")
    else:
        st.warning("Please select at least one category.")
