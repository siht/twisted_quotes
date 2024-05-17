from twisted.internet import (
    endpoints,
    reactor,
)

from TwistedQuotes.quoteproto import QOTDFactory
from TwistedQuotes.quoters import (
    FortuneQuoter,
    StaticQuoter,
)


def main():
    quoterEndpoint = endpoints.serverFromString(reactor, 'tcp:1079')
    quoterEndpoint.listen(QOTDFactory(StaticQuoter(b'mujajajajajajaja')))
    quoterRandomEndpoint = endpoints.serverFromString(reactor, 'tcp:1080')
    quoterRandomEndpoint.listen(QOTDFactory(FortuneQuoter(['/etc/fortune'])))
    reactor.run()


if __name__ == '__main__':
    main()
