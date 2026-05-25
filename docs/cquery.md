# cquery
`cquery` (formerly `cin`), allows you to easily take user input through the console.

## Basic Usage
`cquery` is defined in Cerbose as:
```python
def cquery(tag, text, options, *, text_colour="normal", subtag=None, timestamp=False, log_file=None, lower=False, show_opts=False,
):
```
This means that `type`, `text`, and `options` are required inputs, and the rest are optional keyword arguments.  
You may notice that the keyword arguments and even some of the required inputs are suspiciously similar to those of `cprint`. This is because `cin` uses an `mprint` call to display its prompts.  
Here is an example call:
```python
res = cquery('ok', 'Hello,\nworld!', 'any')
print(res)
```
Output (again...assuming default configuration...)
```plaintext
[OK]: Hello,
    : world!:
> answer  # this answer is not automatic output, assume this is the answer the user typed in
answer  # this is the print(res) activating.
```
There are a lot of things you can observe from this.
**NOTE**: `cquery` returns the answer you get from it, and also makes this interactive prompt.  

The prompt ("Hello,\nworld!") uses the exact same keyword arguments as `cprint`. The `type` and `text` inputs are the same, however the `options` tag is unique.  
If you set `options` to a list (e.g., `['y', 'n', 'yes', 'no']`), the only answers allowed will be the items in that list and this output will appear if an option not in the list is given:  
![`[ERROR]: '(answer you inputted)' is not a valid option!`](assets/docs/f.png)  
Or, you can set the `options` input to `'*'` (string) and allow any input.  

## Keyword Arguments
Most keyword arguments in the `cquery` function are the same as those in `cprint`/`mprint`, however there are two other arguments: `lower` and `show_opts`:
- `lower` assumes all user input is in lowercase. Please do not make uppercase options if using this.
- `show_opts` shows all availible options (it won't do anything if `options` is set to `'any'`) in the prompt. Here is an example in a codeblock:  

```plaintext
[NONE]: Hello, world!
      : 1) a
      : 2) b
      : 3) c
      : 4) d
> 
```

## cyn
`cyn` is a simple function that wraps `cquery` with `y/n` options, `show_opts` off, and `lower` on.  
It is defined as:
```python
def cyn(tag, text, **kwargs):
```
