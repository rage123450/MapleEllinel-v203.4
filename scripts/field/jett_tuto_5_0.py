# Created by MechAviv
# Map ID :: 620100025
# Spaceship : Corridor

sm.completeQuest(5757)
sm.showFieldEffect("newPirate/text6", 0)
sm.sendDelay(1900)


sm.spawnNpc(9201277, 80, -131)
sm.showNpcSpecialActionByTemplateId(9201277, "summon", 0)
sm.showEffect("Skill/000.img/skill/0001227/effect", 0, 10, -20, 0, 9201277, False, 0)
sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Chief! Code red!")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("What is it?")


sm.forcedInput(2)
sm.sendDelay(400)


sm.forcedInput(0)
sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("The king...he's... He's been assassinated! But the thing is...")


sm.sendDelay(1200)


sm.spawnNpc(9270083, -520, -131)
sm.showNpcSpecialActionByTemplateId(9270083, "summon", 0)
sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Jett!")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("Burke! Where have you been?\r\nDid you hear? The king was assassinated!")


sm.forcedInput(1)
sm.sendDelay(30)


sm.forcedInput(0)
sm.moveNpcByTemplateId(9270083, False, 300, 100)
sm.sendDelay(4000)


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("...I've heard. Look at this.")


sm.showFieldEffect("newPirate/pendant_w", 0)
sm.sendDelay(3000)


sm.showEffect("Effect/DirectionNewPirate.img/newPirate/balloonMsg1/1", 2000, 0, -80, -2, -2, False, 0)
sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendNext("Wha......What?! How am I wanted...? For what...? Is this real, Burke?!")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("We were about to tell you.")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Everyone says you were the one who assassinated the king.")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("What?! No! It's not me! I've been right here on the ship!")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("We know, but-")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("There's no time! The royal guards must already be homing in on us. You need to go!")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("No, I won't run! That'll only convince them that I did it! I'm innocent, and I'll prove it!")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("I have no reason to assassinate the king!")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Jett, there are witnesses. I don't know how, but... No one will believe you. And the people are angry.")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("I can't believe it... I didn't do anything...")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Jett, I know you're innocent. We all do. But you have to get out of here. Get somewhere safe first, then think about what we can do to get you out of this mess.")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("It's only been a few hours, but everyone's already convinced you're guilty. I mean, just look at this reward.")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("You're a bounty hunter. You know how this works.")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("Is running away... really the only option I have?")


sm.spawnNpc(9201278, 200, -131)
sm.showNpcSpecialActionByTemplateId(9201278, "summon", 0)
sm.showEffect("Skill/000.img/skill/0001227/effect", 0, 10, -20, 0, 9201278, False, 0)
sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Chief! The royal guardsmen are here! If you're going, it's got to be now. Don't worry, we'll buy you some time!")


sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("No, I don't want anyone else involved in this mess! I don't know how I got into it, but I'm going to get myself out of it.")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("You've saved our lives so many times. Let us do this one thing for you.")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("...You guys...")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("You don't have much time! We've got your back, now go!")


sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Please... Take care!")


sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.boxChatPlayerAsSpeaker()
sm.sendSay("...We'll meet again, I promise!")


sm.moveNpcByTemplateId(9270083, True, 400, 100)
sm.removeNpc(9270083)
sm.forcedInput(1)
sm.sendDelay(4000)


sm.forcedInput(0)
sm.hideUser(True)
sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("We've got to do our part! Even if it means putting our lives on the line...")


sm.removeNpc(9201277)
sm.removeNpc(9201278)
sm.warp(620100026, 0)
