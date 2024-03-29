# Passeo
<div style="text-align: center; display: grid; justify-content: center;"><img style="margin: auto; margin-bottom: 1rem; border-radius: 30%;" height="150" width="150" src="https://raw.githubusercontent.com/ArjunSharda/Passeo/main/ext/passeo.jpg"/></div>

> 🔓 Generate a password with multiple options

# What is Passeo?

Passeo is a python password generator developed by [Arjun Sharda](https://github.com/ArjunSharda), under the [MIT License](https://github.com/ArjunSharda/Passeo/blob/main/LICENSE).

<br>
Passeo is used for checking your password through our strength check (includes Pwned, Length, and Case) and generate a password with multiple options.
</br>

# Why use Passeo?

Passeo is a upcoming password generator project, with massive plans in the future, such as generation of a password and strength checker via CLI/terminal. Passeo is also completely safe to use and is open source for the community to know how the codebase works and learn from how the password generator.


-----------------

Installation
------------
**[Python 3.7+](https://www.python.org/downloads/) is required**
```bash
# MacOS / Linux (via Terminal)
python3 -m pip install -U passeo

# Windows (via CMD Prompt)
py -3 -m pip install -U passeo
```

# Quickstart

```python
>>> from passeo import passeo
>>> print(passeo.generate(length=10, numbers=True, symbols=True, uppercase=True, lowercase=False, space=True, save=True))
```

Docker
------

Building the docker image
```sh
$ docker build -t passeo .
```

Running passeo on the docker container
```sh
$ docker run --rm -it passeo sh
/usr/src/passeo/examples # python generate.py
```

# v1.1.0 changes
----------------
- **[BREAKING]** Changed Passeo to a Enum, meaning that it will now be for generation for example `passeo.generate`, not `passeo().generate`.
- **[ADDED]** Added encrypting and decrypting. It has been supported by CLI.

# v1.1.3 changes
----------------
- **[FIXED]** Fixed CLI and normal issues with encrypting and decrypting (wrong function from Fernet was used)



<hr>
<h6 align="center">© Arjun Sharda 2022-present 
<br>
All Rights Reserved</h6>
