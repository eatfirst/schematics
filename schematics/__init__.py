# -*- coding: utf-8 -*-

version_info = ('1', '1', '0')

__version__ = '{0}.{1}.{2}'.format(*version_info)

class Translator():
    real_translator = staticmethod(lambda message, *args, **kwargs: message)

    def __call__(self, *args, **kwargs):
        trans = self.real_translator(*args, **kwargs)
        print(trans)
        return trans

    def register_translator(self, new_translator):
        self.real_translator = new_translator

_ = Translator()
register_translator = _.register_translator
