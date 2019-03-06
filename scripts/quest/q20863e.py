# Path of a Wind Archer - Completion
from net.swordie.ms.enums import Stat

sm.setJob(1300) # Wind Archer 1st Job
sm.setSpeakerID(1101005) # Irena
sm.sendSayOkay("Congratulations, you are now a wind archer! I have added 5 AP and 5 SP, enjoy your journey!")
sm.addSP(5, True)
sm.resetStats()
sm.completeQuest(parentID)
sm.giveItem(1452002) # War Bow
sm.giveItem(2060000, 1000) # Bow Arrow
sm.dispose()
