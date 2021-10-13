import numpy as np
import pandas as pd
import re
import warnings
from pandas import DataFrame
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv


directory = "<SET YOUR WORKING DIRECTORY HERE>"
save_file = open('fuzzy_match_results.csv', 'w')
writer = csv.writer(save_file, lineterminator='\n')


def parse_csv(path):
    with open(path, 'r', encoding="ANSI") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            yield row


if __name__ == "__main__":
    # Create lookup dictionary by parsing the string csv
    data = {}
    # TAILOR BELOW PER YOUR FILE NAMES
    for row in parse_csv(directory + 'string_file1.csv'):
        data[row[0]] = row[0]

    # For each row in the lookup compute the partial ratio
    # TAILOR BELOW PER YOUR FILE NAMES
    for row in parse_csv(directory + 'string_file2.csv'):
        letters_only = re.sub("[^a-zA-Z]", " ",  str(row))
        # Use different matching techniques by changing scorer value to fuzz.token_set_ratio, fuzz.partial_ratio, or fuzz.ratio per your need:
        for found, score, matchrow in process.extract(letters_only, data, scorer=fuzz.token_sort_ratio, limit=1):
            if score == 100:
                Digi_Results = [row[0], score, found]
                writer.writerow(Digi_Results)
    save_file.close()
