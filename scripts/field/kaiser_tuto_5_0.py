# Created by MechAviv
# Map ID :: 940001150
# Unknown : Unknown

sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.spawnNpc(3000131, -390, 170)
sm.showNpcSpecialActionByTemplateId(3000131, "summon", 0)
sm.spawnNpc(3000122, -740, 170)
sm.showNpcSpecialActionByTemplateId(3000122, "summon", 0)
sm.spawnNpc(3000125, -640, 170)
sm.showNpcSpecialActionByTemplateId(3000125, "summon", 0)
sm.sendDelay(1500)


sm.forcedAction(474, 0)
sm.showEffect("Skill/6112.img/skill/61121100/effect", 0, 0, 0, -2, -2, False, 0)
sm.playSound("Kaiser/61121100", 100)
sm.sendDelay(150)


sm.showNpcSpecialActionByTemplateId(3000122, "die1", 0)
sm.showNpcSpecialActionByTemplateId(3000125, "die1", 0)
sm.showEffect("Skill/6112.img/skill/61121100/hit", 0, 0, 0, 0, 3000122, False, 0)
sm.showEffect("Skill/6112.img/skill/61121100/hit", 0, 0, 0, 0, 3000125, False, 0)
sm.sendDelay(1400)
sm.playExclSoundWithDownBGM("Skill.img/61121100/Hit")


sm.removeNpc(3000122)
sm.removeNpc(3000125)
sm.moveCamera(False, 300, -600, 178)


sm.sendDelay(1002)


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendNext("Bravo, Kaiser. Defiant to the last. I look forward to seeing how many Specters you can cut down before they overwhelm you.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("Sorry to disappoint, but you're going first, Magnus.")


sm.moveCamera(True, 0, 0, 0)


sm.sendDelay(0)


sm.spawnNpc(3000128, -750, 170)
sm.showNpcSpecialActionByTemplateId(3000128, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000128, -650, 170)
sm.showNpcSpecialActionByTemplateId(3000128, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000128, -550, 170)
sm.showNpcSpecialActionByTemplateId(3000128, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000128, -1150, 170)
sm.showNpcSpecialActionByTemplateId(3000128, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000128, -1250, 170)
sm.showNpcSpecialActionByTemplateId(3000128, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000128, -1350, 170)
sm.showNpcSpecialActionByTemplateId(3000128, "summon", 0)
sm.sendDelay(210)


sm.moveCamera(False, 450, -600, 178)


sm.sendDelay(666)


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendNext("Oh, I doubt that very much. There are still plenty of Specters here to head you off. That poison taking effect yet?")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("You're a coward, Magnus. Hiding behind your minions and dirty tricks, all earned by licking the boots of Darmoor. You have no honor.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("Honor is overrated. I just want to watch you suffer, and look! I got what I wanted.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("Oh, but don't worry. I'm merciful enough to end your life with my own hands. Kaiser may return, but I'll take great pleasure in ending your career.")


sm.sendDelay(2000)
sm.avatarOriented("Effect/OnUserEff.img/normalEffect/demonSlayer/chatBalloon0")
sm.reservedEffect("Effect/Direction9.img/kaiserTutorial/Scene2")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendNext("(This poison is spreading too fast. This might be my last chance...I have to do what I can to end this quickly.)")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("Even when you reincarnate, you'll be right back to square one. Too weak to oppose us. It's all over for you.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("Enough talk, Magnus. Let us end this.")


sm.showEffect("Effect/Direction9.img/effect/tuto/Effect/0", 0, 0, 0, -2, -2, False, 0)
sm.sendDelay(1200)


sm.hideUser(True)
sm.spawnNpc(3000142, -900, 170)
sm.showNpcSpecialActionByTemplateId(3000142, "summon", 0)
sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendNext("Now THIS is what I wanted! I was afraid the poison might stop you from transforming, but you don't disappoint. I always wanted to test my strength against your true form. Have at you!")


sm.showFieldEffect("demonSlayer/whiteOut", 0)
sm.sendDelay(5000)


sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.removeNpc(3000131)
sm.removeNpc(3000128)
sm.removeNpc(3000128)
sm.removeNpc(3000128)
sm.removeNpc(3000128)
sm.removeNpc(3000128)
sm.removeNpc(3000128)
sm.removeNpc(3000142)
# [FORCED_STAT_RESET] []
sm.warp(940002030, 0)
