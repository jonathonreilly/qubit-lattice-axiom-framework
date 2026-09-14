#!/usr/bin/env python3
"""Direct sparse cochain check, separate from the dense cellular generator.

Tests a specified pair of actual cubic integer-flux histories and the
failure of their endpoint-balanced event allocation. No energy ordering
or exclusion of more general path transformations is claimed.
"""
from collections import defaultdict
from itertools import product
from pathlib import Path
import json
import sympy as sp

EDGES=[(2,(3,1,1)),(0,(2,1,1)),(0,(2,2,1)),(1,(3,2,1)),
       (0,(3,2,1)),(2,(4,2,1)),(2,(4,1,1))]
FACES=[((0,2),(2,1,1)),((0,1),(2,1,1)),((0,1),(2,2,1)),
       ((0,1),(3,2,1)),((0,2),(3,2,1)),((1,2),(4,1,1)),((0,2),(3,1,1))]
INITIAL={
 ((0,1),(0,1,2)):-1,((0,1),(1,1,2)):1,((0,1),(1,2,1)):1,
 ((0,1),(2,2,1)):-1,((0,2),(0,2,1)):1,((0,2),(1,1,1)):1,
 ((0,2),(2,1,1)):-1,((0,2),(3,2,1)):-1,((1,2),(1,1,1)):-1,
 ((1,2),(1,1,2)):-1,((1,2),(1,2,1)):-1,((1,2),(2,0,1)):1,
 ((1,2),(2,2,0)):-1,((1,2),(3,1,1)):1,((1,2),(3,2,1)):-1,
}

def move_anchor(a,axis,step):
    b=list(a);b[axis]+=step;return tuple(b)

def cleaned(x):return {k:v for k,v in x.items() if v}

def add(x,y,scale=1):
    out=defaultdict(int,x)
    for k,v in y.items():out[k]+=scale*v
    return cleaned(out)

def curl_of_edge(axis,anchor):
    # curl_ij(a)(x)=a_i(x)+a_j(x+ei)-a_i(x+ej)-a_j(x).
    out=defaultdict(int)
    for other in range(3):
        if other==axis:continue
        face=tuple(sorted((axis,other)));sign=1 if axis==face[0] else -1
        out[(face,anchor)]+=sign
        out[(face,move_anchor(anchor,other,-1))]-=sign
    return cleaned(out)

def divergence(flux):
    # Alternating oriented outward faces of a cube.
    out=defaultdict(int)
    for (axes,anchor),value in flux.items():
        missing=next(i for i in range(3) if i not in axes)
        sign=(-1)**missing
        out[move_anchor(anchor,missing,-1)]+=sign*value
        out[anchor]-=sign*value
    return cleaned(out)

def main():
    jumps=[curl_of_edge(*e) for e in EDGES]
    assert all(len(j)==4 and not divergence(j) for j in jumps)
    initial_div=divergence(INITIAL)
    assert initial_div=={(0,1,1):-3,(1,1,1):3}
    x=dict(INITIAL);path=[dict(x)]
    for j in jumps:
        x=add(x,j);assert all(abs(v)<=1 for v in x.values())
        assert divergence(x)==initial_div;path.append(dict(x))
    z={}
    for j in jumps:z=add(z,j)
    M=sp.Matrix([[j.get(f,0) for j in jumps] for f in FACES])
    rhs=sp.Matrix([z.get(f,0)//2 for f in FACES])
    assert all(z.get(f,0)%2==0 for f in FACES)
    assert M.det()==-2
    solution=M.inv()*rhs
    assert solution==sp.ones(7,1)/2
    # A second exact route: enumerate only the 128 event assignments, not
    # an exponentially large lattice Hilbert space.
    feasible=[]
    for assignment in product((0,1),repeat=7):
        if M*sp.Matrix(assignment)==rhs:feasible.append(assignment)
    assert not feasible
    for j in reversed(jumps):
        x=add(x,j,-1);assert all(abs(v)<=1 for v in x.values())
        assert divergence(x)==initial_div
    assert x==INITIAL
    assert divergence({f:-v for f,v in INITIAL.items()})=={k:-v for k,v in initial_div.items()}
    result={'scope':'explicit bulk cubic histories; endpoint-balanced event allocation only',
            'edges':EDGES,'selected_faces':FACES,'initial_nonzero_flux':[(k,v) for k,v in INITIAL.items()],
            'initial_nonzero_divergence':list(initial_div.items()),'forward_event_count':7,
            'closed_moving_path_event_count':14,'second_path':'static opposite initial flux',
            'all_event_star_sizes':[len(j) for j in jumps],
            'selected_minor':[list(map(int,M.row(i))) for i in range(7)],
            'determinant':int(M.det()),'allocation_rhs':list(map(int,rhs)),
            'unique_relaxed_assignment':list(map(str,solution)),
            'binary_assignments_checked':128,'balanced_binary_assignments':0,
            'original_path_verified_with_integer_arithmetic':True}
    Path(__file__).with_name('BLOCK2_CUBIC_PATH_EXACT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
