##Counting triangles
#SQL VERSION
#load the database
imdb = connect('im.db')
imdb_cur = imdb.cursor()

#tables include actors, casts, movies
#a triangle exists if actors a and b are co-stars, b and c are co-stars
#start by computing a table of co-stars

query_make_pairs = '''
CREATE TABLE Costars AS
  SELECT X.actor_id as a, Y.actor_id as b
  from Casts as X, Casts as Y
  where (X.moive_id = Y.movie_id) and (X.actor_id <> Y.actor_id)
  groupby X.actor_id, Y.actor_id
'''
#now we can query co-stars like a regular one
imdb_cur.execute('DROP TABLE IF EXISTS Costars')

imdb_cur.execute(query_make_pairs)

display(read_sql_query('SELECT * FROM Costars LIMIT 3', imdb))

##write a query to count the different triangles
#we are dividing by 6 because there would be 6 results for all of the different outcomes
query_triange = '''
SELECT COUNT(*) / 6 as num_triangles 
FROM Costars as X, Costars as Y, Costars as Z
where (X.b = Y.a) and (Y.b = Z.a) and (X.a = Z.b)
'''

sql_tricount_df = read_sql_query(query_triangles, imdb)

##PANDAS CERSION
costars_df = read_sql_query('SELECT * FROM Costars', imdb)
costars_df.head()

#create the different dataframes and rename the columns
X = costars_df
Y = costars_df.rename(columns={'a': 'b', 'b' :'c'})
Z = costars_df.rename(columns={'a' : 'c', 'b': 'a'})

#join the different tables together
XY = X.merge(Y, on='b')
XYZ = XY.merge(Z, on=['a', 'c'])






