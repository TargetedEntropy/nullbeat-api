""" CharacterDAL

    Character DataLayer, access to the database directly from routed functions.
"""
import json
from db.config import db_session
from db.schema.character_schema import CharacterSchema
from db.tables.character_table import CharacterTable


class CharacterDAL:
    """A class to interact with the character model in the DB

    Attributes
    ----------
    database : the database object

    """

    def __init__(self, db_session: db_session):
        """
        Parameters
        ----------
        database : class
            The database object
        """
        self.db_session = db_session

    async def get_character(self):
        """Get info for a character

        This is where we finally ask the database
        itself about our character..

        Returns:
            str: json about our character
        """

        query = self.db_session.query(CharacterSchema)
        # for attr, value in data.characters():
        # query = query.filter(CharacterSchema.character_completed == False)

        results = query.all()
        return results

    async def set_character(self, data: str):
        """Create a character

        Args:
            character_data (str): Information we have about an character

        Returns:
            str: Repeat the information we were provided
        """
        print(f"Inserting Values: {data}")
        character = CharacterSchema(
            character_name=data.character_name,
            character_pass=data.character_pass,
            account_type=data.account_type,
        )
        print(f"data: {character}")

        print(self.db_session.add(character))
        print(self.db_session.commit())

        return "Success"
