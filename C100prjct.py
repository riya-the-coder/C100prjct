class ATM(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo
 
    def CashWithdrawn(self,object):
        print("Cash Withdrawn",object)

    def BalanceEnquiry(self,object):
        print("Balance is ",object)

Riya=ATM("11008899","5234")
print(Riya.cardNo)
print(Riya.pinNo)
Riya.CashWithdrawn(500)
Riya.BalanceEnquiry(500)
