import typing as tp

def generate_latex_table(data: list[list[tp.Any]]) -> str:
    res = "\\begin{tabular}{"
    res += '|' + '|'.join([' c ' for _ in range(len(data))]) + '|'
    res += "}\n"
    res += '\t\\hline\n'
    res += '\t\\hline\n'.join(map(lambda row: '\t' + ' & '.join(map(lambda el: str(el), row)) + ' \\\\\n', data))
    res += '\t\\hline\n'
    res += "\\end{tabular}"
    return res


def generate_latex_image(path: str) -> str:
    return f'\\includegraphics[]{{{path}}}'
