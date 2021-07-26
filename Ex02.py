from database_ex03.function import get_index
file_name_customer = "Customers.csv"
file_name_catergory = "Catergories.csv"
file_name_employees = "Employees.csv"
file_name_orders = "Orders.csv"
file_name_orderdetail = "OrderDetails.csv"
file_name_shipper = "Shippers.csv"
file_name_supplier = "Suppliers.csv"
file_name_product = "Products.csv"


class Customers:

    def __init__(self, name, contact, address,
                 city, postal_code, country):
        self.index = get_index(file_name_customer) + 1
        self.name = name
        self.contact = contact
        self.address = address
        self.city = city
        self.postalcode = postal_code
        self.country = country

    def save_information(self, file_name=file_name_customer):
        path = "./database_ex03/"
        line = "\n{},{},{},{},{},{},{}".format(
            self.index, self.name, self.contact, self.address, self.city, self.postalcode, self.country)
        with open(path + file_name, mode='a') as f:
            f.write(line)
            f.close()
        print('The information of customer {} has saved! '.format(self.name))


class Categories:

    def __init__(self, name, description):
        self.CatergoryId = get_index(file_name_catergory) + 1
        self.CatergoryName = name
        self.Decription = description

    def save_information(self, file_name=file_name_catergory):
        path = "./database_ex03/"
        line = "\n{},{},{}".format(
            self.CatergoryId, self.CatergoryName, self.Decription)
        with open(path + file_name, mode='a') as f:
            f.write(line)
            f.close()
        print('The information of Caterogry {} has saved! '.format(
            self.CatergoryName))


class Employees:

    def __init__(self, last_name, first_name, birth_date, photo, notes):
        self.EmployeeId = get_index(file_name_employees) + 1
        self.LastName = last_name
        self.FirstName = first_name
        self.BirthDate = birth_date
        self.Photo = photo
        self.Note = notes

    def save_information(self, file_name=file_name_employees):
        path = "./database_ex03/"
        line = "\n{},{},{}, {}, {}, {}".format(
            self.EmployeeId, self.LastName, self.FirstName, self.BirthDate, self.Photo, self.Note)
        with open(path + file_name, mode='a') as f:
            f.write(line)
            f.close()
        print('The information of Employee {} {} has saved! '.format(
            self.FirstName, self.LastName))


class Orders:

    def __init__(self, customer_id, employee_id, order_date, shipper_id):
        self.OrderID = get_index(file_name_orders) + 1
        self.CustomerId = customer_id
        self.EmployeeID = employee_id
        self.OrderDate = order_date
        self.ShipperID = shipper_id

    def save_information(self, file_name=file_name_orders):
        path = "./database_ex03/"
        line = "\n{},{},{}, {}, {}".format(
            self.OrderID, self.CustomerId, self.EmployeeID, self.OrderDate, self.ShipperID)
        with open(path + file_name, mode='a') as f:
            f.write(line)
            f.close()
        print('The information of Orders {} at {} has saved! '.format(
            self.OrderID, self.OrderDate))


class OrderDetails:
    """
    This class containt information such as:
    OrderDetailID, OrderId, ProductId, Quantity
    """

    def __init__(self, order_id, product_id, quantity):
        self.OrderDetailId = get_index(file_name_orderdetail) + 1
        self.OrderId = order_id
        self.ProductId = product_id
        self.Quantity = quantity

    def save_information(self, file_name=file_name_orderdetail):
        path = "./database_ex03/"
        line = "\n{},{},{}, {}".format(
            self.OrderDetailId, self.OrderId, self.ProductId, self.Quantity)
        with open(path + file_name, mode='a') as f:
            f.write(line)
            f.close()
        print('The information of OrdersID {} has saved! '.format(self.OrderId))


class Shippers:
    """
    This class containt information about shipper_id, shipper_name, Phone
    """

    def __init__(self, shipper_name, phone):
        self.ShipperId = get_index(file_name_shipper) + 1
        self.ShipperName = shipper_name
        self.Phone = phone

    def save_information(self, file_name=file_name_shipper):
        path = "./database_ex03/"
        line = "\n{},{},{}".format(
            self.ShipperId, self.ShipperName, self.Phone)
        with open(path + file_name, mode='a') as f:
            f.write(line)
            f.close()
        print('The information of Shipper {} has saved! '.format(self.ShipperName))


class Suppliers:
    """
    This class contain information about SupplierId, ContactName, Address,
    City, PostalCode, Country, Phone
    """

    def __init__(self, contact_name, address,
                 city, postal_code, country, phone):
        self.SupperlierId = get_index(file_name_supplier) + 1
        self.ContactName = contact_name
        self.Address = address
        self.City = city
        self.PostalCode = postal_code
        self.Country = country
        self.Phone = phone

    def save_information(self, file_name=file_name_supplier):
        path = "./database_ex03/"
        line = "\n{},{},{},{},{},{},{}".format(self.SupperlierId, self.ContactName, self.Address, self.City,
                                               self.PostalCode, self.Country, self.Phone)
        with open(path + file_name, mode='a') as f:
            f.write(line)
            f.close()
        print('The information of Supplier {} has saved! '.format(self.ContactName))


class Products:
    """
    This class contain information about ProductID, SupplierID, CatergoryID, Unit, Price
    """

    def __init__(self, product_name, supplier_id, catergory_id, unit, price):
        self.ProductId = get_index(file_name_product) + 1
        self.ProductName = product_name
        self.SupplierId = supplier_id
        self.CatergoryId = catergory_id
        self.Unit = unit
        self.Price = price

    def save_information(self, file_name=file_name_product):
        path = "./database_ex03/"
        line = "\n{},{},{},{},{},{}".format(self.ProductId, self.ProductName, self.SupplierId,
                                            self.CatergoryId, self.Unit, self.Price)
        with open(path + file_name, mode='a') as f:
            f.write(line)
            f.close()
        print('The information of Product {} has saved! '.format(self.ProductName))


if __name__ == '__main__':
    # nghia = Customers(name='Ha Van Nghia', contact="0322314", address="Doan Ke Thien",
    #                   city="Ha Noi", postal_code=10000, country='VietNam')
    # nghia.save_information()

    # bun_dau_mam_tom = Categories('Thuc an', 'Day la dac san cua viet nam')
    # bun_dau_mam_tom.save_information()

    # Data_Science = Employees('Nghia', 'Ha', '02/12/1234', 'NA', 'VuiVui')
    # Data_Science.save_information()

    # mua_dep = Orders(1, 1, '12/03/2021', 1)
    # mua_dep.save_information()

    # dep_to_ong = OrderDetails(1, 1, 10)
    # dep_to_ong.save_information()

    # now_shipper = Shippers('NghiaHV3', '1233455678')
    # now_shipper.save_information()

    # DKT_store = Suppliers('Vinmart', 'Doan Ke Thien',
    #                       'Hanoi', 10000, 'Vietnam', '01234321')
    # DKT_store.save_information()

    bun = Products()
    bun.save_information()
