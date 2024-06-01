from bank import Bank
from creditcard import CreditCard

if __name__ == "__main__":
    bank_name_list = ["ICICI Bank", "HDFC Bank", "Axis Bank"]
    bank_list = []
    credit_cards_icici = [
        "ICICI Bank Emeralde Credit Card",
        "ICICI Bank Sapphiro Credit Card",
        "ICICI Bank Coral Contactless Credit Card",
        "ICICI Bank Rubyx Credit Card",
        "ICICI Bank Platinum Chip Credit Card",
        "ICICI Bank VISA Signature Credit Card",
        "ICICI Bank HPCL Super Saver Credit Card",
        "MakeMyTrip ICICI Bank Signature Credit Card"
      ]
    for bank in bank_name_list:
        b = Bank(bank)
        b.CreditCards = []
        if bank == "ICICI Bank":
            for cc in credit_cards_icici:
                b.CreditCards.append(CreditCard(cc))

        bank_list.append(b)

    for bank in bank_list:
        print(bank)
