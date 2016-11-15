import logging
from baseparser import BaseParser

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class FOLHAParser(BaseParser):
    domain = 'www1.folha.uol.com.br'
    domains = [domain]

    feeder_pat   = '^http://%s/(\w+/)?[a-z0-9-]+/\d{4}/\d{2}/\d+[a-z0-9-]+\.shtml' % domain
    feeder_pages = [
        'http://%s/' % domain,
    ]

    def _parse(self, html):
        soup = self.feeder_bs(html, 'html5lib')

        logger.debug('started parser')
        # logger.debug(html)

        title = soup.find('meta', attrs={'itemprop':'alternativeHeadline'})
        if title is None:
            self.real_article = False
            return

        self.title = title.get('content')
        logger.debug('title: %s' % self.title)

        date = soup.find('time', attrs={'class': None})
        if title is None:
            self.real_article = False
            return

        self.date = date.get('datetime')
        logger.debug('date: %s' % self.date)

        byline = soup.find('div', attrs={'itemprop':'author'})
        if byline is None:
            self.byline = ''
        else:
            self.byline = byline.getText().strip().replace('\n',' ')

        logger.debug('byline: %s' % self.byline)

        div = soup.find('div', attrs={'itemprop': 'articleBody'})

        if div is None:
            self.real_article = False
            return

        self.body = '\n' + '\n\n'.join([x.getText().strip() for x in div.contents if x.name == 'p'])
        logger.debug('body: %s' % self.body)
