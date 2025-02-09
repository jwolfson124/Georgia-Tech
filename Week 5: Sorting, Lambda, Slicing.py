SORTING
#list
function: sorted()
sorted(list) #will output a sorted list

#dictionary
data = dictionary
sorted(data, key = get_year, reverse=False)
#this needs to take a function that it will use to sort

def get_year(s):
  return s['year']

#lambda reverse

sorted(data, key = lambda s: s['year']) #lambda is basically a non-function it takes a data and returns something from it to be used inplace of the function

---------------------------------------------
#SLICING
L = [1,2,3,4,5]

#example
L[-3:] = [3,4,5]

#same output
n = len(L)
L[n-3:n]

previous = ''

for c in L:
  if c != previous[-1:]: #this notation will not cause a failure when looping through
    

-------------------------------------------
SAMPLE PROBLEM
#take the length of the longest run and the letter associated
test = {
  'aaaabb' : (a, 4),
  'bbbaaabaaaa' : (a,4),
  'bbbaabbaaa' : b,3),
  '' : ('', 0)
}

#solution 1
#step 1: Initialize the outputs so that an empty string is going to give you the desired output
def longest_consecutive_subsequence(s):
  best, best_count = "",0
  prev, prev_count = "", 0

  #loop through all characters
  for c in s:
    if c == prev:
      prev_count += 1

    else:
      #if the c does not match the previous character
      if prev_count > best_count:
        best = prev
        best_count = prev_count
        
      prev, prevcount = c, 1
    #check again at the end of the entire string to make sure that the last sequence is recorded
  if prev_count > best_count:
      best = prev
      best_count = prev_count
  return best, best_count
#step 2:



