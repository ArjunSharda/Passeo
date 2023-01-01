# Passeo
<div style="text-align: center; display: grid; justify-content: center;"><img style="margin: auto; margin-bottom: 1rem; border-radius: 30%;" height="150" width="150" src="https://raw.githubusercontent.com/ArjunSharda/Passeo/main/ext/passeo.jpg"/></div>

"🔓 Generate a Password with multiple options"

# What is Passeo?

Passeo is a python password generator developed by [Arjun Sharda](https://github.com/ArjunSharda), under the [MIT License](https://github.com/ArjunSharda/Passeo/blob/main/LICENSE).

<br>
Passeo is used for checking your password through our strength check (includes Pwned, Length, and Case) and generate a password with multiple options.
</br>

# Why use Passeo?

Passeo is a upcoming password generator project, with massive plans in the future, such as generation of a password and strength checker via CLI/terminal. Passeo is also completely safe to use and is open source for the community to know how the codebase works and learn from how the password generator.


-----------------

# Quickstart

```python
from passeo import passeo
print(passeo().generate(10, numbers=True, symbols=True, save=True))
```

# v1.0.6 changes
- [SUPPORT] Added support for command line interface (CLI). Feature request can be found [here](https://github.com/ArjunSharda/Passeo/issues/2), and the CLI commands will be documented in the [examples](https://github.com/ArjunSharda/Passeo/tree/main/examples) page soon.
- [ADDED] New setup.py file to support the adjustments needed for CLI.


<hr>
<h6 align="center">© Arjun Sharda 2022-present 
<br>
All Rights Reserved</h6>
