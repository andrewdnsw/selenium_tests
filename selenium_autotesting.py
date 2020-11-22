#!/usr/bin/python3.6
# coding: utf-8

# а ну и импорты 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import time
import math
import os
from pyzabbix.api import ZabbixAPI
from pyzabbix import ZabbixMetric, ZabbixSender

def test_search_title_in_hrportal(self):
        
        def auth():
            try:
                f = open('C:/pytests/auth.txt', 'r')
            except:
                print("No file")
            lo = f.read()            
            f.close()
            return lo
        ur = 'http://' + auth() + '@intranet.homecredit.ru/'
        print(ur)
        
        def num(toc, tic):
            Treq = float('{:.3f}'.format(toc - tic))
            return Treq

 

        def zaebitrix(zname, rdata):
            user = "webtutor_api"
            password = "12345678"

 

            url = 'https://zabbix.homecredit.ru'
            z = ZabbixAPI(url=url, user=user, password=password)

 

            packet = [ZabbixMetric('intranet.homecredit.ru', zname, rdata)]

 

            result = ZabbixSender(zabbix_server='10.6.141.33', use_config=False).send(packet)
            print(result)
            logout = z.user.logout()
            
        def clean1log():

 

            dat = open('1log.txt', 'r')
            dat_str = int(dat.readline())
            dat_str_2 = dat_str + 1
            dat.close()
            
            inp = open('1log.txt', 'w')
            dat_str_2 = str(dat_str_2)
            inp.write(dat_str_2)
            inp.close()
            print ('write 1log.txt - OK')

 

        def clean2log():

 

            dat = open('2log.txt', 'r')
            dat_str = int(dat.readline())
            dat_str_2 = dat_str + 1
            dat.close()
            
            inp = open('2log.txt', 'w')
            dat_str_3 = str(dat_str_2)
            inp.write(dat_str_3)
            inp.close()
            print ('write 1log.txt - OK')

 

        try:
            driver = self.driver
            tic = time()
            driver.get(ur)
            self.assertIn("Портал для сотрудников", driver.title)
            toc = time()
            print('Load Page - OK', 'Time Req = ', num(toc, tic), 's')
            rdat = num(toc, tic)
            zname = "load"
            zaebitrix(zname, rdat)
        except:
            clean2log()