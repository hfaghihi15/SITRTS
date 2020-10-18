from SitRS import OperatorNode, SituationNode
import index

working_operator1 = OperatorNode("AND", [index.existed1_holds, index.motion1_holds, index.noise_smaller ])
working_operator2 = OperatorNode("AND", [index.existed2_holds, index.motion2_holds, index.light2_bigger ])
working_operator3 = OperatorNode("AND", [index.existed1_holds, index.motion1_holds, index.light1_bigger ])

s_working = SituationNode('working', 'OR', [working_operator1, working_operator2, working_operator3])

