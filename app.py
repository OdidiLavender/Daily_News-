from threading import main_thread
from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def home():
    #enter client id and api_key for authourisation
    newsapi = NewsApiClient(api_key="73488e8c44e24f6bb9ecd72bcac239d8")

    #for top headlines of news,we will code:
    top_headlines = newsapi.get_top_headlines(sources ='bbc-news,the-verge,cnn-news,cbs-news,nbc-news')
    #source is where the news comes from into your appp by api

    #fetech all the articles of top headlines news 
    t_articles =  top_headlines["articles"]

    #making a list of contents to store the values on the list
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    #fetching all the contents of articles by using for loop
    for i in range(len(t_articles)):
        main_article = t_articles[i]

        #appending all the content into each of the lists
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        #making a zip for finfng the contents directly
        contents = zip(news,desc,img,p_date,url)
    #pass it in rendered file
    


        
    return render_template('home.html',contents=contents)

if __name__ == '__main__':
    app.run(debug=True)