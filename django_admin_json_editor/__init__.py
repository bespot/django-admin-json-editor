from .admin import JSONEditorWidget  # noqa

try:
    from .version import __version__
except ImportError:
    __version__ = '0.2.0+bespot.1'
