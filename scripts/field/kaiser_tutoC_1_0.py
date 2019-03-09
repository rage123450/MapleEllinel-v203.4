# Created by MechAviv
# Map ID :: 940001210
# Eastern Region of Pantheon : East Sanctum

sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
sm.spawnNpc(3000103, -300, 220)
sm.showNpcSpecialActionByTemplateId(3000103, "summon", 0)
sm.spawnNpc(3000104, -450, 220)
sm.showNpcSpecialActionByTemplateId(3000104, "summon", 0)
sm.spawnNpc(3000110, -120, 220)
sm.showNpcSpecialActionByTemplateId(3000110, "summon", 0)
sm.spawnNpc(3000114, -100, 220)
sm.showNpcSpecialActionByTemplateId(3000114, "summon", 0)
sm.spawnNpc(3000111, 130, 220)
sm.showNpcSpecialActionByTemplateId(3000111, "summon", 0)
sm.spawnNpc(3000115, 250, 220)
sm.showNpcSpecialActionByTemplateId(3000115, "summon", 0)
sm.setSpeakerID(3000104)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Nothing here, big surprise...")


sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/3", 1200, 0, -120, 0, 3000104, False, 0)
sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/3", 1200, 0, -120, -2, -2, False, 0)
sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/4", 1200, 0, -120, 0, 3000103, False, 0)
sm.sendDelay(1200)


sm.setSpeakerID(3000103)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Well, those priests are keeping busy. It's funny, though...I don't recognize any of them.")


sm.setSpeakerID(3000103)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("Shhh! Something is not right. Velderoth!")


sm.setSpeakerID(3000104)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("You're right. They look suspicious. I'm going to run back to base and get help. You two stay here and keep an eye on them, okay? But no heroics. You get out of here if they spot you.")


sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg0/0", 1200, 0, -120, 0, 3000103, False, 0)
sm.sendDelay(900)


sm.setSpeakerID(3000103)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("What are you talking about?")


sm.removeNpc(3000104)
sm.setSpeakerID(3000103)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("They attacked the East Sanctum? What are they trying to do with the Relic?)")


sm.setSpeakerID(3000110)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("The relic's disappearance should weaken the shields.")


sm.setSpeakerID(3000114)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I thought the relic was cursed... should we really be touching it?")


sm.setSpeakerID(3000110)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I did not realize they allowed superstitious nincompoops entry to our order! Will you balk at the call of destiny?")


sm.setSpeakerID(3000110)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("Are they trying to take the Relic?")


sm.setSpeakerID(3000103)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("We gotta stop them!")


sm.moveNpcByTemplateId(3000103, False, 300, 100)
sm.sendDelay(300)


sm.forcedInput(2)
sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/1", 1200, 0, -120, 0, 3000110, False, 0)
sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/1", 1200, 0, -120, 0, 3000114, False, 0)
sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/1", 1200, 0, -120, 0, 3000111, False, 0)
sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/1", 1200, 0, -120, 0, 3000115, False, 0)
sm.sendDelay(600)


sm.forcedInput(0)
sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/7", 900, 0, -120, 0, 3000103, False, 0)
sm.sendDelay(900)


sm.showFieldEffect("kaiser/tear_rush", 0)
sm.sendDelay(3000)


# Unhandled Message [COLLECTION_RECORD_MESSAGE] Packet: 2A 01 00 00 00 2F 00 31 30 3A 31 3A 32 3A 31 31 3D 34 3B 31 30 3A 31 3A 32 3A 31 32 3D 35 3B 31 30 3A 31 3A 33 3A 31 35 3D 34 3B 31 30 3A 31 3A 33 3A 31 36 3D 35
sm.removeNpc(3000103)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.removeNpc(3000110)
sm.removeNpc(3000114)
sm.removeNpc(3000111)
sm.removeNpc(3000115)
sm.warp(940001220, 0)
