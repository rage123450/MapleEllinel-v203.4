# 1404 - Thieves of Kerning City
from net.swordie.ms.enums import Stat

response = sm.sendAskYesNo("So you want to become a Thief?")

if response:
    sm.completeQuestNoRewards(parentID)
    sm.jobAdvance(400) # Thief
    sm.addSP(5, True)
    sm.resetStats()
    sm.sendSayOkay("You are now a #bThief#k.")
    sm.giveItem(2070000, 500)
    sm.giveItem(1472000, 1)
    sm.giveItem(1332007, 1)
sm.dispose()
