# Sentiment-analysis-of-news-articles

## Instructions on how to run the code:

The file ‘Sentiment_Analysis_of_News_Articles.ipynb’ can be downloaded and executed by using Google Colab, since I primarily used Google Colab for this project.
The file ‘sentiment_analysis_of_news_articles.py’ contains the python code of this project and can be executed through any IDE like Visual Studio Code, IDLE, Spyder, etc.

The file ‘requirements.txt’ contains the the external libraries/packages required to run the code.
The file ‘Sentiment_each_News_article’ is the screenshot of the visualization of sentiment analysis of each news article being classified as positive, negative or neutral.
The file ‘Sentiment_results’ is the screenshot of the visualization of number of articles belonging to each sentiment category.
The file ‘results_SentimentAnalysis_using_vader’ contains the screenshot of result obtained using the vaderSentiment library.
The file ‘sentiment.csv’ contains the dataframe that we generated containing the sentence, polarity, subjectivity and sentiment.

### JSON file format
The file ‘news.json’ contains the 10 news articles which are collected by web scraping the given website. The articles are added in an orderly manner in the form of a list to the json file corresponding to the key "News articles”.

## Choice of sentiment analysis approach:

I have primarily made use of TextBlob library to perform sentiment analysis on the news articles. It makes use of a simple API to perform NLP tasks such as sentiment analysis with good accuracy. Using an inbuilt function ‘polarity’ it finds the polarity of sentiment which is a float value between -1 to 1, where the negative values indicate a negative sentiment, positive value indicates a positive sentiment and zero indicates a neutral sentiment. It also finds a subjectivity score, where if the score is higher, the sentence is more subjective, hence less objective and highly opinionated; whereas a low score indicates that the sentence is more fact based.

As an alternative approach, I tried using the VADER library to perform sentiment analysis. This gives scores to indicate the extent or percentage to which a sentence is positive, negative or neutral.

## High level documentation of the code:

The required packages and libraries required to perform web scraping and sentiment analysis are first installed.
I made use of BeautifulSoup to perform web scraping and obtain the news articles from the given website https://www.aljazeera.com/where/mozambique/  The data is preprocessed to obtain only the most recent 10 articles which contain only English text. The tqdm package is been implemented to show progress on the terminal.
Each news article is passed to TextBlob and we obtain the polarity and sentiment scores of them. These values are stored in a list and later made into a data frame with the columns 'Sentence', 'Polarity', ‘Subjectivity', ‘Sentiment’.
Using plotly visualization library, sentiment of each sentence is plotted. 

## Summary of results:
Using TextBlob, 2 of the news articles were classified as positive sentiment, 2 as negative sentiment and 6 of them as neutral sentiment. In the visualization plot, every article sentence and its corresponding polarity score, subjectivity score and overall sentiment category can be seen.

Using VaderSentiment, we can find the extent to which a news article can be classified as positive, negative or neutral. 
For example, 
['At least 70 killed in storm that struck Madagascar, Mozambique and Malawi as authorities scramble to repair damages.', "{'neg': 0.289, 'neu': 0.711, 'pos': 0.0, 'compound': -0.7579}”]
Here the sentence 'At least 70 killed in storm that struck Madagascar, Mozambique and Malawi as authorities scramble to repair damages.’ is classified 28.9% as negative sentiment, 71.1% as neutral sentiment, 0% as positive sentiment. This indicates that the overall sentiment of the news article sentence is neutral. 

But while using TextBlob, the same sentence is directly classified as ‘negative’. 
Logically when we read and understand the meaning of the sentence, we can confirm that the sentence indeed as a negative sentiment.

Hence, TextBlob performed better in this sentiment analysis project.

Total operation time of the code : 98.2 ms
