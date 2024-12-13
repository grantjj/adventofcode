import helpers

read_data_kwargs = {
    "header": None,
    # "sep": "\s+",
    "names": ["reports_raw"]
}

data_file = helpers.get_data_file_name("reports") #, use_demo_set=True)
# df = helpers.read_data_into_dataframe(data_file, **read_data_kwargs)

with open(data_file, 'r') as input:
    raw_reports = [line.strip() for line in input.readlines()]

reports= [list(map(int, report.split())) for report in raw_reports]

safe = 0
for n, report in enumerate(reports):
    
    if report == sorted(report) or report == sorted(report, reverse=True):
        is_inc_or_dec = True
    else:
        is_inc_or_dec = False

    consecutive_gaps = [abs(x - report[i-1]) for i, x in enumerate(report) if i>0]

    if max(consecutive_gaps) <= 3 and min(consecutive_gaps) > 0:
        good_gaps = True
    else:
        good_gaps = False

    if is_inc_or_dec and good_gaps:
        safe+=1
    
print(f"There are {safe} safe report(s).")
