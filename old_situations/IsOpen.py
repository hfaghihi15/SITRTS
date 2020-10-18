from SitRS import OperatorNode, SituationNode
import index

open_operator1 = OperatorNode("OR", [index.motion1_holds, index.motion2_holds, index.motion3_holds])
open_operator2 = OperatorNode("AND", [index.existed1_not_holds, index.existed2_not_holds, index.existed3_not_holds])
s_open = SituationNode('open', 'OR', [open_operator1, open_operator2])
