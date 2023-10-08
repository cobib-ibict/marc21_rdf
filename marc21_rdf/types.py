from dataclasses import dataclass


@dataclass
class Publisher:
    id: str
    url: str
    first_name: str
    last_name: str


@dataclass
class Publication:
    id: str
    url: str
    subject: str
    publisher: Publisher
    city: str
    issn: str
    language: str

    @property
    def author_ship(self) -> str:
        return f'/publishers/{self.publisher.id}/publications/{self.id}'
