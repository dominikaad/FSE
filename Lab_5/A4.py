number_file = input("Введите номер файла ")
file = open(f'sequences.{number_file}.txt', 'r', encoding='utf-8')
answ_file = open(f'genedata.{number_file}.txt', 'w', encoding='utf-8')
comand_file = open(f'commands.{number_file}.txt', 'r', encoding='utf-8')


number = 1


def search(find_sequence_amin, number_fun):
    i = 0
    count = 0
    new_find_sequence = ''
    file.seek(0)
    chain_aminokisl = file.read().strip().split('\n')
    while i<len(find_sequence_amin):
        if find_sequence_amin[i].isdigit():
            digit_litter = find_sequence_amin[i+1]*int(find_sequence_amin[i])
            new_find_sequence+=digit_litter
            i += 1
        else:
            new_find_sequence += find_sequence_amin[i]
        i += 1
    for amin in chain_aminokisl:
        if new_find_sequence in amin.split('\t')[2]:
            answ_file.write(f'00{number_fun}\t\tsearch\t\t{new_find_sequence}\n')
            answ_file.write(f'organism\t\t\tprotein\n')
            answ_file.write(f'{amin.split('\t')[1]}\t\t{amin.split('\t')[0]}\n')
            answ_file.write('------------------------------------------------------\n')
            break
        else:
            count +=1
            if count==len(chain_aminokisl):
                answ_file.write(f'00{number_fun}\t\tsearch\t\t{new_find_sequence}\n')
                answ_file.write(f'organism\t\t\tprotein\n')
                answ_file.write(f'NOT FOUND\n')
                answ_file.write('------------------------------------------------------\n')


def get_key(list, value):
    for k, v in list.items():
        if v == value:
            return k

def mode(find_belok, number_fun):
    i = 0
    count = 0
    counts = {}
    list_value = []
    file.seek(0)
    chain_aminokisl = file.read().strip().split('\n')
    for amin in chain_aminokisl:
        if amin.split('\t')[0]==find_belok:
            aminokislota = amin.split('\t')[2]
            while i < len(aminokislota):
                if aminokislota[i].isdigit():
                    counts[aminokislota[i+1]] = counts.get(aminokislota[i+1], 0)+int(aminokislota[i])
                    i += 1
                else:
                    counts[aminokislota[i]] = counts.get(aminokislota[i], 0)+1
                i += 1
            counts = sorted(counts.items(), key=lambda x: x[0])
            new_counts = dict(counts)
            for key, value in new_counts.items():
                list_value.append(value)
                max_value = max(list_value)
                max_key = get_key(new_counts, max_value)
            answ_file.write(f'00{number_fun}\t\tmode\t\t{find_belok}\n')
            answ_file.write(f'amino-acid occurs:\n')
            answ_file.write(f'{max_key}\t\t{max_value}\n')
            answ_file.write('------------------------------------------------------\n')
            break
        else:
            count+=1
            if count==len(chain_aminokisl):
                answ_file.write(f'00{number_fun}\t\tmode\t\t{find_belok}\n')
                answ_file.write(f'organism\t\t\tprotein\n')
                answ_file.write(f'MISSING:{find_belok}\n')
                answ_file.write('------------------------------------------------------\n')

def diff(belok_1, belok_2, number):
    file.seek(0)
    score_razn = 0
    chain_aminokisl = file.read().strip().split('\n')
    if belok_1!=belok_2:
        for amin in chain_aminokisl:
            if amin.split('\t')[0]==belok_1:
                aminokisl_1 = amin.split('\t')[2]
            elif amin.split('\t')[0]==belok_2:
                aminokisl_2 = amin.split('\t')[2]
        if len(aminokisl_1)>0 and len(aminokisl_2)>0:
            raznica = abs(len(aminokisl_1)-len(aminokisl_2))
            if len(aminokisl_1)>=len(aminokisl_2):
                for i in range(0, len(aminokisl_2)):
                    if aminokisl_1[i]!=aminokisl_2[i]:
                        score_razn+=1
            elif len(aminokisl_2)>len(aminokisl_1):
                for i in range(0, len(aminokisl_1)):
                    if aminokisl_1[i]!=aminokisl_2[i]:
                        score_razn+=1
            score_razn+=raznica
            answ_file.write(f'00{number}\t\tdiff\t\t{belok_1}\t{belok_2}\n')
            answ_file.write(f'amino-acids difference:\n')
            answ_file.write(f'{score_razn}\n')
            answ_file.write('------------------------------------------------------\n')
        else:
            answ_file.write(f'00{number}\t\tdiff\t\t{belok_1}\t{belok_2}\n')
            answ_file.write(f'amino-acids difference:\n')
            answ_file.write(f'MISSING:\n')
            answ_file.write('------------------------------------------------------\n')
    else:
        answ_file.write(f'00{number}\t\tdiff\t\t{belok_1}\t{belok_2}\n')
        answ_file.write(f'amino-acids difference:\n')
        answ_file.write(f'{score_razn}\n')
        answ_file.write('------------------------------------------------------\n')


answ_file.write('Dominika Dergavko\nGenetic Searching\n')
answ_file.write('------------------------------------------------------\n')

line_comand = comand_file.read().strip().split('\n')
for comand in line_comand:
    if comand.split('\t')[0]=='search':
        search(comand.split('\t')[1], number)
        number+=1
    elif comand.split('\t')[0]=='mode':
        mode(comand.split('\t')[1], number)
        number+=1
    elif comand.split('\t')[0]=='diff':
        diff(comand.split('\t')[1], comand.split('\t')[2], number)
        number+=1

answ_file.close()
file.close()
comand_file.close()