##create a function that will remove non-alphabet characters and punctuation
def normalize_string(s):
    assert type (s) is str
    ###
    ### YOUR CODE HERE
    return "".join([text for text in s.lower() if text.isalpha() or text.isspace()])
  -----------------------------------------------------------------------------
##create a function that will take in a string that has not been normalized and output a list of the different words
def get_normalized_words (s):
    assert type(s) is str
    ###
    ### YOUR CODE HERE
    return normalize_string(s).split()
  -----------------------------------------------------------------------------
#create a function that will turn the different words into a list of itemsets
def make_itemsets_unstructured_text(text):
    ###
    ### YOUR CODE HERE
    return [set(words) for words in get_normalized_words(text)]
  -----------------------------------------------------------------------------
##create a function that will return a paircounts dictionary based on an itemset
#This is assuming that the pair_counts is already a default dictionary
from collections import defaultdict
from itertools import combinations

def update_pair_counts (pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict

    ###
    ### YOUR CODE HERE
    #from collections import defaultdict
    #from itertools import combinations

    for (a, b) in combinations(itemset, 2):
        pair_counts[(a, b)] += 1
        pair_counts[(b, a)] += 1
