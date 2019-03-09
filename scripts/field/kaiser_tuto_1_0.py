# Created by MechAviv
# Map ID :: 940001010
# Hidden Street : East Pantheon

sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.spawnNpc(3000107, -2950, 20)
sm.showNpcSpecialActionByTemplateId(3000107, "summon", 0)
sm.setSpeakerID(3000107)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Kaiser, this won't do. Come with me. There are other trustworthy people in Pantheon besides me.")


sm.moveCamera(False, 300, -2150, 29)


sm.sendDelay(30)


sm.forcedInput(1)
sm.sendDelay(30)


sm.forcedInput(0)
sm.sendDelay(357)


sm.moveNpcByTemplateId(3000107, False, 200, 100)
sm.sendDelay(417)


sm.forcedInput(1)
