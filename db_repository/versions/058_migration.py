from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
reqs = Table('reqs', pre_meta,
    Column('issuer_id', INTEGER),
    Column('projects_id', INTEGER),
    Column('issuee_id', INTEGER),
)

reqs1 = Table('reqs1', post_meta,
    Column('issuer_id', Integer),
    Column('pending_id', Integer),
)

reqs2 = Table('reqs2', post_meta,
    Column('issuee_id', Integer),
    Column('pending_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reqs'].drop()
    post_meta.tables['reqs1'].create()
    post_meta.tables['reqs2'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reqs'].create()
    post_meta.tables['reqs1'].drop()
    post_meta.tables['reqs2'].drop()
