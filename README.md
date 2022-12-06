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

# v1.0.5 changes
- [CRITICAL SECURITY PATCH] Fixed a critical security issue that is affecting currently everyone <1.0.5. It is highly recommended to update.
- [ADDED] Added a new quickgenerate function which can allow people to in bulk generate passwords that have letters and numbers. This will get more update as Passeo is developed to strengthen security of Passeo's users.


<hr>
<h6 align="center">© Arjun Sharda 2022 
<br>
All Rights Reserved</h6>
