Function: Assert
Defintion: Will tell you if a line of code passes a certain logical test
Example:
x_float = 1
assert x_float == 1
assert x_float < 0
#The second will create an assertionerror because that specific line is not true
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Function: Pop
Definition: Will remove the first element from a list
Example:
x = [0,1]
x.pop()
## x will now equal [0]
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Function: copy.deepcopy(*insert item here*)
Definition: Copies over the variable with all of the nested structures in place
x = [1,[2,3]]
bad_copy = x.copy()
good_copy = copy.deepcopy(x)
#the deep copy will keep the index 1 nested properly
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Function: object.reverse()
Definition: This will reverse a list that you have
x = [1,2,3]
x.reverse()
x = [3,2,1]
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Function: int(item, base)
Definition: this will turn a string into a number or multiply the numbers by the base and their place in the number
item = "11010"
base = 10
item = (1 * (10**5)) + (1 * (10**4)) etc
