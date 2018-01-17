import requests
import logging
from config import DATA
from utils import make_dir
from html_content import body, panel, row


class Parser(object):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                 'AppleWebKit/537.36(KHTML, like Gecko) ' \
                 'Chrome/63.0.3239.132 Safari/537.36'

    def __init__(self):
        make_dir(DATA['dir_name'])
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def fetch_request(self, url):
        # Returns json-data from item
        return requests.get(
            url=url, headers={'User-agent': self.user_agent}
        ).json()

    def get_category_ids(self, category):
        # Returns list of ids by category
        return set(self.fetch_request(url=DATA['ids_url'].format(category)))

    def get_item_details(self, item_id):
        # Returns details about item
        return self.fetch_request(url=DATA['item_url'].format(item_id))


if __name__ == '__main__':
    # make 3 parts (rows, panels and body) of web-page and save items in it
    rows = ''
    panels = ''
    panel_number = 1
    id_number = 1
    r_number = 0
    parser = Parser()
    for category in DATA['categories']:
        category_ids = parser.get_category_ids(category)
        for item in category_ids:
            item_detail = parser.get_item_details(item)
            title = item_detail['title']
            rows += row.format(row_text=title, collapse=id_number) + '\n'
            id_number += 1
            r_number += 1
            if r_number == 5:     # if you want to parse all items - delete this lines
                break
            # print(r_number)
        r_number = 0
        panels += panel.format(category_name=category, rows=rows, collapse=panel_number) + '\n'
        panel_number += 1
        rows = ''
    # make web-page and write in html-doc
    html = body.format(body=panels)

    with open('results/index.html', 'w', encoding='windows-1251') as doc:
        doc.write(html)
