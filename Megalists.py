
class Megalist:
    MegaCount = 0

    def __init__(self,n=0,ele=[0]):
        self.ele = ele
        self.n= n
        del ele[0]
   
    def addi_items(self):
        self.n = input("how many items u gonna add? ")
        self.n = int(self.n)
        i=int(0)
        ##print(type(i))
        ##print(type(cant))
        while i <  self.n:
            print(i)
            inp =input("add_item_")
            if inp == "done" :
                break
            value = float(inp)
            self.ele.append(value)
            i=i+1
    def prin_Megalist(self):  
        print(self.ele) 
        print(self.n)
     

del1al10 = Megalist()
del1al10.addi_items()
del1al10.prin_Megalist()       