from random import randint

import pytest
from faker import Faker

from marc21_rdf import RDF
from marc21_rdf.types import Publication, Publisher

fake = Faker()


@pytest.fixture
def rdf() -> RDF:
    return RDF()


@pytest.fixture
def publication() -> Publication:
    return Publication(
        id=randint(100, 999),
        subject=fake.paragraph(nb_sentences=1),
        url=f'http://pinakes.ccn.com/article/{randint(100, 999)}',
        publisher=Publisher(
            id=randint(100, 999),
            url=f'http://pinakes.ccn.com/person/{randint(100, 999)}',
            first_name=fake.name().split(' ')[0],
            last_name=fake.name().split(' ')[1],
        ),
        city=fake.city(),
        issn=randint(100, 999),
        language='pt-BR',
    )


def test_rdf_build(rdf: RDF, publication: Publication):
    sut = rdf.build(publication)
    assert isinstance(sut, str)


def test_rdf_write(rdf: RDF, publication: Publication):
    try:
        rdf.build(publication)
        rdf.write('tests/test')
    except Exception:
        assert False


def test_rdf_write_error(rdf: RDF):
    try:
        rdf.write('tests/test')
    except Exception as error:
        assert isinstance(error, ValueError)
