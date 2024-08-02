from ign_navigator import *
from web_scraper import *
from text_summarizer import *

# Creating two arrays of positive and negative words
pos_words = open('sentiment_words/positive.txt').read().split('\n')
neg_words = open('sentiment_words/negative.txt').read().split('\n')

# Ensuring the files opened correctly
# Uncomment and run these files. If there is an error, ensure the .txt files have been downloaded correctly
# print(pos_words[:5], pos_words[-5:])
# print(neg_words[:5], neg_words[-5:])

# Defining the cutoffs for positive and negative sentiment
# The CONFLICTED_COUNT variable defines, if the net sentiment falls between the cutoffs...
# The fraction of "sentiment" words to total words for it to count as conflicted
POSITIVE_CUTOFF = 3
NEGATIVE_CUTOFF = -3
CONFLICTED_RATIO = 0.25

def main(search_term):
    ign_url = "https://ign.com"

    verdict = perform_search(ign_url, search_term)

    # if verdict is not None:
    #     print("IGN Verdict: ", verdict)
    #     print("Summarization: ", text_summarize(verdict))

    if verdict is None:
        print("No verdict is available for this game.")
        quit()

    num_positive = 0
    num_negative = 0

    for word in verdict.split(' '):
        if word.lower() in pos_words:
            num_positive += 1
        if word.lower() in neg_words:
            num_negative += 1

    # print("Number of Positive Terms: ", num_positive)
    # print("Number of Negative Terms: ", num_negative)
    # print("Sentiment Ratio: ", ((num_positive + num_negative) / (1.0 * len(verdict.split(' ')))))

    if (num_positive - num_negative) >= POSITIVE_CUTOFF:
        sentiment = 'Positive'
    elif (num_positive - num_negative) <= NEGATIVE_CUTOFF:
        sentiment = 'Negative'
    elif ((num_positive + num_negative) / (1.0 * len(verdict.split(' ')))) >= CONFLICTED_RATIO:
        sentiment = 'Conflicted'
    else:
        sentiment = 'Neutral'

    print(f'Summary: {text_summarize(verdict)}\nSentiment Score: {num_positive - num_negative} ({sentiment})')

search_term = input("Enter your search term: ")
main(search_term)