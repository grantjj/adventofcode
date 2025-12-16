from collections import Counter, defaultdict

import helpers

data_file = helpers.get_data_file_name("printer_updates", use_demo_set=True)
raw_data = helpers.read_data_file(data_file)

page_order_rules_raw = [rule for rule in raw_data.split() if rule.find("|") >= 0]
page_updates_raw = [update for update in raw_data.split() if update.find("|") == -1]
print(page_order_rules_raw)
print(page_updates_raw)


# # firsts = Counter([int(n.split("|")[0]) for n in page_order_rules_raw])
# # seconds = Counter([int(n.split("|")[1]) for n in page_order_rules_raw])
# # pages = list(set(list(firsts.keys()) + list(seconds.keys())))
# pages = set()
# # page_order_rules = defaultdict(dict, {0: {"before": [], "after": []}})
# page_order_rules = defaultdict(lambda: defaultdict(list))
# print(page_order_rules)
# for rule in page_order_rules_raw:
#     r0, r1 = [int(r) for r in rule.split("|")]
#     # page_order_rules[before]["after"]
#     # pages.update([int(r[0]), int(r[1])])
#     page_order_rules[r0]["before"].append(r1)
#     page_order_rules[r1]["after"].append(r0)

# # page_order_rules = {p: {} for p in pages}

# # for k, v in page_order_rules.items():
# #     print(k, v)

# for update in page_updates_raw:
#     update_list = [int(u) for u in update.split(",")]
#     # print(update_list)
#     for n, u in enumerate(update_list):
#         # print(u, page_order_rules[u])
#         if any(_u in page_order_rules[u]["after"] for _u in update_list[:n]):
#             print(u, update_list, page_order_rules[u])


# # print(firsts)
# # print(seconds)
# # page_order_list = [page for page in sorted(firsts, key=firsts.get, reverse=True)]
# # page_order_list.extend(
# #     [page for page in sorted(seconds, key=seconds.get) if page not in page_order_list]
# # )

# # page_order_map = {page: n for n, page in enumerate(page_order_list)}
# # print(page_order_map)


# # middle_sum = 0
# # for update in page_updates:
# #     update_list = [int(u) for u in update.split(",")]
# #     update_mapped = [page_order_map[u] for u in update_list]
# #     print(update_list, update_mapped)
# #     if update_mapped == sorted(update_mapped):
# #         middle_sum += update_list[len(update_list) // 2]

# # print(middle_sum)
