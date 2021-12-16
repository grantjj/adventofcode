import argparse

def read_filename():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i')
    args = parser.parse_args()
    return args.i or 'sample.txt'

