#!/usr/bin/env python3
"""Independent implementations of the author's finite-t intensity coefficient.

The full block generator does not use the hazard-correlation formula. Exact
rational transition assembly is reused from the primary empty-start checker;
this is an author cross-check, not independent-context scrutiny.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
from pathlib import Path
import hashlib
import json
import numpy as np
from scipy.sparse import bmat, coo_matrix
from scipy.sparse.linalg import expm_multiply
from empty_start_exact import model, multiply, expectation

HERE = Path(__file__).resolve().parent
nodes, quadrature = np.polynomial.legendre.leggauss(64)
nodes = (nodes+1)/2; quadrature = quadrature/2


def psi(z):
    z = np.atleast_1d(z)
    return (-np.expm1(-z[:,None]*nodes))@((1-nodes)**3*quadrature)


def sparse(rows):
    ri=[];ci=[];values=[]
    for i,row in enumerate(rows):
        for j,rate in row.items():
            ri.append(i);ci.append(j);values.append(float(rate))
    return coo_matrix((values,(ri,ci)),shape=(len(rows),len(rows))).tocsr()


def spectral_coefficient(H, weights, hazard, kappa, time):
    root = np.sqrt(weights)
    symmetric = root[:,None]*H/root[None,:]
    assert np.max(abs(symmetric-symmetric.T)) < 1e-11
    lam, vectors = np.linalg.eigh(-symmetric)
    assert lam.min() > -1e-10
    lam[abs(lam) < 1e-10] = 0
    projections = (vectors.T@(root*hazard))**2
    return time**4/3*np.dot(projections,psi(kappa*time*lam))


def full_block_case(n, edges, raw, kappa, time):
    states,H,B,b,w,_ = model(n,edges,*raw)
    hm,bm = sparse(H),sparse(B)
    blocks = [[kappa*hm.T if i == j else bm.T if i == j+1 else None
               for j in range(5)] for i in range(5)]
    operator = bmat(blocks,format='csr')
    initial = np.zeros(5*len(states)); initial[0] = 1
    evolved = expm_multiply(time*operator,initial,
        traceA=time*operator.diagonal().sum()).reshape(5,len(states))
    N = np.array([sum(a != 0 for a in s) for s in states])
    row = {0:F(1)}; differences=[]
    for k in range(5):
        if k:
            row = multiply(row,B)
        pure = float(expectation(row,N))*time**k/factorial(k)
        differences.append(float(evolved[k]@N-pure))
    assert max(abs(v) for v in differences[:4]) < 1e-8
    two = np.flatnonzero(N == 2)
    pair_h = hm[two][:,two].toarray()
    pair_w = np.array([float(w[i]) for i in two])
    # Removing this constant does not change the quadratic semigroup drop.
    pair_b = np.array([float(b[i]-6*(n-2)) for i in two])
    predicted = spectral_coefficient(pair_h,pair_w,pair_b,kappa,time)
    error = abs(predicted-differences[4])
    assert error < 1e-8*max(1.,abs(predicted)),(predicted,differences,error)
    result = {'vertices':n,'edges':edges,'raw_weights':raw,'kappa':kappa,'physical_time':time,
              'block_generator_coefficient':differences[4],
              'two_record_semigroup_coefficient':predicted,'absolute_difference':error}
    if n == 3 and edges == ((0,1),(1,2)) and raw == (3,1,2):
        closed = time**4/3*(F(9,8)*psi(8*kappa*time/5)[0]+F(3,4)*psi(4*kappa*time/3)[0])
        assert abs(closed-predicted) < 1e-11
        result['path_closed_formula'] = float(closed)
    return result


def torus(side,dim):
    coords = list(product(range(side),repeat=dim)); index = {x:i for i,x in enumerate(coords)}
    nb=[]
    for x in coords:
        local=set()
        for axis in range(dim):
            for step in (-1,1):
                y=list(x);y[axis]=(y[axis]+step)%side;local.add(index[tuple(y)])
        nb.append(local)
    return coords,nb


def position_matrices(side,dim,g):
    coords,nb = torus(side,dim); n=len(coords)
    pairs=list(combinations(range(n),2)); index={p:i for i,p in enumerate(pairs)}
    w=np.array([g if y in nb[x] else 1. for x,y in pairs])
    c=np.array([len(nb[x]&nb[y]) for x,y in pairs],float)
    H=np.zeros((len(pairs),len(pairs)))
    for i,pair in enumerate(pairs):
        for x in pair:
            other=pair[1] if x == pair[0] else pair[0]
            for dest in nb[x]:
                if dest == other:
                    continue
                j=index[tuple(sorted((dest,other)))]
                H[i,j] += w[j]/(w[i]+w[j])
        H[i,i]=-H[i].sum()
    # A different state description: displacement of labeled endpoint two.
    # The zero displacement is forbidden, and each relative step has two
    # physical endpoint moves.
    wr=np.array([g if r in nb[0] else 1. for r in range(1,n)])
    cr=np.array([len(nb[0]&nb[r]) for r in range(1,n)],float)
    Hr=np.zeros((n-1,n-1))
    for r in range(1,n):
        for dest in nb[r]:
            if dest == 0:
                continue
            Hr[r-1,dest-1] += 2*wr[dest-1]/(wr[r-1]+wr[dest-1])
        Hr[r-1,r-1]=-Hr[r-1].sum()
    return H,w,c,Hr,wr,cr,n


if __name__ == '__main__':
    results=[]
    for kappa in (.1,1.,5.):
        for time in (.2,1.,2.):
            result=full_block_case(3,((0,1),(1,2)),(3,1,2),kappa,time)
            results.append(result);print(json.dumps(result),flush=True)
    for n,edges,raw in ((3,((0,1),(1,2)),(1,1,1)),
                       (3,((0,1),(1,2)),(12,1,2)),
                       (4,((0,1),(1,2),(2,3),(0,3)),(3,1,2))):
        result=full_block_case(n,edges,raw,1.,1.)
        results.append(result);print(json.dumps(result),flush=True)
    relative=[]
    for side,dim in ((4,1),(6,1),(3,2),(4,2),(3,3)):
        for g in (.5,1.,1.5):
            H,w,c,Hr,wr,cr,n=position_matrices(side,dim,g)
            original=spectral_coefficient(H,w,c,1.3,.7)/n
            reduced=spectral_coefficient(Hr,wr,cr,1.3,.7)/2
            assert abs(original-reduced) < 1e-11*max(1.,abs(original))
            relative.append({'side':side,'dimension':dim,'pair_weight':g,
                             'full_position_coefficient_per_site':original,
                             'relative_coefficient_per_site':reduced})
    report={'scope':'Primary finite-t Dyson and relative-position checks, not a finite-density theorem.',
            'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                             (Path(__file__),HERE/'empty_start_exact.py')},
            'block_generator_cases':results,'relative_position_cases':relative}
    (HERE/'FORMATION_INTENSITY_CHECK_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
