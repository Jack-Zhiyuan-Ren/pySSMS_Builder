# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:11:22 2023

@author: zr11
"""

import xmltodict

def xml2dict(xml_file):
    with open(xml_file, 'r') as file:
        xml_data = file.read()
        data_dict = xmltodict.parse(xml_data)
    return data_dict