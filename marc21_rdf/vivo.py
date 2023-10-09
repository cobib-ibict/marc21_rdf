import os
from typing import Optional

from jinja2 import Environment, FileSystemLoader, select_autoescape

from marc21_rdf.types import Article


class RDF:
    def __init__(
        self, template_name: str = 'vivo_template.rdf', *args, **kwargs
    ) -> None:
        self.__env = Environment(
            loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)),
            autoescape=select_autoescape(),
        )
        self.__template = self.__env.get_template(template_name)
        self.__cache: Optional[str] = None

    def build(self, article: Article, *args, **kwargs) -> str:
        self.__cache = self.__template.render(article=article)
        return self.__cache

    def write(self, file_name: str, extension: Optional[str] = 'rdf') -> None:
        if not self.__cache:
            raise ValueError('Build method is required before Write')
        with open(f'{file_name}.{extension}', 'w') as file:
            file.write(self.__cache)
            self.__cache = None
