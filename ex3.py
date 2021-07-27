from ex2 import * 
import pandas as pd 


def verify_input(command, type):
    con = False
    while con == False:
        try:
            var = type(input(command))
            con = True

        except ValueError:
            con = False

    return var


def verify_date_input(command):
    con = False
    while con == False:
        try:
            date_str = input(f'Enter the {command} date (DD-MM-YY): ')
            date = datetime.datetime.strptime(date_str, '%d-%m-%y').date()
            con = True

        except ValueError:
            con = False

    return date


class Singleton(type): # su dung lai lop da khoi tao
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Table(metaclass = Singleton):
    def __init__(self):
        self.table ={}
        self.df_file = []

    def add(self, obj):
        pass

    def find_id(self,id):
        try:
            a = self.table[id]
            return a 
        except:
            print('Khong tim thay id')

    def read(self):
        for i in self.table:
            print(self.table[i])

    def dicard(self, id):
        try:
            del self.table[id] 
        except:
            print('Khong ton tai id')

    def save(self,filename):
        for i in self.table:
            self.df_file.append(vars(self.table[i]))
        df_file = pd.DataFrame(self.df_file)
        df_file.to_csv(f'{filename}.csv')
        return

        
class CategoriesTable(Table):
    def add(self, name, des):
        obj = Categories(name, des)
        id = obj.get_id()
        self.table[id] = obj


class SuppliersTable(Table):
    def add(self, name, contact_name, address, city, postcode, country):
        obj = Suppliers(name, contact_name, address, city, postcode, country)
        id = obj.get_id()
        self.table[id] = obj 


class ShippersTable(Table):
    def add(self,name, phone):
        obj = Shippers(name, phone)
        id = obj.get_id()
        self.table[id] = obj  


class EmployeesTable(Table):
    def add(self, lname, fname, birth, photo, notes):
        obj = Employees(lname, fname, birth, photo, notes)
        id = obj.get_id()
        self.table[id] = obj  


class CustomersTable(Table):
    def add(self,name, contact_name, address, city, postcode, country):
        obj = Customers(name, contact_name, address, city, postcode, country)
        id = obj.get_id()
        self.table[id] = obj  


class ProductsTable(Table):
    def add(self, name, supID, catID, unit, price):
        obj = Products(name, supID, catID, unit, price)
        id = obj.get_id()
        self.table[id] = obj  


class OrdersTable(Table):
    def add(self,cusID, empID, order_date, shipID):
        obj = Orders(cusID, empID, order_date, shipID)
        id = obj.get_id()
        self.table[id] = obj  


class OrderDetailsTable(Table):
    def add(self,orderID, proID, quantity):
        obj = OrderDetails(orderID, proID, quantity)
        id = obj.get_id()
        self.table[id] = obj  


# run  + test
"""
c = CategoriesTable()
c.add('quan ao', 'good')
c.add('giay dep','good')
c.add('banh my','bad')
c.read()
print('-------------')
c.dicard(8)
c.read()

d = SuppliersTable()
d.add('trung','aws','HN','VN',1000,'VN')
d.add('trung','aws','HN','VN',1001,'VN')
d.add('trung','aws','HN','VN',1002,'VN')
d.read()
print('-------------')
d.dicard(2)
d.read()
print('-------------')
e = ProductsTable()
e.add('bimbim', 2, 5, 2, 1)
e.read()

c.save('categorial')
d.save('supplier')
"""


class Application:

    @staticmethod
    def input_data():
        while True:
            table = input('Enter the table you want to input data (done to exit): ')
            table = table.capitalize()
            
            if table == 'Customers':
                name = input('Enter the customer name: ')
                contact = input('Enter the customer contact name: ')
                address = input('Enter the customer address: ')
                city = input('Enter the customer city: ')
                postal_code = verify_input('Enter the city postal code: ', int)
                country = input('Enter the customer country: ')
                t1 = CustomersTable()
                t1.add(name, contact, address, city, postal_code, country)
                q2 = input('Save file Y/N')
                if q2 == 'Y':
                    t1.save('Customers')
                else:
                    continue

            elif table == 'Employees':
                last_name = input('Enter the employee last name: ')
                first_name = input('Enter the employee first name: ')
                birth_date = verify_date_input('employee birth')
                photo = input('Enter the file name of employee photo: ')
                notes = input('Enter notes for employee: ')
                t2 = EmployeesTable()
                t2.add(last_name, first_name, birth_date, photo, notes)
                q2 = input('Save file Y/N')
                if q2 == 'Y':
                    t2.save('Employees')
                else:
                    continue

            elif table == 'Categories':
                cat_name = input('Enter the category name: ')
                descript = input('Enter the category description: ')
                t3 = CategoriesTable()
                t3.add(cat_name, descript)
                q2 = input('Save file Y/N')
                if q2 == 'Y':
                    t3.save('Categories')
                else:
                    continue

            elif table == 'Shippers':
                ship_name = input('Enter the shipper name: ')
                phone = input('Enter the shipper phone number: ')
                t4 = ShippersTable()
                t4.add(ship_name, phone)
                q2 = input('Save file Y/N')
                if q2 == 'Y':
                    t4.save('Shippers')
                else:
                    continue


            elif table == 'Suppliers':
                sup_name = input('Enter the supplier name: ')
                contact = input('Enter the supplier contact name: ')
                address = input('Enter the supplier address: ')
                city = input('Enter the supplier city: ')
                postal_code = verify_input('Enter the city postal code: ', int)
                country = input('Enter the supplier country: ')
                phone = input('Enter the supplier phone number: ')
                t5 = SuppliersTable()
                t5.add(sup_name, contact, address, city, postal_code, country, phone)
                q2 = input('Save file Y/N')
                if q2 == 'Y':
                    t5.save('Suppliers')
                else:
                    continue

            elif table == 'Orders':
                cus_id = verify_input('Enter customer ID: ', int)
                emp_id = verify_input('Enter employee ID: ', int)
                order_date = verify_date_input('order')
                shipper_id = verify_input('Enter shipper ID: ', int)
                t6 = OrdersTable()
                t6.add(cus_id, emp_id, order_date, shipper_id)
                q2 = input('Save file Y/N')
                if q2 == 'Y':
                    t6.save('Orders')
                else:
                    continue

            elif table == 'Products':
                prod_name = input('Enter product name: ')
                sup_id = verify_input('Enter the supplier ID: ', int)
                cat_id = verify_input('Enter the category ID: ', int)
                unit = input('Enter the product unit: ')
                price = verify_input('Enter the product price: ', float)
                t7 = ProductsTable()
                t7.add(prod_name, sup_id, cat_id, unit, price)
                q2 = input('Save file Y/N')
                if q2 == 'Y':
                    t7.save('Products')
                else:
                    continue

            elif table == 'Orderdetails':
                order_id = verify_input('Enter the order ID: ', int)
                prod_id = verify_input('Enter the product ID: ', int)
                quantity = verify_input('Enter the order quantity:', int)
                t8 = OrderDetailsTable()
                t8.add(order_id, prod_id, quantity)
                q2 = input('Save file Y/N')
                if q2 == 'Y':
                    t8.save('OrderDetails')
                else:
                    continue

            elif table.lower() == 'done':
                exit()


test = Application()
test.input_data()
