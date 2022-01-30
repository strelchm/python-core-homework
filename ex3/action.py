class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name if isinstance(other, BaseAction) else False

    def __hash__(self):
        return hash(self.name)


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')

    def __lt__(self, other):
        return isinstance(other, PaperAction)


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')

    def __lt__(self, other):
        return isinstance(other, ScissorsAction)


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')

    def __lt__(self, other):
        return isinstance(other, RockAction)
