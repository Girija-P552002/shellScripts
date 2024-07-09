import json

def write_json_file(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

filepath = 'output.json'
data = {
    "name": "Girija",
    "age": 22,
    "city": "Bangalore"
}

write_json_file(filepath, data)
   
       
