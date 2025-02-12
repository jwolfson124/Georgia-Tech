#create a function that takes a string and converts it to binary given a certain base
### Exercise 0 solution
def eval_strint(s, base=2):
    assert type(s) is str
    assert 2 <= base <= 36
    ###
    ### YOUR CODE HERE
    return int(s, base)
------------------------------------------------------------------------------------
#Create a function that uses the same logic as the previous function but if there is a fraction / decimal it is dealt with

    if "." in s:
        result = 0

        #create a new variable that will have the values split up
        x = s.split(".")

        #the positive i and the negative i that will be used to mulitply by the base
        pos_i = len(x[0])-1
        
        neg_i = -1
        
        base = Decimal(base)
        
        #print("The length of the integers before the '.' are", pos_i)

        #create a variable that will hold all values before the decimal and create a loop to do the calculation
        before = x[0]
        
        after = x[1]

        for num in before:
            if not num.isalpha():
                result += Decimal(num) * (base**pos_i)
                pos_i -= 1
            else:
                num = ord(num) - ord('a') + 10
                result += Decimal(num) * (base**pos_i)
                pos_i -= 1

        for num in after:
            if not num.isalpha():
                result += Decimal(num) * (base**neg_i)
                neg_i -= 1
            else:
                num = ord(num) - ord('a') + 10
                result += Decimal(num) * (base**neg_i)
                neg_i -= 1

        return float(result)

    else:
        x = eval_strint(s, base)
        return float(x)
