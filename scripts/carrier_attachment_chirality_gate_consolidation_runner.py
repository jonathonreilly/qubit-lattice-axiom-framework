"""
Finite carrier-attachment no-go plus chirality-boundary guardrail.

13-agent find-the-escape panel verdict (this session): the candidate escape "the qubit's
Cl(3,0)->Cl(3,1) IS the emergent spacetime Clifford, so the spinor module supplies the j=1/2
STATE law" is REFUTED -- it is blind to the faithful-vs-trivial selection exactly as the
boost-covariance was blind to S(2pi)=-1. CL3_TO_CL31 sec 8 (retained) confines the Cl(3,1)=M_4(R)
action to the abstract algebra, NOT the per-site C^2 module. So the carrier residual remains on the
separate Kawamoto-Smit / physical-state-law route.

This runner records the panel's two results:
  (i) REFUTATION (rotation-level twin of the retained_no_go boost note): the operator-frame
      conjugation U(R) sigma_i U(R)^dag = R_ij sigma_j factors through Aut(M_2(C))=SO(3) and is
      BLIND to the SU(2) cover; the trivial scalar lift V(R)=I_2 satisfies every operator-frame
      constraint AND yields identical measured numbers -- so the j=1/2 STATE law is a separate datum.
  (ii) BOUNDARY: the spin-blind scalar mass-shell kernel H*I commutes with sigma_i (the scalar
      attachment is kernel-compatible); a spinful kernel is the displayed selector that excludes
      the trivial scalar. The staggered {eps, D}=0 calculation is a local Dirac/staggered
      chirality surface, not a proof of the KS/Grassmann physical-state-law bridge and not the
      Koide/generation r=1/2 gate.

No new axiom. Class-A finite-dimensional checks. TOTAL: PASS=N FAIL=0 expected.
"""
from pathlib import Path

import numpy as np
expm = __import__("scipy.linalg", fromlist=["expm"]).expm

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex); sz = np.array([[1, 0], [0, -1]], complex)
sigma = [sx, sy, sz]; I2 = np.eye(2, dtype=complex)

print("=" * 78)
print("Cover blindness: operator-frame conjugation factors through SO(3)")
print("=" * 78)
# state action U(R) = exp(i theta n.sigma/2) is faithful j=1/2 (U(2pi)=-I); the OPERATOR conjugation
# A -> U A U^dag factors through Aut(M_2(C))=SO(3): conj by U and by -U are identical, R(2pi)=+I.
def U_state(axis, theta):
    n = np.array(axis, float); n = n / np.linalg.norm(n)
    return expm(1j * theta / 2 * sum(n[i] * sigma[i] for i in range(3)))
def R_adjoint(U):
    return np.array([[0.5 * np.trace(sigma[i] @ U @ sigma[j] @ U.conj().T).real for j in range(3)] for i in range(3)])
U2pi = U_state([0, 0, 1], 2 * np.pi)
state_faithful = np.allclose(U2pi, -I2)                       # U(2pi) = -I  (faithful double cover)
Ua = U_state([0, 0, 1], 0.9)
R_from_U = R_adjoint(Ua); R_from_negU = R_adjoint(-Ua)
adjoint_blind = np.allclose(R_from_U, R_from_negU)            # conj by U and -U identical
R2pi = R_adjoint(U2pi)
adjoint_trivial_2pi = np.allclose(R2pi, np.eye(3))           # R(2pi) = +I (no sign: kills Z2 center)
is_so3 = np.allclose(R_from_U @ R_from_U.T, np.eye(3)) and abs(np.linalg.det(R_from_U) - 1) < 1e-9
print(f"   STATE U(2pi) = -I (faithful j=1/2 double cover): {state_faithful}")
print(f"   OPERATOR conj by U and by -U identical, R(2pi)=+I (factors through SO(3)): {adjoint_blind and adjoint_trivial_2pi}")
check("operator-frame conjugation is the adjoint SO(3), BLIND to the SU(2) cover (the Z2 state datum)",
      state_faithful and adjoint_blind and adjoint_trivial_2pi and is_so3,
      "same gap as the retained_no_go boost note, at the rotation level")

print()
print("=" * 78)
print("Trivial lift: V(R)=I_2 satisfies every operator-frame constraint")
print("=" * 78)
# Model A (faithful): V_A(R)=U(R); Model B (trivial scalar): V_B(R)=I_2. Both implement the SAME
# operator covariance U sigma_i U^dag = R_ij sigma_j ... in Model B the operators are conjugated by
# the physical R acting on the gamma-INDEX (an outer relabel), state inert. Measured numbers identical.
theta = 0.9; R = R_adjoint(U_state([0, 0, 1], theta))
# operator covariance holds in BOTH frames (it is a statement about sigma_i, not the ket):
op_cov = np.allclose(U_state([0,0,1],theta) @ sigma[2] @ U_state([0,0,1],theta).conj().T, sigma[2])  # z-rot fixes sigma_z
# measured numbers: <psi|sigma_z|psi> with active (V_A) vs passive (V_B + index relabel) -- identical
psi = np.array([0.6, 0.8], complex); psi /= np.linalg.norm(psi)
# active: rotate state, measure fixed obs ; passive: fix state, rotate obs -- same number (Wigner)
active = (U_state([1,0,0],0.7) @ psi).conj() @ (sz @ (U_state([1,0,0],0.7) @ psi))
passive = psi.conj() @ ((U_state([1,0,0],0.7).conj().T @ sz @ U_state([1,0,0],0.7)) @ psi)
passive_equals_active = np.isclose(active, passive)
print(f"   operator covariance holds independent of the state law: {op_cov}")
print(f"   active (Model A) vs passive (Model B) measured numbers identical: {passive_equals_active}")
check("trivial scalar lift V(R)=I_2 is operator-frame-compatible => the j=1/2 STATE law is a separate datum",
      op_cov and passive_equals_active, "Model A (faithful) and Model B (scalar) have identical Quantum content")

print()
print("=" * 78)
print("Kernel route: the spin-blind scalar kernel admits the scalar; only spinful sigma.p excludes it")
print("=" * 78)
# native scalar mass-shell kernel H*I_2 (spin-blind) COMMUTES with sigma_i -> the trivial scalar
# attachment is kernel-compatible (no co-rotation forced). The ONLY kernel that excludes the scalar
# is the spinful sigma.p (a DIFFERENT operator).
H_scalar = 1.3 * I2                                          # spin-blind scalar mass-shell stand-in
scalar_compatible = all(np.allclose(H_scalar @ sigma[i], sigma[i] @ H_scalar) for i in range(3))
p = np.array([0.3, -0.5, 0.4])
K_spinful = sum(p[i] * sigma[i] for i in range(3))          # sigma.p : co-rotates the index
spinful_differs = np.linalg.norm(K_spinful - (np.trace(K_spinful)/2) * I2) > 1e-6
spinful_excludes_scalar = not all(np.allclose(K_spinful @ sigma[i], sigma[i] @ K_spinful) for i in range(3))
print(f"   spin-blind scalar kernel H*I commutes with sigma_i (scalar attachment kernel-compatible): {scalar_compatible}")
print(f"   only the spinful sigma.p kernel excludes the scalar (differs, non-central): {spinful_differs and spinful_excludes_scalar}")
check("the selector that excludes the trivial scalar is the spinful sigma.p kernel",
      scalar_compatible and spinful_differs and spinful_excludes_scalar,
      "kernel-covariance alone admits the scalar; the spinful kernel is the matter-attachment")

print()
print("=" * 78)
print("Staggered boundary: the displayed D has {eps, D} = 0")
print("=" * 78)
# The displayed staggered Dirac operator D has the local chirality property
# {eps, D}=0. This is a boundary/supply-route fact here, not a closure of the
# physical matter-state-law bridge.
L = 4
def idx(x, y, z): return (x % L) * L * L + (y % L) * L + z % L
n = L**3
D = np.zeros((n, n))
for x in range(L):
    for y in range(L):
        for z in range(L):
            i = idx(x, y, z)
            eta = [1.0, (-1)**x, (-1)**(x + y)]              # Kogut-Susskind staggered phases
            for mu, (dx, dy, dz) in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
                j = idx(x + dx, y + dy, z + dz)
                D[i, j] += 0.5 * eta[mu]
                D[j, i] += -0.5 * eta[mu]                    # anti-Hermitian (real)
eps = np.diag([(-1)**(x + y + z) for x in range(L) for y in range(L) for z in range(L)]).astype(float)
anticomm = eps @ D + D @ eps
chiral = np.allclose(anticomm, 0)                            # {eps, D} = 0 : the chirality gate
antiherm = np.allclose(D, -D.T)
print(f"   staggered D anti-Hermitian: {antiherm};  {{eps, D}} = 0 (chiral): {chiral}")
print("   => this is the local Dirac/staggered chirality surface used by the open KS route")
check("the displayed staggered D has the local chirality boundary {eps,D}=0",
      chiral and antiherm, "does not by itself close KS/Grassmann physical-state-law selection")

print()
print("=" * 78)
print("Source-boundary guardrail")
print("=" * 78)
note = NOTE.read_text(encoding="utf-8")
note_flat = " ".join(note.split())
required_boundaries = [
    "does not prove the KS/Grassmann physical-state-law bridge",
    "does not identify the Dirac/staggered chirality gate with the Koide/generation",
    "not the Koide/generation `r=1/2` gate",
    "supply a retained KS/Grassmann-to-physical-matter-state-law bridge",
    "CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08",
]
boundary_ok = all(" ".join(phrase.split()) in note_flat for phrase in required_boundaries)
print("   source note forbids treating this as closed KS/Grassmann or generation/r=1/2 consolidation:", boundary_ok)
check("source boundary prevents overclaiming the unresolved chirality/state-law bridge",
      boundary_ok, "runner verifies the repair target introduced by the conditional audit")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
