import pandas as pd
import pprint

# File variables 
input_file_name = "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/chilli/CSV/chilli_b1_validated_data.csv"
nlu_output_filename = "data/nlu-faq-hort-chilli-b1-pun.yml"
domain_output_filename = "domain-grp/domain-hort-chilli-b1-pun.yml"

# Intant name variable
intent_name = "faq-hort-chilli-b1-pun"

pp = pprint.PrettyPrinter(indent=4)
data = pd.read_csv(input_file_name)

# print(data.columns)
# ['questoions', 'answers', 'Google_Question_punjabi', 'Google_Answer_punjabi']

# print(data.head())
print(data['answers'].nunique())

df_sliced_dict = {}

for ans in data['answers'].unique():
    df_sliced_dict[ans] = data[data['answers'] == ans]

with open(nlu_output_filename, "w") as file, open(domain_output_filename, "w") as file2:
    file.write("version: \"3.0\"\n")
    file.write("nlu:\n")

    file2.write("version: \"3.0\"\n\n")
    file2.write("intents:\n")
    file2.write(f"  - {intent_name}\n\n")
    file2.write("responses:\n")
    for key in df_sliced_dict.keys():
        print(key)
        name = df_sliced_dict[key]['questions'].iloc[0].strip().replace(" ", "-")
        file.write(f"- intent: {intent_name}/{name}\n")
        file.write("  examples: |\n")
        file2.write(f"  utter_{intent_name}/{name}:\n")
        df_key = df_sliced_dict[key].copy()
        lst = df_key['Google_Question_punjabi'].tolist()
        string = "    - "+"\n    - ".join(lst) + "\n"
        file.write(string)
        answer = df_key["Google_Answer_punjabi"].iloc[0]
        file2.write(f"  - text: {answer}\n")
