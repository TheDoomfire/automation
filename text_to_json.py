import json

# Edit this
file_path = 'DaleChallEasyWordList.txt'


file_name = file_path.rsplit('.', 1)
output_path = file_name[0] + ".json"

with open(file_path, 'r') as file:
    content = file.read()

words = content.split('\n')

data = {"words": words}

json_data = json.dumps(data, indent=4)

with open(output_path, 'w') as json_file:
    json_file.write(json_data)
