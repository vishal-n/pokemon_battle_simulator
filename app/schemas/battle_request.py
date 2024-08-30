from pydantic import BaseModel


class BattleRequest(BaseModel):
    pokemonA: str
    pokemonB: str
