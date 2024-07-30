import json

def merge_json_objects(json1, json2):
    merged = {**json1, **json2} #dictionary unpacking
    return merged

if __name__ == "__main__":
    json1 = {"name": "anu", "age": 22}
    json2 = {"city": "vijayanagar", "country": "India"}
    merged_json = merge_json_objects(json1, json2)
    print(json.dumps(merged_json,indent=10))

