# Created by MechAviv
# Map ID :: 931050960
# Classified Lab : Prison

sm.forcedInput(0)
sm.sendDelay(30)


sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
sm.spawnNpc(2159380, 450, 180)
sm.showNpcSpecialActionByTemplateId(2159380, "summon", 0)
sm.spawnNpc(2159384, 700, 180)
sm.showNpcSpecialActionByTemplateId(2159384, "summon", 0)
sm.sendSessionValue("luti", 2159380)
sm.sendSessionValue("sig", 2159384)
sm.sendDelay(300)


sm.forcedInput(2)
