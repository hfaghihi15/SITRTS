from SitRS import OperatorNode, SituationNode
import index

close_operator1 = OperatorNode("AND", [index.motion1_not_holds, index.motion2_not_holds, index.motion3_not_holds])
close_operator2 = OperatorNode("OR", [index.existed1_holds, index.existed2_holds, index.existed3_holds])
s_close = SituationNode('close', 'OR', [close_operator1, close_operator2])

# print(type(s_close))
