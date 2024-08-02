from string import punctuation
from heapq import nlargest
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# The "percentage" of the original string to retrun
# This amount tested best with the most results to be a straight-to-the-point summary
# May update later to be a dynamic amount so the length is usually set
PERCENT_SUMMARIZE = 0.3

def text_summarize(text):
    print("Summarizing text...")
    # English translation pipeline for the nlp to use
    nlp_model = spacy.load('en_core_web_sm')
    document = nlp_model(text)

    # Dividing the text into tokens for readability 
    tokens = [token.text for token in document]

    # Dict in the formation {word: frequency}
    word_frequencies = {}
    for word in document:
        # If a word is not a stop word or a punctuation mark, find how frequently it occurs
        if word.text.lower() not in STOP_WORDS and word.text not in punctuation:
            word_frequencies[word.text] = word_frequencies.get(word.text, 0) + 1
    
    # Find the maximum frequency of a word
    max_frequency = max(word_frequencies.values())

    # Making each word a fraction of how much it occurs in comparison to the most occurring word
    word_frequencies = {word: freq / max_frequency for word, freq in word_frequencies.items()}
    
    # Same process as before, but with sentences
    sentence_tokens = list(document.sents)
    sentence_frequencies = {}

    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies:
                if sent not in sentence_frequencies:
                    sentence_frequencies[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_frequencies[sent] += word_frequencies[word.text.lower()]
    
    # Finding the length of the target string based on the number of sentences
    select_length = int(len(sentence_tokens) * PERCENT_SUMMARIZE)
    summary = nlargest(select_length, sentence_frequencies, key=sentence_frequencies.get)

    # Adding the most repeating words/sentences into the final summary
    final_summary = ''.join([sent.text for sent in summary])
    return final_summary