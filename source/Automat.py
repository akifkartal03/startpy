
import random


class Automat:

    def __init__(self, cash_box=None, products=None, total_money = 0.0, user_money = 0.0,
                 user_request=None, user_request_money = 0.0, remainder = 0.0):

        self.cash_box = {'25Kurus': 0, '50Kurus': 0, '1TL': 0}
        self.products = [

            {'id': 1, 'name': 'su', 'stockNumber': 0, 'price': 50, 'type': 0},
            {'id': 2, 'name': 'cay', 'stockNumber': 0, 'price': 1, 'type': 1},
            {'id': 3, 'name': 'kahve', 'stockNumber': 0, 'price': 1.5, 'type': 1},
            {'id': 4, 'name': 'cikolata', 'stockNumber': 0, 'price': 1.75, 'type': 1},
            {'id': 5, 'name': 'biskuvi', 'stockNumber': 0, 'price': 2, 'type': 1}
        ]
        self.__fill_cash_info_from_file()
        self.__fill_product_info_from_file()
    def run_machine(self):

        n = int(input("Enter number of run time of machine:"))
        for _ in range(n):
            self.user_money = 0.0
            self.user_request = {}
            self.remainder = 0.0
            self.user_request_money = 0.0
            self.__get_money_info_from_user()
            self.__get_product_request_from_user()
            if self.__check_money_press():
                print("Money press to the machine your request was canceled!!")
                continue
            else:
                if self.__check_enough_money():
                    if self.user_money >= self.user_request_money:
                        self.__update_info()
                else:
                    print("Machine don't have enough money operation was canceled!!")
                    continue

    def __fill_cash_info_from_file(self):
        file_name = 'urunler.txt'
        try:
            with open(file_name) as f_obj:
                lines = f_obj.readlines()
            quantities = lines[0].split(",")  # get money info from file
            self.cash_box['25Kurus'] = int(quantities[0])
            self.cash_box['50Kurus'] = int(quantities[1])
            self.cash_box['1TL'] = int(quantities[2])
        except Exception as e:
            print(e, type(e))
        else:
            self.total_money = int(quantities[0])*0.25 + \
                int(quantities[1])*0.50 + int(quantities[0])*1

    def __fill_product_info_from_file(self):
        # only stock number and price will be updated
        file_name = 'urunler.txt'
        try:
            with open(file_name) as f_obj:
                lines = f_obj.readlines()
            for i in range(1, 6):
                information = lines[i].split(",")
                self.products[i-1]['stockNumber'] = int(information[2])
                values = information[3].split()
                self.products[i - 1]['price'] = float(values[0])
                if values[1] == 'Kurus':
                    self.products[i - 1]['type'] = 0
                else:
                    self.products[i - 1]['type'] = 1

        except Exception as e:
            print(e, type(e))

    def __update_stock(self, id, new_stock):
        if new_stock < 0:
            print("invalid stock amount try again!")
            return
        if id <= 0 or id > 5:
            print("invalid id try again!")
            return
        self.products[id-1]['stockNumber'] = new_stock

    def __get_money_info_from_user(self):
        finish = False
        self.user_money = 0.0
        while not finish:
            self.__show_menu1()
            input = self.__get_user_input(4)
            if input == 1:
                self.user_money = self.user_money + 0.25
            elif input == 2:
                self.user_money = self.user_money + 0.50
            elif input == 3:
                self.user_money = self.user_money + 1
            else:
                finish = True
        print("You gave %.2f TL money." % self.user_money)

    def __show_menu1(self):
        print("\t *** Money Menu ****")
        print("1 - 25 Kurus")
        print("2 - 50 Kurus")
        print("3 - 1 TL")
        print("4 - Exit")

    def __get_user_input(self, upper_bound):
        try:
            number = int(input("Choice: "))
        except Exception:
            print("Enter a number!")
        else:
            while number < 1 or number > upper_bound:
                print("Enter a number between 1 and %d!" % upper_bound)
                number = int(input("Choice: "))
            return number

    def __get_product_request_from_user(self):
        finish = False
        while not finish:
            self.__show_menu2()
            input = self.__get_user_input(7)
            if input == 1:
                if '1' in self.user_request.keys():
                    self.user_request['1'] = self.user_request['1'] + 1
                else:
                    self.user_request['1'] = 1
            elif input == 2:
                if '2' in self.user_request.keys():
                    self.user_request['2'] = self.user_request['2'] + 1
                else:
                    self.user_request['2'] = 1
            elif input == 3:
                if '3' in self.user_request.keys():
                    self.user_request['3'] = self.user_request['3'] + 1
                else:
                    self.user_request['3'] = 1
            elif input == 4:
                if '4' in self.user_request.keys():
                    self.user_request['4'] = self.user_request['4'] + 1
                else:
                    self.user_request['4'] = 1
            elif input == 5:
                if '5' in self.user_request.keys():
                    self.user_request['5'] = self.user_request['5'] + 1
                else:
                    self.user_request['5'] = 1
            elif input == 6:
                self.__reset()
            else:
                finish = True
        for id, quan in self.user_request.items():
            self.user_request_money = self.user_request_money + \
                self.__get_price(int(id)) * quan
        if self.user_money < self.user_request_money:
            print("your money is not enough to buy these!!")
            print("Take your money and try again!!")

    def __show_menu2(self):
        print("\t *** Product Menu ****")
        print("1 - Su")
        print("2 - Çay")
        print("3 - Kahve")
        print("4 - Çikolata")
        print("5 - Biskivu")
        print("6 - Reset")
        print("7 - Exit")

    def __get_price(self, id):
        if self.products[id-1]['type'] == 0:
            return (self.products[id-1]['price']) / 100.0
        else:
            return self.products[id - 1]['price']

    def __get_stock(self, id):
        return self.products[id-1]['stockNumber']

    def __reset(self):
        self.run_machine()

    def __check_money_press(self):
        if random.randint(1, 4) == 2:
            return True
        else:
            return False

    def __get_remainder(self):
        if self.user_money < self.user_request_money:
            # don't update anything
            self.remainder = 0.0
        elif self.user_money == self.user_request_money:
            self.remainder = 0.0
        else:
            self.remainder = self.user_money - self.user_request_money

    def __check_enough_money(self):
        self.__get_total_money()
        self.__get_remainder()
        if self.remainder > self.total_money:
            return False
        else:
            return True

    def __update_info(self):
        rem = self.remainder
        if rem != 0.0:
            if rem >= 1 and self.cash_box['1TL'] > 0:
                absolute = int(rem)
                if absolute <= self.cash_box['1TL']:
                    self.cash_box['1TL'] = self.cash_box['1TL'] - absolute
                    rem = rem - absolute
                    if rem > 0:
                        if rem >= 0.50 and self.cash_box['50Kurus'] > 0:
                            rem = rem - 0.50
                            self.cash_box['50Kurus'] = self.cash_box['50Kurus'] - 1
                            if rem > 0:
                                if self.cash_box['25Kurus'] > 0:
                                    rem = rem - 0.25
                                    self.cash_box['25Kurus'] = self.cash_box['25Kurus'] - 1
                                else:
                                    print(
                                        "The cash box will give you more money to complete its operation")
                                    if self.cash_box['50Kurus'] > 0:
                                        rem = rem - 0.50
                                        self.cash_box['50Kurus'] = self.cash_box['50Kurus'] - 1
                                    else:
                                        rem = rem - 1
                                        self.cash_box['1TL'] = self.cash_box['1TL'] - 1

                        elif rem >= 0.50:
                            amount = rem / 0.25
                            self.cash_box['25Kurus'] = self.cash_box['25Kurus'] - amount
                            rem = 0.0
                        else:
                            self.cash_box['25Kurus'] = self.cash_box['25Kurus'] - 1
                            rem = 0.0
                else:
                    rem = rem - self.cash_box['1TL']
                    self.cash_box['1TL'] = 0
                    if rem > 0:
                        abs50 = int(rem / 0.50)
                        if abs50 <= self.cash_box['50Kurus']:
                            self.cash_box['50Kurus'] = self.cash_box['50Kurus'] - abs50
                            rem = rem - abs50*0.50
                            if rem > 0:
                                self.cash_box['25Kurus'] = self.cash_box['25Kurus'] - 1
                                rem = rem - 0.25
                        else:
                            rem = rem - self.cash_box['50Kurus']*0.50
                            self.cash_box['50Kurus'] = 0
                            if rem > 0:
                                abs25 = rem / 0.25
                                rem = rem - abs25 * 0.25
                                self.cash_box['25Kurus'] = self.cash_box['25Kurus'] - abs25
            elif rem > 0:
                abs50 = int(rem / 0.50)
                if abs50 <= self.cash_box['50Kurus']:
                    self.cash_box['50Kurus'] = self.cash_box['50Kurus'] - abs50
                    rem = rem - abs50 * 0.50
                    if rem > 0:
                        self.cash_box['25Kurus'] = self.cash_box['25Kurus'] - 1
                        rem = rem - 0.25
                else:
                    rem = rem - self.cash_box['50Kurus'] * 0.50
                    self.cash_box['50Kurus'] = 0
                    if rem > 0:
                        abs25 = rem / 0.25
                        rem = rem - abs25 * 0.25
                        self.cash_box['25Kurus'] = self.cash_box['25Kurus'] - abs25
            print("Your remainder money was given to you as %.2f" % self.remainder)
        self.__update_product_info()
        self.__write_to_file()

    def __update_product_info(self):
        for id, quan in self.user_request.items():
            real_id = int(id)
            self.__update_stock(real_id, self.__get_stock(real_id) - quan)

    def __write_to_file(self):
        filename = 'urunler.txt'
        with open(filename, 'w') as f:
            f.write(str(self.cash_box['25Kurus']))
            f.write(",")
            f.write(str(self.cash_box['50Kurus']))
            f.write(",")
            f.write(str(self.cash_box['1TL']))
            f.write("\n")
            for i in range(0, 5):
                f.write(str(self.products[i]['id']))
                f.write(",")
                f.write(str(self.products[i]['name']))
                f.write(",")
                f.write(str(self.products[i]['stockNumber']))
                f.write(",")
                f.write(str(self.products[i]['price']))
                f.write(" ")
                if self.products[i]['type'] == 0:
                    f.write("Kurus")
                else:
                    f.write("TL")
                f.write("\n")

    def __get_total_money(self):
        self.total_money = 0.0
        self.total_money = self.total_money + self.cash_box['25Kurus']*0.25 +\
            self.cash_box['50Kurus']*0.50 + self.cash_box['1TL']

