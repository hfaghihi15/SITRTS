import operator


def calculate_accuracy(situation_data, situation_label, test_data, test_labels):

    correct = 0
    total = 0
    count = 0
    total1 = 0
    tn = 0
    tp = 0
    fp = 0
    fn = 0


    for k in test_labels:
        if k == situation_label:
            total += 1

    other_totals = len(test_labels) - total

    for k in range(0, len(test_labels)):
        if test_labels[k] == situation_label:
            for situation in situation_data:
                # print(situation)
                for rule in situation:
                    # print(rule)
                    if get_truth(test_data[k][rule[0]], rule[1], rule[2]):
                        count += 1
                if count == len(situation):
                    correct += 1
                    tp += 1
                    count = 0
                    break
                count = 0

    for k in range(0, len(test_labels)):
        if test_labels[k] != situation_label:
            for situation in situation_data:
                # print(situation)
                for rule in situation:
                    # print(rule)
                    if get_truth(test_data[k][rule[0]], rule[1], rule[2]):
                        count += 1
                if count != len(situation):
                    tn += 1
                    count = 0
                    break
                count = 0

    for k in range(0, len(test_labels)):
        for situation in situation_data:
            for rule in situation:
                if get_truth(test_data[k][rule[0]], rule[1], rule[2]):
                    count += 1
            if count == len(situation):
                total1 += 1
                if test_labels[k] != situation_label :
                    fp += 1
                count = 0
                break
            count = 0

    # print(total1)
    # print(tp)
    # print(total1-fp)
    fn = total - tp
    accuracy = [0, 0, 0]
    try:
        accuracy[0] = str(((tp + tn) / len(test_labels)) * 100)#accuracy
        accuracy[1] = str((tp / (tp + fp)) * 100) #precision
        accuracy[2] = str((tp / (tp + fn)) * 100) #recall
    except:
        total = 1
        accuracy[0] = str(((tp + tn) / len(test_labels)) * 100) # accuracy
        accuracy[1] = str((tp / (tp + fp)) * 100)# precision
        accuracy[2] = str((tp / (tp + fn)) * 100) #recall
    return accuracy


def get_truth(inp, relate, cut):
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '=': operator.eq}
    return ops[relate](inp, cut)
