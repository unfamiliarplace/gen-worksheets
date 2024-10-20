import random
import docx
from worksheet import Worksheet
from pathlib import Path

path_template = Path('functions/templates/bingo_5x5.docx')
path_data = Path('functions/data/bingo_questions.txt')
path_output = Path('output/bingo_questions')

INSTRUCTIONS = 'Find the right answer for each question! Write the '
TITLE = 'Bingo des Questions'

ROWS = 5
COLS = 5

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

        for (i, cell) in enumerate(table._cells):
            # Skip star
            if i == ((ROWS * COLS) // 2):
                continue

            Worksheet.fill_cell(cell, questions[i][1])
        
        # tag it
        Worksheet.replace(d, 'TAG', tag)
        Worksheet.replace(d, 'TITLE', TITLE)
        Worksheet.replace(d, 'INSTRUCTIONS', INSTRUCTIONS)

        return d

if __name__ == '__main__':
    BingoQuestions.test(path_output)
