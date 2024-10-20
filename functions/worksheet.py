from docx import Document
import docx2pdf
from pathlib import Path

class Worksheet:
    @staticmethod
    def parse_data() -> dict:
        return {}
    
    @staticmethod
    def reset() -> None:
        return
    
    @staticmethod
    def make(tag: str='', data: dict={}) -> Document:
        raise NotImplementedError

    @classmethod
    def test(cls: object, path_output: Path) -> None:        
        data = cls.parse_data()
        cls.reset()
        d = cls.make('test', data)
        path_output.mkdir(parents=True, exist_ok=True)
        d.save(path_output / '_test.docx')
        docx2pdf.convert(path_output / '_test.docx', path_output / '_test.pdf')
