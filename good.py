#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
        �6[n�)���@����u���#���ŏ$����GO�i��ѕ�E���17���&�_w�~�4�O��ڂ�� ��<�6�+%�[E,�|�V���z�\{��~c=z����,{f֣�[��xk,~�"""
from hashlib import sha256
h=sha256(blob).hexdigest()
if h[0]=='b':
    print "Go Blue!"
else:
    print "O-H-I-O Go Bucks!"
