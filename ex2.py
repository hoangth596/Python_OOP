import datetime
import os
import pandas as pd

def get_index(table_name):
    file_path = 'Database Exercise 03/' + table_name + '.csv'
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        index = len(pd.read_csv(file_path)) + 1
    else:
        index = 1

    return index


class Categories: # thu tu tao obj 1
    """
    This class contain CategoryID, CategoryName
    and Description from Categories table
    """
    
    def __init__(self, name, des):
        self.__catID = Categories.get_index('Categories')
        self.__validate_type(name, des)
        self.cat_name = name 
        self.cat_des = des
    
    @classmethod
    def get_index(cls,table_name):
        file_path = table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index = 1

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

    def __init__(self, name, contact_name, address, city, postcode, country, phone):
        self.__supID = Suppliers.get_index('Suppliers')
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
        file_path = table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index = 1

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

    def __init__(self, name, phone):
        self.__id = Shippers.get_index('Shippers')
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

    def __init__(self, lname, fname, birth, photo, notes):
        self.__empID = Employees.get_index('Employees')
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
        assert type(birth) == datetime.date
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

    def __init__(self, name, contact_name, address, city, postcode, country):
        self.__cusID = Customers.get_index('Customers')
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

    def __init__(self, name, supID, catID, unit, price):
        self.__proID = Products.get_index('Products')
        self.__validate_type(name, supID, catID, unit, price)
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
    def __validate_type(name, supID, catID, unit, price):
        assert type(name) == str
        assert type(supID) == int
        assert type(catID) == int
        assert type(unit) == str
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

    def __init__(self, cusID, empID, order_date, shipID):
        self.__orderID = Orders.get_index('Orders')
        self.__validate_type(cusID, empID, order_date, shipID)
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


    @staticmethod
    def __validate_type(cus_id, employ_id, order_date, shipper_id):
        assert type(cus_id) == int
        assert type(employ_id) == int
        assert type(order_date) == datetime.date
        assert type(shipper_id) == int


    def get_id(self):
        return self.__orderID 


class OrderDetails: # thu tu tao obj 
    """
    This class containt OrderDetailID, OrderId, ProductId, Quantity
    from OrderDetails table
    """

    def __init__(self, orderID, proID, quantity):
        self.__ord_detail_ID = OrderDetails.get_index('OrderDetails')
        self.__validate_type(orderID, proID, quantity)
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


    @staticmethod
    def __validate_type(ord_id, prod_id, quantity):
        assert type(ord_id) == int
        assert type(prod_id) == int
        assert type(quantity) == int

        
    def get_id(self):
        return self.__ord_detail_ID


def test(a,b):
    return a+b 