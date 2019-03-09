# Created by MechAviv
# NPC ID :: 9131007
# Takeda Shingen


if sm.getFieldID() == 807100000:
    sm.setSpeakerID(9131007)
    sm.sendNext("Get to the Honnou-ji Outer Wall and open the Eastern Door.")
elif sm.getFieldID() == 807100002: # Honnou-ji Eastern Grounds
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 31
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 32
    # Unhandled Field Effect [ObjectStateByString] Packet: 02 06 00 67 75 69 64 65 33
    sm.setSpeakerID(9131007)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendNext("You did all right, samurai. I'll let you join my side for now.")


    sm.setSpeakerID(9131007)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("The battle goes well. I fear the Uesugi troops barged in too early. They may require assistance.")


    sm.setSpeakerID(9131007)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("Wouldn't surprise me. Kenshin couldn't keep her men under control if she had a stack of gold for each of them. It's not like her to be early though...")


    sm.setSpeakerID(9131007)
    sm.removeEscapeButton()
    sm.flipDialogue()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendSay("It's not important. We're doing well so far and I hate to break good momentum. Men, prepare for the final charge! TO THE TEMPLE!")


    sm.setSpeakerID(9131007)
    sm.removeEscapeButton()
    sm.flipSpeaker()
    sm.flipDialoguePlayerAsSpeaker()
    sm.setBoxChat()
    sm.boxChatPlayerAsSpeaker()
    sm.setBoxOverrideSpeaker()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.setColor(1)
    sm.sendPrev("We shall meet again, Tiger of Kai!")