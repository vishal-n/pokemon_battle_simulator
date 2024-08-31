### File containing all the services used by the APIs

import json
import pandas as pd
from fastapi import APIRouter, HTTPException
from app.schemas.battle_request import BattleRequest
from app.services.battle_service import BattleService
from app.repositories.pokemon_repository import PokemonRepository

router = APIRouter()

pokemon_repository = PokemonRepository('data/pokemon.csv')
battle_service = BattleService(pokemon_repository)


### To return a paginated response for all the pokemon characters
@router.get('/pokemon')
def list_pokemon(page: int = 1, per_page: int = 10):
    start = (page - 1) * per_page
    end = start + per_page
    df = pd.read_csv("data/pokemon.csv")
    df = df[start:end]
    final_rows = df.to_records(index=False).tolist()    
    rows_json = json.dumps(final_rows, indent=1)
    response = {"response": rows_json}
    return response 


### To initiate a battle between two pokemon characters
@router.post('/battle')
def initiate_battle(request: BattleRequest):
    try:
        battle_id = battle_service.start_battle(request.pokemonA, request.pokemonB)
        return {"battle_id": battle_id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


### To fetch the status of a given battle
@router.get('/battle/{battle_id}')
def get_battle_status(battle_id: str):
    try:
        status = battle_service.get_battle_status(battle_id)
        return status
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
