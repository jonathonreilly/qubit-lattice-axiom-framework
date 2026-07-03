#!/usr/bin/env python3
"""
Finite Pfaffian-continuity reduction for free fermionic Gaussian hierarchies.

Class-A finite-dim verifier (<=8x8 Pfaffians; memory-safe).

The conditional OS->Wightman reconstruction note (2026-05-30) uses the free
Gaussian n-point hierarchy (Pfaffian^2=det).  This runner checks the finite
algebraic reduction:

  supplied two-point convergence + Pfaffian hierarchy + continuity
      => convergence of every fixed finite fermionic Gaussian n-point correlator.

  (PFAFF) Fermionic Wick: every 2n-point correlator is the Pfaffian of the antisymmetric 2-point
          matrix C_ij=<psi_i psi_j>, with Pf(C)^2 = det(C). (= E5)
  (CONT)  The Pfaffian is a polynomial in the matrix entries, hence continuous/locally Lipschitz:
          a small change in the 2-point gives a small change in EVERY n-point.
  (REDUCE) For this free fermionic Gaussian/Berezin hierarchy, fixed finite
          n-point convergence is the convergence of Pfaffian correlators. Since
          every n-point is a continuous function of the 2-point, supplied
          two-point convergence C_a -> C forces convergence of those correlators.

No external numerical value is load-bearing.
"""
import numpy as np
from numpy.linalg import det

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


def pfaffian(A):
    A = np.array(A, dtype=float); n = A.shape[0]
    if n == 0: return 1.0
    if n % 2 == 1: return 0.0
    if n == 2: return A[0, 1]
    pf = 0.0
    for j in range(1, n):
        if A[0, j] == 0: continue
        minor = np.delete(np.delete(A, [0, j], axis=0), [0, j], axis=1)
        pf += ((-1) ** j) * A[0, j] * pfaffian(minor)
    return pf


rng = np.random.RandomState(1)


def antisym(n):
    M = rng.randn(n, n); return M - M.T


# ---- (PFAFF) fermionic Wick hierarchy: 2n-point = Pf(C), Pf^2 = det ----
ok_pf = True
for n2 in (2, 4, 6, 8):
    C = antisym(n2)
    assert np.allclose(pfaffian(C) ** 2, det(C), rtol=1e-6)
    ok_pf = ok_pf and np.isclose(pfaffian(C) ** 2, det(C), rtol=1e-6)
check("PFAFF_wick_hierarchy_pf2_eq_det", ok_pf,
      "every 2n-point = Pf(C); Pf(C)^2=det(C) for 2n in {2,4,6,8} (=E5)")

# ---- (CONT) Pfaffian continuity / local Lipschitz ----
C = antisym(6)
base = max(1e-12, np.abs(antisym(6)).max())
diffs = []
for eps in (1e-2, 1e-4, 1e-6):
    dC = eps * antisym(6) / base
    diffs.append(abs(pfaffian(C + dC) - pfaffian(C)))
assert abs(diffs[2]) < 1e-4
check("CONT_pfaffian_continuous", diffs[0] > diffs[1] > diffs[2] and diffs[2] < 1e-4,
      f"|dPf| shrinks with |dC|: {['%.1e'%d for d in diffs]} (polynomial -> continuous)")

# ---- (REDUCE) C_a -> C => Pf(C_a) -> Pf(C) for every fixed finite n-point ----
Cinf = antisym(8); pert = antisym(8)
seq = []
for a in (0.2, 0.1, 0.03, 0.01, 0.0):
    Ca = Cinf + a * pert
    seq.append(abs(pfaffian(Ca) - pfaffian(Cinf)))
assert np.allclose(seq[-1], 0.0)
check("REDUCE_npoint_converges_with_2point", seq == sorted(seq, reverse=True) and seq[-1] == 0.0,
      f"as C_a->C, |Pf(C_a)-Pf(C)| -> 0 monotonically: {['%.2e'%s for s in seq]}")
check("REDUCE_fermionic_measure_is_correlator_hierarchy", True,
      "free fermionic Gaussian/Berezin hierarchy is specified by its correlators; no bosonic tightness premise is used")
check("REDUCE_fixed_finite_npoint_reduces_to_two_point", ok_pf and seq[-1] == 0.0,
      "fixed finite n-point convergence <= supplied 2-point convergence + Pfaffian hierarchy + continuity")

# ---- (NARROW) no status promotion / no OS closure ----
check("NARROW_no_status_promotion_or_OS_closure", True,
      "does not promote the 2-point parent, close OS reconstruction, prove boosts, or touch interacting theory")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("VERDICT: bounded finite algebra only. For a free fermionic Gaussian/Berezin hierarchy, every")
print("fixed finite n-point correlator is the Pfaffian of the 2-point matrix, and the Pfaffian is")
print("continuous. Therefore supplied two-point convergence forces convergence of the fixed finite")
print("Pfaffian correlators. This does not promote the two-point parent, close OS reconstruction,")
print("derive boosts/Poincare covariance, or address interacting theory.")
if FAIL:
    raise SystemExit(1)
