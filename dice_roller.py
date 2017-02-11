import random

def dice_roller(dice_count, sides):
    total = 0
    for i in range(dice_count):
        total += int(random.randint(1, sides))
    print total
    
dice_roller(2, 4)
