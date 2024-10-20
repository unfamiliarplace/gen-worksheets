
from pathlib import Path
import docx2pdf

from functions.worksheet import Worksheet
from functions.binary import Binary
from functions.bingo_questions import BingoQuestions

# TODO Do this dynamically...
FNS: dict[str, Worksheet] = {
    'binary': Binary,
    'bingo (questions)': BingoQuestions
}

def choose() -> str:
    choices = list(FNS)
    choice_str = 'Choose one of the following worksheet functions:\n\n'
    for (i, choice) in enumerate(choices):
        choice_str += f'{i + 1:>2} : {choice}\n'
    choice_str += '\nChoice: '

    i = int(input(choice_str)) - 1
    fn_name = choices[i]
    return fn_name

def run() -> None:
    fn_name = choose()
    fn = FNS[fn_name]
    data = fn.parse_data()

    n = int(input('Enter number of worksheets to make: '))
    digits = len(str(n))
    path_output = Path(f'output/{fn_name}')
    path_output.mkdir(parents=True, exist_ok=True)

    for i in range(n):
        tag = str(i + 1).zfill(digits)
        path_outfile = path_output / f'{fn_name} {tag}.docx'

        fn.reset()
        d = fn.make(tag, data)

        d.save(path_outfile)
        docx2pdf.convert(path_outfile, path_output / f'{fn_name} {tag}.pdf')

    print(f'Created {n} files under {path_output}')

if __name__ == '__main__':
    run()
