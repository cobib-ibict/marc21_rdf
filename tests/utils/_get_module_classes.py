import importlib
import inspect


def get_module_classes(module_path: str):
    module = importlib.import_module(module_path)
    return [classe for name, classe in inspect.getmembers(module, inspect.isclass)]


def get_module_class_names(module_path: str):
    return [classe.__name__.lower() for classe in get_module_classes(module_path)]
