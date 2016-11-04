# encoding = utf-8
import json
from datetime import datetime,timedelta

url_list = []
# with open("D://Users//Administrator//PycharmProjects//coolscrapy//allQuestions.json", "r") as f:
with open("D://Users//Administrator//PycharmProjects//coolscrapy//answer_all.json", "r") as f:
    data = json.load(f)
    counter = 0
    for item in data:
        # url_list.append(item['link'][0])
        # string = item['content'][0].encode('utf-8')
        post_time = item['post_time'][0][3:].encode('utf-8')
        if len(post_time) < 3:
            continue
        answer_date = datetime.strptime(post_time, ' %Y-%m-%d %H:%M:%S')
        time_point = datetime.now()+timedelta(days = - 30)
        time_interval = time_point - answer_date
        counter = counter +1
        # print counter
        # url_list.append(string)
        if time_point < answer_date :
            # print answer_date
            print item['content'][0].encode('utf-8')
        # print post_time

    # print url_list
    # print len(url_list)


class data_parser():

    name = "parse_json"

    def parse_json(self):
        with open("D://Users//Administrator//PycharmProjects//coolscrapy//answer.json", "r") as f:
            data = json.load(f)
            # get date time
            # counter =0
            for item in data:
                str = item['post_time'][0].encode('utf-8')
                answer_date = datetime.strptime(str[9:], ' %Y-%m-%d %H:%M:%S')
                print answer_date
                print item['author'][0].encode('utf-8')
                # print item['question'].encode('utf-8')
                print item['content'][0].encode('utf-8')