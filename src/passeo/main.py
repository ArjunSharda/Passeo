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
def generate(generate, length, numbers, symbols, uppercase, lowercase, space, save):
    try:

        if click.confirm("Do you want to generate a password? Details: \n Length: " + str(length) + "\n Numbers: " + str(numbers) +"\n Symbols: " + str(symbols) + "\n Uppercase: " + str(uppercase) + "\n Lowercase: " + str(lowercase) + "\n Space: " + str(space) + "\n Save: " + str(save)):
            FinalPassword = ''.join(passeo().generate(length=length, numbers=numbers, symbols=symbols, uppercase=uppercase, lowercase=lowercase, space=space, save=save))
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

@cli.command()
@click.option(
    "-qg",
    "--quickgenerate",
    "--qg",
    "--quickgen",
    "--qgen",
    "--quick",
    "-quickgen",
    is_flag=True,
    help="Generate a password.",
)
@click.argument("length", type=int)
@click.argument("save", type=bool)
@click.argument("bulk", type=int)
def quickgenerate(quickgenerate, length, save, bulk):
    password = passeo().quickgenerate(length, save, bulk)
    click.confirm("Do you want to quickgenerate a password? Details: \n Length: " + str(length) + "\n Save: " + str(save) + "\n Bulk: " + str(bulk))
    if save is True:
        with open("passeo_quickgen_passwords.txt", "a") as f:
            f.write(password + "\n")

    if bulk > 1:
         with open("passeo_quickgen_bulk_passwords.txt", "a") as f:
            for i in range(bulk):
                 bulk_password = passeo().quickgenerate(length, save, bulk)
                 f.write(bulk_password + "\n")
                 click.echo(bulk_password)

    click.echo(password)




if __name__ == "__main__":
    cli()
