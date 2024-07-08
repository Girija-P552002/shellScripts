import json

def read_json_file(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

file_path = "text1.txt"
data = read_json_file(file_path)
print(json.dumps(data,indent=4))


