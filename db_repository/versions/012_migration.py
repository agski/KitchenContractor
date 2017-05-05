from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
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
