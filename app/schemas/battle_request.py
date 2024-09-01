### Pydantic model for request / response validation

from pydantic import BaseModel


class BattleRequest(BaseModel):
    pokemonA: str
    pokemonB: str
