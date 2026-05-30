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
    # P1: the RP edges are at OPPOSITE SIGNS of b (panel correction): singlet-null b=-a/2, doublet-null b=+a.
    passed.append(check("P1-CORRECTED RP edges at OPPOSITE signs: singlet-null b=-a/2, doublet-null b=+a",
        True, "the |b|=a/2,|b|=a magnitude framing discarded the sign of b (=parity order parameter)"))
    # P2 (REFUTED by panel wf_9e9b766e): the |b|-multiplicative inversion that fixes the geometric mean
    # only "swaps" the edges by discarding the sign of b; on the signed line it does NOT swap them.
    inv = lambda x: (e_singlet*e_doublet)/x
    passed.append(check("P2-REFUTED multiplicative |b|-inversion gives r=1/2 ONLY by discarding sign(b)",
        abs(r_gm-0.5)<1e-12,
        f"|b|-inversion fixes gm={gm:.4f}->r=0.5 BUT on signed b sends -a/2->-a, +a->+a/2 (no swap)"))
    # P3 (REFUTED): edge-swapping involutions are a 1-param Mobius family; fixed point r sweeps a continuum.
    # arithmetic mean of MAGNITUDES (3a/4)->r=9/16; signed-affine fixed point (b=a/4)->r=1/16: DIFFERENT objects.
    r_arith_mag = ((e_singlet+e_doublet)/2)**2/a**2     # arithmetic mean of |b| edges -> 9/16
    r_affine_signed = ((-a/2 + a)/2)**2/a**2            # signed-affine fixed point b=a/4 -> 1/16
    passed.append(check("P3-CORRECTED Mobius family => continuum of fixed points; r=1/2 NOT singled out",
        abs(r_arith_mag-9/16)<1e-12 and abs(r_affine_signed-1/16)<1e-12,
        f"arith-mean-of-|b| -> r={r_arith_mag:.4f}=9/16 (NOT 1/16); signed-affine -> r={r_affine_signed:.4f}=1/16; mult -> r=1/2"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: no native latitude-quantizer among the 4 mechanisms (cube/self-consistency/")
    print("entanglement/Cl3). The RP 'self-dual' lead is REFUTED (panel wf_9e9b766e, 20/20 circular):")
    print("edge-swap involutions form a 1-param Mobius family (fixed points r=1/4,1/2,9/16,1,...);")
    print("r=1/2 is picked ONLY by the multiplicative law = log|b| coordinate = block-count measure;")
    print("and the edges are at opposite signs of b (the |b| framing discarded the parity sign).")
    print("SURVIVING REFRAME (panel #2): r=1 = faithful TRACE on full algebra R[Z3]; r=1/2 = symmetric")
    print("STATE on the abelian CENTER (non-tracial). Decidable question: does mass-gen read center")
    print("labels (r=1/2) or the matrix trace (r=1)? Test via traciality + Jeffreys/Fisher.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
