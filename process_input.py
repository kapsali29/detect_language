from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import operator


def utf8len(snippet):
    """
    Return snippet's size in kbytes
    :param snippet: text
    :return: snippet's size in kb
    """
    return len(snippet.encode('utf-8')) * 0.001


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
    snippet_size = utf8len(snippet)
    if snippet_size > 3.0:
        return "Snippet size must not exceed 3 kilo bytes"
    else:
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
