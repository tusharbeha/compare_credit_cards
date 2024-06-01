from features import Features


class CreditCard:
    def __init__(self, name, features):
        self.name = name
        self.features: Features = features

    def __str__(self):
        return "   |__" + self.name + "\n" + str(self.features)
