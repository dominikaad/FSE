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
                    if precipitation[t] != 0.00:
                        count_star = '*'*int((precipitation[t]//0.25)+1)
                        answ_file.write(f'{str(k)}\t\t{precipitation[t]:.2f} {count_star}\n')
                    else:
                        answ_file.write(f'{str(k)}\t\t{precipitation[t]:.2f}\n')
                    break
        else:
            answ_file.write(f'{str(k)}\t\tNA\n')





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
    count_num_31 = 0
    count_num_30 = 0
    count_num_28 = 0
    array_num = []
    array_precip = []
    replay_num = 0
    sum_precip = 0

    answ_file.write('Programmer: Dominika Dergavko\n')
    answ_file.write(f'{inf_project}\n')
    answ_file.write(f'Precipitation report for {place} during {data}\n')
    answ_file.write('Error\t\tDay\t\tLine\n')

    # if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    #     flag_31 = True
    # elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
    #     flag_30 = True
    # elif month == 'February':
    #     flag_28 = True

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
                if key!=replay_num:
                    replay_num = key
                    write_error('R', key, h)
                    list_inf[key] = 1
                    print(list_inf)
                    # print(precipitation)
                    # sum_precip += precipitation

        if month=='January' or month=='March' or month=='May' or month=='July' or month=='August' or month=='October' or month=='December':
            count_num_31+=1
            count_precip = 31
            if 0>number or number>31:
                write_error('N', number, h)
        elif month=='April' or month=='June' or month=='September' or month=='November':
            count_num_30+=1
            count_precip = 30
            if 0>number or number>30:
                write_error('N', number, h)
        elif month=='February':
            count_num_28+=1
            count_precip = 28
            if 0>number or number>28:
                write_error('N', number, h)

    if count_num_30==len_inf-3:
        write_inf(30, array_num, array_precip, len_array_num)
    elif count_num_31 == len_inf - 3:
        write_inf(31, array_num, array_precip, len_array_num)
    elif count_num_28 == len_inf - 3:
        write_inf(28, array_num, array_precip, len_array_num)
    answ_file.write('Minimum\t\tMaximum\t\tAverage\n')
    print(sum_precip)
    print(count_precip)
    average = sum_precip/count_precip
    answ_file.write(str(format(average, ".2f")))
    answ_file.close()
    file.close()