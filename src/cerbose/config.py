# SPDX-License-Identifier: LGPL-3.0-or-later

# Cerbose v2.0.0 | made by jasperredis | LGPLv3 (see LICENSE)
# configuration module

__version__ = "2.0.0"

# Config variables
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

symbols = {
    "bracket_left": "[",
    "bracket_right": "]",
    "divider": ":",
    "fill_symbol": "#",
    "empty_symbol": "-"
}

space_repeat_tolerance = 5
time_format = "%H:%M:%S"

# Optional wrapper functions
def add_tag(name, text, colour):
    global tags
    tags[name] = { "text": text, "colour": colour }

def remove_tag(name):
    global tags
    tags.pop(name)
