
ticket = int(input('Введите количество билетов :'))

age = []


for i in range(0, ticket):
    input_age = int(input(f'Введите Ваш возвраст {i+1}: '))
    age.append(input_age)
    def price(age) :
        if age<18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
    full_price = sum(map(price, age))
    min_price = int(full_price*0.9)
    if ticket > 3:
        print('Стоимость  билетов со скидкой', min_price, 'руб.')
    else:
        print('Стоимисть билетов', full_price, 'руб.')
