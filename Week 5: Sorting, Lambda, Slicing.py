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

