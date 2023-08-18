import json

file_path = 'nounlist.txt'
output_path = 'nounlist.json'

with open(file_path, 'r') as file:
    content = file.read()

words = content.split('\n')

data = {"words": words}

json_data = json.dumps(data, indent=4)

with open(output_path, 'w') as json_file:
    json_file.write(json_data)
