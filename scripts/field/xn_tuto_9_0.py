# Created by MechAviv
# Map ID :: 931050970
# Classified Lab : Corridor

sm.forcedInput(0)
sm.sendDelay(30)


sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
sm.spawnNpc(2159381, -1700, 20)
sm.showNpcSpecialActionByTemplateId(2159381, "summon", 0)
sm.spawnNpc(2159384, -1600, 20)
sm.showNpcSpecialActionByTemplateId(2159384, "summon", 0)
sm.setSpeakerID(2159381)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("This corridor leads to the Silo, and outside. We're going to run into a lot of Guard Robots on the way.")


sm.setSpeakerID(2159381)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("I will handle them. Don't worry.")


sm.setSpeakerID(2159384)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I'm afraid I'm not going to be much use in a fight with this injured arm... Are you sure about this?")


sm.setSpeakerID(2159384)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("Let's give it a try.")


sm.moveNpcByTemplateId(2159381, False, 2200, 100)
sm.moveNpcByTemplateId(2159384, False, 2200, 100)
sm.sendDelay(2100)


sm.chatScript("Press the CTRL key to attack. Defeat any monsters that block your path.")
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)