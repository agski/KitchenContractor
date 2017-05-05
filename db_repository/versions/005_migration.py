from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
project = Table('project', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('timestamp', DATETIME),
    Column('descrip', VARCHAR(length=140)),
    Column('des_stps', VARCHAR(length=120)),
    Column('demo_stps', VARCHAR(length=120)),
    Column('framing_stps', VARCHAR(length=120)),
    Column('plumb_stps', VARCHAR(length=120)),
    Column('elec_stps', VARCHAR(length=120)),
    Column('drywall_stps', VARCHAR(length=120)),
    Column('paint_stps', VARCHAR(length=120)),
    Column('floor_stps', VARCHAR(length=120)),
    Column('cab_stps', VARCHAR(length=120)),
    Column('back_stps', VARCHAR(length=120)),
    Column('app_stps', VARCHAR(length=120)),
    Column('owner_id', INTEGER),
    Column('design_id', INTEGER),
    Column('demo_id', INTEGER),
    Column('framing_id', INTEGER),
    Column('plumb_id', INTEGER),
    Column('elec_id', INTEGER),
    Column('drywall_id', INTEGER),
    Column('paint_id', INTEGER),
    Column('floor_id', INTEGER),
    Column('cab_id', INTEGER),
    Column('back_id', INTEGER),
    Column('app_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
    Column('user_type', VARCHAR(length=120)),
)

projects = Table('projects', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('descrip', String(length=140)),
    Column('des_stps', String(length=120)),
    Column('demo_stps', String(length=120)),
    Column('framing_stps', String(length=120)),
    Column('plumb_stps', String(length=120)),
    Column('elec_stps', String(length=120)),
    Column('drywall_stps', String(length=120)),
    Column('paint_stps', String(length=120)),
    Column('floor_stps', String(length=120)),
    Column('cab_stps', String(length=120)),
    Column('back_stps', String(length=120)),
    Column('app_stps', String(length=120)),
    Column('owner_id', Integer),
    Column('design_id', Integer),
    Column('demo_id', Integer),
    Column('framing_id', Integer),
    Column('plumb_id', Integer),
    Column('elec_id', Integer),
    Column('drywall_id', Integer),
    Column('paint_id', Integer),
    Column('floor_id', Integer),
    Column('cab_id', Integer),
    Column('back_id', Integer),
    Column('app_id', Integer),
)

users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('user_type', String(length=120)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['project'].drop()
    pre_meta.tables['user'].drop()
    post_meta.tables['projects'].create()
    post_meta.tables['users'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['project'].create()
    pre_meta.tables['user'].create()
    post_meta.tables['projects'].drop()
    post_meta.tables['users'].drop()
