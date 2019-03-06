# 1403 - Bowmen of Henesys

response = sm.sendAskYesNo("So you want to become a Bowman?")

if response:
    sm.completeQuestNoRewards(parentID)
    sm.jobAdvance(300) # Archer
    sm.addSP(5, True)
    sm.resetStats()
    sm.sendSayOkay("You are now an #bArcher#k.")
sm.dispose()
