# locstats

![CI](https://github.com/kokkonisd/locstats/workflows/CI/badge.svg)
![codecov](https://codecov.io/gh/kokkonisd/locstats/branch/master/graph/badge.svg)

A Python tool that tells you approximately how many LOC (Lines Of Code) you
have written in a given language.

---

## what is locstats?

Wondering how many LOC (Lines Of Code) you have written in a given language?
Well, this is the tool for you! Given a programming language and a directory
list, `locstats` calculates the amount of LOC you have written in that
language.

## installing locstats

**Note: `locstats` is only compatible with Python 3.6 or newer.**

You can install `locstats` via `pip`:

```bash
$ pip3 install locstats # Only Python 3 is supported!
```

Or you can build it directly from its sources by cloning this repo:

```bash
$ git clone https://github.com/kokkonisd/locstats
$ cd locstats/
$ pip3 install .
```

Then you can run it to make sure that it's installed properly:

```text
$ locstats --help
Usage: locstats [OPTIONS] LANGUAGE [SRC_DIRS]...

  Counts the LOC in a given language in a given directory set.

Options:
  --strict        Run in strict mode (ignore comments and empty lines).
  -m, --minimal   Give minimal output (just the LOC count).
  --silent        Silence all warnings (such as directories not being found).
  -d, --detailed  Output a detaled list of LOC per file.
  --help          Show this message and exit.
```

If you have installed `locstats` with `pip` but it can't find the executable
when you run it, then you need to add Python to your `PATH` variable. You can
do that by adding the following line to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH=your-python-path-here/bin:$PATH
```

For example, on my computer (OSX) it's:

```bash
export PATH=/Users/kokkonisd/Library/Python/3.7/bin:$PATH
```

If you still can't get `locstats` to run, please create new
[issue](https://github.com/kokkonisd/locstats/issues) and we'll get to it ASAP.

## using locstats

Using locstats is pretty simple! Let's say I want to find out my LOC count in C
given all the C projects I have inside my `~/code/C/` folder:

```text
$ locstats c ~/code/C/
You have written approximately 39590 LOC in C, 27.26% of which are comments.
```

But wait! I try to document the code I write, so there's gonna be a lot of
lines of comments, which shouldn't count towards my actual _code_ line count.
I also try to format my code nicely, leaving blank lines where I have to to
make it more readable; those do not contribute to the code line count either.

Thankfully, I can just run `locstats` in strict mode:

```text
$ locstats c ~/code/C/ --strict
You have written approximately 28807 LOC in C.
```

Unsurprisingly, this returns fewer lines.

But what if I want to use the output of `locstats` in some other script? Well,
I can tell it to give me minimal output, which will only print the LOC count
(without the extra text):

```text
$ locstats c ~/code/C/ --minimal
39590
```

You can also get a detailed view of the LOC count per file using the `-d` or
`--detailed` flag:

```text
$ locstats python ~/code/locstats/ --detailed
FILENAME              LOC (%)
----------------------------------------
__main__.py         : 105 (32.71%)
loc.py              : 73 (22.74%)
test_loc.py         : 54 (16.82%)
definitions.py      : 47 (14.64%)
setup.py            : 28 (8.72%)
test_definitions.py : 12 (3.74%)
__init__.py         : 2 (0.62%)
----------------------------------------
TOTAL LOC           : 321 (100%)
```


## supported languages

Currenlty, we support the following languages:

- C
- C#
- C++
- CSS
- D
- Dart
- F#
- Fortran
- Go
- HTML
- Java
- JavaScript
- Julia
- LaTeX
- Markdown
- MATLAB
- MIPS assembly
- Objective-C
- Perl
- PHP
- Python
- R
- Ruby
- Rust
- Sass
- Swift
- TypeScript
- Verilog
- VHDL
- x86 assembly


## contributing

Do you want to contribute to an open source project? `locstats` needs your
help! I've just started working on this project and there are still tons of
things to add (mainly other programming languages in the `languages.json` 
file!).

So go ahead, fork this repo, write some code and make a pull request :)
