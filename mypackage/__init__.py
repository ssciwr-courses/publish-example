try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata  # type: ignore
from mypackage.transform import area_circ
from mypackage.decorator import my_decorator

# Export the version defined in project metadata
__version__ = metadata.version(__package__)
del metadata

__all__ = [
    "area_circ",
    "my_decorator",
]
