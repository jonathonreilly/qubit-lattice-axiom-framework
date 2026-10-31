#!/usr/bin/env python3
"""tw1 -- exact feasibility of the decoupled exponent system of 𝔐 / BFT-1.

Criteria pre-registered in checks/tw1_criteria.md BEFORE this file was written.
Exact rational arithmetic only (fractions.Fraction). No floating point. No BLAS.

Variables (all exponents of L, per level, in OWN units):
    tc  = theta_w^c   curvature decay / 𝔐's curvature displacement weight
    tr  = theta_w^r   residual (soft-fluctuation) decay / 𝔐's residual leg
    tA  = theta_A     potential decay (the gauge representative)
    th  = theta       source weight, omega_l = L^{theta(k-l)}   (RTARGET §33, SF, BFT_A)
    al  = alpha       Campanato/Hoelder exponent

Constraints, each tagged with the file:line that imposes it (see criteria).
"""
from fractions import Fraction as F
from itertools import product

# --------------------------------------------------------------------------
# constraint encoding: a constraint is (name, predicate, kind) with
# kind in {"PROVEN","ARGUED","OPEN-conditional"} for reporting only.
# --------------------------------------------------------------------------

def wilson_ok(d, tc, tA):
    "NORMS l.650: level-0 Wilson vertex k-uniform iff tc + 2 tA >= d"
    return tc + 2 * tA >= d

def soft_ok(d, tr, tA):
    "NORMS l.651/654: level-j soft vertex k-uniform iff tr + 2 tA > d"
    return tr + 2 * tA > d

def tA_of(tc):
    "NORMS l.656-657: theta_A = min(1, theta_w^c - 1)"
    return min(F(1), tc - 1)

def A_exponent(d, tr, tA):
    "NORMS l.654: A = L^{d - tr - 2 tA}; return the exponent."
    return d - tr - 2 * tA

# --------------------------------------------------------------------------
# a finite exact grid. The system is piecewise linear with breakpoints at
# integers and halves; a grid of step 1/12 over [0,4] separates every
# constraint boundary used here, and every verdict is checked for robustness
# by also testing the exact boundary points.
# --------------------------------------------------------------------------
STEP = F(1, 12)
def grid(lo, hi, step=STEP):
    out, x = [], F(lo)
    while x <= F(hi):
        out.append(x)
        x += step
    return out

# --------------------------------------------------------------------------
# tw1-A : reproduction gate. Single common theta_w in (0,2]. MUST be EMPTY.
# --------------------------------------------------------------------------
def tw1_A(d=4):
    sols = []
    for tw in grid(0, 2):
        if tw <= 0:
            continue                      # (0,2], open at 0
        tA = tA_of(tw)
        if wilson_ok(d, tw, tA) and soft_ok(d, tw, tA):
            sols.append((tw, tA))
    return sols

# --------------------------------------------------------------------------
# tw1-B : the decoupled system.
#   tc  : ceiling 2 (NORMS l.660, ARGUED); floor from wilson_ok
#   tr  : free, subject to soft_ok and to the supply ceiling (see note)
#   tA  : bound to tc by NORMS l.656-657
#   th  : 0 < th < 1 (BFT_A l.834, PROVEN); al < th (BFT_A l.834 + G♯R strict)
#   al  : 0 < al < 1 (BFT_A l.36)
# The supply ceiling on tr is the only place where the source weight couples to
# the displacement weights; it is passed in as `tr_cap(th)` so that the
# coupling is explicit and can be switched off to test its effect.
# --------------------------------------------------------------------------
def tw1_B(d=4, tc_ceiling=F(2), th_lo_strict=True, th_fixed=None,
          tr_cap=None, al_max=F(1)):
    sols = []
    ths = [th_fixed] if th_fixed is not None else grid(0, 1)
    for th in ths:
        if th_lo_strict and th <= 0:
            continue
        if th >= 1:                       # BFT_A l.834: theta < 1 (BL-6(a), BA-6)
            continue
        for al in grid(0, al_max):
            if al <= 0:
                continue
            if not (al < th):             # BFT_A l.834 + Cor. G♯R strict alpha<theta
                continue
            for tc in grid(0, tc_ceiling):
                if tc <= 0:
                    continue
                tA = tA_of(tc)
                if tA <= 0:
                    continue
                if not wilson_ok(d, tc, tA):
                    continue
                cap = tr_cap(th) if tr_cap else F(99)
                for tr in grid(0, cap):
                    if tr <= 0:
                        continue
                    if tr > cap:
                        continue
                    if not soft_ok(d, tr, tA):
                        continue
                    sols.append((al, th, tc, tr, tA, A_exponent(d, tr, tA)))
    return sols

def summarize(sols, label):
    if not sols:
        print(f"  {label}: EMPTY (no admissible point)")
        return None
    cols = list(zip(*sols))
    names = ["alpha", "theta", "tc", "tr", "tA", "expA"]
    print(f"  {label}: FEASIBLE, {len(sols)} grid points")
    for nm, c in zip(names, cols):
        print(f"      {nm:>6}: min {min(c)}  max {max(c)}")
    best = min(sols, key=lambda s: s[5])
    print(f"      best contraction exponent d-tr-2tA = {best[5]}  at "
          f"(alpha,theta,tc,tr,tA) = {best[:5]}")
    return best

# the coupling actually found in the lane (see THETAW.md §T3):
#   BFT_A l.1551 gives the residual response to residual-type sources an extra
#   L^{-theta(k-i)} on top of 𝔐's exponent-2 residual leg, so the residual
#   exponent that the FULL (nonlinear-source) contraction can use is 2 + theta.
#   BFT_A l.1549 gives 3 for the data part alone.
def cap_nonlinear(th):
    return 2 + th
def cap_dataonly(th):
    return F(3)

print("=" * 72)
print("tw1 -- exact feasibility of the decoupled exponent system")
print("exact Fractions only; criteria pre-registered in tw1_criteria.md")
print("=" * 72)

print("\n[tw1-A] reproduction gate: single common theta_w in (0,2], d=4")
solsA = tw1_A(4)
if solsA:
    print(f"  RESULT: FEASIBLE at {solsA}  ->  gate FAILS")
    print("  VERDICT tw1-A: FAIL")
else:
    print("  RESULT: EMPTY")
    print("  VERDICT tw1-A: PASS (reproduces PROOF.md l.30-34 [S24-fix 3])")

print("\n[tw1-B] decoupled system, d=4, residual supply capped at 2+theta "
      "(nonlinear sources)")
bB = summarize(tw1_B(4, tr_cap=cap_nonlinear), "tw1-B")

print("\n[tw1-B'] decoupled system, d=4, residual supply capped at 3 "
      "(level-k data only)")
summarize(tw1_B(4, tr_cap=cap_dataonly), "tw1-B'")

print("\n[tw1-C] designed-FAIL control 1: source weight pinned to theta = 0")
solsC = tw1_B(4, th_fixed=F(0), th_lo_strict=True, tr_cap=cap_nonlinear)
if solsC:
    print("  RESULT: FEASIBLE  ->  CONTROL DID NOT FIRE; tw1-B withdrawn")
else:
    print("  RESULT: EMPTY  ->  CONTROL FIRED (the theta>0 floor is live)")

print("\n[tw1-D] designed-FAIL control 2: d = 5")
solsD = tw1_B(5, tr_cap=cap_nonlinear)
if solsD:
    print(f"  RESULT: FEASIBLE ({len(solsD)} pts)  ->  CONTROL DID NOT FIRE; "
          "tw1-B withdrawn")
else:
    print("  RESULT: EMPTY  ->  CONTROL FIRED (the count carries d)")

print("\n[tw1-D'] control 2 variant: d = 5 with the data-only cap tr <= 3")
solsDp = tw1_B(5, tr_cap=cap_dataonly)
print("  RESULT:", "FEASIBLE %d pts" % len(solsDp) if solsDp else "EMPTY")

print("\n[tw1-E] d-sweep (reporting only)")
for d in (2, 3, 4, 5, 6):
    s_nl = tw1_B(d, tr_cap=cap_nonlinear)
    s_do = tw1_B(d, tr_cap=cap_dataonly)
    # slack in the Wilson clause at the maximal proven supply (tc=2 -> tA=1)
    wslack = F(2) + 2 * F(1) - d
    print(f"  d={d}: nonlinear-source system {'FEASIBLE' if s_nl else 'EMPTY':>8}"
          f" | data-only system {'FEASIBLE' if s_do else 'EMPTY':>8}"
          f" | Wilson slack at (tc,tA)=(2,1): {wslack}")

print("\n[tw1-F] the pinning of theta_w^c at d=4 (exact, no grid)")
# wilson_ok with tA = min(1, tc-1):
#   tc >= 2  ->  tA = 1  ->  tc + 2 >= 4  <=>  tc >= 2
#   tc <  2  ->  tA = tc-1 ->  3tc - 2 >= 4 <=> tc >= 2  (contradiction)
for tc in (F(3,2), F(7,4), F(2), F(9,4), F(5,2)):
    tA = tA_of(tc)
    print(f"  tc={tc}: tA={tA}, tc+2tA={tc + 2*tA}, Wilson(d=4) "
          f"{'OK' if wilson_ok(4, tc, tA) else 'FAILS'}")
print("  => floor theta_w^c >= 2 (PROVEN given the tA cap); ceiling 2 (ARGUED,"
      " NORMS l.660) => theta_w^c = 2 exactly.")

print("\n[tw1-G] A = L^{d-tr-2tA} at L=3, exact")
for name, tr in (("data-only tr=3", F(3)), ("nonlinear tr=2+1/2", F(5, 2)),
                 ("nonlinear tr=2+1/4", F(9, 4)), ("boundary tr=2", F(2))):
    e = A_exponent(4, tr, F(1))
    print(f"  {name:>22}: exponent {e}, A = 3^({e}) = "
          f"{F(3)**e if e >= 0 else F(1, 3**(-e))}")
print("=" * 72)
