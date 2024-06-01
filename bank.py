from creditcard import CreditCard


class Bank:
    def __init__(self, name):
        self.name = name
        self.CreditCards: [CreditCard] = []

    def __str__(self):
        returnStr = self.name + "\n"
        for cc in self.CreditCards:
            returnStr += str(cc)
        return returnStr

