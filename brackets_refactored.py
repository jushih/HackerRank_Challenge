##!/usr/bin/env python3
import re
import argparse

def parse_args():
    ap = argparse.ArgumentParser(description='Accepts input and checks if brackets are closed',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument( 'input', help='Arithmetic expression')
    
    return ap.parse_args()

ARGS = parse_args()

s = ARGS.input

result = re.sub(r'[^(){}\[\]]', '',s)

openers = ['(','[','{']
pairs = {'}' : '(', ']' : '[','}':'{'}

def locate_pair(bracket):
    for i in len(pairs):
        print(i)

stack = []

for bracket in result:
    if len(stack) == 0:
        stack.append(bracket)
    else:
        if bracket in openers:
            stack.append(bracket)
        #if it's a closing bracket, check whether it closes the last item in the stack
        else: 
            if pairs.get(bracket) == stack[-1]:
                stack.pop()

                
if len(stack) == 0:
    check = 'Y'
else:
    check = 'N'
    
print(check, result)
