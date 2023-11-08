import sqlalchemy

from db.config import metadata, engine

JobTable = sqlalchemy.Table(
    "job",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    
    sqlalchemy.Column("job_type", sqlalchemy.String),
    sqlalchemy.Column("character_name", sqlalchemy.String),
    sqlalchemy.Column("job_completed", sqlalchemy.Boolean),
    sqlalchemy.Column("nbt_data", sqlalchemy.String)
)


metadata.create_all(bind=engine)
