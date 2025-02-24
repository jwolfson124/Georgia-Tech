##SERIES

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

#DATAFRAME: Creating and getting basic info from
cafes = DataFrame({'name': ['name1', 'name2', 'name3'],
                  'zip' : [30325, 30324, 30233]})
cafes.columns #will result in name, zip both columns are Series!
cafes['zip'] #to reference the column zip
cafes.index #will return the row values start and end point

#choosing specific columns
target_fields = ['zip']
cafes[target_fields] #this will create a dataframe with only those referenced columns

#slicing
cafes[1::2] #this will take every other row

#changing the index
cafes2 = cafes['zip']
cafes2.index = cafes['name']
cafes2.index.name = None #remove the index name
#now the indexs will be the name

#referencing subsets of rows
cafes2.loc[['name1', 'name2']] #this will refernce the names of those shops

#referencing by index location
cafes2.iloc[[1,3]] #this will give the same result but uses the index location instead of the name

#creating new columns
cafes2['rating'] = 4.0 #this will be applied to all of the different rows
cafes2['price'] = '$$'

#using math to create new column values
price_as_ints = cafes2['price'].apply(len) #takes the length of each price or .apply(lambda s: len(s))
cafes2['value'] = cafes2['rating'] / price_as_ints #this will now divide the rating by the lenth of the price

#MULTIPLE WAYS TO SOLVE THIS PROBLEM
#increasing price based on zip codes
cafes3 = cafes2.copy()
is_fancy = cafes3['zip'].isin({30325}) #returns true false values

#one way to make the changes
cafes3.loc[is_fancy, 'price'] += '$' #this is going to use the true and false values to update the table

fancy_shops = cafes4.index[is_fancy]
fancy_markup =  Series(['$'] * len(fancy_shops), index=fancy_shops)

is_fancy * Series(['$'] * len(is_fancy), index = is_fancy.index) #this will give you all of the different indexes and if it is True than it will give you a '$' sign
cafes4['price] += is_fancy.apply(lambda e: e * '$') 

cafes4.apply(lambda x: repr(type(x))) #will return type for the different columns
cafes4.apply(lambda x: print(x), axis=1) #will return type for all rows based on the index

#using apply with a function
def calc_value(row):
  return row['rating'] / len(row['price'])

cafes4['value'] = cafes4.apply(calc_value, axis=1)
#OR
vafes4['value'] = cafes['rating'] / cafes4['price'].apply(len)

#USING CONCAT
is_cheap = cafes4['price'] <= '$$'
cafes_cheap = cafes4[is_cheap]
cafes_pricey = cafes4[~is_cheap]

#recombines the two different dataframes
pd.concat([cafes_cheap, cafes_pricey])

#using indexs
cafes4.index.isin(['brash', '3heart']) #this will return an array of true and false

#reindexing
cafes5 = cafes4.reindex(Index(['3heart', 'starbucks'])) #this will give you a data table with the same values for 3heart however starbucks will only have NaN

cafes4.reset_index(drop=True) #resets the index to integer and then the old index becomes a column, if drop=True then it will drop the old index from becoming a colummn

#accessing rows example
largest_donors = fecmain['amount'].nlargest(7) #this will give you the 7 largest numbers from the pandas dataframe and their index
fecmain.loc[largest_donors.index]

#using groupby
grouped = fecmain.groupby('cand_nm') #this is used to help prepare the data and returns different tables for each of the candidates
grouped['amount'].nlargest(3) #this will then use those "different" tables to show you the largest 3 for each candidate

grouped.apply(lambda x: type(x)) #this will go through each of the candidate names dataframes
grouped.apply(type)

#getting the different groups after groupby
grouped.groups #will show you the different groups available and their index values
grouped.get_group('Obama, Barack') #this will get you the one specific group that you are looking for




