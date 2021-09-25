def game_map(PLAYER_NAME, FRIEND1_NAME, FRIEND2_NAME):
    """ Maps and their properties """
    maps_list = [["Room 0 - where unused objects are kept", 0, 0, False, False]]

    for map_list in range(1, 26):
        maps_list.append(["The dusty planet surface", 13, 13, True, True])

    maps_list += [
        # ["Room name", height, width, Top exit?, Right exit?]
        ["The airlock", 13, 5, True, False],  # room 26
        ["The engineering lab", 13, 13, False, False],  # room 27
        ["Poodle Mission Control", 9, 13, False, True],  # room 28
        ["The viewing gallery", 9, 15, False, False],  # room 29
        ["The crew's bathroom", 5, 5, False, False],  # room 30
        ["The airlock entry bay", 7, 11, True, True],  # room 31
        ["Left elbow room", 9, 7, True, False],  # room 32
        ["Right elbow room", 7, 13, True, True],  # room 33
        ["The science lab", 13, 13, False, True],  # room 34
        ["The greenhouse", 13, 13, True, False],  # room 35
        [PLAYER_NAME.name + "'s sleeping quarters", 9, 11, False, False],  # room 36
        ["West corridor", 15, 5, True, True],  # room 37
        ["The briefing room", 7, 13, False, True],  # room 38
        ["The crew's community room", 11, 13, True, False],  # room 39
        ["Main Mission Control", 14, 14, False, False],  # room 40
        ["The sick bay", 12, 7, True, False],  # room 41
        ["West corridor", 9, 7, True, False],  # room 42
        ["Utilities control room", 9, 9, False, True],  # room 43
        ["Systems engineering bay", 9, 11, False, False],  # room 44
        ["Security portal to Mission Control", 7, 7, True, False],  # room 45
        [FRIEND1_NAME.name + "'s sleeping quarters", 9, 11, True, True],  # room 46
        [FRIEND2_NAME.name + "'s sleeping quarters", 9, 11, True, True],  # room 47
        ["The pipeworks", 13, 11, True, False],  # room 48
        ["The chief scientist's office", 9, 7, True, True],  # room 49
        ["The robot workshop", 9, 11, True, False]  # room 50
    ]
    return maps_list
