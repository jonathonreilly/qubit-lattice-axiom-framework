#!/usr/bin/env python3
"""Exact rational empty-start derivatives, assembled from full configurations."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
AXES = ((0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))


def model(n, edges, p, q, r):
    scale = F(6, p+q+4*r)
    W = [[F(1) for _ in range(7)] for _ in range(7)]
    for a in range(1,7):
        for b in range(1,7):
            W[a][b] = scale*(p if a == b else q if ((a-1)^1) == b-1 else r)
    states = list(product(range(7), repeat=n))
    index = {s:i for i,s in enumerate(states)}
    nb = [[b if a == x else a for a,b in edges if x in (a,b)] for x in range(n)]
    weight = []
    for s in states:
        value = F(1)
        for x,y in edges:
            value *= W[s[x]][s[y]]
        weight.append(value)
    H, B, hazard = [], [], []
    for k,s in enumerate(states):
        h, birth = {}, {}
        for x in range(n):
            if s[x]:
                continue
            for a in range(1,7):
                rate = F(1)
                for y in nb[x]:
                    rate *= W[a][s[y]]
                t = list(s); t[x] = a; dest = index[tuple(t)]
                birth[dest] = rate
        hazard.append(sum(birth.values(), F(0)))
        birth[k] = -hazard[-1]
        for x,y in edges:
            if (s[x] == 0) == (s[y] == 0):
                continue
            t = list(s); t[x],t[y] = t[y],t[x]; dest = index[tuple(t)]
            h[dest] = weight[dest]/(weight[k]+weight[dest])
        h[k] = -sum(h.values(), F(0))
        assert sum(h.values()) == sum(birth.values()) == 0
        H.append(h); B.append(birth)
    return states, H, B, hazard, weight, scale*(p-q)


def multiply(row, matrix):
    out = defaultdict(F)
    for i, value in row.items():
        for j, rate in matrix[i].items():
            out[j] += value*rate
    return {k:v for k,v in out.items() if v}


def mixture(H, B, kappa, epsilon):
    out = []
    for h,b in zip(H,B):
        keys = h.keys() | b.keys()
        out.append({j:kappa*h.get(j,0)+epsilon*b.get(j,0) for j in keys})
    return out


def expectation(row, observable):
    return sum((value*observable[k] for k,value in row.items()), F(0))


def check(n, edges, p, q, r):
    states,H,B,b,w,theta = model(n,edges,p,q,r)
    N = [sum(a != 0 for a in s) for s in states]
    empty = {0:F(1)}
    B1 = multiply(empty,B); B2 = multiply(B1,B); B3 = multiply(B2,B)
    assert not multiply(B1,H)
    assert not multiply(B2,H)
    for k,s in enumerate(states):
        target = 36*n*n if N[k] == 0 else -6*(2*n-1) if N[k] == 1 else 2*w[k] if N[k] == 2 else 0
        assert B2.get(k,0) == target
        if N[k] == 2:
            assert B3[k] == -2*w[k]*(6*(2*n-1)+b[k])
        if N[k] == 3:
            assert B3[k] == 6*w[k]
    dirichlet = F(0)
    for i in range(len(states)):
        if N[i] == 2:
            for j,rate in H[i].items():
                dirichlet += w[i]*rate*(b[j]-b[i])**2/2
    hb = [sum(rate*b[j] for j,rate in h.items()) for h in H]
    assert dirichlet == -sum(w[i]*b[i]*hb[i] for i in range(len(states)) if N[i] == 2)
    assert dirichlet >= 0
    assert expectation(multiply(B3,H), b) == 2*dirichlet
    # Two actual generators, without using the derived power expansion.
    kappa,epsilon = F(2),F(1,3)
    moving = mixture(H,B,kappa,epsilon)
    fixed = mixture(H,B,F(0),epsilon)
    left,right = empty,empty
    derivatives = []
    for order in range(1,6):
        left = multiply(left,moving); right = multiply(right,fixed)
        difference = expectation(left,N)-expectation(right,N)
        if order <= 3:
            assert left == right
        if order <= 4:
            assert difference == 0
        else:
            assert difference == 2*kappa*epsilon**4*dirichlet
        derivatives.append(str(difference))
    # Initial spatial pair covariance from the full second law derivative.
    second = multiply(multiply(empty,moving),moving)
    chi = [F(v[0]) for v in AXES]; nu = F(1,3)
    for x in range(n):
        for y in range(x+1,n):
            observable = [chi[s[x]]*chi[s[y]] for s in states]
            edge = (x,y) in edges or (y,x) in edges
            assert expectation(second,observable)/2 == 6*nu*theta*epsilon**2*edge
    return {'vertices':n,'edges':edges,'raw_weights':[p,q,r],
            'states':len(states),'theta':str(theta),'D2':str(dirichlet),
            'population_t5_coefficient_per_kappa_epsilon4':str(dirichlet/60),
            'population_derivative_differences_orders_1_to_5':derivatives,
            'kappa':str(kappa),'epsilon':str(epsilon)}


if __name__ == '__main__':
    began = time.monotonic()
    cases = []
    for n,edges in ((2,((0,1),)), (3,((0,1),(1,2))),
                    (3,((0,1),(1,2),(0,2))),
                    (4,((0,1),(1,2),(2,3),(0,3)))):
        for p,q,r in ((1,1,1),(3,1,2),(1,3,2),(12,1,2)):
            result = check(n,edges,p,q,r)
            cases.append(result)
            print(json.dumps(result), flush=True)
    report = {'scope':'Exact rational finite-state verification of empty-start identities; no limit inference.',
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'cases':cases,'elapsed_seconds':time.monotonic()-began}
    (HERE/'EMPTY_START_EXACT_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
