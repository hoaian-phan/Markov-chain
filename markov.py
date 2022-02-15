"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file():
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(sys.argv[1])
    text_string = file.read()
    file.close()

    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    words = text_string.split()
    # choice_options = [2, 3, 4]
    
    # n = choice(choice_options)
    # for i in range(len(words)-n):
    #     key = (words[i])
    #     while n != 0:
    #         n = choice(choice_options)
    # for i in range(len(words)-n):
    #     key = (words[i])
    #     while n != 0:
    #         #key = (words[i], words[i+1]..... words[i+(n-1)])
    #         key = (key + words[i])
    #         n -= 1
    #     value = words[i+n]
    #     if key in chains:
    #         chains[key].append(value)
    #     else:
    #         chains[key] = [value]key = (words[i], words[i+1]..... words[i+(n-1)])
    #         key = (key + words[i])
    #         n -= 1
    #     value = words[i+n]
    #     if key in chains:
    #         chains[key].append(value)
    #     else:
    #         chains[key] = [value]
    
    for i in range(len(words)-2):
        key = (words[i], words[i+1])
        value = words[i+2]
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = [] # empty output list
    keys = list(chains.keys()) # a list of all the keys (tuples)
    pair_word = choice(keys) # randomly choose a key (tuple)
    words.extend(pair_word)
    
    while pair_word in chains:
        next_word = choice(chains[pair_word]) # pick random word from the list (corresponding value)
        words.append(next_word) # add this word to the output list
        pair_word = (pair_word[1], next_word) # create new key pair to search for the next word in correcp value

    return ' '.join(words)


# input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file()

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
