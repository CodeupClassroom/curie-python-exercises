# IPython log file


# a five letter word where the alphabetical value of the last 4 characters == the alphabetical value of the first character
# several pieces here:
# - how do we find the alphabetical value of a letter?
# - we only need 5 letter words
# - to be a "match" alpha_value(word[0]) = sum(the rest of the letters)
# Plan
# filter the list down to only 5 letter words
# define a function to find the alphabetical value of a character
# create a function to see if a word is a "match"
# loop through all the words and use the function defined above
import pandas as pd
with open('/usr/share/dict/words') as f:
    words = f.read().split()
    
words[:10]
pd.Series(words)
pd.DataFrame({'word': words})
df = pd.DataFrame({'word': words})
df.word
df.word.apply(len)
df['word_length'] = df.word.apply(len)
df
five_letter_words = df[df.word_length == 5]
five_letter_words
def alphabetical_value(ch: str) -> int:
    '''
    a -> 1
    b -> 2
    ...
    z -> 26
    '''
    return 'abcdefghijklmnopqrstuvwxyz'.index(ch.lower()) + 1
    
assert alphabetical_value('a') == 1
assert alphabetical_value('b') == 2
assert alphabetical_value('z') == 26
assert alphabetical_value('z') == 266
def test_word(word: str) -> bool:
    '''
    returns True if the alphabetical value of the first letter
    is the same as the sum of the alphabet values of the last
    four letters
    '''
    first_letter, *last_four = word
    return False
    
first, second = 'ab'
first
second
first, second = 'abc'
first, second, *rest = Codeup
first, second, *rest = 'Codeup'
first
second
rest
def test_word(word: str) -> bool:
    '''
    returns True if the alphabetical value of the first letter
    is the same as the sum of the alphabet values of the last
    four letters
    '''
    first_letter, *last_four = word
    return alphabetical_value(first_letter) == sum([alphabetical_value(ch) for ch in last_four])
    
    
test_word('chair')
test_word('zebra')
test_word('table')
five_letter_words.apply(test_word)
five_letter_words
five_letter_words.word.apply(test_word)
five_letter_words[five_letter_words.word.apply(test_word)]
five_letter_words[five_letter_words.word.apply(test_word)]
[word for word in words if len(word) == 5 and test_word(word)]
def test_word(word: str) -> bool:
    '''
    returns True if the alphabetical value of the first letter
    is the same as the sum of the alphabet values of the last
    four letters
    '''
    first_letter, *last_four = word
    return alphabetical_value(first_letter) == sum([alphabetical_value(ch) for ch in last_four])
    
    
def alphabetical_value(ch: str) -> int:
    '''
    a -> 1
    b -> 2
    ...
    z -> 26
    '''
    return 'abcdefghijklmnopqrstuvwxyz'.index(ch.lower()) + 1
    
[word for word in words if len(word) == 5 and test_word(word)]
