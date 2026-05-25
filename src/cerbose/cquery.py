# SPDX-License-Identifier: LGPL-3.0-or-later

# Cerbose v2.0.0 | made by jasperredis | LGPLv3 (see LICENSE)
# cquery module

__version__ = "2.0.0"

# Import modules
from .cprint import cprint, mprint

def _get_cquery(options, cprint, lower):
    while True:
        ans = input("> ")
        if lower:
            ans = ans.lower()
        if options != "*" and ans not in options:
            cprint("error", f"'{ans}' is not a valid option!")
        else:
            break
    return ans

def cquery(
    tag,
    text,
    options,
    *,
    text_colour="normal",
    subtag=None,
    timestamp=False,
    log_file=None,
    lower=False,
    show_opts=False,
):
    """
    Take user input. https://jasperredis.github.io/cerbose/docs.html?page=docs-cin.md
    """
    print_text = text
    if show_opts and options != "*":  # Print options
        count = 0
        for item in options:
            count += 1
            print_text += f"\n{count}) {item}"
    mprint( # Actually print options
        tag,
        print_text,
        text_colour=text_colour,
        subtag=subtag,
        timestamp=timestamp,
        log_file=log_file,
    )
    return _get_cquery(options, cprint, lower)

def cyn(tag, text, **kwargs):
    return cquery(tag, text, ["y", "n"], lower=True, **kwargs)
