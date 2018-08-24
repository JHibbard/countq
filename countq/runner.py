# Standard Libraries
import pathlib
import datetime

# External Libraries
import click
import pandas as pd


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'],
                        max_content_width=80)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
@click.pass_context
def cli(ctx):
    pass


@cli.command('count')
@click.option('--sequence', '-s', required=True,
              help='sequence to search for in fastq files')
@click.option('--output', '-o',
              help='output counts to excel file')
@click.argument('files', nargs=-1, type=click.Path())
@click.pass_context
def count(ctx, sequence, output, files):
    """Count instances of 'sequence' in a list of files"""
    results = {'filename': [], 'reads': [], 'seq': []}
    files = [f for f in files if pathlib.Path(f).is_file()]
    for filename in files:
        line_count = 0
        sequence_count = 0
        with open(filename, 'r') as file:
            for line in file:
                if sequence in line:
                    sequence_count += 1
                line_count += 1

        read_count = line_count / 4
        results['filename'].append(pathlib.Path(filename).name)
        results['reads'].append(read_count)
        results['seq'].append(sequence_count)

    df = pd.DataFrame(data=results)
    df.index.name = sequence
    if output:
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        df.to_excel(f'./{date}_{output}.xlsx')
    else:
        click.echo(df)
