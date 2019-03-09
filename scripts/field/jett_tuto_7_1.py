# Created by MechAviv
# Map ID :: 620100027
# Spaceship : Spaceship Cockpit

sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.completeQuest(5672)
sm.forcedInput(1)
sm.sendDelay(30)


sm.forcedInput(0)
sm.sendDelay(1000)


sm.showEffect("Effect/DirectionNewPirate.img/newPirate/balloonMsg1/20", 2000, 0, -100, -2, -2, False, 0)
sm.sendDelay(2000)


sm.setSpeakerID(9270085)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendNext("You there! Get away from those controls, and drop that key!")


sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.chatScript("Eliminate the Key Keeper and find the Master Key.")
sm.startQuest(5672)