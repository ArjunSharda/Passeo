# Generate

Generates a password, using the core of Passeo.

Supported: ✅

Usage example:

```bash
$ passeo generate 10 n y n y n n
```

`length`[int] - The length of the password. (Required argument)
`numbers`[bool] - Adds numbers to the password if y/true. (Required argument)
`symbols`[bool] - Adds symbols to the password if y/true. (Required argument)
`uppercase`[bool] - Adds uppercase to the password if y/true. (Required argument)
`lowercase`[bool] - Adds lowercase to the password if y/true. (Required argument)
`space`[bool] - Adds spacing to the password if y/true. (Required argument)
`save`[bool] - Saves the generated password to `passeo_passwords.txt` if y/true. (Required argument)




# Common Errors

Why is my code resulting in `"Uppercase and lowercase are both true, please make one of them false."`?
**Answer: If uppercase and lowercase are both true, this will result in a error. Please make for example lowercase false and uppercase true or uppercase false and lowercase true.**
