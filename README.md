# News Recommendation Bot

## Overview

The **News Recommendation Bot** is a Python-based application built using Streamlit that provides users with personalized news recommendations. The app fetches real-time news articles from various categories and displays summaries and top headlines based on user selection.

## Features

- **Real-Time News Fetching:** Integrates with NewsAPI to fetch the latest news articles.
- **Category Filtering:** Allows users to select from multiple news categories (e.g., Technology, Health, Business).
- **Top Headlines Summary:** Displays a summary of top headlines for each selected category.
- **User-Friendly Interface:** Utilizes Streamlit to create an interactive and intuitive web interface.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- Requests library
- NewsAPI key (You need to sign up at [NewsAPI](https://newsapi.org/) to get your API key)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/news-recommendation-bot.git
   cd news-recommendation-bot
   ```

2. **Install Required Packages:**

 ```bash
   pip install -r requirements.txt
```
3. **Create a requirements.txt file with the following contents:**
   ```bash
   streamlit
   requests
   ```
4. **Set Up Your NewsAPI Key:**

- Replace your_newsapi_key in the script with your actual API key obtained from NewsAPI.
  
### Running the App
1. ***Navigate to the directory containing your script:**
 ```bash
cd path/to/your/project
```
2. **Run the Streamlit app:**
```bash
streamlit run news recommendation.py
```
3.**Open the provided local URL in your web browser to interact with the app.**

## Usage
- Select Categories: Use the multi-select widget to choose news categories you’re interested in.
- Get News: Click the "Get News" button to fetch and display news articles and summaries.

## Acknowledgements
Streamlit - For the easy-to-use framework for creating web apps.
NewsAPI - For providing the news data.
  



