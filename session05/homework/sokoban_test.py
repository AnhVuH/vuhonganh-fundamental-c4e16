map_sokoban = {
        'x' : 6,
        'y' : 6,
        }

boxes = [
        {'x' : 1, 'y' : 2},
        {'x' : 2, 'y' : 3},
        {'x' : 4, 'y' : 2},
        ]

destinations = [
            {'x' : 0, 'y' : 3},
            {'x' : 4, 'y' : 0},
            {'x' : 2, 'y' : 2},
            ]

player = [{'x' : 3, 'y' : 3}]

def display(list_parts,symbol, x,y):
    part_is_here = False
    for part in list_parts:
        if part['x'] == x and part['y'] == y:
            print(symbol, end =' ')
            part_is_here = True
            break
    return part_is_here

def out_map(obj,dx,dy):
    if 0 <= obj['x'] + dx < map_sokoban['x'] and 0 <= obj['y'] + dy < map_sokoban['y']:
        return True

def moved(obj,dx,dy):
    obj['x'] += dx
    obj['y'] += dy


#display map
while True:
    for y in range(map_sokoban['y']):
        for x in range(map_sokoban['x']):
            player_is_here = display(player,'P',x,y)
            if player_is_here:
                continue
            box_is_here = display(boxes,'B',x,y)
            if box_is_here:
                continue
            des_is_here = display(destinations,'D',x,y)
            if des_is_here:
                continue
            print('-', end =' ')
        print()

    #check win
    win = True
    for box in boxes:
        if box not in destinations:
            win = False
            break
    if win == True:
        print('You win!!!')
        break

    #moving

    dx = 0
    dy = 0
    move = input('Your move? ').upper()
    if move == 'A':
        dx = -1
    elif move == 'D':
        dx = 1
    elif move =='W':
        dy = -1
    elif move == 'S':
        dy = 1

    box_pos = []
    for box in boxes:
        box_pos.append(list(box.values()))

    player_on_box = False
    for box in boxes:
        if player[0]['x'] + dx == box['x'] and player[0]['y'] + dy == box['y']:
            player_on_box = True
            if out_map(box,dx,dy) and [box['x'] + dx, box['y'] + dy] not in box_pos:
                moved(box,dx,dy)
                moved(player[0],dx,dy)
                break
    if out_map(player[0],dx,dy) and not player_on_box:
        moved(player[0],dx,dy)
