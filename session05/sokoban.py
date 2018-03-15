map_sokoban={
    'x': 5,
    'y': 5,
}

player = {
    'x': 3,
    'y': 2
}

boxes =[
    {'x':1, 'y': 1},
    {'x':2, 'y': 2},
    {'x':3, 'y': 3},
    ]

destinations =[
    {'x':1, 'y': 2},
    {'x':2, 'y': 4},
    {'x':3, 'y': 1},
]

while True:
    for y in range(map_sokoban['y']):
        for x in range(map_sokoban['x']):
            #print map
            box_is_here = False
            for box in boxes:
                if x == box['x'] and y== box['y']:
                    box_is_here = True
                    break

            des_is_here = False
            for des in destinations:
                if x == des['x'] and y== des['y']:
                    des_is_here = True
                    break

            player_is_here = False
            if y == player['y'] and x == player['x']:
                player_is_here = True
            if box_is_here:
                print("B", end=" ")
            elif des_is_here:
                print("D", end=" ")
            elif player_is_here:
                print("P", end=" ")
            else:
                print("-", end =" ")
        print()
    #### end of print map

    win = True
    for box in boxes:
        if box not in destinations:
            win = False

    if win:
        print("You win!!!")
        break

    ### move
    move = input('Your move? ').upper()
    dx = 0
    dy = 0

    if move == 'W':
        #print('Up')
        dy -= 1
    elif move =='S':
        #print('Down')
        dy = 1
    elif move == 'A':
        #print('Left')
        dx = -1
    elif move =='D':
        #print('Right')
        dx = 1

    if  0 <= player['x'] + dx < map_sokoban['x'] \
        and 0 <= player['y'] + dy < map_sokoban['y'] :
        player['x'] += dx
        player['y'] += dy


    for box in boxes:
        if player['x'] == box['x'] and player['y']== box['y']:
            if  0 <= box['x'] + dx < map_sokoban['x'] \
                and 0 <= box['y'] + dy < map_sokoban['y'] :
                box['x'] += dx
                box['y'] += dy
            break

    # check = 0
    # for box in boxes:
    #     for des in destinations:
    #         if box['x'] == des['x'] and box['y'] == des['y']:
    #             check +=1
    # if  check == len(boxes):
    #     print("You win")
    #     break
