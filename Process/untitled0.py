# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:16:07 2015

@author: m01i795
"""

A = [1, 4, 5, 3, 2, 2, 2, 2, 2, 2, 4, 9]

def solution(A):
    N = len(A)
    result = 0
    interim = {}
    for i in xrange(N):
        if interim.has_key(A[i]):
            result = max(result, i - interim[A[i]])
        else:
            interim[A[i]]=i
    return result
    
print solution(A)