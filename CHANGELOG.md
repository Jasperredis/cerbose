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
