#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i')
args = parser.parse_args()
filename = args.i or 'sample.txt'

with open(filename) as f:
    prev = None
    count = 0
    for line in f:
        current = int(line.strip())

        if prev is not None:
            if prev < current:
                print(f'{current} ++ ascending')
                count += 1
            else:
                print(f'{current}')

        prev = current

    print(f'Found {count} increases')
