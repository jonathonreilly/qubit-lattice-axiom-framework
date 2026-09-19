#!/usr/bin/env python3
"""J:derive:formation-in-3plus1:a5 (worker w-macbookpro90c72-jd7c3, grok-4.6).

Route distinct from grok a1/a4 (linear dichotomy / 1/r Green) and a2/a6
(MF 3/4, Hessian envelope): the backward 4-predecessor kernel is a DAG,
phi is not identically real, and 1/(1-phi) is not a real multiple of
1/(1-|phi|^2). Contrast: the control's symmetric 7-stencil is real-phi.
"""
from __future__ import annotations

import sympy as sp

FAIL, PASS = [], []


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


def e_dag():
    # Record at x formed from x-e_j, j=1..4. Predecessors of y=x-e_1 never include x.
    def preds(x):
        out = []
        for j in range(4):
            y = list(x)
            y[j] -= 1
            out.append(tuple(y))
        return out

    x = (0, 0, 0, 0)
    pset = set(preds(x))
    ok("U.1a four distinct predecessors", len(pset) == 4)
    rev_hits = [x in preds(y) for y in pset]
    ok("U.1b no reverse edges (DAG: x not a predecessor of any predecessor)", not any(rev_hits))
    # every formation edge decreases level by 1
    lev = lambda z: sum(z)
    ok(
        "U.1c every predecessor has level(x)-1",
        all(lev(y) == lev(x) - 1 for y in pset),
    )


def e_phi():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2) + sp.exp(sp.I * k3)) / 4
    abssq = sp.simplify(sp.expand_complex(sp.conjugate(phi) * phi))
    ok("F.1 |phi|(0)=1", sp.simplify(abssq.subs({k1: 0, k2: 0, k3: 0}) - 1) == 0)

    ident = (
        2
        + sp.cos(k1)
        + sp.cos(k2)
        + sp.cos(k3)
        + sp.cos(k1 - k2)
        + sp.cos(k1 - k3)
        + sp.cos(k2 - k3)
    ) / 8
    ok("I.1 cosine identity for |phi|^2", sp.simplify(abssq - ident) == 0)

    ph = phi.subs({k1: sp.pi / 2, k2: 0, k3: 0})
    ok("F.2 phi is not real at k=(pi/2,0,0)", sp.simplify(sp.im(ph)) != 0)
    ok("F.5 phi(pi/2,0,0)=(3+i)/4", sp.simplify(ph - (3 + sp.I) / 4) == 0)

    R = 1 / (1 - ph)
    C = 1 / (1 - sp.simplify(sp.expand_complex(sp.conjugate(ph) * ph)))
    ok("F.3 1/(1-phi) is not real at that mode", sp.simplify(sp.im(R)) != 0)
    ok(
        "F.4 1/(1-|phi|^2) is real and differs from 1/(1-phi)",
        sp.simplify(sp.im(C)) == 0 and sp.simplify(R - C) != 0,
        f"R={sp.simplify(R)} C={sp.simplify(C)}",
    )
    ok(
        "F.6 C=8/3, R=2(1+i)",
        sp.simplify(C - sp.Rational(8, 3)) == 0
        and sp.simplify(R - 2 * (1 + sp.I)) == 0,
    )
    ratio = sp.simplify(R / C)
    ok(
        "F.7 R/C=(3/4)(1+i) is not real",
        sp.simplify(ratio - sp.Rational(3, 4) * (1 + sp.I)) == 0
        and sp.simplify(sp.im(ratio)) != 0,
        f"R/C={ratio}",
    )
    # no real lambda with R = lambda C
    ok("F.8 Im(R/C) != 0 so R is not a real multiple of C", sp.simplify(sp.im(ratio)) != 0)


def e_drift_ir():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2) + sp.exp(sp.I * k3)) / 4
    dphi = [sp.diff(phi, kj).subs({k1: 0, k2: 0, k3: 0}) for kj in (k1, k2, k3)]
    ok("D.1 d phi/d k_j |0 = i/4 (drift (1,1,1)/4)", dphi == [sp.I / 4] * 3, str(dphi))

    steps = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    w = sp.Rational(1, 4)
    centroid = tuple(sum(s[j] * w for s in steps) for j in range(3))
    ok(
        "D.2 centroid of {0,e1,e2,e3} with equal weights is (1,1,1)/4",
        centroid == (sp.Rational(1, 4),) * 3,
        str(centroid),
    )

    abssq = sp.simplify(sp.expand_complex(sp.conjugate(phi) * phi))
    gC = [sp.diff(1 - abssq, kj).subs({k1: 0, k2: 0, k3: 0}) for kj in (k1, k2, k3)]
    gR = [sp.diff(1 - phi, kj).subs({k1: 0, k2: 0, k3: 0}) for kj in (k1, k2, k3)]
    ok("I.2a grad(1-|phi|^2)|0 = 0", all(sp.simplify(g) == 0 for g in gC), str(gC))
    ok(
        "I.2b grad(1-phi)|0 = -i(1,1,1)/4 != 0",
        all(sp.simplify(g + sp.I / 4) == 0 for g in gR),
        str(gR),
    )


def e_symmetric_contrast():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi_s = (1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))) / 7
    ok("S.1 symmetric 7-stencil phi is real (Im identically 0)", sp.im(phi_s) == 0)
    ph = phi_s.subs({k1: sp.pi / 2, k2: 0, k3: 0})
    ok("S.2 phi_s(pi/2,0,0)=5/7", sp.simplify(ph - sp.Rational(5, 7)) == 0)
    R = 1 / (1 - ph)
    C = 1 / (1 - ph**2)
    ratio = sp.simplify(R / C)
    ok(
        "S.3 R_s=7/2, C_s=49/24, R/C=12/7=1+phi (real multiple)",
        sp.simplify(R - sp.Rational(7, 2)) == 0
        and sp.simplify(C - sp.Rational(49, 24)) == 0
        and sp.simplify(ratio - sp.Rational(12, 7)) == 0
        and sp.simplify(ratio - (1 + ph)) == 0
        and sp.simplify(sp.im(ratio)) == 0,
        f"R={R} C={C} R/C={ratio}",
    )


def main():
    e_dag()
    e_phi()
    e_drift_ir()
    e_symmetric_contrast()
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: PARTIAL the 3+1 backward 4-predecessor kernel is a DAG (not undirected), "
        "so phi is not identically real and fluctuation-dissipation fails: at k=(pi/2,0,0), "
        "phi=(3+i)/4, |phi|^2=5/8, the static response 1/(1-phi)=2(1+i) is not a real multiple "
        "of the covariance 1/(1-|phi|^2)=8/3 (R/C=(3/4)(1+i)). Drift is (1,1,1)/4; "
        "grad(1-phi)|0 != 0 while grad(1-|phi|^2)|0 = 0. Contrast: the control's symmetric "
        "7-stencil at the same mode has real phi=5/7 and R/C=12/7=1+phi. Sphere LRO is not "
        "proved. This is not the linear dichotomy/Green of grok a1/a4 or the MF 3/4 envelope of a6."
    )
    print(
        "HIT: 3+1 backward formation is irreversible; at mode (pi/2,0,0) phi=(3+i)/4, "
        "covariance symbol 8/3 versus causal response 2(1+i), ratio (3/4)(1+i) not real. "
        "A gravity node that reads the covariance sees a 3d Green function at small k; "
        "one that reads the linear response sees a complex directed kernel with drift "
        "(1,1,1)/4 per level. Symmetric 7-stencil contrast: R/C real. Sphere LRO not proved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
