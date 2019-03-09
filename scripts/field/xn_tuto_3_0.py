# Created by MechAviv
# Map ID :: 931050920
# Classified Lab : Laboratory

sm.forcedInput(0)
sm.forcedInput(1)
sm.sendDelay(30)


sm.forcedInput(0)
sm.spawnNpc(2159377, -200, 50)
sm.showNpcSpecialActionByTemplateId(2159377, "summon", 0)
sm.showEffect("Effect/Direction12.img/effect/tuto/doorOpen", 0, -15, 2, 0, 0, True, 0)
sm.sendDelay(3000)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/8", 1200, 0, -120, 0, 2159377, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/9", 1200, 0, -120, 0, 2159377, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/10", 1200, 30, -250, 0, 2159377, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/8", 1200, 0, -120, 0, 2159377, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction12.img/effect/tuto/BalloonMsg2/7", 1200, 0, -250, 0, 2159377, False, 0)
sm.sendDelay(1200)


sm.removeNpc(2159377)
sm.warp(931060081, 0)
