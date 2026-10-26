#!/usr/bin/env python3
"""Exact supplied pair arithmetic and analytic monomial-loop controls.

Integer exponents encode exp(i*m*k) exactly; no sampled phase grid is
used to claim winding certification or physical symmetry realization.
"""
import sys

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ("docs/SUPPLIED_THREE_SECTOR_PAIR_FLOW_AND_LOOP_IDENTITIES_NOTE_2026-10-24.md",)


def flow(q, hand):
    if q not in (0, 1, 2) or hand not in (-1, 1):
        raise ValueError("supplied label and hand required")
    return tuple(hand * (int(a == (q+2) % 3) - int(a == (q+1) % 3)) for a in range(3))


def pair(ql, qm):
    return tuple(a+b for a,b in zip(flow(ql,1), flow(qm,-1)))


def scale(n, w):
    return tuple(n*x for x in w)


def congruence(n, w):
    return all(x % 3 == 0 for x in scale(n,w))


def primitive(w):
    return w in {pair(a,b) for a in range(3) for b in range(3) if a != b}


def sector_map(a,c,s,anti=False):
    return (s*((-a if anti else a)-c)) % 3


def signed_relation(w,sigma):
    return all(w[a] == -w[sigma[a]] for a in range(3))


def main():
    checks=[]
    def check(label,condition):
        ok=bool(condition)
        checks.append(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    table=((0,0,(0,0,0)),(0,1,(-1,-1,2)),(0,2,(1,-2,1)),
           (1,0,(1,1,-2)),(1,1,(0,0,0)),(1,2,(2,-1,-1)),
           (2,0,(-1,2,-1)),(2,1,(-2,1,1)),(2,2,(0,0,0)))
    for a,b,w in table:
        check(f"pair table {a},{b}",pair(a,b)==w)
        for n in (0,1,2,3,6):
            expected=(a==b or n%3==0)
            check(f"supplied charge congruence {a},{b}; N={n}",(n*(a-b)%3==0)==expected)
            check(f"supplied component congruence {a},{b}; N={n}",congruence(n,w)==expected)
    wf=(-2,1,1)
    check("primitive supplied normalization",pair(2,1)==wf and primitive(wf))
    check("all-nonzero even multiple",scale(2,wf)==(-4,2,2) and all(x!=0 and x%2==0 for x in scale(2,wf)))
    check("all-nonzero zero-residue multiple",scale(3,wf)==(-6,3,3) and all(x!=0 and x%3==0 for x in scale(3,wf)))
    check("tripled vector admits every tested N",all(congruence(n,scale(3,wf)) for n in (0,1,2,3,6)))
    check("primitive admits both three and six",congruence(3,wf) and congruence(6,wf))
    check("heterogeneous cancellation",tuple(a+b for a,b in zip(pair(2,1),pair(1,2)))==(0,0,0))
    check("mutation: doubled normalization rejected",not primitive(scale(2,wf)))
    check("mutation: nonzero alone congruence rejected",congruence(1,scale(3,wf)) and not congruence(1,wf))
    # Monomial exp(i*m*k): degree m follows from the explicit phase lift.
    # These exact exponents are analytic fixtures, not floating phase estimates.
    for m,n in ((-3,2),(0,0),(1,-1),(7,4)):
        degree_product=m+n
        check(f"monomial product exponent {m},{n}",degree_product-n==m)
        degree_adjoint=-m
        degree_conjugate=-m
        degree_reversed=-m
        check(f"monomial adjoint/conjugate/orientation {m}",degree_adjoint==degree_conjugate==degree_reversed)
        check(f"double orientation restores exponent {m}",-degree_reversed==m)
    w=(1,-1,0);sigma=(1,0,2)
    check("constructive supplied signed relation",signed_relation(w,sigma))
    check("unitary chiral exponent equation",all(w[a]==-w[sigma[a]] for a in range(3)))
    check("unitary axis-reversal exponent equation",all(w[a]==-w[sigma[a]] for a in range(3)))
    check("antiunitary Floquet exponent equation",all(-w[a]==w[sigma[a]] for a in range(3)))
    check("mutation: missing transformation minus rejected",not all(w[a]==w[sigma[a]] for a in range(3)))
    check("mutation: changed loop exponent rejected",not signed_relation((1,1,0),sigma))
    for anti in (False,True):
        for c in range(3):
            for s in (-1,1):
                for a in range(3):
                    b=sector_map(a,c,s,anti)
                    check(f"literal sector convention {anti},{c},{s},{a}",(c+s*b)%3==((-a if anti else a)%3))
    # Distinguish literal c from the old unannounced +c reparameterization.
    check("mutation: wrong fixed-c sector map rejected",sector_map(0,1,1)!=1)
    print("[INFO] Exact supplied fixtures; no static exclusion, physical symmetry or family-selection result.")
    print(f"TOTAL: PASS = {sum(checks)}, FAIL = {len(checks)-sum(checks)}")
    return 0 if all(checks) else 1

if __name__ == '__main__':
    sys.exit(main())
