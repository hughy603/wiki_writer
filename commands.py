#!/usr/bin/env python
import click


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('--terms/--no-terms', default=False)
@click.pass_context
def cli(ctx, debug, terms):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    click.echo('Terms mode is %s' % ('on' if terms else 'off'))


@cli.command()
@click.option('--columns/--no-columns', default=False)
@click.pass_context
def load_wiki(ctx, columns):
    click.echo('Loading Wiki')


@cli.command()
@click.pass_context
def load_stage(ctx):
    click.echo('Loading Stage')


if __name__ == "__main__":
    cli()
