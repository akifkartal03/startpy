class Automat:
    cash_box = {}
    products = []
    total_money = 0.0
    user_money = 0.0
    user_request = []
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

    def fill_cash_info_from_file(self):
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

    def fill_product_info_from_file(self):
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

    def update_stock(self, id, new_stock):
        print("incomplete")

    def get_money_info_from_user(self):
        print("incomplete")

    def get_product_request_from_user(self):
        print("incomplete")

    def reset(self):
        print("incomplete")

    def check_money_press(self):
        print("incomplete")
        return False

    def get_remainder(self):
        print("incomplete")
        return 0.0

    def check_enough_money(self):
        print("incomplete")
        return False

    def update_cash_and_product_info(self):
        print("incomplete")

#x = Automat()
# x.fill_product_info_from_file()
# for a in x.products:
    # print(a)
