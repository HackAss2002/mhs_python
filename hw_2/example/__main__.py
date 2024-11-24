from latex_generator.latex import generate_latex_table, generate_latex_image

if __name__ == '__main__':
    with open('res.tex', 'wt') as f:
        print('\\documentclass{article}', file=f)
        print('\\usepackage{graphicx}', file=f)
        print('\\begin{document}', file=f)
        print(generate_latex_table([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), file=f)
        print(generate_latex_image('1.png'), file=f)
        print('\\end{document}', file=f)
