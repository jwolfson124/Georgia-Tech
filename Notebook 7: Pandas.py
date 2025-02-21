#this notebook will show examples of how to use stuff in pandas
#INDEXING THROUGH A SERIES
index = [0,2,3]
object[index]
#this will return the objects at those indexs
#CREATING A VARIABLE FROM A SERIES
is_positive = object > 0
#IF YOU WERE TO PRINT THIS THE OUTPUT WOULD BE THE INDEX ASSOCAITED WITH EACH ITEM AND TRUE OR FALSE
#INDEXING WITH DATAFRAMES
from pandas import Index
cafes4.index #will show you all the indexs
cafes4.index.isin(['brash', '3heart']) #will return true or false depending on if they are in or not
cafes4.index.union(['chattahoochee']) # this will add chattahoochee to the indexs but it will not show up on the dataframe

#this will change the indexs of cafes4 and any index that was not originally in will have all values of NaN
cafes5 = cafes4.reindex(Index(['3heart', 'east pole', 'brash', 'starbucks']))

display(cafes4)
display(cafes5)

#if you want to go back all you have to do is reset the index
cafes6 = cafes4.reset_index(drop=True)
cafes6['name'] = cafes4.index
cafes6


#TURNING A SERIES INTO A DICTIONARY
obj3 = Series([      1,    -2,       3,     -4,        5,      -6],
              ['alice', 'bob', 'carol', 'dave', 'esther', 'frank'])
obj3['bob'] #would produce -2

#turning a series into a dictionary
peeps = {'alice': 1, 'carol': 3, 'esther': 5, 'bob': -2, 'dave': -4, 'frank': -6}
obj4 = Series(peeps)

#PLAYING AROUND WITH INDEX AND THEIR VALUES
mujeres = [0, 2, 4] # list of integer offsets
print("* las mujeres of `obj3` at offsets {}:\n{}\n".format(mujeres, obj3[mujeres]))
#this will print the objects and their associated number

hombres = ['bob', 'dave', 'frank'] # list of index values
print("* hombres, by their names, {}:\n{}".format(hombres, obj3[hombres]))
#this will print the object and their associated value

#using the in operator
print('carol' in obj3)
#will return true

#VECTOR MATH
print(obj3, "\n")
print(obj3 + 5, "\n")
print(obj3 + 5 > 0, "\n")
print((-2.5 * obj3) + (obj3 + 5))
#this will do all of this to each item. For the second line every item would have 5 added to it

obj_l = obj3[mujeres]
obj_l + obj3
#this will work somewhat similar to a realtional database. Because obj_l does not have all of the keys when they are added together all items that do have a matching key will 
#be added and the rest will come through as NaN

#applying python functions
obj3.apply(abs)
#this will apply the absolute figure to all items in the Series

#naming series
obj3.name = "peep"
obj3
#when this is printed at the bottom you will see peep

#DATAFRAMES
cafes = DataFrame({'name': ['east pole', 'chrome yellow', 'brash', 'taproom', '3heart', 'spiller park pcm', 'refuge', 'toptime'],
                   'zip': [30324, 30312, 30318, 30317, 30306, 30308, 30303, 30318],
                   'poc': ['jared', 'kelly', 'matt', 'jonathan', 'nhan', 'dale', 'kitti', 'nolan']})
print("type:", type(cafes))
print(cafes)
#this will print as a table with name, zip, and poc being the column names and the index 0 will be the first row
display(cafes)
#this will print out a table structure that is easier to read
cafes.columns
#this will print out a list of the different columns
type(cafes['zip']) 
#this will print out a series meaning that each column is actually a named series
cafes.index #this will output the start and stop of the indexs
cafes.index == cafes['zip'].index #this will print out all Trues because they all have the same index

#limiting the dataframe
target_fields = ['zip', 'poc']
cafes[target_fields]
#this line of code will go through and take only the target fields that have those column names
#SLICING
cafes[1::2]
#this will apply to the different rows, not columns, and will take every other row until the end
#CHANGING THE INDEX
cafes2 = cafes[['poc', 'zip']]
cafes2.index = cafes['name']
cafes2.index.name = None #removes name from above the index column
cafes2
#now whatever was in the name column will now be the index
cafes2.loc[['chrome yellow', '3heart']]
cafes2.iloc[[1, 3]]
#now you can use the names of these indexs to pull in rows from cafes2
#adding columns
cafes2['rating'] = 4.0
cafes2['price'] = '$$'
cafes2
#there will now be a rating and price category all of which will have the values shown
#vector math on the columns
prices_as_ints = cafes2['price'].apply(lambda s: len(s))
prices_as_ints #turns the price as ints by looking at how long each row in the price column is
cafes2['value'] = cafes2['rating'] / prices_as_ints
cafes2
#this now adds a new column value and sets that equal to the rating / the len of the price_as_ints
#changing specific columns
cafes3 = cafes2.copy()
cafes3
is_fancy = cafes3['zip'].isin({30306, 30308})
# Alternative:
#is_fancy = cafes3['zip'].apply(lambda z: z in {30306, 30308})
is_fancy

cafes3.loc[is_fancy, 'price'] += '$'
cafes3 #this will now return only cafes that are in zipcodes listed above

#this is another way to go about changing the prices based on the indexs
cafes4 = cafes2.copy()
cafes4['price'] += Series([x * '$' for x in is_fancy.tolist()], index=is_fancy.index)
cafes4

#using concatentation
# Split based on price
is_cheap = cafes4['price'] <= '$$' #split based on the price
cafes_cheap = cafes4[is_cheap]
cafes_pricey = cafes4[~is_cheap]

display(cafes_cheap)
display(cafes_pricey)

pd.concat([cafes_cheap, cafes_pricey]) #this line will put them back together

#get a random sample
dataset.sample(5) #this will get you a random sample of the dataset
dataset.describe() #this will summarize numerical data
dataset['column'].unique() #will give you a list of all unique values in that column

#example of using assigning values to all rows
party = {name: 'D' if name == 'Obama' else 'R' for name in unique_candidates}
#using this information to add on to the different datasets
sample = data['column'].sample(5)
sample.map(party)

data['party'] = data['name'].map(party)

#summing columns
data['column'].sum()

#count entries to the different rows
data['party'].value_counts()

#use groupby to sort data
data.groupby('party')['reciept_amounts'].sum()

#limiting the dataset based on values
keep_candidates = {'obama', 'romney'}
matches = data['candidate_name'].apply(lambda x: x in keep_candidates)

#create a pivot table
by_occ = data.pivot_table('contb_receipt_amt', index='contbr_occupation', columns='party', aggfunc='sum')

#MERGING DATASETS
A = datset1
B = dataset2

C = A.merge(B, on=['column1', 'column2'])

#different join options
C = A.merge(B, on=['column1', 'column2'], how = 'outer')
C = A.merge(B, on=['column1', 'column2'], how = 'left')
C = A.merge(B, on=['column1', 'column2'], how = 'right')

#VECTOR MATH ON A DATAFRAME for changing year to just be the last 2 digits
table['year'] = table['year'].apply(lambda x: "'{:0d}".format(x % 100))


#MELTING A TABLE
def melt(df, col_vals, key, value):
  keep_vars = df.columns.difference(col_vals) #returns the column values not in df
  melted_sections = [] #empty dataframe
  for c in col_vals:
    melted_c = df[keep_vars].copy()
    melted_c[key] = c
    melted_c[value] = df[c]
    melted_sections.append(melted_c)

  melted = pd.concat(melted_sections)
  return melted


#CASTING A TABLE
def cast(df, key, avlue, join_how='outer'):
  fixed_vars = df.columns.difference(['key','value'])
  tibble = pd.DataFrame (columns=fixed_vars) #empty frame

  new_vars = df[key].unique()
  for v in new_vars:
    df_v = df[df[key] == v]
    del df_v[key]
    df_v = df_v.rename(columns={value:v})
    tiblle = tibble.merge(df_v, on=list(fixed_Vars), how=join_how)

  return tibble

#delimitting pandas dataframe
            




