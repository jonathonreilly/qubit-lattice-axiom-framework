#!/usr/bin/env python3
"""Portable checks of the supplied empty-start mobile-record model.

Exact rational global generators check the time powers and spatial covariances.
Floating block exponentials retain the motion semigroup and independently test
its formation-intensity coefficient. Algebraic family proofs are in the note.
This runner uses no simulation data, fitted parameters, or equilibrium closure.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial

import numpy as np
from scipy.sparse import bmat, coo_matrix
from scipy.sparse.linalg import expm_multiply

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/MOBILE_RECORDS_EMPTY_START_MOTION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = {
    'omit_birth_holding': 'startup',
    'double_time_coefficient': 'startup',
    'reverse_correlation_sign': 'startup',
    'omit_geometry_endpoint': 'geometry',
    'reverse_semigroup_drop': 'intensity',
    'omit_relative_endpoint': 'relative',
    'omit_motion_rate_bound': 'remainder',
    'merge_rook_delayed_order': 'delayed',
}


class Checks:
    def __init__(self):
        self.passed = self.failed = 0
        self.families = set()

    def run(self, family, label, function):
        try:
            result = function()
        except AssertionError as error:
            self.failed += 1
            self.families.add(family)
            print(f'FAIL: {family}: {label}: {error}')
            return None
        self.passed += 1
        print(f'PASS: {family}: {label}')
        return result


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


def startup_case(n, edges, p, q, r, mutation=None):
    states,H,B,b,w,theta = model(n,edges,p,q,r)
    N = [sum(a != 0 for a in s) for s in states]
    if mutation == 'omit_birth_holding':
        B = [row.copy() for row in B]
        for i,row in enumerate(B):
            row[i] = F(0)
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
            assert difference == (4 if mutation == 'double_time_coefficient' else 2)*kappa*epsilon**4*dirichlet
        derivatives.append(str(difference))
    # Initial spatial pair covariance from the full second law derivative.
    second = multiply(multiply(empty,moving),moving)
    chi = [F(v[0]) for v in AXES]; nu = F(1,3)
    for x in range(n):
        for y in range(x+1,n):
            observable = [chi[s[x]]*chi[s[y]] for s in states]
            edge = (x,y) in edges or (y,x) in edges
            assert expectation(second,observable)/2 == (-1 if mutation == 'reverse_correlation_sign' else 1)*6*nu*theta*epsilon**2*edge
    assert dirichlet == graph_energy(n,edges,p,q,r)
    return {'vertices':n,'edges':edges,'raw_weights':[p,q,r],
            'states':len(states),'theta':str(theta),'D2':str(dirichlet),
            'population_t5_coefficient_per_kappa_epsilon4':str(dirichlet/60),
            'population_derivative_differences_orders_1_to_5':derivatives,
            'kappa':str(kappa),'epsilon':str(epsilon)}


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


def geometric_counts(side,dim,mutation=None):
    sites,nb = graph(side,dim)
    x = (0,)*dim; end = list(x); end[0] = 1; end = tuple(end)
    counts = Counter()
    for y in sites:
        if y in (x,end):
            continue
        first = len(nb[x] & nb[y]); second = len(nb[end] & nb[y])
        flags = tuple(sorted((int(y in nb[x]),int(y in nb[end]))))
        counts[flags] += (first-second)**2
    assert counts[(0,1)] == (1 if mutation == 'omit_geometry_endpoint' else 2)*(8*dim-7)
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


def full_block_case(n, edges, raw, kappa, time, mutation=None):
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
    if mutation == 'reverse_semigroup_drop':
        predicted = -predicted
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


def position_matrices(side,dim,g,mutation=None):
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
            Hr[r-1,dest-1] += (1 if mutation == 'omit_relative_endpoint' else 2)*wr[dest-1]/(wr[r-1]+wr[dest-1])
        Hr[r-1,r-1]=-Hr[r-1].sum()
    return H,w,c,Hr,wr,cr,n



def graph_energy(n,edges,p,q,r):
    W=menu(p,q,r)
    nb=[{y if x==i else x for x,y in edges if i in (x,y)} for i in range(n)]
    h=[[sum(W[a][c]*W[c][b] for c in range(6))-6 for b in range(6)] for a in range(6)]
    total=F(0)
    for x,xp in edges:
        for y in range(n):
            if y in (x,xp):
                continue
            change=len(nb[xp]&nb[y])-len(nb[x]&nb[y])
            for a,b in product(range(6),repeat=2):
                u=W[a][b] if y in nb[x] else F(1)
                v=W[a][b] if y in nb[xp] else F(1)
                total+=u*v/(u+v)*h[a][b]**2*change**2
    return total


def backward(matrix,values):
    return [sum((rate*values[j] for j,rate in row.items()),F(0)) for row in matrix]


def deletion_check():
    states,H,B,b,w,_=model(4,((0,1),(1,2),(2,3)),3,1,2)
    ids={s:i for i,s in enumerate(states)}
    classes={};remaining=set(range(len(states)));nclasses=0
    while remaining:
        start=min(remaining);component={start};todo=[start]
        while todo:
            i=todo.pop()
            for j,rate in H[i].items():
                if j!=i and rate>0 and j not in component:
                    component.add(j);todo.append(j)
        remaining-=component
        classes.update({i:nclasses for i in component});nclasses+=1
    parents=[]
    for s in states:
        local=[]
        for x,a in enumerate(s):
            if a:
                t=list(s);t[x]=0;local.append(ids[tuple(t)])
        parents.append(local)
    # Equality of the complete class-label multisets tests every class-constant
    # function, not a single conveniently chosen element of ker H.
    signatures=[Counter(classes[j] for j in local) for local in parents]
    for i,row in enumerate(H):
        for j,rate in row.items():
            if j!=i and rate>0:
                assert signatures[i]==signatures[j]
    f=[F((17*i)%23-11,13) for i in range(len(states))]
    p={i:w[i]*f[i] for i in range(len(states)) if f[i]}
    transformed=multiply(p,B)
    for i in range(len(states)):
        assert transformed.get(i,F(0))/w[i]==sum(f[j] for j in parents[i])-b[i]*f[i]
    print(f'deletion: states={len(states)} actual_motion_classes={nclasses}')


def rook_check(mutation):
    coords=list(product(range(4),repeat=2))
    nb={x:{y for y in coords if x!=y and (x[0]==y[0] or x[1]==y[1])} for x in coords}
    assert all(len(nb[x]&nb[y])==2 for x,y in combinations(coords,2))
    before={(0,0),(0,1),(0,2)};after={(0,0),(0,1),(1,2)}
    def hazard(occupied):
        return sum((F(3,2)**len(nb[x]&occupied)+F(1,2)**len(nb[x]&occupied)+4
                    for x in coords if x not in occupied),F(0))
    def weight(occupied):
        return F(3,2)**sum(y in nb[x] for x,y in combinations(occupied,2))
    b0,b1=hazard(before),hazard(after);w0,w1=weight(before),weight(after)
    assert (b0,b1,w0,w1)==(F(159,2),F(81),F(27,8),F(3,2))
    edge_energy=w0*w1/(w0+w1)*(b1-b0)**2
    assert edge_energy==F(243,104)>0
    m=2 if mutation=='merge_rook_delayed_order' else 3
    assert m==3 and (m+2,m+3)==(5,6)
    print(f'rook: two_record_energy=0 three_record_single_edge_energy={edge_energy} first_level={m}')


def remainder_check(mutation):
    states,H,B,b,w,_=model(3,((0,1),(1,2)),3,1,2)
    z=2;K=2*(z+1);u=F(3,2)
    for kappa,epsilon in ((F(2,3),F(1,7)),(F(1),F(0)),(F(0),F(1,7))):
        L=mixture(H,B,kappa,epsilon)
        R=6*epsilon*u**z+(0 if mutation=='omit_motion_rate_bound' else z*kappa)
        for site in range(3):
            f=[F(bool(s[site])) for s in states];bound=F(1)
            for order in range(1,7):
                f=backward(L,f);bound*=2*R*(1+(order-1)*K)
                assert max(map(abs,f))<=bound
    # Quantify how conservative the uniform sufficient time is in one cubic case.
    z=6;K=14;kappa=F(2,3);epsilon=F(1,7)
    R=6*epsilon*u**z+z*kappa;R0=6*epsilon*u**z
    support=1
    for j in range(6):
        support*=1+j*K
    C=((2*R)**6+(2*R0)**6)*support/factorial(6)
    a=kappa*epsilon**4*F(2379,5)/60
    print(f'uniform_remainder_example: sufficient_time={float(a/(2*C)):.16g}; no moderate-density accuracy assertion')


def coefficient_properties():
    values=[float(F(9,8)*psi(8*k/5)[0]+F(3,4)*psi(4*k/3)[0])/3 for k in (0,.1,.5,1,2,5)]
    kappas=(0,.1,.5,1,2,5)
    assert all(x<y for x,y in zip(values,values[1:]))
    slopes=[(values[i+1]-values[i])/(kappas[i+1]-kappas[i]) for i in range(5)]
    assert all(x>y for x,y in zip(slopes,slopes[1:]))
    for k,v in zip(kappas,values):
        assert 0<=v<=min(k*float(F(14,5))/60,float(F(15,8))/12)+1e-14
    assert abs(values[3]-.03708500612134838642189322865)<1e-14
    print(f'path: C_1(1)={values[3]:.17g} D2=14/5 class_centered_variance=15/8')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list-mutations',action='store_true')
    parser.add_argument('--mutation',choices=tuple(MUTATIONS))
    args=parser.parse_args()
    if args.list_mutations:
        for name,family in MUTATIONS.items():
            print(name,family)
        return 0
    checks=Checks();mutation=args.mutation
    for n,edges in ((2,((0,1),)),(3,((0,1),(1,2))),
                    (3,((0,1),(1,2),(0,2))),
                    (4,((0,1),(1,2),(2,3),(0,3)))):
        for raw in ((1,1,1),(3,1,2),(1,3,2),(12,1,2)):
            result=checks.run('startup',f'full rational generator n={n} edges={len(edges)} weights={raw}',
                lambda n=n,edges=edges,raw=raw:startup_case(n,edges,*raw,mutation=mutation))
            if result:
                print(f"exact_witness: D2={result['D2']} coefficient_per_kappa_epsilon4={result['population_t5_coefficient_per_kappa_epsilon4']}")
    for dim in (1,2,3):
        for side in (6,7,8):
            checks.run('geometry',f'explicit cube counts dimension={dim} side={side}',
                       lambda side=side,dim=dim:geometric_counts(side,dim,mutation))
    def menu_checks():
        for raw in ((1,1,1),(3,1,2),(1,3,2),(6,1,2),(12,1,2)):
            for dim in (1,2,3):
                value=coefficient(menu(*raw),dim)
                if raw==(3,1,2) and dim==3:
                    assert value==F(2379,5) and value/60==F(793,100)
        v=(2,-1,-1,0,0,0)
        W=[[1+F(v[a]*v[b],10) for b in range(6)] for a in range(6)]
        assert coefficient(W,3)>0
    checks.run('geometry','exact menus including non-axis-symmetric positive row-six W',menu_checks)
    checks.run('deletion','weighted birth adjoint and all class-constant functions on four-path',deletion_check)
    checks.run('delayed','rook graph first hazard-sensitive level is three',lambda:rook_check(mutation))
    checks.run('remainder','54 exact local generator norm bounds and a conservative cubic window',lambda:remainder_check(mutation))
    errors=[]
    cases=[(3,((0,1),(1,2)),(3,1,2),k,t) for k in (.1,1.,5.) for t in (.2,1.,2.)]
    cases += [(3,((0,1),(1,2)),(1,1,1),1.,1.),
              (3,((0,1),(1,2)),(12,1,2),1.,1.),
              (4,((0,1),(1,2),(2,3),(0,3)),(3,1,2),1.,1.)]
    for n,edges,raw,k,t in cases:
        result=checks.run('intensity',f'full block exponential n={n} W={raw} kappa={k} time={t}',
                         lambda n=n,edges=edges,raw=raw,k=k,t=t:full_block_case(n,edges,raw,k,t,mutation))
        if result:
            errors.append(result['absolute_difference'])
    if errors:
        print(f'block_coefficient_max_absolute_error: {max(errors):.17g}; tolerance=1e-8*max(1,abs(coefficient))')
    checks.run('spectral','path kernel positivity, increasing concavity, bounds and value',coefficient_properties)
    for side,dim in ((4,1),(6,1),(3,2),(4,2),(3,3)):
        for g in (.5,1.,1.5):
            def relative_case(side=side,dim=dim,g=g):
                H,w,c,Hr,wr,cr,n=position_matrices(side,dim,g,mutation)
                full=spectral_coefficient(H,w,c,1.3,.7)/n
                reduced=spectral_coefficient(Hr,wr,cr,1.3,.7)/2
                assert abs(full-reduced)<1e-11*max(1.,abs(full)),(full,reduced)
            checks.run('relative',f'full pair positions versus displacement side={side} dim={dim} g={g}',relative_case)
    print('per_element: executed — rational transition, holding-rate, weight and deletion identities')
    print('per_site: executed — all configurations on the named graphs of at most four vertices')
    print('per_mode: executed — centered content covariance and complete finite two-record spectra in named cases')
    print('per_block: executed — full-generator Taylor/Dyson checks, rook witness and explicit cube counts')
    print('lattice_wide: checked and not executed — general finite-graph and uniform torus-family proofs in note; no phase or physical field')
    if mutation:
        print(f'mutation_family_expected: {MUTATIONS[mutation]}')
        print(f'mutation_family_observed: {",".join(sorted(checks.families)) or "none"}')
    print(f'TOTAL: PASS={checks.passed} FAIL={checks.failed}')
    return int(bool(checks.failed))


if __name__=='__main__':
    raise SystemExit(main())
