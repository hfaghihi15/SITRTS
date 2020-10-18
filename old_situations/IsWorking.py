from SitRS import OperatorNode, SituationNode
import index

working_operator1 = OperatorNode("OR", [index.monotone_off, index.light3_on, index.noise_bigger])
working_operator2 = OperatorNode("AND", [index.existed1_holds, index.motion1_holds])
working_operator3 = OperatorNode("OR", [index.light2_smaller, index.existed2_holds, index.noise_smaller,
                                        index.motion1_not_holds])
s_working = SituationNode('working', 'OR', [working_operator1, working_operator2, working_operator3])

