# tool-research
The journey to find a tool for running common project commands

### Introduction

Actions such as linting, formatting, testing, possibly some cleanup, and package building, will be probably run very frequently by project template users. We should provide a standardized way to do this, or at least a centralized spot to collect these command chains.

One alternative is using a Makefile, but that has some perils (like each line running in a separate shell). (stolen from an issue text).

Lets investigate some alternative tools to make, and answer the following questions:

1. Does it require a software install? How easy is it to install?
2. How easy is it to use once configured?
3. How easy is it to write tasks? Our tasks are usually just a couple commands one after the other, we don't usually need looping and more complex constructs.
4. Does state carry over lines? For example, Makefile is known to run each line in a new shell, so state doesn't carry over.
5. How can the user pass arguments to each task?

### Task:

1. easy installable through:
```console
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
```

2. simple enough to use and cool to maintain considering its all yaml files.

3. Very easy, just add the tasks at the yaml file one line after the other, or join everything with ; or && in one big line of fun 

4. By defautl state does not carry over lines, but its possible to create multiple lines shells

5. 
```console
  format:
    desc: "Format code using Black"
    cmds:
      - black "{{.FOLDER}}"
```

![alt text](assets/image_task.png)

For documentation this is the best in my opinion

### Just: 

1. very easy installable by package managers or also a shell. Cool name "just" lol, "just run", "just build".

2. simple enough to use and cool to maintain, doesn't use yaml, uses a more simple approach. Reminds me of Make.

3. Also easy to use, just add the lines one after the other.

4. By default, state does not carry over lines. Like Make, it runs each recipe line in a new shell process. If you have two lines in a recipe, they don’t share state. can if using "\" or "&&" etc

5.
```console
format folder="src":
  black {{folder}}
  echo "IT WORKED !!!!!!"
```
![alt text](assets/image_just.png)

### Do it

1. easy to install via pip, not so much for os package systems

2. LoL I think this overcomplicates things a bit 
Even though I love python, I don't think we need more code to maintain / test / run
This also creates some .doit files, that bring some extra bloat to the project folder"

3. doesn't print output by default, easy to write tasks, easy to write multiople lined tasks. yet the more flexible in my opinion, since i am very used to python code. Doesn't let you create tasks named "run"

4. By default no, but you can do some tricks, since its python code.

5. 

```console
def task_format(folder="src"):
  """Format code using Black"""
  return {
    "actions": [
        f'black {folder}',
        'echo IT WORKED !!!!!!'
    ],
    'verbosity': 2,
  }
```

  ![alt text](assets/image_doit.png)

  ### mise

  1. easy to install via shell command, apparently it doesn't have package manager way of doing it

  2. uses a .toml file to keep the conf in, very easy to use

  3. Easy to use, just add the lines one after the other.

  4. Not by default, but possible to use env vars for that

  5. 
```console
[vars]
folder = 'src'
...
[tasks.format]
description = ""Format code using Black""
run = [
    'black {{arg(name=""folder"", default=""src"")}}',
    'echo it works !!!'
]
```

![alt text](assets/image_mise.png)