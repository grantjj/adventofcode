#!/usr/bin/env python3
import numpy as np

import sys
sys.path.append('../')
from common.readinput import read_filename


def read_file(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return lines

def build_map(lines):
    results = []
    for i, line in enumerate(lines):
        results.append([])
        for c, char in enumerate(line):
            cleaned_char = char.strip()
            bit = int(cleaned_char) if str.isdigit(cleaned_char) else None
            if bit == 0 or bit == 1:
                results[i].append(bit)

    return results

def calculate_gamma(data):
    num_digits = len(data[0])
    num_rows = len(data)
    gamma_bits = ''
    for i in range(num_digits):
        count_of_set_bits = 0
        for row in data:
            count_of_set_bits += row[i]

        if count_of_set_bits > num_rows / 2:
            gamma_bits += '1'
        else:
            gamma_bits += '0'

    return gamma_bits

def calculate_epsilon(gamma):
    bits = 32

    ugamma = bin(np.uint32(int(gamma, 2)))
    print(ugamma)

    shift_count = bits - len(gamma)
    print(shift_count)

    leftgamma = bin(int(ugamma, 2)<< shift_count)
    print(leftgamma)

    inverted = bin(~np.uint32(int(leftgamma, 2)))
    print(inverted)

    normalized = bin(int(inverted,2) >> shift_count)
    print(normalized)

    return normalized


def main():
    input = read_file(read_filename())
    model = build_map(input)
    print(model)

    gamma = calculate_gamma(model)
    print(f'Gamma: {gamma} as decimal: {int(gamma, 2)}')

    epsilon = calculate_epsilon(gamma)
    print(f'Epsilon: {epsilon} as decimal: {int(epsilon, 2)}')

    print(f'Total Power Consumption: {int(gamma, 2)*int(epsilon,2)}')





main()

