# SPDX-License-Identifier: LGPL-3.0-or-later

# Cerbose v2.0.0 | made by jasperredis | LGPLv3 (see LICENSE)
# cprint module

__version__ = "2.0.0"

# Import libraries
from colorama import Fore, Style
import datetime as dt
import re
# Import modules
from .colours import COLOURS
from . import config

align = 0
space_repeat_count = 0

def _create_tag(tag, subtag, timestamp):
    """Subfunction for cprint/mprint."""
    label = ""
    # Add timestamp
    if timestamp:
        date = dt.datetime.now()
        time_output = date.strftime(config.time_format)
        time_output = (
            f"{config.symbols['bracket_left']}{time_output}{config.symbols['bracket_right']}"
        )
        label += time_output
    # Add subtag
    if subtag != None:
        subtag = subtag if subtag in config.tags else "none"
        subtag_text = config.tags[subtag]["text"]
        subtag_colour = config.tags[subtag]["colour"]
        subtag_output = (
            f"{config.symbols['bracket_left']}{COLOURS[subtag_colour]}{subtag_text}{Style.RESET_ALL}{config.symbols['bracket_right']}"
        )
        label += subtag_output
    # Add tag
    if tag == "":
        tag_text = ""
    else:
        tag = tag if tag in config.tags else "none"
        tag_text = config.tags[tag]["text"]
        tag_colour = config.tags[tag]["colour"]
        tag_output = (
            f"{config.symbols['bracket_left']}{COLOURS[tag_colour]}{tag_text}{Style.RESET_ALL}{config.symbols['bracket_right']}"
        )
        label += tag_output
    return label

def _align_pad_label(label):
    """Subfunction for cprint/mprint."""
    global align, space_repeat_count
    # Align
    label_len = len(label)
    if label_len > align: # Update label length to new longest
        align = label_len
        space_repeat_count = 0
    else:
        # Reset space repeat count if over tolerance
        space_repeat_count += 1
        if space_repeat_count >= config.space_repeat_tolerance and align > label_len:
            align = label_len
            space_repeat_count = 0
    # Add padding
    padding_len = align - label_len
    padding = " " * padding_len
    label += padding
    return label

def _colour_text(text, text_colour):
    """Subfunction for cprint/mprint."""
    if text_colour in COLOURS:
        text = COLOURS[text_colour] + text
    return text

def _log(log_file, output):
    """Subfunction for cprint/mprint."""
    if log_file != None:
        with open(log_file, "a") as f:
             f.write(_strip_ansi(output + "\n"))

def _strip_ansi(string):
    """Subfunction for cprint/mprint."""
    return re.sub(r'\x1b\[[0-9;]*m', '', string)

def cprint(
    tag,
    text,
    *,
    text_colour="normal",
    subtag=None,
    timestamp=False,
    log_file=None,
    as_string=False,
):
    """Print a coloured, tagged message. https://jasperredis.github.io/cerbose/docs.html?page=docs-cprint.md"""
    global align, space_repeat_count
    label = _create_tag(tag, subtag, timestamp)
    label = _align_pad_label(label)
    text_result = _colour_text(text, text_colour)
    output = label + (config.symbols["divider"] + " ") + text_result
    _log(log_file, output)
    if as_string:
        return output
    else:
        print(output)

def mprint(
    tag,
    text,
    *,
    text_colour="normal",
    subtag=None,
    timestamp=False,
    log_file=None,
    as_string=False
):
    """Print a coloured, tagged message, with multiline. Heading "mprint" @ https://jasperredis.github.io/cerbose/docs.html?page=docs-cprint.md"""
    global align, space_repeat_count
    text = text.splitlines()
    label = _create_tag(tag, subtag, timestamp)
    label = _align_pad_label(label)
    label_len = len(_strip_ansi(label))
    divider = (config.symbols["divider"] + " ")
    text_result = _colour_text(text[0], text_colour)
    output = label + divider + text_result + "\n" + Style.RESET_ALL
    for i, line in enumerate(text[1:]):
        text_result = _colour_text(line, text_colour)
        padding = " " * label_len
        newline = "\n" if i != len(text) - 1 else ""
        output += padding + divider + text_result + newline + Style.RESET_ALL
    _log(log_file, output)
    if as_string:
        return output
    else:
        print(output)

def reset_align():
    """
    Resets all alignment-based variables (align and space_repeat_count).
    """
    global align, spacerepeatcount
    align = 0
    spacerepeatcount = 0
