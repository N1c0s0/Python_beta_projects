class Greeter:
    Greet_count = 0 
    def __init__(self):
        self.name = input("enter greeter name ")
        self.lang= input("enter the greeter language, press 1 for english ")
        print(self.name+self.lang)
        Greeter.Greet_count += 1

    def greet(self) :
        if self.lang == 1 :
            print('hello '+ self.name )   

    ##def ask_join_greeter(cant):
        ##cant= input("how many greeter to add")
        ##for i in range (i,cant) :
            
greeter1 = Greeter()
greeter1.greet()

print(list(Greeter))