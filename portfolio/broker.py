from dataclasses import dataclass, field
from .utils import to_dict

@dataclass
class Broker:
    """Class for keeping track of your broker."""
    name: str
    account: str
    account_type: str
    currency: str
    id: str = field(default='')

    def __post_init__(self):
        self.id = '_'.join([self.name, self.account])

    def to_dict(self) -> dict:
        return to_dict(self)
