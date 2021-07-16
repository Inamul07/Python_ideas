import string as s
from random import *

ch = s.ascii_letters + s.digits + s.punctuation
password = "".join(choice(ch) for i in range(randint(8, 12)))
print("Random Password: ", password)