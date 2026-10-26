from engine import *
import sympy as sp, pickle, time
dim=2
W=Walk(dim,2,[(0,1)])
table={}   # (comp) -> list of (r(2), c1,c2, z1(2), z2(2), d1,d2, coef(re,im))
for comp in (0,1):
    rows=[]
    for rx in range(-3,4):
        for ry in range(-3,4):
            for c1 in range(2):
                for c2 in range(2):
                    st=(((rx,ry),c1),((0,0),c2))
                    if not W.allowed(st): continue
                    o=W.O16({st:(1,0)},comp)
                    for t,a in o.items():
                        rows.append(((rx,ry),c1,c2,t[0][0],t[1][0],t[0][1],t[1][1],a))
    table[comp]=rows
    print(comp,len(rows))
pickle.dump(table,open('O16_table.pkl','wb'))
# translation invariance check of the table: shift s by (2,-1) and compare
W2=W
import random
for comp in (0,1):
    for (rx,ry) in [(1,0),(0,1),(1,1),(-1,0),(2,0)]:
        for c1,c2 in [(0,1),(1,0),(0,0)]:
            sh=(5,-7)
            st=(((rx+sh[0],ry+sh[1]),c1),(sh,c2))
            st0=(((rx,ry),c1),((0,0),c2))
            o=W.O16({st:(1,0)},comp); o0=W.O16({st0:(1,0)},comp)
            o0s={ (((t[0][0][0]+sh[0],t[0][0][1]+sh[1]),t[0][1]),((t[1][0][0]+sh[0],t[1][0][1]+sh[1]),t[1][1])):a for t,a in o0.items()}
            assert o==o0s
print("translation covariance ok")
