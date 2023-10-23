import pytest

from marc21_rdf.utils import get_module_class_names, get_module_classes


@pytest.fixture
def module_name():
    return 'marc21_rdf.types.publications'


def test_get_module_classes(module_name):
    classes = get_module_classes(module_name)
    assert len(classes) > 0


def test_get_module_class_names(module_name):
    class_names = get_module_class_names(module_name)
    assert len(class_names) > 0


def test_get_module_classes_nonexistent_module():
    with pytest.raises(ModuleNotFoundError):
        get_module_classes('nonexistent_module')


def test_get_module_class_names_nonexistent_module():
    with pytest.raises(ModuleNotFoundError):
        get_module_class_names('nonexistent_module')


def test_get_module_classes_empty_module():
    with pytest.raises(ModuleNotFoundError):
        get_module_classes('empty_module')


def test_get_module_class_names_empty_module():
    with pytest.raises(ModuleNotFoundError):
        get_module_class_names('empty_module')
