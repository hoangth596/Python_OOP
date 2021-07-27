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


if __name__ == "__main__":
    try:
        db.create_tables([RetailCenters, ShippedItems, TransportationEvents, ItemTransportations])
    except OperationalError:
        print('Some table already exists')
    

    center_list = [
        {'center_type' : 'Good', 'address' : 'My Dinh District, Hanoi'},
        {'center_type' : 'Drink & Beverages', 'address' : 'Thanh Xuan District, Hanoi'},
        {'center_type' : 'Good', 'address' : 'District 1, HCM City'},
        {'center_type' : 'Good', 'address' : 'Binh Thanh District, HCM City'}
    ]

    RetailCenters.insert_many(center_list).execute()


    item_list = [
        {'item_number' : 210701, 'retail_center_id' : 1, 'weight' : 1.5, 'dimensions' : '20 x 30', 'insurance_amount' : 200,
            'destination' : 'FPT Tower, Pham Van Bach Str., Cau Giay Dist., Hanoi', 'final_delivery_date' : '20/7/2021'},
        {'item_number' : 210702, 'retail_center_id' : 1, 'weight' : 3.5, 'dimensions' : '40 x 30', 'insurance_amount' : 500,
            'destination' : 'FPT Tower, Pham Van Bach Str., Cau Giay Dist., Hanoi', 'final_delivery_date' : '20/7/2021'},
        {'item_number' : 210703, 'retail_center_id' : 2, 'weight' : 0.5, 'dimensions' : '10 x 20', 'insurance_amount' : 200,
            'destination' : 'FPT Building, Duy Tan Str., Cau Giay Dist., Hanoi', 'final_delivery_date' : '21/7/2021'},
        {'item_number' : 210704, 'retail_center_id' : 2, 'weight' : 4.2, 'dimensions' : '30 x 50', 'insurance_amount' : 500,
            'destination' : 'FPT Building, Duy Tan Str., Cau Giay Dist., Hanoi', 'final_delivery_date' : '21/7/2021'},
        {'item_number' : 210705, 'retail_center_id' : 1, 'weight' : 50, 'dimensions' : '200 x 150', 'insurance_amount' : 5000,
            'destination' : 'Military Hospital 175, Go Vap District, HCM city', 'final_delivery_date' : '25/7/2021'},
        {'item_number' : 210706, 'retail_center_id' : 2, 'weight' : 20, 'dimensions' : '80 x 100', 'insurance_amount' : 2000,
            'destination' : 'Military Hospital 175, Go Vap District, HCM city', 'final_delivery_date' : '25/7/2021'},
        {'item_number' : 210707, 'retail_center_id' : 3, 'weight' : 5.5, 'dimensions' : '50 x 40', 'insurance_amount' : 700,
            'destination' : 'Crescent Mall, Tan Phu District, HCM city', 'final_delivery_date' : '22/7/2021'},
        {'item_number' : 210708, 'retail_center_id' : 4, 'weight' : 10, 'dimensions' : '80 x 50', 'insurance_amount' : 1000,
            'destination' : 'Landmark 81, Tan Phu District, HCM city', 'final_delivery_date' : '23/7/2021'},
    ]
    
    ShippedItems.insert_many(item_list).execute()


    transport_event_list = [
        {'schedule_number' : 2107001, 'transport_type' : 'Trucks',
            'delivery_route' : 'My Dinh Str. - Nguyen Hoang Str. - Ton That Thuyet Str. - Pham Van Bach Str.'},
        {'schedule_number' : 2107002, 'transport_type' : 'Trucks',
            'delivery_route' : 'Nguyen Trai Str. - Khuat Duy Tien Str. - Pham Hung Str. - Duy Tan Str.'},
        {'schedule_number' : 2107003, 'transport_type' : 'Flight',
            'delivery_route' : 'Noi Bai International Airport - Tan Son Nhat International Airport'},
        {'schedule_number' : 2107004, 'transport_type' : 'Trucks',
            'delivery_route' : 'Ham Nghi Str. - Khanh Hoi Bridge - Nguyen Tat Thanh Str. - Tan Thuan 2 Bridge - Nguyen Van Linh Str. - Nguyen Luong Bang Str. - Hoang Van Thai Str.'},
        {'schedule_number' : 2107005, 'transport_type' : 'Trucks',
            'delivery_route' : 'Dinh Bo Linh Str. - Bach Dang Str. - Xo Viet Nghe Tinh Str. - Dien Bien Phu Str. - Tran Trong Kim Str.'}
    ]
    
    TransportationEvents.insert_many(transport_event_list).execute()


    item_transport_list = [
        {'item_number' : 210701, 'schedule_number' : 2107001},
        {'item_number' : 210702, 'schedule_number' : 2107001},
        {'item_number' : 210703, 'schedule_number' : 2107002},
        {'item_number' : 210704, 'schedule_number' : 2107002},
        {'item_number' : 210705, 'schedule_number' : 2107003},
        {'item_number' : 210706, 'schedule_number' : 2107003},
        {'item_number' : 210707, 'schedule_number' : 2107004},
        {'item_number' : 210708, 'schedule_number' : 2107005}
    ]

    ItemTransportations.insert_many(item_transport_list).execute()
