#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
        �6[n�)���@����ui���#���ŏ$����GO�i����E���17���&��w�~�4�O��ڂ�� ��<�6�+��[E,�|�V���z�\{��~c=z���,{f֣�[���k,~�"""
from hashlib import sha256
h=sha256(blob).hexdigest()
if h[0]=='b':
    print "Go Blue!"
else:
    print "O-H-I-O Go Bucks!"
