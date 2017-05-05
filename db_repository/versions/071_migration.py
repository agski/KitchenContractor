from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
projects = Table('projects', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('proj_name', VARCHAR(length=140)),
    Column('demo_stps', VARCHAR(length=300)),
    Column('framing_stps', VARCHAR(length=300)),
    Column('plumb_stps', VARCHAR(length=300)),
    Column('elec_stps', VARCHAR(length=300)),
    Column('window_stps', VARCHAR(length=300)),
    Column('drywall_stps', VARCHAR(length=300)),
    Column('paint_stps', VARCHAR(length=300)),
    Column('floor_stps', VARCHAR(length=300)),
    Column('cab_stps', VARCHAR(length=300)),
    Column('counter_stps', VARCHAR(length=300)),
    Column('back_stps', VARCHAR(length=300)),
    Column('app_stps', VARCHAR(length=300)),
    Column('Demoltion', VARCHAR(length=300)),
    Column('Framing', VARCHAR(length=300)),
    Column('Plumbing', VARCHAR(length=300)),
    Column('Electrical', VARCHAR(length=300)),
    Column('Windows', VARCHAR(length=300)),
    Column('Drywall', VARCHAR(length=300)),
    Column('Painting', VARCHAR(length=300)),
    Column('Flooring', VARCHAR(length=300)),
    Column('Cabinets', VARCHAR(length=300)),
    Column('Countertops', VARCHAR(length=300)),
    Column('Tiles', VARCHAR(length=300)),
    Column('Appliances', VARCHAR(length=300)),
)

projects = Table('projects', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('proj_name', String(length=140)),
    Column('demo_stps', String(length=300)),
    Column('framing_stps', String(length=300)),
    Column('plumb_stps', String(length=300)),
    Column('elec_stps', String(length=300)),
    Column('window_stps', String(length=300)),
    Column('drywall_stps', String(length=300)),
    Column('paint_stps', String(length=300)),
    Column('floor_stps', String(length=300)),
    Column('cab_stps', String(length=300)),
    Column('counter_stps', String(length=300)),
    Column('back_stps', String(length=300)),
    Column('app_stps', String(length=300)),
    Column('Demolition', String(length=300)),
    Column('Framing', String(length=300)),
    Column('Plumbing', String(length=300)),
    Column('Electrical', String(length=300)),
    Column('Windows', String(length=300)),
    Column('Drywall', String(length=300)),
    Column('Painting', String(length=300)),
    Column('Flooring', String(length=300)),
    Column('Cabinets', String(length=300)),
    Column('Countertops', String(length=300)),
    Column('Tiles', String(length=300)),
    Column('Appliances', String(length=300)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['projects'].columns['Demoltion'].drop()
    post_meta.tables['projects'].columns['Demolition'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['projects'].columns['Demoltion'].create()
    post_meta.tables['projects'].columns['Demolition'].drop()
