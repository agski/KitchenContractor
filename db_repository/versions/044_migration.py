from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
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
    Column('demo_cont', String(length=300)),
    Column('framing_cont', String(length=300)),
    Column('plumb_cont', String(length=300)),
    Column('elec_cont', String(length=300)),
    Column('window_cont', String(length=300)),
    Column('drywall_cont', String(length=300)),
    Column('paint_cont', String(length=300)),
    Column('floor_cont', String(length=300)),
    Column('cab_cont', String(length=300)),
    Column('counter_cont', String(length=300)),
    Column('back_cont', String(length=300)),
    Column('app_cont', String(length=300)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['projects'].columns['app_cont'].create()
    post_meta.tables['projects'].columns['back_cont'].create()
    post_meta.tables['projects'].columns['cab_cont'].create()
    post_meta.tables['projects'].columns['counter_cont'].create()
    post_meta.tables['projects'].columns['demo_cont'].create()
    post_meta.tables['projects'].columns['drywall_cont'].create()
    post_meta.tables['projects'].columns['elec_cont'].create()
    post_meta.tables['projects'].columns['floor_cont'].create()
    post_meta.tables['projects'].columns['framing_cont'].create()
    post_meta.tables['projects'].columns['paint_cont'].create()
    post_meta.tables['projects'].columns['plumb_cont'].create()
    post_meta.tables['projects'].columns['window_cont'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['projects'].columns['app_cont'].drop()
    post_meta.tables['projects'].columns['back_cont'].drop()
    post_meta.tables['projects'].columns['cab_cont'].drop()
    post_meta.tables['projects'].columns['counter_cont'].drop()
    post_meta.tables['projects'].columns['demo_cont'].drop()
    post_meta.tables['projects'].columns['drywall_cont'].drop()
    post_meta.tables['projects'].columns['elec_cont'].drop()
    post_meta.tables['projects'].columns['floor_cont'].drop()
    post_meta.tables['projects'].columns['framing_cont'].drop()
    post_meta.tables['projects'].columns['paint_cont'].drop()
    post_meta.tables['projects'].columns['plumb_cont'].drop()
    post_meta.tables['projects'].columns['window_cont'].drop()
