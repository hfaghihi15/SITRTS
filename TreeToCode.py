import numpy as np
import copy


def tree_to_code(input_tree, feature_names):
    left = input_tree.tree_.children_left
    right = input_tree.tree_.children_right
    threshold = input_tree.tree_.threshold
    features = [feature_names[k] for k in input_tree.tree_.feature]
    classLabels = input_tree.classes_
    valuesInEachNode = input_tree.tree_.value

    # get ids of child nodes
    childIndices = np.argwhere(left == -1)[:, 0]
    leafStrengths = list()
    leafPurities = list()

    for child in childIndices:
        leafStrengths.append(valuesInEachNode[child].max())
        purity = round(valuesInEachNode[child].max() / valuesInEachNode[child].sum(), 2)
        leafPurities.append(purity)
    # print(childIndices)
    # print(valuesInEachNode)
    # print(leafStrength)

    def recurse(left, right, child, lineage=None):
        if lineage is None:
            leafClass = classLabels[valuesInEachNode[child].argmax()]
            # leafStrength = valuesInEachNode[child].max()
            # print(leafStrength)
            lineage = [leafClass]
        if child in left:
            parent = np.where(left == child)[0].item()
            splitAnalog = '<='
            splitDiscrete = '= 0'
        else:
            parent = np.where(right == child)[0].item()
            splitAnalog = '>'
            splitDiscrete = '= 1'

        if threshold[parent] != 0.5:
            lineage.append("%s %s %s" % (features[parent], splitAnalog, round(threshold[parent], 3)))
        else:
            lineage.append("%s %s" % (features[parent], splitDiscrete))

        if parent == 0:
            lineage.reverse()
            # print(lineage)
            return lineage
        else:
            return recurse(left, right, parent, lineage)

    leafClasses = list()
    leafRules = list()
    temp1 = list()
    for child in childIndices:
        for node in recurse(left, right, child):
            if node.isalpha():
                leafClasses.append(node)
                temp2 = copy.deepcopy(temp1)
                # print(leafRules)
                leafRules.append(temp2)
                temp1.clear()
            else:
                temp1.append(node)
    return zip(leafRules, leafClasses, leafStrengths, leafPurities)
