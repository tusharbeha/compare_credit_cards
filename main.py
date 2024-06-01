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

    credit_cards_hdfc = ["HDFC Bank Regalia Credit Card",
                         "HDFC Bank Diners Club Credit Card",
                         "HDFC Bank Millenia Credit Card",
                         "HDFC Bank MoneyBack Credit Card",
                         "HDFC Bank Platinum Plus Credit card"]

    credit_cards_axis = ["Axis Bank Ace Credit card",
                         "Axis Bank Flipkart Credit card",
                         "Axis Bank Neo Credit card",
                         "Axis Bank Vistara Credit card",
                         "Axis Bank Magnus Credit card"]

    for bank in bank_name_list:
        b = Bank(bank)
        b.CreditCards = []
        if bank == "ICICI Bank":
            for cc in credit_cards_icici:
                b.CreditCards.append(CreditCard(cc))
        elif bank == "HDFC Bank":
            for cc in credit_cards_hdfc:
                b.CreditCards.append(CreditCard(cc))
        elif bank == "Axis Bank":
            for cc in credit_cards_axis:
                b.CreditCards.append(CreditCard(cc))
        bank_list.append(b)

    for bank in bank_list:
        print(bank)
