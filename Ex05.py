from peewee import *

db = SqliteDatabase('UPS.db')


class BaseModel(Model):
    class Meta:
        database = db


class RetailCenters(BaseModel):
    retail_center_id = AutoField(primary_key=True)
    center_type = CharField()
    address = CharField()

    class Meta:
        table_name = 'RetailCenters'


class ShippedItems(BaseModel):
    item_number = IntegerField(primary_key=True)
    retail_center_id = ForeignKeyField(RetailCenters, column_name='retail_center_id')
    weight = FloatField()
    dimensions = CharField()
    insurance_amount = IntegerField()
    destination = CharField()
    final_delivery_date = DateField()

    class Meta:
        table_name = 'ShippedItems'


class TransportationEvents(BaseModel):
    schedule_number = IntegerField(primary_key=True)
    transport_type = CharField()
    delivery_route = CharField()

    class Meta:
        table_name = 'TransportationEvents'


class ItemTransportations(BaseModel):
    item_transportation_id = AutoField(primary_key=True)
    item_number = ForeignKeyField(ShippedItems, column_name='item_number')
    schedule_number = ForeignKeyField(TransportationEvents, column_name='schedule_number')

    class Meta:
        table_name = 'ItemTransportations'