apart = int(input('Введите количество квартир на площадке: '))
floor = int(input('Введите количество этажей в подъезде: '))
apart_number = int(input('Введите номер квартиры: '))

apart_count = apart * floor
entrance_number = (apart_number-1) // apart_count+1
apart_entrance = (apart_number - 1) % apart_count + 1
print('Номер подъезда: ', entrance_number+1)
floor_apart = (apart_entrance - 1) // apart + 1
print('Номер этажа: ', floor_apart)
