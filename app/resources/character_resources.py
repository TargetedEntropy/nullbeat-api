from fastapi import Depends
from dependencies import get_character_dal


class CharacterClass:
    """A class to interact with the characters

    This is where we use the Character DAL to respond to the
    routers. Creating, getting characters and thier paramters
    is done from this class.

    Attributes
    ----------
    CharacterDAL : the character data access layer

    """

    def __init__(self, CharacterDAL=Depends(get_character_dal)):
        """
        Parameters
        ----------
        CharacterDAL : class

        The character data access layer
        """
        self.CharacterDAL = CharacterDAL

    async def get_character(self):
        """Get a character

        Return any and all infomration we have
        about a character.

        """
        return await self.CharacterDAL.get_character()

    async def set_character(self, data: str):
        """Create a Character"""
        return await self.CharacterDAL.set_character(data)
