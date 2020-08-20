#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   language.py
@Time    :   2020/08/19
@Author  :   Yaronzz
@Version :   1.0
@Contact :   yaronhuang@foxmail.com
@Desc    :   
'''
from tidal_dl.lang.english import LangEnglish
from tidal_dl.lang.chinese import LangChinese
from tidal_dl.lang.turkish import LangTurkish
from tidal_dl.lang.italian import LangItalian
from tidal_dl.lang.czech import LangCzech


def initLang(index):  # 初始化
    global LANG
    return setLang(index)

def setLang(index):
    global LANG
    if str(index) == '0':
        LANG = LangEnglish()
    elif str(index) == '1':
        LANG = LangChinese()
    elif str(index) == '2':
        LANG = LangTurkish()
    elif str(index) == '3':
        LANG = LangItalian()
    elif str(index) == '4':
        LANG = LangCzech()
    else:
        LANG = LangEnglish()
    return LANG

def getLang():
    global LANG
    return LANG

def getLangName(index):
    if str(index) == '0':
        return "English"
    if str(index) == '1':
        return "中文"
    if str(index) == '2':
        return "Turkish"
    if str(index) == '3':
        return "Italian"
    if str(index) == '4':
        return "Czech"
    return "English"