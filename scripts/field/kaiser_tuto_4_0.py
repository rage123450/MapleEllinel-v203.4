# Created by MechAviv
# Map ID :: 940001110
# Heliseum : Heliseum Outskirts

sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.spawnNpc(3000131, -390, 170)
sm.showNpcSpecialActionByTemplateId(3000131, "summon", 0)
sm.moveCamera(False, 300, -600, 170)


sm.sendDelay(999)


sm.sendDelay(1000)
sm.reservedEffect("Effect/Direction9.img/kaiserTutorial/Scene2")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendNext("How DARE you lay Heliseum at Darmoor's feet! You are a DISGRACE to the people of Nova!")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("The Council spared you, and this is how you repay them? I'll never forgive you! NEVER!")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("I wouldn't expect you to understand. I want power...and Darmoor gave it to me.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("I don't know what kind of power you've got, and I don't care. This wound isn't going to stop me from striking you down!")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("Temper, temper. I don't think you understand your situation. Let me break it down for you.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("First, I admit that I might not have the power to defeat you, mighty Kaiser, even with my added power from Darmoor. However, don't make the mistake of thinking I have no plan to counter your strength.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("You say your wound isn't going to stop you. But that blade was coated in a vicious poison that will sap your strength, tipping the odds in my favor.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("Heh... Then all I have to do is beat your before the poison takes full effect.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("Indeed. Which brings me to my second point. You're not just fighting me, you know. Heliseum has been overrun with thousands of Specters, all under my command. Even at full strength, I doubt you could beat so many.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("I won't know until I try.")


sm.spawnNpc(3000125, -750, 170)
sm.showNpcSpecialActionByTemplateId(3000125, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000122, -650, 170)
sm.showNpcSpecialActionByTemplateId(3000122, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000125, -550, 170)
sm.showNpcSpecialActionByTemplateId(3000125, "summon", 0)
sm.sendDelay(210)


sm.moveCamera(False, 450, -1300, 170)


sm.forcedInput(1)
sm.sendDelay(30)


sm.forcedInput(0)
sm.sendDelay(1526)


sm.spawnNpc(3000122, -1150, 170)
sm.showNpcSpecialActionByTemplateId(3000122, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000125, -1250, 170)
sm.showNpcSpecialActionByTemplateId(3000125, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000122, -1350, 170)
sm.showNpcSpecialActionByTemplateId(3000122, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000125, -1450, 170)
sm.showNpcSpecialActionByTemplateId(3000125, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000122, -1550, 170)
sm.showNpcSpecialActionByTemplateId(3000122, "summon", 0)
sm.sendDelay(210)


sm.spawnNpc(3000125, -1650, 170)
sm.showNpcSpecialActionByTemplateId(3000125, "summon", 0)
sm.moveCamera(True, 0, 0, 0)


sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
sm.sendDelay(30)


sm.sendDelay(2000)
sm.avatarOriented("Effect/OnUserEff.img/normalEffect/demonSlayer/chatBalloon0")
sm.reservedEffect("Effect/Direction9.img/kaiserTutorial/Scene2")


sm.showEffect("Effect/Direction9.img/effect/tuto/BalloonMsg2/0", 0, 0, -120, -2, -2, False, 0)
sm.sendDelay(2000)


sm.moveCamera(False, 450, -600, 170)


sm.sendDelay(585)


sm.showNpcSpecialActionByTemplateId(3000131, "alert", 0)
sm.showEffect("Effect/Direction9.img/effect/tuto/BalloonMsg1/2", 0, 0, -130, 0, 3000131, False, 0)
sm.sendDelay(2000)


sm.moveCamera(True, 0, 0, 0)


sm.removeNpc(3000125)
sm.removeNpc(3000122)
sm.removeNpc(3000125)
sm.removeNpc(3000122)
sm.removeNpc(3000125)
sm.removeNpc(3000122)
sm.removeNpc(3000125)
sm.removeNpc(3000122)
sm.removeNpc(3000125)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.showFieldEffect("lightning/screenMsg/0", 0)
sm.removeNpc(3000131)
# [FORCED_STAT_RESET] []
sm.warp(940001150, 0)
