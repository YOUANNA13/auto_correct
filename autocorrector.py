from textblob import TextBlob
from transformers import pipeline
import nltk
nltk.download('punkt')

class AutoCorrector:
    def __init__(self):
        self.context_model = pipeline('fill-mask', model='bert-base-uncased')

    def basic_correct(self, text):
        return str(TextBlob(text).correct())

    def context_correct(self, text):
        words = nltk.word_tokenize(text)
        corrected_text = text
        for i, word in enumerate(words):
            masked = words.copy()
            masked[i] = '[MASK]'
            sentence = ' '.join(masked)
            predictions = self.context_model(sentence)
            top_prediction = predictions[0]['sequence'].replace('[CLS]', '').replace('[SEP]', '').strip()
            corrected_text = top_prediction
        return corrected_text
