import helpers

read_data_kwargs = {
    "header": None,
    # "sep": "\s+",
    "names": ["reports_raw"]
}

data_file = helpers.get_data_file_name("reports") #, use_demo_set=True)
reports = helpers.parse_data_file(data_file)
# df = helpers.read_data_into_dataframe(data_file, **read_data_kwargs)

def safety_check(report):

    diffs = [(val - report[i-1]) for i, val in enumerate(report) if i>0]
    safe_and_increasing_flg = all(val > 0 and val in range(1,4) for val in diffs)
    safe_and_decreasing_flg = all(val < 0 and val in range(-3, 0) for val in diffs)

    if safe_and_increasing_flg or safe_and_decreasing_flg:
        return True
    else:
        return False
    

safe_reports = 0
for n, report in enumerate(reports):

    report_is_safe = safety_check(report)
    if report_is_safe:
        safe_reports += 1

    # part 2
    else:
        for n, level in enumerate(report):
            report_copy = report.copy()
            report_copy.pop(n)
            print(report_copy)
            if safety_check(report_copy):
                safe_reports += 1
                break


print(f"There are {safe_reports} safe report(s).")
