import sys
sys.path.append(sys.path[0] + "\situations")
from situations import IsOpen, IsClose, IsWorking


def tree_to_dnf():
    # output of the decision tree (TreeToCode.py) is basically DNF formed, so there is no need to convert
    # this function is just for more intuition
    pass


def situation_to_dnf(situation):

    situation = list(situation)
    mainOperator = situation[-1]

    if mainOperator == 'OR':
        pass

    situation.pop()
    split_situation = list()
    for this_situation in situation:

        to_split(this_situation[:-1])
        subOperator = this_situation[-1]

        if subOperator == 'AND':
            split_situation.append(list(this_situation[:-1]).pop())
        else:
            for temp in this_situation[:-1]:
                for rule in temp:
                    make_reverse(rule)
            split_situation.append(list(this_situation[:-1]).pop())

    return split_situation


def to_split(input_structure):
    for element in input_structure:
        for i in range(len(element)):
            element[i] = element[i].split()
            element[i][2] = float(element[i][2])
    return input_structure


def make_reverse(rule):

    if rule[2] == 1.0:
        rule[2] = 0.0
    elif rule[2] == 0.0:
        rule[2] = 1.0
    else:
        if rule[1] == '<=':
            rule[1] = '>'
        elif rule[1] == '>':
            rule[1] = '<='


# temp = situation_to_dnf(IsWorking.s_working.situation_definition())
# print(temp)
# print(IsWorking.s_working.situation_definition())
