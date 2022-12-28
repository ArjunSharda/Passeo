import click
import secrets
import string
from passeo import passeo

@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-g",
    "--generate",
    is_flag=True,
    help="Generate a password.",

)
@click.argument("length", type=int)
@click.argument("numbers", type=bool)
@click.argument("symbols", type=bool)
@click.argument("uppercase", type=bool)
@click.argument("lowercase", type=bool)
@click.argument("space", type=bool)
@click.argument("save", type=bool)
def generate(generate, length, numbers, symbols, uppercase, lowercase, space, save):
    try:
        password = ''

        if numbers is True:
            password += secrets.choice(string.digits)

        if symbols is True:
            password += secrets.choice(string.punctuation)


        if uppercase is True:
            password += secrets.choice(string.ascii_uppercase)

        if lowercase is True:
            password += secrets.choice(string.ascii_lowercase)

        if space is True:
            password += password.join (' ')

        if save is True:
            with open("passeo_passwords.txt", "a") as f:
                f.write(password + "\n")

        elif numbers is False:
            pass

        elif symbols is False:
            pass

        elif uppercase is False:
            pass

        elif lowercase is False:
           pass

        elif space is False:
            pass

        elif save is False:
            pass


        if click.confirm("Do you want to generate a password? Details: \n Length: " + str(length) + "\n Numbers: " + str(numbers) +"\n Symbols: " + str(symbols) + "\n Uppercase: " + str(uppercase) + "\n Lowercase: " + str(lowercase) + "\n Space: " + str(space) + "\n Save: " + str(save)):
            FinalPassword = ''.join(secrets.choice(password) for i in range(length))
            click.echo(FinalPassword)

    except Exception:
            click.echo(Exception)


@cli.command()
@click.option(
    "-s",
    "--strengthcheck",
    is_flag=True,
    help="Check the strength of a password.",
)
@click.argument("password", type=str)
def strengthcheck(strengthcheck, password):
    try:
        if click.confirm("Do you want to check the strength of a password?"):
            click.echo(passeo().strengthcheck(password))
    except Exception:
        click.echo(Exception)




if __name__ == "__main__":
    cli()
