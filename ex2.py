
import datetime
import os
import pandas as pd


class Categories: # thu tu tao obj 1
    """
    This class contain CategoryID, CategoryName
    and Description from Categories table
    """

    check = False
    __index = 0
    def __init__(self, name, des):
        if Categories.check == False:
            self.__catID = Categories.get_index('Categories')
        else:
            Categories.__index += 1
            self.__catID = Categories.__index
        self.__validate_type(name, des)
        self.cat_name = name 
        self.cat_des = des
    
    @classmethod
    def get_index(cls,table_name):
        file_path = '/content/' + table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
            cls.check = True 
        else:
            cls.__index += 1
        return cls.__index

    @staticmethod
    def __validate_type(name, description) -> None:
        assert type(name) == str
        assert type(description) == str


    def get_id(self):
        return self.__catID


    def __str__(self):
        return f'Categorical : {self.get_id()},{self.cat_name}, {self.cat_des}'

class Suppliers: # thu tu tao obj 2
    """
    This class contains SupplierID, SupplierName, ContactName, Address,
    City, PostalCode, Country and Phone from Suppliers table
    """
    check = False
    __index = 0
    def __init__(self, name, contact_name, address, city, postcode, country, phone):
        if Suppliers.check == False:
            self.__supID = Suppliers.get_index('Suppliers')
        else:
            Suppliers.__index += 1
            self.__supID = Suppliers.__index

        self.__validate_type(name, contact_name, address, city, postcode, country, phone)
        self.sup_name = name 
        self.sup_contact_name = contact_name
        self.sup_address = address 
        self.sup_city = city 
        self.sup_postcode = postcode 
        self.sup_country = country
        self.sup_phone = phone


    @classmethod
    def get_index(cls,table_name):
        file_path =  table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
            cls.check = True 
        else:
            cls.__index += 1
        return cls.__index


    @staticmethod
    def __validate_type(name, contact_name, address,
                        city, postal_code, country, phone):
        assert type(name) == str
        assert type(contact_name) == str
        assert type(address) == str
        assert type(city) == str
        assert type(postal_code) == int
        assert type(country) == str
        assert type(phone) == str


    def get_id(self):
        return self.__supID


    def __str__(self):
        return f'Suppliers : {self.get_id()},{self.sup_name}, {self.sup_contact_name}, {self.sup_address }, {self.sup_city}, {self.sup_postcode},{self.sup_country}'


class Shippers: # # thu tu tao obj 3
    """
    This class containt ShipperID, ShipperName and Phone
    from Shippers table
    """

    check = False
    __index = 0
    def __init__(self, name, phone):
        if Shippers.check == False:
            self.__shipID = Shippers.get_index('Shippers')
        else:
            Suppliers.__index += 1
            self.__shipID = Shippers.__index

        self.__validate_type(name, phone)
        self.ship_name = name 
        self.ship_phone = phone

    @classmethod
    def get_index(cls,table_name):
        file_path = table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index = 1

        return cls.__index

    @staticmethod
    def __validate_type(name, phone) -> None:
        assert type(name) == str
        assert type(phone) == str


    def get_id(self):
        return self.__shipID


    def __str__(self):
        return f'Shippers : {self.get_id()},{self.ship_name},{self.ship_phone}' 

class Employees: # # thu tu tao obj 4
    """
    This class contain EmployeeID, LastName, FirstName,
    BirthDate, Photo and Notes from Employees table
    """

    check = False
    __index = 0
    def __init__(self, lname, fname, birth, photo, notes):
        if Employees.check == False:
            self.__empID = Employees.get_index('Employees')
        else:
            Employees.__index += 1
            self.__empID = Employees.__index
        self.__validate_type(lname, fname, birth, photo, notes)
        self.emp_lname = lname
        self.emp_fname = fname
        self.emp_birth = birth
        self.emp_photo = photo
        self.emp_notes = notes

    @classmethod
    def get_index(cls,table_name):
        file_path = table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index = 1

        return cls.__index

    @staticmethod
    def __validate_type(lname, fname, birth, photo, notes) -> None:
        assert type(lname) == str
        assert type(fname) == str
        assert type(birth) == str
        assert type(photo) == str
        assert type(notes) == str


    def get_id(self):
        return self.__empID


    def __str__(self):
        return f'Employees : {self.get_id()},{self.emp_lname},{self.emp_fname},{self.emp_birth},{self.emp_photo},{self.emp_notes}'


class Customers: # # thu tu tao obj 5
    """
    This class contain the CustomerID, CustomerName, ContactName,
    Address, City, PostalCode and Country from Customers table
    """

    check = False
    __index = 0
    def __init__(self, name, contact_name, address, city, postcode, country):
        if Customers.check == False:
            self.__cusID = Customers.get_index('Customers')
        else:
            Customers.__index += 1
            self.__cusID = Customers.__index
        self.__validate_type(name, contact_name, address, city, postcode, country)
        self.cus_name = name 
        self.cus_contact_name = contact_name 
        self.cus_address = address 
        self.cus_city = city 
        self.cus_postcode = postcode 
        self.cus_country= country

    
    @classmethod
    def get_index(cls,table_name):
        file_path = table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index = 1

        return cls.__index

    @staticmethod
    def __validate_type(name, contact_name, address, city, postcode, country) -> None:
        assert type(name) == str
        assert type(contact_name) == str
        assert type(address) == str
        assert type(city) == str
        assert type(postcode) == int
        assert type(country) == str

    
    def get_id(self):
        return self.__cusID

class Products: # thu tu tao obj 6
    """
    This class contains ProductID, SupplierID, CatergoryID,
    Unit and Price from Products table
    """

    check = False
    __index = 0
    def __init__(self, name, supID, catID, unit, price):
        if Products.check == False:
            self.__proID = Products.get_index('Products')
        else:
            Products.__index += 1
            self.__proID = Products.__index 
        self.__validate_type(name, unit, price)
        self.pro_name = name 
        self.pro_unit = unit 
        self.pro_price = price 
        self.pro_catID = catID
        self.pro_supID = supID

    @classmethod
    def get_index(cls,table_name):
        file_path = table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index = 1

        return cls.__index
        
    @staticmethod
    def __validate_type(name, unit, price):
        assert type(name) == str

        assert type(unit) == int
        assert type(price) == float


    def get_id(self):
        return self.__proID


    def __str__(self):
        return f'Products : {self.get_id()}, {self.pro_name}, {self.pro_supID}, {self.pro_catID}, {self.pro_unit}, {self.pro_price}' 

class Orders: # thu tu tao obj 7
    """
    This class contain OrderID, CustomerID, EmployeeID,
    OrderDate and ShipperID from Orders table
    """

    check = False
    __index = 0
    def __init__(self, cusID, empID, order_date, shipID):
        if Orders.check == False:
            self.__orderID = Orders.get_index('Orders')
        else:
            Orders.__index += 1
            self.__orderID = Orders.__index 


        self.ord_cusID = cusID
        self.ord_empID = empID
        self.ord_shipID = shipID
        self.ord_order_date = order_date

    @classmethod
    def get_index(cls,table_name):
        file_path = table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index = 1

        return cls.__index


    def get_id(self):
        return self.__orderID 



class OrderDetails: # thu tu tao obj 
    """
    This class containt OrderDetailID, OrderId, ProductId, Quantity
    from OrderDetails table
    """

    check = False
    __index = 0
    def __init__(self,orderID, proID, quantity):
        if OrderDetails.check == False:
            self.__ord_detail_ID = OrderDetails.get_index('OrderDetails')
        else:
            OrderDetails.__index += 1
            self.__ord_detail_ID = OrderDetails.__index 
        self.ord_detail_orderID = orderID 
        self.ord_detail_proID = proID
        self.ord_detail_quantity = quantity

    @classmethod
    def get_index(cls,table_name):
        file_path = table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index = 1

        return cls.__index

   

        
    def get_id(self):
        return self.__ord_detail_ID 
    
a1 = Categories('car','4 banh')
a2 = Suppliers('AWS','USA','My','NY',10000,'Queen street','100')
a3 = Shippers('Shiper1','9002642')
a4 = Employees('Mc','Donal','13-12-2000','None','Good')
a5 = Customers('Mr','Baby','11Queen','NY',10000,'USA')
a6 = Products('Tesla',a1,a2,10,5000.)
a7 = Orders(a5, a4, '10-10-2021',a3)
a8 = OrderDetails(a7, a6, 2)
