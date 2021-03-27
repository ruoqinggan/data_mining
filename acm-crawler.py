import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'acm-spider'
    start_urls = ['https://dl.acm.org/people']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):
        # CARD_SELECTOR = '#pb-page-content > div > main > div.container > div > div > div.row.section.section--no-padding-top > div.col-lg-9.col-sm-8.sticko__side-content > div > ul > li:nth-child(n)'
        CARD_SELECTOR = '#pb-page-content > div > main > div.container > div > div > div.row.section.section--no-padding-top > div.col-lg-9.col-sm-8.sticko__side-content > div > ul > li:nth-child(2)'

        for person in response.css(CARD_SELECTOR):

            NAME_SELECTOR = './/div/div[3]/div[1]/text()'
            # PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            # MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            # IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': person.xpath(NAME_SELECTOR).extract_first(),
                # 'location':
                # 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                # 'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                # 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }


# //*[@id = "pb-page-content"]/div/main/div[1]/div/div/div[2]/div[2]/div/ul/li[1]/div/div[3]/div[1]
