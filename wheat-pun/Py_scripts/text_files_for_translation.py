from fileinput import filename
import yaml
import os
import pandas as pd

nlu_file_names = [
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/data/nlu-faq-agri-wheat-b0-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/data/nlu-faq-agri-wheat-b1-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/data/nlu-faq-agri-wheat-b2-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/data/nlu-faq-agri-wheat-b3-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/data/nlu-faq-agri-wheat-b4-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/data/nlu-faq-agri-wheat-b5-pun.yml" 
    ]

domain_file_names = [
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/domain-grp/domain-agri-wheat-b0-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/domain-grp/domain-agri-wheat-b1-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/domain-grp/domain-agri-wheat-b2-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/domain-grp/domain-agri-wheat-b3-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/domain-grp/domain-agri-wheat-b4-pun.yml",
    "/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/domain-grp/domain-agri-wheat-b5-pun.yml"
    ]

questions_list = []
intent_names = []
sentences = []
for filename in nlu_file_names:
    with open(filename) as file:
        documents = yaml.full_load(file)
        # print(documents)
        for item, doc in documents.items():
            if item == "nlu":
                # print(item, ":")
                for i in range(len(doc)):
                    for sen in doc[i]["examples"].split("\n"):
                        # print(sen[2:])
                        # print()
                        # print(doc[i]['intent'])
                        if len(sen) > 1:    
                            intent_names.append(doc[i]['intent'])
                            sentences.append(sen[2:])
                        # questions_list.append()
                        # intent_names.append(doc[i]['intent'])

answer_list = []
second_answer_list = []
for filename in domain_file_names:        
    with open(filename) as file:
        documents = yaml.full_load(file)
        # print(documents)
        for item, doc in documents.items():
            if item == "responses":
                print(item, ":")
                for intent in intent_names:
                    try:
                        # print(doc["utter_{}".format(intent)])
                        if len(doc["utter_{}".format(intent)]) == 1:
                            answer_list.append(doc["utter_{}".format(intent)][0]['text'])
                            second_answer_list.append(" ")
                        else:
                            answer_list.append(doc["utter_{}".format(intent)][0]['text'])
                            second_answer_list.append(doc["utter_{}".format(intent)][1]['text'])
                    except:
                        pass
                    # print(doc[i]["examples"].split("\n")[0])


with open("/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/TEXT/question_wheat.txt", "w") as question_file:
    for question in sentences:
        # print(question)
        question_file.write(question.strip())
        question_file.write("\n")
        question_file.write("\n")
print(f"{len(sentences)} question written")

with open("/home/ubuntu/SSA/Diff_Bot_setup/FourteenBot/wheat-pun/TEXT/answers_wheat.txt", "w") as answer_file:
    for answer in answer_list:
        answer_file.write(answer.strip())
        answer_file.write("\n")
        answer_file.write("\n")
print(f"{len(sentences)} answers written")