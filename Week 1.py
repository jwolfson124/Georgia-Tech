Loop Examples:
x = [1,2,3]

#without indexing
for variable in x:
  print(variable)
  
#with indexing
for i in range(len(x)):
  print(x[i])

----------------------------------------------------------------------------------------

Example for cumalitive sum:



----------------------------------------------------------------------------------------
List Manipulation within a list:
x = [1,2,3]
[e**2 for e in x]
#this syntax will create a new list and for each element in x will be squared

----------------------------------------------------------------------------------------
Functions as values THIS NEEDS TO BE RUN TO SEE OUTPUT AND FINISH EXPLANATION

from itertools import accumulate #this function does a cumulative sum

def multiply(a,b):
  return a*b

x=[1,2,3]

list(accumulate(x, func=multiply))
