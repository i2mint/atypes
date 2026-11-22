# atypes.util

Utilities to use in atypes functionality

### Functions

| [`MyType`](#atypes.util.MyType)(name[, tp, doc, aka, assign_to_globals])   | Like `typing.NewType` with some extras (`__doc__` and `_aka` attributes, etc.)   |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [`MyVar`](#atypes.util.MyVar)(name[, constraint, doc, aka, ...])          | Like `typing.TypeVar` with some extras (`__doc__` and `_aka` attributes, etc.)   |

### atypes.util.MyType(name, tp=typing.Any, doc=None, aka=None, , assign_to_globals=False)

Like `typing.NewType` with some extras (`__doc__` and `_aka` attributes, etc.)

See (NewType docs)[[https://docs.python.org/3/library/typing.html#typing.NewType](https://docs.python.org/3/library/typing.html#typing.NewType)]
for more.

* **Parameters:**
  * **name** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str)) – Name to give the variable
  * **tp** ([`type`](https://docs.python.org/3/builtins/functions.html#type)) – Type
  * **doc** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str) | [`None`](https://docs.python.org/3/builtins/constants.html#None)) – Optional string to put in \_\_doc_\_ attribute
  * **aka** ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str) | [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str)] | [`None`](https://docs.python.org/3/builtins/constants.html#None)) – Optional set (or any iterable) to put in \_aka attribute,
    meant to list names the variables of this type often appear as.
* **Returns:**
  None

```pycon
>>> from typing import Any, List
>>> T = MyType('T')  # can be Anything (`Any` is the default type
>>> Key = MyType('Key', Any, aka=['key', 'k'])
```

The `aka` argument will be added to the a `._aka` attribute, which is a set
containing names instances of the type might come as.

```pycon
>>> assert isinstance(Key._aka, set)
>>> sorted(Key._aka)
['k', 'key']
```

You can also add docs:

```pycon
>>> Val = MyType(
... 'Val',
... Union[int, float, List[Union[int, float]]],
... doc="A number or list of numbers."
... )
>>> Val.__doc__
'A number or list of numbers.'
```

`MyType` is neither a type nor returns a type – contrary to what the name would
make you expect. We chose this name to mimic `typing.NewType` since `MyType` just
does what `NewType` does, just a bit more.
What is returned is really the identity function, so
`x is NewType('Name', int)(x)` is always `True`.

```pycon
>>> callable(Val)  # a function (py<3.10) or a typing.NewType (py>=3.10)
True
```

### atypes.util.MyVar(name, constraint=typing.Any, \*more_constraints, doc=None, aka=None, covariant=False, contravariant=False, assign_to_globals=False)

Like `typing.TypeVar` with some extras (`__doc__` and `_aka` attributes, etc.)

See (TypeVar docs)[[https://docs.python.org/3/library/typing.html#typing.TypeVar](https://docs.python.org/3/library/typing.html#typing.TypeVar)]
for more.

```pycon
>>> from typing import Any, List, Union
>>> Key = MyVar('Key', Any, aka=['key', 'k'])
```

The `aka` argument will be added to the a `._aka` attribute, which is a set
containing names instances of the type might come as.

```pycon
>>> assert isinstance(Key._aka, set)
>>> sorted(Key._aka)
['k', 'key']
```

You can also add docs:

```pycon
>>> Val = MyVar(
... 'Val',
... int, float, List[Union[int, float]],
... doc="A number or list of numbers.")
>>> Val.__doc__
'A number or list of numbers.'
```

Contrary to `MyType`, `MyVar` actually returns a type (though `MyVar` is not
itself a type, contrary to pep8’s expectations – blame `typing.NewVar`;
`MyVar` is just an enanced version of it).

```pycon
>>> type(Val)
<class 'typing.TypeVar'>
```
