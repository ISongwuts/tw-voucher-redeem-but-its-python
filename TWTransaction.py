from urllib.parse import urlparse, parse_qs
import requests
import json
import re

class TWTransaction:
    def __init__(self, phoneNumber: str, URLOrCode: str) -> None:
        self.__phoneNumber = phoneNumber
        self.__URLOrCode = URLOrCode

    def redeem(self) -> any:
        redeemCode: str = self.__getRedeemCode(self.__URLOrCode)
        redeemURL: str = f'https://gift.truemoney.com/campaign/vouchers/{redeemCode}/redeem'
        headers: dict = { 
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        payload: dict = { "mobile": self.__phoneNumber }
        
        try:
            response: requests.Response = requests.post(redeemURL, headers=headers, json=payload)

            if response.headers.get('content-type') == 'application/json':
                data = response.json()
                return data
            else:
                print("Response does not contain JSON content:", response.text)
        except requests.RequestException as e:
            print("Error occurred during request:", e)

    def __getRedeemCode(self, s: str) -> str:
        return parse_qs(urlparse(s).query)['v'][0] if self.__isURL(s) else s


    def __isURL(self, s: str) -> bool:
        pattern: str = '^(?!mailto:)(?:(?:http|https|ftp)://)(?:\\S+(?::\\S*)?@)?(?:(?:(?:[1-9]\\d?|1\\d\\d|2[01]\\d|22[0-3])(?:\\.(?:1?\\d{1,2}|2[0-4]\\d|25[0-5])){2}(?:\\.(?:[0-9]\\d?|1\\d\\d|2[0-4]\\d|25[0-4]))|(?:(?:[a-z\\u00a1-\\uffff0-9]+-?)*[a-z\\u00a1-\\uffff0-9]+)(?:\\.(?:[a-z\\u00a1-\\uffff0-9]+-?)*[a-z\\u00a1-\\uffff0-9]+)*(?:\\.(?:[a-z\\u00a1-\\uffff]{2,})))|localhost)(?::\\d{2,5})?(?:(/|\\?|#)[^\\s]*)?$'
        return True if re.match(pattern, s) else False