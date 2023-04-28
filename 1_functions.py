# this is a user-defined function
def function1(x,y): # x and y are formal parameters
    Sum=x+y
    return Sum

def function2():
    for i in range(10):
        # calling a function inside another function- function2 is the calling function
        # function1 is the called function
        print(function1(i,i*2))

if __name__=='__main__':
    # print is a built-in function of Python
    print(function1(2,5)) # 2 and 5 are the actual parameters
    function2()

    # usage of lambda function
    multiply=lambda x,y: x*y
    print(multiply(4,9))