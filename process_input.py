from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import operator


def read_snippet(filepath):
    """
    The following function read the files with the data input
    :param filepath: snippet file path
    :return:
    """
    with open(filepath, encoding="utf-8", errors="ignore") as file:
        text = file.read()
        return text


def detect_language(snippet):
    """
    That function counts the german, spanish, english and French stopwords inside the snipet.

    :param snippet: text content
    :return:
    """
    tokenizer = RegexpTokenizer(r'\w+')
    English = set(stopwords.words('english'))
    Spanish = set(stopwords.words('spanish'))
    German = set(stopwords.words('german'))
    French = set(stopwords.words('french'))
    text_unigrams = tokenizer.tokenize(snippet)
    counts = {"French": 0, "English": 0, "German": 0, "Spanish": 0, "Not": 0}
    for word in text_unigrams:
        if word in English:
            counts["English"] += 1
        elif word in Spanish:
            counts["Spanish"] += 1
        elif word in German:
            counts["German"] += 1
        elif word in French:
            counts["French"] += 1
        else:
            continue
    return max(counts.items(), key=operator.itemgetter(1))[0]
