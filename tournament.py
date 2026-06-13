from ex0 import CreatureFactory
from ex2 import BattleStrategy


def fight(
        opponent1: tuple[CreatureFactory, BattleStrategy],
        opponent2: tuple[CreatureFactory, BattleStrategy]
        ) -> None:
    pass


def battle(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]
        ) -> None:
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            fight(opponents[i], opponents[j])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
