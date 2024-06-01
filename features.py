class Features:
    def __init__(self,joining_fee="", annual_fee="", interest="", reward_points="", redeem="", fuel="", annual_fee_waiver="", movie="", dining="", airport="", railway=""):
        self.joining_fee = joining_fee
        self.annual_fee = annual_fee
        self.interest = interest
        self.reward_points = reward_points
        self.redeem = redeem
        self.fuel = fuel
        self.annual_fee_waiver = annual_fee_waiver
        self.movie = movie
        self.dining = dining
        self.airport = airport
        self.railway = railway


    def __str__(self):
        resultStr = ""
        if len(self.joining_fee) > 0:
            resultStr += "         |__Joining fee: " + self.joining_fee + "\n"
        if len(self.annual_fee) > 0:
            resultStr += "         |__Annual fee: " + self.annual_fee + "\n"
        if len(self.interest) > 0:
            resultStr += "         |__Interest: " + self.interest + "\n"
        if len(self.reward_points) > 0:
            for r in self.reward_points:
                resultStr += "               |__Reward points: " + r + "\n"
        if len(self.redeem) > 0:
            resultStr += "         |__Redeem: " + self.redeem + "\n"
        if len(self.fuel) > 0:
            resultStr += "         |__Fuel: " + self.fuel + "\n"
        if len(self.annual_fee_waiver) > 0:
            resultStr += "         |__Annual fee waiver: " + self.annual_fee_waiver + "\n"
        if len(self.movie) > 0:
            resultStr += "         |__Movie: " + self.movie + "\n"
        if len(self.dining) > 0:
            resultStr += "         |__Dining: " + self.dining + "\n"
        if len(self.airport) > 0:
            resultStr += "         |__Airport: " + self.airport + "\n"
        if len(self.railway) > 0:
            resultStr += "         |__Railway: " + self.railway + "\n"

        return resultStr
