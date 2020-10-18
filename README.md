# SitRTS: Situation Recognition Tree-based Service
### SitRTS is a situation recognition service based on the decision trees

**- How to run?:**

Simply clone/ download the codes, run `main.py` to get the output in the IDE terminal.
If you wanna change the input data (_/data segments/_), first make sure that the new files are named correctly
in-format (DataSegment(number).json; like `DataSegment2.json`). First, run `RawDataVerifier.py` then run `main.py` module.

**- What is SitRTS?:**

SitRS is the abbreviation of Situation Recognition Service. As a part of smart homes, it uses the knowledge of experts
to find the predefined situation in a place (here, a company's office) and does something. For example, if condition1
and condition2 and ... happened; its class-label is 'working', so do something... SitRS is an expert system.

SitRTS uses decision tree to fit into the previous happened situations. Then, updates expert-defined situation templates,
if there is any changes in the pattern. SitRTS rests behind the SitRS, and in certain time-intervals updates it
according to new occurring patterns. SitRTS is a data system.

**- How does the code work?:**

1) `Sensor.py` is where the class for creating sensors is defined in.

2) `SitRS.py` is the home for defining classes for creating situations and situation nodes.

3) In `index.py` 12 sensor were created; existed1, existed2, etc. Then a value is assigned to the sensors
with analog value (light1, light2 and noise). These values are between [0, 1]. Moreover, using
SituationRule() from SitRS, all possible situations are defined.

4) In situations folder, we have 4 python scripts where we assigned some random (or expert-based) situations
a label. (labels including: close, edu, open, working)

5) `DataGenerator.py` file is for creating random situations without class labels defined. output files will be created
in the _/data segment/_ directory. Data files are created as objects of the class DataFile, which is written inside 
`DataFile.py` module.

6) In data segments, there are some json files with many randomly-created situations with class labels.

7) `RawDataVerifier.py` checks if any data has a class-label conflicting with the expert's comprehension of the
situations' conditions.

8) `TrainTestSplitter.py` uses json files in data segments folder to create a `training-set.json` and a `test-set.json` file.

9) Then, train_test_splitter() from `TrainTestSplitter.py` is used to create data. After that, decision tree
is created and fit to training-set. Using graphviz, a graphical tree is been drew, rules and strengths
are extracted using `TreeToCode.py` module. These are done within `DecisionTree.py` module

10) In `TreeToCode.py` the low level attribute of sklearn decision trees (_tree) is used to convert
high-level decision tree into rules.

11) In `DNF.py` Both situation templates and decision tree rules are converted into DNF (SoP) form for convenience.

12) In `Comparator.py`, three functions are ran over situation templates and decision tree output rules:
1. If there is a sub-situation in SitRS but not in tree, remove it!
2. If there is a tree branch in tree but not in sub-situations, add it to the situation templates.
3. If a sub-situation has similar tree branch in tree, optimize rules of sub-situation due to the tree branch.

13) `AccuracyCalculator.py` is for calculating the accuracy of a situation template structure over the input test-data.

14) `TreePlotter.py` draws the tree graph for tree-structured lists (like temp_situations). It is also known as
data-tree simple graphs. In this module, the graphviz's dot language is used to create the trees.

* Graphviz is an awesome tool for creating graphs and visual structures, with a simple XML-liked language, 
named "dot language". [More about graphviz.](https://www.graphviz.org)
* Drawing simple bash-style data tree is also made possible via "anytree" python package.
[Read the documentation to find out more.](https://anytree.readthedocs.io/en/latest/)


15) Finally, `main.py`: Some situation templates are defined manually. "comparator" function from `Comparator.py` updates 
situation templates based on the decision tree (imported at top). Then, the variable 'iterations' makes the preceding 
for-loop iterate multiple times. In the for-loop, train_test_splitter() creates test and train files. calculate_accuracy()
is called to compute the accuracies of situation temp and updated situation temp, accuracy_score is called from
sklearn.metrics to compute the accuracy of decision tree, all over the test file. Then, the accuracies are printed
in the standard output. At last, tree_plotter() function from `TreePlotter.py` is called to draw simple tree graphs
per each situation template. Created graphs are located inside the _/data trees/_ directory.

* Note: `TemplateData.json` has 287 labeled situations, which could be used as the training-set/ test-set. But not
used in the main program.

* Note: After running the main module, `DT` and `DT.pdf` will be automatically created by graphviz.

* Note: _/data trees/_ directory is empty at first. Running main file will drop graph files (`.dot` and `.pdf`) 
inside it.

* Important note for understanding json-files:
1. The key 'existed' means that someone was present (moving) in this room (1,2 or 3) moments ago
2. The key 'motion' means that someone is present (moving) in the room now! which has values yes(1) or no(0)
3. The key 'TV' means that TV (IN ROOM 1) is off(0) or on(1)
4. Keys 'light1' and 'light2' are dimmer-based lights, which values may vary between [0, 1] but 'light3' can just be
        on(1) or off(0)
5. Key 'monotone' means that just one person is speaking (IN ROOM 1), eg. the boss
6. Finally, the key 'noise' is also varying between [0, 1]
7. The key 'class' can get values from the list: ["close", "edu", "open", "unknown", "working"]
