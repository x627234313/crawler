#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Spider(object):
    '''爬虫类，根据需求从网站中获取指定的url。
    '''

    def __init__(self, parser, downloader, repository):
        '''所需的三个功能对象。

        :param parser:从页面中获取需要的url。
        :param downloader:将返回的url内容下载。
        :param repository:存储url。
        '''
        self.parser = parser
        self.downloader = downloader
        self.repository = repository

    def fetch_urls(self, start_url):
        '''获取url。

        :param start_url:抓取的入口。
        '''
        img_urls = self.parser.parse_html(start_url)
        return img_urls

    def get_imgs(self, imgs_url):
        '''下载图片。
        '''
        self.downloader.download_imgs(imgs_url)

    def query_img(self, sites, description, tag, time):
        '''根据需求查询图片。

        :param sites:来自哪个网站
        :param description:图片描述
        :param tag:图片标签
        :param time:下载时间
        '''
        imgs = self.repository.find_img(sites, description, tag, time)
        return imgs

