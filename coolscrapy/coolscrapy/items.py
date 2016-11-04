# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    corp = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    click = scrapy.Field()


class NextPageItem(scrapy.Item):
    url = scrapy.Field()


class QuestionItem(scrapy.Item):
    title = scrapy.Field()#问题
    link = scrapy.Field()#问题链接
    desc = scrapy.Field()#描述信息
    author  = scrapy.Field()#提问者
    post_time = scrapy.Field()#问题时间
    question_id = scrapy.Field()#问题的唯一id（保证答案的爬取不重）


class AnswerItem (scrapy.Item):
    question = scrapy.Field()#对应的问题原文
    content = scrapy.Field()#答案内容
    post_time = scrapy.Field()#回答的发布时间
    author = scrapy.Field()#答案作者
    answer_id = scrapy.Field()#答案唯一id（保证每天增量更新）
    answer_url = scrapy.Field()#答案的url
