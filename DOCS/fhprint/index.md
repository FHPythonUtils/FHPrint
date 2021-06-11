# fhprint

> Auto-generated documentation for [fhprint](../../fhprint/__init__.py) module.

Print in fancy ways.

- [Fhprint](../README.md#fhprint-index) / [Modules](../README.md#fhprint-modules) / fhprint
    - [LogCode](#logcode)
    - [Logger](#logger)
        - [Logger().pprint](#loggerpprint)
        - [Logger().pstr](#loggerpstr)

## LogCode

[[find in source code]](../../fhprint/__init__.py#L10)

```python
class LogCode(str, Enum):
```

Provide the capability to use an enum for logcodes if the user prefers.

BOLD = "bold"
ITALIC = "italic"
HEADING = "head"
DEBUG = "d"
INFO = "i"
OK = "ok"
WARNING = "w"
ERROR = "e"
CRITICAL = "crit"

## Logger

[[find in source code]](../../fhprint/__init__.py#L38)

```python
class Logger():
    def __init__(mapping: dict[(str, str)] = None) -> None:
```

Logger class. Can be used to make a custom logger.

pprint and pstr methods have the same signature as the inbuilt print
method so migration is easy and use ll/loglevel. For prefab methods
supplied by this library, ll/loglevel can be any of:

"bold": For bold text,
"italic": For italic text,
"head": For a heading,
"d": For a debug message,
"i": Info message,
"ok": For some successful operation,
"w": For a warning,
"e": For some error,
"crit": For some critical event,

However, you can create your own... eg `mylogger = Logger({"cat": "🐱 {}"})
to add a cat emoji before a message (if so inclined)

### Logger().pprint

[[find in source code]](../../fhprint/__init__.py#L89)

```python
def pprint(
    sep: str = ' ',
    end: str = '\n',
    file: TextIO = sys.stdout,
    flush: bool = False,
    ll: str = '',
    loglevel: str = None,
    *values: object,
):
```

The pprint function with the same signature as the inbuilt print...

method so migration is easy and use ll/loglevel. For prefab methods
supplied by this library, ll/loglevel can be any of:

"bold": For bold text,
"italic": For italic text,
"head": For a heading,
"d": For a debug message,
"i": Info message,
"ok": For some successful operation,
"w": For a warning,
"e": For some error,
"crit": For some critical event,

#### Arguments

- `*values` *tuple[object]* - values to print to stream
- `sep` *str, optional* - string inserted between values. Defaults to " ".
- `end` *str, optional* - string appended after last value. Defaults to "\n".
- `file` *TextIO, optional* - a file like object/ stream. Defaults to sys.stdout.
- `flush` *bool, optional* - whether to forcibly flush the stream. Defaults to False.
- `ll` *str, optional* - set the loglevel (shorthand). Defaults to "".
- `loglevel` *str, optional* - set the loglevel, omit this for normal print behaviour. Defaults to "".

### Logger().pstr

[[find in source code]](../../fhprint/__init__.py#L130)

```python
def pstr(
    sep: str = ' ',
    end: str = '\n',
    ll: str = '',
    loglevel: str = None,
    *values: object,
) -> str:
```

The pstr function with a similar signature as the inbuilt print...

method so migration is easy and use ll/loglevel. For prefab methods
supplied by this library, ll/loglevel can be any of:

"bold": For bold text,
"italic": For italic text,
"head": For a heading,
"d": For a debug message,
"i": Info message,
"ok": For some successful operation,
"w": For a warning,
"e": For some error,
"crit": For some critical event,

#### Arguments

- `*values` *tuple[object]* - values to create string from
- `sep` *str, optional* - string inserted between values. Defaults to " ".
- `end` *str, optional* - string appended after last value. Defaults to "\n".
- `ll` *str, optional* - set the loglevel (shorthand). Defaults to "".
- `loglevel` *str, optional* - set the loglevel, omit this for normal print behaviour. Defaults to "".

#### Returns

- `str` - Formatted string
