from graphviz import Digraph
import os

# tmp = [[['existed1', '=', 0], ['existed3', '=', 0], ['monotone', '=', 1]],
#        [['existed1', '=', 0], ['motion2', '=', 1], ['existed2', '=', 0], ['existed3', '=', 0], ['noise', '<=', 0.45]],
#        [['existed1', '=', 0], ['motion3', '=', 1], ['existed2', '=', 0]],
#        [['TV', '=', 0], ['monotone', '=', 0], ['existed3', '=', 1], ['motion2', '=', 0], ['existed1', '=', 1]],
#        [['light1', '>', 0.5], ['light2', '<=', 0.24]]]


def tree_plotter(tree, tree_name, tree_label):

    directory = 'data trees/'
    file_comment = 'The data tree for %s label:' % tree_label
    i = 0

    # If the compiler raised any error about unable to rewrite existing files, uncomment next few lines:
    # directory_files = os.listdir(directory)
    # for file in directory_files:
    #     path = directory + file
    #     os.remove(path)

    dot = Digraph(comment=file_comment)
    dot.node(name='0', label=tree_label)
    dot.node(name='1', label='OR')
    dot.edge('0', '1', constraint='True')

    for branch in tree:

        branch_name = str(tree.index(branch) + 2)
        dot.node(name=branch_name, label='AND')
        dot.edge('1', branch_name, constraint='True')
        # i -= 1
        for rule in branch:
            rule_name = str(int(branch_name) + branch.index(rule) + len(tree) + i)
            rule[2] = str(rule[2])
            rule_label = ' '.join(rule)
            dot.node(name=rule_name, label=rule_label)
            dot.edge(branch_name, rule_name, constraint='True')
            # i += 1
        i += len(branch)-1

    dot.format = 'PNG'
    dot.render(directory=directory, view=False, filename=tree_name)


# tree_plotter(tmp, 'tmp', 'working')
