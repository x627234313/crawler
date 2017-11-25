#!/usr/bin/env python
# encoding: utf-8

import os
import requests
import settings


class Downloader(object):
    '''下载器'''
    def download_imgs(self, imgs_url):
        img = requests(imgs_url)
        with open(file, 'wb') as img_file:
            img_file.write(img)

