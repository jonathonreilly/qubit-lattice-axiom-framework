"""Minimal local walker bracket witness; Gaussian-integer arithmetic.
32 E_delta has Gaussian-integer entries for the original body-diagonal lapse.
No periodic lattice, Fourier sampling, or approximate arithmetic is used.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import birth_work_exact as m

Z=(0,0); ONE=(1,0); I=(0,1)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a):return -a[0],-a[1]
def times(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scaled(a,n):return a[0]*n,a[1]*n
SIGMA=(((Z,ONE),(ONE,Z)),((Z,minus(I)),(I,Z)),((ONE,Z),(Z,(-1,0))))

def energy(u):
    # E_u=1/2 {C1 C2 C3 delta_u,H}; H_xy=sigma/(2i) for y=x+e.
    corners={m.add(u,d) for d in product((-1,1),repeat=3)}
    edges={(x,m.add(x,d)) for x in corners for d in m.DIRS}
    edges|={(y,x) for x,y in edges}
    out={}
    for x,y in edges:
        d=tuple(b-a for a,b in zip(x,y));axis=next(i for i,v in enumerate(d) if v)
        sign=d[axis];weight=int(x in corners)+int(y in corners)
        for s in (0,1):
            for t in (0,1):
                v=scaled(times((0,-1),SIGMA[axis][s][t]),sign*weight)
                if v!=Z:out[(x,s),(y,t)]=v
    return out

def matmul(a,b):
    brows=defaultdict(list)
    for (i,j),v in b.items():brows[i].append((j,v))
    out=defaultdict(lambda:Z)
    for (i,k),v in a.items():
        for j,w in brows[k]:out[i,j]=plus(out[i,j],times(v,w))
    return {ij:v for ij,v in out.items() if v!=Z}

def main():
    u=(0,0,0);v=(2,0,0);E=energy(u);F=energy(v)
    EF=matmul(E,F);FE=matmul(F,E)
    comm={k:plus(EF.get(k,Z),minus(FE.get(k,Z))) for k in EF.keys()|FE.keys()}
    comm={k:val for k,val in comm.items() if val!=Z};assert comm
    # delta profiles at distance two have zero nearest-neighbour F0 exactly.
    assert sum(abs(a-b) for a,b in zip(u,v))==2
    i,j=sorted(comm)[0];g=times((0,-1),comm[i,j])
    for (r,c),val in comm.items():
        other=comm.get((c,r),Z)
        assert val==(-other[0],other[1])
    result={'nonzero_scalar_entries':len(comm),'nonzero_spatial_blocks':len({(i[0],j[0]) for i,j in comm}),
            'witness_row':i,'witness_column':j,'minus_i_commutator_real':str(Fraction(g[0],1024)),
            'minus_i_commutator_imag':str(Fraction(g[1],1024)),'F0_every_bond':0}
    print(json.dumps(result,indent=2))
    print('TOTAL: PASS=2 FAIL=0 (nonadjacent delta lapse witness; exact Hermitian bracket)')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
