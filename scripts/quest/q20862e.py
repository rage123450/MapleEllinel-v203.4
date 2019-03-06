# The Path of a Blaze Wizard - Completion
from net.swordie.ms.enums import Stat

sm.setJob(1200) # Blaze Wizard 1st Job
sm.setSpeakerID(1101004) # Oz
sm.sendSayOkay("Congratulations, you are now a blaze wizard! I have added 5 AP and 5 SP, enjoy your journey!")
sm.addSP(5, True)
sm.resetStats()
sm.completeQuest(parentID)
sm.giveItem(1382000) # Wooden Staff
sm.dispose()
