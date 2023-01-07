
import requests
from bs4 import BeautifulSoup
from keyboard import DISTANCES, Keyboard

def scrape_wikipedia_frequency_list(url, dataset_length):
    words_and_frequencies = [([],0)] * dataset_length # pre-allocate memory

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    main_text = soup.find_all("div", attrs={"id": "mw-content-text"})[0]
    table = main_text.find_all("tbody")[0]

    entries = table.find_all("tr")[1:] # skip the heading of the table
    for i, entry in enumerate(entries):
        word = entry.find("a").text.strip().split(" ")[0].lower()
        word = word.replace("'","") # remove apostrophes, not relevant to swipe typing
        word = list(map(lambda x: ord(x) - 97, list(word)))

        tds = entry.find_all("td")[::-1]
        freq = None

        for td in tds:
            try:
                freq = int(td.text.split(" ")[0])
                break
            except ValueError as e:
                continue

        if freq is None:
            print("error parsing frequencies")
            return None

        words_and_frequencies[i] = (word, freq)

    return words_and_frequencies

def score(keyboard, word):
    total = 0
    for letter1, letter2 in zip(word[:-1], word[1:]):
        total += DISTANCES[keyboard.pos(letter1)][keyboard.pos(letter2)]
    return total

class FitnessFn:
    """
    lower fitness is better
    """

    def __init__(self, words_and_frequencies):
        def f(keyboard):
            total = 0
            for (word, frequency) in words_and_frequencies:
                total += score(keyboard, word) * frequency
            return total
        self.fn = f

    def __call__(self, keyboard):
        return self.fn(keyboard)