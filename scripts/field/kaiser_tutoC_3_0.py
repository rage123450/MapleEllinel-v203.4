# Created by MechAviv
# Map ID :: 940001230
# Eastern Region of Pantheon : East Sanctum

sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.hideUser(True)
sm.spawnNpc(3000142, -100, 220)
sm.showNpcSpecialActionByTemplateId(3000142, "summon", 0)
sm.spawnNpc(3000139, -150, 220)
sm.showNpcSpecialActionByTemplateId(3000139, "summon", 0)
sm.spawnNpc(3000114, 70, 220)
sm.showNpcSpecialActionByTemplateId(3000114, "summon", 0)
sm.spawnNpc(3000111, 130, 220)
sm.showNpcSpecialActionByTemplateId(3000111, "summon", 0)
sm.spawnNpc(3000115, 250, 220)
sm.showNpcSpecialActionByTemplateId(3000115, "summon", 0)
sm.setSpeakerID(3000114)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Wh-What is this...")


sm.setSpeakerID(3000111)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("That kid transformed into this?")


sm.setSpeakerID(3000114)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Looks dangerous...")


sm.showEffect("Effect/Direction9.img/effect/tuto/BalloonMsg0/2", 1200, 0, -200, 0, 3000142, False, 0)
sm.showNpcSpecialActionByTemplateId(3000142, "DKgigaSlasher", 0)
sm.showEffect("Skill/6112.img/skill/61121201/effect", 0, 0, 0, -2, -2, False, 0)
sm.playSound("Kaiser/61121100", 100)
sm.sendDelay(300)


sm.showNpcSpecialActionByTemplateId(3000114, "die1", 0)
sm.showNpcSpecialActionByTemplateId(3000111, "die1", 0)
sm.sendDelay(1500)


sm.removeNpc(3000114)
sm.removeNpc(3000111)
sm.setSpeakerID(3000115)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("W-what is this madness?!")


sm.showFieldEffect("demonSlayer/whiteOut", 0)
sm.sendDelay(1950)


sm.hideUser(False)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.removeNpc(3000142)
sm.removeNpc(3000139)
sm.removeNpc(3000115)
sm.warp(940001240, 0)
