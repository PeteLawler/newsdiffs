import logging
from baseparser import BaseParser

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class G1Parser(BaseParser):
    domain = 'g1.globo.com'
    domains = [domain]

    feeder_pat   = '^http://%s/[a-z0-9/-]+/\d{4}/\d{2}/[a-z0-9-]+\.html' % domain
    feeder_pages = [
        'http://%s/' % domain,
    ]

    def _parse(self, html):
        soup = self.feeder_bs(html, 'html5lib')

        logger.debug('started parser of: %s' % self.url)

        title = soup.find('h1', attrs={'class':'entry-title'})

        if title is None:
            self.real_article = False
            return

        self.title = title.getText()
        logger.debug('title: %s' % self.title)

        byline = soup.find('p', attrs={'class':'vcard author'})

        if byline is None:
            self.byline = ''
        else:
            self.byline = ' '.join([c.getText() for c in list(byline.children)])

        logger.debug('byline: %s' % self.byline)

        self.date = soup.find('abbr', attrs={'class': 'published'}).getText()
        logger.debug('date: %s' % self.date)

        div = soup.find(id='materia-letra')
        logger.debug('div: %s' % div.string)

        if div is None:
            self.real_article = False
            return

        paragraphs = div.findAll('p')

        self.body = '\n' + '\n\n'.join([p.getText().strip() for p in paragraphs])
        # logger.debug('body: %s' % self.body)
