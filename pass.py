# This program involves two functions: rand_password(), which is the
# password generator, and passStrength(p), which grades the strength
# of the generated password.

import re
import string
import random
import numpy as np

# Password Generator Function
def rand_password(pass_length, select):

    if pass_length >= 6 and pass_length <= 128:
        # Fills the empty string password with random characters from select
        new_password = ''.join(np.random.choice(select, pass_length))
    else:
        print('Password length range invalid')

    return(new_password)

# Password Strength Function
def passStrength(p):
        strflag = True
        # Uses regex search method to check specific criteria
        if not re.search('[a-z]', p):
            pass
        elif not re.search('[A-Z]', p):
            pass
        elif not re.search('[0-9]', p):
            pass
        elif not re.search('[!"#$%&()*+,-./:;<=>?@^_`{|}~]', p):
            pass
        elif re.search('\s', p): # The '\s' matches whitespace
            pass
        else:
            strflag = False
        return strflag

# Selection of possible characters
select = list(string.ascii_letters + '0123456789' + '!"#$%&()*+,-./:;<=>?@^_`{|}~')

# Set password length within given valid range
pass_length = int(input('Enter password length from 6 to 128: '))

gen_pass = rand_password(pass_length, select)
# Will continue to generate a password until proper strength is met
count = 0
while passStrength(gen_pass) and (count < 100):
    gen_pass = rand_password(pass_length, select)
    count += 1

if count == 100:
    print('Could not generate password of selected length with acceptable strength.')

print('New password generated:', gen_pass)
