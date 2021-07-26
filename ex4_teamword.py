# !pip install peewee
from peewee import *

db = pw.SqliteDatabase('CarDealship.db')

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

class SalesInvoices(BaseModel):
    invoiceID = AutoField(primary_key=True)
    invoice_name = CharField()
    date = DateField()
    car_id =  ForeignKeyField(Cars, column_name='car_id')
    cus_id =  ForeignKeyField(Customers, column_name='cus_id')
    saleperson_id = ForeignKeyField(SalePersons, column_name='sale_id')

    class Meta:
        table_name = 'SalesInvoices'

class Cars(BaseModel):
    car_id = AutoField(primary_key=True)
    car_series_number = CharField()
    model = CharField()
    color = CharField()
    year = CharField()
    avaliable = CharField()

    class Meta:
        table_name = 'Cars'

class PartsUsed(BaseModel):
    part_used_id =  AutoField(primary_key=True)
    service_mechanic_id = ForeignKeyField(ServiceMechanic, column_name='service_mechanic_id')
    part_id = ForeignKeyField(Parts, column_name='part_id')
    number_used = IntegerField()
    price = FloatField()

    class Meta:
        table_name = 'PartsUsed'

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