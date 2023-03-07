# import os
# print(os.environ['OPENAI_API_KEY']);

import json
import jsonlines

#  read txt file from category.txt and split it into a list of categories removing \n from string, separator is ','
with open('category.txt', 'r') as file:
    categories = file.read().split(',')
    categories = [category.strip() for category in categories]


# Open the text file containing the arrays
with open('questions.txt') as f:
    # Create an empty dictionary to store the arrays
    questions = {}
    # Loop through each line in the file
    for line in f:
        # Split the line into a key and a value
        line = line.strip()
        if line:
            # if line ends with : then it is a category
            if line.endswith(':'):
                category = line.replace(':', '').strip()
                questions[category] = []
            else:
                questions[category].append(line.replace(',', ''))

# Print the dictionary
print(questions)
print(categories)

# using categories create trainingdata.jsonl file with 10 examples for each category
with jsonlines.open('trainingData.jsonl', 'w') as writer:
    for category in categories:
        mainRef = category.split(':')[1].strip() if len(category.split(':')) == 2 else category.split(':')[0]
        if mainRef in questions and len(questions[mainRef]) > 0:
            for question in questions[mainRef]:
                question = question + " /n/nIntent/n/n"
                writer.write({"prompt": question , "completion": category + " END"})
                # writer.write({"prompt": "<prompt text>", "completion": category})



# with open('trainingData.jsonl', 'r') as json_file:
#     json_list = list(json_file)
#
# for json_str in json_list:
#     result = json.loads(json_str)
#     print(f"result: {result}")
#
# # with jsonlines.open('output.jsonl', 'w') as writer:
# #     writer.write_all(items)