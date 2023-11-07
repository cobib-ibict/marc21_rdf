from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from marc21_rdf.interfaces import PublicationInterface
from marc21_rdf.types.authors import Author
from marc21_rdf.types.editors import Editor
from marc21_rdf.types.publishers import Publisher


@dataclass
class Book(PublicationInterface):
    id: str
    url: str
    subject: str
    author: Author
    editor: Editor
    publisher: Publisher
    published_at: datetime
    city: str
    issn: str
    language: str = 'pt-BR'
    abstract: Optional[str] = None
    volume: Optional[str] = None
    number: Optional[str] = None
    num_pages: Optional[int] = None
    doi: Optional[str] = None
    isbn: Optional[str] = None
    edition: Optional[str] = None
