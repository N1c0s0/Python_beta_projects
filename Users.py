class Users_:
 
 def __init__(self, name="", passwo="", passwo2=""):
        print(0)
        self.name = name
        self.passwo = passwo
        self.passwo2 = passwo2
 def Create(self):  
        self.name= input("type username: ")
        self.passwo2= input("type new password: ") 
        if input("type new password again: ")  == self.passwo2:
             self.passwo=self.passwo2
             print("user: "+self.name+" was created")
        else:
            print("thats not correct, user and password not created")
            self.name="0"
            self.passwo2="0"
            self.passwo="0"
            exit()


 def print_all(self): 
            print(self.name)
            print(self.passwo)

 def Login(self): 
        if self.name == input("type your username : "):
                ##print("correct user")
                if self.passwo == input("type your password : "):
                    print("correct password, you are inside the system")
                else:
                    print("wrong password")    
        else:
             print("wrong user, try again")        

             

user_nico = Users_()    
user_nico.Create()
##user_nico.print_all()
user_nico.Login()



