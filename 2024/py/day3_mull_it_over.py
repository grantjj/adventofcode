import re

import helpers

data_file = helpers.get_data_file_name("memory")  # , use_demo_set = True)
# print(helpers.parse_data_file(data_file, convert_to_int=False))


def mul(x, y):
    return x * y


def do():
    return True


def dont():
    return False


raw_data = ""
with open(data_file, "r") as s:
    for line in s.readlines():
        raw_data += line

# part 1
# valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", raw_data)

# total = 0
# for instruction in valid_instructions:
#     total += eval(instruction)

# part 2
valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", raw_data)
print(valid_instructions)
enabled = True
total = 0
for instruction in valid_instructions:
    result = eval(instruction.replace("'", ""))
    if type(result) is bool:
        enabled = result

    if enabled and type(result) is int:
        total += eval(instruction)

print(total)
