import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from b24lib import *
def lv(w,k): return [(round(E/np.pi,4),m) for E,m in levels(Wb(w,np.asarray(k,float)[None])[0])]
for nm,w in [('S2.H20.S2.L202',['S2',onH(2,0),'S2',PC['L202']]),('S.H13.S.L202',['S',onH(1,3),'S',PC['L202']])]:
    Lt,L0=lattices(w); print(nm, lat_name(L0))
    for lab,k in [('k*',kst),('-k*',-kst),('0',[0,0,0]),('(pi/4)ex',[np.pi/4,0,0]),('(pi/4)(110)',[np.pi/4,np.pi/4,0]),('(pi/2)ex',[np.pi/2,0,0]),('(pi/2)(110)',[np.pi/2,np.pi/2,0]),('(pi/4)(111)',[np.pi/4]*3)]:
        print('  ',lab, point_type(np.array(k,float),L0), lv(w,k))
