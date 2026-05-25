# Changelog

## 1.0.0
- Released the library. (well duh)


## 1.0.0.post1
- Fixed some issues with the PyPI library (misconfigured pyproject.toml)


## 1.0.1
General patches and maintainability updates:

- Fixed bug where using a non-existent file would output "[ERROR]: File '{content}' does not exist."
- Fixed bug where using a non-existent colour in textcol in cprint (or any function that relies on cprint) would supress the output and only print a warning.
- Renamed internal functions to be snake_case.
- Used black to format to PEP 8.

Yes, this was copied from the commit message, but that's because said commit message was concise and explained what this did well.


## 1.0.1.post1
Updated repository link in pyproject.toml to new repository.


## 2.0.0
Near-entire rewrite, several breaking changes, new function, and more:

### Breaking Changes
- New configuration system. See docs for more info, but to summarise, individual options are modified, either by wrapper functions (config.add_tag()) or manual variable changes.
- Renamed parameters: 
  - `stagtype` → `subtag`
  - `logfile` → `log_file`
  - `textcol` → `text_colour`
  - `valonly` → `as_string`
  - `showop` → `show_opts`
- `cin()` renamed to `cquery()`.
- `cquery()` (now formerly `cin()`) wildcard changed from `'any'` to `'*'`.

### New Features
- New function `cyn()`; wrapper for `cquery()` with options as y/n.

### Other Changes
- Codebase is now entirely modularised; split across:
  - `__init__.py`
  - `cerbar.py`
  - `colours.py`
  - `config.py`
  - `cprint.py`
  - `cquery.py`
- Cleaned up a lot of terribly coded internal logic, especially in `cprint()`/`mprint()`.
- `INTERNAL_SUBSITUTE` now `COLOURS` (from `colours.py`).

### External Changes
- Updated docs, not only along with these updates, but also with a note about this library not using American English.
- Updated `examples/test.py` to use the new names of everything.
- Updated the website to use the new names of everything.
- Removed `examples/config.json` as file support no longer exists.
