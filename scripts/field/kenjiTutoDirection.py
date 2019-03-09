# Created by MechAviv

# Unknown : Unknown
if sm.getFieldID() == 807100010:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.setStandAloneMode(True)
    sm.showFieldEffect("JPKenji/text0", 0)
    sm.sendDelay(7000)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.warp(807100000, 1)

# Honnou-ji : Honnou-ji Eastern Wall
elif sm.getFieldID() == 807100000:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.forcedInput(1)
    sm.sendDelay(4300)


    sm.forcedInput(0)
    sm.setSpeakerID(9130000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendNext("Finally, the time has come! Today, we will put an end to the so-called Demon King. Today we wipe Oda Nobunaga from history!")


    sm.setSpeakerID(9131007)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("My hands shake with anticipation. The disgrace of the Matsuyama clan will haunt me no more.")


    sm.setSpeakerID(9130000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("Clear your head, falcon. You get all emotional on me, and I'll shave your head bald.")


    sm.setSpeakerID(9131007)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("The Mist Cutter yearns for vengeance. That is the only emotion I feel.")


    sm.setSpeakerID(9130000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("Hahahaha! You're just as serious as I'd heard you were. I like that. How about you start the attack on Honnou-ji?")


    sm.setSpeakerID(9131007)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("The Eastern Door?")


    sm.setSpeakerID(9130000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("Get over the wall and open up the eastern gate. My cavalry will be waiting for you on the other side, ready to trample the enemy into submission. ")


    sm.setSpeakerID(9131007)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("All right, but I hope that your horsemen will forgive me when there are no enemies left to be trampled.")


    sm.setSpeakerID(9130000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("Haha. I wish I could adopt you! Good luck out there, soldier. Try not to beat them all!")


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 31
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 32
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 33
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 34

# Unknown : Unknown
elif sm.getFieldID() == 807100011:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.showFieldEffect("JPKenji/text1", 0)
    sm.sendDelay(7000)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.warp(807100001, 1)

# Honnou-ji : Honnou-ji Eastern Grounds
elif sm.getFieldID() == 807100001:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, False, False, False)
    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/0", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/1", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/2", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.setSpeakerID(0)
    sm.setSpeakerType(3)
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendNext("Take down all enemies and open the east gate!")


    sm.showFieldEffect("aran/tutorialGuide2", 0)
    sm.removeSkill(40011183)
    sm.removeSkill(40011184)
    sm.removeSkill(40011185)

# Unknown : Unknown
elif sm.getFieldID() == 807100012:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, True, False, False)
    sm.showFieldEffect("JPKenji/text2", 0)
    sm.sendDelay(7000)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.warp(807100003, 1)

# Honnou-ji : Honnou-ji Courtyard
elif sm.getFieldID() == 807100003:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, True, False, False)
    sm.forcedInput(1)
    sm.sendDelay(2200)


    sm.forcedInput(0)
    sm.setSpeakerID(9131000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxOverrideSpeaker()
    sm.sendSayNextIllustration("A little deer comes to meet the tiger? You cannot possibly belong to the Oda clan. You are far too unkempt. What brings you to Honnou-ji?", 9131000, True)


    sm.setSpeakerID(9131000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setPlayerAsSpeaker()
    sm.boxChatPlayerAsSpeaker()
    sm.sendSay("(This woman appears delicate, but her voice is deep and rough with callous intent. Could she be one of Oda's?)")


    sm.setSpeakerID(9131000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setPlayerAsSpeaker()
    sm.boxChatPlayerAsSpeaker()
    sm.sendSay("My name is Anegasaki Kenji, eldest son of Anegasaki Tomonobu, retainer to the Matsuyama clan. I have come to avenge my family and rescue the princess. Who are you, fair maiden?")


    sm.setSpeakerID(9131000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxOverrideSpeaker()
    sm.sendSayIllustration("Hehe, am I truly so fair that you would mistake me for a maiden? I vaguely recall an unimportant family from the southwest named Matsuyama, though I thought I had put it from my memory long ago.", 9131000, True)


    sm.setSpeakerID(9131000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setPlayerAsSpeaker()
    sm.boxChatPlayerAsSpeaker()
    sm.sendSay("Only Nobunaga's followers would be so sharp of tongue and empty of mind. I do not relish harming one so beautiful, but my katana is less discerning.")


    sm.setSpeakerID(9131000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setPlayerAsSpeaker()
    sm.boxChatPlayerAsSpeaker()
    sm.sendSay("I will give you one last chance to tell me your name. Bear in mind, it will be the last thing you say on this plane of existence.")


    sm.setSpeakerID(9130000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxOverrideSpeaker()
    sm.sendSayIllustration("No need to get caught up dealing with this louse, Hayato.", 9130000, True)


    sm.spawnNpc(9131007, 135, 30)
    sm.showNpcSpecialActionByTemplateId(9131007, "summon", 0)
    sm.setSpeakerID(9131007)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setPlayerAsSpeaker()
    sm.boxChatPlayerAsSpeaker()
    sm.sendSay("Master Shingen!")


    sm.setSpeakerID(9130000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxOverrideSpeaker()
    sm.sendSayIllustration("Honnou-ji has fallen on worse times than I'd hoped. Though I can't say I'm surprised, now that I see one of Oda's Four Heavenly Kings standing before me. Wouldn't you agree, Akechi Mitsuhide?!", 9130000, True)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/0", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/3", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/4", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.setSpeakerID(9131000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxOverrideSpeaker()
    sm.sendSayNextIllustration("You are slightly less idiotic than your portrait made you out to be, Takeda Shingen. Yet you figured out what is going on here, and you figured out that I was the one who started this rebellion. Bravo, you goonish oaf. Bravo!", 9131000, True)


    sm.setSpeakerID(9130000)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxOverrideSpeaker()
    sm.sendSayIllustration("I've been told you're the kind of guy that'd stab his mother in the back for the right price. How about you and I team up, turn the tables on the Demon King?", 9130000, True)


    sm.setSpeakerID(9131007)
    sm.setSpeakerType(3)
    sm.removeEscapeButton()
    sm.setPlayerAsSpeaker()
    sm.boxChatPlayerAsSpeaker()
    sm.sendSay("You would count yourself in league with this trickster?! This scoundrel who destroyed my family?! I will not let that happen! Prepare yourself, Akechi Mitsuhide!")


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/5", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(1000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/6", 0, -100, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/7", 0, -100, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/8", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/9", 0, -100, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/10", 0, 0, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.forcedInput(1)
    sm.sendDelay(1300)


    sm.forcedInput(0)
    sm.forcedAction(1752, 0)
    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/11", 0, -100, -120, -2, -2, False, 0)
    sm.sendDelay(2000)
    # Unhandled User Effect [PlayPortalSE] Packet: 0D


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/12", 0, -100, -120, -2, -2, False, 0)
    sm.sendDelay(2000)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/balloonMsg/13", 0, 150, -120, -2, -2, False, 0)
    sm.sendDelay(1400)


    sm.showNpcSpecialActionByTemplateId(9131007, "attack", 0)
    sm.sendDelay(300)


    sm.showEffect("Effect/DirectionJP3.img/effect/kenjiTuto/shingenAttack/0", 0, 0, 0, -2, -2, False, 0)
    sm.sendDelay(400)


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.removeNpc(9131007)
    sm.warp(807100004, 1)

    # Unknown : Unknown
elif sm.getFieldID() == 807100005:
    sm.curNodeEventEnd(True)
    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(True, True, False, False)
    # Inventory Operation with 1 operations.
    sm.playURLVideoByScript("http://nxcache.nexon.net/maplestory/video/yt/JPHayato.html")


    sm.setTemporarySkillSet(0)
    sm.setInGameDirectionMode(False, True, False, False)
    sm.setStandAloneMode(False)
    sm.warp(807040000, 0)
