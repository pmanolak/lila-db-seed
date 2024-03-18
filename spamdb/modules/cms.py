from modules.env import env
import modules.util as util

default_pages = [
    ['About', 'about'],
    ['Terms of Service', 'tos'],
    ['Privacy', 'privacy'],
    ['Title Verification', 'master'],
    ['Source Code', 'source'],
    ['Contribute', 'help'],
    ['Changelog', 'changelog'],
    ['Thank you!', 'thanks'],
    ['Ads', 'ads'],
    ['Chess Calendar', 'broadcast-calendar', '/broadcast/calendar'],
    ['About broadcasts', 'broadcasts', '/broadcast/help'],
    ['Puzzle Racer', 'racer'],
    ['Puzzle Storm', 'storm'],
    ['Studies: Staff Picks', 'studies-staff-picks'],
]


def update_cms_colls() -> None:
    args = env.args
    db = env.db

    if args.drop:
        db.cms_page.drop()

    pages: list[CmsPage] = []

    for page in default_pages:
        pages.append(CmsPage(page))

    if args.no_create:
        return

    util.bulk_write(db.cms_page, pages)


class CmsPage:
    def __init__(self, page: list):
        self._id = env.next_id(CmsPage)
        self.key = page[1]
        self.title = page[0]
        self.markdown = env.random_paragraph()
        self.language = 'en'
        self.live = True
        self.by = 'admin'
        self.at = util.time_since_days_ago(30)

        if len(page) > 2:
            self.canonicalPath = page[2]
