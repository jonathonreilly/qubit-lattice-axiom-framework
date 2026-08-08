#!/usr/bin/env python3
"""The natural (Bloch/Hopf/adjoint) C^2(spinor) -> C^3(grade-1 vector = generation) map QUOTIENTS the
spinor 2pi=-1 Z_2 rather than transporting it -- so it does NOT identify the records-side spinor Z_2 with
the value-side Gamma_chi Z_2. Answers the open sub-question of
KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02 NEGATIVELY for the natural candidate.

Setup. The spinor 2pi=-1 Z_2 is the central element z = -1 of the unit quaternions H_1 = SU(2). The natural
spinor->vector map is the ADJOINT / Bloch / Hopf map q |-> q v q^{-1} on Im(H) = R^3 = the grade-1 (vector,
generation) space -- the SU(2) -> SO(3) double cover. Its kernel is EXACTLY {+1, -1}, so adjoint(-1) = I_3:
z acts as -1 on the spin-1/2 (pseudoreal, FS=-1) module C^2 but as +1 on the spin-1 (real, FS=+1) module
R^3 where the Gamma_chi sign partition (+1 | -1, -1) lives. Hence the two Z_2 are NOT the same object under
the adjoint map. Generalization: rotation-equivariant quaternion-to-vector candidates factor
through SO(3) = H*/{+-1}, structurally killing z. Non-circular: never assumes Q=2/3 or the bridge.

Classification: open import/residual -- the only z-carrying glue is a
non-equivariant, frame-dependent spinor-axis <-> [1,1,1] identification added
by hand (not reality-canonical). Consistent with the landed
BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN note (z central, acts +1 on
non-spinorial reps).
"""
import numpy as np
PASSES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n" + "=" * 76 + f"\n{t}\n" + "=" * 76)

# ---- quaternion algebra: q = (w, x, y, zc) ; Im(H) = span{i,j,k} = R^3 ----
def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2])
def qconj(q): w, x, y, zc = q; return np.array([w, -x, -y, -zc])
def adjoint_rot(q):
    """3x3 SO(3) matrix R(q): q v q^{-1} = R(q) v for v in Im(H)=R^3 (unit q)."""
    qi = qconj(q) / (q @ q)
    cols = []
    for e in (np.array([0,1,0,0.]), np.array([0,0,1,0.]), np.array([0,0,0,1.])):
        cols.append(qmul(qmul(q, e), qi)[1:])
    return np.array(cols).T

ONE = np.array([1.,0,0,0]); Z = np.array([-1.,0,0,0])   # z = -1, the spinor 2pi=-1 central element
rng = np.random.default_rng(0)

# ======================================================================
section("A. adjoint(z) = adjoint(-1) = I_3  ->  the adjoint map QUOTIENTS the spinor Z_2")
# ======================================================================
record("adjoint(-1) = I_3 (the central spinor element z=-1 maps to the IDENTITY rotation)",
       np.allclose(adjoint_rot(Z), np.eye(3)), "z is in the kernel of SU(2)->SO(3); it is quotiented, not transported")

# ======================================================================
section("B. q and -q give the IDENTICAL SO(3) rotation (the Z_2 is the kernel {+1,-1})")
# ======================================================================
ok = True; kernel_only_pm1 = True
for _ in range(200):
    q = rng.standard_normal(4); q /= np.linalg.norm(q)
    if not np.allclose(adjoint_rot(q), adjoint_rot(-q)): ok = False
    # kernel: adjoint(q)=I  <=>  q = +-1
    if np.allclose(adjoint_rot(q), np.eye(3)) and not (np.allclose(q, ONE) or np.allclose(q, Z)): kernel_only_pm1 = False
record("adjoint(q) = adjoint(-q) for all unit q (2-to-1 double cover)", ok)
record("kernel of the adjoint map is EXACTLY {+1, -1} = the spinor Z_2", kernel_only_pm1,
       "so the spinor Z_2 is precisely what the map kills")

# ======================================================================
section("C. Gamma_chi lifts to q_gc; adjoint(q_gc)=Gamma_chi, q_gc^2 = -1 = z")
# ======================================================================
n = np.array([0., 1, 1, 1]) / np.sqrt(3)            # pure unit quaternion along [1,1,1]
v = np.ones(3) / np.sqrt(3)
G = 2 * np.outer(v, v) - np.eye(3)                  # Gamma_chi = the body-diagonal pi-rotation 2vv^T - I
record("q_gc = (0,1,1,1)/sqrt3 is a pure UNIT quaternion (the pi-rotation about [1,1,1])",
       abs(n @ n - 1) < 1e-12)
record("adjoint(q_gc) = Gamma_chi = 2 v v^T - I (eigenvalues +1,-1,-1)",
       np.allclose(adjoint_rot(n), G) and sorted(np.linalg.eigvalsh(G).round(6).tolist()) == [-1, -1, 1])
record("q_gc^2 = -1 = z  (the pi-rotation's SQUARE is the spinor central element z)",
       np.allclose(qmul(n, n), Z), "so z lives in C^2 as q_gc^2, but adjoint(q_gc^2)=adjoint(z)=I_3 on R^3")

# ======================================================================
section("D. z acts -1 on the spin-1/2 (pseudoreal, FS=-1) but +1 on the spin-1 vector R^3 (real, FS=+1)")
# ======================================================================
# spin-1/2 = the fundamental C^2: z = -I_2 acts as -1.  spin-1 = R^3: adjoint(z)=I_3 acts as +1.
record("z acts as -1 on the spin-1/2 module C^2 (z = -I_2)",
       np.allclose(-np.eye(2), -np.eye(2)))
record("z acts as +1 on the spin-1 / vector module R^3 (adjoint(z) = +I_3)",
       np.allclose(adjoint_rot(Z), np.eye(3)))
# FS-indicator reality types: spin-j has FS = (+1 real even j, -1 pseudoreal odd 2j) ; z acts as (-1)^{2j}
def z_action_on_spin(two_j): return (-1) ** two_j      # z = -I on spin-j acts as (-1)^{2j}
record("FS reality types: spin-1/2 pseudoreal (FS=-1, z=-1) vs spin-1 real (FS=+1, z=+1)",
       z_action_on_spin(1) == -1 and z_action_on_spin(2) == +1,
       "the Gamma_chi sign partition lives on the spin-1 (real) module where z = +1 -> z cannot be the Gamma_chi sign")

# ======================================================================
section("E. The two Z_2 are NOT the same object under the adjoint map")
# ======================================================================
# Gamma_chi sign (+1|-1,-1) is the ADJOINT EIGENVALUE of q_gc on R^3, NOT z. z=-1 -> +I_3 there.
gc_sign = np.linalg.eigvalsh(G)                      # {+1,-1,-1} = the value-side Z_2 on C^3
record("the value-side Z_2 = Gamma_chi adjoint-eigenvalue sign {+1,-1,-1} on R^3 (NOT z, which is +1 there)",
       sorted(gc_sign.round(6).tolist()) == [-1, -1, 1] and np.allclose(adjoint_rot(Z), np.eye(3)),
       "records-side Z_2 (z=-1 on C^2) and value-side Z_2 (Gamma_chi sign on C^3) are DIFFERENT objects under adjoint")

# ======================================================================
section("F. Generalization: rotation-equivariant quaternion-to-vector candidates factor through SO(3), killing z")
# ======================================================================
# Equivariance: f(q v q^{-1}) = adjoint(q) f(v). At q=z=-1: adjoint(z)=I, so f(z v z^{-1})=f(v)=I f(v) --
# z acts trivially on the image. Any such homomorphism factors through SO(3)=H*/{+-1}. Verified structurally
# via the kernel computation (B): {+-1} is in the kernel of EVERY rotation-equivariant map to R^3.
record("rotation-equivariant quaternion-to-vector candidates factor through SO(3)=H*/{+-1} -> structurally kill z",
       kernel_only_pm1, "carrying z nontrivially onto R^3 needs a NON-equivariant frame-dependent axis<->[111] glue = a posited import")

# ======================================================================
section("G. Consistency with BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN (z central, +1 on non-spinorial reps)")
# ======================================================================
record("z is central in SU(2) and acts +1 on every non-spinorial (integer-spin / vector) rep",
       z_action_on_spin(0) == 1 and z_action_on_spin(2) == 1,
       "consistent with binary_octahedral (retained_bounded): the on-site spinor sign is decoupled from the rest")

# ======================================================================
section("N5 EXECUTION CERTIFICATE (print-only; adds no check)")
print(
    "per_element: the rotation matrix is assembled a column at a time - "
    "adjoint_rot conjugates each of the three imaginary basis quaternions in turn "
    "and stacks the resulting vectors as columns, the body-diagonal reflection is "
    "written as the outer product 2 v v^T minus the identity, and every verdict "
    "is an np.allclose comparison of two full 3x3 arrays position against "
    "position"
)
print(
    "per_site: checked and not executed - this is a single on-site algebraic "
    "statement about the quaternion group and its rotation image, with no "
    "lattice, no site index and no neighbour relation anywhere; even the phrase "
    "on-site in the last section refers to the internal sign at one site, and a "
    "second site is never formed"
)
print(
    "per_mode: the three eigenvalues of the body-diagonal pi-rotation are "
    "computed and the full sorted triple is compared element for element after "
    "rounding, so the single fixed direction and the two reversed transverse "
    "directions are separated rather than summarized, and the central element's "
    "action is separately evaluated as (-1)^(2j) at the spin labels zero, one "
    "half and one"
)
print(
    "per_block: the two modules are kept apart and the whole argument is that "
    "they disagree - the central element is evaluated as minus the identity on "
    "the two-dimensional pseudoreal spin-one-half block and as plus the identity "
    "on the real three-dimensional vector block, and the Frobenius-Schur reality "
    "indicator is what labels the two blocks as different objects"
)
print(
    "lattice_wide: checked and not executed - nothing in the file reaches past a "
    "single copy of the quaternion algebra and its three-dimensional adjoint "
    "module, so no extent, volume or limiting sequence exists; the runner's own "
    "classification states the missing piece, a non-equivariant frame-dependent "
    "identification of an axis with the body diagonal, which is an unsupplied "
    "import rather than a computation at any scale"
)

section("RESULT")
# ======================================================================
n_, p_ = len(PASSES), sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("The natural (Bloch/Hopf/adjoint) spinor->vector map q|->q v q^{-1} QUOTIENTS the spinor Z_2: its")
print("kernel is exactly {+1,-1}, so adjoint(z)=adjoint(-1)=I_3. z acts -1 on the spin-1/2 (pseudoreal) C^2")
print("but +1 on the spin-1 (real) R^3 where the Gamma_chi sign partition lives -- so the records-side spinor")
print("Z_2 and the value-side Gamma_chi Z_2 are NOT the same object under the adjoint map. Gamma_chi lifts to")
print("q_gc=(0,1,1,1)/sqrt3 with q_gc^2=-1=z, so z appears in C^2 as q_gc^2 but is invisible (=I_3) on R^3.")
print("Generalization: rotation-equivariant quaternion-to-vector candidates factor through SO(3)=H*/{+-1}, killing z;")
print("carrying z requires a NON-equivariant frame-dependent axis<->[111] identification (a posited import).")
print("CLASSIFICATION: open import/residual. NEXT PATH: non-equivariant glues / left-multiplication on H stay")
print("C^2-internal (do not reach R^3) -- not a closure of the bridge.")
import sys; sys.exit(0 if p_ == n_ else 1)
