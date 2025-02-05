import re
#create a pattern object
pattern_obect = re.compile(pattern)
matches = pattern_object.earch(input)

pattern = 'fox'
pattern_matches = re.compile (pattern)

input = 'The quick brown fox jumps over the lazy dog'
matches  = pattern_matcher.seearch(input)

matches.group() 
matches.start() #starting index
matches.end() #ending index
matches.span()
match() - #determine if the RE matches at the beginning of the string
search() - #Scans through a string, looking for any location where this RE matches
findall() - #Find all substrings where the RE matches, and teruns them as a list
finditer() - #find all substrings where the RE matches, and returns them as an iterator


#Searching for inrequently used aptterns
matches_2 = re.search('jump', input)
assert matches_2 is not None
print("Found, matches_2.group(), "@", matches_2.span())

      
