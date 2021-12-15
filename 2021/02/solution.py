#!/usr/bin/env python3

import argparse

def read_filename():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i')
    args = parser.parse_args()
    return args.i or 'sample.txt'


def main():
    horizontal = 0
    depth = 0

    with open(read_filename()) as f:
        for line in f:
            direction, value = line.strip().split(' ')
            value = int(value)
            match direction:
                case 'forward':
                    horizontal += value
                case 'backward':
                    horizontal -= value
                case 'down':
                    depth += value
                case 'up':
                    depth -= value
                case '_':
                    print('unhandled: {dierction}')

        print(f"Horizontal {horizontal} * Depth: {depth}  = {horizontal*depth}")

main()
