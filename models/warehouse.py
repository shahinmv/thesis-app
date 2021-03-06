from db import db
from sqlalchemy.ext.associationproxy import association_proxy


class Warehouse(db.Model):
    __tablename__ = 'PilotApp_warehouse_test'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50))
    volume_available = db.Column(db.Integer)
    volume_total = db.Column(db.Integer)
    labelling = db.Column(db.Boolean)
    manual_geo_data_entry = db.Column(db.Boolean)
    item_packaging = db.Column(db.Boolean)
    palette_packaging = db.Column(db.Boolean)
    address = db.Column(db.String(200))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    warehouse_services = db.relationship('WarehouseServices', lazy='dynamic')


    def __init__(self, name, volume_available, volume_total, labelling, manual_geo_data_entry, item_packaging, palette_packaging, address, email, phone, owner_id):
        self.name = name
        self.volume_available = volume_available
        self.volume_total = volume_total
        self.labelling = labelling
        self.manual_geo_data_entry = manual_geo_data_entry
        self.item_packaging = item_packaging
        self.palette_packaging = palette_packaging
        self.address = address
        self.email = email
        self.phone = phone
        self.owner = owner_id
    
    labelling_price = association_proxy('warehouse_services', 'goods_receiving_labelling')
    manualgeo_price = association_proxy('warehouse_services', 'goods_receiving_manuel_geo_data')
    itempackaging_price = association_proxy('warehouse_services', 'item_packaging')
    palettepackaging_price = association_proxy('warehouse_services', 'palette_packaging')
    storage = association_proxy('warehouse_services', 'storage')
    goods_receiving_processing = association_proxy('warehouse_services', 'goods_receiving_processing')
    item_picking = association_proxy('warehouse_services', 'item_picking')
    packaging_material = association_proxy('warehouse_services', 'packaging_material')