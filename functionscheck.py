"""8 6 VarArgs parameters
Sometimes you might want to define a function that can take any number of parameters, i.e. variable number of arguments, this can be achieved by using the stars (save as function_varargs.py ): """

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count
print (total(10, 1, 2, 3, vegetables=50, fruits=100))
