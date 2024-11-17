import click

def count(storage):
    lines, words, bytes_ = 0, 0, 0
    for line in storage:
        lines += 1
        words += len(line.split())
        bytes_ += len(line.encode())
    return (lines, words, bytes_)


def wc(file):
    if file:
        with open(file, 'r') as f:
            return count(f)
    else:
        stdin = click.get_text_stream('stdin')
        return count(stdin)

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(files):
    if not files:
        lines, words, bytes_ = wc(None)
        print(f"{lines:7} {words:7} {bytes_:7}")
    else:
        total_lines, total_words, total_bytes = 0, 0, 0
        results = []
        for file in files:
            lines, words, bytes_ = wc(file)
            results.append((lines, words, bytes_, file))
            total_lines += lines
            total_words += words
            total_bytes += bytes_
        if len(files) > 1:
            results.append((total_lines, total_words, total_bytes, "total"))
        max_bytes_width = len(str(results[-1][2]))
        for r in results:
            print(f"{r[0]:{max_bytes_width}} {r[1]:{max_bytes_width}} {r[2]:{max_bytes_width}} {r[3]}")

if __name__ == "__main__":
    main()
