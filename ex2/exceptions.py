class InvalidStrategyError(Exception):
    def __init__(self, name: str, strategy: str):
        super().__init__(
            f"Invalid Creature '{name}' for this {strategy} strategy")
