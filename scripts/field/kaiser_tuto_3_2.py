# Created by MechAviv
# Map ID :: 940001100
# Heliseum : Heliseum Outskirts

sm.showNpcSpecialActionByTemplateId(3000131, "summon", 0)
sm.sendSessionValue("magnus", 3000131)
sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipSpeaker()
sm.flipBoxChat()
sm.sendNext("Kaiser...you're late.")


sm.moveCamera(False, 450, -600, 178)


sm.setSpeakerID(3000131)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.flipBoxChatPlayerAsSpeaker()
sm.sendNext("Magnus! What are you doing here? What happened to Heliseum?")


sm.forcedInput(2)
sm.curNodeEventEnd(True)
