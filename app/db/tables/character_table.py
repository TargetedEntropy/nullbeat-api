import sqlalchemy

from db.config import metadata, engine

CharacterTable = sqlalchemy.Table(
    "character",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("character_name", sqlalchemy.String),
    sqlalchemy.Column("character_pass", sqlalchemy.String),
    sqlalchemy.Column("account_type", sqlalchemy.Boolean),
)


metadata.create_all(bind=engine)
