# locstats

![build status](https://travis-ci.org/kokkonisd/locstats.svg?branch=master)

A Python tool that tells you approximately how many LOC (Lines Of Code) you
have written in a given language.

# what is locstats?

Wondering how many LOC (Lines Of Code) you have written in a given language?
Well, this is the tool for you! Given a programming language and a directory
list, `locstats` calculates the amount of LOC you have written in that
language.

# installing locstats

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

# using locstats

Using locstats is pretty simple! Let's say I want to find out my LOC count in C
given all the C projects I have inside my `~/code/C/` folder:

```bash
$ locstats c ~/code/C/
You have written approximately 39590 LOC in C.
```

But wait! I try to document the code I write, so there's gonna be a lot of
lines of comments, which shouldn't count towards my actual _code_ line count.
I also try to format my code nicely, leaving blank lines where I have to to
make it more readable; those do not contribute to the code line count either.

Thankfully, I can just run `locstats` in strict mode:

```bash
$ locstats c ~/code/C/ --strict
You have written approximately 28807 LOC in C.
```

Unsurprisingly, this returns fewer lines.

But what if I want to use the output of `locstats` in some other script? Well,
I can tell it to give me minimal output, which will only print the LOC count
(without the extra text):

```bash
$ locstats c ~/code/C/ --minimal
39590
```

# contributing

Do you want to contribute to an open source project? `locstats` needs your
help! I've just started working on this project and there are still tons of
things to add (mainly other programming languages in the `languages.json` 
file!).

So go ahead, fork this repo, write some code and make a pull request :)
