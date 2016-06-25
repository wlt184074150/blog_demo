#!/usr/bin/env python
# -*- coding: utf-8 -*-

from metaclass.base_case import BaseCase

__author__ = 'litang.wang'


class Case(BaseCase):
    def find_element_by_id(self, element_id):
        try:
            raise Exception('find element by id fail;id=%s' % element_id)
        except Exception, e:
            print 'catch %s' % e

    @staticmethod
    def find_element_by_name(name):
        try:
            raise Exception('find element by name fail;name=%s' % name)
        except Exception, e:
            print 'catch %s' % e


if __name__ == '__main__':
    case = Case()
    case.find_element_by_id('123')
    case.find_element_by_name('abc')
    Case.find_element_by_name('def')
