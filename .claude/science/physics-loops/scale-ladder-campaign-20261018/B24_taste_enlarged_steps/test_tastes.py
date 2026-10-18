import sys,os,time; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from b24lib import *
t0=time.time()
for nm,w in [('S2.H20.S2.L202',['S2',onH(2,0),'S2',PC['L202']]),('S.H13.S.L202',['S',onH(1,3),'S',PC['L202']]),('corner step S.R.UH.UL',['S','R',UH,UL]),
             ('S4.H20.S4.L202',['S4',onH(2,0),'S4',PC['L202']]),('S2.H20.S4.L202',['S2',onH(2,0),'S4',PC['L202']]),('S2.H20.S2.H13',['S2',onH(2,0),'S2',onH(1,3)]),
             ('S.H20.S2.L202',['S',onH(2,0),'S2',PC['L202']]),('S2.H20.S4.H13',['S2',onH(2,0),'S4',onH(1,3)])]:
    Lt,L0=lattices(w); T=tastes(w)
    print(nm, 'Lt',lat_name(Lt),'L0',lat_name(L0), 'omegas',sorted({o for v in T.values() for o in v})[:6], f'{time.time()-t0:.1f}s')
