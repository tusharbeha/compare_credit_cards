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
            cc_features = cc["features"]

            f = Features(cc_features["joining_fee"], cc_features["annual_fee"],
                         cc_features["interest"] if "interest" in cc_features else "",
                         cc_features["reward_points"] if "reward_points" in cc_features else "",
                         cc_features["redeem"] if "redeem" in cc_features else "",
                         cc_features["fuel"] if "fuel" in cc_features else "",
                         cc_features["annual_fee_waiver"] if "annual_fee_waiver" in cc_features else "",
                         cc_features["movie"] if "movie" in cc_features else "",
                         cc_features["dining"] if "dining" in cc_features else "",
                         cc_features["airport"] if "airport" in cc_features else "",
                         cc_features["railway"] if "railway" in cc_features else "")
            b.CreditCards.append(CreditCard(cc["name"], f))
        result_list.append(b)


if __name__ == "__main__":
    result_list = []
    add_bank_cards("ICICI Bank", "data/icici.json", result_list)
    add_bank_cards("HDFC Bank", "data/hdfc.json", result_list)
    add_bank_cards("Axis Bank", "data/axis.json", result_list)

    for bank in result_list:
        print(bank)
