import click
from collections import deque

def tail(file, num_lines=10):
    if file:
        with open(file, 'r') as f:
            lines = deque(f, maxlen=num_lines)
            for line in lines:
                print(line, end='')
    else:
        stdin = click.get_text_stream('stdin')
        lines = deque(stdin, maxlen=17)
        for line in lines:
            print(line, end='')

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(files):
    if not files:
        tail(None)
    else:
        for i, file in enumerate(files):
            if len(files) > 1:
                if i != 0:
                    print("")
                print(f"==> {file} <==")
            tail(file)

if __name__ == "__main__":
    main()
