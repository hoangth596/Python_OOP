from peewee import *


db = SqliteDatabase('CarDealship.db')


class BaseModel(Model):
    class Meta:
        database = db


class SalePersons(BaseModel):
    sale_id = AutoField(primary_key=True)
    lname = CharField()
    fname = CharField()

    class Meta:
        table_name = 'SalePersons'


class Parts(BaseModel):
    part_id = AutoField(primary_key=True)
    part_name = CharField()
    des = CharField()
    purchase_price = FloatField()
    retail_price = FloatField()

    class Meta:
        table_name = 'Parts'


class Cars(BaseModel):
    car_id = AutoField(primary_key=True)
    car_series_number = CharField()
    model = CharField()
    color = CharField()
    year = CharField()
    avaliable = CharField()

    class Meta:
        table_name = 'Cars'

class Customers(BaseModel):
    cus_id = AutoField(primary_key=True)
    lname = CharField()
    nname = CharField()
    phone = CharField()
    address = CharField()
    lname = CharField()
    city = CharField()
    province = CharField()
    postcode = IntegerField()
    country = CharField()

    class Meta:
        table_name = 'Customers'


class SalesInvoices(BaseModel):
    invoiceID = AutoField(primary_key=True)
    invoice_name = CharField()
    date = DateField()
    car_id = ForeignKeyField(Cars, column_name='car_id')
    cus_id = ForeignKeyField(Customers, column_name='cus_id')
    saleperson_id = ForeignKeyField(SalePersons, column_name='sale_id')

    class Meta:
        table_name = 'SalesInvoices'

class ServiceTickets(BaseModel):
    service_ticket_id = AutoField(primary_key=True)
    car_serial_number = ForeignKeyField(Cars, column_name='car_series_number')
    customer_id = ForeignKeyField(Customers, column_name='cus_id')
    date_recieved = DateField()
    comments = CharField()
    date_return = DateField()

    class Meta:
        table_name = "ServiceTickets"

class Services(BaseModel):

    service_id = AutoField(primary_key=True)
    service_name = CharField()
    hourly_rate = FloatField()

    class Meta:
        table_name = "Services"

class Mechanics(BaseModel):

    mechanic_id = AutoField(primary_key=True)
    last_name = CharField()
    first_name = CharField()

    class Meta:
        table_name = "Mechanics"

class ServiceMechanics(BaseModel):

    service_mechanic_id = AutoField(primary_key=True)
    service_ticket_id = ForeignKeyField(ServiceTickets, column_name='service_ticket_id')
    service_id = ForeignKeyField(Services, column_name='service_id')
    mechanic_id = ForeignKeyField(Mechanics, column_name='mechanic_id')
    hour = IntegerField()
    comment = CharField()
    rate = IntegerField()

    class Meta:
        table_name = "ServiceMechanics"

class PartsUsed(BaseModel):
    part_used_id = AutoField(primary_key=True)
    service_mechanic_id = ForeignKeyField(ServiceMechanics, column_name='service_mechanic_id')
    part_id = ForeignKeyField(Parts, column_name='part_id')
    number_used = IntegerField()
    price = FloatField()

    class Meta:
        table_name = 'PartsUsed'




try:
    db.create_tables([SalePersons, Parts, SalesInvoices, Cars ,PartsUsed,Customers,ServiceTickets,ServiceMechanics,Services,Mechanics])
except pw.OperationalError:
    print('Some table already exists')

nghia_sale = SalePersons(lname="Nghia", fname="ha")
nghia_sale.save()
