# encoding = utf-8
import scrapy
from scrapy.http import Request
from coolscrapy.items import QuestionItem
from coolscrapy.items import NextPageItem

class woaika_spider(scrapy.Spider):
    name = "woaika"
    allowed_domains = ["woaika.com"]
    start_urls = [
        # "http://www.huxiu.com/index.php"
        "http://zhannei.baidu.com/cse/search?s=12455798804538985593&q=%D0%C5%D3%C3%C7%AE%B0%FC&partner=discuz"
        # "http://zhannei.baidu.com/cse/search?q=%E9%87%8F%E5%8C%96%E6%B4%BE&click=1&s=12455798804538985593&nsid=1"
        # "http://zhannei.baidu.com/cse/search?q=%E4%BF%A1%E7%94%A8%E9%92%B1%E5%8C%85%E7%99%BD%E6%9D%A1&click=1&s=12455798804538985593&nsid=1"
        # "http://zhannei.baidu.com/cse/search?q=%E4%BF%A1%E7%94%A8%E9%92%B1%E5%8C%85%E5%A5%97%E7%8E%B0&click=1&s=12455798804538985593&nsid=1"

    ]

    def parse(self, response):
        url = "http://zhannei.baidu.com/cse/"
        # print response
        for sel in response.xpath('//div/div/div[@class="result f s3"]'):
            # print sel
            item = QuestionItem()

            item['title'] = sel.xpath('h3/a/em/text()').extract() + sel.xpath('h3/a/text()').extract()
            item['link'] = sel.xpath('h3/a/@href').extract()
            item['author'] = sel.xpath('div[@class="c-summary-1"]/span/text()')[1].extract()
            item['posttime'] = sel.xpath('div[@class="c-summary-1"]/span/text()')[2].extract()
            # yield item

            # url = response.urljoin(item['link'])
            # item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract()
            # print(item['title'],item['link'])
            # for t in item['title']:
            #     print t.encode('gbk')
            # yield item

        # nextLink = response.xpath('//*[@class = "pager-next-foot n"]/@href')[0].extract()
        for sel in response.xpath('//*[@class = "pager-next-foot n"]'):
            item = NextPageItem()
            item['url']  = url + sel.xpath('./@href')[0].extract()
            # print text
            next_link_url = item['url']
            # print next_link_url
            yield item
        yield Request(response.urljoin(url + next_link_url), callback=self.parse)
            # yield item
        # print nextLink
        # yield nextLink
        # if nextLink:
        #     nextLinkUrl = nextLink[0]
        #     print nextLink
        #     yield Request(url+nextLinkUrl,callback = self.parse)


# if __name__ == 'main':
#     print 'woaikalalala'