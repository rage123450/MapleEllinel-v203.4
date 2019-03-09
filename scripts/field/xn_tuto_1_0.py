# Created by MechAviv
# Map ID :: 931050910
# Peacetime Edelstein : Edelstein Outskirts 2

sm.hideUser(True)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
sm.spawnNpc(2159369, -1050, -30)
sm.showNpcSpecialActionByTemplateId(2159369, "summon", 0)
sm.spawnNpc(2159376, -1800, -30)
sm.showNpcSpecialActionByTemplateId(2159376, "summon", 0)
sm.moveNpcByTemplateId(2159369, True, 300, 100)
sm.moveCamera(False, 80, -1600, -34)


sm.sendDelay(6870)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg0/2", 900, 0, -120, 0, 2159369, False, 0)
sm.sendDelay(810)


sm.setSpeakerID(2159369)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Who is that grandpa? I don't think he's from this town...")


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/6", 900, 0, -120, 0, 2159376, False, 0)
sm.sendDelay(810)


sm.spawnNpc(2159422, -1450, -30)
sm.showNpcSpecialActionByTemplateId(2159422, "summon", 0)
sm.spawnNpc(2159422, -1350, -30)
sm.showNpcSpecialActionByTemplateId(2159422, "summon", 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg1/0", 1200, 0, -120, 0, 2159369, False, 0)
sm.sendDelay(1200)


sm.spawnNpc(2159371, -1400, -30)
sm.showNpcSpecialActionByTemplateId(2159371, "summon", 0)
sm.removeNpc(2159369)
sm.removeNpc(2159422)
sm.removeNpc(2159422)
sm.sendDelay(600)


sm.setSpeakerID(2159376)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Finally, I find what I'm looking for... It's a good thing I looked all over town.")


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/8", 1200, 0, -120, 0, 2159376, False, 0)
sm.sendDelay(900)


sm.moveNpcByTemplateId(2159376, True, 300, 100)
sm.moveNpcByTemplateId(2159371, True, 300, 100)
sm.sendDelay(1500)


sm.spawnNpc(2159372, -500, -30)
sm.showNpcSpecialActionByTemplateId(2159372, "summon", 0)
sm.moveNpcByTemplateId(2159372, True, 200, 100)
sm.moveCamera(False, 150, -950, -34)


sm.sendDelay(4335)


sm.moveNpcByTemplateId(2159372, False, 1, 100)
sm.sendDelay(90)


sm.moveNpcByTemplateId(2159372, True, 1, 100)
sm.sendDelay(90)


sm.moveNpcByTemplateId(2159372, False, 1, 100)
sm.sendDelay(90)


sm.moveNpcByTemplateId(2159372, True, 1, 100)
sm.sendDelay(90)


sm.setSpeakerID(2159372)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Did #h0# already go home? I was going to return the dagger I borrowed.")


sm.setSpeakerID(2159372)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I'll give it back tomorrow.")


sm.moveNpcByTemplateId(2159372, False, 100, 100)
sm.sendDelay(150)


sm.removeNpc(2159376)
sm.removeNpc(2159371)
sm.removeNpc(2159372)
sm.warp(931060080, 0)
