from bardapi import Bard
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "cghBBIw5QpAvtqPuMQuFkIlk8RGX6gU0QDHSuIk0oi20Umn-dc8M8Glfzf65ru_YWl5rgQ.",
    "__Secure-1PSIDTS": "sidts-CjEBNiGH7sFZ-lzxSL4iFfvDSg2PlnOltF8qTfy3in5Df4wHMRXPruqDbh3OPvcC3lqnEAA",
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)

print(bard.get_answer("こんにちは"))
print(bard.get_answer("give me a Japanese sentence which contains 'ラーメン'")['content'])

