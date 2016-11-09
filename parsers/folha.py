import logging
from baseparser import BaseParser
from BeautifulSoup import BeautifulSoup, Tag

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class FOLHAParser(BaseParser):
    domain = 'folha.uol.com.br'
    domains = ['www1.%s' % domain]

    feeder_pat   = '^http://www1.%s/(\w+/)?[a-z0-9-]+/\d{4}/\d{2}/\d+[a-z0-9-]+\.shtml' % domain
    feeder_pages = [
        'http://www1.%s/' % domain,
    ]

    def _parse(self, html):
        soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES,
                             fromEncoding='utf-8')

        logger.debug('started parser')
        # logger.debug(html)

        self.title = soup.find('meta', attrs={'itemprop':'alternativeHeadline'}).get('content')
        logger.debug('title: %s' % self.title)

        byline = soup.find('div', attrs={'itemprop':'author'})

        if byline is None:
            self.byline = ''
        else:
            self.byline = byline.getText().strip().replace('\n',' ')

        logger.debug('byline: %s' % self.byline)

        self.date = soup.find('time', attrs={'class': None}).get('datetime')
        logger.debug('date: %s' % self.date)

        div = soup.find('div', attrs={'itemprop': 'articleBody'})

        if div is None:
            self.real_article = False
            return

        self.body = '\n' + '\n\n'.join([x.getText().strip() for x in div.contents if isinstance(x, Tag) and x.name == 'p'])
        logger.debug('body: %s' % self.body)
