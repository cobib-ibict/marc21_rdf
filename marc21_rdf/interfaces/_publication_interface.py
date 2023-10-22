class PublicationInterface:
    @property
    def __name__(self) -> str:
        return self.__class__.__name__

    @property
    def template_name(self) -> str:
        return f'{self.__name__.lower()}_template.rdf'
