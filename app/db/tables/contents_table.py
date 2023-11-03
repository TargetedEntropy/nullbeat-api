import sqlalchemy

from db.config import metadata, engine

ContentsTable = sqlalchemy.Table(
    "contents",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("item_slot", sqlalchemy.Integer),
    sqlalchemy.Column("item_count", sqlalchemy.Integer),
    sqlalchemy.Column("item_id", sqlalchemy.String),
)


metadata.create_all(bind=engine)
