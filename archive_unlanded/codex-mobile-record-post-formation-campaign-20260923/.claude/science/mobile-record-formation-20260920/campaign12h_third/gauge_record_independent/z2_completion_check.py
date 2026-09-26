#!/usr/bin/env python3
"""Exact C4 control including all physical matter/gauge coherences."""
from pathlib import Path
import hashlib
import json
import sys
import time
import sympy as s
from sympy.polys.domains import QQ_I

HERE = Path(__file__).resolve().parent
EDGES = [(0,1),(1,2),(2,3),(3,0)]
V = 4
N = 16  # Every gauge-Z configuration fixes its physical matter occupation.


def occupation(z):
    out = [0]*V
    for e,(x,y) in enumerate(EDGES):
        if (z>>e)&1:
            out[x] ^= 1
            out[y] ^= 1
    return out


def model(active_births, d=1):
    H = s.zeros(N)
    births = []
    ns = [s.diag(*[occupation(z)[x] for z in range(N)]) for x in range(V)]
    for e,(x,y) in enumerate(EDGES):
        J = s.zeros(N)
        for z in range(N):
            occ = occupation(z)
            zz = z^(1<<e)
            if occ[x] != occ[y]:
                H[zz,z] += 1
                assert occupation(zz)[x] == occ[y]
                assert occupation(zz)[y] == occ[x]
            if e in active_births and occ[x] == occ[y] == 0:
                J[zz,z] = 1
                assert occupation(zz)[x] == occupation(zz)[y] == 1
        if e in active_births:
            assert J.T*J == (s.eye(N)-ns[x])*(s.eye(N)-ns[y])
            births.append(J)
    I = s.eye(N)
    count = sum(ns, s.zeros(N))
    assert H.T == H and H*count == count*H
    L = -s.I*(s.kronecker_product(I,H)-s.kronecker_product(H.T,I))
    for J in births:
        assert count*J-J*count == 2*J
        R = J.T*J
        L += s.kronecker_product(J,J)-(s.kronecker_product(I,R)+s.kronecker_product(R.T,I))/2
    for n in ns:
        L += d*(s.kronecker_product(n,n)-(s.kronecker_product(I,n)+s.kronecker_product(n.T,I))/2)
    assert I.vec().T*L == s.zeros(1,N*N)
    return H,L,count


def main():
    started = time.monotonic()
    basis = [{'gauge_negative_mask':z,'matter_occupation':occupation(z)} for z in range(N)]
    assert all(sum(r['matter_occupation'])%2 == 0 for r in basis)
    full = [z for z in range(N) if all(occupation(z))]
    assert full == [5,10]
    controls=[]
    for name,active in [('all_birth_edges',range(4)),('one_birth_edge',[0])]:
        H,L,count = model(active)
        for a in full:
            for b in full:
                X = s.zeros(N);X[a,b]=1
                assert L*X.vec() == s.zeros(N*N,1)
        nullity = L.rows-L.to_DM().convert_to(QQ_I).rank()
        assert nullity == 4
        transient = [z for z in range(N) if z not in full]
        indices = [r+N*c for c in transient for r in transient]
        K = L.extract(indices,indices)
        inv = K.inv(method='DM')
        q = len(transient)
        vt = -inv.conjugate().T*s.eye(q).vec()
        T = s.Matrix(q,q,lambda r,c:vt[r+q*c]).applyfunc(s.expand)
        assert (T-T.conjugate().T).applyfunc(s.expand)==s.zeros(q)
        assert (K.conjugate().T*T.vec()+s.eye(q).vec()).applyfunc(s.expand)==s.zeros(q*q,1)
        # Exact positivity by Sylvester's criterion on the 14-dimensional
        # physical transient Hilbert space, retaining every gauge coherence.
        minors=[s.factor(T[:j,:j].det(method='domain-ge')) for j in range(1,q+1)]
        assert all(x>0 for x in minors)
        controls.append({'case':name,'physical_Hilbert_dimension':N,
                         'full_occupation_Hilbert_dimension':len(full),
                         'full_Liouville_dimension':N*N,
                         'stationary_operator_nullity':nullity,
                         'transient_Hilbert_dimension':q,
                         'all_full_sector_coherences_stationary':True,
                         'mean_from_all_vacancies_all_Z_positive':str(T[transient.index(0),transient.index(0)]),
                         'positive_mean_operator_principal_minors':list(map(str,minors))})
        print(name,'nullity',nullity,'mean',controls[-1]['mean_from_all_vacancies_all_Z_positive'],flush=True)
    result={'boundary':'Independent pre-author-source finite gauge control.',
            'physical_basis':basis,'controls':controls,
            'rates':'all nonzero couplings and monitoring rates are 1; each listed birth edge has beta=1; H0=0',
            'method':'Eliminate the Gx=+1 constraints exactly, then construct the complete physical Liouvillian. No gauge coherence is omitted.',
            'runtime_seconds':time.monotonic()-started,
            'python':sys.version,'sympy':s.__version__}
    (HERE/'Z2_COMPLETION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
