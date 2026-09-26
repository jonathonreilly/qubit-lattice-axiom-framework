#!/usr/bin/env python3
"""Exact graph counts and menu arithmetic for the empty-start density effect."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent


def graph(side,dim):
    sites = list(product(range(side),repeat=dim))
    neighbors = {}
    for x in sites:
        adj = set()
        for axis in range(dim):
            for step in (-1,1):
                y = list(x); y[axis] = (y[axis]+step)%side
                adj.add(tuple(y))
        neighbors[x] = adj
    return sites,neighbors


def geometric_counts(side,dim):
    sites,nb = graph(side,dim)
    x = (0,)*dim; end = list(x); end[0] = 1; end = tuple(end)
    counts = Counter()
    for y in sites:
        if y in (x,end):
            continue
        first = len(nb[x] & nb[y]); second = len(nb[end] & nb[y])
        flags = tuple(sorted((int(y in nb[x]),int(y in nb[end]))))
        counts[flags] += (first-second)**2
    assert counts[(0,1)] == 2*(8*dim-7)
    assert counts[(0,0)] == 2*(8*dim*dim-14*dim+7)
    assert counts[(1,1)] == 0
    return {str(k):v for k,v in sorted(counts.items())}


def menu(p,q,r):
    return [[F(6*(p if a == b else q if (a^1) == b else r),p+q+4*r)
             for b in range(6)] for a in range(6)]


def coefficient(W,dim):
    assert all(sum(row) == 6 for row in W)
    assert all(W[a][b] == W[b][a] > 0 for a in range(6) for b in range(6))
    h = [[sum(W[a][c]*W[c][b] for c in range(6))-6 for b in range(6)] for a in range(6)]
    square = sum(value*value for row in h for value in row)
    conductance = sum(h[a][b]**2*W[a][b]/(1+W[a][b]) for a in range(6) for b in range(6))
    result = dim*(2*(8*dim-7)*conductance+(8*dim*dim-14*dim+7)*square)
    assert (result == 0) == all(value == 1 for row in W for value in row)
    return result


if __name__ == '__main__':
    graphs = []
    for dim in (1,2,3):
        for side in (6,7,8):
            graphs.append({'dimension':dim,'side':side,'counts':geometric_counts(side,dim)})
    menus = []
    for p,q,r in ((1,1,1),(3,1,2),(1,3,2),(6,1,2),(12,1,2)):
        for dim in (1,2,3):
            value = coefficient(menu(p,q,r),dim)
            menus.append({'dimension':dim,'raw_weights':[p,q,r],'D2_per_site':str(value),
                          'density_t5_coefficient_per_kappa_epsilon4':str(value/60)})
            if (p,q,r,dim) == (3,1,2,3):
                assert value == F(2379,5)
                assert value/60 == F(793,100)
    # A centered symmetric menu without signed-axis permutation symmetry.
    v = (2,-1,-1,0,0,0)
    nonsymmetric = [[1+F(v[a]*v[b],10) for b in range(6)] for a in range(6)]
    extra = str(coefficient(nonsymmetric,3))
    result = {'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'graphs':graphs,'menus':menus,'non_axis_symmetric_D2_per_site':extra}
    (HERE/'EMPTY_START_GEOMETRY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
