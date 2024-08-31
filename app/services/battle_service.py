### Services for a given battle

from uuid import uuid4
from threading import Thread

from app.models.pokemon import Pokemon
from app.models.battle import Battle
from app.repositories.pokemon_repository import PokemonRepository


class BattleService:
    def __init__(self, repository: PokemonRepository):
        self.repository = repository
        self.battles = {}

    def start_battle(self, pokemon_a_name: str, pokemon_b_name: str) -> str:
        battle_id = str(uuid4())
        self.battles[battle_id] = {"status": "BATTLE_INPROGRESS", "result": None}

        thread = Thread(target=self._execute_battle, args=(battle_id, pokemon_a_name, pokemon_b_name))
        thread.start()
        return battle_id

    def _execute_battle(self, battle_id: str, pokemon_a_name: str, pokemon_b_name: str):
        try:
            pokemon_a = self.repository.get_pokemon(pokemon_a_name)
            pokemon_b = self.repository.get_pokemon(pokemon_b_name)
            battle = Battle(pokemon_a, pokemon_b)
            result = battle.execute()
            self.battles[battle_id] = {"status": "BATTLE_COMPLETED", "result": result}
        except Exception:
            self.battles[battle_id] = {"status": "BATTLE_FAILED", "result": None}

    def get_battle_status(self, battle_id: str) -> dict:
        if battle_id not in self.battles:
            raise ValueError(f"Battle ID {battle_id} not found.")
        return self.battles[battle_id]
