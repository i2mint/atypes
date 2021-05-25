"""Protocols for sound recognition"""

import typing as ty
from typing import Callable, Protocol, Iterable, Any

import atypes.scrap.slang as st
from atypes.scrap.slang import Waveform, Chunks


class Gettable(Protocol):
    """Can fetch an element from obj with brackets: obj[k]"""
    def __getitem__(self, k: Any) -> Any:
        pass

@ty.runtime_checkable
class WfChunker(Protocol):
    def __call__(self, wf: st.Waveform, *args, **kwargs) -> st.Chunks:
        """Transforms a waveform into an iterable of fixed sized iterables called chunks"""


@ty.runtime_checkable
class ChkFeaturizer(Protocol):
    def __call__(self, chk: st.Chunk, *args, **kwargs) -> st.Feature:
        """Transforms a waveform chk into an iterable of fixed sized iterables called chunks"""


import typing as ty
import collections.abc


class SizableIterable(collections.abc.Sized, collections.abc.Iterable):
    pass


class SizableIterable2(ty.Protocol):
    __len__: Callable
    __iter__: Callable


# return
# [[1, 2, 3], [3, 4, 5], [5, 6, 7]]  # Iterable[SizableIterable[T]]

T = ty.TypeVar("T")


class Chunker(ty.Protocol):
    def __call__(self, x: Iterable[T]) -> Iterable[SizableIterable[T]]:
        ...

