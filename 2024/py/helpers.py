
import pandas as pd

ROOT_DIRECTORY =  '/home/jeff/projects/adventofcode/2024'
DATA_DIRECTORY = f"{ROOT_DIRECTORY}/data"

def get_data_file_name(puzzle_input, extension = 'txt', use_demo_set=False) -> str:

    file_name = puzzle_input
    if use_demo_set:
        file_name = f"demo_{puzzle_input}"

    data_file = f"{DATA_DIRECTORY}/{file_name}.{extension}"
    msg = f"Using file {data_file} from {DATA_DIRECTORY}."
    print(msg)

    return data_file


def parse_data_file(file_name, convert_to_int=True) -> list:

    with open(file_name, "r") as f:
        raw_data = [line.strip() for line in f.readlines()]

    if convert_to_int:
        data = [list(map(int, r.split())) for r in raw_data]
    else:
        data = [r.split() for r in raw_data]

    return data

def read_data_into_dataframe(data_file, **kwargs):
    
    df = pd.read_csv(data_file, **kwargs)

    return df


# df = read_data("reports", use_demo_set=True, header=None, sep='\s+', names=['a','b','c','d','e'])