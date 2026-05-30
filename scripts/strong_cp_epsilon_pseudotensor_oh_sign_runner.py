"""Runner: Wilson invariance and epsilon-pseudotensor O_h sign law.

Verifies the narrow theorem in
docs/STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE_BOUNDED_NOTE_2026-05-26.md:

  (WILSON) Wilson plaquette action S_W = -(β/N_c) Σ Re tr(U_P) is
       O_h-invariant under permutation of plaquettes.
  (EPSILON) 4D Levi-Civita with one temporal index, ε^{0ijk} = ε^{ijk}, is
       an O_h pseudotensor: ε → det(R) · ε.
  (QSIGN) Generic determinant-odd slot Q = ε^{ijk} F_{0i} F_{jk}
       transforms as Q → det(R) · Q under O_h whenever F transforms as
       an antisymmetric rank-two tensor.

Concrete verification: small spatial-cubic lattice; random SU(3) link
variables for Wilson check; random F-tensors for structural ε·F·F
check. Exclusion of a physical action coefficient remains conditional
on a separate O_h-invariant action-class result.
"""

from __future__ import annotations

import itertools

import numpy as np

RNG = np.random.default_rng(20260526)


# ----------------------------------------------------------------------
# SU(3) sampling
# ----------------------------------------------------------------------

GELL_MANN = [
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
    np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
    np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
    np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
    np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
    np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
    np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
    np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3),
]


def random_su3():
    from scipy.linalg import expm
    coeffs = RNG.normal(0, 1.0, size=8)
    H = sum(c * g / 2 for c, g in zip(coeffs, GELL_MANN))
    U = expm(1j * H)
    return U / np.linalg.det(U)**(1 / 3)


# ----------------------------------------------------------------------
# Tiny 2×2×2 lattice
# ----------------------------------------------------------------------

L_S = 2
SPATIAL_DIRS = [0, 1, 2]


def all_o_h():
    out = []
    for perm in itertools.permutations([0, 1, 2]):
        for signs in itertools.product([+1, -1], repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for r, (c, s) in enumerate(zip(perm, signs)):
                M[r, c] = s
            out.append(M)
    return out


def o_h_act_on_site(R, x):
    new = np.array([sum(R[i, j] * x[j] for j in range(3)) for i in range(3)])
    return tuple(int(v % L_S) for v in new)


def build_random_config():
    cfg = {}
    for x in itertools.product(range(L_S), repeat=3):
        for mu in SPATIAL_DIRS:
            cfg[(x, mu)] = random_su3()
    return cfg


def plaquette(cfg, x, mu, nu):
    e_mu = tuple((x[i] + (1 if i == mu else 0)) % L_S for i in range(3))
    e_nu = tuple((x[i] + (1 if i == nu else 0)) % L_S for i in range(3))
    U1 = cfg[(x, mu)]
    U2 = cfg[(e_mu, nu)]
    U3 = cfg[(e_nu, mu)].conj().T
    U4 = cfg[(x, nu)].conj().T
    return U1 @ U2 @ U3 @ U4


def all_plaquettes(cfg):
    out = []
    for x in itertools.product(range(L_S), repeat=3):
        for mu, nu in itertools.combinations(SPATIAL_DIRS, 2):
            out.append(plaquette(cfg, x, mu, nu))
    return out


def wilson_action(cfg, beta=2.0, N_c=3):
    s = 0.0
    for U_P in all_plaquettes(cfg):
        s += np.trace(U_P).real
    return -(beta / N_c) * s


def transform_config(cfg, R):
    """Apply signed-permutation R ∈ O_h to gauge configuration."""
    new_cfg = {}
    for x in itertools.product(range(L_S), repeat=3):
        Rx = o_h_act_on_site(R, x)
        for mu in SPATIAL_DIRS:
            j = [k for k in range(3) if R[mu, k] != 0][0]
            sign = R[mu, j]
            U_orig = cfg[(x, mu)]
            if sign == +1:
                new_cfg[(Rx, j)] = U_orig
            else:
                Rx_neighbor = tuple((Rx[i] - (1 if i == j else 0)) % L_S for i in range(3))
                new_cfg[(Rx_neighbor, j)] = U_orig.conj().T
    return new_cfg


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------

PASS = 0
FAIL = 0


def report(name, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    PASS += int(ok)
    FAIL += int(not ok)
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def test_wilson_invariance(cfg, R_proper_list, R_improper_list):
    """Wilson action is invariant under all O_h.

    Key fact: Re tr(U_P) is invariant under both cyclic permutation and
    U → U^†, so the per-plaquette Wilson contribution doesn't care about
    orientation. The set of plaquettes is just permuted by R."""
    S_W_orig = wilson_action(cfg)
    all_ok = True
    fail_count = 0
    for R in R_proper_list + R_improper_list:
        cfg_R = transform_config(cfg, R)
        S_W_R = wilson_action(cfg_R)
        if not np.isclose(S_W_orig, S_W_R, atol=1e-8):
            all_ok = False
            fail_count += 1
    report(f"Wilson action invariant under {len(R_proper_list) + len(R_improper_list)} O_h elements",
           all_ok, detail=f"S_W = {S_W_orig:.4f}")


def test_levi_civita_pseudotensor():
    """3D Levi-Civita ε_{ijk} transforms with det(R) under all 48 O_h."""
    eps = np.zeros((3, 3, 3), dtype=int)
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1

    all_ok = True
    for R in all_o_h():
        Reps = np.einsum('ia,jb,kc,abc->ijk', R.astype(float), R.astype(float),
                         R.astype(float), eps.astype(float))
        det_R = int(round(np.linalg.det(R)))
        expected = det_R * eps
        if not np.allclose(Reps, expected, atol=1e-9):
            all_ok = False
            break
    report(f"epsilon_{{ijk}} -> det(R)*epsilon for all 48 O_h elements", all_ok)


def test_qsign_density_structural(R_proper_list, R_improper_list, n_trials=5):
    """Q = ε^{ijk} F_{0i} F_{jk} transforms with det(R) for any rank-2
    antisymmetric F tensor.

    This is the index-contraction identity. Concrete discretizations can
    use it only after their rank-two O_h covariance has been established.
    Verify on randomly sampled abstract F tensors.
    """
    eps = np.zeros((3, 3, 3), dtype=int)
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1

    all_ok_proper = True
    all_ok_improper = True
    for _ in range(n_trials):
        # Sample F^{(r)}_{0i} (3-vector, possibly complex/SU(N)-valued)
        F_0i = RNG.normal(size=3) + 1j * RNG.normal(size=3)
        # Sample F^{(r)}_{ij} (3x3 antisymmetric)
        F_ij = np.zeros((3, 3), dtype=complex)
        for i in range(3):
            for j in range(i + 1, 3):
                v = RNG.normal() + 1j * RNG.normal()
                F_ij[i, j] = v
                F_ij[j, i] = -v

        # Q = ε^{ijk} F_{0i} F_{jk}  (the 4D ε^{μνρσ} F·F restricted to one temporal)
        Q_orig = np.einsum('ijk,i,jk->', eps.astype(complex), F_0i, F_ij)

        for R in R_proper_list:
            R_f = R.astype(float)
            F_0i_R = np.einsum('ij,j->i', R_f, F_0i)
            F_ij_R = np.einsum('ij,kl,jl->ik', R_f, R_f, F_ij)
            Q_R = np.einsum('ijk,i,jk->', eps.astype(complex), F_0i_R, F_ij_R)
            if not np.isclose(Q_orig, Q_R, atol=1e-9):
                all_ok_proper = False
                break

        for R in R_improper_list:
            R_f = R.astype(float)
            F_0i_R = np.einsum('ij,j->i', R_f, F_0i)
            F_ij_R = np.einsum('ij,kl,jl->ik', R_f, R_f, F_ij)
            Q_R = np.einsum('ijk,i,jk->', eps.astype(complex), F_0i_R, F_ij_R)
            if not np.isclose(Q_orig, -Q_R, atol=1e-9):
                all_ok_improper = False
                break

    report(f"Q = epsilon^{{ijk}} F_{{0i}} F_{{jk}} invariant under proper R ({n_trials} F samples x {len(R_proper_list)} R)",
           all_ok_proper)
    report(f"Q = epsilon^{{ijk}} F_{{0i}} F_{{jk}} sign-flips under improper R ({n_trials} F samples x {len(R_improper_list)} R)",
           all_ok_improper)


def test_sample_labels_share_index_law():
    """Different abstract F samples share the index law.

    These labels are diagnostics only. They do not prove covariance of any
    named lattice field-strength discretization.
    """
    eps = np.zeros((3, 3, 3), dtype=int)
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1

    # Three different abstract samples with labels used only for diagnostics.
    R = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=int)  # single-axis reflection
    R_f = R.astype(float)
    det_R = int(round(np.linalg.det(R)))

    all_ok = True
    for label in ["sample_F_0", "sample_F_1", "sample_F_2"]:
        F_0i = RNG.normal(size=3) + 1j * RNG.normal(size=3)
        F_ij = np.zeros((3, 3), dtype=complex)
        for i in range(3):
            for j in range(i + 1, 3):
                v = RNG.normal() + 1j * RNG.normal()
                F_ij[i, j] = v
                F_ij[j, i] = -v

        Q_orig = np.einsum('ijk,i,jk->', eps.astype(complex), F_0i, F_ij)
        F_0i_R = np.einsum('ij,j->i', R_f, F_0i)
        F_ij_R = np.einsum('ij,kl,jl->ik', R_f, R_f, F_ij)
        Q_R = np.einsum('ijk,i,jk->', eps.astype(complex), F_0i_R, F_ij_R)
        ratio = Q_R / Q_orig if abs(Q_orig) > 1e-12 else float('nan')

        ok = np.isclose(ratio, det_R, atol=1e-9)
        report(f"{label}: Q_R / Q_orig = det(R) = {det_R}",
               ok, detail=f"ratio = {ratio:.4f}")
        if not ok:
            all_ok = False
    return all_ok


def test_o_h_count():
    """Sanity: |O_h| = 48 with 24+24 split."""
    o_h = all_o_h()
    n = len(o_h)
    proper = sum(1 for R in o_h if np.linalg.det(R) > 0)
    improper = sum(1 for R in o_h if np.linalg.det(R) < 0)
    report("|O_h| = 48", n == 48, detail=f"got {n}")
    report("24 proper + 24 improper rotations",
           proper == 24 and improper == 24,
           detail=f"proper={proper}, improper={improper}")


def main():
    print("=" * 76)
    print("STRONG-CP SUPPORT: EPSILON-PSEUDOTENSOR O_h SIGN BRIDGE")
    print("=" * 76)
    print()

    o_h = all_o_h()
    R_proper = [R for R in o_h if np.linalg.det(R) > 0]
    R_improper = [R for R in o_h if np.linalg.det(R) < 0]

    print("Sanity: O_h structure")
    print("-" * 76)
    test_o_h_count()

    # Build a random gauge config
    print()
    print("Wilson plaquette action is O_h-invariant")
    print("-" * 76)
    cfg = build_random_config()
    test_wilson_invariance(cfg, R_proper[:6], R_improper[:6])

    print()
    print("Levi-Civita with one temporal index is O_h-pseudotensor")
    print("-" * 76)
    test_levi_civita_pseudotensor()

    print()
    print("Epsilon F F slot transforms as Q -> det(R) * Q")
    print("-" * 76)
    test_qsign_density_structural(R_proper[:6], R_improper[:6], n_trials=5)

    print()
    print("Multiple abstract F samples share the same index law")
    print("-" * 76)
    test_sample_labels_share_index_law()

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: Wilson plaquette invariance and epsilon-pseudotensor")
        print("sign law hold on the bounded checks; coefficient exclusion")
        print("remains conditional on a separate O_h-invariant action-class")
        print("result.")
        return 0
    print("VERDICT: epsilon-pseudotensor O_h sign bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
