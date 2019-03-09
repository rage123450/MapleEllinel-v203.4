# Created by MechAviv
# Map ID :: 940001100
# Heliseum : Heliseum Outskirts

sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendNext("Heliseum? Darmoor took it. Plain and simple.")


sm.showNpcSpecialActionByTemplateId(3000131, "fake", 0)
sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/1", 0, 0, -110, -2, -2, False, 0)
sm.forcedInput(2)
sm.curNodeEventEnd(True)