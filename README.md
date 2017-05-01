# `todo` - A smarter way to organise your to-do lists

##  Introduction
`todo` is a tool that allows you to easily manage your to-do lists. At the current stage `todo` doesn't do much, but new features are added weekly. The goal is to provide a web interface where the user could create, edit and remove tasks. Differently from other tools, tasks can move from one state to the other based on recency rules. For instance, assuming you organised your board with a Backlog, Master, High Impact Tasks (HIT) and Done states. You could create a rule to move all tasks from Backlog to Master when the deadline associated with a task is due in 7 days.

`todo` aims to simplify the maintainance of your to-do lists, encapsulating the logic behind moving a task from a state to the other, based on the proximity to the deadline.

## Installation
To use the service you should simply build the project and then run it with the following two commands:

```
$ make build
$ make run
```

## Getting started
To collaborate on the project you could just send a Pull Request in GitHub, describing the bug you're closing or the feature you're adding. Before opening a Pull Request, please make sure all the automated tests pass, running the following command from your terminal:

```
$ make test
```

## Motivation
`todo` is a learning project I wanted to start to familiarise with some popular tools to build Python services (`Docker`, `PostgreSQL`, `SQLAlchemy`, `alembic`, etc...). The project is not (yet) meant to be used by anyone else but the author. The choice of publishing it in GitHub was based on the fact that I'm a strong advocate for open-source software. If I could help even a single use to solve one bug in his application looking at some of the stuff I did here, I've reached my goal!
