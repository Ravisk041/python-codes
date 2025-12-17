t1 = input('enter model: ')
t2 = int(input('enter purchase year: '))
t3 = int(input('enter price: '))

if t1 == 'iphone' or t1 == 'google' or t1 == 'samsungs24':
    price = t3   # assign once

    if t2 == 2024:
        print(f'{t1} is costing {price} which was bought in the year {t2}')

    elif t2 == 2025:
        new_price = price * 1.20
        print(f'{t1} is costing {new_price} due to the increase in tax rate in the year {t2}')

    else:
        print('Invalid year')
else:
    print('Invalid model')
