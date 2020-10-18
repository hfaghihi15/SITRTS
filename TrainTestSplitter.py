import json
import os
import random

directory = 'data segments/'
directory_files = os.listdir(directory)
# test_index = random.randint(1, len(directory_files)-1)
test_index = 1
# print(test_index)


def train_test_splitter():

    training = []
    test = []

    for fileName in directory_files:
        path = directory + fileName
        if directory_files.index(fileName) != test_index:
            if fileName.endswith(".json"):
                with open(path, 'r') as training_file:
                    s = json.load(training_file)

                for i in s:
                    if i['class'] != '':
                        training.append(i)
        else:
            with open(path, 'r') as test_file:
                s = json.load(test_file)
            for i in s:
                test.append(i)

    with open('training-set.json', 'w+') as training_file:
        json.dump(training, training_file, indent=2)

    # with open('test-set.json', 'w+') as test_file:
    #     json.dump(test, test_file, indent=2)
    #
    training_file.close()
    # test_file.close()
