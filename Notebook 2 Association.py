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

  -----------------------------------------------------------------------------
#create a function that will update itemcounts based on itemsets that are put into a code
def update_item_counts(item_counts, itemset):
    ###
    ### YOUR CODE HERE
    for letter in itemset:
        item_counts[letter] += 1

    return item_counts

  -----------------------------------------------------------------------------
#write a code that is going to take in a group of pairs and the amount of times they appear and then divide them by the times that specific item has appeared
#this will return a set of "rules" which will be used to help identify how often item sets appear together
def create_rules_from_counts(pair_counts, item_counts):
    rules = {} # (item_a, item_b) -> conf (item_a => item_b)
    ###
    ### YOUR CODE HERE
    for (a, b) in pair_counts:
        rules[(a, b)] = pair_counts[(a,b)] / item_counts[a]
    return rules

-----------------------------------------------------------------------------
#create a code that will output a certain set of rules
def filter_rules_by_conf(rules, threshold):
    ###
    ### YOUR CODE HERE

    rules_output = {}

    for rule in rules:
        if rules[rule] >= threshold:
            rules_output[rule] = rules[rule]

    return rules_output
-----------------------------------------------------------------------------
# This takes in a csv input and turns it into a list of sets. These sets need to be split by row because there are multiple which is what row.splits does
#milk,eggs,peanut butter,oatmeal\nbutter,pancake mix,maple syrup\ndog treats,milk,milk'
def make_itemsets_csv(csv_str):
    ###
    ### YOUR CODE HERE
    #csv_str = demo_csv_str_ex8
    csv = csv_str.split("\n")
    x = [set(row.split(",")) for row in csv]
    return x
-----------------------------------------------------------------------------
#using this function we will take a source, whether CSV or string and use all of the functions previously created to create a set of rules.
def create_rules_from_source(source, itemset_maker, conf_threshold=0, min_count=0):
    ###
    ### YOUR CODE HERE

    #this part of the function will take in the function to format the specific text that we are looking for and 
    #organize it into a list of sets
    x = itemset_maker(source)

    #here we create a defaultdict to put into our function
    pair_counts = defaultdict(int)

    #for each line we update the pair counts as in how often a pair is found together
    for line in x:
        update_pair_counts(pair_counts, line)

    #here we create the item counts this will check how many times an item appears
    item_counts = defaultdict(int)

    #this loop fills in the default dictionary so we know how many times each item appears
    for line in x:
        update_item_counts(item_counts, line)

    #uses the create_rules_from_counts to create our ruleset
    rules = create_rules_from_counts(pair_counts, item_counts)

    #using the confidence threshold we take in the rules and filter them
    threshold_rules = filter_rules_by_conf(rules, conf_threshold)

    #this final rules dictionary will be used for those that meet the min count filter
    final_rules = {}

    for (a, b) in threshold_rules:

        if item_counts[a] >= min_count:
            final_rules[(a,b)] = threshold_rules[(a,b)]

    return final_rules
-----------------------------------------------------------------------------
#Create a function to check and see of two sources what rules are the same
def common_rules(source_0, source_1, itemset_maker, conf_threshold, min_count):
    ###
    ### YOUR CODE HERE
    first_rules = create_rules_from_source(source_0, itemset_maker, conf_threshold, min_count)

    second_rules = create_rules_from_source(source_1, itemset_maker, conf_threshold, min_count)

    common_rules = []

    for rule in first_rules:

        if rule in second_rules:

            common_rules.append(rule)

    return set(common_rules)
