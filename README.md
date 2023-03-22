# WiBaSets
Basque data for NLP and ML

TXT Data
-----------
Master file (master.txt) includes 5,129,348 Basque tokens extracted from news articles, wikipedia pages, book reviews, and more. Feel free to dowload it, clean it, or add more data to the corpus. 

CSV data
-----------
There are several files for developing sentiment analysis models in Basque. I add a trainning, test, and validation files for such purposes. All utterances are labeled as positive (1), negative (-1), or neutral (0). The root of the dataset was retrieved from BasqueGLUE, which was latter expanded with 1,000 tweets. The dataset has been used for several purposes, including Basque word embeddings.

Code
-----------
I include a Basque rule-based lemmatizer. It is still under development, but it shows good results when dealing with simple utterances. New suffixes can be added to the code if needed.

Stopwords
-----------
For data cleaning purposes, a brief stopword list has been added.
