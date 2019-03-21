## Twitter Project

In this project i wanted to scrape twitter and build out a league table based on the sentiment of the tweets for each football club.
Each team would still play eachother over the course of the season however the results wouldnt be acted out on the pitch but analysed 
an average sentimaent of that day for the fans using twitter.

#Twitter-scrape.py
To start i want to scrape twitter every day for all 20 football teams and load the data to a file.
In this file i have logged onto the twitter api and scrapped the tweets for each team and loaded into the file.
The callenges were the extract all the text only from the tweets not including the urls and hastagsd ect.
The load myfile.txt consist of the following colums
    1. Tweet number for the team
    2. Date of the tweet
    3. Team name
    4. Polarity of the tweet ( the positive or negative sentiment of the tweet that is -1 to +1)
    5. The tweet itself