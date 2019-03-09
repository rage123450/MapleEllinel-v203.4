# Created by MechAviv
# Map ID :: 620100020
# Spaceship : Corridor

sm.spawnNpc(9201276, 40, -131)
sm.showNpcSpecialActionByTemplateId(9201276, "summon", 0)
sm.spawnNpc(9201277, -270, -131)
sm.showNpcSpecialActionByTemplateId(9201277, "summon", 0)
sm.spawnNpc(9201278, -170, -131)
sm.showNpcSpecialActionByTemplateId(9201278, "summon", 0)
sm.spawnNpc(9201279, -90, -131)
sm.showNpcSpecialActionByTemplateId(9201279, "summon", 0)
sm.spawnNpc(9270083, 150, -131)
sm.showNpcSpecialActionByTemplateId(9270083, "summon", 0)
sm.showFieldEffect("newPirate/text4", 0)
sm.sendDelay(1900)


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Good work, team. All of you together were able to bring in the whole group.")


sm.sendDelay(1000)


sm.setSpeakerID(9201276)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Whatever, Burke! You're nothing without that loser with the Core. That's the only reason you had a chance!")


sm.setSpeakerID(9201276)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("Man, shut your face. I don't want to rough you up before we turn you in. Lock them up and keep an eye on them!")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Roger that, chief.")


sm.sendDelay(1200)


sm.removeNpc(9201276)
sm.removeNpc(9201277)
sm.removeNpc(9201278)
sm.removeNpc(9201279)
sm.removeNpc(9270083)
sm.warp(620100021, 0)
