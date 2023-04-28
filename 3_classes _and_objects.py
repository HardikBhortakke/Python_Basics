class MyClass(): # class declaration
    def __init__(self, x, y): # constructor function for the class
        self.__x=6
        self.var1=x
        self.var2=y
        print("MyClass has been initialised")
    
    def get_data(self):
        self.var=int(input("Enter the value of a variable"))

    def print_data(self):
        print(self.var)
        print(self.var1)
        print(self.var2)

if __name__=="__main__":
    class1 = MyClass(6, 7) # instantiating an object
    print(class1.__x)
    class1.get_data()
    class1.print_data()
    print(class1.var1)