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

list(accumulate(x, func=multiply)) #function does not need to be created. Can use inputs like addition or subtraction etc

##EXAMPLE OF USING THIS FOR STOCK PRICES
prices = [13,11,10,8,5,8,9,6,7,7,10,7,4,3]

#just consider prices up to this point
j = 4
def max_profit_on_day(j, prices)
  sell = prices[j] # this will be the day that you sell
  best_buy = min(prices[:j]) #you can buy anytime before that
  gain = sell - best_buy #this is the profit that you can make
  return max(gain,0) #this will return the higher of either the gain or 0

for j in range(1, len(prices)):
  max_gain = 0
  for j in range(1, len(prices)):
    gain = max_profit_on_day(j, prices)
    max_gain = max(max_gain, gain)
  return max_gain












