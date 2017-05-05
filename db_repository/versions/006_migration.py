from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
projects = Table('projects', pre_meta,
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['projects'].columns['app_id'].drop()
    pre_meta.tables['projects'].columns['back_id'].drop()
    pre_meta.tables['projects'].columns['cab_id'].drop()
    pre_meta.tables['projects'].columns['demo_id'].drop()
    pre_meta.tables['projects'].columns['design_id'].drop()
    pre_meta.tables['projects'].columns['drywall_id'].drop()
    pre_meta.tables['projects'].columns['elec_id'].drop()
    pre_meta.tables['projects'].columns['floor_id'].drop()
    pre_meta.tables['projects'].columns['framing_id'].drop()
    pre_meta.tables['projects'].columns['paint_id'].drop()
    pre_meta.tables['projects'].columns['plumb_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['projects'].columns['app_id'].create()
    pre_meta.tables['projects'].columns['back_id'].create()
    pre_meta.tables['projects'].columns['cab_id'].create()
    pre_meta.tables['projects'].columns['demo_id'].create()
    pre_meta.tables['projects'].columns['design_id'].create()
    pre_meta.tables['projects'].columns['drywall_id'].create()
    pre_meta.tables['projects'].columns['elec_id'].create()
    pre_meta.tables['projects'].columns['floor_id'].create()
    pre_meta.tables['projects'].columns['framing_id'].create()
    pre_meta.tables['projects'].columns['paint_id'].create()
    pre_meta.tables['projects'].columns['plumb_id'].create()
