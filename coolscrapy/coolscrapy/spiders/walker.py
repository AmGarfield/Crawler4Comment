
import scrapy
from coolscrapy.items import QuestionItem
from scrapy.selector import HtmlXPathSelector

class WalkerSpider(scrapy.Spider):
    name = "walker"
    question_id_counter =0
    # allowed_domains = ["xjh.haitou.cc"]
    # start_urls = ["http://xjh.haitou.cc/nj/uni-21"]
    allowed_domains = ["zhannei.baidu.com"]
    # start_urls = ["http://zhannei.baidu.com/cse/search?s=12455798804538985593&q=%D0%C5%D3%C3%C7%AE%B0%FC&partner=discuz"]

    start_urls = [
        "http://zhannei.baidu.com/cse/search?s=12455798804538985593&q=%D0%C5%D3%C3%C7%AE%B0%FC&partner=discuz",
        # xinyongqianbao
        "http://zhannei.baidu.com/cse/search?q=%E9%87%8F%E5%8C%96%E6%B4%BE&click=1&s=12455798804538985593&nsid=1",
        # lianghuapai
        "http://zhannei.baidu.com/cse/search?q=%E4%BF%A1%E7%94%A8%E9%92%B1%E5%8C%85%E7%99%BD%E6%9D%A1&click=1&s=12455798804538985593&nsid=1",
        # xinyongqianbaobaitiao
        "http://zhannei.baidu.com/cse/search?q=%E4%BF%A1%E7%94%A8%E9%92%B1%E5%8C%85%E5%A5%97%E7%8E%B0&click=1&s=12455798804538985593&nsid=1"
        # xinyongqianbaotaoxian
    ]


    def parse(self, response):
        item = QuestionItem()
        preachs = response.xpath('//div/div/div[@class="result f s3"]')
        for preach in preachs:
            # item['title']=preach.xpath('.//div[@class="text-success company"]/text()').extract()
            item['title'] =preach.xpath('h3/a/em/text()').extract() + preach.xpath('h3/a/text()').extract()
            item['link']=preach.xpath('h3/a/@href').extract()
            item['author'] = preach.xpath('div[@class="c-summary-1"]/span/text()')[1].extract()
            item['posttime'] = preach.xpath('div[@class="c-summary-1"]/span/text()')[2].extract()
            self.question_id_counter = self.question_id_counter + 1
            item['question_id'] = self.question_id_counter
            yield item

        # preachs=response.xpath('//table[@id="mainInfoTable"]/tbody/tr')
        # for preach in preachs:
        #     item['corp']=preach.xpath('.//div[@class="text-success company"]/text()').extract()
        #     item['date']=preach.xpath('.//span[@class="hold-ymd"]/text()').extract()
        #     item['location']=preach.xpath('.//td[@class="text-ellipsis"]/span/text()').extract()
        #     item['click']=preach.xpath('.//td[@class="text-right"]/text()').extract()
        #     yield item

        nextlink = response.xpath('//a[@class = "pager-next-foot n"]/@href').extract()
        # nextlink=response.xpath('//li[@class="next"]/a/@href').extract()

        if nextlink:
            yield scrapy.Request(response.urljoin(nextlink[0]),callback=self.parse )