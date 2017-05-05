from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
users = Table('users', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('user_type', VARCHAR(length=120)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

appers = Table('appers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

backers = Table('backers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

cabers = Table('cabers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

demoers = Table('demoers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

designers = Table('designers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

drywallers = Table('drywallers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

electricians = Table('electricians', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

floorers = Table('floorers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

framers = Table('framers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

owners = Table('owners', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('user_type', String(length=120)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

painters = Table('painters', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
)

plumbers = Table('plumbers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=120)),
    Column('pw', String(length=120)),
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].drop()
    post_meta.tables['appers'].create()
    post_meta.tables['backers'].create()
    post_meta.tables['cabers'].create()
    post_meta.tables['demoers'].create()
    post_meta.tables['designers'].create()
    post_meta.tables['drywallers'].create()
    post_meta.tables['electricians'].create()
    post_meta.tables['floorers'].create()
    post_meta.tables['framers'].create()
    post_meta.tables['owners'].create()
    post_meta.tables['painters'].create()
    post_meta.tables['plumbers'].create()
    post_meta.tables['projects'].columns['app_id'].create()
    post_meta.tables['projects'].columns['back_id'].create()
    post_meta.tables['projects'].columns['cab_id'].create()
    post_meta.tables['projects'].columns['demo_id'].create()
    post_meta.tables['projects'].columns['design_id'].create()
    post_meta.tables['projects'].columns['drywall_id'].create()
    post_meta.tables['projects'].columns['elec_id'].create()
    post_meta.tables['projects'].columns['floor_id'].create()
    post_meta.tables['projects'].columns['framing_id'].create()
    post_meta.tables['projects'].columns['paint_id'].create()
    post_meta.tables['projects'].columns['plumb_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].create()
    post_meta.tables['appers'].drop()
    post_meta.tables['backers'].drop()
    post_meta.tables['cabers'].drop()
    post_meta.tables['demoers'].drop()
    post_meta.tables['designers'].drop()
    post_meta.tables['drywallers'].drop()
    post_meta.tables['electricians'].drop()
    post_meta.tables['floorers'].drop()
    post_meta.tables['framers'].drop()
    post_meta.tables['owners'].drop()
    post_meta.tables['painters'].drop()
    post_meta.tables['plumbers'].drop()
    post_meta.tables['projects'].columns['app_id'].drop()
    post_meta.tables['projects'].columns['back_id'].drop()
    post_meta.tables['projects'].columns['cab_id'].drop()
    post_meta.tables['projects'].columns['demo_id'].drop()
    post_meta.tables['projects'].columns['design_id'].drop()
    post_meta.tables['projects'].columns['drywall_id'].drop()
    post_meta.tables['projects'].columns['elec_id'].drop()
    post_meta.tables['projects'].columns['floor_id'].drop()
    post_meta.tables['projects'].columns['framing_id'].drop()
    post_meta.tables['projects'].columns['paint_id'].drop()
    post_meta.tables['projects'].columns['plumb_id'].drop()
