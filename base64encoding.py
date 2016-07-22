# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 12:50:09 2016

@author: student
"""

import base64

encoded = base64.b64encode(b'"""my message"""')

print(encoded)