#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'litang.wang'


class BaseCase(object):
    def find_element_by_id(self, element_id):
        raise Exception('find element by id fail;id=%s' % element_id)

    @staticmethod
    def find_element_by_name(name):
        raise Exception('find element by name fail;name=%s' % name)
