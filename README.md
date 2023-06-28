# Gitigno

Gitigno is a Python CLI tool that automatically generates .ignore templates using the [gitignore.io](https://gitignore.io) API. 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gitignore-generator.

```bash
pip install gitigno
```

## Usage

```python
# creating a .gitignore template
> python gitigno create -t "<template-name>"

# if you want to create for more than one template
> python gitigno create -t "<template-name>,<template-name>,..."


"""
 Here are examples for creating a .gitignore template for django & astro
"""
> python gitigno create -t "django,astro"
# or 
> python gitigno create --template "django,astro"
# or 
> python gitigno create # a prompt will ask you to enter template


""" 
Shows a table of available templates on gitignore.io.
Not all templates names are listed becasue the list is too long
"""
> python gitigno --tnames

# for help
> python gitigno --help


```

## Contributing

This is just a fun project for my portfolio which I may or may not continue to improve in the future.

I made it pip package for easy installation for anyone who wants to check it out.

## License

[MIT](https://choosealicense.com/licenses/mit/)