#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


class Case(BaseCase):
    @catch
    def find_element_by_id(self, element_id):
        raise Exception('find element by id fail;id=%s' % element_id)

    @staticmethod
    @catch
    def find_element_by_name(name):
        raise Exception('find element by name fail;name=%s' % name)


if __name__ == '__main__':
    case = Case()
    case.find_element_by_id('123')
    case.find_element_by_name('abc')
    Case.find_element_by_name('def')
