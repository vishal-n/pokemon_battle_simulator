from app.models.pokemon import Pokemon
import pandas as pd


class PokemonFactory:
    @staticmethod
    def create_pokemon(data: pd.Series) -> Pokemon:
        against_types = {col: data[col] for col in data.index if col.startswith('against_')}
        return Pokemon(
            name=data['name'],
            type1=data['type1'],
            type2=data['type2'],
            attack=data['attack'],
            against_types=against_types
        )
