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

print(bard.get_answer("「契約」に似た言葉を教えてください。「」の中に似た言葉を入れてください。")['content'])
