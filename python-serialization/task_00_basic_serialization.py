import json
''' 0 '''


def serialize_and_save_to_file(data, filename):
    ''' 0 '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
