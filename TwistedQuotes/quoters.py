from random import choice
from zope.interface import implementer
from . import quoteproto


@implementer(quoteproto.IQuoter)
class StaticQuoter:
    '''
    Return a static quote.
    '''
    def __init__(self, quote):
        self.quote = quote

    def getQuote(self):
        return self.quote


@implementer(quoteproto.IQuoter)
class FortuneQuoter:
    '''
    Load quotes from a fortune-format file.
    '''
    def __init__(self, filenames):
        self.filenames = filenames

    def getQuote(self):
        with open(choice(self.filenames), 'rb') as quoteFile:
            quotes = [i for i in quoteFile.read().split(b'\n') if i]
        return choice(quotes)
