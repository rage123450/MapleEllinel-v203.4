# Created by MechAviv
# Map ID :: 620100022
# Spaceship : Corridor

sm.hideUser(True)
sm.spawnNpc(9201277, -270, -131)
sm.showNpcSpecialActionByTemplateId(9201277, "summon", 0)
sm.spawnNpc(9201278, -180, -131)
sm.showNpcSpecialActionByTemplateId(9201278, "summon", 0)
sm.spawnNpc(9201279, -90, -131)
sm.showNpcSpecialActionByTemplateId(9201279, "summon", 0)
sm.spawnNpc(9270083, 610, -131)
sm.showNpcSpecialActionByTemplateId(9270083, "summon", 0)
sm.moveNpcByTemplateId(9270083, True, 100, 100)
sm.sendDelay(1200)


sm.moveCamera(False, 150, 200, -167)


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Jett was all sorts of awesome today. I've never seen anyone so strong.")


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("?")


sm.sendDelay(1200)


sm.setSpeakerID(9201278)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Yeah, that Core thing is just amazing. Jett's unstoppable... I bet even Captain Burke couldn't win that fight.")


sm.setSpeakerID(9201279)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Hah, that's kind of sad.")


sm.setSpeakerID(9201279)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("I mean, maybe Jett should just be the captain. The king trusts Jett more anyway. We'd probably all be better off.")


sm.setSpeakerID(9201277)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("That's what everyone's been saying. Ah well, let's get to the party before all the food is gone.")


sm.sendDelay(1200)


sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext(".......")


sm.sendDelay(1200)


sm.removeNpc(9201277)
sm.removeNpc(9201278)
sm.removeNpc(9201279)
sm.removeNpc(9270083)
sm.warp(620100030, 0)
