import numpy as np
import json
import graphviz
from sklearn import tree
from sklearn.tree import _tree
from TreeToCode import tree_to_code
from TrainTestSplitter import train_test_splitter

train_test_splitter()
with open('training-set.json', 'r') as f:
    data = json.load(f)

X = []
Y = []
names = ["existed1", "existed2", "existed3", "motion1", "motion2", "motion3", "TV", "light1", "light2", "light3",
         "monotone", "noise"]
classes = ["close", "edu", "open", "unknown", "working"]
for i in data:
    X.append(list(i.values())[:-1])
    Y.append(list(i.values())[-1])


# X = [[0, 0], [1, 1]]
# Y = [0, 1]
clf = tree.DecisionTreeClassifier(criterion="entropy", min_impurity_decrease=0.015)
# some of arguments which could be used for pruning the tree:
min_impurity_decrease=0.015
# min_samples_leaf = 20
min_samples_split = 30
# min_weight_fraction_leaf=0.05
clf = clf.fit(X, Y)

# pred = clf.predict(X)
# from sklearn.metrics import accuracy_score
# acc = accuracy_score(pred, Y)
# print(acc)

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=names, filled=True, rounded=True,
                                class_names=classes, special_characters=True)

graph = graphviz.Source(dot_data)
graph.render("DT")

# accessing low level attributes of decision tree via tree_ (intuition)
#
# numOfNodes = clf.tree_.node_count
# feature = clf.tree_.feature
# threshold = clf.tree_.threshold
# children_left = clf.tree_.children_left
# childIndices = np.argwhere(children_left == -1)[:, 0]
# children_right = clf.tree_.children_right
# classLabels = clf.classes_
# valuesInEachNode = clf.tree_.value
# #
# node_indicator = clf.decision_path(X)
# print(numOfNodes)
# print(feature)
# print(threshold)
# print(children_left)
# print(children_right)
# print(classLabels)
# print(valuesInEachNode)


# implementation method one: high-level sentences with indents
#
# # part one: finding out whether any node is leaf or not
# node_depth = np.zeros(shape=numOfNodes, dtype=np.int64)
# is_leaf = np.zeros(shape=numOfNodes, dtype=bool)
# stack = [(0, -1)]
# while len(stack) > 0:
#     node_id, parent_depth = stack.pop()
#     node_depth[node_id] = parent_depth + 1
#
#     if children_left[node_id] != children_right[node_id]:
#         stack.append((children_left[node_id], parent_depth + 1))
#         stack.append((children_right[node_id], parent_depth + 1))
#     else:
#         is_leaf[node_id] = True
#
# # part two: printing tree structure in words and sentences
# for i in range(numOfNodes):
#     if is_leaf[i]:
#         leafClass = classLabels[valuesInEachNode[i].argmax()]
#         print("%s node=%s leaf node And its class is %s" % (node_depth[i] * "\t", i, leafClass))
#     else:
#         print("%snode=%s middle node: go to node %s if %s <= %s else to node %s"
#               % (node_depth[i] * "\t", i, children_left[i], names[feature[i]], round(threshold[i], 3),
#                  children_right[i]))


print("------------------------------------------")


# implementation method two: IF-THEN rules with indents
#
#
# def tree_visualizer(input_tree, feature_names):
#     tree_ = input_tree.tree_
#     feature_name = [feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!" for i in tree_.feature]
#     print("def tree({}):".format(", ".join(feature_names)))
#
#     def recurse(node, depth):
#         indent = "  " * depth
#         if tree_.feature[node] != _tree.TREE_UNDEFINED:
#             name = feature_name[node]
#             threshold = round(tree_.threshold[node], 3)
#             print("{}if {} <= {}:".format(indent, name, threshold))
#             recurse(tree_.children_left[node], depth + 1)
#             print("{}else:  # if {} > {}".format(indent, name, threshold))
#             recurse(tree_.children_right[node], depth + 1)
#         else:
#             leafClass = classLabels[valuesInEachNode[node].argmax()]
#             print("{}return {}".format(indent, leafClass))
#     recurse(0, 1)
#
#
# tree_visualizer(clf, names)


print("------------------------------------------")


# implementation method three: extracting each branch's decision path as a tuple of rules & labels

decisionPaths = tree_to_code(clf, names)
rules, labels, strengths, purities = zip(*decisionPaths)

# extracting rules for each situation in a separate list

openRules = list()
openRuleStrength = list()
openRulePurities = list()

closeRules = list()
closeRuleStrength = list()
closeRulePurities = list()

eduRules = list()
eduRuleStrength = list()
eduRulePurities = list()

workingRules = list()
workingRuleStrength = list()
workingRulePurities = list()

unknownRules = list()
unknownRuleStrength = list()
unknownRulePurities = list()

openIndices = [ind for ind, arg in enumerate(labels) if arg == 'open']
closeIndices = [ind for ind, arg in enumerate(labels) if arg == 'close']
eduIndices = [ind for ind, arg in enumerate(labels) if arg == 'edu']
workingIndices = [ind for ind, arg in enumerate(labels) if arg == 'working']
unknownIndices = [ind for ind, arg in enumerate(labels) if arg == 'unknown']

for ind in openIndices:
    openRules.append(rules[ind])
    openRuleStrength.append(strengths[ind])
    openRulePurities.append(purities[ind])
for ind in closeIndices:
    closeRules.append(rules[ind])
    closeRuleStrength.append(strengths[ind])
    closeRulePurities.append(purities[ind])
for ind in eduIndices:
    eduRules.append(rules[ind])
    eduRuleStrength.append(strengths[ind])
    eduRulePurities.append(purities[ind])
for ind in workingIndices:
    workingRules.append(rules[ind])
    workingRuleStrength.append(strengths[ind])
    workingRulePurities.append(purities[ind])
for ind in unknownIndices:
    unknownRules.append(rules[ind])
    unknownRuleStrength.append(strengths[ind])
    unknownRulePurities.append(purities[ind])

# print(closeRuleStrength)
# print(openIndices)
# print(strengths)
# print(unknownRules)
# print(eduRules)
# print(openRules)
