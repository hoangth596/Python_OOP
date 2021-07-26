class Customers:
    __id = 0
    def __init__(self, name, phone):
        Customers.__id += 1
        self.CustomerID = Customers.__id
        self.CustomerName = name
        self.Phone = phone


class Salesperson:
    __id = 0
    def __init__(self, name):
        Salesperson.__id += 1
        self.SalespersonID = Salesperson.__id
        self.SalespersonName = name


class Cars:
    __id = 0
    def __init__(self, serial, name, cus_id):
        Cars.__id += 1
        self.CarID = Cars.__id
        self.SerialNumber = serial
        self.CarName = name
        self.CustomerID = cus_id


