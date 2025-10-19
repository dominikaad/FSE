number_game = int(input("Введите номер игры: "))

initial_line_m = 0
initial_column_m = 0
initial_line_c = 0
initial_column_c = 0
flag_m = False
flag_c = False
distance_mouse = 0
distance_cat = 0
flag_game = False


file = open(f'{number_game}.ChaseData.txt', 'r', encoding='utf-8')
inf_file = file.readlines()
amount_inf = int(len(inf_file))
size_game = inf_file[0].split(' ')
print(size_game)
amount_line = size_game[3]
amount_column = size_game[6].strip()
print('Cat and Mouse\n')
print('\tCat\t\tMouse\tDistance')
print('-----------------------------------')


for i in range(1, amount_inf):
    way = inf_file[i].split('        ')
    player = way[0].strip()
    if player=='M' and flag_game == False:
        way_line = int(way[1])
        way_column = int(way[2])
        initial_line_m+=way_line
        initial_column_m+=way_column
        if initial_line_m<=0:
            initial_line_m+=int(amount_line)
        elif initial_line_m>int(amount_line):
            initial_line_m-=int(amount_line)
        elif initial_column_m<=0:
            initial_column_m+=int(amount_column)
        elif initial_column_m>int(amount_column):
            initial_column_m-=int(amount_column)
        if flag_m:
            distance_mouse+=(abs(way_line)+abs(way_column))
            if initial_line_m==initial_line_c and initial_column_m==initial_column_c:
                flag_game=True
                line_meeting = initial_line_c
                column_meeting = initial_column_c
                break
        flag_m = True



    elif player=='C' and flag_game == False:
        way_line = int(way[1])
        way_column = int(way[2])
        initial_line_c+=way_line
        initial_column_c+=way_column
        if initial_line_c<=0:
            initial_line_c+=int(amount_line)
        elif initial_line_c>int(amount_line):
            initial_line_c-=int(amount_line)
        elif initial_column_c<=0:
            initial_column_c+=int(amount_column)
        elif initial_column_c>int(amount_column):
            initial_column_c-=int(amount_column)
        if flag_c:
            distance_cat+=(abs(way_line)+abs(way_column))
            if initial_line_c==initial_line_m and initial_column_c==initial_column_m:
                flag_game=True
                line_meeting = initial_line_c
                column_meeting = initial_column_c
                break
        flag_c = True


    elif player=='P':
        if flag_m==True and flag_c==False:
            print(f'( ?, ?)     ({initial_line_m},{initial_column_m})')
        elif flag_c==True and flag_m==False:
            print(f'({initial_line_c},{initial_column_c})     ( ?, ?)')
        else:
            distance = abs(initial_line_m-initial_line_c)+abs(initial_column_m-initial_column_c)
            print(f'({initial_line_c},{initial_column_c})     ({initial_line_m},{initial_column_m})      {distance}')


print('------------------------------------\n\n')
print('Distance\t\tMouse\tCat')
print(f' \t\t\t\t{distance_mouse}\t\t{distance_cat}\n')
if flag_game:
    print(f'Mouse caught at:({line_meeting},{column_meeting})')
else:
    print('Mouse evaded Cat')
file.close()