import contextlib
from contextvars import ContextVar

current_tag = ContextVar("tag", default=None)


@contextlib.contextmanager
def with_tag(tag):
    _old = current_tag.get()
    current_tag.set(tag)
    try:
        yield
    finally:
        current_tag.set(_old)
