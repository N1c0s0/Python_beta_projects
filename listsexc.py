
class Megalist:
    MegaCount = 0

    def __init__(self,n=0,ele=[0]):
        self.ele = ele
        self.n= n
       
    def addi_items(self):
        
        ##print(type(cant))
        self.n = input("how many items u gonna add? ")
        self.n = int(self.n)
        i=int(0)
        ##print(type(i))
        ##print(type(cant))
        while i <  self.n:
            print(i)
            self.ele[i] = self.ele.append(input("add_item_"))
            print(self.ele)
            i=i+1
    def prin_Megalist(self):  
        print(self.ele) 
        print(self.n)
     

del1al10 = Megalist()
del1al10.addi_items()
del1al10.prin_Megalist()       