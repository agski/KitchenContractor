from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
appers = Table('appers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

backers = Table('backers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

cabers = Table('cabers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

demoers = Table('demoers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

designers = Table('designers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

drywallers = Table('drywallers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

electricians = Table('electricians', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

floorers = Table('floorers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

framers = Table('framers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

owners = Table('owners', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('user_type', VARCHAR(length=120)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

painters = Table('painters', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
)

plumbers = Table('plumbers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('pw', VARCHAR(length=120)),
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
    pre_meta.tables['appers'].drop()
    pre_meta.tables['backers'].drop()
    pre_meta.tables['cabers'].drop()
    pre_meta.tables['demoers'].drop()
    pre_meta.tables['designers'].drop()
    pre_meta.tables['drywallers'].drop()
    pre_meta.tables['electricians'].drop()
    pre_meta.tables['floorers'].drop()
    pre_meta.tables['framers'].drop()
    pre_meta.tables['owners'].drop()
    pre_meta.tables['painters'].drop()
    pre_meta.tables['plumbers'].drop()
    post_meta.tables['users'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['appers'].create()
    pre_meta.tables['backers'].create()
    pre_meta.tables['cabers'].create()
    pre_meta.tables['demoers'].create()
    pre_meta.tables['designers'].create()
    pre_meta.tables['drywallers'].create()
    pre_meta.tables['electricians'].create()
    pre_meta.tables['floorers'].create()
    pre_meta.tables['framers'].create()
    pre_meta.tables['owners'].create()
    pre_meta.tables['painters'].create()
    pre_meta.tables['plumbers'].create()
    post_meta.tables['users'].drop()
