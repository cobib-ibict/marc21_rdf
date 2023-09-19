from random import randint

import pytest
from faker import Faker

from marc21_rdf import RDF

fake = Faker()


@pytest.fixture
def rdf() -> RDF:
    return RDF(content_id=f'n{randint(100, 999)}')


def test_rdf_build(rdf: RDF):
    sut = rdf.build(
        fake.paragraph(nb_sentences=1),
        fake.name(),
        fake.city(),
        fake.postcode(),
        'pt-BR',
    )
    assert isinstance(sut, str)


def test_rdf_write(rdf: RDF):
    try:
        rdf.build(
            fake.paragraph(nb_sentences=1),
            fake.name(),
            fake.city(),
            f'{fake.random}',
            'pt-BR',
        )
        rdf.write('tests/test')
    except Exception:
        assert False


def test_rdf_write_error(rdf: RDF):
    try:
        rdf.write('tests/test')
    except Exception as error:
        assert isinstance(error, ValueError)
