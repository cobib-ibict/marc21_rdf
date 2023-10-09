from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Publisher:
    id: str
    url: str
    first_name: str
    last_name: str


@dataclass
class Article:
    id: str
    url: str
    subject: str
    publisher: Publisher
    city: str
    issn: str
    language: str = 'pt-BR'
    abstract: Optional[str] = None
    published_at: Optional[datetime] = None

    @property
    def author_ship(self) -> str:
        return f'/publishers/{self.publisher.id}/articles/{self.id}'
