#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import string
import enum


class StopWordType(enum.Enum):
    """停用词类型"""
    PUNCTUATION = string.punctuation + "￥！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏."
    NUMBER = '0123456789０１２３４５６７８９'
    SPACE = ' \t\n\r　'


def remove_stop_word(input_string, stop_word_type_list):
    """
    去掉停用词
    :param input_string: 输入的字符串
    :type input_string: str
    :param stop_word_type_list: 停用词的list
    :return: 处理完的
    """
    if type(stop_word_type_list) is not list or len(stop_word_type_list) == 0:
        raise TypeError('stop_word_type_list is not list or is empty')

    for stop_word_type in stop_word_type_list:
        if stop_word_type not in StopWordType:
            raise TypeError('stop_word_type_list is not StopWordType')

    if type(input_string) is not str:
        raise TypeError('input_string is not string')

    # 合并停用词
    stop_word = ''
    for stop_word_type in stop_word_type_list:
        stop_word += stop_word_type.value
    stop_word = set(stop_word)

    # 去掉停用词
    result_string = ''
    for char in input_string:
        if char not in stop_word:
            result_string += char

    return result_string
