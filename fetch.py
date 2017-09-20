from scraper.BaseScraper import BaseScraper
from util import write_all


def save_terms(url, selector, path, cookie=None):
    terms = BaseScraper(url, selector, cookie).fetch()
    write_all(path, terms)


save_terms('https://web.archive.org/web/20120919090519/http://500px.com/terms',
           '#terms > div.left-legal > div.section > div.left', 'data/500px.md')

save_terms('https://web.archive.org/web/20120831073421/http://windows.microsoft.com/en-us/windows-live/microsoft-services-agreement',
           'div.topic_body_full.contentPiece', 'data/microsoft_services.md')

save_terms('https://web.archive.org/web/20130724003432/http://instagram.com/about/legal/terms/',
           'section.nav-page-content', 'data/instagram.md')

save_terms('https://web.archive.org/web/20120815231316/https://signup.netflix.com/TermsOfUse',
           'article.tou.clearfix', 'data/netflix.md')

save_terms('https://web.archive.org/web/20120909061211/http://store.steampowered.com/subscriber_agreement/',
           '#ssa_body', 'data/steam.md')

save_terms('https://web.archive.org/web/20130505225004/https://www.amazon.com/gp/help/customer/display.html/ref=footer_privacy?ie=UTF8&nodeId=468496',
           'td.center-col > span.small', 'data/amazon_privacy_notice.md')

save_terms('https://web.archive.org/web/20120810143123/http://soundcloud.com/pages/privacy',
           '#main-wrapper-inner', 'data/soundcloud_privacy.md')

save_terms('https://web.archive.org/web/20130426005003/https://www.mint.com/how-it-works/security/policy/',
           '#content', 'data/mint_privacy_policy.md')
