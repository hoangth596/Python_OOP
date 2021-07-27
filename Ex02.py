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


class Customers:
    """
    This class contain the CustomerID, CustomerName, ContactName,
    Address, City, PostalCode and Country from Customers table
    """

    def __init__(self, name, contact, address, city, postal_code, country) -> None:
        self.__CustomerID = get_index('Customers')
        self.__validate_type(name, contact, address, city, postal_code, country)
        self.__CustomerName = name
        self.__ContactName = contact
        self.__Address = address
        self.__City = city
        self.__Postal_code = postal_code
        self.__Country = country


    @staticmethod
    def __validate_type(name, contact, address, city, postal_code, country) -> None:
        assert type(name) == str
        assert type(contact) == str
        assert type(address) == str
        assert type(city) == str
        assert type(postal_code) == int
        assert type(country) == str


class Employees:
    """
    This class contain EmployeeID, LastName, FirstName,
    BirthDate, Photo and Notes from Employees table
    """

    def __init__(self, last_name, first_name, birth_date, photo, notes) -> None:
        self.__EmployeeID = get_index('Employees')
        self.__validate_type(last_name, first_name, birth_date, photo, notes)
        self.__LastName = last_name
        self.__FirstName = first_name
        self.__BirthDate = birth_date
        self.__Photo = photo
        self.__Notes = notes


    @staticmethod
    def __validate_type(last_name, first_name, birth_date, photo, notes) -> None:
        assert type(last_name) == str
        assert type(first_name) == str
        assert type(birth_date) == datetime.date
        assert type(photo) == str
        assert type(notes) == str


class Categories:
    """
    This class contain CategoryID, CategoryName
    and Description from Categories table
    """

    def __init__(self, name, description) -> None:
        self.__CategoryID = get_index('Categories')
        self.__validate_type(name, description)
        self.__CategoryName = name
        self.__Description = description


    @staticmethod
    def __validate_type(name, description) -> None:
        assert type(name) == str
        assert type(description) == str


class Shippers:
    """
    This class containt ShipperID, ShipperName and Phone
    from Shippers table
    """

    def __init__(self, name, phone):
        self.__ShipperID = get_index('Shippers')
        self.__validate_type(name, phone)
        self.__ShipperName = name
        self.__Phone = phone

    
    @staticmethod
    def __validate_type(name, phone) -> None:
        assert type(name) == str
        assert type(phone) == str


class Suppliers:
    """
    This class contains SupplierID, SupplierName, ContactName, Address,
    City, PostalCode, Country and Phone from Suppliers table
    """

    def __init__(self, name, contact_name, address,
                 city, postal_code, country, phone):
        self.__SupplierID = get_index('Suppliers')
        self.__validate_type(postal_code)
        self.__SupplierName = name
        self.__ContactName = contact_name
        self.__Address = address
        self.__City = city
        self.__PostalCode = postal_code
        self.__Country = country
        self.__Phone = phone


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


class Orders:
    """
    This class contain OrderID, CustomerID, EmployeeID,
    OrderDate and ShipperID from Orders table
    """

    def __init__(self, cus_id, employ_id, order_date, shipper_id):
        self.__OrderID = get_index('Orders')
        self.__validate_type(cus_id, employ_id, order_date, shipper_id)
        self.__CustomerID = cus_id
        self.__EmployeeID = employ_id
        self.__OrderDate = order_date
        self.__ShipperID = shipper_id


    @staticmethod
    def __validate_type(cus_id, employ_id, order_date, shipper_id):
        assert type(cus_id) == int
        assert type(employ_id) == int
        assert type(order_date) == datetime.date
        assert type(shipper_id) == int


class Products:
    """
    This class contains ProductID, SupplierID, CatergoryID,
    Unit and Price from Products table
    """

    def __init__(self, product_name, sup_id, cat_id, unit, price):
        self.__ProductID = get_index('Products')
        self.__validate_type(product_name, sup_id, cat_id, unit, price)
        self.__ProductName = product_name
        self.__SupplierID = sup_id
        self.__CatergoryID = cat_id
        self.__Unit = unit
        self.__Price = price


    @staticmethod
    def __validate_type(product_name, sup_id, cat_id, unit, price):
        assert type(product_name) == str
        assert type(sup_id) == int
        assert type(cat_id) == int
        assert type(unit) == str
        assert type(price) == float


class OrderDetails:
    """
    This class containt OrderDetailID, OrderId, ProductId, Quantity
    from OrderDetails table
    """

    def __init__(self, ord_id, prod_id, quantity):
        self.__OderDetailID = get_index('OrderDetails')
        self.__validate_type(ord_id, prod_id, quantity)
        self.__OrderID = ord_id
        self.__ProductID = prod_id
        self.__Quantity = quantity


    @staticmethod
    def __validate_type(ord_id, prod_id, quantity):
        assert type(ord_id) == int
        assert type(prod_id) == int
        assert type(quantity) == int

