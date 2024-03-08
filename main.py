from TWTransaction import TWTransaction
import json
if __name__ == "__main__":
    t: TWTransaction = TWTransaction(
        '0944271168', 
        'https://gift.truemoney.com/campaign/voucher_detail?v=662fe462daf74b14b001fd65ad006161643'
    )
    resData = t.redeem()
    print(json.dumps(resData, indent=2))