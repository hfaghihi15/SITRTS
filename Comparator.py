from DNF import to_split
import copy
import numpy as np


def comparator(decision_tree, decision_tree_strength, decision_tree_purities, situation_template):

    updated_template = copy.deepcopy(situation_template)
    decision_tree = to_split(decision_tree)
    updated_template = similarity_reformer(decision_tree, situation_template, decision_tree_strength,
                                           decision_tree_purities, updated_template)
    temp = copy.deepcopy(updated_template)
    # print(decision_tree_strength)
    # print(decision_tree_purities)
    if sum(decision_tree_strength) > 100 and min(decision_tree_purities) >= 0.8:
        print('Tree is reliable, deprecated situations will be cleaned:')
        for situation in temp:
            clean_deprecated_situation(updated_template, situation, decision_tree)
    else:
        print('Tree is not reliable, no situation will be cleaned!')

    print('Adding decision tree branches to the situation template:')
    for branch in decision_tree:
        branch_strength = decision_tree_strength[decision_tree.index(branch)]
        branch_purity = decision_tree_purities[decision_tree.index(branch)]

        if branch_strength > 10 and branch_purity > 0.65:
            print('Branch%d is reliable...' % (decision_tree.index(branch)+1))
            add_newly_formed_branch(updated_template, branch)
        else:
            print('Branch%d is not reliable!' % (decision_tree.index(branch)+1))

    print('\n\n')
    print('The initial situation template was: %s' % situation_template, end='\n\n')
    print('The DT was: %s' % decision_tree, end='\n\n')
    print('The updated situation template is: %s' % updated_template, end='\n\n')
    return remove_redundant(updated_template)


def similarity_finder(decision_tree, situation_template):

    matching_points = list()
    similar_tree_branches = list()
    similar_sub_situations = list()

    for situation in situation_template:
        for subTree in decision_tree:
            matching_points.append(similarity_count(subTree, situation))
        # print(matching_points)

        if max(matching_points) >= 0.6:
            print('Founded similar branch for a situation;')
            similar_sub_situations.append(situation)
            similar_tree_branches.append(decision_tree[matching_points.index(max(matching_points))])
        matching_points.clear()

    return similar_sub_situations, similar_tree_branches


def similarity_count(sub_tree, situation):
    count = 0

    for sit_rule in situation:
        has_similar = False

        for tree_rule in sub_tree:

            if tree_rule[1] == '=' and sit_rule[1] == '=':
                if tree_rule[0] == sit_rule[0] and tree_rule[2] == sit_rule[2]:
                    has_similar = True
                    count += 1
                else:
                    pass
            else:
                if tree_rule[0] == sit_rule[0] and tree_rule[1] == sit_rule[1] and abs(tree_rule[2]-sit_rule[2]) < 0.25:
                    has_similar = True
                    count += 1

        if has_similar is False:
            count -= 1

    count = round(count/len(situation), 2)
    return count


def similarity_reformer(decision_tree, situation_template, dt_rule_strength, dt_rule_purity, updated_template):

    similar_sub_situations, similar_tree_branches = similarity_finder(decision_tree, situation_template)

    for s in range(0, len(similar_sub_situations)):

        similar_sub_situation = similar_sub_situations[s]
        similar_tree_branch = similar_tree_branches[s]
        branch_strength = dt_rule_strength[decision_tree.index(similar_tree_branch)]
        branch_purity = dt_rule_purity[decision_tree.index(similar_tree_branch)]

        if branch_strength > 20 and branch_purity > 0.65:
            print('Reliable branch ... added.')
            updated_template.append(similar_tree_branch)
            del updated_template[updated_template.index(similar_sub_situation)]
        else:
            print('Not a reliable branch!')

    return updated_template


def clean_deprecated_situation(updated_template, situation, decision_tree):

    has_similar = False
    # print(situation)
    for branch in decision_tree:
        if branch == situation:
            has_similar = True
    if has_similar is False:
        print('Deprecated situation is removed!')
        del updated_template[updated_template.index(situation)]
    else:
        print('Situation has a similar branch in the decision tree, no need to remove!')
    # has_similar = False


def add_newly_formed_branch(updated_template, branch):
    has_similar = False
    for situation in updated_template:
        if branch == situation:
            has_similar = True
    if has_similar is False:
        print('Branch added to situation template!')
        updated_template.append(branch)
    else:
        print('Branch has a similar situation in the situation template, no need to add!')
    # has_similar = False

def remove_redundant(updated_template) :
    remove_values = []
    for situation in updated_template:
        for situation1 in updated_template:
            if situation == situation1:
                continue
            contained = [a in situation for a in situation1]
            if all(item == True for item in contained):
                if situation1 in remove_values:
                    continue
                remove_values.append(situation1)

    for item in remove_values:
        print(item)
        updated_template.remove(item)

    return updated_template

