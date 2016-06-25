#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
from functools import wraps

from metaclass.base_case import BaseCase

__author__ = 'litang.wang'


def catch(func):
    @wraps(func)  # 使用wrap注解,保证添加注解后,方法的__name__属性不变
    def _catch(cls, *args, **kwargs):
        try:
            func(cls, *args, **kwargs)
        except Exception, e:
            print 'catch %s' % e

    return _catch


class CatchMetaclass(type):
    def __new__(cls, name, bases, attrs):
        for base in bases:

            method_list = inspect.getmembers(base, inspect.ismethod)
            for method in method_list:  # 如果是method,直接用catch封装,设置为父类属性
                setattr(base, method[0], catch(method[1]))

            function_list = inspect.getmembers(base, inspect.isfunction)
            for function in function_list:  # 如果是function,需要用staticmethod再封装一下,否则该方法将不再是静态方法
                setattr(base, function[0], staticmethod(catch(function[1])))

        return type.__new__(cls, name, bases, attrs)


class Case(BaseCase):
    __metaclass__ = CatchMetaclass


if __name__ == '__main__':
    case = Case()
    case.find_element_by_id('123')
    case.find_element_by_name('abc')
    Case.find_element_by_name('def')
