# The Path of a Thunder Breaker - Completion
from net.swordie.ms.enums import Stat

sm.setJob(1500) # Thunder Breaker 1st Job
sm.setSpeakerID(1101007) # Hawkeye
sm.sendSayOkay("Congratulations, you are now a thunder breaker! I have added 5 AP and 5 SP, enjoy your journey!")
sm.addSP(5, True)
sm.resetStats()
sm.completeQuest(parentID)
sm.giveItem(1482000) # Steel Knuckler
sm.dispose()
