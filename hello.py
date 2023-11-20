from bardapi import Bard
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "cghBBIw5QpAvtqPuMQuFkIlk8RGX6gU0QDHSuIk0oi20Umn-dc8M8Glfzf65ru_YWl5rgQ.",
    "__Secure-1PSIDTS": "sidts-CjEBNiGH7gqctZrl14Kcm6h9DWjb3KI8riGLREF0P0f4YusXthosA787QGMsbDvhBrMNEAA",
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)

print(bard.get_answer("こんにちは"))

