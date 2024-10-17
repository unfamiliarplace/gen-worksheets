import functions.binary as binary
from pathlib import Path

# TODO Do this dynamically...
FNS = {
    'binary': binary
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

    n = int(input('Enter number of worksheets to make: '))
    digits = len(str(n))
    path_output = Path(f'output/{fn_name}')
    path_output.mkdir(parents=True, exist_ok=True)

    for i in range(n):
        tag = str(i + 1).zfill(digits)
        d = fn.make()
        d.save(path_output / f'{fn_name} {tag}.docx')

    print(f'Created {n} files under {path_output}')

if __name__ == '__main__':
    run()
