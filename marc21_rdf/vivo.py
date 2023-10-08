import os
from typing import Optional

from jinja2 import Environment, FileSystemLoader, select_autoescape

from marc21_rdf.types import Publisher


class RDF:
    def __init__(
        self,
        template_name: str = 'vivo_template.rdf',
        host_name: Optional[str] = 'http://example.com/article',
        content_id: Optional[str] = '5554',
    ) -> None:
        self.host_name = host_name
        self.content_id = content_id
        self.__env = Environment(
            loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)),
            autoescape=select_autoescape(),
        )
        self.__template = self.__env.get_template(template_name)
        self.__cache: Optional[str] = None

    def build(
        self,
        subject: str,
        publisher: Publisher,
        city: str,
        issn: str,
        language: str = 'pt-BR',
        content_url: Optional[str] = None,
    ) -> str:
        if not content_url:
            content_url = f'{self.host_name}/{self.content_id}'
        self.__cache = self.__template.render(
            title=subject,
            publisher=publisher,
            city=city,
            issn=issn,
            language=language,
            content_url=content_url,
        )
        return self.__cache

    def write(self, file_name: str, extension: Optional[str] = 'rdf') -> None:
        if not self.__cache:
            raise ValueError('Build method is required before Write')
        with open(f'{file_name}.{extension}', 'w') as file:
            file.write(self.__cache)
            self.__cache = None
