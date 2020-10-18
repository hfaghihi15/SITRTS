from SitRS import OperatorNode, SituationNode
import index

edu_operator1 = OperatorNode("AND", [index.existed1_holds, index.motion1_holds, index.monotone_on, index.light1_bigger,])
edu_operator2 = OperatorNode("AND", [index.existed1_holds, index.motion1_holds, index.monotone_on])
edu_operator3 = OperatorNode("AND", [index.existed1_holds, index.motion1_holds, index.monotone_on,  index.noise_smaller])
s_edu = SituationNode('working', "OR", [edu_operator1, edu_operator2, edu_operator3])
