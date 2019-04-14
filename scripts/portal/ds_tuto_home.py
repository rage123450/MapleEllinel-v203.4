# Created by MechAviv
# ID :: [924020000]
# Hidden Street : Demon Slayer's Childhood Home

if not sm.hasQuest(23200) and not sm.hasQuestCompleted(23200):
    sm.startQuest(23200)
    sm.avatarOriented("Effect/OnUserEff.img/normalEffect/demonSlayer/chatBalloon1")
elif sm.hasQuest(23200) and not sm.hasQuestCompleted(23200):
    sm.avatarOriented("Effect/OnUserEff.img/normalEffect/demonSlayer/chatBalloon0")