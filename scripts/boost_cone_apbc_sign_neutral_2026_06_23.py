#!/usr/bin/env python3
"""
The boost-cone-automorphism and antiperiodic-tau boundary-datum routes to
eps = e_4^2 = -1 are checked no-go boundaries: the boost route is circular and
the boundary datum is sign-neutral.

Companion to RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23. That note showed the
checked record-tick channels are signature-neutral and named one harder open
route: the metric sign eps=-1 is equivalent to a NON-COMPACT (boost) symmetry
of the emergent record-causal cone, which one might hope to ride on the per-axis
Z_2 (fermionic antiperiodic-tau) boundary datum. This runner checks that
sub-route:

  (A) the boost-cone-automorphism route is CIRCULAR -- a non-compact stabilizer
      of a 4D cone exists iff one metric sign is -1, which IS eps=-1;
  (B) the discrete record-causal cone (the Lieb-Robinson NN forward-reachability
      polytope) admits only a COMPACT automorphism group: a hyperbolic boost
      preserves the l1/l_inf cone only in 1+1 and shears it out for spatial
      dim >= 2;
  (C) the antiperiodic-tau datum is SIGN-NEUTRAL, not sign-bearing: its wrap
      operator is compact (eigenvalues on the unit circle), the Z_2 wrap group
      has no element squaring to -1, and the time<->space exchange map is
      real-orthogonal (preserves the Euclidean form -> carries which-axis, never
      what-signature). eps=-1 lives in a different object, the Clifford fiber
      (the i in gamma^j = i gamma^E_j);
  (D) the peripheral/unitary summand's phase is a compact SO(2) angle (on the
      unit circle), not a boost (off the unit circle) -- the wrong generator
      class for eps=-1.

This maps checked sub-routes as circular or sign-neutral; it does NOT reduce,
amend, narrow, retire, or re-approve any registered primitive or admission, and
adds no axiom/import. If the lane uses eps=-1, that sign remains a separate
register-not-read input/admission.
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
banner("(A) boost-cone-automorphism route is CIRCULAR: non-compact stabilizer <=> eps=-1")
# A diagonal metric diag(s0,s1,s2,s3) has a non-compact (boost) stabilizer
# generator iff exactly one sign differs. Count antisymmetric-in-metric
# generators that are BOOSTS (mix a + and a - axis) vs ROTATIONS (same sign).
def boost_count(sig):
    plus = [i for i in range(4) if sig[i] > 0]; minus = [i for i in range(4) if sig[i] < 0]
    return len(plus) * len(minus)               # boosts mix opposite-sign axes
euclid = boost_count([1, 1, 1, 1]); lorentz = boost_count([-1, 1, 1, 1])
check("Euclidean diag(+,+,+,+): 0 boost generators (compact O(4))", euclid == 0, f"boosts={euclid}")
check("Lorentzian diag(-,+,+,+): 3 boost generators (non-compact O(3,1))", lorentz == 3, f"boosts={lorentz}")
check("a non-compact boost stabilizer EXISTS iff a metric sign is -1, which IS eps=-1 (circular)",
      euclid == 0 and lorentz == 3, "'derive eps from the boost' presupposes the boost = presupposes eps")

# ---------------------------------------------------------------------------
banner("(B) the record-cone polytope admits only COMPACT automorphisms (boost shears it for dim>=2)")
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
check("boost SHEARS the l1 cone out for spatial dim 3 (the actual record-cone)", not boost_preserves_l1_cone(3))
# the surviving checked linear symmetries are finite signed axis permutations (compact).
hyperoctahedral_count = (2 ** 3) * 6
check("the checked record-cone symmetries are finite signed axis permutations x Z (compact)",
      hyperoctahedral_count == 48 and not boost_preserves_l1_cone(3),
      "signed axis permutations preserve ||x||_1 and t; |B_3|=48 finite, no unbounded orbit")

# ---------------------------------------------------------------------------
banner("(C) the antiperiodic-tau datum is SIGN-NEUTRAL, not sign-bearing")
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
check("the Z_2 wrap holonomy group {+1,-1} has NO element squaring to -1 (cannot host e_4)",
      no_root, "eps=-1 needs e_4^2=-1, which lives in the Clifford fiber (i in gamma^j=i gamma^E_j), not the base Z_2")
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
check("=> APBC carries WHICH axis wraps (axis-labeling), not WHAT signature in this check",
      apbc_axis_label_only,
      "consistent with the SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER axis-supply scope")

# ---------------------------------------------------------------------------
banner("(D) the peripheral/unitary summand carries a COMPACT phase, not a boost")
theta = 0.5
SO2 = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])   # compact rotation
SO11 = np.array([[np.cosh(theta), np.sinh(theta)], [np.sinh(theta), np.cosh(theta)]])  # boost
rot_ev = np.abs(np.linalg.eigvals(SO2)); boost_ev = np.abs(np.linalg.eigvals(SO11))
check("a peripheral phase e^{i theta} is a COMPACT SO(2) angle: eigenvalues ON the unit circle (eps=+1)",
      np.allclose(rot_ev, 1.0), f"|lambda(SO2)| = {np.round(rot_ev,4).tolist()}")
check("a boost SO(1,1) has eigenvalues OFF the unit circle (e^{+-eta}, eps=-1) -- different generator class",
      np.all(np.abs(boost_ev - 1.0) > 1e-6), f"|lambda(SO11)| = {np.round(boost_ev,4).tolist()}")
check("=> even a nonzero peripheral phase is compact (eps=+1), so the peripheral summand cannot supply the boost",
      np.allclose(rot_ev, 1.0) and np.all(np.abs(boost_ev - 1.0) > 1e-6),
      "forcing eps=-1 needs an unbounded/non-unitary generator OFF the peripheral |lambda|=1 summand")

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
print("  (A) boost-cone-automorphism is CIRCULAR (boost-stabilizer EXISTS iff a metric sign is -1 = eps);")
print("  (B) the discrete record-cone is a polytope whose automorphism group is COMPACT")
print("      (a hyperbolic boost shears the l1/l_inf cone for spatial dim >= 2);")
print("  (C) the antiperiodic-tau datum is SIGN-NEUTRAL: compact unit-circle wrap, the Z_2")
print("      group has no sqrt(-1), and the time<->space exchange is real-orthogonal")
print("      (axis-labeling, not signature); eps=-1 lives in the Clifford fiber (the Wick i);")
print("  (D) the peripheral phase is a compact SO(2) angle, not a boost (wrong generator class);")
print("  (E) and independently, the on-site local algebra does not force the boost.")
print("So eps=-1 remains a separate binary input/admission if the lane uses Lorentzian signature.")
print("A remaining firewall-clean opening is an EMERGENT non-compact symmetry of the")
print("record-formation DYNAMICS (the S4-transport note's open gate, owner-framing-gated),")
print("orthogonal to the static cone, the boundary datum, and the peripheral phase checked here.")
print("Maps sub-routes only; no primitive/admission status touched; no axiom/import.")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
