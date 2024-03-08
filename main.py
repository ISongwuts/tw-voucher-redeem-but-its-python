from TWTransaction import TWTransaction
import json
if __name__ == "__main__":
    t: TWTransaction = TWTransaction(
        'Your mobile phone.', 
        'Your redeem link or code.'
    )
    resData = t.redeem()
    print(json.dumps(resData, indent=2))