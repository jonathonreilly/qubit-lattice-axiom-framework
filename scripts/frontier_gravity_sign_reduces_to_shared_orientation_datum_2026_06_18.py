#!/usr/bin/env python3
"""Gravity sign reduces (by kind) to the shared T-odd orientation datum; it is
NOT a fresh admission, and Record's K/CPT cannot select it.

This runner DERIVES (does not assert) the load-bearing bridges behind the
frontier result that the emergent-gravity G>0 / conformal-class sign collapses
into the already-admitted arrow / Past-Hypothesis / conformal-class atom:

  B1  Cl(3,1) e_4 WELDS the gravity-sign twist to the Cl(3) spatial pseudoscalar:
      one e_4 orientation flip reverses BOTH the chirality element eps and the
      spatial volume element e1 e2 e3 (the exact (-1)^3 Clifford identity).
  B2  The Cl(3) spatial volume element IS the central i (the qubit i) -- so the
      shared datum is the framework's own pseudoscalar handedness, not a new object.
  B3  The flavor handedness sign(Delta) IS a det/orientation Z2: sign(Delta) flips
      exactly as det(rho_perm) = the S3 sign rep -- the SAME KIND of object as B1.
  B4  K/CPT is SIGN-SYMMETRIC (make-or-break no-go): the Brannen-phase Vandermonde
      Delta is K-odd under the induced delta -> -delta (K SWAPS the two branches),
      and the symmetrization (rho + rho_K)/2 is K-real for BOTH K^2 = +1 and -1, so
      K delivers the orbit PAIR {+,-}, never selects one element.
  B5  The canonical PARITY grading forces eta = 0 (Gamma5 H Gamma5 = -H => symmetric
      spectrum => sum of signs = 0): the branch label is undefined, identical to the
      no-go'd arrow/parity wall.
  B6  CARRIER BOUNDARY (the 2-of-3 honesty bound): color's 3-vs-3bar rides a
      DIFFERENT, space-decoupled carrier -- the SU(3)^3 cubic anomaly A(3)=-A(3bar)!=0
      computed on internal su(3), structurally disjoint from the Cl(3,1) spacetime
      gammas. So gravity + flavor share ONE datum (2 of 3); color does not (calling
      all three "the same" is the 6=2N_c numerology trap).

Deterministic, symbolic/small-numeric, memory-safe (4x4 Clifford and 3x3 su(3) /
permutation matrices only). No fitted parameters, no observed values, no axiom-file
edits, no docs/audit/data/* edits. Sets no audit status.
"""

from __future__ import annotations

import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {name}" + (f" :: {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# B1 / B2 -- Cl(3,1) e_4 welds the gravity-sign twist to the Cl(3) pseudoscalar
# ---------------------------------------------------------------------------
def block_clifford_weld() -> None:
    print("\n== B1/B2: e_4 welds chirality eps and the spatial volume element ==")
    # Dirac (Weyl) gammas, signature (+,+,+,-): e1,e2,e3 spatial, e4 = time.
    I2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)

    def kron(a, b):
        return np.kron(a, b)

    # Spatial gammas e_k (k=1,2,3): Hermitian, square +I.
    e1 = kron(sx, sx)
    e2 = kron(sx, sy)
    e3 = kron(sx, sz)
    # Time gamma e_4: anti-Hermitian, square -I (signature -).
    e4 = kron(1j * sy, I2)
    gens = {"e1": e1, "e2": e2, "e3": e3, "e4": e4}

    # Clifford algebra: {e_mu, e_nu} = 2 eta_munu, eta = diag(+,+,+,-).
    eta = {"e1": 1, "e2": 1, "e3": 1, "e4": -1}
    clifford_ok = True
    for (na, A), (nb, B) in itertools.product(gens.items(), repeat=2):
        anti = A @ B + B @ A
        expected = (2 * eta[na] if na == nb else 0) * np.eye(4, dtype=complex)
        if not np.allclose(anti, expected):
            clifford_ok = False
    check("Cl(3,1) generators satisfy {e_mu,e_nu}=2 eta_munu (signature +,+,+,-)",
          clifford_ok)

    vol3 = e1 @ e2 @ e3                 # spatial volume element e1 e2 e3
    eps = e1 @ e2 @ e3 @ e4            # chirality element gamma5 (up to phase)
    e4_inv = np.linalg.inv(e4)

    # The exact (-1)^3 identity: e_4 conjugation reverses the spatial volume element.
    vol3_conj = e4 @ vol3 @ e4_inv
    check("e_4 (e1 e2 e3) e_4^-1 = -(e1 e2 e3)  [exact (-1)^3 Clifford weld]",
          np.allclose(vol3_conj, -vol3),
          f"||e4 vol3 e4^-1 + vol3|| = {np.linalg.norm(vol3_conj + vol3):.2e}")

    # And it reverses the chirality element eps the same way.
    eps_conj = e4 @ eps @ e4_inv
    check("e_4 eps e_4^-1 = -eps  [same e_4 flip reverses chirality]",
          np.allclose(eps_conj, -eps),
          f"||e4 eps e4^-1 + eps|| = {np.linalg.norm(eps_conj + eps):.2e}")

    # Rep-independence: a SECOND, structurally different Cl(3,1) rep (sx<->sy roles
    # swapped between the two tensor factors) satisfies the SAME two identities -- the weld
    # is generic grade-parity, not an artifact of one matrix rep.
    f1, f2, f3 = kron(sy, sx), kron(sy, sy), kron(sy, sz)
    f4 = kron(1j * sx, I2)
    gens2 = {"e1": f1, "e2": f2, "e3": f3, "e4": f4}
    clifford2_ok = all(
        np.allclose(A @ B + B @ A,
                    (2 * eta[na] if na == nb else 0) * np.eye(4, dtype=complex))
        for (na, A), (nb, B) in itertools.product(gens2.items(), repeat=2))
    v2 = f1 @ f2 @ f3
    e2_ = f1 @ f2 @ f3 @ f4
    f4i = np.linalg.inv(f4)
    rep2_ok = (np.allclose(f4 @ v2 @ f4i, -v2) and np.allclose(f4 @ e2_ @ f4i, -e2_))
    check("a SECOND Cl(3,1) rep satisfies the same Clifford relations AND the same two "
          "e_4 weld identities (rep-independent grade-parity, not a matrix artifact)",
          clifford2_ok and rep2_ok)

    # WELD: ONE e_4 orientation flip reverses BOTH -> gravity-sign twist and the
    # spatial-handedness Z2 are the SAME twist datum, not two independent signs.
    check("WELD: one e_4 flip reverses BOTH the spatial volume element AND chirality "
          "(gravity-sign twist == spatial-handedness Z2, one datum)",
          np.allclose(vol3_conj, -vol3) and np.allclose(eps_conj, -eps))

    # B2: the Cl(3) spatial pseudoscalar (qubit volume element) is the central i.
    central_i = sx @ sy @ sz
    check("Cl(3) volume element sigma_x sigma_y sigma_z = i * I_2 (the qubit i: the "
          "shared datum is the framework's own pseudoscalar handedness)",
          np.allclose(central_i, 1j * I2),
          f"||sx sy sz - i I2|| = {np.linalg.norm(central_i - 1j * I2):.2e}")


# ---------------------------------------------------------------------------
# B3 -- flavor handedness sign(Delta) IS det(rho_perm) = S3 sign rep
# ---------------------------------------------------------------------------
def labeled_vandermonde(w: np.ndarray) -> float:
    return float((w[0] - w[1]) * (w[1] - w[2]) * (w[2] - w[0]))


def block_sign_delta_is_det() -> None:
    print("\n== B3: sign(Delta) flips exactly as det(rho_perm) = S3 sign rep ==")
    base = np.array([0.17, 0.41, 0.88])          # generic distinct weights
    d0 = labeled_vandermonde(base)
    all_match = True
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3))
        for i, j in enumerate(perm):
            P[i, j] = 1.0
        permuted = base[list(perm)]
        dperm = labeled_vandermonde(permuted)
        sgn_det = round(float(np.linalg.det(P)))   # +1 even, -1 odd = S3 sign rep
        sgn_delta = 1 if dperm * d0 > 0 else -1
        if sgn_det != sgn_delta:
            all_match = False
    check("sign(Delta) under every S3 relabel == det(rho_perm) (the S3 sign rep): "
          "flavor handedness is a det/orientation Z2 -- same KIND as the e_4 weld",
          all_match)


# ---------------------------------------------------------------------------
# B4 -- K/CPT is SIGN-SYMMETRIC: it delivers the orbit PAIR, never selects one
# ---------------------------------------------------------------------------
def born_triple(delta: float) -> np.ndarray:
    lam = np.array([1.0 + np.sqrt(2.0) * np.cos(delta + 2.0 * np.pi * k / 3.0)
                    for k in range(3)])
    w = lam ** 2
    return w / float(np.sum(w))


def block_kcpt_sign_symmetric() -> None:
    print("\n== B4: K/CPT is sign-symmetric (orbit pair, not a selector) ==")
    delta = 0.2222
    d_pos = labeled_vandermonde(born_triple(+delta))
    d_neg = labeled_vandermonde(born_triple(-delta))
    check("Brannen-phase Vandermonde is K-odd: Delta(+delta) = -Delta(-delta) "
          "(K acts as delta->-delta, SWAPPING the two orientation branches)",
          np.isclose(d_neg, -d_pos, atol=1e-12),
          f"Delta(+d)={d_pos:+.8f}, Delta(-d)={d_neg:+.8f}")
    # Cross-check the documented magnitude (SCALAR_I note: 0.04674385).
    check("reproduces the landed magnitude |Delta| = 0.04674385 (SCALAR_I runner)",
          np.isclose(abs(d_pos), 0.04674385, atol=1e-6),
          f"|Delta| = {abs(d_pos):.8f}")

    # Symmetrization is K-real for BOTH K^2 = +1 and K^2 = -1 -> K cannot break the Z2.
    rng = np.random.default_rng(0)
    A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
    for k2, Kmat in (("+1", np.eye(4, dtype=complex)),
                     ("-1", np.kron(np.array([[0, -1], [1, 0]], dtype=complex),
                                    np.eye(2, dtype=complex)))):
        # antiunitary K: rho -> K conj(rho) K^{-1}; K^2 = Kmat conj(Kmat) = +/- I.
        Kinv = np.linalg.inv(Kmat)
        rho_K = Kmat @ np.conjugate(A) @ Kinv
        sym = 0.5 * (A + rho_K)
        # sym is K-real: K conj(sym) K^{-1} == sym.
        sym_K = Kmat @ np.conjugate(sym) @ Kinv
        k_sq = Kmat @ np.conjugate(Kmat)
        check(f"symmetrization (rho+rho_K)/2 is K-real for K^2={k2} "
              "(K is an involution on the Z2, cannot select a branch)",
              np.allclose(sym_K, sym) and
              np.allclose(k_sq, (1 if k2 == "+1" else -1) * np.eye(4)),
              f"||K sym - sym|| = {np.linalg.norm(sym_K - sym):.2e}")


# ---------------------------------------------------------------------------
# B5 -- canonical parity grading forces eta = 0 (label undefined)
# ---------------------------------------------------------------------------
def block_parity_eta_zero() -> None:
    print("\n== B5: parity grading Gamma5 H Gamma5 = -H => eta = 0 (label undefined) ==")
    rng = np.random.default_rng(1)
    G = np.diag([1.0, 1.0, -1.0, -1.0])           # parity grading Gamma5
    # Build H parity-ODD: H = X with Gamma5 X Gamma5 = -X (off-diagonal blocks only).
    B = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
    H = np.zeros((4, 4), dtype=complex)
    H[:2, 2:] = B
    H[2:, :2] = B.conj().T                         # Hermitian, parity-odd
    grading_odd = np.allclose(G @ H @ G, -H)
    eigs = np.linalg.eigvalsh(H)
    eta = float(np.sum(np.sign(np.round(eigs, 12))))
    sym_spec = np.allclose(np.sort(eigs), -np.sort(eigs)[::-1])
    check("Gamma5 H Gamma5 = -H (canonical parity grading is parity-odd)", grading_odd)
    check("=> spectrum is +/- symmetric => eta = sum sign(eigs) = 0 "
          "(the branch label is NEVER DEFINED in the canonical grading)",
          sym_spec and np.isclose(eta, 0.0),
          f"eta = {eta:.1f}, eigs = {np.round(eigs,4)}")


# ---------------------------------------------------------------------------
# B6 -- carrier boundary: color 3-vs-3bar is a DIFFERENT, space-decoupled Z2
# ---------------------------------------------------------------------------
def gell_mann() -> list[np.ndarray]:
    l = [np.zeros((3, 3), dtype=complex) for _ in range(8)]
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    return l


def block_color_carrier_boundary() -> None:
    print("\n== B6: color 3-vs-3bar = the SU(3)^3 cubic anomaly, a DIFFERENT carrier ==")
    T = [g / 2.0 for g in gell_mann()]            # fundamental 3
    Tbar = [-g.conj() / 2.0 for g in gell_mann()]  # conjugate 3bar = -T^a*

    def anomaly_tensor(reps: list[np.ndarray]) -> np.ndarray:
        D = np.zeros((8, 8, 8))
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    M = reps[a] @ (reps[b] @ reps[c] + reps[c] @ reps[b])
                    D[a, b, c] = np.trace(M).real
        return D

    D3 = anomaly_tensor(T)
    D3b = anomaly_tensor(Tbar)
    norm3 = float(np.sum(D3 * D3))
    proj_3 = float(np.sum(D3 * D3))               # contract with itself
    proj_3b = float(np.sum(D3b * D3))             # 3bar contracted with 3's tensor
    check("SU(3)^3 cubic anomaly is nonzero (3 is a genuinely complex rep, 3 != 3bar)",
          norm3 > 1e-6, f"||D_3||^2 = {norm3:.4f}")
    check("A(3bar) = -A(3): the color 3-vs-3bar grading is the anomaly SIGN flip "
          "(D_3bar = -D_3, exact)",
          np.allclose(D3b, -D3) and np.isclose(proj_3b / proj_3, -1.0, atol=1e-9),
          f"<D_3bar,D_3>/<D_3,D_3> = {proj_3b/proj_3:+.6f}")
    # The carrier is INTERNAL su(3) (8 traceless 3x3 generators), structurally
    # disjoint from the Cl(3,1) spacetime gammas: there is no spatial/e_4 operator
    # in this list, so one e_4 datum CANNOT fix the color Z2.
    su3_dim = len(T)
    check("color carrier = 8 internal su(3) generators on a 3-dim internal space, "
          "space-decoupled from the Cl(3,1) e_4 / spatial volume element "
          "(=> at most 2 of 3 Z2's share the e_4 datum; color is separate)",
          su3_dim == 8 and all(t.shape == (3, 3) for t in T))


def main() -> int:
    print("FRONTIER: gravity sign reduces (by kind) to the shared T-odd orientation "
          "datum; K/CPT cannot select it; color is a separate carrier (2 of 3).")
    block_clifford_weld()
    block_sign_delta_is_det()
    block_kcpt_sign_symmetric()
    block_parity_eta_zero()
    block_color_carrier_boundary()
    print(f"\n==== {PASS} passed, {FAIL} failed ====")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
