### To access the Pokemon data

import pandas as pd

from app.models.pokemon import Pokemon
from app.factories.pokemon_factory import PokemonFactory


class PokemonRepository:
    def __init__(self, csv_path: str):
        self.df = pd.read_csv(csv_path)
        
    def get_pokemon(self, name: str) -> Pokemon:
        normalized_name = name.lower()
        matches = self.df[self.df['name'].str.lower() == normalized_name]
        if matches.empty:
            raise ValueError(f"Pokémon {name} not found.")
        return PokemonFactory.create_pokemon(matches.iloc[0])
