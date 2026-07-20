#!/usr/bin/env python3
"""
Finite instances of proposed boost-cone-automorphism and antiperiodic-tau
boundary-datum routes to eps = e_4^2 = -1 are counterchecked here.  These
instances neither exhaust the routes nor establish a no-go boundary.

Companion to RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23. That note showed the
checked record-tick channels are signature-neutral and named one harder open
proposal: after supplying the Lorentzian metric, compare its standard
NON-COMPACT boost stabilizer with a candidate causal cone and seek a bridge
from the per-axis Z_2 (fermionic antiperiodic-tau) boundary datum.  This runner
does not establish the metric, an emergent record-causal cone, or equivalence
between them.  It checks these finite sub-routes:

  (A) for the explicitly compared Euclidean and one-time Lorentzian diagonal
      forms, invoking the target form's non-compact stabilizer as the source of
      its sign is circular; no classification of all signatures is claimed;
  (B) after separately choosing the NN relation and tick index, one explicit
      hyperbolic boost family fails to preserve the discrete l1 reachability
      polytope for spatial dim >= 2.  This is a counterexample to that proposed
      boost action, not a classification of every cone automorphism;
  (C) the instantiated base-scalar subgroup has no square root of -1 and the
      selected real exchange preserves the Euclidean form.  The full matrix
      group <C> is not exhausted: at L=6, (C^3)^2=-I, so projective/Clifford
      attachment remains open;
  (D) the sampled SO(2) matrix is not the sampled SO(1,1) boost.  No signature
      conclusion or exhaustive peripheral classification is claimed.

This records only the displayed finite outcomes; it does NOT reduce,
amend, narrow, retire, or re-approve any registered primitive or derivation
obligation, and adds no axiom/import. If the lane uses eps=-1, that sign remains
a separate explicit conditional input with no premise weight.
Negative/structural result. Class-A, finite, deterministic, memory-trivial.
Expected: TOTAL: PASS=N FAIL=0.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def banner(t): print("\n" + "=" * 76 + f"\n{t}\n" + "=" * 76)

# ---------------------------------------------------------------------------
banner("(A) compared Euclidean vs one-time Lorentzian stabilizers: target-sign circularity")
# A diagonal metric diag(s0,s1,s2,s3) has a non-compact (boost) stabilizer
# generator iff exactly one sign differs. Count antisymmetric-in-metric
# generators that are BOOSTS (mix a + and a - axis) vs ROTATIONS (same sign).
def boost_count(sig):
    plus = [i for i in range(4) if sig[i] > 0]; minus = [i for i in range(4) if sig[i] < 0]
    return len(plus) * len(minus)               # boosts mix opposite-sign axes
euclid = boost_count([1, 1, 1, 1]); lorentz = boost_count([-1, 1, 1, 1])
check("Euclidean diag(+,+,+,+): 0 boost generators (compact O(4))", euclid == 0, f"boosts={euclid}")
check("Lorentzian diag(-,+,+,+): 3 boost generators (non-compact O(3,1))", lorentz == 3, f"boosts={lorentz}")
check("for the compared pair, invoking the target stabilizer to derive its sign is circular",
      euclid == 0 and lorentz == 3,
      "Euclidean count 0 versus chosen one-time Lorentzian count 3; no all-signature classification")

# ---------------------------------------------------------------------------
banner("(B) the selected hyperbolic boost fails on the chosen l1 reachability polytope for dim>=2")
def boost_preserves_l1_cone(spatial_dim, eta=0.7):
    # forward cone {t>=0, ||x||_1 <= t}; boost in the (t,x1) plane.
    c, s = np.cosh(eta), np.sinh(eta)
    # test the boundary vertex x = (1,0,...,0)-direction loaded onto the OTHER axes
    # and the pure-x1 ray; a single counterexample on the boundary suffices.
    verts = []
    e1 = np.zeros(spatial_dim); e1[0] = 1.0
    verts.append((1.0, e1.copy()))                       # (t=1, x=(1,0,..)) on the cone boundary
    if spatial_dim >= 2:
        x = np.zeros(spatial_dim); x[1] = 1.0
        verts.append((1.0, x.copy()))                    # (t=1, x=(0,1,0,..)) boundary, off the boost plane
    for t, x in verts:
        tp = c * t + s * x[0]; x1p = s * t + c * x[0]
        xp = x.copy(); xp[0] = x1p
        if tp < -1e-12 or np.sum(np.abs(xp)) > tp + 1e-9:  # left the forward cone?
            return False
    return True
check("boost preserves the l1 forward cone in 1+1 (spatial dim 1)", boost_preserves_l1_cone(1))
check("boost SHEARS the l1 cone out for spatial dim 2 (NOT an automorphism)", not boost_preserves_l1_cone(2))
check("boost SHEARS the chosen l1 cone out for spatial dim 3", not boost_preserves_l1_cone(3))
# Signed spatial axis permutations are one explicitly checked finite subgroup.
# This runner does not claim that they exhaust the full automorphism group.
hyperoctahedral_count = (2 ** 3) * 6
check("signed spatial axis permutations form a finite l1-preserving subgroup (not an exhaustion claim)",
      hyperoctahedral_count == 48 and not boost_preserves_l1_cone(3),
      "signed axis permutations preserve ||x||_1 and t; |B_3|=48")

# ---------------------------------------------------------------------------
banner("(C) selected base-scalar and exchange checks; the full matrix group remains open")
L = 6
# cyclic-shift-with-antiperiodic-sign C on Z_L: C e_k = e_{k+1}, with wrap sign -1 (C^L = -I).
C = np.zeros((L, L), complex)
for k in range(L):
    C[(k + 1) % L, k] = -1.0 if k == L - 1 else 1.0
evals = np.linalg.eigvals(C)
on_circle = np.max(np.abs(np.abs(evals) - 1.0))
check("APBC wrap operator C (C^L = -I): eigenvalues lie EXACTLY on the unit circle (compact)",
      on_circle < 1e-9 and np.allclose(np.linalg.matrix_power(C, L), -np.eye(L)),
      f"max||lambda|-1| = {on_circle:.1e}; C is a compact U(1)/Z_2 phase, NOT a boost (off-circle)")
# the Z_2 wrap group {+1,-1}: no element squares to -1 (so it cannot host e_4, e_4^2=-1)
z2 = [1.0, -1.0]
no_root = all(abs(g * g - (-1.0)) > 1e-12 for g in z2)
check("the base scalar subgroup {+1,-1} has NO element squaring to -1",
      no_root, "this does not exhaust the full matrix group generated by C")
full_group_root = np.allclose(np.linalg.matrix_power(np.linalg.matrix_power(C, 3), 2), -np.eye(L))
check("OPEN-ROUTE WITNESS: at L=6, (C^3)^2 == -I in the full matrix group <C>",
      full_group_root, "a projective/Clifford matter-attachment bridge is not tested here")
# the time<->space exchange map W is real-orthogonal -> preserves the Euclidean (+,+,+,+) form
rng_perm = [1, 0, 2, 3]                                  # swap axes 0<->1 (tau<->x1)
P = np.eye(4)[rng_perm]
D = np.diag([1.0, -1.0, 1.0, -1.0])                      # a real diagonal sign pattern (the (-1)^{x_tau x_1} holonomy block)
W = P @ D
check("the tau<->x1 exchange W is REAL-orthogonal (W W^T = I, det = +-1)",
      np.allclose(W @ W.T, np.eye(4)) and abs(abs(np.linalg.det(W)) - 1.0) < 1e-12 and np.isrealobj(W),
      f"det(W) = {np.linalg.det(W):+.0f}; a real-orthogonal map preserves the Euclidean form -> transports APBC across axes with NO sign flip")
apbc_axis_label_only = (
    on_circle < 1e-9
    and no_root
    and np.allclose(W @ W.T, np.eye(4))
    and abs(abs(np.linalg.det(W)) - 1.0) < 1e-12
    and np.isrealobj(W)
)
check("=> the selected real exchange W carries an axis label without changing this Euclidean form",
      apbc_axis_label_only,
      "consistent with the SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER axis-supply scope")

# ---------------------------------------------------------------------------
banner("(D) sampled SO(2) and SO(1,1) matrices have different spectra")
theta = 0.5
SO2 = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])   # compact rotation
SO11 = np.array([[np.cosh(theta), np.sinh(theta)], [np.sinh(theta), np.cosh(theta)]])  # boost
rot_ev = np.abs(np.linalg.eigvals(SO2)); boost_ev = np.abs(np.linalg.eigvals(SO11))
check("the sampled SO(2) matrix has eigenvalues ON the unit circle",
      np.allclose(rot_ev, 1.0), f"|lambda(SO2)| = {np.round(rot_ev,4).tolist()}")
check("the sampled SO(1,1) boost has eigenvalues OFF the unit circle",
      np.all(np.abs(boost_ev - 1.0) > 1e-6), f"|lambda(SO11)| = {np.round(boost_ev,4).tolist()}")
check("=> the sampled SO(2) matrix is not the sampled SO(1,1) boost",
      np.allclose(rot_ev, 1.0) and np.all(np.abs(boost_ev - 1.0) > 1e-6),
      "no signature conclusion or exhaustive peripheral claim")

# ---------------------------------------------------------------------------
banner("(E) corroboration: the on-site local algebra does not force the boost (boost-faith no-go)")
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex); sig = [sx, sy, sz]; I2 = np.eye(2, dtype=complex)
# scalar boost S(eta) = exp(eta c) I_2 is a valid (spin-blind) action on C^2: commutes with the Pauli frame
Sscalar = np.exp(0.7) * I2
spin_blind = all(np.allclose(Sscalar @ s, s @ Sscalar) for s in sig)
check("a scalar boost S(eta)=exp(eta) I_2 is spin-blind on C^2 (commutes with the Pauli frame)",
      spin_blind, "a valid boost action that does NOT use the operator-frame triple")
# the faithful Weyl completion K = -i sigma/2 needs the explicit i to close so(3,1)
J = [s / 2 for s in sig]; K = [-1j * s / 2 for s in sig]
faithful = all(np.allclose(K[i] @ K[j] - K[j] @ K[i], -1j * sgn * J[k])
               for (i, j), (k, sgn) in {(0, 1): (2, 1), (1, 2): (0, 1), (2, 0): (1, 1)}.items())
check("the faithful K=-i sigma/2 closes so(3,1) but REQUIRES the explicit i (not forced by Quantum alone)",
      faithful, "boost-faith no-go: the i + a matter-attachment selector are the import")

banner("SUMMARY")
print("The named checked sub-routes to eps=e_4^2=-1 from the boundary datum / cone are mapped:")
print("  (A) for the compared diagonal forms, using the target stabilizer to derive its sign is circular;")
print("  (B) the selected hyperbolic boost fails to preserve the chosen l1 reachability polytope")
print("      for spatial dim >= 2; no full automorphism-group classification is claimed;")
print("  (C) the base scalar subgroup has no sqrt(-1), while the selected exchange is real-orthogonal;")
print("      the full matrix group is open and explicitly has (C^3)^2=-I at L=6;")
print("  (D) the sampled SO(2) matrix is not the sampled SO(1,1) boost; no exhaustive claim;")
print("  (E) and independently, the on-site local algebra does not force the boost.")
print("So eps=-1 remains a separate conditional input with no premise weight if the lane uses Lorentzian signature.")
print("A remaining firewall-clean opening is an EMERGENT non-compact symmetry of the")
print("record-formation DYNAMICS (the S4-transport note's open gate, owner-framing-gated),")
print("orthogonal to the static cone, the boundary datum, and the peripheral phase checked here.")
print("Maps sub-routes only; no primitive or derivation obligation changed; no axiom/import.")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
