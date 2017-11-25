#!/usr/bin/env python
# encoding: utf-8

import requests
from bs4 import BeautifulSoup

class Parser(object):
    '''解析器'''
    #def __init__(self, start_url):
    #    '''
    #    :param start_url:页面的入口。
    #    '''
    #    self.start_url = start_url

    def parse_html(self, start_url):
        start_html = requests.get(start_url)
        img_urls = BeautifulSoup(start_html.text, 'lxml').find_all('li', class_='')
        return img_urls
