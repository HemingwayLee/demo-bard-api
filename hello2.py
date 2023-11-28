import os
from bardapi import Bard
from bardapi import BardCookies

# psid = os.getenv('BARD_PSID')
# psidts = os.getenv('BARD_PSIDTS')

cookie_dict = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
}

bard = BardCookies(cookie_dict=cookie_dict)

print(bard.get_answer("文字「a」を含む文を教えてください。その文全体を [] に入れてください。")['content'])
