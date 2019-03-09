# Created by MechAviv
# Map ID :: 931050900
# Peacetime Edelstein : Edelstein Outskirts 1

sm.hideUser(True)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
sm.spawnNpc(2159369, 665, -20)
sm.showNpcSpecialActionByTemplateId(2159369, "summon", 0)
sm.spawnNpc(2159374, 380, -20)
sm.showNpcSpecialActionByTemplateId(2159374, "summon", 0)
sm.spawnNpc(2159372, 450, -20)
sm.showNpcSpecialActionByTemplateId(2159372, "summon", 0)
sm.spawnNpc(2159373, 520, -20)
sm.showNpcSpecialActionByTemplateId(2159373, "summon", 0)
sm.spawnNpc(2159375, 590, -20)
sm.showNpcSpecialActionByTemplateId(2159375, "summon", 0)
sm.showFieldEffect("xenon/text0", 0)
sm.sendDelay(1900)


sm.setSpeakerID(2159373)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Okay, here we go.")


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/0", 900, 0, -120, 0, 2159373, False, 0)
sm.sendDelay(900)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/1", 900, 0, -120, 0, 2159375, False, 0)
sm.sendDelay(1000)


sm.setSpeakerID(2159375)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Red M-Forcer!")


sm.setSpeakerID(2159373)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Yellow M-Forcer!")


sm.setSpeakerID(2159372)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Blue M-Forcer!")


sm.setSpeakerID(2159374)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Green M-Forcer!")


sm.setSpeakerID(2159369)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Black M-Forcer!")


sm.setSpeakerID(2159373)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("All together..")


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/2", 900, 0, -120, 0, 2159373, False, 0)
sm.sendDelay(900)


sm.showNpcSpecialActionByTemplateId(2159373, "happy", 0)
sm.sendDelay(900)


sm.setSpeakerID(2159373)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Oh! Awesome!")


sm.setSpeakerID(2159372)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Belle likes to pretend she's an M-Forcer.")


sm.setSpeakerID(2159373)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("It's so fun! They are righteous heroes who protect places like Edelstein from evil! Like me!")


sm.setSpeakerID(2159374)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Too bad there's never anybody for ME to beat up.")


sm.setSpeakerID(2159375)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("That's why we usually just yell at each other and dance around. It's super fun.")


sm.setSpeakerID(2159369)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I can be the bad guy...")


sm.setSpeakerID(2159373)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("No way, #h0#! We all have to be super righteous heroes! It's no fun if you're the bad guy.")


sm.setSpeakerID(2159369)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Yes.....")


sm.setSpeakerID(2159374)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Well, I guess as long as it's fun, it wouldn't matter. Maybe we can play more later.")


sm.setSpeakerID(2159369)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I have to head home! Talk to you later!")


sm.setSpeakerID(2159373)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("See you tomorrow!")


sm.moveNpcByTemplateId(2159369, True, 550, 100)
sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/3", 1200, 0, -120, 0, 2159375, False, 0)
sm.sendDelay(600)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/4", 1200, 0, -120, 0, 2159374, False, 0)
sm.sendDelay(600)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/5", 1200, 0, -120, 0, 2159369, False, 0)
sm.sendDelay(3000)


sm.removeNpc(2159369)
sm.removeNpc(2159374)
sm.removeNpc(2159372)
sm.removeNpc(2159373)
sm.removeNpc(2159375)
sm.warp(931050910, 0)
