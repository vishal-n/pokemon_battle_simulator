from typing import List, Optional
import pandas as pd
from uuid import uuid4
from threading import Thread
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.models.pokemon import Pokemon


class BattleStrategy:
    def calculate_damage(self, attacker: Pokemon, defender: Pokemon) -> float:
        against_type1 = defender.get_against_value(attacker.type1)
        against_type2 = defender.get_against_value(attacker.type2)
        return (attacker.attack / 200) * 100 - (((against_type1 / 4) * 100) + ((against_type2 / 4) * 100))


class Battle:
    def __init__(self, pokemon_a: Pokemon, pokemon_b: Pokemon):
        self.pokemon_a = pokemon_a
        self.pokemon_b = pokemon_b
        self.strategy = BattleStrategy()

    def execute(self) -> dict:
        damage_to_b = self.strategy.calculate_damage(self.pokemon_a, self.pokemon_b)
        damage_to_a = self.strategy.calculate_damage(self.pokemon_b, self.pokemon_a)

        if damage_to_b > damage_to_a:
            return {"winnerName": self.pokemon_a.name, "wonByMargin": damage_to_b - damage_to_a}
        elif damage_to_a > damage_to_b:
            return {"winnerName": self.pokemon_b.name, "wonByMargin": damage_to_a - damage_to_b}
        else:
            return {"winnerName": "Draw", "wonByMargin": 0}
