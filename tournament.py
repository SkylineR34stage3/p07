from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, DefensiveStrategy
from ex2 import AggressiveStrategy, InvalidStrategyError


def fight(
        opponent1: tuple[CreatureFactory, BattleStrategy],
        opponent2: tuple[CreatureFactory, BattleStrategy]
        ) -> None:
    factory1, strategy1 = opponent1
    factory2, strategy2 = opponent2
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print("\n* Battle *")
    print(creature1.describe(), " vs.",
          creature2.describe(), sep="\n")
    print(" now fight!")
    strategy1.act(creature1)
    strategy2.act(creature2)


def battle(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]
        ) -> None:
    print("*** Tournament ***")
    opponents_num = len(opponents)
    print(f"{opponents_num} opponents involved")
    for i in range(opponents_num):
        for j in range(i + 1, opponents_num):
            fight(opponents[i], opponents[j])


def err_catcher(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]
        ) -> None:
    try:
        battle(opponents)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    print("Tournament 0 (basic)")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ]
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    err_catcher(opponents)

    print("\nTournament 1 (error)")
    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ]
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    err_catcher(opponents)

    print("\nTournament 2 (multiple)")
    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
        ]
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    err_catcher(opponents)


if __name__ == "__main__":
    main()
