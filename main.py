from bank import Bank
from creditcard import CreditCard
from features import Features
import json


def add_bank_cards(bank_name, json_data_path, result_list):
    with open(json_data_path) as data:
        cc_data = json.load(data)
        b = Bank(bank_name)
        b.CreditCards = []
        for cc in cc_data:
            f = Features(cc["features"]["joining_fee"], cc["features"]["annual_fee"])
            b.CreditCards.append(CreditCard(cc["name"], f))
        result_list.append(b)


if __name__ == "__main__":
    result_list = []
    add_bank_cards("ICICI Bank", "data/icici.json", result_list)
    add_bank_cards("HDFC Bank", "data/hdfc.json", result_list)
    add_bank_cards("Axis Bank", "data/axis.json", result_list)

    for bank in result_list:
        print(bank)
