# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint
class Train:
    
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getstate(self):
        print(f"Train no: {self.trainNo} is running on time")

    def gerFare(self, fro,to):
        print(f"Train fare in train no: {self.trainNo} from {fro} to {to} is {randit(222 , 5555)}")            

t = Train(12399)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")    


