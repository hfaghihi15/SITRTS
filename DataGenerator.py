import random
import pandas as pd
import ast
from DataFile import DataFile
import sys
sys.path.append(sys.path[0] + "\data segments")
this_directory = sys.path[-1]

sensors = ["existed1", "existed2", "existed3", "motion1", "motion2", "motion3", "TV",
           "light1", "light2", "light3", "monotone", "noise", "class"]
dataset = list()
objects = list()
number = 0

for i in range(10):
    objectName = 'DataSegment%s' % (i+1)
    objects.append(DataFile(objectName, this_directory))
    objects[i].create_file()


for _ in range(0, 2000):
    this_record = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1),
                   random.randint(0, 1), random.randint(0, 1), random.randint(0, 1),
                   random.randint(0, 1),
                   round(random.uniform(0.0, 1.0), 2), round(random.uniform(0.0, 1.0), 2), random.randint(0, 1),
                   random.randint(0, 1),
                   round(random.uniform(0.0, 1.0), 2),
                   '']
    this_record = pd.Series(this_record, index=sensors)
    this_record = this_record.to_json(orient='index')
    this_record = ast.literal_eval(this_record)
    dataset.append(this_record)

    if len(dataset) == 200:
        objects[number].append_to_file(dataset)
        number += 1
        dataset.clear()

# for j in objects:
#     print(j)
#     print(j.name)
#     print(len(j.content))

