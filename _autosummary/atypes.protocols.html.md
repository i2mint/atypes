# atypes.protocols

Protocols for sound recognition

### Classes

| [`ChkFeaturizer`](#atypes.protocols.ChkFeaturizer)(\*args, \*\*kwargs)   |                                                        |
|--------------------------------------------------------------------------------------|--------------------------------------------------------|
| [`Gettable`](#atypes.protocols.Gettable)(\*args, \*\*kwargs)        | The missing type for objects that can be fetched from. |
| [`Sliceable`](#atypes.protocols.Sliceable)(\*args, \*\*kwargs)       | Can fetch an element from obj with brackets: obj[i:j]  |
| [`WfChunker`](#atypes.protocols.WfChunker)(\*args, \*\*kwargs)       | Experimental.                                          |

### *class* atypes.protocols.ChkFeaturizer(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

### *class* atypes.protocols.Gettable(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

The missing type for objects that can be fetched from.
The contract is that we can fetch an element from `obj` with brackets: `obj[k]`.
That is, `obj` has a `__getitem__` method.

```pycon
>>> isinstance(3, Gettable)  # 3 is not Gettable (can't do 3[...])
False
```

But `dict`, `list`, and `str` are Gettable:

```pycon
>>> isinstance([1, 2, 3], Gettable)
True
>>> isinstance({'foo': 'bar'}, Gettable)
True
>>> isinstance('foo', Gettable)
True
```

Note that so are their types:

```pycon
>>> all(isinstance(c, Gettable) for c in (list, dict, str))
True
```

### *class* atypes.protocols.Sliceable(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

Can fetch an element from obj with brackets: obj[i:j]

```pycon
>>> t: Sliceable = 3  # will make linter complain
>>> tt: Sliceable = [1, 2, 3]  # linter won't complain because a list is Gettable
```

### *class* atypes.protocols.WfChunker(\*args, \*\*kwargs)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

Experimental. Doesn’t have the desired behavior (yet).

```text
foo: WfChunker

# linter (unexpectedly) DOES NOT COMPLAIN
def foo(wf) -> int:
    return 3


def bar(wf_chunker: WfChunker):
    return 42


bar(wf_chunker=3)  # linter complains (wf_chunker not Callable)
bar(wf_chunker=lambda wf: 3)  # linter complains (wf_chunker doesn't return iterable)
bar(wf_chunker=lambda wf: [1, 2, 3])  # linter complains
bar(wf_chunker=lambda wf: [[1, 2, 3], [4, 5]])  # linter (unexpectedly) complains
bar(wf_chunker=lambda wf: None)  # linter (unexpectedly) DOES NOT complain


def not_a_chunker(wf):
    return 3


bar(wf_chunker=not_a_chunker)  # linter complains


def chunker(wf):
    return [[1, 2, 3], [3, 4, 5]]


bar(wf_chunker=chunker)  # linter (unexpectedly) complains


def annotated_chunker(wf: Waveform) -> Chunks:
    return [[1, 2, 3], [3, 4, 5]]


bar(wf_chunker=annotated_chunker)  # linter (unexpectedly) complains


def still_not_a_chunker(wf):
    return 3


still_not_a_chunker: WfChunker
bar(wf_chunker=still_not_a_chunker)  # linter (unexpectedly) DOES NOT COMPLAIN


# Try again with

from atypes.typ import Waveform, Chunks

WfChunker = Callable[[Waveform], Chunks]

# There, too many cases pass
```
