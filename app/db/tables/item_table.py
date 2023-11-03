import sqlalchemy

from db.config import metadata, engine

ItemTable = sqlalchemy.Table(
    "item",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("item_name", sqlalchemy.String),
    sqlalchemy.Column("item_contents", sqlalchemy.String),
    sqlalchemy.Column("character_name", sqlalchemy.String),
)


metadata.create_all(bind=engine)
