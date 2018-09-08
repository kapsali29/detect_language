import os
from os import listdir

from os.path import isfile, join

from process_input import read_snippet, detect_language

data_dir = "/input"
inputs = [f for f in listdir(os.getcwd() + data_dir) if isfile(join(os.getcwd() + data_dir, f))]
for file in inputs:
    snippet = read_snippet("input/" + file)
    estimated_language = detect_language(snippet)
    print(estimated_language)
