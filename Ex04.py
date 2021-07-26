
file_name_salepersons = "SalePersons.csv"


class SalePerson:

    def __init__(self, sale_person_name, branch):
        self.SalePersonId = 'None'
        self.SalePersonName = sale_person_name
        self.Branch = branch

    def create_invoice(self):
        pass


class Invoice:

    def __init__(self, customer_id, car_serial_number,
                 sale_person_id, invoice_date):

        self.InvoiceID = 'None'
        self.CustomerID = customer_id
        self.CarSerialNumber = car_serial_number
        self.SalePersonID = sale_person_id
        self.InvoiceDate = invoice_date


class Customer:

    def __init__(self, customer_name, address, phone):
        self.CustomerID = None
        self.CustomerName = customer_name
        self.Address = address
        self.Phone = phone


if __n