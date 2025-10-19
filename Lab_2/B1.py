for i in range(0,3):
    total_dis = 0
    file = open(f'inmap{i}.dat', 'r', encoding='utf-8')
    mile = file.readlines(1)
    print(mile)
    a = mile[0].split(' ')
    scale = float(a[2].strip())
    print('Dominika Dergavko\nSimple Map Distance Computations\n')
    print(f'Map Scale Factor:    {scale} miles per inch\n')
    print('    Map        Mileage')
    print('    Measure    Distance')
    print('=============================================================')
    for h in range(1, int(a[0])+1):
        measure = file.readlines(2)
        distance_0 = float(measure[0].strip())*scale
        distance = round(distance_0,1)
        total_dis+=distance
        print(f'#{h}  {measure[0].strip()}          {distance}')
    print('=============================================================')
    print(f'Total Distance:   {total_dis}\n\n\n')
    file.close()