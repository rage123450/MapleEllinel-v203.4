# Created by MechAviv
# Map ID :: 620100021
# Spaceship : Captain's Quarters

sm.spawnNpc(9270083, 40, -75)
sm.showNpcSpecialActionByTemplateId(9270083, "summon", 0)
sm.forcedInput(1)
sm.sendDelay(30)


sm.forcedInput(0)
sm.sendDelay(2000)


sm.setSpeakerID(0)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendNext("Forget those idiots. You'er the captain of this crew. We all know that.")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I know. Thanks, Jett.")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("Right, hey, we're gonna party before we make the drop-off. Come on!")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Okay, I'll be there soon.")


sm.forcedInput(2)
