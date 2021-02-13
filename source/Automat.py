class Automat:
    cash_box = {}
    products = []
    total_money = 0.0
    user_money = 0.0
    user_request = {}
    remainder = 0.0

    def __init__(self):
        self.cash_box = {'25Kurus': 0, '50Kurus': 0, '1TL': 0}
        self.products = [

            {'id': 1, 'name': 'su', 'stockNumber': 0, 'price': 50, 'type': 0},
            {'id': 2, 'name': 'cay', 'stockNumber': 0, 'price': 1, 'type': 1},
            {'id': 3, 'name': 'kahve', 'stockNumber': 0, 'price': 1.5, 'type': 1},
            {'id': 4, 'name': 'cikolata', 'stockNumber': 0, 'price': 1.75, 'type': 1},
            {'id': 5, 'name': 'biskuvi', 'stockNumber': 0, 'price': 2, 'type': 1}
        ]

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
                self.products[i-1]['stockNumber'] = information[2]
                values = information[3].split()
                self.products[i - 1]['price'] = values[0]
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
                self.user_request = {}
            else:
                finish = True
        total_user_req = 0.0
        for id, quan in self.user_request.items():
            total_user_req = total_user_req + self.__get_price(int(id)) * quan
        if self.user_money < total_user_req:
            print("your money is not enough to buy these!!")
            print("Take your money and try again!!")
            return False
        else:
            return True

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
            return self.products[id-1]['price'] / 100
        else:
            return self.products[id - 1]['price']

    def __get_stock(self, id):
        return self.products[id-1]['stockNumber']

    def __reset(self):
        print("incomplete")

    def __check_money_press(self):
        print("incomplete")
        return False

    def __get_remainder(self):
        print("incomplete")
        return 0.0

    def __check_enough_money(self):
        print("incomplete")
        return False

    def __update_cash_and_product_info(self):
        print("incomplete")

##x = Automat()
# x.get_money_info_from_user()
# x.get_product_request_from_user()
