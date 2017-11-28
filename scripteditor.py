from PyQt5.Qsci import QsciScintilla


class ScriptEditor(QsciScintilla):

    path = None

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.load_file()

    def copy(self):
        self.SendScintilla(self.SCI_COPY)

    def paste(self):
        self.SendScintilla(self.SCI_PASTE)

    def load_file(self):
        try:
            src = open(self.path, 'r')
            source = src.read()
            src.close()
            self.setText(source)
        except:
            return None
