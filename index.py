from Sensor import Sensor, SensorShot
from SitRS import SituationRule

sensor1 = Sensor('existed1')
sensor2 = Sensor('existed2')
sensor3 = Sensor('existed3')
sensor4 = Sensor('motion1')
sensor5 = Sensor('motion2')
sensor6 = Sensor('motion3')
sensor7 = Sensor('TV')
sensor8 = Sensor('light1')
sensor9 = Sensor('light2')
sensor10 = Sensor('light3')
sensor11 = Sensor('monotone')
sensor12 = Sensor('noise')

light1_shot = SensorShot('light1', 0.23)
light2_shot = SensorShot('light2', 0.88)
noise_shot = SensorShot('noise', 0.20)


motion1_holds = SituationRule(1, 'motion1', '=', 1)
motion1_not_holds = SituationRule(2, 'motion1', '=', 0)
motion2_holds = SituationRule(3, 'motion2', '=', 1)
motion2_not_holds = SituationRule(4, 'motion2', '=', 0)
motion3_holds = SituationRule(5, 'motion3', '=', 1)
motion3_not_holds = SituationRule(6, 'motion3', '=', 0)

existed1_holds = SituationRule(7, 'existed1', '=', 1)
existed1_not_holds = SituationRule(8, 'existed1', '=', 0)
existed2_holds = SituationRule(9, 'existed2', '=', 1)
existed2_not_holds = SituationRule(10, 'existed2', '=', 0)
existed3_holds = SituationRule(11, 'existed3', '=', 1)
existed3_not_holds = SituationRule(12, 'existed3', '=', 0)

TV_on = SituationRule(13, 'TV', '=', '1')
TV_off = SituationRule(14, 'TV', '=', '0')

light1_smaller = SituationRule(15, 'light1', '<=', light1_shot.value)
light1_bigger = SituationRule(16, 'light1', '>', light1_shot.value)

light2_smaller = SituationRule(17, 'light2', '<=', light2_shot.value)
light2_bigger = SituationRule(18, 'light2', '>', light2_shot.value)

light3_on = SituationRule(19, 'light3', '=', '1')
light3_off = SituationRule(20, 'light3', '=', '0')

monotone_on = SituationRule(21, 'monotone', '=', '1')
monotone_off = SituationRule(22, 'monotone', '=', '0')

noise_smaller = SituationRule(23, 'noise', '<=', noise_shot.value)
noise_bigger = SituationRule(24, 'noise', '>', noise_shot.value)

