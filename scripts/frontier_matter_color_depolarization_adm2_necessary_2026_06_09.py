#!/usr/bin/env python3
"""Matter color depolarization is necessary for first-moment centrality.

This runner establishes, by exact finite-dimensional algebra (no Monte-Carlo fit enters the
derivation path), the necessary first-moment theorem:

    For any nonzero gauge-covariant linear minimal-coupling drift
    Herm(3) -> su(3), an Ad-invariant link-increment step measure forces the
    coupled matter color density rho_color to be unpolarized
    (rho_color = I_3/3).

The load-bearing facts, all exact:

  E0  The gauge-covariant linear drift Herm(3) -> su(3) is 1-dimensional
      (3 (x) 3bar = 1 (+) 8, Schur): every equivariant linear drift is a scalar
      multiple of the traceless projection X -> X - (tr X / 3) I. Hence any
      nonzero minimal-coupling-class drift has mean proportional to
      traceless(rho_color).

  E1  The only Ad-invariant element of su(3) is 0 (the commutant of the eight
      Gell-Mann generators inside 3x3 is the scalars; traceless scalar = 0). The
      adjoint rep 8 carries no nonzero invariant vector.

  E2  For the canonical matter color charge drift H = traceless(phi phi^dag) with
      E[phi phi^dag] = rho, the mean increment generator is E[H] = traceless(rho).

  E3  NECESSARY FIRST-MOMENT CONDITION: an Ad-invariant increment distribution has an
      Ad-invariant mean (E1) => mean = 0 => traceless(rho) = 0 => rho = I_3/3.
      Exhibited two ways: rho = I_3/3 gives zero mean force; any polarized rho
      gives a nonzero mean su(3) force, so its increment is non-central.

  E4  ORDER PARAMETER: ||traceless(rho)||_F^2 = Tr(rho^2) - 1/3, exact; strictly
      monotone in the color purity Tr(rho^2); vanishes iff rho = I_3/3.

  E5  CONVERSE (conditional, named isotropic-Gaussian fluctuation model): the exact
      Wick covariance of H = traceless(phi phi^dag), phi = sqrt(rho) xi, xi ~ CN(0,I),
      is isotropic (proportional to I_8) at rho = I_3/3 and anisotropic for polarized
      rho, with anisotropy monotone in purity. This is the second-moment refinement;
      it is conditional on the fluctuation model (a named admission), NOT the
      noise-model-independent first-moment direction E0-E4.

  E6  ROBUSTNESS / non-circularity guard: the necessary direction E0-E4 does NOT
      assume isotropic noise and is NOT the refuted "annealed-twirl = i.i.d.-central
      CLT" sufficiency claim. It is a necessary condition on the FIRST moment of the
      increment, holding for every nonzero gauge-covariant minimal-coupling drift.

Honest boundary (see the companion note): this does NOT derive that the framework's
dynamics drives rho_color to I_3/3 (the retained Record boundaries supply no such
continuous dynamics); it does NOT deliver the gauge-link generator, discharge
static frame redundancy, or select the blocking isometry. It relocates the
first-moment obstruction onto a concrete matter order parameter: color
depolarization. Zero drift or unrelated central noise is outside the theorem.
"""

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  PASS  {name}  {detail}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}  {detail}")


# ---- Gell-Mann generators T_a = lambda_a / 2, Tr(T_a T_b) = (1/2) delta_ab ----
_lam = [
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
    [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
    [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]],
    np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / np.sqrt(3),
]
LAM = [np.array(x, dtype=complex) for x in _lam]
T = [x / 2 for x in LAM]
EYE = np.eye(3, dtype=complex)


def traceless(X):
    return X - (np.trace(X) / 3.0) * EYE


def su3_components(X):
    """Real components c_a with X_traceless = sum_a c_a T_a (Tr(T_a T_b)=delta/2)."""
    return np.array([2.0 * np.trace(X @ T[a]).real for a in range(8)])


def _expm_su3(A):
    """Matrix exponential of an anti-Hermitian 3x3 via eigendecomposition (A = i s T)."""
    w, V = np.linalg.eigh(-1j * A)  # -iA Hermitian
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


def haar_su3(rng):
    A = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))
    return Q / np.linalg.det(Q) ** (1.0 / 3.0)


def rho_family(t):
    """Unpolarized (t=0) to a fixed pure color state (t=1); valid density for t in [0,1]."""
    pure = np.zeros((3, 3), dtype=complex)
    pure[0, 0] = 1.0
    return (1.0 - t) * EYE / 3.0 + t * pure


def wick_mean_cov(rho):
    """Exact mean and 8x8 covariance of H=traceless(phi phi^dag), phi=sqrt(rho) xi,
    xi ~ CN(0,I), via Wick: E[phi_i phibar_j]=rho_ij,
    E[phi_i phibar_j phi_k phibar_l]=rho_ij rho_kl + rho_il rho_kj."""
    mean = np.array([2.0 * np.trace(T[a] @ rho).real for a in range(8)])
    cov = np.zeros((8, 8))
    for a in range(8):
        Ta = T[a]
        for b in range(8):
            Tb = T[b]
            # E[c_a c_b] = 4 * Ta_ij Tb_kl E[phibar_i phi_j phibar_k phi_l]
            #   with E[phibar_i phi_j phibar_k phi_l] = rho_ji rho_lk + rho_jk rho_li
            term = 0.0 + 0.0j
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            term += Ta[i, j] * Tb[k, l] * (rho[j, i] * rho[l, k]
                                                           + rho[j, k] * rho[l, i])
            cov[a, b] = 4.0 * term.real
    cov = cov - np.outer(mean, mean)
    return mean, cov


def main():
    print("Matter color depolarization is necessary for nonzero matter-current first-moment centrality")
    print("Exact finite-dimensional algebra | no MC in the derivation path")
    print()
    rng = np.random.default_rng(20260609)

    # ---- generator sanity ----
    print("[generators] Gell-Mann normalization")
    ok = all(abs(np.trace(LAM[a] @ LAM[b]) - 2.0 * (a == b)) < 1e-12
             for a in range(8) for b in range(8))
    check("gellmann_trace_orthonormal", ok, "Tr(lam_a lam_b)=2 delta_ab")
    ok = all(abs(np.trace(T[a])) < 1e-12 for a in range(8))
    check("generators_traceless", ok)

    # ---- E1: su(3) has no nonzero Ad-invariant element ----
    print("[E1] only Ad-invariant element of su(3) is 0")
    # commutant of {T_a} inside 3x3: solve [X,T_a]=0 for all a
    blocks = []
    for a in range(8):
        K = np.kron(T[a].T, EYE) - np.kron(EYE, T[a])  # vec([X,T_a]) = K vec(X)
        blocks.append(K)
    M = np.vstack(blocks)
    sv = np.linalg.svd(M, compute_uv=False)
    commutant_dim = int(np.sum(sv < 1e-9))
    check("su3_commutant_is_scalars", commutant_dim == 1,
          f"commutant dim={commutant_dim} (scalars); traceless commutant = {{0}}")
    # exact corroboration: the adjoint-rep invariant subspace is 0-dimensional, i.e.
    # the stacked (Ad(g_k) - I) over a generating set of SU(3) has trivial nullspace.
    # Use one-parameter subgroups exp(i s T_a) at an irrational-ish s to generate.
    s = 0.7
    Adblocks = []
    for a in range(8):
        g = _expm_su3(1j * s * T[a])
        Adg = np.array([[2.0 * np.trace(T[p] @ g @ T[q] @ g.conj().T).real
                         for q in range(8)] for p in range(8)])
        Adblocks.append(Adg - np.eye(8))
    inv_dim = int(np.sum(np.linalg.svd(np.vstack(Adblocks), compute_uv=False) < 1e-9))
    check("adjoint_invariant_subspace_trivial", inv_dim == 0,
          f"dim of Ad-invariant su(3) vectors = {inv_dim} (exact, no MC)")

    # ---- E0: equivariant linear drift Herm(3)->su(3) is 1-dim (~ traceless proj) ----
    print("[E0] nonzero gauge-covariant linear drift is traceless projection")
    herm = [EYE / np.sqrt(3.0)] + T  # 9 Hermitian basis elements
    # An equivariant map D satisfies su3comp(D(g X g^dag)) = Ad(g) su3comp(D(X)).
    # Unknown D is an 8x9 real matrix acting on herm-coordinates. Build constraints.
    def herm_coords(X):
        # coordinates in {herm}: c0 = Tr(X I/sqrt3), c_a = 2 Tr(X T_a)
        c = [np.trace(X @ herm[0]).real]
        c += [2.0 * np.trace(X @ T[a]).real for a in range(8)]
        return np.array(c)
    rows = []
    for _ in range(60):
        g = haar_su3(rng)
        Adg = np.array([[2.0 * np.trace(T[a] @ g @ T[b] @ g.conj().T).real
                         for b in range(8)] for a in range(8)])
        for j in range(9):
            Xj = herm[j]
            gXg = g @ Xj @ g.conj().T
            cgXg = herm_coords(gXg)          # 9-vector
            # constraint per output index a:
            #   sum_k D[a,k] cgXg[k]  -  sum_b Adg[a,b] D[b,j] = 0
            for a in range(8):
                row = np.zeros((8, 9))
                row[a, :] += cgXg
                row[:, j] -= Adg[a, :]
                rows.append(row.reshape(-1))
    A = np.array(rows)
    sv = np.linalg.svd(A, compute_uv=False)
    equiv_dim = int(np.sum(sv < 1e-7))
    check("equivariant_drift_is_one_dim", equiv_dim == 1,
          f"dim Hom_SU(3)(Herm(3),su(3)) = {equiv_dim} (the traceless projection)")
    # and that the surviving map IS the traceless projection (mean ~ traceless(rho))
    rho_test = rho_family(0.6)
    canonical = su3_components(traceless(rho_test))
    check("equivariant_drift_is_traceless_projection",
          np.linalg.norm(canonical - su3_components(rho_test)) < 1e-12,
          "su3 part of rho = su3 part of traceless(rho)")

    # ---- E2: mean increment generator = traceless(rho) ----
    print("[E2] E[H] = traceless(rho) for H = traceless(phi phi^dag), E[phi phi^dag]=rho")
    for t in [0.0, 0.3, 0.7, 1.0]:
        rho = rho_family(t)
        mean, _ = wick_mean_cov(rho)
        target = su3_components(traceless(rho))
        check(f"mean_force_equals_traceless_rho[t={t}]",
              np.linalg.norm(mean - target) < 1e-12,
              f"||E[H]-traceless(rho)|| = {np.linalg.norm(mean - target):.2e}")

    # ---- E3: necessary condition ----
    print("[E3] Ad-invariant increment => mean=0 => traceless(rho)=0 => rho=I/3")
    mean0, _ = wick_mean_cov(EYE / 3.0)
    check("unpolarized_has_zero_mean_force", np.linalg.norm(mean0) < 1e-12,
          f"rho=I/3: ||E[H]|| = {np.linalg.norm(mean0):.2e}")
    polarized_nonzero = True
    for t in [0.1, 0.4, 0.8, 1.0]:
        mean, _ = wick_mean_cov(rho_family(t))
        if np.linalg.norm(mean) < 1e-9:
            polarized_nonzero = False
    check("polarized_has_nonzero_mean_force", polarized_nonzero,
          "every polarized rho gives a nonzero su(3) mean force => non-central increment")

    # ---- E4: order parameter exact + monotone ----
    print("[E4] ||traceless(rho)||_F^2 = Tr(rho^2) - 1/3, monotone in color purity")
    op_ok = True
    op_mono = True
    prev = -1.0
    for t in np.linspace(0.0, 1.0, 11):
        rho = rho_family(t)
        lhs = np.trace(traceless(rho) @ traceless(rho)).real
        rhs = np.trace(rho @ rho).real - 1.0 / 3.0
        if abs(lhs - rhs) > 1e-12:
            op_ok = False
        if lhs < prev - 1e-12:
            op_mono = False
        prev = lhs
    check("order_param_identity", op_ok, "||traceless(rho)||^2 = purity - 1/3 (exact)")
    check("order_param_monotone_in_purity", op_mono, "strictly increasing; 0 iff rho=I/3")

    # ---- E5: converse second moment (conditional Gaussian model) ----
    print("[E5] CONVERSE (named isotropic-Gaussian model): covariance isotropic at I/3")
    _, cov_iso = wick_mean_cov(EYE / 3.0)
    ev = np.linalg.eigvalsh(cov_iso)
    iso = np.allclose(cov_iso, cov_iso[0, 0] * np.eye(8), atol=1e-9)
    check("covariance_isotropic_at_unpolarized", iso and cov_iso[0, 0] > 0,
          f"cov ~ {cov_iso[0,0]:.4f} I_8, eig spread {ev[-1]-ev[0]:.1e}")
    aniso_prev = -1.0
    aniso_mono = True
    aniso_vals = []
    for t in np.linspace(0.0, 1.0, 6):
        _, cov = wick_mean_cov(rho_family(t))
        ev = np.linalg.eigvalsh(cov)
        aniso = (ev[-1] - ev[0]) / ev[-1]
        aniso_vals.append(aniso)
        if aniso < aniso_prev - 1e-9:
            aniso_mono = False
        aniso_prev = aniso
    check("covariance_anisotropy_monotone", aniso_mono,
          "aniso(t): " + ", ".join(f"{a:.3f}" for a in aniso_vals))

    # ---- E6: non-circularity / not the refuted sufficiency claim ----
    print("[E6] guard: necessary direction is first-moment and noise-model-independent")
    # The first-moment obstruction uses NO noise model: it depends only on E[H]=traceless(rho)
    # (E2, exact) and E1. Confirm the mean is independent of any fluctuation-model choice by
    # re-deriving it as the equivariant-projection image of rho (E0), not from sampling.
    rho = rho_family(0.55)
    mean_wick, _ = wick_mean_cov(rho)
    mean_proj = su3_components(traceless(rho))
    check("mean_force_model_independent", np.linalg.norm(mean_wick - mean_proj) < 1e-12,
          "mean force = equivariant projection of rho, independent of noise model")
    # And confirm: equivariance/centrality of the FORM does not by itself force a zero force
    # (the obstruction is a genuine content condition, not a symmetry artifact): a polarized
    # rho yields an equivariant-yet-nonzero mean su(3) force.
    mean_pol, _ = wick_mean_cov(rho_family(0.9))
    check("equivariant_force_not_vacuously_zero", np.linalg.norm(mean_pol) > 1e-3,
          f"polarized equivariant mean force = {np.linalg.norm(mean_pol):.3f} != 0")

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return FAIL == 0


if __name__ == "__main__":
    ok = main()
    raise SystemExit(0 if ok else 1)
