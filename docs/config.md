# Configuration
A lot of items in this documentation have referenced this very file for configuration.  
Cerbose is configured using variables (and, optionally, wrapper functions) found in `config.py`.

## Tags
Tags in Cerbose are stored in the `config.tags` dict. Here is an example tag:  
```python
{ "name": { "colour": "white", "text": "NAME" }
```
Use this structure for defining tags. Or, use the `config.add_tag` and/or `config.remove_tag` functions:  
```python
config.add_tag("name", "text", "colour")
config.remove_tag("name")
```
Here is the default tags dict:
```python
tags = {
    "none":  { "text": "NONE",  "colour": "white"     },
    "ok":    { "text": "OK",    "colour": "green"     },
    "note":  { "text": "NOTE",  "colour": "cyan"      },
    "warn":  { "text": "WARN",  "colour": "yellow"    },
    "error": { "text": "ERROR", "colour": "red"       },
    "debug": { "text": "DEBUG", "colour": "magenta"   },
    "info":  { "text": "INFO",  "colour": "cyan"      },
    "input": { "text": "INPUT", "colour": "lightblue" },
    "query": { "text": "QUERY", "colour": "lightblue" },
    "load":  { "text": "LOAD",  "colour": "red"       },
    "pause": { "text": "PAUSE", "colour": "yellow"    },
    "stat":  { "text": "STAT",  "colour": "magenta"   },
    "fatal": { "text": "FATAL", "colour": "red"       },
    "trace": { "text": "TRACE", "colour": "magenta"   },
    "proc":  { "text": "PROC",  "colour": "magenta"   }
}
```

## Symbols
The symbols in Cerbose, such as the brackets on tags (**`[`**`OK`**`]`**) or the space in `cerbar`, are customisable.  
To customise them, modify them in the `config.symbols` dict. Here is this dict:  
```python
symbols = {
    "bracket_left": "[",
    "bracket_right": "]",
    "divider": ":",
    "fill_symbol": "#",
    "empty_symbol": "-"
}
```
> Note: As of Cerbose v2.0.0, `bracket_left` and `bracket_right` apply to both the brackets on `cprint`/`cprint`-based functions *and* `cerbar`.

## Other Settings
There are two other settings that you can configure in Cerbose:
- `config.space_repeat_tolerance`: See `cprint.md`.
- `config.timestamp_format`: The `strftime` format for `cprint` timestamps. See https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior for time formatting (it uses this function).
