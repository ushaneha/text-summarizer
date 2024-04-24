import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize_text(text, select_length=2):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    
    # Tokenize the text
    doc = nlp(text)
    
    # Remove stopwords and punctuation, and count word frequencies
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_frequencies:
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
    
    # Normalize word frequencies
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / max_frequency
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in doc.sents:
        for word in sentence:
            if word.text.lower() in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sentence] += word_frequencies[word.text.lower()]
    
    # Select top sentences based on scores
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    
    # Convert selected sentences to text
    summarized_text = ' '.join([str(sentence) for sentence in summary])
    
    return summarized_text
