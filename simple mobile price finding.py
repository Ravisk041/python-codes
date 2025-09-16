t1=input('enter model:')
t2=int(input('enter purchase year'))
t3=int(input('enter price'))
if t1 == 'iphone' or t1 == 'google' or t1 == 'samsungs24':
  if t2 == 2024:
    price = t3
    print(f'{t1} is costing {price} which bought in the year {t2}')
  elif t2 == 2025:
    price1 = price * 0.20
    print(f'{t1} is costing {price+price1} due to the increase in tax rate in the year {t2}')
    
