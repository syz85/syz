#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys
import os
import time


def get_current_path():
    """获取脚本的路径"""
    return sys.path[0]


def get_file_full_path_recursively(root_path, file_extension_list=None):
    """
    获取文件夹中的所有文件（递归）
    :param root_path: 目标文件夹的路径
    :param file_extension_list: 过滤的文件类型，如：jpg png
    :return: 文件的全路径list
    """
    if not os.path.exists(root_path):
        raise FileNotFoundError

    if not os.path.isdir(root_path):
        raise Exception('root_path is not a directory')

    if type(file_extension_list) is not list and file_extension_list is not None:
        raise Exception('file_extension_list is neither a list nor None')

    if file_extension_list is not None:
        file_extension_set = set([temp.lower() for temp in file_extension_list])
    else:
        file_extension_set = None

    result_list = list()

    file_list = os.listdir(root_path)
    for file_name in file_list:
        file_full_path = os.sep.join([root_path, file_name])

        if os.path.isdir(file_full_path):
            # 如果是文件夹，则递归
            result_list += get_file_full_path_recursively(file_full_path, file_extension_list)
        else:
            # 如果是文件，则记录结果
            if file_extension_list is not None:
                extension = os.path.splitext(file_name)[1].replace('.', '').lower()
                if extension in file_extension_set:
                    result_list.append(file_full_path)
            else:
                result_list.append(file_full_path)

    return result_list


def get_now_date_str():
    """获取当前的日期字符串"""
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def get_now_datetime_str():
    """获取当前的日期时间字符串"""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def datetime_str_2_timestamp(datetime_str):
    """将日期时间的字符串转为时间戳"""
    datetime_tuple = time.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(datetime_tuple))


def timestamp_2_datetime_str(timestamp):
    """将时间戳转为日期时间字符串"""
    datetime_tuple = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%Mget_file_full_path_recursively:%S", datetime_tuple)


def get_file_extension(file_name):
    """获取文件的后缀名"""
    return os.path.splitext(file_name)[1].replace('.', '').lower()
