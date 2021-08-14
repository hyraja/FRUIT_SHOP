print('Fruit management system')

f = {}
cart = []


def main_menu():
    print("1.Add fruit ")
    print("2.-Delete fruit by name")
    print("3.Search fruit by name and rate")
    print("4.change fruit name and rate")
    print("5.-Add to cart")
    print("6.-Display all fruit data")
    print("7.display cart")
    print('8.Delete item from cart')
    print('9.exit')


def add_fruit():
    f_id = 0
    s_no = int(input('Enter serial number '))
    if s_no not in f.keys():
        f_id = f_id + 1
        f[s_no] = {
            'fruit_id': f_id,
            'fruit_name': input("Enter fruit name : "),
            'Fruit_rate': int(input('Enter rate of fruit : ')),
            'imported_from': input('Enter import place of fruit : '),
            'imported_date': input('enter import date : '),
            'buy_price': float(input('enter buy price like xx.xx : '))
        }
        print('fruit added successfully')

    else:
        print('serial key already taken')


def delete_fruit():
    s_no = int(input('enter serial number'))
    if s_no not in f.keys():
        print('wrong serial number')
    else:
        del f[s_no]


def search_fruit():
    print('a,A => search by name \n b,B => search by rate')
    choice = input('enter choice: ')
    if choice == 'a' or choice == 'A':
        for i in f.values():
            name = input('Enter fruit name to search : ')
            if i['fruit_name'] == name:
                print(
                    f" {i['fruit_id']} | {i['fruit_name']} |{i['Fruit_rate']} | {i['imported_from']} |{i['imported_date']} | {i['buy_price']}  ")
            else:
                print('wrong fruit name ')
    elif choice == 'b' or choice == 'B':
        for v in f.values():
            rate = float(input('provide rate for searching like xx.xx'))
            if v['fruit_rate'] == rate:
                print(
                    f" {v['fruit_id']} | {v['fruit_name']} |{v['Fruit_rate']} | {v['imported_from']} |{v['imported_date']} | {v['buy_price']}  ")
            else:
                print('Not available with this price')


def change_fruit():
    s_no = int(input('Enter serial number : '))
    if s_no not in f.keys():
        print('Please provide right serial number ')
    else:
        print('modify fruit data')
        f[s_no]['fruit_name'] = input('Enter new fruit name :')
        f[s_no]['fruit_rate'] = input('Enter new rate : ')
        print('fruit name modified successfully ')


def add_to_cart():
    for i in f.keys():
        print('-'*10)
        print(f'fruit ids :  {i} ')

        print('-'*10)

    print('press on fruit id number to add to cart ')
    cart.append(f[int(input('enter fruit id to add on cart : '))])
    print('Fruit added in the cart successfully')


def diplay_fruit():
    if len(f) == 0:
        print('!' * 30)
        print('There is no fruit available')
    else:
        for i, j in f.items():
            print(
                f" {i} | {j['fruit_name']} |{j['Fruit_rate']} | {j['imported_from']} |{j['imported_date']} | {j['buy_price']}  ")


def display_cart():
    print(cart)


def delete_from_cart():
    display_cart()
    print('*'*20)
    s_no = int(input(('Enter fruit_id for delete fruit from cart : ')))
    cart.remove(f[s_no])
    print(f'fruit removed from cart !!!!')


while True:
    main_menu()

    ch = int(input('Enter choice : '))

    if ch == 1:
        # add fruit
        add_fruit()

    elif ch == 2:
        # delete fruit name
        delete_fruit()
    elif ch == 3:
        # search fruit by name and rate
        search_fruit()

    elif ch == 4:
        # change fruit name and rate
        change_fruit()

    elif ch == 5:
        # add to cart
        add_to_cart()

    elif ch == 6:
        # display
        diplay_fruit()
    elif ch == 7:
        # display cart
        display_cart()

    elif ch == 8:
        # delete item from cart
        delete_from_cart()
    elif ch == 9:
        break
    else:
        print('Invalid choice')
