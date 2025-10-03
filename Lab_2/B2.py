for i in range(1,4):
    sum_temp = 0
    file = open(f'{i}.WCData.txt', 'r', encoding='utf-8')
    answ_file = open(f'{i}.WindChillReport.txt', 'w', encoding='utf-8')
    mile = file.readlines()
    amt = len(mile)
    answ_file.write('Time          WC temp          WC Effect\n')
    answ_file.write('-----------------------------------------------------\n')
    for h in range(amt-2):
        inform = mile[h+2].split(' ')
        temp = int(inform[11])
        speed = int(inform[24].strip())
        wc_temp = round(35.74+(0.6125*temp)+((0.4275*temp-35.75)*speed**0.16), 1)
        sum_temp+=wc_temp
        average_temp = round(sum_temp/(amt-2),1)
        wc_effect = round(wc_temp-temp,1)
        answ_file.write(f'{inform[0]}          {wc_temp}          {wc_effect}\n')
    answ_file.write('-----------------------------------------------------\n')
    answ_file.write(f'The average adjusted temperature, based on {amt-2} observations, was {average_temp}')
    answ_file.close()
    file.close()