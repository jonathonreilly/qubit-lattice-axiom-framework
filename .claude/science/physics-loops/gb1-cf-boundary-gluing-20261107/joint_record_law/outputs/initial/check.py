#!/usr/bin/env python3
"""Exact finite diagnostics; mathematical proofs and assumptions live in RESULT.md."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import argparse
import hashlib
import json
import resource
import time

START = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (45, 50))


def guard():
    assert time.monotonic() - START < 50, 'wall budget'
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256*1024*1024, 'RSS budget (macOS bytes)'


class Q:
    """Q(i,sqrt(2)), coefficients of 1,sqrt(2),i,i*sqrt(2)."""
    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = (a.v if isinstance(a, Q) else tuple(map(F, (a,b,c,d))))

    def __add__(self, other):
        other = Q(other)
        return Q(*(x+y for x,y in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return Q(*(-x for x in self.v))

    def __sub__(self, other):
        return self + (-Q(other))

    def __rsub__(self, other):
        return Q(other) - self

    def __mul__(self, other):
        other = Q(other)
        out = [F(0)]*4
        for j,x in enumerate(self.v):
            if not x:
                continue
            for k,y in enumerate(other.v):
                if not y:
                    continue
                ie, re = j//2+k//2, j%2+k%2
                out[(ie%2)*2+re%2] += x*y*((-1)**(ie//2))*(2**(re//2))
        return Q(*out)

    __rmul__ = __mul__

    def __truediv__(self, rational):
        return self * F(1, rational)

    def __eq__(self, other):
        return self.v == Q(other).v

    def __hash__(self):
        return hash(self.v)

    def conj(self):
        a,b,c,d = self.v
        return Q(a,b,-c,-d)

    def nonnegative(self):
        a,b,c,d = self.v
        assert c == d == 0, 'expected real number'
        if a >= 0 and b >= 0:
            return True
        if a <= 0 and b <= 0:
            return a == b == 0
        return a*a >= 2*b*b if a >= 0 else 2*b*b >= a*a

    def serial(self):
        return [str(x) for x in self.v]


def matrix(rows):
    return tuple(tuple(Q(x) for x in r) for r in rows)


def ident(n):
    return matrix([[int(j==k) for k in range(n)] for j in range(n)])


def add(a,b):
    return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))


def scale(a,c):
    return tuple(tuple(c*x for x in row) for row in a)


def mul(a,b):
    return tuple(tuple(sum((a[j][k]*b[k][l] for k in range(len(b))),Q())
                       for l in range(len(b[0]))) for j in range(len(a)))


def adj(a):
    return tuple(tuple(a[j][k].conj() for j in range(len(a))) for k in range(len(a[0])))


def kron(a,b):
    return tuple(tuple(x*y for x in ra for y in rb) for ra in a for rb in b)


def tr(a):
    return sum((a[j][j] for j in range(len(a))), Q())


I = ident(2)
X = matrix([[0,1],[1,0]])
Y = matrix([[0,Q(0,0,-1)],[Q(0,0,1),0]])
Z = matrix([[1,0],[0,-1]])
R = Q(0,F(1,2))  # 1/sqrt(2)
PAULI = (X,Y,Z)


def direction(n):
    return add(add(scale(X,n[0]),scale(Y,n[1])),scale(Z,n[2]))


def projector(n,a):
    return scale(add(I,scale(direction(n),a)),F(1,2))


def local_isometry(n):
    ps = [projector(n,a) for a in (1,-1)]
    return tuple(ps[k][j] for j in range(2) for k in range(2))


def joint(rho,n,m):
    weights = {}
    for a,b in product((1,-1),repeat=2):
        k = kron(projector(n,a),projector(m,b))
        weights[a,b] = tr(mul(mul(k,rho),adj(k)))
    return weights


def dot(n,m):
    return sum((x*y for x,y in zip(n,m)),Q())


def corr(weights):
    return sum((a*b*w for (a,b),w in weights.items()),Q())


def site_add(a,b):
    return tuple(x+y for x,y in zip(a,b))


NEIGHBORS = tuple(tuple(s if j==k else 0 for j in range(3))
                  for k in range(3) for s in (-1,1))
T = scale(I,100)
SOURCE = scale(I,200)


def setting(c):
    n = add(c,scale(I,-2))
    return tr(n)==0 and mul(n,n)==I


def menu(records,site):
    values = [records[site_add(site,d)] for d in NEIGHBORS if site_add(site,d) in records]
    if T in values and sum(setting(c) for c in values)==1:
        return {I:Q(F(1,2)),scale(I,-1):Q(F(1,2))}
    if not values:
        return {scale(I,0):Q(1)}
    out = {}
    for c in values:
        out[c] = out.get(c,Q()) + Q(F(1,len(values)))
    return out


def prepared(n,m,L=6):
    records = {(0,0,-4):SOURCE,(0,0,-5):SOURCE}
    targets = ((0,0,0),(0,0,L))
    for c,v in zip(targets,(n,m)):
        for offset in ((1,0,0),(2,0,0)):
            records[site_add(c,offset)] = T
        for offset in ((0,1,0),(0,2,0)):
            records[site_add(c,offset)] = add(scale(I,2),direction(v))
    return records,targets


def targets_from_records(records):
    candidates = {site_add(s,d) for s in records for d in NEIGHBORS}
    found = set()
    for c in candidates:
        for u,v in product(NEIGHBORS,repeat=2):
            if sum(x*y for x,y in zip(u,v)) != 0:
                continue
            t1,t2 = site_add(c,u),site_add(c,tuple(2*x for x in u))
            x1,x2 = site_add(c,v),site_add(c,tuple(2*x for x in v))
            if records.get(t1)==T and records.get(t2)==T and x1 in records:
                if setting(records[x1]) and records.get(x2)==records[x1]:
                    found.add(c)
    return found


def supported(records):
    for s,c in records.items():
        assert menu(records,s).get(c,Q()) != 0, ('record support',s)
    return len(records)


def rotations():
    for p in permutations(range(3)):
        parity = (-1)**sum(p[j]>p[k] for j in range(3) for k in range(j+1,3))
        for signs in product((-1,1),repeat=3):
            if parity*signs[0]*signs[1]*signs[2]==1:
                yield lambda s,p=p,signs=signs: tuple(signs[j]*s[p[j]]+11*(j+1) for j in range(3))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fault',choices=['independent-draws','remote-setting','missing-buddy'])
    args = parser.parse_args()
    H = scale(add(X,Z),R)
    cnot = matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    psi = mul(mul(mul(kron(Z,I),cnot),kron(H,I)),matrix([[0],[1],[0],[0]]))
    rho = mul(psi,adj(psi))
    rho_formula = scale(add(ident(4),scale(sum_matrices([kron(p,p) for p in PAULI]),-1)),F(1,4))
    assert rho==rho_formula and mul(rho,rho)==rho and tr(rho)==1
    triplet = add(ident(4),scale(rho,-1))
    assert mul(triplet,triplet)==triplet and tr(triplet)==3 and tr(mul(rho,triplet))==0
    axes = [tuple(map(Q,n)) for n in [(1,0,0),(0,1,0),(0,0,1),
             (R,0,R),(-R,0,R),(F(3,5),0,F(4,5)),(F(2,3),F(2,3),F(1,3))]]
    support_count = branches = pairs = 0
    for n,m in product(axes,repeat=2):
        guard()
        assert dot(n,n)==dot(m,m)==1
        va,vb = local_isometry(n),local_isometry(m)
        assert mul(adj(va),va)==mul(adj(vb),vb)==I
        full = mul(kron(va,vb),psi)
        w = joint(rho,n,m)
        if args.fault=='independent-draws':
            w = {k:Q(F(1,4)) for k in w}
        assert sum(w.values(),Q())==1 and all(v.nonnegative() for v in w.values())
        records,targets = prepared(n,m)
        if args.fault=='missing-buddy':
            del records[(0,2,0)]
        support_count += supported(records)
        assert targets_from_records(records)==set(targets), 'target parser'
        for (a,b),weight in w.items():
            ia,ib = int(a==-1),int(b==-1)
            pointer = sum((full[((i*2+ia)*2+j)*2+ib][0].conj()*
                           full[((i*2+ia)*2+j)*2+ib][0] for i,j in product(range(2),repeat=2)),Q())
            assert weight==pointer, 'local pointer/joint record mismatch'
            assert weight==(1-a*b*dot(n,m))/4, 'effect/amplitude identity'
            ka,kb = kron(projector(n,a),I),kron(I,projector(m,b))
            assert mul(ka,kb)==mul(kb,ka)
            if weight!=0:
                post = dict(records)
                for s,value in zip(targets,(a,b)):
                    assert s not in post
                    post[s] = scale(I,value)
                assert all(post[s]==v for s,v in records.items())
                support_count += supported(post)
                branches += 1
        for a in (1,-1):
            assert sum((w[a,b] for b in (1,-1)),Q())==Q(F(1,2))
        for b in (1,-1):
            assert sum((w[a,b] for a in (1,-1)),Q())==Q(F(1,2))
        pairs += 1
    # All-state no-communication theorem is analytic. This product-state guard
    # detects a remote setting input hidden by the singlet's fair marginals.
    product_state = matrix([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    for m in axes:
        n = axes[2] if args.fault!='remote-setting' else m
        wa = joint(product_state,n,m)
        assert sum((wa[1,b] for b in (1,-1)),Q())==1, 'remote setting entered Alice instrument'
    records,targets = prepared(axes[2],axes[0],17)
    covariance = 0
    for transform in rotations():
        transformed = {transform(s):v for s,v in records.items()}
        assert targets_from_records(transformed)=={transform(s) for s in targets}
        for s in list(records)+list(targets):
            assert menu(transformed,transform(s))==menu(records,s)
        covariance += 1
    selected = [(axes[2],axes[3]),(axes[2],axes[4]),(axes[0],axes[3]),(axes[0],axes[4])]
    es = [corr(joint(rho,n,m)) for n,m in selected]
    signed = es[0]+es[1]+es[2]-es[3]
    assert signed==Q(0,-2)
    nonlinear = []
    for n,m in selected:
        t=dot(n,m);h=(3*t-t*t*t)/2
        nonlinear.append(-h)
    bad_score=nonlinear[0]+nonlinear[1]+nonlinear[2]-nonlinear[3]
    assert bad_score==Q(0,F(-5,2))
    same = joint(rho,axes[2],axes[2])
    conditional = [same[a,1]*2 for a in (1,-1)]
    assert conditional==[Q(0),Q(1)]
    base,targets=prepared(axes[2],axes[2])
    left,right=dict(base),dict(base)
    left[targets[0]]=I;right[targets[0]]=scale(I,-1)
    assert menu(left,targets[1])==menu(right,targets[1])
    assert menu(left,targets[1])[I]==Q(F(1,2))
    guard()
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'status':'exact finite diagnostics passed','arithmetic':'Q(i,sqrt(2))',
        'setting_pairs':pairs,'positive_atomic_branches':branches,'old_and_new_support_instances':support_count,
        'rotations_with_translation':covariance,'initial_records':10,'max_records':12,
        'CHSH_signed_coefficients':signed.serial(),'nonlinear_signed_coefficients':bad_score.serial(),
        'B_plus_conditioned_on_A_plus_minus':[x.serial() for x in conditional],
        'N5':{'per_element':'exact complex algebra and local pointer effects',
              'per_site':'complete six-neighbor menus; permanent support',
              'per_mode':'no propagating mode or causal timing computation',
              'per_block':'two-wing instruments and one atomic record pair',
              'lattice_wide':'finite translated/rotated patches only; physical realization open'},
        'elapsed_seconds':time.monotonic()-START,
        'max_rss_host_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))


def sum_matrices(items):
    out = scale(items[0],0)
    for item in items:
        out = add(out,item)
    return out


if __name__=='__main__':
    main()
