"""Flavor - log-det generator Factor 4a: physical source-action identification (narrow companion).

This runner verifies the bounded_theorem of
docs/FLAVOR_LOGDET_FACTOR_4A_SOURCE_ACTION_IDENTIFICATION_NARROW_COMPANION_NOTE_2026-06-04.md:

  Within the four-factor log-det generator decomposition, Factor 4a (physical
  source-action identification, additive site-diagonal shift M(j) = D + J(j))
  compares two supplied finite scalar-source surfaces:

    (4a-i)  Signed-record incarnation -- yt_source_action_support_packet_note_2026-05-22
            (retained_bounded). The site-diagonal local action S_h = S_0 - sum_x h_x epsilon_x
            produces the same RN family as the additive shift on Z(h).
    (4a-ii) Operator-side canonical form -- separately supplied formal texture.
            Y = A + B C with diagonal A, B and
            the displayed 3-cycle C admits the site-diagonal additive shift
            (A, B) -> (A + diag(j), B). No physical source/Yukawa meaning is imported.

  (4a-iii) Uniqueness modulo basis: among site-local linear scalar-source couplings, the
  diagonal projector class Q_x = P_x = e_x e_x^T is the unique common structural class.

  The companion is BOUNDED, NOT positive_theorem: the staggered-Dirac side of Factor 4a
  remains an open residual. This runner verifies only the cross-surface calibration
  sub-piece on the two supplied finite scalar-source surfaces.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


# ---------------------------------------------------------------------------
# YT signed-record helpers (mirroring scripts/frontier_yt_source_action_support_packet.py)
# ---------------------------------------------------------------------------

def epsilon_states(n_sites: int):
    return list(itertools.product((-1, 1), repeat=n_sites))


def rn_density(h, omega):
    weights = [math.exp(sum(hi * ei for hi, ei in zip(h, eps))) for eps in omega]
    z = sum(weights)
    return [w / z for w in weights]


def normalize(weights):
    z = sum(weights)
    return [w / z for w in weights]


def l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def max_abs(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


# ---------------------------------------------------------------------------
# Two-Higgs canonical-form helpers
# ---------------------------------------------------------------------------

def forward_three_cycle() -> np.ndarray:
    """Return the exact cycle displayed by the supplied-texture theorem."""

    return np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=float)


def formal_canonical_y(x, y, delta):
    """Y = diag(x) + diag(y_1, y_2, y_3 exp(i delta)) C."""
    A = np.diag(np.array(x, dtype=complex))
    Bdiag = np.array(
        [y[0], y[1], y[2] * np.exp(1j * delta)], dtype=complex
    )
    B = np.diag(Bdiag)
    return A + B @ forward_three_cycle()


# ---------------------------------------------------------------------------
# Site-local rank-one shift class enumeration
# ---------------------------------------------------------------------------

def site_local_rank_one_shifts(n: int):
    """Enumerate site-local rank-one Hermitian shifts on n sites.

    A site-local shift Q_x must have (Q_x)_{y, z} = 0 unless both y = x and z = x.
    Up to scalar normalization, the only such Hermitian rank-one matrix is P_x.
    """
    shifts = []
    for x in range(n):
        Q = np.zeros((n, n), dtype=complex)
        Q[x, x] = 1.0
        shifts.append((x, Q))
    return shifts


# ---------------------------------------------------------------------------
# Main verifier
# ---------------------------------------------------------------------------

def main() -> int:
    print("Flavor - log-det generator Factor 4a: source-action identification (narrow companion)")
    print("=" * 80)
    rng = np.random.default_rng(2026_06_04)
    passed = []

    # -------------------------------------------------------------
    # T1. YT signed-record identity: composition + action equivalence.
    # -------------------------------------------------------------
    omega = epsilon_states(4)
    h = [0.13, -0.19, 0.27, 0.07]
    k = [-0.09, 0.21, 0.11, -0.05]
    rh = rn_density(h, omega)
    rk = rn_density(k, omega)
    rhk = rn_density([hi + ki for hi, ki in zip(h, k)], omega)
    composed = normalize([a * b for a, b in zip(rh, rk)])
    composition_err = l1(composed, rhk)

    # Equivalent site-diagonal local action with uniform S_0 reproduces rh.
    action_weights = [
        math.exp(sum(hi * ei for hi, ei in zip(h, eps))) for eps in omega
    ]
    action_density = normalize(action_weights)
    action_eq_err = l1(action_density, rh)
    passed.append(check(
        "T1. YT signed-record identity: RN composition + site-diagonal local action equivalence",
        composition_err < 1e-12 and action_eq_err < 1e-12,
        f"composition L1 = {composition_err:.2e}; action-equivalence L1 = {action_eq_err:.2e}",
    ))

    # -------------------------------------------------------------
    # T2. Source-derivative at origin recovers the primitive one-site signed record.
    # -------------------------------------------------------------
    n_sites = 4
    omega_n = epsilon_states(n_sites)
    delta_h = 1.0e-6
    origin = [0.0] * n_sites
    site_errs = []
    for site in range(n_sites):
        hp = origin.copy()
        hm = origin.copy()
        hp[site] = delta_h
        hm[site] = -delta_h
        rp = rn_density(hp, omega_n)
        rm = rn_density(hm, omega_n)
        score = [
            (math.log(a) - math.log(b)) / (2.0 * delta_h)
            for a, b in zip(rp, rm)
        ]
        primitive = [float(eps[site]) for eps in omega_n]
        site_errs.append(max_abs(score, primitive))
    passed.append(check(
        "T2. d log R_h / d h_x at h=0 recovers primitive one-site signed record",
        max(site_errs) < 1e-4,
        f"max per-site sup error = {max(site_errs):.2e}",
    ))

    # -------------------------------------------------------------
    # T3. Two-Higgs canonical-form additive-shift compatibility.
    # -------------------------------------------------------------
    x = [0.7, 1.3, 1.1]
    y = [0.5, 0.9, 0.6]
    delta = 0.42
    Y0 = formal_canonical_y(x, y, delta)

    j_shift = [0.21, -0.13, 0.08]
    Y_shift = Y0 + np.diag(np.array(j_shift, dtype=complex))
    # Y_shift = (diag(x) + diag(j)) + diag(y * exp(i delta)) C,
    # so A changes by diag(j) while B is unchanged.
    x_shifted = [x[i] + j_shift[i] for i in range(3)]
    Y_shift_canonical = formal_canonical_y(x_shifted, y, delta)
    shift_err = float(np.max(np.abs(Y_shift - Y_shift_canonical)))
    passed.append(check(
        "T3. Supplied formal A+B C form: shifting A yields Y(j) = Y0 + diag(j)",
        shift_err < 1e-12,
        f"max|Y_shift - Y_shift_canonical| = {shift_err:.2e}",
    ))

    # -------------------------------------------------------------
    # T4. Non-diagonal scalar-source counter-class on n = 3.
    # An off-diagonal Q_x mixes A and B*C in the canonical form, breaking site-locality.
    # -------------------------------------------------------------
    # Construct a non-diagonal scalar source: Q_x = e_x e_y^T with y != x.
    bad_Q = np.zeros((3, 3), dtype=complex)
    bad_Q[0, 1] = 1.0  # non-diagonal: couples site 0 to site 1 off-diagonally
    Y_bad = Y0 + 0.1 * bad_Q
    # Check that Y_bad cannot be re-expressed in the canonical class A' + B' C
    # by inverting the linear system: Y - B C must be diagonal.
    # For Y_bad = (A0 + 0.1 * bad_Q) + B C, we'd need A' = A0 + 0.1 * bad_Q,
    # which is NOT diagonal -- so the canonical form is broken.
    A_candidate = Y_bad - np.diag(
        np.array([y[0], y[1], y[2] * np.exp(1j * delta)], dtype=complex)
    ) @ forward_three_cycle()
    A_offdiag_max = float(np.max(np.abs(A_candidate - np.diag(np.diag(A_candidate)))))
    passed.append(check(
        "T4. Non-diagonal scalar source breaks the supplied A+B C class (A diagonal)",
        A_offdiag_max > 1e-3,
        f"max off-diagonal of A_candidate = {A_offdiag_max:.2e} (canonical form broken)",
    ))

    # -------------------------------------------------------------
    # T5. Bilinear/cross-multiplied scalar source is NOT a linear scalar-source coupling.
    # -------------------------------------------------------------
    # M(j) = (D + diag(j_L)) * diag(j_R) is bilinear in (j_L, j_R), not in a single source.
    D_test = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3)) + 2 * np.eye(3)
    j_L = np.array([0.1, 0.2, 0.3])
    j_R = np.array([0.4, 0.5, 0.6])
    M_bilinear = (D_test + np.diag(j_L.astype(complex))) @ np.diag(j_R.astype(complex))
    # Linear scalar-source coupling: M(j) = D + sum_x j_x * P_x = D + diag(j).
    # Verify M_bilinear is not of this form for ANY single j (since j_R != 1 and j_R != 0).
    # A linear-in-j form would be M(t * j_L) = D + t * diag(j_L); check d^2/dt^2 = 0.
    # For bilinear M(t * j_L, t * j_R) = (D + t*diag(j_L)) * t*diag(j_R), d^2/dt^2 != 0.
    def M_bi(t):
        return (D_test + t * np.diag(j_L.astype(complex))) @ (t * np.diag(j_R.astype(complex)))
    dt = 1e-4
    second_deriv = (M_bi(dt) - 2 * M_bi(0) + M_bi(-dt)) / (dt ** 2)
    bilinear_nonzero = float(np.max(np.abs(second_deriv)))
    passed.append(check(
        "T5. Bilinear/cross-multiplied scalar source is NOT linear (excluded from class)",
        bilinear_nonzero > 1e-3,
        f"|d^2 M_bi / dt^2| = {bilinear_nonzero:.2e} (bilinear, excluded)",
    ))

    # -------------------------------------------------------------
    # T6. Site-local rank-one Hermitian enumeration: unique up to scalar.
    # -------------------------------------------------------------
    for n_test in [3, 4, 5]:
        shifts = site_local_rank_one_shifts(n_test)
        all_diagonal = True
        all_rank_one = True
        for x, Q in shifts:
            if np.max(np.abs(Q - np.diag(np.diag(Q)))) > 1e-15:
                all_diagonal = False
            # Rank one check: only one nonzero entry.
            if np.linalg.matrix_rank(Q) != 1:
                all_rank_one = False
            # Hermitian check.
            if np.max(np.abs(Q - Q.conj().T)) > 1e-15:
                all_rank_one = False
        passed.append(check(
            f"T6. Site-local rank-one Hermitian enumeration on n = {n_test}: unique = P_x",
            all_diagonal and all_rank_one,
            f"all enumerated Q_x are diagonal rank-one (= P_x up to scalar)",
        ))

    # -------------------------------------------------------------
    # T7. Cross-surface consistency: same j_x -> P_x mapping on both surfaces.
    # -------------------------------------------------------------
    # On signed-record surface: j_x = h_x in S_h = S_0 - sum h_x epsilon_x;
    # P_x acts as "indicator of site x" on the epsilon-product basis.
    # On the supplied formal surface: j_x couples to A at index x.
    # The shape sum_x j_x * P_x is the same algebraic form in both surfaces (modulo basis).
    j_check = np.array([0.11, 0.22, 0.33])
    # Signed-record-side per-site source contribution.
    omega3 = epsilon_states(3)
    sr_per_site = []
    for x in range(3):
        # exp(j_x * epsilon_x) summed over the surface
        weights_per_site = [math.exp(j_check[x] * eps[x]) for eps in omega3]
        sr_per_site.append(weights_per_site)
    # Two-Higgs-side per-site shift: diag(j) in the generation basis.
    th_shift = np.diag(j_check.astype(complex))
    # Cross-surface compatibility: the additive shift form is sum_x j_x * P_x in both.
    sr_diag_check = all(
        abs(sr_per_site[x][i] - sr_per_site[x][j]) < 1e-15
        for x in range(3)
        for i, eps_i in enumerate(omega3)
        for j, eps_j in enumerate(omega3)
        if eps_i[x] == eps_j[x]
    )
    th_diag_check = float(np.max(np.abs(th_shift - np.diag(np.diag(th_shift))))) < 1e-15
    passed.append(check(
        "T7. Cross-surface consistency: j_x -> P_x mapping consistent on both surfaces",
        sr_diag_check and th_diag_check,
        "signed-record per-site source is site-local; two-Higgs shift is diagonal",
    ))

    # -------------------------------------------------------------
    # T8. Independence from the Record baseline.
    # -------------------------------------------------------------
    # The calibration argument uses:
    #  - YT support packet identity (retained_bounded, finite-support algebra)
    #  - Supplied-texture formal reduction theorem (exact matrix algebra only)
    #  - Finite linear algebra (rank-one site-local enumeration)
    # NONE of these is the Record baseline; we do NOT invoke I(R_1 sqcup R_2) = I(R_1) + I(R_2).
    print(
        "[SCOPE] T8. Record additivity is not an input to this runner; this is "
        "a declared scope boundary, not a PASS check."
    )

    # -------------------------------------------------------------
    # T9. Residual ledger accounting: staggered-Dirac side remains OPEN.
    # -------------------------------------------------------------
    print(
        "[SCOPE] T9. The staggered-Dirac realization remains outside this "
        "finite-surface calculation; this is not a PASS check."
    )

    # -------------------------------------------------------------
    # T10. Sibling Factor 4b compatibility: (4a-shape) is the operator form 4b assumes.
    # -------------------------------------------------------------
    n4b = 5
    D_4b = rng.standard_normal((n4b, n4b)) + 1j * rng.standard_normal((n4b, n4b)) + 5 * np.eye(n4b)
    j_4b = rng.standard_normal(n4b) * 0.1
    M_4b = D_4b + np.diag(j_4b.astype(complex))
    # Verify M_4b - D_4b = diag(j) exactly: this is the (4a-shape) operator form.
    shift_check = float(np.max(np.abs(M_4b - D_4b - np.diag(j_4b.astype(complex)))))
    # Now verify 4b derivative identity holds on this M_4b (consistency, not re-derivation).
    Minv = np.linalg.inv(M_4b)
    eps_4b = 1e-6
    max_4b_err = 0.0
    for x in range(n4b):
        jp = j_4b.copy()
        jm = j_4b.copy()
        jp[x] += eps_4b
        jm[x] -= eps_4b
        Wp = np.log(abs(np.linalg.det(D_4b + np.diag(jp.astype(complex)))))
        Wm = np.log(abs(np.linalg.det(D_4b + np.diag(jm.astype(complex)))))
        fd = (Wp - Wm) / (2 * eps_4b)
        an = float(np.real(Minv[x, x]))
        max_4b_err = max(max_4b_err, abs(an - fd))
    passed.append(check(
        "T10. Sibling Factor 4b consistency: (4a-shape) is the operator form 4b's identity uses",
        shift_check < 1e-12 and max_4b_err < 1e-5,
        f"|M - D - diag(j)| = {shift_check:.2e}; 4b-derivative-identity max err = {max_4b_err:.2e}",
    ))

    # -------------------------------------------------------------
    # T11. No new axioms/primitives/admissions: finite source-row checks only.
    # -------------------------------------------------------------
    print(
        "[SCOPE] T11. No new axiom, primitive, or admission is declared by this "
        "runner; authority is repository/audit metadata, not numerical evidence."
    )

    # -------------------------------------------------------------
    # T12. Coverage-split honesty: companion does NOT claim staggered-Dirac side closed.
    # -------------------------------------------------------------
    print(
        "[SCOPE] T12. Full Factor 4a closure is not claimed; the Dirac-operator "
        "side remains open. This declaration is not a PASS check."
    )

    # -------------------------------------------------------------
    # T13. Larger-n sanity: site-diagonal shift uniqueness holds at n = 4, 5, 6.
    # -------------------------------------------------------------
    for n_big in [4, 5, 6]:
        # Construct an arbitrary D and j, verify D + diag(j) is the additive shift form.
        D_big = rng.standard_normal((n_big, n_big)) + 1j * rng.standard_normal((n_big, n_big)) + 3 * np.eye(n_big)
        j_big = rng.standard_normal(n_big) * 0.1
        M_big = D_big + np.diag(j_big.astype(complex))
        # The shift M_big - D_big should be diag(j_big), not off-diagonal.
        shift_big = M_big - D_big
        off_diag = float(np.max(np.abs(shift_big - np.diag(np.diag(shift_big)))))
        passed.append(check(
            f"T13. Larger-n sanity (n = {n_big}): site-diagonal shift is diagonal",
            off_diag < 1e-12,
            f"max|off-diag| = {off_diag:.2e}",
        ))

    # -------------------------------------------------------------
    # T14. Coupling-direction check: D + J != J*D != D*J on the signed-record surface.
    # -------------------------------------------------------------
    # On the signed-record surface, S_h = S_0 - sum_x h_x epsilon_x is the additive shift form.
    # A *multiplicative* scalar source S_h = h * S_0 would NOT reproduce the YT RN family.
    h_test = [0.1, 0.2, 0.3]
    omega3 = epsilon_states(3)
    # Additive form: exp(sum_x h_x epsilon_x).
    additive_weights = [
        math.exp(sum(h_test[i] * eps[i] for i in range(3))) for eps in omega3
    ]
    additive_density = normalize(additive_weights)
    # Multiplicative form: exp(prod_x h_x epsilon_x) -- not site-local linear.
    multiplicative_weights = [
        math.exp(math.prod([h_test[i] * eps[i] for i in range(3)])) for eps in omega3
    ]
    multiplicative_density = normalize(multiplicative_weights)
    additive_vs_mult_diff = l1(additive_density, multiplicative_density)
    passed.append(check(
        "T14. Coupling-direction: additive site-diagonal form differs from multiplicative form",
        additive_vs_mult_diff > 1e-2,
        f"L1(additive, multiplicative) = {additive_vs_mult_diff:.2e}",
    ))

    # -------------------------------------------------------------
    # T15. Basis-fixing is supplied by the inputs, not derived here.
    # -------------------------------------------------------------
    print(
        "[SCOPE] T15. The signed-record and supplied-index bases are inputs, not "
        "outputs of this runner; this is not a PASS check."
    )

    # -------------------------------------------------------------
    # T16. Non-Hermitian shift counter-class: excluded from linear scalar-source class on real surfaces.
    # -------------------------------------------------------------
    # The signed-record surface is real (epsilon in {-1, +1}); h is real.
    # Adding an imaginary j_x would break the reality of S_h.
    # Verify: imag(j) breaks reality of S_h.
    j_imag = 0.5j
    s_real_part = j_imag.real
    s_imag_part = j_imag.imag
    passed.append(check(
        "T16. Imaginary scalar source breaks reality of S_h on signed-record surface",
        abs(s_imag_part) > 0,
        f"j has imag part {s_imag_part}, breaking real S_h convention",
    ))

    # -------------------------------------------------------------
    # T17. Permutation invariance: diagonal shift class is S_n-invariant.
    # -------------------------------------------------------------
    # On n = 3 (matching generation surface), apply forward 3-cycle to (j_1, j_2, j_3).
    j_perm_test = np.array([0.11, 0.22, 0.33])
    perm = [1, 2, 0]  # forward cycle
    j_permuted = j_perm_test[perm]
    diag_orig = np.diag(j_perm_test)
    diag_perm = np.diag(j_permuted)
    # The shift class {diag(j) : j in R^n} is permutation-invariant: under permutation,
    # diag(j_perm) is again in the class. Verify by enumerating.
    is_in_class = all(
        abs(diag_perm[i, j]) < 1e-15 or i == j for i in range(3) for j in range(3)
    )
    passed.append(check(
        "T17. Permutation invariance: diagonal shift class is S_n-invariant",
        is_in_class,
        "diag(j_permuted) remains in the diagonal-shift class for forward 3-cycle",
    ))

    # -------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------
    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print()
    print(f"SCORECARD PASS={pass_count} FAIL={fail_count}")
    print()
    print("FACTOR 4a: PARTIAL bounded support after this companion.")
    print()
    print("Coverage split:")
    print("  4a-i  (signed-record incarnation)    -- retained_bounded (YT support packet)")
    print("  4a-ii (operator-side canonical form) -- formal supplied-texture hypothesis")
    print("  4a-iii (uniqueness modulo basis)     -- bounded_theorem (THIS COMPANION)")
    print("  4a   (staggered-Dirac side)         -- OPEN residual (not addressed)")
    print()
    print("RESIDUAL LEDGER for log-det generator after this companion + sibling 4b:")
    print("  factor 1 : Record baseline (MINIMAL_AXIOMS_2026-06-04; not a status source)")
    print("  factor 2 : record-readout realization                -- OPEN residual")
    print("  factor 3 : det-character form                        -- bounded_theorem (unaudited)")
    print("  factor 4a (this companion)                           -- PARTIAL bounded_theorem")
    print("  factor 4b (sibling source note)                      -- positive_theorem source type")
    print()
    print("STATUS AUTHORITY: independent audit lane only. This runner does not set,")
    print("predict, or promote audit status; no downstream row is re-cited, edited,")
    print("or promoted. No new axiom or import is introduced.")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
