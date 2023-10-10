import click
from . import api, utils

@click.group()
def cli():
    pass

@cli.command()
def setup():
    api_key = input("Inserisci la tua chiave API di Bitbucket: ")
    utils.save_config({"api_key": api_key})

@cli.command()
@click.argument('repo')
def list_pipelines(repo):
    config = utils.load_config()
    if not config:
        print("Esegui prima il setup.")
        return

    pipelines = api.get_pipelines(config['api_key'], repo)
    for pipeline in pipelines['values']:
        print(pipeline['name'], "-", pipeline['state']['name'])

# Puoi aggiungere altri comandi qui...

if __name__ == "__main__":
    cli()
