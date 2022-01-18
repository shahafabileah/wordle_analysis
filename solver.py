from collections import defaultdict
from queue import PriorityQueue

def get_five_letter_words():
  filename = "five_letter_words.txt"
  with open(filename) as f:
    words = f.read().splitlines()  
  return words

def letter_frequency_histogram(words):
  # This histogram has entries like
  #   ('a', 1) => the number words that have at least 1 a
  #   ('a', 2) => the number of words that have at least 2 a's
  histogram = defaultdict(int)

  for word in words:
    # This histogram is a simple tally of the number of times each letter appears in the word.
    # For the word 'esses':
    #   'e' => 2
    #   's' => 3
    word_histogram = defaultdict(int)
    for letter in word:
      word_histogram[letter] += 1
      count_so_far = word_histogram[letter]
      histogram[(letter, count_so_far)] += 1

  return histogram

def score_word_by_letter_in_word_frequency(word, histogram):
  score = 0
    # Kind of redundant - once again keeping track of the histogram per word
  word_histogram = defaultdict(int)
  for letter in word:
    word_histogram[letter] += 1
    count_so_far = word_histogram[letter]
    score += histogram[(letter, count_so_far)]
  # Multiply score by -1 so that higher frequencies come first in PriorityQueue
  return score * -1

def rank_words_by_letter_in_word_frequency(words, histogram):
  ranked_words = PriorityQueue()
  for word in words:
    score = score_word_by_letter_in_word_frequency(word, histogram)
    ranked_words.put((score, word))
  return ranked_words

def pick_next_word_to_try(remaining_words):
  histogram = letter_frequency_histogram(remaining_words)
  ranked_words = rank_words_by_letter_in_word_frequency(remaining_words, histogram)
  top_word = ranked_words.get()
  return top_word[1]

def word_matches(word, attempted_word, colors):
  # The logic is tricky in cases when the attempted word has a certain letter multiple times.
  #
  #   Example:
  #     REUSE
  #     YBBYG
  # Note that 'E' is black in the second position and green in the last position.
  #
  # To account for this, we use the following approach:
  # 1. Process the greens.  If the candidate_word matches, convert that position to '0' to
  #    indicate that this position was used.
  # 2. Process the yellows.  Again, whenever you match the letter, convert that position to
  #    '0' to indicate that this position was used.
  # 3. Process the blacks.  At this point if the given letter appears anywhere else in the
  #    word, it's safe to eliminate it.

  # Changing to a list allows us to update characters as we go.
  candidate_word = list(word)

  # Greens
  for i in range(0, 5):
    if colors[i] == 'G':
      # The candidate word must have the given letter in this position
      if candidate_word[i] != attempted_word[i]:
        return False

      candidate_word[i] = '0'

  # Yellows
  for i in range(0, 5):
    if colors[i] == 'Y':
      # The candidate word must have the given letter somewhere
      letter = attempted_word[i]
      position = candidate_word.index(letter) if letter in candidate_word else -1
      if position == -1:
        return False
      
      candidate_word[position] = '0'

  # Blacks
  for i in range(0, 5):
    if colors[i] == 'B':
      # The candidate word must not have the given letter anywhere
      if attempted_word[i] in candidate_word:
        return False
  
  return True

def filter_words(old_remaining_words, attempted_word, colors):
  new_remaining_words = []
  for word in old_remaining_words:
    if word == 'shire':
      print("shire: " + str(word_matches(word, attempted_word, colors)))

    if word_matches(word, attempted_word, colors):
      new_remaining_words.append(word)
  return new_remaining_words

def interactive_mode():
  print("This is an interactive solver for wordle.")
  print("In each turn, it gives you which word to try.")
  print("It then asks you to indicate how it went.")
  print("Use the letters: B = black, Y = yellow, G = green.")
  print("For example if you tried AROSE and got black-yellow-black-yellow-green, type BYBYG")
  print("")

  remaining_words = get_five_letter_words()

  while len(remaining_words) > 0:
    print("Number of remaining words: " + str(len(remaining_words)))
    next_word_to_try = pick_next_word_to_try(remaining_words)
    print("Try this word: " + next_word_to_try)
    colors = input("How did it go? ")

    if colors == "GGGGG":
      break

    remaining_words = filter_words(remaining_words, next_word_to_try, colors)

def main():
  interactive_mode()

if __name__ == "__main__":
    main()
