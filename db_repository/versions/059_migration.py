from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
reqs1 = Table('reqs1', pre_meta,
    Column('issuer_id', INTEGER),
    Column('pending_id', INTEGER),
)

reqs2 = Table('reqs2', pre_meta,
    Column('issuee_id', INTEGER),
    Column('pending_id', INTEGER),
)

pending = Table('pending', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('req_type', VARCHAR(length=300)),
    Column('issuee_id', INTEGER),
    Column('issuer_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reqs1'].drop()
    pre_meta.tables['reqs2'].drop()
    pre_meta.tables['pending'].columns['issuee_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reqs1'].create()
    pre_meta.tables['reqs2'].create()
    pre_meta.tables['pending'].columns['issuee_id'].create()
