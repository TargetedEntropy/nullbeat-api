import sqlalchemy

from db.config import metadata, engine

ItemTable = sqlalchemy.Table(
    "item",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("displayName", sqlalchemy.String),
    sqlalchemy.Column("itemGroups", sqlalchemy.String),
    sqlalchemy.Column("count", sqlalchemy.Integer),
    sqlalchemy.Column("maxCount", sqlalchemy.Integer),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("tags", sqlalchemy.String),
    sqlalchemy.Column("nbt", sqlalchemy.String, nullable=True)
)


metadata.create_all(bind=engine)
