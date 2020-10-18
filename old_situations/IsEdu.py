from SitRS import OperatorNode, SituationNode
import index

edu_operator1 = OperatorNode("OR", [index.monotone_on, index.light1_bigger, index.noise_smaller])
edu_operator2 = OperatorNode("AND", [index.existed1_holds, index.motion1_holds])
edu_operator3 = OperatorNode("OR", [index.light2_smaller, index.light3_off,
                                    index.motion1_holds, index.motion3_not_holds])
s_edu = SituationNode('working', "OR", [edu_operator1, edu_operator2, edu_operator3])
