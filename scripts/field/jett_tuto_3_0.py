# Created by MechAviv
# Map ID :: 620100030
# Dark Cave : Dark Cave

sm.hideUser(True)
sm.spawnNpc(9201277, -180, 37)
sm.showNpcSpecialActionByTemplateId(9201277, "summon", 0)
sm.spawnNpc(9201278, -100, 37)
sm.showNpcSpecialActionByTemplateId(9201278, "summon", 0)
sm.spawnNpc(9201279, -30, 37)
sm.showNpcSpecialActionByTemplateId(9201279, "summon", 0)
sm.spawnNpc(9270083, 60, 37)
sm.showNpcSpecialActionByTemplateId(9270083, "summon", 0)
sm.showFieldEffect("newPirate/text5", 0)
sm.sendDelay(1900)


sm.moveNpcByTemplateId(9270083, False, 50, 100)
sm.sendDelay(1200)


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("They're here... They've got nowhere else to run. I'm going to get them today!")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Captain, shouldn't we call for backup? This might-")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("No! They're not getting away from me! I won't let them!")


sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("But what if it's a trap like last time? We were lucky Jett was there to-")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Jett? Jett?! What's so great about Jett? Jett is nothing without the Core! NOTHING!")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I'M the captain here!")


sm.sendDelay(1200)


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Captain, calm down. We just need to be careful...")


sm.sendDelay(1200)


sm.tremble(0, 1300, 30)
sm.sendDelay(1200)


sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("What was that?")


sm.spawnNpc(9201280, 440, 37)
sm.showNpcSpecialActionByTemplateId(9201280, "summon", 0)
sm.spawnNpc(9201281, 530, 37)
sm.showNpcSpecialActionByTemplateId(9201281, "summon", 0)
sm.spawnNpc(9201282, 590, 37)
sm.showNpcSpecialActionByTemplateId(9201282, "summon", 0)
sm.spawnNpc(9201283, 650, 37)
sm.showNpcSpecialActionByTemplateId(9201283, "summon", 0)
sm.spawnNpc(9201284, 710, 37)
sm.showNpcSpecialActionByTemplateId(9201284, "summon", 0)
sm.spawnNpc(9201285, 770, 37)
sm.showNpcSpecialActionByTemplateId(9201285, "summon", 0)
sm.sendDelay(1900)


sm.setSpeakerID(9201280)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Ha! Gotcha! Burke, you fool. I heard you've been losing your edge. Guess the rumors were true.")


sm.setSpeakerID(9201280)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("And without Jett, you're easy pickings. Say goodnight, buddy.")


sm.moveNpcByTemplateId(9201280, True, 20, 100)
sm.moveNpcByTemplateId(9201281, True, 20, 100)
sm.moveNpcByTemplateId(9201282, True, 20, 100)
sm.moveNpcByTemplateId(9201283, True, 20, 100)
sm.moveNpcByTemplateId(9201284, True, 20, 100)
sm.moveNpcByTemplateId(9201285, True, 20, 100)
sm.sendDelay(1200)


sm.setSpeakerID(9201280)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendNext("Stop!")


sm.showEffect("Skill/000.img/skill/0001227/effect", 0, 0, 0, -2, -2, False, 0)
sm.hideUser(False)
sm.sendDelay(1200)


sm.setSpeakerID(9201280)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("...It's you!")


sm.setSpeakerID(9201280)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("Glad I decided to drop in.")


sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Chief! Thank goodness!")


sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("You guys sit tight, I've got this!")


sm.setSpeakerID(9201280)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Rrgh, everyone, run for it! We can't take the one with the Core.")


sm.forcedAction(5, 0)
sm.showEffect("Skill/572.img/skill/5721064/effect", 0, 0, 0, -2, -2, False, 0)
sm.sendDelay(1200)


sm.setSpeakerID(9201280)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("N-no...")


sm.removeNpc(9201277)
sm.removeNpc(9201278)
sm.removeNpc(9201279)
sm.removeNpc(9270083)
sm.removeNpc(9201280)
sm.removeNpc(9201281)
sm.removeNpc(9201282)
sm.removeNpc(9201283)
sm.removeNpc(9201284)
sm.removeNpc(9201285)
sm.warp(620100023, 0)
