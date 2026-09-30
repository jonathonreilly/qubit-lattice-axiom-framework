#!/usr/bin/env python3
"""Exact physical N=6 creator contractions; no Hamiltonian assembly imported.

Gaussian integers are stored as integer pairs. Translation orbit stabilizers
are calculated, not presumed absent. This is a bounded coefficient control.
"""
import json
from collections import defaultdict
from itertools import product

def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def times(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def scale(s,a): return (s*a[0],s*a[1])

def canon(S,L):
    copies=[]
    for p in S:
        copies.append(tuple(sorted(tuple((q[j]-p[j])%L for j in range(3)) for q in S)))
    key=min(copies)
    return key,copies.count(key)

def product_state(D,weights,L):
    """Fixed D anchor zero, all C anchors: full amplitude is stabilizer*g."""
    out=defaultdict(lambda:(0,0)); stabilizers={}; forbidden=0
    for x in product(range(L),repeat=3):
        for j,w in enumerate(weights):
            if w==(0,0): continue
            y=list(x); y[j]=(y[j]+2)%L; y=tuple(y)
            if x in D or y in D:
                forbidden+=1
                continue
            key,s=canon(tuple(D)+(x,y),L)
            out[key]=plus(out[key],w)
            assert key not in stabilizers or stabilizers[key]==s
            stabilizers[key]=s
    return dict(out),stabilizers,forbidden

def inner_per_volume(a,b):
    av,ast,_=a; bv,bst,_=b; result=(0,0)
    for key,v in av.items():
        if key in bv:
            assert ast[key]==bst[key]
            result=plus(result,scale(ast[key],times(conj(v),bv[key])))
    return result

def run():
    rectangle=((0,0,0),(2,0,0),(0,2,0),(2,2,0))
    line=((0,0,0),(2,0,0),(4,0,0),(6,0,0))
    e=((1,0),(-1,0),(0,0))
    c=((1,0),(0,1),(-1,-1))
    rows=[]
    for L in (17,19):
        V=L**3
        de=product_state(rectangle,e,L)
        dc=product_state(rectangle,c,L)
        fe=product_state(line,e,L)
        ne=inner_per_volume(de,de)
        nc=inner_per_volume(dc,dc)
        ec=inner_per_volume(de,dc)
        ef=inner_per_volume(de,fe)
        rows.append({'L':L,'V':V,'norm_DC_e_per_V':ne,
                     'norm_DC_complex_per_V':nc,'cross_same_D_per_V':ec,
                     'cross_distinct_DF_per_V':ef,
                     'remainders':{'e':plus(ne,(-2*V,0)),
                                   'complex':plus(nc,(-4*V,0)),
                                   'cross':plus(ec,(-V,V)),'DF':ef},
                     'forbidden_words':[de[2],dc[2],fe[2]],
                     'orbit_counts':[len(de[0]),len(dc[0]),len(fe[0])],
                     'max_stabilizer':max(max(x[1].values()) for x in (de,dc,fe))})
    assert rows[0]['remainders']==rows[1]['remainders']
    # A real non-free translation orbit: six equally spaced sites on L=18.
    _,s=canon(tuple((j*3,0,0) for j in range(6)),18)
    assert s==6
    result={'arithmetic':'exact Gaussian-integer pairs',
            'normalization':'inner/V=sum_orbit stabilizer*conj(g_left)*g_right',
            'rows':rows,'explicit_nontrivial_stabilizer':s,
            'passed':['four independent coefficients stabilize after leading V term',
                      'literal hard-core exclusion retained',
                      'non-free orbit stabilizer control'],
            'limits':'Two N=6 fixture families, not a general all-N proof.'}
    print(json.dumps(result,indent=2))
    print('TOTAL PASS 3 FAIL 0')

if __name__=='__main__': run()
