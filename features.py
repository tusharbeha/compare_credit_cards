class Features:
    def __init__(self,joining_fee, annual_fee):
        self.joining_fee = joining_fee
        self.annual_fee = annual_fee

    def __str__(self):
        return "         |__Joining Fee: " + self.joining_fee + "\n" +\
                "         |__Annual Fee: " + self.annual_fee + "\n"
