from . import queues

submodules = ["Stacks"]
__version__ = "0.3.4"
__name__ = "danielsdatastructures"
__author__ = "Daniel Sääw"
__all__ = submodules + ["__version__", "__name__"]

import importlib as _importlib

def __getattr__(name):
    if name in submodules:
        _importlib.import_module(f"danielsdatastructures.{name}")
    else:
        try:
            return globals()[name]
        except KeyError:
            raise AttributeError(
                f"Module 'danielsdatastructures' has no attribute '{name}'"
            )