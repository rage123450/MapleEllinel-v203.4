# Created by MechAviv
# Map ID :: 620100026
# Spaceship : In Front of the Shuttle

sm.giveSkill(228, 1, 1)
sm.completeQuest(5671)
sm.completeQuest(5672)
sm.completeQuest(5758)
sm.spawnNpc(9270083, 430, -131)
sm.showNpcSpecialActionByTemplateId(9270083, "summon", 0)
sm.forcedInput(1)
sm.sendDelay(30)


sm.forcedInput(0)
sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("The guardsmen are already here! Does this mean our crew is...")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("No... They were good people! I'm innocent! WHY CAN'T YOU SEE THAT?!")


sm.showEffect("Effect/DirectionNewPirate.img/newPirate/balloonMsg1/3", 2000, 0, -80, -2, -2, False, 0)
sm.sendDelay(500)


sm.showEffect("Effect/DirectionNewPirate.img/newPirate/attack_tuto", 3000, 0, -200, -2, -2, False, 0)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.chatScript("Eliminate all Guards.")
sm.startQuest(5671)