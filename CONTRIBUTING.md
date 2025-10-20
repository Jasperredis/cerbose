# Contributing
This file explains how to contribute to Cerbose!  


**What files can I contribute to?**
- All of them
- That technically includes `LICENSE`, but...why?
- Anyway, contribute to:
  + Source code (`src/cerbose`)
  + Documentation (`docs/`)
  + Tests (`examples/`)
  + Config/build files (`pyproject.toml`, `requirements.txt`, `MANIFEST.in`, etc.)
  + Assets (`docs/assets`, `.readme/`)
  + README (`README.md`)
  + .gitignore (technically, dunno why)
  + CHANGELOG.md (i guess maybe more accurate/clear info?)
  + LICENSE (why? this is better as an Issue or Discussion.)

> Did you know that you can contribute to Cerbose without writing code for it?  
> Starring the repository, mentioning it, and/or using the library count as contributing!
> Reporting issues is also a very helpful contribution.

## Table of Contents
> Do note that links may not reliably work on the website. You can try, they might!
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
  + Beginning to work on your contribution.
- [Requirements to Submit Code](#requirements-to-submit-code)
- [Standards](#standards)
  + Standards required in code (e.g., PEP 8)
- [Testing](#testing)
  + How to test your code.
- [Submitting Contributions](#submitting-contributions)
  + How to submit a contribution.
- [Writing a PR](#writing-a-pr)
  + How a PR (pull request) should be written.
- [Writing a Commit Message](#writing-a-commit-message)
- [Reporting Issues](#reporting-issues)
  + How to write an issue.
- [Contacting](#contacting)
  + How to contact maintainers (me).

## Code of Conduct
This isn't long...
1. No harrasment. None. Zilch. Nada. Cero.
2. No discrimination for any reason, whether that be upon the common list of reasons or a niche one.
3. Please keep discussions on-topic to Cerbose.
4. Don't hate on opinions.

While there isn't something clearly defined to "report", report any "violation" to GitHub or me (see [Contacting](#contacting)).

## Getting started
To contribute code to Cerbose:

1. Fork the repository (`Jasperredis/cerbose-lib`) on GitHub.
2. Clone your fork locally.
```bash
$ git clone https://github.com/YOUR_USERNAME/cerbose-lib.git
$ cd cerbose-lib
```
3. Make a venv inside of the repo locally.
```bash
$ python -m venv venv
$ source venv/bin/activate  # do "venv\Scripts\activate" if you use Windows
```

> Please ensure you have at least Python 3.7 installed. **Python 3.10/3.12 or later is preferred.**

## Requirements to Submit Code
- Ensure code is 100% authored by you.
- Ensure no functionality (unless harmful) is removed.

## Standards
- Conform to **PEP 8**.
- Please use Black to format your code before submitting:
```bash
$ black src/cerbose/*
```
- Name functions and variables with snake_case.

> Note: You can make a contribution to fix code that doesn't do this.

## Testing
There is no required method to run tests for Cerbose. You are free to use:

- The included `examples/test.py` on this repository (as long as its output reasonably demonstrates a working edit)
- A custom-written script to target what needs to be tested
- A Python testing framework (e.g., `pytest`, `unittest`, etc.)

What matters most is that:

- Your submission includes the results of your tests somewhere (e.g., pull request description, a file (if so, preferably `TESTS.md`)
- Your tests cover the code you changed, and, preferably, any related parts that may depend on it.
- If patching a bug, please reproduce the bug as a test.
- If adding a feature, please include tests that demonstrate that it works as intended.
- If changing a behaviour, please demonstrate the previous behaviour via test.


## Submitting Contributions

1. Make a branch in your local clone.
```bash
$ git checkout -b fix-or-feature/short-description
```
2. Ensure you have a GitHub Personal Access Token (PAT) configured if your Git client requires it for authentication.
3. Add changes and commit
```bash
$ git add .
$ git commit -m "Really cool commit message (i'll show you how to structure these later dw fella)"
$ git push origin the-same-branch/name-as-earlier  # origin should point to YOUR fork
```
4. Make a pull request on your new branch for the original repository.

### Writing a PR

**Title**:  
```plaintext
(Version of Cerbose) Short description of your changes (is it a feature? bugfix? what does it do?)
```
**Description**:   
```markdown
- List
- Of
- Your
- Changes

### TESTS: (Optional)
insert test results here
```

Example:

**Title**:  
```plaintext
(1.0.1) General patches and maintainability updates
```
**Description**:  
```markdown
- Fixed bug where using a non-existent file would output "[ERROR]: File '{content}' does not exist."
- Fixed bug where using a non-existent colour in textcol in cprint (or any function that relies on cprint) would supress the output and only print a warning.
- Renamed internal functions to be snake_case.
- Used black to format to PEP 8.  
(yes, this is real)

### Tests:  
none lawlz (this isn't real dw)
```

### Writing a Commit Message
What was your PR's title? That should be your commit message.


## Reporting Issues
In an issue report, you need:

1. The title should be clear, concise, and descriptive. No "Broken!"; that's how you get ignored! :) 
2. How to reproduce the bug.
3. A more detailed description of the problem.
4. OS details:
  + OS (Linux, Windows, macOS)
  + Version (for Windows/macOS, optionally kernel version for Linux)
  + Distribution (for Linux)
5. Python and Cerbose versions (e.g., Python 3.12, Cerbose 1.0.1)
6. Error messages, logs, etc. if available
7. Other relevant info (e.g., configs)

These can be included in any format, and in any structure, though here is this template:

**Title:**
```plaintext
Short description of the problem
```
**Description:**
```markdown
Detailed description of problem.

### Reproduce
How to reproduce the problem.

### Environment
- **OS:** Name (Version)  
- **Python:** X.Y.Z  
- **Cerbose:** 1.0.1

### Logs, Tracebacks, and Configs
info
```

## Contacting
The best place to contact maintainers (me, hehe) is GitHub.  
For general concerns and talk on Cerbose, always use GitHub Discussions on this repository.  
For bugs/issues, use Issues.  

For something private or a "violation" of code of conduct, email me personally at jasperredisispublic@gmail.com.
