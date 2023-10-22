import os
from typing import Optional

from jinja2 import Environment, FileSystemLoader, select_autoescape

from marc21_rdf.interfaces import PublicationInterface


class RDF:
    def __init__(self, *args, **kwargs) -> None:
        self.__env = Environment(
            loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)),
            autoescape=select_autoescape(),
        )
        self.__cache: Optional[str] = None

    def build(self, obj: PublicationInterface, *args, **kwargs) -> str:
        self.__template = self.__env.get_template(obj.template_name)
        self.__cache = self.__template.render(obj=obj)
        return self.__cache

    def write(self, file_name: str, extension: Optional[str] = 'rdf') -> None:
        if not self.__cache:
            raise ValueError('The build method must be executed before writing.')
        with open(f'{file_name}.{extension}', 'w') as file:
            file.write(self.__cache)
            self.__cache = None
