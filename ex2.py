
class Categories: # thu tu tao obj 1
    __index = 0
    def __init__(self, name, des):
        Categories.__index += 1
        self.cat_name = name 
        self.cat_des = des 
        self.__catID = self.__index

    def get_id(self):
        return self.__catID

    def __str__(self):
        return f'Categorical : {self.get_id()},{self.cat_name}, {self.cat_des}'

class Suppliers: # thu tu tao obj 2
    __index = 0
    def __init__(self, name, contact_name, address, city, postcode, country):
        Suppliers.__index += 1
        self.__supID = self.__index 
        self.sup_name = name 
        self.sup_contact_name = contact_name
        self.sup_address = address 
        self.sup_city = city 
        self.sup_postcode = postcode 
        self.sup_country = country 

    def get_id(self):
        return self.__supID
    def __str__(self):
        return f'Suppliers : {self.get_id()},{self.sup_name}, {self.sup_contact_name}, {self.sup_address }, {self.sup_city}, {self.sup_postcode},{self.sup_country}'

class Products: # thu tu tao obj 6
    __index = 0
    def __init__(self, name, unit, price, catID, supID):
        Products.__index += 1
        self.__proID = self.__index
        self.pro_name = name 
        self.pro_unit = unit 
        self.pro_price = price 
        self.pro_catID = catID
        self.pro_supID = supID

    def get_id(self):
        return self.__proID
    def __str__(self):
        return f'Products : {self.get_id()},{self.pro_name}, {self.pro_unit},{self.pro_price}, {self.pro_catID}, {self.pro_supID} '

class Shippers: # # thu tu tao obj 3
    __index = 0
    def __init__(self, name, phone):
        Shippers.__index += 1
        self.ship_name = name 
        self.ship_phone = phone 
        self.__shipID = self.__index

    def get_id(self):
        return self.__shipID

    def __str__(self):
        return f'Shippers : {self.get_id()},{self.ship_name},{self.ship_phone}'

class Employees: # # thu tu tao obj 4
    __index = 0
    def __init__(self, lname, fname, birth, photo, notes):
        Employees.__index += 1
        self.__empID = self.__index
        self.emp_lname = lname
        self.emp_fname = fname
        self.emp_birth = birth
        self.emp_photo = photo
        self.emp_notes = notes 

    def get_id(self):
        return self.__empID

    def __str__(self):
        return f'Employees : {self.get_id()},{self.emp_lname},{self.emp_fname},{self.emp_birth},{self.emp_photo},{self.emp_notes}'


class Customers: # # thu tu tao obj 5
    __index = 0
    def __init__(self, name, contact_name, address, city, postcode, country):
        Customers.__index += 1
        self.__cusID = self.__index 
        self.cus_name = name 
        self.cus_contact_name = contact_name 
        self.cus_address = address 
        self.cus_city = city 
        self.cus_postcode = postcode 
        self.cus_country= country
    
    def get_id(self):
        return self.__cusID

class Order: # thu tu tao obj 7
    __index = 0
    def __init__(self, cusID, empID, shipID, order_date):
        Order.__index += 1
        self.__orderID = self.__index 
        self.ord_cusID = cusID
        self.ord_empID = empID
        self.ord_shipID = shipID
        self.ord_order_date = order_date

    def get_id(self):
        return self.__orderID 

class OrderDetail: # thu tu tao obj 
    __index = 0
    def __init__(self, orderID, proID, quantity):
        OrderDetail.__index += 1
        self.__ord_detail_ID = self.__index 
        self.ord_detail_orderID = orderID 
        self.ord_detail_proID = proID 
        self.ord_detail_quantity = quantity 
        
    def get_id(self):
        return self.__ord_detail_ID


def test(a,b):
    return a+b 