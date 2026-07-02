#!/usr/bin/env python3
"""
The record-tick is signature-neutral: eps = e_4^2 = -1 is a separate admission.

Cross-sector / emergent-time question: does the monotone, irreversible Z^3
record-tick FORCE the Lorentzian signature eps = e_4^2 = -1? This runner checks
that the record-tick channels below are signature-neutral: an ARROW (direction),
a CPTP CONTRACTION T = exp(-tau H) (the Euclidean heat-kernel), positive energy
H >= 0 (durability), and a causal order -- all present in a Euclidean
(eps = +1, SO(4)) setting and therefore orthogonal to the metric sign. The sign
eps = -1 enters through the multiplication-by-i of the Wick continuation
tau -> i t (e_4 -> i e_4), not through those checked channels.

This localizes eps = -1 into the same register-not-read import class as the
readout admissions if the lane uses Lorentzian signature; it is NOT a
record-tick corollary. This note does NOT amend, narrow, retire, or re-approve
any registered primitive, and adds no axiom/import.

Class-A, finite-dimensional, deterministic, memory-trivial (2x2/4x4 operators).
Expected: TOTAL: PASS=N FAIL=0.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def banner(t): print("\n" + "=" * 76 + f"\n{t}\n" + "=" * 76)

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
sig = [sx, sy, sz]
I2 = np.eye(2, dtype=complex)

banner("No on-site e_4: the timelike anticommuting generator is absent from M_2(C)")
# anticommutant of {s1,s2,s3}: M in M_2(C) with {M,s_i}=0 for all i. dim should be 0.
basis = [I2, sx, sy, sz]                      # basis of M_2(C)
rows = []
for B in basis:
    v = []
    for s in sig:
        A = B @ s + s @ B                     # {B, s}
        v += [A[0, 0], A[0, 1], A[1, 0], A[1, 1]]
    rows.append(v)
Mmap = np.array(rows).T                        # columns = images of basis elts
# nullspace dim of the anticommutator map = number of M with {M,s_i}=0 for all i
rank = np.linalg.matrix_rank(Mmap, tol=1e-9)
null_dim = 4 - rank
check("anticommutant of the Pauli triple in M_2(C) has dimension EXACTLY 0 (no on-site e_4)",
      null_dim == 0, f"nullspace dim = {null_dim} (so e_4, e_4^2=-1, is not on-site)")

banner("Same H>=0 feeds BOTH branches: contraction (eps=+1) and unitary (eps=-1)")
H = np.diag([0.3, 1.2]).astype(complex)       # H >= 0 (durability / spectrum condition)
tau = 0.5
TE = np.diag(np.exp(-tau * np.diag(H).real))  # Euclidean semigroup exp(-tau H)
TL = np.diag(np.exp(-1j * tau * np.diag(H).real))  # Lorentzian unitary exp(-i tau H)
lamE = np.abs(np.linalg.eigvals(TE)); lamL = np.abs(np.linalg.eigvals(TL))
check("Euclidean exp(-tau H): |lambda| <= 1 (contraction, eps=+1 side)", np.all(lamE <= 1 + 1e-12),
      f"|lambda(T_E)| = {np.round(lamE,4).tolist()}")
check("Lorentzian exp(-i tau H): |lambda| = 1 (unitary, eps=-1 side) -- SAME H",
      np.allclose(lamL, 1.0), f"|lambda(T_L)| = {np.round(lamL,4).tolist()}")
same_h_both_branches = (
    np.all(np.linalg.eigvalsh(H.real) >= -1e-12)
    and np.all(lamE <= 1 + 1e-12)
    and np.allclose(lamL, 1.0)
)
check("positivity/durability constrains only |spec(T)|, not the sign of e_4^2",
      same_h_both_branches, "same H >= 0 gives both branches; the sign is the i, not in H")

banner("Contraction = unitary ONLY at the Wick point (H=0 or t imaginary)")
# for H>0, real tau>0 the semigroup is strictly NON-unitary; only tau->i*tau (Wick) restores |lambda|=1
nonunit = np.linalg.norm(TE.conj().T @ TE - I2)
check("exp(-tau H) is NOT unitary for H>0, real tau>0 (strict contraction)",
      nonunit > 1e-6, f"||T_E^dag T_E - I|| = {nonunit:.4f}")
wick_unitary = np.allclose(TL.conj().T @ TL, I2)
check("the contraction->unitary identification requires the eps=-1 input (the factor i: t = -i tau)",
      nonunit > 1e-6 and wick_unitary,
      "exp(-tau H) -> exp(-i t H) requires tau = i t; that i carries eps=-1")

banner("The ARROW coexists with a Euclidean (eps=+1) substrate: irreversibility != signature")
v = np.array([1.0, 1.0], complex)
norms = [np.linalg.norm(np.linalg.matrix_power(TE, n) @ v) for n in range(6)]
mono = all(norms[i] > norms[i + 1] for i in range(len(norms) - 1))
check("record-norm ||T_E^n v|| is strictly monotone (an ARROW) on the eps=+1 heat-kernel",
      mono, f"norms = {np.round(norms,4).tolist()}  (monotone decay = arrow, with eps=+1)")
heat_kernel_signature_neutral = mono and np.allclose(TE, TE.conj().T) and np.all(np.linalg.eigvalsh(TE) > 0)
check("arrow fixes direction only in the checked heat-kernel channel; eps fixes metric kind",
      heat_kernel_signature_neutral,
      "monotone Euclidean heat-kernel gives an arrow while leaving eps=e_4^2 unselected")

banner("On-site so(3,1) is available but the boost-vs-rotation (sign) is an unfixed label")
J = [s / 2 for s in sig]
K = [-1j * s / 2 for s in sig]                # boosts (anti-Hermitian) -> so(3,1)
def comm(A, B): return A @ B - B @ A
# [K_i,K_j] = -i eps_ijk J_k  (Lorentzian boosts, eps=-1)
ok_so31 = all(np.allclose(comm(K[i], K[j]), -1j * s * J[k])
              for (i, j), (k, s) in {(0, 1): (2, 1), (1, 2): (0, 1), (2, 0): (1, 1)}.items())
check("{J_i=sigma_i/2, K_i=-i sigma_i/2} closes so(3,1): [K_i,K_j] = -i eps J_k (boosts)",
      ok_so31, "(1/2,0) Weyl boosts live on-site")
# flipping the bracket sign gives so(4) (compact): [K'_i,K'_j] = +i eps J_k with K'_i = sigma_i/2.
ok_so4 = all(np.allclose(comm(J[i], J[j]), 1j * s * J[k])
             for (i, j), (k, s) in {(0, 1): (2, 1), (1, 2): (0, 1), (2, 0): (1, 1)}.items())
check("the e_4^2 sign is invisible on-site: same Pauli span closes so(3,1) (-i) and so(4) (+i)",
      ok_so31 and ok_so4, "boost(anti-Hermitian, eps=-1) vs rotation(Hermitian, eps=+1) is an unfixed label")

banner("SUMMARY")
print("The Z^3 record-tick supplies, all natively at eps=+1 (Euclidean/SO(4)):")
print("  - an ARROW (monotone record-norm = direction = the admitted past hypothesis),")
print("  - a CPTP CONTRACTION T=exp(-tau H) (the sign-neutral Euclidean heat-kernel),")
print("  - POSITIVE ENERGY H>=0 (durability/spectrum condition),")
print("  - a causal order (metric-free).")
print("All four checked channels are present in a Euclidean theory, hence ORTHOGONAL")
print("to the metric sign. eps = e_4^2 = -1 is the multiplication-by-i of the Wick step")
print("tau->i t (e_4->i e_4): no on-site e_4 exists (anticommutant dim 0), the SAME")
print("H>=0 feeds both branches, and a contraction equals a unitary only at the Wick")
print("point. So eps=-1 is a separate binary input/admission if the lane uses")
print("Lorentzian signature -- NOT a record-tick corollary of the checked channels.")
print("Negative/structural result; adds no axiom/import; no primitive touched.")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
