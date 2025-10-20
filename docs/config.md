# Configuration
A lot of items in this documentation have referenced this very file for configuration.  
Cerbose uses JSON files for its configuration. These allow lots of configurations, including:
- Custom tags (text and colour required)
- Symbols (e.g., brackets, text divisor, `cerbar` characters)
- Space repeat tolerance
- Timestamp format
Skip to the "defconf" header for setting configs in your program.

## Meta
This is a completely optional section of your JSON file that has yet to see any use. However, you can add it incase it gets a use in the future:
```json
// There are comments here. JSON does not support comments. Please pretend that it does.
"meta" {
  "program": "" // What program this configuration was primarily made for.
  "author": ""  // You, obviously.
}
```

## Tags
This is where you define, well, tags. Having the "colours" and "text" keys is required. Defining tags:
```json
// There are comments here. JSON does not support comments. Please pretend that it does.
"colours": {
  "mycooltag": "magenta"
},
"text": {
  "mycooltag": "COOLIO"
}
// Add your tag's colour and text like this for every tag you want to add.
```
Setting symbols (e.g., [ in [OK]). All of these are **MANDATORY!!**:
```json
"symbols": {
    "bracket left": "[",  // [ in [OK]:
    "bracket right": "]", // ] in [OK]:
    "text divisor": ":"   // : in [OK]:
}
```

## Cerbar
This is where you set symbols for cerbar.
```json
  "cerbar": {
      "bracket left": "[",  // [ in [####----]
      "bracket right": "]", // ] in [####----]
      "fill symbol": "#",   // # in [####----]
      "empty symbol": "-"   // - in [####----]
  },
```

## Other Root
These go below all of the previous tags.
```json
    "space-repeat-tolerance": 5, // How many times padding can repeat, see cprint.md
    "timeformat": "%H:%M:%S"     // Time formatting.
```
See https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior for time formatting (it uses this function).

## Full Config
This is the default configuration.
```json
{
  "meta": {
    "program": "Cerbose",
    "author": "jasperredis"
  },
  "tags": {
    "colours": {
      "none": "white",
      "ok": "green",
      "note": "cyan",
      "warn": "yellow",
      "error": "red",
      "debug": "magenta",
      "info": "cyan",
      "input": "lightblue",
      "load": "red",
      "pause": "yellow",
      "stat": "magenta",
      "fatal": "red",
      "trace": "magenta",
      "proc": "magenta"
    },
    "text": {
      "none": "NONE",
      "ok": "OK",
      "note": "NOTE",
      "warn": "WARN",
      "error": "ERROR",
      "debug": "DEBUG",
      "info": "INFO",
      "input": "INPUT",
      "load": "LOAD",
      "pause": "PAUSE",
      "stat": "STAT",
      "fatal": "FATAL",
      "trace": "TRACE",
      "proc": "PROC"
    },
    "symbols": {
      "bracket left": "[",
      "bracket right": "]",
      "text divisor": ":"
    }
  },
  "cerbar": {
    "bracket left": "[",
    "bracket right": "]",
    "fill symbol": "#",
    "empty symbol": "-"
  },
  "space-repeat-tolerance": 5,
  "timeformat": "%H:%M:%S"
}
```

## defconf
`defconf` in Cerbose is a function to set your configuration.  
In Cerbose, `defconf()` is defined as:
```python
def defconf(type, content)
```
This means that both `type` and `content` are required.  

The `type` variable can be set to `'f'`/`'file'` or `'i'`/`'input'`.  
If set to `'f'`/`'file'`, `content` must be set to the path to a configuration file.  
Example:
```python
cerbose.defconf('f', 'config.json')
```
It will then load the file and set the configuration.  

If `type` is set to `'i'`/`'input'`, `content` must be set to a raw JSON string or dict.  
A raw JSON string looks like a string containing a JSON file's contents.  
Example:
```
string = '{"meta": {"program": "Cerbose Default", "author": "jasperredis"}, "tags": {"colours": {"none": "white", "error": "red", "warn": "yellow", "info": "cyan"}, "text": {"none": "NONE", "error": "ERROR", "warn": "WARN", "info": "INFO"}, "symbols": {"bracket left": "[", "bracket right": "]", "text divisor": ":"}}, "cerbar": {"bracket left": "[", "bracket right": "]", "fill symbol": "#", "empty symbol": "-"}, "space-repeat-tolerance": 5, "timeformat": "%H:%M:%S"}'
```

If the wrong type is used, Cerbose will print out an error message.  
Example:
```plaintext
[ERROR]: defconf: File '{content}' does not exist.
```
> '`{content}`' is a bug. This should be fixed in the next update of Cerbose.

Cerbose **will** verify that a config file is valid. If not, it will print an error message explaining why it is not, e.g.:
```plaintext
[ERROR]: defconf: configIsValid: Invalid configuration was passed. Missing key: tags
[ERROR]: defconf: Config validity check failed.
```
