import pickle, collections
from ilib import *
exec(open('check_4.py').read().split('# ================= T-junction')[0])
H=HalfModel(6)
exec(open('check_4.py').read().split('# ================= signed sectors and pair test')[1].split('H = HalfModel(L)')[0].replace('def pair_test','def _pt'))
for (o,st) in codes[:3]:
  for M in st:
    if not rot_type(M).startswith('C2'): continue
    g=generators(H,o); sp=span_of(H,g)
    perm=H.rot_qubit_perm(M)
    x=offaxis_points(M)[0]; Rx=mvec(M,x)
    Sx=string(H,o,x,Rx); SR=permute_pauli(Sx,perm); T=pmul(pdag(Sx),SR)
    anti=[i for i,G in enumerate(g) if not commute(T,G)]
    # which generators anticommute with Sx and SR
    a1=[i for i,G in enumerate(g) if not commute(Sx,G)]
    a2=[i for i,G in enumerate(g) if not commute(SR,G)]
    print(rot_type(M), x, Rx, 'T anti', len(anti), 'S flips', a1, 'SR flips', a2, sp.eig(T))
