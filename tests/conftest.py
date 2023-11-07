from datetime import datetime
from random import randint

import pytest
from faker import Faker

from marc21_rdf import RDF
from marc21_rdf.types.authors import Author
from marc21_rdf.types.editors import Editor
from marc21_rdf.types.publications import Article, Book, Journal
from marc21_rdf.types.publishers import Publisher

fake = Faker()


@pytest.fixture(scope='function')
def rdf() -> RDF:
    return RDF()


@pytest.fixture
def article() -> Article:
    return Article(
        id=randint(100, 999),
        subject=fake.paragraph(nb_sentences=1),
        abstract=fake.paragraph(nb_sentences=10),
        url=f'http://pinakes.ccn.com/article/{randint(100, 999)}',
        author=Author(
            id=randint(100, 999),
            url=f'http://pinakes.ccn.com/author/{randint(100, 999)}',
            first_name=fake.name().split(' ')[0],
            last_name=fake.name().split(' ')[1],
        ),
        publisher=Publisher(
            id=randint(100, 999),
            url=f'http://pinakes.ccn.com/person/{randint(100, 999)}',
            first_name=fake.name().split(' ')[0],
            last_name=fake.name().split(' ')[1],
        ),
        city=fake.city(),
        issn=randint(100, 999),
        language='pt-BR',
        published_at=datetime.now(),
    )


@pytest.fixture
def journal() -> Journal:
    return Journal(
        id=randint(100, 999),
        subject=fake.paragraph(nb_sentences=1),
        abstract=fake.paragraph(nb_sentences=10),
        url=f'http://pinakes.ccn.com/Journal/{randint(100, 999)}',
        author=Author(
            id=randint(100, 999),
            url=f'http://pinakes.ccn.com/author/{randint(100, 999)}',
            first_name=fake.name().split(' ')[0],
            last_name=fake.name().split(' ')[1],
        ),
        publisher=Publisher(
            id=randint(100, 999),
            url=f'http://pinakes.ccn.com/publisher/{randint(100, 999)}',
            first_name=fake.name().split(' ')[0],
            last_name=fake.name().split(' ')[1],
        ),
        city=fake.city(),
        issn=randint(100, 999),
        language='pt-BR',
        published_at=datetime.now(),
    )


@pytest.fixture
def book() -> Book:
    return Book(
        id=randint(100, 999),
        subject=fake.paragraph(nb_sentences=1),
        abstract=fake.paragraph(nb_sentences=10),
        url=f'http://pinakes.ccn.com/Book/{randint(100, 999)}',
        author=Author(
            id=randint(100, 999),
            url=f'http://pinakes.ccn.com/author/{randint(100, 999)}',
            first_name=fake.name().split(' ')[0],
            last_name=fake.name().split(' ')[1],
        ),
        editor=Editor(
            id=randint(100, 999),
            url=f'http://pinakes.ccn.com/editor/{randint(100, 999)}',
            first_name=fake.name().split(' ')[0],
            last_name=fake.name().split(' ')[1],
        ),
        publisher=Publisher(
            id=randint(100, 999),
            url=f'http://pinakes.ccn.com/publisher/{randint(100, 999)}',
            first_name=fake.name().split(' ')[0],
            last_name=fake.name().split(' ')[1],
        ),
        city=fake.city(),
        issn=randint(100, 999),
        language='pt-BR',
        published_at=datetime.now(),
        doi='doi 123',
        edition='2° edição',
        isbn='12345',
        num_pages=20,
        number=1,
        volume='1',
    )


@pytest.fixture
def instance(
    article: Article, book: Book, journal: Journal, request: pytest.FixtureRequest
):
    if not hasattr(request, 'param'):
        raise ValueError(
            'Param is required! Use: @pytest.mark.parametrize("instances", ["journal"], indirect=True)'
        )
    return {
        'article': article,
        'book': book,
        'journal': journal,
    }.get(request.param)
