## given a list return the concatenation of thes trings in reverse order
def strcat_list(L):
    assert type(L) is list
    ###
    ### YOUR CODE HERE
    
    x = copy.deepcopy(L)
    x.reverse()
    return "".join(x)
-------------------------------------------------------------------------
#given two numbers return the floor fraction, which means 3/2 = 1 because you just remove the decimal place
def floor_fraction(a, b):
    assert is_number(a) and a >= 0
    assert is_number(b) and b > 0
    ###
    ### YOUR CODE HERE
    return int(a // b)
-------------------------------------------------------------------------
#given two numbers return the ceiling fraction, which means 3/2 = 2 because you need to round up
def ceiling_fraction(a, b):
    assert is_number(a) and a >= 0
    assert is_number(b) and b > 0
    ###
    ### YOUR CODE HERE
    return int(a // b)+1
-------------------------------------------------------------------------
#given 3 values take the average
def report_exam_avg(a, b, c):
    #assert is_number(a) and is_number(b) and is_number(c)
    ###
    ### YOUR CODE HERE
    average = round((a+b+c)/3,1)
    return f"Your average score: {average}"
-------------------------------------------------------------------------
#write a function that givena  string consisting of words and spaces return a list with the lengths of the words. There will be multiple spaces
def count_word_lengths(s):
    assert all([x.isalpha() or x == ' ' for x in s])
    assert type(s) is str
    ###
    ### YOUR CODE HERE
    everything_list = s.split(" ")

    my_list = []

    for i in range(len(everything_list)):
        if everything_list[i].isalpha():
            my_list.append(everything_list[i])

    count_list = [len(my_list[i]) for i in range(len(my_list))]
    return count_list
