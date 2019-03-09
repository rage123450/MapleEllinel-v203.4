# Created by MechAviv
# Map ID :: 931060060
# Classified Lab : Silo

sm.forcedInput(0)
sm.sendDelay(30)


sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
sm.spawnNpc(2159381, -1040, 20)
sm.showNpcSpecialActionByTemplateId(2159381, "summon", 0)
sm.spawnNpc(2159384, -990, 20)
sm.showNpcSpecialActionByTemplateId(2159384, "summon", 0)
sm.spawnNpc(2159379, -780, 20)
sm.showNpcSpecialActionByTemplateId(2159379, "summon", 0)
sm.spawnNpc(2159385, -470, 20)
sm.showNpcSpecialActionByTemplateId(2159385, "summon", 0)
sm.spawnNpc(2159386, -550, 20)
sm.showNpcSpecialActionByTemplateId(2159386, "summon", 0)
sm.spawnNpc(2159387, -370, 20)
sm.showNpcSpecialActionByTemplateId(2159387, "summon", 0)
sm.spawnNpc(2159388, -620, 20)
sm.showNpcSpecialActionByTemplateId(2159388, "summon", 0)
sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/17", 2400, -500, -130, 0, 0, True, 0)
sm.sendDelay(2400)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/18", 1500, 0, -145, 0, 2159385, False, 0)
sm.sendDelay(1380)


sm.setSpeakerID(2159384)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("The cavalry is here!")


sm.setSpeakerID(2159387)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Save the hugs for later, Claudine. We've gotta get you out of here first!")


sm.showNpcSpecialActionByTemplateId(2159387, "shoot", 0)
sm.sendDelay(720)


sm.showEffect("Effect/Direction12.img/effect/tuto/smogStart", 0, -370, 20, 0, 0, True, 0)
sm.sendDelay(1050)


sm.showEffect("Effect/Direction12.img/effect/tuto/smog", 3900, -370, 20, 0, 0, True, 0)
sm.sendDelay(1500)


sm.removeNpc(2159381)
sm.removeNpc(2159384)
sm.removeNpc(2159385)
sm.removeNpc(2159386)
sm.removeNpc(2159387)
sm.removeNpc(2159388)
sm.hideUser(True)
sm.sendDelay(2220)


sm.showEffect("Effect/Direction12.img/effect/tuto/smogEnd", 0, -370, 20, 0, 0, True, 0)
sm.sendDelay(420)


sm.sendDelay(600)


sm.sendDelay(600)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg0/1", 1200, 0, -120, 0, 2159379, False, 0)
sm.sendDelay(1200)


sm.removeNpc(2159379)
sm.warp(931060070, 0)
