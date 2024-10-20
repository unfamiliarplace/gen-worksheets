import random
import math
from functions.worksheet import Worksheet
from docx import Document
from docx.table import Table
from pathlib import Path

path_template = Path('functions/templates/binary.docx')
path_output = Path('output/binary')

# Dumb and potentially infinite... TODO
used_default = {
    'dec_to_bin': set(),
    'bin_to_dec': set(),
    'bits_to_states': set(),
    'states_to_bits': set(),
}

used = {}

def dec_to_bin(lower: int, upper: int) -> tuple[str]:
    n = random.randint(lower, upper)
    while n in used['dec_to_bin']:
        n = random.randint(lower, upper)
    used['dec_to_bin'].add(n)

    return str(n), str(bin(n))[2:]

def bin_to_dec(lower: int, upper: int) -> tuple[str]:
    answer, n = dec_to_bin(lower, upper)
    while n in used['bin_to_dec']:
        answer, n = dec_to_bin(lower, upper)
    used['bin_to_dec'].add(n)

    return n, answer

def bits_to_states(lower: int, upper: int) -> tuple[str]:
    n = random.randint(lower, upper)
    while n in used['bits_to_states']:
        n = random.randint(lower, upper)
    used['bits_to_states'].add(n)

    return str(n), str(math.ceil(math.log2(n)))

def states_to_bits(lower: int, upper: int) -> tuple[str]:
    bits = random.randint(lower, upper)
    while bits in used['states_to_bits']:
        bits = random.randint(lower, upper)
    used['states_to_bits'].add(bits)

    states = random.randint(((2 ** (bits - 1)) + 1), (2 ** bits) + 1)
    return str(states), str(bits)

def fill_table(t: Table, coords: tuple[int], func: callable, args: list=[], kwargs: dict={}) -> None:
    for coord in coords:
        Worksheet.fill_cell(t.cell(*coord), func(*args, **kwargs)[0])

class Binary(Worksheet):

    @staticmethod
    def reset() -> None:
        for k in used_default:
            used[k] = used_default[k].copy()

    @staticmethod
    def make(tag: str='', data: dict={}) -> None:

        d = Document(path_template)
        tables = d.tables
        coords = ((0, 0), (1, 0), (0, 2), (1, 2))

        fill_table(tables[0], coords, bin_to_dec, [0, 64])
        fill_table(tables[1], coords, dec_to_bin, [0, 64])
        fill_table(tables[2], coords, bits_to_states, [1, 9])
        fill_table(tables[3], coords, states_to_bits, [1, 9])
        
        Worksheet.replace(d, 'TAG', tag)
        return d

if __name__ == '__main__':
    Binary.test(path_output)
