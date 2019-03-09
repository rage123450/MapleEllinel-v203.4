# Created by MechAviv
# Map ID :: 940001100
# Heliseum : Heliseum Outskirts

sm.showNpcSpecialActionByTemplateId(3000131, "fake", 0)
sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendNext("No... But what of you? Are you injured? You fought against Darmoor's army?")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("I am...unharmed. And the fight? What do you expect from someone who was exiled?")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("But... How did Darmoor's army get inside Heliseum? What did they do to the shield?")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("There was a traitor, of course. The traitor disabled the shield so the Specters could overrun Heliseum.")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendSay("Magnus... Who would do such a thing?")


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendSay("Me.")


sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
# [FORCED_STAT_RESET] []
sm.warp(940002010, 0)
