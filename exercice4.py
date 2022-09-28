# Fontion fournie ne pas modifier
clearConsole = lambda: print('\n' * 10)

def print_table(table):
    # Dimension 1 = ligne
    # Dimension 2 = colonne
    clearConsole()
    for i, row in enumerate(table):
        row_str = "{:>2}" * len(row)
        row_str = row_str.format(*row)
        print("{:^20}".format(row_str), '\n')

# ________________________________________________________________

# Partie 1
def init_maze(nb_row, nb_col, player_pos, end_pos, walls):
    maze=[]# TODO Générer un labyrinthe vide -> rempli de "_"
    for i in range(nb_row):
        line = []
        for j in range(nb_col):
            line.append("_")
        maze.append(line)
    # TODO Placer le joueur "O" la sortie "X" les murs "W"
    for index_row, row in enumerate(maze):
        if index_row == player_pos[0]:
            for i in range(len(row)):
                if i == player_pos[1]:
                    row[i]='O'
        if index_row == end_pos[0]:
            for j in range(len(row)):
                if j == end_pos[1]:
                    row[j] = 'X'
        for wall in walls:
            if index_row==wall[0]:
                for k in range(len(row)):
                    if k==wall[1]:
                        row[k]="W"
    print(maze)
    return  maze

# Partie 2
def validate_move(maze, new_player_pos):
    result = False
    # TODO Vérifier si la position est valide -> dans le labyrinthe et pas sur un mur
    if new_player_pos[0] >= len(maze) or new_player_pos[0] < 0 or \
            new_player_pos[1] >= len(maze[0]) or new_player_pos[1] < 0:
        result = False
    elif maze[new_player_pos[0]][new_player_pos[1]] == "W":
        result = False
    else:
        result = True
    return result

#Partie 3
def move(key_pressed, maze, player_pos):
    # TODO Créer le dictionnaire d'équivalence entre la touche appuyée et la direction ("up", "left", "down", "right")
    move_dic = {"w": "up", "a": "left", "s": "down", "d": "right"}
    # TODO Vérifier si la touche appuyée est dans le dictionnaire
    if key_pressed in move_dic:
        # TODO Récupérer la direction du mouvement
        move = move_dic[key_pressed]
        # TODO Générer la position potentielle du joueur en fonction de la direction
        if move == "up":
            new_player_pos = [player_pos[0]-1, player_pos[1]]
        if move == "left":
            new_player_pos = [player_pos[0], player_pos[1]-1]
        if move == "down":
            new_player_pos = [player_pos[0]+1, player_pos[1]]
        if move == "right":
            new_player_pos = [player_pos[0], player_pos[1]+1]
        if validate_move(maze, new_player_pos):
            # TODO Changer réellement la position du joueur
            for i in range(len(maze)):
                for j in range(len(maze[0])):
                    if [i,j]==player_pos:
                        

            pass
    return maze, player_pos
if __name__ == '__main__':
    nb_row = 4
    nb_col = 7
    player_pos = [0,0]  # TODO Définir la position ligne, colonne sur en haut à gauche
    end_pos = [nb_row-1,nb_col-1]  # TODO Définir la position ligne, colonne sur en bas à droite
    # Coordoné sous la forme (ligne, colone)
    walls = [[0, 1],[1, 1], [1, 2], [1, 3], [1, 5], [2, 1], [2, 5], [3, 3], [3, 5]]
    maze = init_maze(nb_row, nb_col, player_pos, end_pos, walls)

    print_table(maze)

    # TODO Décommenter pour tester votre code en Partie 2
    test_pos = [0,1] #changez les valeurs pour tester tous les cas possibles
    valid = validate_move(maze, test_pos)
    print(valid)


    # TODO Décommenter pour tester votre code en Partie 3
    while player_pos != end_pos:
        key_pressed = input("mouvement : ")
        maze, player_pos = move(key_pressed, maze, player_pos)
        print_table(maze)

    print("Vous avez gagnez !")
