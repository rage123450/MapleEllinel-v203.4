# 1402 - Magicians of Ellinia

sm.setSpeakerID(9000025) # Grendel the Really Old
response = sm.sendAskYesNo("So you want to become a Magician?")

if response:
    sm.completeQuestNoRewards(parentID)
    sm.setJob(200) # Magician
    sm.addSP(5, True)
    sm.resetStats()
    sm.giveItem(1372043)
    sm.sendSayOkay("You are now a #bMagician#k.")
sm.dispose()
