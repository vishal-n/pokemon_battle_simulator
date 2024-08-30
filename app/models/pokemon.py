

class Pokemon:
    def __init__(self, name: str, type1: str, type2: str, attack: int, against_types: dict):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.attack = attack
        self.against_types = against_types

    def get_against_value(self, attack_type: str) -> float:
        return self.against_types.get(f'against_{attack_type}', 1.0)
