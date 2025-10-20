# cerbar
`cerbar` is a function that returns a configurable ASCII progress bar.  
**NOTE**: This is NOT outputted to the console. It returns a string containing the bar.

## Basic Usage
In Cerbose, `cerbar` is defined as:
```python
def cerbar(length, total, fill, *, perc=None, count=None):
```
This means that `length`, `total`, and `fill` are required inputs and `perc` and `count` are optional keyword arguments.  
**Example**:  
```python
print(cerbose.cerbar(20, 70, 42))
```
Assuming default configurations, the output would look like this:  
```python
[############--------]
```

## Basic Usage: Arguments
The `length` input determines how many characters long the bar is (NOT COUNTING THE BORDERS! ([])). In the example, the first input--length--was set to 20, so the inside of the bar was 20 characters wide.  
The `total` and `fill` inputs determine what value the bar represents. Essentially, the bar represents the percentage of `fill` out of `total` (e.g., `cerbose.cerbar(20, 70, 42)` represents `42/70`).  
These are the basic options for `cerbar`.

## Perc & Count
These are optional keyword arguments.  
`perc` adds a percentage (e.g., `42/70` = `60.0%`) before or after the bar. It can be set to either `'l'` for the left of the bar, or `'r'` for the right of the bar.  
`count` can have the same inputs with the same results, however instead of outputting a percentage, it just outputs `fill`/`total` (e.g., with 42/70, it just adds 42/70 before/after the bar).  
If both are present on the same side, perc is always on the far left (whether that be farther from the bar in left or closer in right), and obviously the opposite for count.

## REMEMBER
cerbar does NOT output to the console. It RETURNS THE BAR IN A STRING. This is so that you can do:
```python
cprint("stat", f"YOU CAN PUT ANY TEXT BEFORE... {cerbose.cerbar(20, 70, 42)} OR AFTER THAT BAR! (also you can use cprint for tagging/logging)")
```

See configuration in 5-9.md.
