# Created by MechAviv
# Map ID :: 940001220
# Eastern Region of Pantheon : East Sanctum

sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
sm.spawnNpc(3000139, -150, 220)
sm.showNpcSpecialActionByTemplateId(3000139, "summon", 0)
sm.spawnNpc(3000110, -20, 220)
sm.showNpcSpecialActionByTemplateId(3000110, "summon", 0)
sm.spawnNpc(3000114, 70, 220)
sm.showNpcSpecialActionByTemplateId(3000114, "summon", 0)
sm.spawnNpc(3000111, 130, 220)
sm.showNpcSpecialActionByTemplateId(3000111, "summon", 0)
sm.spawnNpc(3000115, 250, 220)
sm.showNpcSpecialActionByTemplateId(3000115, "summon", 0)
sm.sendSessionValue("enemy0", 3000110)
sm.sendSessionValue("enemy1", 3000114)
sm.sendSessionValue("enemy2", 3000111)
sm.sendSessionValue("enemy3", 3000115)
sm.setSpeakerID(3000110)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Eh? A child dares to interfere?")


sm.setSpeakerID(3000110)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("Tear, wait!")


sm.setSpeakerID(3000110)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("These kids are fearless. A pity we cannot allow any witnesses to escape.")


sm.setSpeakerID(3000110)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("You think you can take me down? Bring it!")


sm.setSpeakerID(3000114)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Ha! What can you do all by yourself?")


sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/0", 1200, 0, -120, -2, -2, False, 0)
sm.forcedInput(2)
