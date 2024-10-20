import random
import docx
from worksheet import Worksheet
from docx.table import Table
from pathlib import Path

path_template = Path('templates/bingo_5x5.docx')
path_output = Path('output/bingo_questions')
path_test = path_output / 'test.docx'

PH_TAG = '__TAG__'
PH_INSTRUCTIONS = '__INSTRUCTIONS__'

# Dumb and potentially infinite... TODO
used = set()

def fill_table(t: Table, coords: tuple[int], func: callable, args: list=[], kwargs: dict={}) -> None:
    for coord in coords:
        cell = t.cell(*coord)
        cell.text = func(*args, **kwargs)[0]

class BingoQuestions(Worksheet):

    @staticmethod
    def parse_data() -> dict:
        d = {}


    @staticmethod
    def reset() -> None:
        used.clear()

    @staticmethod
    def make(tag: str='', data: dict={}) -> None:

        d = docx.Document(path_template)
        tables = d.tables
        coords = ((0, 0), (1, 0), (0, 2), (1, 2))

        fill_table(tables[0], coords, bin_to_dec, [0, 64])
        fill_table(tables[1], coords, dec_to_bin, [0, 64])
        fill_table(tables[2], coords, dec_to_power, [1, 8])
        fill_table(tables[3], coords, power_to_states, [1, 256])
        
        # tag it
        for p in d.paragraphs:
            if p.text.find(PH_TAG) >= 0:
                p.text = p.text.replace(PH_TAG, tag)

        return d

if __name__ == '__main__':
    BingoQuestions.test(path_output)
