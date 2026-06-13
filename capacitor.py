from ex1 import HealingCreatureFactory, TransformCreatureFactory


def heal_factory_test(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    sproutling = factory.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print(" evolved:")
    bloomelle = factory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())


def trans_factory_test(factory: TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")

    print(" base:")
    shiftling = factory.create_base()
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    print(" evolved:")
    morphagon = factory.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())


def main() -> None:
    heal_factory_test(HealingCreatureFactory())
    trans_factory_test(TransformCreatureFactory())


if __name__ == "__main__":
    main()
