import os


class FileOperator:
    def __init__(self):
        self.fileDir = self.get_current_directory()
        self.filename = os.path.join(self.fileDir, 'db\\db.txt')

    @staticmethod
    def get_current_directory():
        return os.path.dirname(os.path.realpath('__file__'))

    def load_from_file(self):
        with open(self.filename, mode="r", encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
        return lines

    def save_to_file(self, lines):
        with open(self.filename, mode="w", encoding="utf-8") as f:
            f.writelines(lines)
