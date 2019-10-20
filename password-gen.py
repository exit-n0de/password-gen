#!/usr/bin/env python
import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
#Next line you can change the variable of the range
#It depends on how long you want your generated password
password =  "".join(choice(characters) for x in range(25))
print ""
print password
print ""
