import click

def nl(file):
    if file:
        with open(file, 'r') as f:
            for i, line in enumerate(f, start=1):
                print(f"{i:6}  {line}", end='')
    else:
        stdin = click.get_text_stream('stdin')
        for i, line in enumerate(stdin, start=1):
            print(f"{i:6}  {line}", end='')

@click.command()
@click.argument('file', required=False, type=click.Path(exists=True))
def main(file):
    nl(file)

if __name__ == "__main__":
    main()
