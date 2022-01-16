This is an exercise to think through what is the best starter word in the game Wordle:
https://www.powerlanguage.co.uk/wordle/

This analysis is based on a list of 5757 five letter English words taken from here:
https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

So far the code includes two approaches

# Approach 1: simple histogram

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

# Approach 2: consider letters and positions

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
