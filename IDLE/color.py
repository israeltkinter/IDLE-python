from PyQt5.QtWidgets import QTextEdit

class PythonWords:
    def __init__(self, textEdit: QTextEdit):
        if isinstance(textEdit, QTextEdit):
            self.textEdit = textEdit
        else:
            raise ValueError(f"The value that you entered {textEdit} is not a QtextEdit")

    def words(self) -> None:
        words_of_orange = ["if", "elif", "break", "while", "for", "continue", "def", "class",
                           "import", "from", "lambda", "True", "False", "as", "try", "except",
                           "with", "else", "and", "or", "return", "pass", "is", "raise", "assert",
                           "async", "yield", "del", "in", "not", "None", "finally"
                           ]

        words_of_purple = ["print", "property", "classmethod", "staticmethod", "str", "super",
                           "int", "list", "set", "isinstance", "issubclass", "round", "repr",
                           "range", "globals", "getattr", "copyright", "help", "credits", "license",
                           "filter", "map", "float", "frozenset", "hasattr", "all", "abs", "aiter",
                           "anext", "any", "ascii", "format", "eval", "breakpoint", "bytearray",
                           "bytes", "bin", "bool", "callable", "delattr", "enumerate", "hash", "max",
                           "min", "locals", "setattr", "vars", "object", "compile", "chr", "ord",
                           "complex", "exec", "dict","oct", "slice", "dir", "divmod", "sorted", "id",
                           "reversed", "exit", "ellipsis", "type", "tuple", "open", "len", "hex",
                           "iter", "memoryview", "next", "input", "quit", "zip", "sum", "pow", "NotImplemented"]

        errors_of_purple = ["NameError", "NotImplementedError", "TypeError", "NotADirectoryError",
                            "FileNotFoundError", "ModuleNotFoundError", "Exception", "BaseException",
                            "StopIteration", "UnicodeDecodeError", "PermissionError", "AssertionError",
                            "BaseExceptionGroup", "BlockingIOError", "BrokenPipeError", "BytesWarning",
                            "ConnectionAbortedError", "ConnectionError","ConnectionRefusedError", "ConnectionResetError",
                            "DeprecationWarning",
                            "EncodingWarning", "EnvironmentError", "ExceptionGroup", "FloatingPointError",
                            "FutureWarning", "GeneratorExit", "ImportWarning", "IndentationError",
                            "IndexError", "InterruptedError", "KeyboardInterrupt", "PendingDeprecationWarning",
                            "RecursionError", "ReferenceError", "ResourceWarning", "RuntimeError",
                            "RuntimeWarning", "StopAsyncIteration", "SyntaxError", "SyntaxWarning",
                            "UnboundLocalError", "UnicodeEncodeError", "UnicodeError", "UnicodeTranslateError",
                            "UnicodeWarning", "UserWarning", "Warning", "WindowsError", " ZeroDivisionError",
                            "AttributeError", "ArithmeticError", "IsADirectoryError", "TabError", "ValueError",
                            "BufferError", "ChildProcessError", "EOFError", "OSError", "IOError", "ImportError"]
        self._check_duplicates(words_of_orange, words_of_purple, errors_of_purple)


    def _check_duplicates(self, words_of_orange: list, words_of_purple: list, errors_of_purple: list) -> None:
        for word in words_of_orange:
            count = words_of_orange.count(word)
            print(count if count == 1 else "duplicates in words of orange")
        print("stoping check duplicates in words of orange")
        for word2 in words_of_purple:
            count2 = words_of_purple.count(word2)
            print(count2 if count2 == 1 else "duplicates in words of purple")
        print("stoping check duplicates in words of purple")
        for word3 in errors_of_purple:
            count3 = errors_of_purple.count(word3)
            print(count3 if count3 == 1 else "duplicates in errors of purple")
        print("stoping check duplicates in errors of purple")


    def set_color(self, w_orange: list, w_purple: list, e_purple: list) -> None:
        # איך משנים צבע של מילה בודדת ב QtextEdit ב PyQt5
        # ניסיתי המון פתרונות ולא הצלחתי לשנות צבע של מילה בודדת
        pass







