# tokenizer.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

class Tokenizer:
    def __init__(self):
        self.stemmer = PorterStemmer()
    
    def tokenize(self, text):
        tokens = word_tokenize(text)
        token_stream = []
        for token in tokens:
            stemmed_token = self.stemmer.stem(token.lower())
            token_stream.append(stemmed_token)
        return token_stream
