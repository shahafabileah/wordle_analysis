This project has code to help solve the game Wordle:
https://www.powerlanguage.co.uk/wordle/

There are two files:
1. first_word.py - tells you the best first word to try.
2. solver.py - guides you through a full game, telling you which word to use at every turn.

For this analysis, I'm using a list of 5757 five letter English words taken from here:
https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

# First Word

Usage: `python3 first_word.py`

## TL;DR

If you just want to maximize greens in the first round, use "sores".

If you want to maximize overall hits (greens and yellows) in the first round, use "arose".

## Approach 1: simple histogram

We look at how often each letter (a, b, c...) appears across all 5-letter English words.  Then we assign a score to each word by adding up the frequency of each of its letters.  This is akin to "area under the curve".

If a given word has a popular letter multiple times, it gets credit for that letter multiple times.  So, this may not be the best approach.

Here are the top ranked words from this approach:
```
Find best words by simple letter frequency
(-15117, 'esses')
(-14456, 'asses')
(-14432, 'eases')
(-13994, 'seers')
(-13669, 'seest')
(-13369, 'sense')
(-13338, 'oases')
(-13333, 'arses')
(-13333, 'sears')
(-13309, 'erase')
```

Words that have a higher diversity of letters should probably be scored higher.

# Approach 2: simple histogram, adjusting for letter repetition

This is a variation on Approach 1.  The intuition is that a word like "esses" probably shouldn't be scored so highly.  Sure, the letter 's' is a popular letter, but how many words have 3 s's??  So the adjustment here is to look at how many words have 1 "s", how many have 2 s's, etc.  (Side note: isn't it a fun coincidence that the word that motivates this variation is "esses"?).

This approach seems to yield that greater diversity noted above.

```
Approach 2: Find best words by letter frequency, adjusting for letter repetition
(-10995, 'arose')
(-10851, 'arise')
(-10851, 'raise')
(-10774, 'aster')
(-10774, 'rates')
(-10774, 'stare')
(-10774, 'tares')
(-10774, 'tears')
(-10746, 'earls')
(-10746, 'laser')
```

This is probably the best approach to take to maximize the number of overall hits in the first round, greens and yellows.

# Approach 3: consider letters and positions

We look at how often a given letter appears in a given position.  In other words, how often does 'a' appear in the first position, second position, etc.  Same for 'b', 'c', and so on.

This is probably the best approach for maximizing the number of greens in the first round, which is a kind of greedy algorithm.  It doesn't necessarily optimize for helping you find the ultimate solution in the fewest turns.  Put another way, you may be better sacrificing greens in the first round in order to get additional yellows that point the way to the final solution more quickly.

Nonetheless, here's what you get:
```
Find best words by letter-position frequency
(-5102, 'sores')
(-5034, 'sales')
(-5015, 'soles')
(-4926, 'sates')
(-4864, 'sires')
(-4837, 'cares')
(-4829, 'bares')
(-4818, 'cores')
(-4810, 'bores')
(-4799, 'sines')
```

# Solver

Sample usage:
```
% python3 solver.py                                   
This is an interactive solver for wordle.
In each turn, it suggests a word to try.
It then asks you to indicate how it went.
Use the letters: B = black, Y = yellow, G = green.
For example if you tried AROSE and got black-yellow-black-yellow-green, type BYBYG

Number of remaining words: 5757
Try this word: arose
How did it go? BYBYG
Number of remaining words: 19
Try this word: reuse
How did it go? YBBYG
Number of remaining words: 4
Try this word: prise
How did it go? BYGYG
Number of remaining words: 1
Try this word: shire
How did it go? GGGGG
```

The solver begins with the full list of candidate words.  After each turn, it reduces the list of candidate words by eliminating ones that definitely don't work.  It then suggests the most likely word from the remaining set (using "Approach 2" from above).

This approach works, but it's rather "greedy".  It would be better to test _unique_ letters in subsequent rounds in order to maximize information gain and reduce the remaining search space.

You can also run the script in _evaluation_ mode:
```
% python3 solver.py -e
which 5
there 4
their 8
about 3
would 5
```

This will test every 5-letter word to see how many rounds it would take to reach the correct answer using the same suggested words.  After going through all the words, it prints the average.

Current result:
```
Average: 5.0010422094841065
```

However, there are plenty of words in the mix that take more than the allowed 6 guesses.  So, this is still not a satisfactory solution.

# Related work

Apparently I'm not the first person to wonder what's the best first word to use: https://www.google.com/search?q=best+first+word+to+use+in+wordle

Lots of people offer an answer to this question.  I think this one deserves special credit:
https://bert.org/2021/11/24/the-best-starting-word-in-wordle/
This person looked at the wordle source code and discovered the official list of 5-letter words used in the game.  So, his solution is even more accurate than mine (which relies on a different/standard list of 5-letter words).

Also, some people have created helper tools or complete solvers.  Here are a couple:
* https://notfunatparties.com/wordle-solver
* https://www.thewordfinder.com/wordle-solver/
