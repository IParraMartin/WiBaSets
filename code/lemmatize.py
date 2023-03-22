import nltk
import pandas as pd


data = pd.read_csv('FILEPATH')


def basque_stemmer(sentence):
    
    suffixes = ['ak', 'ekin', 'arekin', 'gaz', 'ek', 'taz', 
                'tzeko', 'ko', 'az', 'ten', 'ntz','tik', 'rik']
    
    words = nltk.word_tokenize(sentence)

    stemmed_words = []

    for word in words:

        for suffix in suffixes:

            if word.endswith(suffix):

                word = word[:-len(suffix)]

                break

        stemmed_words.append(word)

    stemmed_sentence = ' '.join(stemmed_words)

    return stemmed_sentence


stemmed_data = data['text'].apply(basque_stemmer)
print(stemmed_data.head(10))




