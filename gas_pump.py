from datetime import datetime


def gas_price(gas_type):
    if gas_type == 'regular':
        return 2.5
    elif gas_type == 'plus':
        return 2.8
    elif gas_type == 'premium':
        return 3.0
    elif gas_type == 'e-85':
        return 2.35


def main():
    print('\nHello Chevron\n')

    while True:
        payment = input('Prepay or pay after?').strip().lower()
        if payment == 'prepay':
            print('\n(Plus)', '(Regular)', '(Premium)', '(E-85)')
            gas_type = input('\nWhat Type Of Gas You Want?').strip().lower()
            amount = float(input('\n How much are you paying?'))
            cost = amount / gas_price(gas_type)
            print(cost)
            print('\n ${:.2f}:  {:.2f}      gallons of gas!'.format(
                amount, cost))
            break
        elif payment == 'pay after':
            print('\ninsert card')
            print('\n(Plus)', '(Regular)', '(Premium)', '(E-85)')
            gas_type = input('\nWhat Type Of Gas You Want?').strip().lower()
            amount = float(input('\n How much are you paying?')).digit
            cost = amount / gas_price(gas_type)
            print(cost)
            print('\n ${:.2f}:  {:.2f}      gallons of gas!'.format(
                amount, cost))
            break
        else:
            print('invalid response')

    receipt = input('Do you want a receipt?')
    if receipt == ('yes'):
        print('\n......printing.....')
        print('\nEnjoy the rest of your day')
        print('\nThanks for shopping with chevron fueling')

    store_in_workshop(gas_type, amount)


def store_in_workshop(gas_type, amount):
    time = datetime.now()
    text = '\n{}, {}, {}'.format(time, gas_type, amount)

    with open('store_money.txt', 'a') as file:
        file.write(text)


if __name__ == '__main__':
    main()
