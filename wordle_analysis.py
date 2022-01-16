from collections import defaultdict
from queue import PriorityQueue

def get_five_letter_words():
  filename = "five_letter_words.txt"
  with open(filename) as f:
    words = f.read().splitlines()  
  return words

# in: words, a list of all 5-letter words in English
# out: a dictionary mapping from each letter (a, b, c) to the number of times that letter appears across all words
def letter_histogram(words):
  histogram = defaultdict(int)

  for word in words:
    for letter in word:
      histogram[letter] += 1
    
  return histogram

def score_word_by_letter_frequency(word, histogram):
  score = 0
  for letter in word:
    score += histogram[letter]
  # Multiply score by -1 so that higher frequencies come first in PriorityQueue
  return score * -1

def rank_words_by_letter_frequency(words, histogram):
  ranked_words = PriorityQueue()
  for word in words:
    score = score_word_by_letter_frequency(word, histogram)
    ranked_words.put((score, word))
  return ranked_words

def find_best_words_by_letter_frequency():
  words = get_five_letter_words()
  histogram = letter_histogram(words)
  ranked_words = rank_words_by_letter_frequency(words, histogram)
  return ranked_words

def letter_position_histogram(words):
  histogram = defaultdict(int)

  for word in words:
    for (index, letter) in enumerate(word):
      histogram[(index, letter)] += 1
    
  return histogram

def score_word_by_letter_position_frequency(word, histogram):
  score = 0
  for (index, letter) in enumerate(word):
    score += histogram[(index, letter)]
  # Multiply score by -1 so that higher frequencies come first in PriorityQueue
  return score * -1

def rank_words_by_letter_position_frequency(words, histogram):
  ranked_words = PriorityQueue()
  for word in words:
    score = score_word_by_letter_position_frequency(word, histogram)
    ranked_words.put((score, word))
  return ranked_words

def find_best_words_by_letter_position_frequency():
  words = get_five_letter_words()
  histogram = letter_position_histogram(words)
  ranked_words = rank_words_by_letter_position_frequency(words, histogram)
  return ranked_words

def main():
    print('Find best words by simple letter frequency')
    ranked_words = find_best_words_by_letter_frequency()
    for i in range(0,10):
      print(ranked_words.get())

    print('Find best words by letter-position frequency')
    ranked_words = find_best_words_by_letter_position_frequency()
    for i in range(0,10):
      print(ranked_words.get())

if __name__ == "__main__":
    main()
