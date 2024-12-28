import helpers

data_file = helpers.get_data_file_name("printer_updates", use_demo_set=True)
raw_data = helpers.read_data_file(data_file)

page_order_rules = [rule for rule in raw_data.split() if rule.find("|") >= 0]
page_updates = [update for update in raw_data.split() if update.find("|") == -1]

# >>> for rule in print_rules:
# ...     r = rule.split("|")
# ...     befores[r[0]] = [] <-- move out of loop
# ...     befores[r[0]].append(r[1])
# ...
