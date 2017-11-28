""" Edit buffer for holding contents of a QScintilla session"""


class EditBuffer:

    """ EditBuffer class - a simple container"""

    def __init__(self, source=''):  # text='', dirty=False):
        self.text_buffer = source
        self.isdirty = False

    @property
    def text(self):
        return self.text_buffer

    @text.setter
    def text(self, txt):
        self.text_buffer = txt

    @property
    def dirty(self):
        return self.isdirty

    @dirty.setter
    def dirty(self, state):
        self.isdirty = state
