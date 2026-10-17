from polytools import *
CH=(0,1,1,3,3,2,2); Dx=(0,)+tuple(l|4 for l in CH[1:])
print(recordfree([Dx],[4],'d1'))
print(recordfree([Dx],[],'d2'))   # all ops allowed: expect even triple to fail containment
print(recordfree([CH],[],'d3'))
