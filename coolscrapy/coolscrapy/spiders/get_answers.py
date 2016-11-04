
import scrapy
import datetime
from coolscrapy.items import AnswerItem
import json

# get questions (all)
url_list = []
with open("D://Users//Administrator//PycharmProjects//coolscrapy//allQuestions.json", "r") as f:
    data = json.load(f)
    for item in data:
        # url_list.append(item['link'][0])
        string = item['link'][0]
        url_list.append(string)

class WalkerSpider(scrapy.Spider):
    name = "answer_walker"
    answer_id_counter = 0
    allowed_domains = ["bbs.51credit.com"]

    # start_urls = [
    #     "http://bbs.51credit.com/thread-2497175-1-1.html"
    # ]
    start_urls = url_list

    url = "http://bbs.51credit.com/"

    def parse(self, response):
        item = AnswerItem()
        question = response.xpath('//span[@id="thread_subject"]/text()')[0].extract()
        # preachs = response.xpath('//div[@id="postlist"]/div')
        preachs = response.xpath('//table[@class="plhin"]')

        for preach in preachs:
            item['question'] = question
            item['author'] = preach.xpath('*/*/div[@class="pls favatar"]/div[1]/div/a/text()').extract()
            item['post_time'] = preach.xpath('*/*/*/*/div[@class="authi"]/em/text()').extract()

            # content_container = preach.xpath('//div[@class="t_fsz"]/table/tbody/tr/td[@class="t_f"]/text()').extract()
            content_container = preach.xpath('*/*/*/*/*/*/tr/td[@class="t_f"]')
            content  = content_container[0].xpath('string(.)').extract()

            # for branch in content_container:
            #     content  = content + branch.xpath('text()').extract()
            item['content'] = content
            # item['content'] = content_container
            yield item

        # # total = len(preachs)
        # counter = 0
        # sum =  len(preachs)#15
        # print sum
        # for preach in preachs:
        #     # self.answer_id_counter = self.answer_id_counter + 1
        #     # item['answer_id'] = str(self.getTime()) +'_'+ str(self.answer_id_counter)
        #     item['question'] = question
        #     # item['link'] = preach.xpath('h3/a/@href').extract()
        #     item['author'] = preach.xpath('//div[@class="pls favatar"]/div[@class="pi"]/div[@class="authi"]/a/text()')[counter].extract()
        #     item['post_time'] = preach.xpath('//div[@class="pti"]/div[@class="authi"]/em/text()')[counter].extract()
        #     # content = ''
        #     # for branch in preach.xpath('//td[@class ="t_f"]'):
        #     #      content += str(branch.xpath('/text()').extract())
        #     # item['content'] = content
        #     # item['content'] = preach.xpath('////td[@class ="t_f"]/text()')[counter].extract()
        #     counter = counter + 1
        #     print counter
        #     yield item
        #
        # nextlink = self.url + response.xpath('//div[@class="pg"]/a[@class="nxt"]/@href')[0].extract()
        # # print nextlink
        #
        # if nextlink:
        #     yield scrapy.Request(response.urljoin(nextlink[0]),callback=self.parse)