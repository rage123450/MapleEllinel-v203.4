# Monster Hot Air Balloon  |  (2435554)
def init():
    if sm.getSkillByItem() == 0:    # Check whether item has an vehicleID stored,  0 if false.
        sm.chat("An Error occurred whilst trying to find the mount.")
    elif sm.hasSkill(sm.getSkillByItem()):
        sm.chat("You already have the 'Monster Hot Air Balloon' mount.")
    else:
        sm.consumeItem()
        sm.giveSkill(sm.getSkillByItem())
        sm.chat("Successfully added the 'Monster Hot Air Balloon' mount.")
    sm.dispose()