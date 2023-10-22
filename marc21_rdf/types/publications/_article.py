from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from marc21_rdf.interfaces import PublicationInterface
from marc21_rdf.types.authors import Author
from marc21_rdf.types.publishers import Publisher


@dataclass
class Article(PublicationInterface):
    id: str
    url: str
    subject: str
    author: Author
    publisher: Publisher
    city: str
    issn: str
    language: str = 'pt-BR'
    abstract: Optional[str] = None
    published_at: Optional[datetime] = None
