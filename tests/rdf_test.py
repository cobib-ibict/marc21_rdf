import os

import pytest

from marc21_rdf import RDF
from marc21_rdf.interfaces import PublicationInterface
from marc21_rdf.utils import get_module_class_names

instances_types = get_module_class_names('marc21_rdf.types.publications')


@pytest.mark.parametrize('instance', instances_types, indirect=True)
def test_rdf_build(rdf: RDF, instance: PublicationInterface):
    sut = rdf.build(instance)
    assert isinstance(sut, str)


@pytest.mark.parametrize('instance', instances_types, indirect=True)
def test_rdf_write(rdf: RDF, instance: PublicationInterface):
    file_path = f'tests/out/{instance.__name__}'
    try:
        rdf.build(instance)
        rdf.write(file_path)
    except Exception:
        assert False
    assert os.path.exists(f'{file_path}.rdf'), f'File {file_path} not found.'


def test_rdf_write_error(rdf: RDF):
    file_path = 'tests/out/error_file'
    try:
        rdf.write(file_path)
    except Exception as error:
        assert isinstance(error, ValueError)
    assert not os.path.exists(f'{file_path}.rdf'), f'File {file_path} not found.'
