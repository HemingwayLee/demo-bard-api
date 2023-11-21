from bardapi import Bard
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "",
    "__Secure-1PSIDTS": "",
}

bard = BardCookies(cookie_dict=cookie_dict)

# print(bard.get_answer("こんにちは"))
print(bard.get_answer("give me a Japanese sentence which contains 'ラーメン'")['content'])
print(bard.get_answer("give me 2 Japanese sentences which contains '年'")['content'])
