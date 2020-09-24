from enum import IntEnum, auto


class Operation(IntEnum):
    ADD_MEMBER = auto()
    SET_FATHER = auto()
    SET_MOTHER = auto()
    SET_SPOUSE = auto()
    SHOW_FAMILY_TREE = auto()
    SHOW_ALL_DATA = auto()
    LOAD_FROM_FILE = auto()
    SAVE_TO_FILE = auto()
    EXIT_PROGRAM = auto()
