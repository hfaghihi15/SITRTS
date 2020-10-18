class SituationRule:
    def __init__(self, _id, _name, _operator, _value=None):
        self.name = _name
        self.value = _value
        self.operator = _operator

    def __str__(self):
        return "%s %s %s" % (self.name, self.operator, self.value)

    def rule_definition(self):
        return "%s %s %s" % (self.name, self.operator, self.value)


class OperatorNode:

    def __init__(self, _operator="AND", _conditions=None):
        self.operator = _operator
        self.conditions = _conditions

    def node_definition(self):
        rules = list()
        for i in self.conditions:
            # print(i)
            rules.append(str(i))
        this_condition = (rules, self.operator)
        return this_condition


class SituationNode:
    numReg = []

    def __init__(self, _name, _operator, _operators=None):
        # super().__init__("OR", _operators)
        self.name = _name
        self.operators = _operators
        self.operator = _operator
        self.numReg.append(self)

    def __str__(self):
        return "It's %s there, when: %s" % (self.name, self.operators)

    def situation_definition(self):
        rules = list()
        for i in self.operators:
            rules.append(OperatorNode.node_definition(i))
        all_conditions = tuple(rules) + tuple([self.operator])
        return all_conditions

