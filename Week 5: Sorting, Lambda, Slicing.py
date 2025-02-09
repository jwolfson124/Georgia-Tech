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

#solution 2
s = 'bbbaaabaaaa'
#location = [s[0:3], s[3:6], s[6:7], s[7:11]]
#max(location, key = len)

def zip_neighbors(s):
  return list(zip(s[:-1], s[1:]))

#will output [(b,b), (b,b), (b,a)...]

list(enumerate(zip_neighbors(s)))
#will return [(0, (b,b)), (1, (b,b)), (2, (b,a))...]

c = [0] + [position+1 for position, (left, right) in list(enumerate(zip_neighbors(s))) if left != right] 
#this will give you the different indexs where the left does not match the right

splits = [s[i:j] for i, j in zip_neighbors(c)] #returns a list of the indiciese
max(splits, key=len) #returns the largest length found in splits

