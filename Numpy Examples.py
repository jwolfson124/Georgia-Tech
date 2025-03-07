###
B = np.array([0,1,2,3],
         [4,5,6,7],
         [8,9,10,11]
)
B.ndim #gives the number of dimensions
B.shape #returns the shape of the array
len(B) # gives the number of rows

np.ones((3,4)) #will create an array of 3,4 with only 1's
np.eye(3) #will give a diagnol of 1. throughout a matrix of 0
np.diag([1,2,3]) #will give a diagnol of 1,2,3 throughout the matrix
np.empty((3,4)) #this will give an empty array 3,4 whos inital values do not hold meaning

array.dtype #will give you the type of values in the array

##SLICING: when getting a slice of a list it does not effect the inital values of the list
array[select array, select row, select column values]
#going backwards

array[1,0.::-1] #will give the second array, first row, backwards

#do numpy arrays overlap
np.may_share_memory(array a, array b)

#pulling by index
index_pull_list = [1,2,5,6]
new_array = array[index_pull_list] #this will take all of the values at those indexs and create a new array

#boolean masking example greater than 0 and multiple of 3
mask = (x > 0) & ((x % 3) == 0) #must use & sign instead of and

array[mask]


##aggregation and reductions 
np.max(array) #to all elements
np.min(array)
np.sum(array)

#axis function
np.max(array, axis = 0) #the max for each column so you get the number of rows back
np.max(array, axis = 1) #the max for each row so you get the number of columns back
#based on the .shape function





