#Omid Akbari
#bqh5sd
import uvage
import random as rand

camera = uvage.Camera(800, 600)

# set positions:

xpos_floor2 = 650
ypos_floor = 600

# increasing size is half the step size
# set limits to x position for floors: 600 and 1150

def x_randomizer(type):
    '''
    The purpose of this function is to randomize to give a new set of x positions to the right and left floor
    to change the location of the gap of the new floor formed
    :param type: This functions takes in the type of floor, or in other words, whether the gap is to the right or
    to the left
    :return: Returns the new x position
    '''
    if type == 1:
        x_pos = rand.randint(600,800)
    else:
        x_pos = rand.randint(1000,1200)
    return x_pos

player = uvage.from_color(500, 85, "red", 30, 30)
floor2 = uvage.from_color(x_randomizer(1), ypos_floor, "black", 900, 30)
floor1 = uvage.from_color(floor2.x - 1000, ypos_floor, "black", 900, 30)

floor4 = uvage.from_color(x_randomizer(2), ypos_floor + 140, "black", 900, 30)
floor3 = uvage.from_color(floor4.x-1000, ypos_floor + 140, "black", 900, 30)

floor6 = uvage.from_color(x_randomizer(1), ypos_floor + 290, "black", 900, 30)
floor5 = uvage.from_color(floor6.x - 1000, ypos_floor + 290, "black", 900, 30)

floor8 = uvage.from_color(x_randomizer(2), ypos_floor + 440, "black", 900, 30)
floor7 = uvage.from_color(floor8.x - 1000, ypos_floor + 440, "black", 900, 30)

floor10 = uvage.from_color(x_randomizer(1), ypos_floor + 590, "black", 900, 30)
floor9 = uvage.from_color(floor10.x - 1000, ypos_floor + 590, "black", 900, 30)

floor12 = uvage.from_color(x_randomizer(2), ypos_floor + 740, "black", 900, 30)
floor11 = uvage.from_color(floor12.x - 1000, ypos_floor + 740, "black", 900, 30)


diff = 890

def y_set(floor):
    '''
    The purpose of this function is to set a new y-position for the floor which the player has just passed. This
    new location will be below the lowest floor at the moment
    :param floor: This function takes in the floor number which the new floor will be underneath
    :return: The function returns the new y-position for the floor
    '''
    y_pos = 0
    #7 floor
    if floor == 11:
        floor1.y += diff
        floor2.y += diff
        floor2.x = x_randomizer(1)
        floor1.x = floor2.x - 1000
    #8 floor
    elif floor == 9:
        floor3.y += diff
        floor4.y += diff
        floor4.x = x_randomizer(2)
        floor3.x = floor4.x - 1000
    #9 floor
    elif floor == 7:
        floor5.y += diff
        floor6.y += diff
        floor6.x = x_randomizer(1)
        floor5.x = floor6.x - 1000
    #10 floor
    elif floor == 5:
        floor7.y += diff
        floor8.y += diff
        floor8.x = x_randomizer(2)
        floor7.x = floor8.x - 1000
    elif floor == 3:
        floor9.y += diff
        floor10.y += diff
        floor10.x = x_randomizer(1)
        floor9.x = floor10.x - 1000
    elif floor == 1:
        floor11.y += diff
        floor12.y += diff
        floor12.x = x_randomizer(2)
        floor11.x = floor12.x - 1000

    return y_pos

def draw_floor():
    '''
    The purpose of this function is to draw all the individual floors specified
    :return: This function does not return any data
    '''
    for obj in [floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8, floor9, floor10, floor11, floor12]:
        camera.draw(obj)

score = 0
rate = 2.5
x_move = 7

def tick():
    '''
    this function is the main program of the game which repeats in a loop within a certain tick
    :return: This function does not return anything
    '''
    #Background Settings
    camera.clear("White")
    global rate
    global score
    global x_move
    global center_x

    center_x = camera.center[1]
    score_board = uvage.from_text(750, center_x - 250, (str(int(score))), 30, "blue", italic=False)
    game_over = uvage.from_text(camera.center[0], camera.center[1] - 60, "GAME OVER!", 60, "blue", italic=False)
    camera.move(0, rate)

    if camera.center[1] > (player.y + 330):
        rate = 0
        x_move = 0
        camera.draw(game_over)
    else:
        score += 0.02
        rate += 0.001

    if uvage.is_pressing("right arrow"):
        player.x += x_move
        if player.x > 800:
            player.x = 793
    elif uvage.is_pressing("left arrow"):
        player.x -= x_move
        if player.x < 0:
            player.x = 7

    if player.bottom_touches(floor2) or player.bottom_touches(floor1) or player.bottom_touches(floor3) or player.bottom_touches(floor4) or player.bottom_touches(floor5) or player.bottom_touches(floor6) or player.bottom_touches(floor7) or player.bottom_touches(floor8) or player.bottom_touches(floor9) or player.bottom_touches(floor10) or player.bottom_touches(floor11) or player.bottom_touches(floor12):
        for floor in [floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8, floor9, floor10, floor11, floor12]:
            player.move_to_stop_overlapping(floor)
    else:
        player.y += 8
        player.move_to_stop_overlapping(floor1,1,2)
        player.move_to_stop_overlapping(floor2,0.5)

    if player.y > floor1.y + 350:
        y_set(11)
        draw_floor()
    elif player.y > floor3.y + 350:
        y_set(9)
        draw_floor()
    elif player.y > floor5.y + 350:
        y_set(7)
        draw_floor()
    elif player.y > floor7.y + 350:
        y_set(5)
        draw_floor()
    elif player.y > floor9.y + 350:
        y_set(3)
        draw_floor()
    elif player.y > floor11.y + 350:
        y_set(1)
        draw_floor()

    draw_floor()
    camera.draw(player)
    camera.draw(score_board)
    camera.display()

uvage.timer_loop(50, tick)


