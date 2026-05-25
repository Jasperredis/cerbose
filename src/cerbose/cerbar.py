# SPDX-License-Identifier: LGPL-3.0-or-later

# Cerbose v2.0.0 | made by jasperredis | LGPLv3 (see LICENSE)
# cerbar module

__version__ = "2.0.0"

# Import modules
from . import config

def cerbar(length, total, fill, *, percent=None, count=None):
    """
    Output an ASCII progress bar (with formatting). https://jasperredis.github.io/cerbose/docs.html?page=docs-cerbar.md
    """
    item = total / length
    fillcnt = fill / item
    filled_chars = round(fillcnt)
    filltxt = config.symbols["fill_symbol"] * filled_chars
    remaincnt = length - filled_chars
    remaintxt = config.symbols["empty_symbol"] * remaincnt

    # Get percentage (if needed)
    percent_val = None
    if percent is not None:
        percent_val = (fill / total) * 100
        percent_val = round(percent_val, 3)

    # Form output
    output = ""
    # Add left statistics
    if percent == "l":
        output += f"{percent_val:.1f}% "
    if count == "l":
        output += f"({fill}/{total}) "
    # Add bar
    output += f"{config.symbols['bracket_left']}{filltxt}{remaintxt}{config.symbols['bracket_right']}"
    # Add right statistics
    if percent == "r":
        output += f" {percent_val:.1f}%"
    if count == "r":
        output += f" ({fill}/{total})"
    return output
