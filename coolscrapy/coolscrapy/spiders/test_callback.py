import scrapy
from scrapy.selector import HtmlXPathSelector
from coolscrapy.items import QuestionItem
from coolscrapy.items import NextPageItem
from scrapy.http import Request

class test(scrapy.Spider):
    name = "test"
    start_urls = [
        "http://zhannei.baidu.com/cse/search?s=12455798804538985593&q=%D0%C5%D3%C3%C7%AE%B0%FC&partner=discuz",#xinyongqianbao
        "http://zhannei.baidu.com/cse/search?q=%E9%87%8F%E5%8C%96%E6%B4%BE&click=1&s=12455798804538985593&nsid=1",#lianghuapai
        "http://zhannei.baidu.com/cse/search?q=%E4%BF%A1%E7%94%A8%E9%92%B1%E5%8C%85%E7%99%BD%E6%9D%A1&click=1&s=12455798804538985593&nsid=1",#xinyongqianbaobaitiao
        "http://zhannei.baidu.com/cse/search?q=%E4%BF%A1%E7%94%A8%E9%92%B1%E5%8C%85%E5%A5%97%E7%8E%B0&click=1&s=12455798804538985593&nsid=1"#xinyongqianbaotaoxian
    ]


    def parse(self, response):
        url = "http://zhannei.baidu.com/cse/"
        # print response
        # for sel in response.xpath('//div/div/div[@class="result f s3"]'):
        #     # print sel
        #     item = QuestionItem()
        #
        #     item['title'] = sel.xpath('h3/a/em/text()').extract() + sel.xpath('h3/a/text()').extract()
        #     item['link'] = sel.xpath('h3/a/@href').extract()
        #     item['author'] = sel.xpath('div[@class="c-summary-1"]/span/text()')[1].extract()
        #     item['posttime'] = sel.xpath('div[@class="c-summary-1"]/span/text()')[2].extract()

        # nextLink = response.xpath('//*[@class = "pager-next-foot n"]')[0].extract()
        for sel in response.xpath('//*[@class = "pager-next-foot n"]'):
            item = NextPageItem()
            item['url']  = url + sel.xpath('./@href')[0].extract()
            # print text
            yield item

    # def parse(self, response):
    #     hxs = HtmlXPathSelector(response)
    #
    #     # sites = hxs.select("//li[contains(concat(' ', @class, ' '), ' mod-searchresult-entry ')]")
    #     # questions = hxs.select('//*[@id="results"]/div[2]/h3')
    #     questions = response.xpath('//div/div/div[@class="result f s3')
    #     # items = []
    #
    #     for site in questions[:2]:
    #         item = QuestionItem()
    #         item['title'] = site.select('h3/a/em/text()').select("string()")[0].extract()
    #         item['link_url'] = site.select('h3/a/@href').select("string()").extract()
    #         yield item
            # item['description'] = site.select('dl/dd/p').select("string()").extract()

            # if item['link_url']:
            #     request = Request("http://www.example.com/some_page.html", callback=self.parseItemDescription)
            #     request.meta['item'] = item
            #     return request

    # def parseItemDescription(self, response):
    #     item = response.meta['item']
    #     hxs = HtmlXPathSelector(response)
    #     sites = hxs.select("//li[contains(concat(' ', @class, ' '), ' mod-searchresult-entry ')]")
    #     item['description'] = "mytest"
    #     return item