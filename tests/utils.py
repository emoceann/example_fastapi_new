import random


def generate_data(start: int, stop: int) -> list[dict]:
    return [dict(id=i, name=random.choice("abcdefg")) for i in range(start, stop)]