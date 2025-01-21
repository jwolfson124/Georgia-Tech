#create a function that removes any non-alphabetic characters
def normalize_strings(s):
  return "".join[c for c in s.lower() if c.isalpha() or c.isspace()]
-------------------------------------------------------------------------------------
#given a string return a list of its words
def get_normalized_words(s):
  return normalize_string(s).split()
-------------------------------------------------------------------------------------
#given a list of strings convert the characters of each string to an itemset
def make_itemsets(words):
  return [set(w) for w in words]
-------------------------------------------------------------------------------------
#implement a function that enumerates all item-pairs within an itemset and updates a table in-place that tracks the count of those item pairs
def update_pair_counts (pair_counts, itemset):
  

-------------------------------------------------------------------------------------
#creating a filter rules by confidence
def filter_rules_by_conf(pair_counts, item_counts, threshold):
  rules = {}
  for (a, b) in pair_counts:
    assert a in item_counts #checks to make sure that a is in the item counts
    conf_ab = pair_counts[(a, b)] / item_counts[a]
    if conf_ab >= threshold:
      rules[(a, b)] = conf_ab
  return rules
  #this function will be used in the next function
-------------------------------------------------------------------------------------
def find_assoc_rules(receipts, threshold):
  pair_counts = defaultdict(int)
  item_counts = defaultdict(int)
  for itemset in receipts:
    update_pair_counts(pair_counts, itemset)
    update_item_counts(item_counts, itemset)
  rules = filter_rules_by_conf(pair_counts, item_counts, threshold)
  return rules
