# Created by MechAviv
# Map ID :: 620100024
# Spaceship : Jett's Room

sm.hideUser(True)
sm.completeQuest(5757)
sm.spawnNpc(9270083, -230, -85)
sm.showNpcSpecialActionByTemplateId(9270083, "summon", 0)
sm.moveNpcByTemplateId(9270083, False, 100, 100)
sm.sendDelay(1900)


sm.completeQuest(5757)
sm.setSpeakerID(9270083)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Jett... I'm so sorry, but I need your power.\r\nJust the Core... Please forgive me.")


sm.sendDelay(3000)


sm.removeNpc(9270083)
sm.warp(620100025, 0)
