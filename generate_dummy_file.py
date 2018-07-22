#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import os

def create_dummy_files():
    if not os.path.exists("output"):
        os.mkdir("output")
    print ('How many files will you create?')
    input_time = raw_input('>>>  ')
    if not input_time.isdigit():
        print ('[Err] Please enter half-width numeric characters.')
        return
    digit = 16
    for i in range(int(input_time)):
        random_str = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(digit)])
        with open('output/{}.txt'.format(random_str), 'w') as f:
            f.write('Dummy')
    print ('Creation of the file is completed.')

if __name__ == '__main__':
    create_dummy_files()
