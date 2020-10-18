import DecisionTree
import json
import Comparator

from AccuracyCalculator import calculate_accuracy
from TrainTestSplitter import train_test_splitter
from situations import IsOpen, IsClose, IsWorking, IsEdu
from DNF import situation_to_dnf
from sklearn.metrics import accuracy_score, classification_report
from TreePlotter import tree_plotter


# temp_situation_open = [[['existed1', '=', 0.0], ['motion1', '=', 1.0], ['existed2', '=', 0.0], ['existed3', '=', 0.0]],
#                        [['existed1', '=', 0.0], ['motion2', '=', 1.0], ['existed2', '=', 0.0], ['existed3', '=', 0.0]],
#                        [['existed1', '=', 0.0], ['motion3', '=', 1.0], ['existed2', '=', 0.0], ['existed3', '=', 0.0]]]

temp_situation_open = [[['existed1', '=', 0.0], ['motion1', '=', 1.0]],
                       [['existed2', '=', 0.0], ['motion2', '=', 1.0]],
                       [['existed3', '=', 0.0], ['motion3', '=', 1.0]]]


temp_situation_close = [[['motion1', '=', 0.0], ['existed1', '=', 0.0], ['existed3', '=', 1.0]],
                        [['existed1', '=', 1.0], ['motion2', '=', 0.0], ['motion1', '=', 0.0]],
                        [['motion1', '=', 0.0]]]

temp_situation_working = [[['monotone', '=', 0.0], ['light1', '>', 0.4], ['noise', '<=', 0.3]],
                          [['existed1', '=', 1.0], ['motion1', '=', 1.0], ['noise', '<=', 0.3]],
                          [['light2', '>', 0.5], ['existed2', '=', 1.0], ['motion2', '=', 1.0]]]

temp_situation_edu = [[['existed1', '=', 1.0],['TV', '=', 1.0], ['motion1', '=', 1.0]],
                      [['existed1', '=', 1.0], ['monotone', '=', 1.0], ['motion1', '=', 1.0]]
                      ]
# temp_situation_open = situation_to_dnf(IsOpen.s_open.situation_definition())
# temp_situation_close = situation_to_dnf(IsClose.s_close.situation_definition())
# temp_situation_working = situation_to_dnf(IsWorking.s_working.situation_definition())
# temp_situation_edu = situation_to_dnf(IsEdu.s_edu.situation_definition())


def main():

    print('updating situation templates ...')
    print('__________________')
    print("Analyzing for 'open' class: ")
    updated_situation_open = Comparator.comparator(DecisionTree.openRules, DecisionTree.openRuleStrength,
                                                   DecisionTree.openRulePurities, temp_situation_open)
    # return 0
    print('__________________')
    print("Analyzing for 'close' class: ")
    updated_situation_close = Comparator.comparator(DecisionTree.closeRules, DecisionTree.closeRuleStrength,
                                                    DecisionTree.closeRulePurities, temp_situation_close)
    print('__________________')
    print("Analyzing for 'working' class: ")
    updated_situation_working = Comparator.comparator(DecisionTree.workingRules, DecisionTree.workingRuleStrength,
                                                      DecisionTree.workingRulePurities, temp_situation_working)
    print('__________________')
    print("Analyzing for 'edu' class: ")
    updated_situation_edu = Comparator.comparator(DecisionTree.eduRules, DecisionTree.eduRuleStrength,
                                                  DecisionTree.eduRulePurities, temp_situation_edu)
    print('__________________')
    print('situation templates updated!')
    print('__________________')

    accuracy = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0],[0, 0, 0]]
    tree_accuracy = [0, 0, 0, 0]
    iterations = 1

    for number in range(iterations):

        train_test_splitter()
        with open('test-set.json', 'r') as file:
            testData = json.load(file)
        file.close()

        X = []
        X1 = []
        Y = []
        Y1 = []

        x_open = list()
        y_open = list()
        x_close = list()
        y_close = list()
        x_working = list()
        y_working = list()
        x_edu = list()
        y_edu = list()

        for i in testData:
            data = list(i.values())[:-1]
            data_dict = {}
            for j in i.keys():
                if not j == 'class':
                    data_dict[j] = i[j]
            label = list(i.values())[-1]
            X.append(data_dict)
            Y.append(label)
            X1.append(data)
            Y1.append(label)
            if label == 'open':
                x_open.append(data)
                y_open.append('open')
            elif label == 'close':
                x_close.append(data)
                y_close.append('close')
            elif label == 'working':
                x_working.append(data)
                y_working.append('working')
            elif label == 'edu':
                x_edu.append(data)
                y_edu.append('edu')

        acc_open_initial = calculate_accuracy(temp_situation_open, 'open', X, Y)
        acc_open_updated = calculate_accuracy(updated_situation_open, 'open', X, Y)
        # accuracy[0] += acc_open_initial
        accuracy[0] = acc_open_initial
        # accuracy[1] += acc_open_updated
        accuracy[1] = acc_open_updated

        acc_close_initial = calculate_accuracy(temp_situation_close, 'close', X, Y)
        acc_close_updated = calculate_accuracy(updated_situation_close, 'close', X, Y)
        accuracy[2] = acc_close_initial
        # accuracy[2] += acc_close_initial
        # accuracy[3] += acc_close_updated
        accuracy[3] = acc_close_updated

        acc_working_initial = calculate_accuracy(temp_situation_working, 'working', X, Y)
        acc_working_updated = calculate_accuracy(updated_situation_working, 'working', X, Y)
        # accuracy[4] += acc_working_initial
        accuracy[4] = acc_working_initial
        # accuracy[5] += acc_working_updated
        accuracy[5] = acc_working_updated

        acc_edu_initial = calculate_accuracy(temp_situation_edu, 'edu', X, Y)
        acc_edu_updated = calculate_accuracy(updated_situation_edu, 'edu', X, Y)
        accuracy[6] = acc_edu_initial
        # accuracy[6] += acc_edu_initial
        # accuracy[7] += acc_edu_updated
        accuracy[7] = acc_edu_updated

        pred_open = DecisionTree.clf.predict(x_open)
        tree_acc_open = accuracy_score(y_open, pred_open)
        pred_tree = DecisionTree.clf.predict(X1)
        print()
        DecisionTree_prediction = classification_report(Y1, pred_tree, output_dict=True) #the metrics of decision tree
        tree_accuracy[0] += tree_acc_open

        pred_close = DecisionTree.clf.predict(x_close)
        tree_acc_close = accuracy_score(y_close, pred_close)
        tree_accuracy[1] += tree_acc_close

        pred_working = DecisionTree.clf.predict(x_working)
        tree_acc_working = accuracy_score(y_working, pred_working)
        tree_accuracy[2] += tree_acc_working

        pred_edu = DecisionTree.clf.predict(x_edu)
        tree_acc_edu = accuracy_score(y_edu, pred_edu)
        tree_accuracy[3] += tree_acc_edu

    # print("The average SitRS accuracy for 'open' situation is: %.2f" % (accuracy[0]/iterations))
    print(" Situation Open, SITRS accuracy : " + accuracy[0][0] + " precision : " + accuracy[0][1] + " Recall : " + accuracy[0][2])
    # print("The average SitRTS accuracy for 'open' situation is: %.2f" % (accuracy[1]/iterations))
    print(" Situation Open, SITRTS accuracy : " + accuracy[1][0] + " precision : " + accuracy[1][1] + " Recall : " + accuracy[1][2])
    print()
    # print("The average SitRS accuracy for 'close' situation is: %.2f" % (accuracy[2] / iterations))
    print(" Situation Close, SITRS accuracy : " + accuracy[2][0] + " precision : " + accuracy[2][1] + " Recall : " + accuracy[2][2])
    # print("The average SitRTS accuracy for 'close' situation is: %.2f" % (accuracy[3] / iterations))
    print(" Situation Close, SITRTS accuracy : " + accuracy[3][0] + " precision : " + accuracy[3][1] + " Recall : " + accuracy[3][2])
    print()
    # print("The average SitRS accuracy for 'working' situation is: %.2f" % (accuracy[4] / iterations))
    print(" Situation WORK, SITRS accuracy : " + accuracy[4][0] + " precision : " + accuracy[4][1] + " Recall : " + accuracy[4][2])
    # print("The average SitRTS accuracy for 'working' situation is: %.2f" % (accuracy[5] / iterations))
    print(" Situation WORK, SITRTS accuracy : " + accuracy[5][0] + " precision : " + accuracy[5][1] + " Recall : " + accuracy[5][2])
    print()
    # print("The average SitRS accuracy for 'edu' situation is: %.2f" % (accuracy[6] / iterations))
    print(" Situation EDU, SITRS accuracy : " + accuracy[6][0] + " precision : " + accuracy[6][1] + " Recall : " + accuracy[6][2])
    # print("The average SitRTS accuracy for 'edu' situation is: %.2f" % (accuracy[7] / iterations))
    print(" Situation EDU, SITRTS accuracy : " + accuracy[7][0] + " precision : " + accuracy[7][1] + " Recall : " + accuracy[7][2])

    print()
    # print("The average DT accuracy for 'open' situation: %.2f" % ((tree_accuracy[0] / iterations)*100))
    print(" Situation Open, DT accuracy : " + str(tree_accuracy[0] * 100) +
          " precision : " + str(DecisionTree_prediction['open']['precision'])
          + " Recall : " + str(DecisionTree_prediction['open']['recall']))
    print()
    # print("The average DT accuracy for 'close' situation: %.2f" % ((tree_accuracy[1] / iterations)*100))
    print(" Situation Close, DT accuracy : " + str(tree_accuracy[1] * 100) +
          " precision : " + str(DecisionTree_prediction['close']['precision'])
          + " Recall : " + str(DecisionTree_prediction['close']['recall']))
    print()
    # print("The average DT accuracy for 'working' situation: %.2f" % ((tree_accuracy[2] / iterations)*100))
    print(" Situation Working, DT accuracy : " + str(tree_accuracy[2] * 100) +
          " precision : " + str(DecisionTree_prediction['working']['precision'])
          + " Recall : " + str(DecisionTree_prediction['working']['recall']))
    print()
    # print("The average DT accuracy for 'edu' situation: %.2f" % ((tree_accuracy[3] / iterations)*100))
    print(" Situation EDU, DT accuracy : " + str(tree_accuracy[3] * 100) +
          " precision : " + str(DecisionTree_prediction['edu']['precision'])
          + " Recall : " + str(DecisionTree_prediction['edu']['recall']))
    print('______________')
    print('Drawing simple data trees for situations:')
    print('...')

    tree_plotter(temp_situation_open, 'temp_situation_open', 'open')
    tree_plotter(updated_situation_open, 'updated_situation_open', 'open')
    tree_plotter(temp_situation_close, 'temp_situation_close', 'close')
    tree_plotter(updated_situation_close, 'updated_situation_close', 'close')
    tree_plotter(temp_situation_working, 'temp_situation_working', 'working')
    tree_plotter(updated_situation_working, 'updated_situation_working', 'working')
    tree_plotter(temp_situation_edu, 'temp_situation_edu', 'edu')
    tree_plotter(updated_situation_edu, 'updated_situation_edu', 'edu')

    print('...')
    print('Data trees are plotted and saved in the /data trees/ directory.')
    print('Totally Finished!')


if __name__ == '__main__':
    main()
