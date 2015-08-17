class Translator():
    real_translator = staticmethod(lambda message, *args, **kwargs: message)

    def __call__(self, *args, **kwargs):
        return self.real_translator(*args, **kwargs)

    def register_translator(self, new_translator):
        self.real_translator = new_translator

_ = Translator()
register_translator = _.register_translator
