from ex2 import * 
import pandas as pd 


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
    def add(self,lname, fname, birth, photo, notes):
        obj = Employees(lname, fname, birth, photo, notes)
        id = obj.get_id()
        self.table[id] = obj  

class CustomersTable(Table):
    def add(self,name, contact_name, address, city, postcode, country):
        obj = Customers(name, contact_name, address, city, postcode, country)
        id = obj.get_id()
        self.table[id] = obj  

class ProductsTable(Table):
    def add(self, name, unit, price, catID, supID):
        obj = Products(name, unit, price, catID, supID)
        id = obj.get_id()
        self.table[id] = obj  


class OrderTable(Table):
    def add(self,cusID, empID, shipID, order_date):
        obj = Order(cusID, empID, shipID, order_date)
        id = obj.get_id()
        self.table[id] = obj  

class OrderDetailTable(Table):
    def add(self,orderID, proID, quantity):
        obj = OrderDetail(orderID, proID, quantity)
        id = obj.get_id()
        self.table[id] = obj  


# run  + test

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