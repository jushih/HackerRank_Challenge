##!/usr/bin/env python3
import re
import argparse

def parse_args():
    ap = argparse.ArgumentParser(description='Determines if an email address is valid or invalid',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument( 'email', help='E-mail address')
    return ap.parse_args()

ARGS = parse_args()


def validate(email):
    
    email = email.lower()
    split = re.split("@",email)
    front = split[0]

    if (len(email) == 0                                 # email is empty
        or len(split) != 2                              # has more or less than one @ symbol
        or email[0].isalpha() is False                  # doesn't begin with letter
        or len(re.sub('[a-zA-Z0-9_]','',front)) > 0):   # front half is not alphanumeric
        return False

    back = split[1]
    back_split = back.split(".")
    
    # for addresses with 2 parts
    if len(back_split) == 2:
        if (len(back_split[1]) not in [2,3]             # last part contains more or less than 2-3 letters
        or back_split[1].isalpha() == False             # last part contains non-alpha characters
        or len(re.sub('[a-zA-Z0-9_]','',back_split[0])) > 0): # first part is not alphanumeric
            return False

    # for addresses with 3 parts
    elif len(back_split) == 3:
        if (len(back_split[2]) not in [2,3]             # last part contains more or less than 2-3 letters
        or back_split[2].isalpha() is False             # last part contains non-alpha characters
        or len(re.sub('[a-zA-Z0-9_]','',back_split[1])) > 0 # middle part is not alphanumeric
        or len(re.sub('[a-zA-Z0-9_]','',back_split[0])) > 0 # first part is not alphanumeric
           ):
            return False
    else:
        return false                                    # back half doesn't have between 2 and 3 parts

if validate(ARGS.email) is False:
    print('Invalid')
else:
    print('Valid')
    
