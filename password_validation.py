# password validation

import re

pattern = re.compile("[a-zA-Z0-9$%#@]{8,}\d$")

password = 'testesenha#4'

a = pattern.fullmatch(password)
print(a)
