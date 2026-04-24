import re

class FileNamer:
    @staticmethod
    def clean(name: str) -> str:
        name = re.sub(r'[^A-Za-z0-9]+', '-', name)
        return name.strip('-')

    @classmethod
    def build(cls, title: str) -> str:
        return f"{cls.clean(title)}.zip"
