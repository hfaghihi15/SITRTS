import json
import copy
import os


class DataFile:
    def __init__(self, name, directory, content=None):
        if content is None:
            content = list()
        self.name = name + '.json'
        self.content = content
        file_path = os.path.join(directory, self.name)
        self.path = file_path

    def create_file(self):
        open(self.path, 'w')

    def append_to_file(self, data):
        self.content = copy.deepcopy(data)
        with open(self.path, 'w') as outfile:
            json.dump(data, outfile, indent=2)
