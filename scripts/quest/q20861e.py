# The Path of a Dawn Warrior - Completion
from net.swordie.ms.enums import Stat

sm.setJob(1100) # Dawn Warrior 1st Job
sm.setSpeakerID(1101003) # Mihile
sm.sendSayOkay("Congratulations, you are now a thunder breaker! I have added 5 AP and 5 SP, enjoy your journey!")
sm.addSP(5, True)
sm.resetStats()
sm.completeQuest(parentID)
sm.giveItem(1402001) # Wooden Sword (2H)
sm.dispose()
