#!/usr/bin/env python
# encoding: utf-8

import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='spider',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

