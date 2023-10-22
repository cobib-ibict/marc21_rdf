from dataclasses import dataclass


@dataclass
class Author:
    id: str
    url: str
    first_name: str
    last_name: str

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
