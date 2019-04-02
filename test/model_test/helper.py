import random
import string


def anyvalue(N=1, size=8):
    return [''.join(random.choices(string.ascii_uppercase + string.digits, k=size)) for _ in range(N)]
