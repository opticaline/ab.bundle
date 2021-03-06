# -*- coding: utf-8 -*-
import json
from subtitile import Ass
from utils import Requests


class DanMuManager:
    handler_map = dict()

    def __init__(self):
        self.handler_map['acfun'] = AcFunParse

    def can_do(self, site):
        return site in self.handler_map.keys()

    def trans(self, site, url):
        handler = self.handler_map[site]
        return handler(url).trans()


class Parse:
    context = None
    ass = Ass()

    def __init__(self, url):
        self.context = Requests(url=url).request()


class AcFunParse(Parse):
    def trans(self):
        data = json.loads(self.context)
        temp = []
        for d in data:
            temp.extend(d)
        for d in temp:
            c = d['c'].split(',')
            self.ass.add_message(float(c[0]), int(c[1]), d['m'], int(c[2]))

        return str(self.ass)
