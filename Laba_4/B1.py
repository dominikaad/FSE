from collections import Counter


def write_error(type, day, line):
    if type=='R':
        answ_file.write(f'Repeated\t{day}\t\t{line}\n')
    if type=='N':
        answ_file.write(f'Invalid\t\t{day}\t\t{line}\n')

def write_inf(count_num, number, precipitation, len):
    for k in range(1, count_num+1):
        if k in number:
            for t in range(0, len):
                if k ==number[t]:
                    answ_file.write(f'{str(k)}\t\t{str(precipitation[t])}\n')
                    break
        else:
            answ_file.write(f'{str(k)}\t\tNA\n')



    # list_num_precip = {number[t]:
    #                    precipitation[t] for t in range(len)}
    # for k in range(1, count_num+1):
    #     if k in list_num_precip:
    #         answ_file.write(f'{k}\t\t{list_num_precip[k]}\n')
    #     else:
    #         answ_file.write(f'{str(k)}\t\tNA\n')


flag_31 = False
flag_30 = False
flag_28 = False

for i in range(0,3):
    if i == 0:
        file = open(f'Precip.txt', 'r', encoding='utf-8')
        answ_file = open(f'Report.txt', 'w', encoding='utf-8')
    else:
        file = open(f'Precip{i}.txt', 'r', encoding='utf-8')
        answ_file = open(f'Report{i}.txt', 'w', encoding='utf-8')


    information = file.readlines()
    print(information)
    len_inf = len(information)
    inf_project = information[0]
    place = information[1].strip()
    data = information[2].strip()
    month = data.split(',')[0]
    flag_num = False
    flag_replay = False

    array_num = []
    array_precip = []
    replay_num = 0



    answ_file.write('Programmer: Dominika Dergavko\n')
    answ_file.write(f'{inf_project}\n')
    answ_file.write(f'Precipitation report for {place} during {data}\n')
    answ_file.write('Error\t\tDay\t\tLine\n')

    if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        flag_31 = True
    elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
        flag_30 = True
    elif month == 'February':
        flag_28 = True


    for h in range(3, len_inf):
        if len(information[h].split(' '))==1:
            inf_num_precipitation = information[h].split('\t')
            number = int(inf_num_precipitation[0])
            precipitation = float(inf_num_precipitation[1])
        else:
            inf_num_precipitation = information[h].split(' ')
            number = int(inf_num_precipitation[0])
            precipitation = float(inf_num_precipitation[-1].strip())

        array_num.append(number)
        len_array_num = len(array_num)
        array_precip.append(precipitation)
        list_num_precip = dict(zip(array_num, array_precip))


        list_inf = Counter(array_num)
        for key, value in list_inf.items():
            if value==2:
                flag_replay = True
                if key==replay_num:
                    flag_replay = False
                else:
                    replay_num = key
                    write_error('R', key, h)
                    list_inf[key] = 1
                    print(list_inf)
                    flag_replay = False

        if month=='January' or month=='March' or month=='May' or month=='July' or month=='August' or month=='October' or month=='December':
            if 0>number or number>31:
                flag_num = True
                write_error('N', number, h)
                flag_num = False
        elif month=='April' or month=='June' or month=='September' or month=='November':
            if 0>number or number>30:
                flag_num = True
                write_error('N', number, h)
                flag_num = False
        elif month=='February':
            if 0>number or number>28:
                flag_num = True
                write_error('N', number, h)
                flag_num = False
    if flag_30:
        for key, value in list_num_precip.items():
            write_inf(30, array_num, array_precip, len_array_num)
            flag_30 = False
    elif flag_31:
        for key, value in list_num_precip.items():
            write_inf(31, array_num, array_precip, len_array_num)
            flag_31 = False
    elif flag_28:
        for key, value in list_num_precip.items():
            write_inf(28, array_num, array_precip, len_array_num)
            flag_28 = False

    answ_file.close()
    file.close()