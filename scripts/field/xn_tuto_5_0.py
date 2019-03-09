# Created by MechAviv
# Map ID :: 931050930
# Classified Lab : Laboratory

sm.spawnNpc(2159377, -180, 50)
sm.showNpcSpecialActionByTemplateId(2159377, "summon", 0)
sm.sendSessionValue("geli", 2159377)
sm.moveCamera(False, 100, -272, -63)


sm.sendDelay(2701)


sm.setSpeakerID(2159377)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("This is the last phase of testing. I know it's been a long time... are you ready?")


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/11", 1200, 0, -120, 0, 2159377, False, 0)
sm.sendDelay(900)


sm.moveCamera(True, 100, 0, 0)


sm.sendDelay(2381)


sm.startQuest(23600)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)