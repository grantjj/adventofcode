import pandas as pd

root_directory = '/home/jeff/projects/adventofcode/2024'
data_dir = f"{root_directory}/data"

data_file = "significant_locations.txt" 

df = pd.read_csv(f"{data_dir}/{data_file}", header=None, sep='\s+', names = ['list1', 'list2'])

df_1 = df.list1.sort_values().reset_index(drop=True)
df_2 = df.list2.sort_values().reset_index(drop=True)
df_joined = pd.concat([df_1, df_2], axis=1)
df_joined['diffs'] = abs(df_joined.list1 - df_joined.list2)

total_distance = sum(df_joined['diffs'])
print(f"The total distance between lists is {total_distance}.")

df_counts = df.join(df.value_counts("list2"), on="list1", how="left").fillna(0)
df_counts['similarity_score'] = df_counts['count'] * df_counts['list1']
print(sum(df_counts.similarity_score))