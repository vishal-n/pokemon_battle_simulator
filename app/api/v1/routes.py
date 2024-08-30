from fastapi import APIRouter, HTTPException
from app.schemas.battle_request import BattleRequest
from app.services.battle_service import BattleService
from app.repositories.pokemon_repository import PokemonRepository

router = APIRouter()

pokemon_repository = PokemonRepository('data/pokemon.csv')
battle_service = BattleService(pokemon_repository)

@router.get('/pokemon')
def list_pokemon(page: int = 1, per_page: int = 10):
    start = (page - 1) * per_page
    end = start + per_page
    pokemon_list = pokemon_repository.df.iloc[start:end].to_dict(orient='records')
    return pokemon_list


@router.post('/battle')
def initiate_battle(request: BattleRequest):
    try:
        battle_id = battle_service.start_battle(request.pokemonA, request.pokemonB)
        return {"battle_id": battle_id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get('/battle/{battle_id}')
def get_battle_status(battle_id: str):
    try:
        status = battle_service.get_battle_status(battle_id)
        return status
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
