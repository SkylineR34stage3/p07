from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle_base(fire: CreatureFactory, aqua: CreatureFactory) -> None:
    print("\nTesting battle")

    f_base = fire.create_base()
    a_base = aqua.create_base()

    print(f_base.describe(), " vs.", a_base.describe(), sep="\n")
    print(" fight!", f_base.attack(), a_base.attack(), sep="\n")


def main() -> None:
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    test_factory(flame_fac)
    print()
    test_factory(aqua_fac)

    battle_base(flame_fac, aqua_fac)


if __name__ == "__main__":
    main()
