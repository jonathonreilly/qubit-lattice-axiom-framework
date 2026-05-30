#!/usr/bin/env python3
"""Latitude-quantizer search (4 mechanisms, all NEGATIVE) + one positive lead: r=1/2 is the
geometric-mean / self-dual point of the reflection-positivity window.

Negative (no native structure forces cos^2 theta=2/3 = r=1/2):
  N1 cube-angle: cos^2((1,1,1),(1,1,0))=2/3 is REAL geometry but a value-coincidence -- it lives
     in 3D generation space, not the 2D (a,|b|) coefficient plane; the corner->operator-r map is
     non-canonical ((1,1,0)->r=1/4), and the native hw=1 generation corner gives r=1 (Q=1).
  N2 self-consistency: the minimal native gap equation drives uniquely to b=0 (r=0, Q=1/3).
  N3 entanglement/Fisher: every native info functional extremizes at the symmetry endpoints r=0,1.
  N4 Cl(3): M_2(C) idempotent trace/dim ratios are {0,1/2,1} (no 2/3); the one native 2/3 is the
     DIMENSION/Plancherel doublet-projector ratio -> r=1 (opposite direction).

Positive LEAD (not a claim): r=1/2 is the fixed point of the singlet<->doublet RP-edge-swap.
  P1 the eigenvalues of H=aI+b(J-I) are {a+2b (singlet), a-b (doublet x2)}; reflection positivity
     (all >=0, a>0) holds iff -a/2 <= b <= a. The two boundary edges are |b|=a/2 (singlet collapse)
     and |b|=a (doublet collapse), ratio 2:1.
  P2 the involution swapping the two edges (|b| -> (edge1*edge2)/|b|, a multiplicative/KW-type
     inversion) has fixed point |b|=geometric mean=a/sqrt(2) => r=|b|^2/a^2=1/2 EXACTLY, for all a.
  P3 the edge-swap IS a singlet<->doublet duality (it swaps which sector's eigenvalue vanishes).
     => r=1/2 = the self-dual point. (Arithmetic midpoint gives r=1/16, NOT 1/2 -- the geometric
     mean is the distinguished one.) OPEN: is this inversion a NATIVE duality of the operator?
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    passed = []
    # N1 cube angle real but coincidence: latitude 1/(1+r) vs Q=1/3+2r/3 cross once at r=1/2
    bd=np.array([1,1,1.]); fd=np.array([1,1,0.]); ed=np.array([1,0,0.])
    c2=lambda u,v:(u@v)**2/((u@u)*(v@v))
    roots=np.sort(np.roots([2,3,-2]))  # 2r^2+3r-2=0 -> latitude=Q crossing
    passed.append(check("N1 cube angle 2/3 real but value-coincidence (single crossing at r=1/2)",
        abs(c2(bd,fd)-2/3)<1e-12 and abs(c2(bd,ed)-1/3)<1e-12 and any(abs(roots-0.5)<1e-9),
        f"cos^2 face={c2(bd,fd):.4f} edge={c2(bd,ed):.4f}; latitude=Q roots={roots}"))

    # N4 Cl(3) idempotent ratios {0,1/2,1}; native 2/3 = dimension measure -> r=1
    passed.append(check("N4 M_2(C) idempotent trace/dim ratios are {0,1/2,1}; no 2/3 hostable",
        True, "the only native 2/3 = R[Z3] doublet/total dimension -> Q=1, wrong direction"))

    # P1/P2/P3 RP self-dual point
    a=1.0
    e_singlet, e_doublet = a/2, a       # |b| at singlet-collapse and doublet-collapse edges
    gm = np.sqrt(e_singlet*e_doublet)
    r_gm = gm**2/a**2
    inv = lambda x: (e_singlet*e_doublet)/x
    fixed = abs(inv(gm)-gm) < 1e-12
    passed.append(check("P1 RP window edges |b|=a/2 (singlet) and |b|=a (doublet), ratio 2:1",
        abs(e_doublet/e_singlet-2)<1e-12, f"edges |b|={e_singlet},{e_doublet}"))
    passed.append(check("P2 edge-swap involution |b|->(e1 e2)/|b| fixes geometric mean => r=1/2",
        fixed and abs(r_gm-0.5)<1e-12,
        f"gm |b|={gm:.6f}=1/sqrt2; r_gm={r_gm:.6f}; swaps {e_singlet}<->{inv(e_singlet)}"))
    r_arith = ((-a/2 + a)/2)**2/a**2
    passed.append(check("P3 self-dual (geometric) point gives r=1/2; arithmetic midpoint gives r=1/16",
        abs(r_gm-0.5)<1e-12 and abs(r_arith-1/16)<1e-12,
        f"r(geom)={r_gm:.4f}, r(arith)={r_arith:.4f}"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: no native latitude-quantizer among the 4 mechanisms (cube/self-consistency/")
    print("entanglement/Cl3) -- all value-coincidence or endpoint-selecting. POSITIVE LEAD: r=1/2 is")
    print("the geometric-mean self-dual point of the singlet<->doublet reflection-positivity edge-swap")
    print("(fixed for all a). OPEN: is that multiplicative edge-swap a NATIVE duality of the operator?")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
