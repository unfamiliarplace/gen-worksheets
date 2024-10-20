import random
import docx
from functions.worksheet import Worksheet
from docx.table import Table
from pathlib import Path

path_template = Path('functions/templates/bingo_5x5.docx')
path_data = Path('functions/data/bingo_questions.txt')
path_output = Path('output/bingo_questions')

INSTRUCTIONS = 'Find the right answer for each question! Write the '
TITLE = 'Bingo des Questions'

used = set()

class BingoQuestions(Worksheet):

    @staticmethod
    def parse_data() -> dict:
        d = {
            'questions': []
        }

        with open(path_data, 'r', encoding='utf-8') as f:
            for line in filter(None, (line.strip() for line in f.readlines())):
                n, q, a = line.split('::')
                d['questions'].append((n, q, a))

        return d

    @staticmethod
    def reset() -> None:
        used.clear()

    @staticmethod
    def make(tag: str='', data: dict={}) -> None:
        questions = data['questions'][:]
        random.shuffle(questions)

        d = docx.Document(path_template)
        table = d.tables[0]

        for cell in table._cells:
            print(cell)

        # coords = ((0, 0), (1, 0), (0, 2), (1, 2))

        # fill_table(tables[0], coords, bin_to_dec, [0, 64])
        # fill_table(tables[1], coords, dec_to_bin, [0, 64])
        # fill_table(tables[2], coords, dec_to_power, [1, 8])
        # fill_table(tables[3], coords, power_to_states, [1, 256])
        
        # tag it
        Worksheet.replace(d, 'TAG', tag)
        Worksheet.replace(d, 'TITLE', TITLE)
        Worksheet.replace(d, 'INSTRUCTIONS', INSTRUCTIONS)

        return d

if __name__ == '__main__':
    BingoQuestions.test(path_output)
