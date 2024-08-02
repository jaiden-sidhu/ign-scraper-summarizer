# IGN Verdict Scraper + Summarizer + Sentiment Analysis
This project utilizes the IGN website's built-in game search function to web-scrape the verdict of a given game using a search term. The program then uses an NLP model to summarize the verdict into a summary 20% of the original size. The code then uses a sentiment analysis algorithm to "score" the verdict as "Positive", "Negative", "Conflicted", or "Neutral".

## How It's Made:

**Languages used:** Python.
**Packages used:** SpaCy, Selenium, Requests, BeautifulSoup.

The navigator code uses Selenium to manually navigate the page as if a user was using it. The "Verdict" section of the review is then scraped using Requests and BeautifulSoup. Finally, the summarizer method uses SpaCy's "en_core_web_sm" NLP model to shorted the summary to a given percent of the original verdict's length.

## How To Run:

Run the main.py file. If any errors are given, the Python classes have comments that list the errors and what to fix to make sure it runs correctly. When the main.py file is run, the terminal should give you an input to put in a search term. 

NOTE: Some errors may appear that look similar to "[0801/232145.815:ERROR:socket_manager.cc(141)]". You do not have to worry about these errors, they are minor errors in the loading of the page (due to adblocks, location services, etc.) Any errors that should be noted will terminate the Python code.

NOTE: Some videogames may not have reviews as they are not listed/reviewed on the IGN website. This code's function is to display webscraping/NLP/sentiment analysis algorithms, not provide an in-depth database of game reviews

## Things To Do:

- Develop into a webapp that can be displayed onto a website (an early but not functional version of the HTML/CSS/JS code is in this repository)
- Make the length of the sumamry set within an acceptable range rather than targeting a percent length of the original verdict
- Use a more expansive database of game reviews/multiple reviewer sources to enhance the summarization

## Lessons Learned:

- Selenium Chrome Driver navigation and how to run a test build of Google Chrome
- How to webscrape a page based on a given HTML location and how to return it
- How to use NLPs to summarize a given text input
- Sentiment analysis algorithms
