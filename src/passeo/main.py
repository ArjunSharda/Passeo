import click
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
def main(generate, length, numbers, symbols, uppercase, lowercase, space, save):
    try:

        if numbers == "y" or numbers == "Y" or numbers == "yes" or numbers == "Yes" or numbers == "YES" or numbers == "true" or numbers == "True" or numbers == "TRUE":
            numbers = True

        if symbols == "y" or symbols == "Y" or symbols == "yes" or symbols == "Yes" or symbols == "YES" or symbols == "true" or symbols == "True" or symbols == "TRUE":
            symbols = True

        if uppercase == "y" or uppercase == "Y" or uppercase == "yes" or uppercase == "Yes" or uppercase == "YES" or uppercase == "true" or uppercase == "True" or uppercase == "TRUE":
            uppercase = True

        if lowercase == "y" or lowercase == "Y" or lowercase == "yes" or lowercase == "Yes" or lowercase == "YES" or lowercase == "true" or lowercase == "True" or lowercase == "TRUE":
            lowercase = True

        if space == "y" or space == "Y" or space == "yes" or space == "Yes" or space == "YES" or space == "true" or space == "True" or space == "TRUE":
            space = True
        if save == "y" or save == "Y" or save == "yes" or save == "Yes" or save == "YES" or save == "true" or save == "True" or save == "TRUE":
            save = True

        elif numbers == "n" or numbers == "N" or numbers == "no" or numbers == "No" or numbers == "NO" or numbers == "false" or numbers == "False" or numbers == "FALSE":
            numbers = False

        elif symbols == "n" or symbols == "N" or symbols == "No" or symbols == "no" or symbols == "NO" or symbols == "false" or symbols == "False" or symbols == "FALSE":
            symbols = False

        elif uppercase == "n" or uppercase == "N" or uppercase == "No" or uppercase == "no" or uppercase == "NO" or uppercase == "false" or uppercase == "False" or uppercase == "FALSE":
            uppercase = False

        elif lowercase == "n" or lowercase == "N" or lowercase == "No" or lowercase == "no" or lowercase == "NO" or lowercase == "false" or lowercase == "False" or lowercase == "FALSE":
            lowercase = False

        elif space == "n" or space == "N" or space == "No" or space == "no" or space == "NO" or space == "false" or space == "False" or space == "FALSE":
            space = False

        elif save == "n" or save == "N" or save == "No" or save == "no" or save == "NO" or save == "false" or save == "False" or save == "FALSE":
            save = False


    finally:
        if click.confirm("Do you want to generate a password? Details: \n Length: " + str(length) + "\n Numbers: " + str(numbers) +"\n Symbols: " + str(symbols) + "\n Uppercase: " + str(uppercase) + "\n Lowercase: " + str(lowercase) + "\n Space: " + str(space) + "\n Save: " + str(save)):
            click.echo(passeo().generate(length, symbols, uppercase, lowercase, space, save))


if __name__ == "__main__":
    cli()
