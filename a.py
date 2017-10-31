#!/usr/bin/env python
# coding:utf8

import time
import os

def Foo():
	count = 0
    while count <= 10:
	    print "OK"
		time.sleep(0.5)
		count += 1

	return count

if __name__ == "__main__":
    Foo()
