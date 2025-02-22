from pandas import DataFrame, Series

#putting a list into a series, biggest difference is that a list can have items with different types whereas a Series can not
obj = Series([-1,2,-3,4,-5])
#Series gets an index / integer name as well as holding the value it has, however it can have different values as the index

#if you want to know if a value is in a series
a_series.isin(1) #this will produce a boolean value

obj.index #will result in RangeIndex

#using indicies lists to get object items
I = [0,2,3]
x = obj[I]
#x will equal a series -1, -3, 4

#indexing via boolean values
I_pos = obj > 0 #this will apply for each element in obj is it greater than 0 and return True / False values
x = obj[I_pos]) #x will be equal to all of the true values
print(obj[I_pos]).index #this will return the index's from the original obj
print(obj([~I_pos]).index #this will return the opposite index's that are false
#this is how the index's and series operate more like a dictionary

obj3 = Seres([1,       -2,    3,       -4,       5,        -6],
             'alice','bob', 'carol', 'dave', ' esther', 'frank'])
#when this is printed the index's will be the names of the people
obj[3] = 'carol'

#converting dictionary to a Series
#imagine obj3 is a dictionary
obj4 = Series(dict)

obj[['alice', 'carol', 'esther']] #this will print out the numbers associated

#is there an index value in a Series
'carol' in obj3 #will return True

#arithmatic
obj3 + 5 #will add 5 to every value
(-2.5 * obj3) + (obj3 + 5) #this will take the value of obj3 and input it at both places and then give the final output

#name the series:
obj3.name = 'peep'



