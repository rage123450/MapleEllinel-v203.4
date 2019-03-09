# Created by MechAviv
# Map ID :: 940001220
# Eastern Region of Pantheon : East Sanctum

sm.forcedAction(451, 0)
sm.playSound("Kaiser/61001101", 100)
sm.showEffect("Skill/6100.img/skill/61001101/effect", 0, 0, 0, -2, -2, False, 0)
sm.sendDelay(210)


sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/5", 1200, 0, -120, 0, 3000110, False, 0)
sm.sendDelay(150)


sm.showNpcSpecialActionByTemplateId(3000110, "die1", 0)
sm.sendDelay(1500)


sm.setSpeakerID(3000114)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Ho-How dare you... Attack!")


sm.showNpcSpecialActionByTemplateId(3000114, "attack1", 0)
sm.showNpcSpecialActionByTemplateId(3000115, "attack1", 0)
sm.sendDelay(1500)


sm.showEffect("Npc/3000114.img/hit", 0, 0, 0, -2, -2, False, 0)
sm.sendDelay(300)


sm.showEffect("Effect/Direction9.img/effect/story/BalloonMsg1/6", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(900)
sm.reservedEffect("Effect/Direction9.img/KaiserTutorial/Scene2")


sm.setSpeakerID(3000111)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendNext("Wha-! How can kids be so strong?")


sm.setSpeakerID(3000114)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.sendSay("Down in one strike?! We can't let this happen! Get them!")


sm.showEffect("Effect/Direction9.img/effect/tuto/Effect/0", 0, 0, 0, -2, -2, False, 0)
sm.sendDelay(1200)


sm.showFieldEffect("demonSlayer/whiteOut", 0)
sm.sendDelay(1950)


sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.warp(940002020, 0)
