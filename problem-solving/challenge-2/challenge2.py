def dice_faces_calculator(dice1: int, dice2: int, dice3: int) -> int:
    if dice1 == dice2:
        if dice2 == dice3:
            return dice1 * 3
        else:
            return dice1 * 2
    elif dice1 == dice3:
        return dice1 * 2
    elif dice2 == dice3:
        return dice2 * 2
    else:
        return max([dice1, dice2, dice3])


print(dice_faces_calculator(3, 3, 3))
