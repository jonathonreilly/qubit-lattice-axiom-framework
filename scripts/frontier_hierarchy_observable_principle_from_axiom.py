#!/usr/bin/env python3
"""
Hierarchy observable principle from the lattice axiom.

Goal:
  Check the exact finite log|det| source-response theorem on the runner block:

      W[J] = log |det(D + J)| - log |det D|

  The 2026-05-29 scope repair removes P2 scalar-generator selection from the
  load-bearing claim. This runner verifies only the exact algebra after W is
  explicitly supplied; it does not prove that physical scalar observables must
  select W from all possible generator choices.

  On the minimal hierarchy block this W reproduces the exact dimension-4
  source-curvature coefficient A(L_t), and the resulting temporal kernel is
  exactly the sign/conjugation-closed orbit kernel that selects L_t=4.
"""

from __future__ import annotations

import cmath
import math
import sys
from pathlib import Path

import numpy as np
from canonical_plaquette_surface import CANONICAL_ALPHA_LM, CANONICAL_PLAQUETTE, CANONICAL_U0

np.set_printoptions(precision=10, linewidth=120, suppress=True)

PASS_COUNT = 0
FAIL_COUNT = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"


def check(name: str, condition: bool, detail: str = ""):
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def build_dirac_4d_apbc(ls: int, lt: int, u0: float, mass: float = 0.0) -> np.ndarray:
    n = ls**3 * lt
    d = np.zeros((n, n), dtype=complex)

    def idx(x0: int, x1: int, x2: int, t: int) -> int:
        return (((x0 % ls) * ls + (x1 % ls)) * ls + (x2 % ls)) * lt + (t % lt)

    for x0 in range(ls):
        for x1 in range(ls):
            for x2 in range(ls):
                for t in range(lt):
                    i = idx(x0, x1, x2, t)
                    d[i, i] += mass

                    eta = 1.0
                    xf = (x0 + 1) % ls
                    sign = -1.0 if x0 + 1 >= ls else 1.0
                    d[i, idx(xf, x1, x2, t)] += u0 * eta * sign / 2.0
                    xb = (x0 - 1) % ls
                    sign = -1.0 if x0 - 1 < 0 else 1.0
                    d[i, idx(xb, x1, x2, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** x0
                    xf = (x1 + 1) % ls
                    sign = -1.0 if x1 + 1 >= ls else 1.0
                    d[i, idx(x0, xf, x2, t)] += u0 * eta * sign / 2.0
                    xb = (x1 - 1) % ls
                    sign = -1.0 if x1 - 1 < 0 else 1.0
                    d[i, idx(x0, xb, x2, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** (x0 + x1)
                    xf = (x2 + 1) % ls
                    sign = -1.0 if x2 + 1 >= ls else 1.0
                    d[i, idx(x0, x1, xf, t)] += u0 * eta * sign / 2.0
                    xb = (x2 - 1) % ls
                    sign = -1.0 if x2 - 1 < 0 else 1.0
                    d[i, idx(x0, x1, xb, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** (x0 + x1 + x2)
                    tf = (t + 1) % lt
                    sign = -1.0 if t + 1 >= lt else 1.0
                    d[i, idx(x0, x1, x2, tf)] += u0 * eta * sign / 2.0
                    tb = (t - 1) % lt
                    sign = -1.0 if t - 1 < 0 else 1.0
                    d[i, idx(x0, x1, x2, tb)] -= u0 * eta * sign / 2.0
    return d


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    dim = sum(block.shape[0] for block in blocks)
    out = np.zeros((dim, dim), dtype=complex)
    start = 0
    for block in blocks:
        n = block.shape[0]
        out[start : start + n, start : start + n] = block
        start += n
    return out


def projector(n: int, idx: int) -> np.ndarray:
    p = np.zeros((n, n), dtype=complex)
    p[idx, idx] = 1.0
    return p


def logabs_det(m: np.ndarray) -> float:
    return float(np.linalg.slogdet(m)[1])


def observable_generator(d: np.ndarray, source: np.ndarray) -> float:
    """Additive CPT-even scalar generator: log|det(D+J)| - log|det D|."""
    return logabs_det(d + source) - logabs_det(d)


def temporal_modes(lt: int):
    return [(2 * n + 1) * math.pi / lt for n in range(lt)]


def exact_uniform_generator(lt: int, u0: float, j: float) -> float:
    return 4.0 * sum(
        math.log1p(j**2 / (u0**2 * (3.0 + math.sin(w) ** 2))) for w in temporal_modes(lt)
    )


def exact_uniform_coefficient_total(lt: int, u0: float) -> float:
    return 4.0 * sum(1.0 / (u0**2 * (3.0 + math.sin(w) ** 2)) for w in temporal_modes(lt))


def exact_local_a(lt: int, u0: float) -> float:
    return (1.0 / (2.0 * lt * u0**2)) * sum(
        1.0 / (3.0 + math.sin(w) ** 2) for w in temporal_modes(lt)
    )


def canon(z: complex):
    return (round(z.real, 12), round(z.imag, 12))


def apbc_phases(lt: int):
    return [cmath.exp(1j * (2 * n + 1) * math.pi / lt) for n in range(lt)]


def orbit_partition(lt: int):
    ops = [lambda w: w, lambda w: -w, lambda w: w.conjugate(), lambda w: -w.conjugate()]
    phases = sorted({canon(z) for z in apbc_phases(lt)})
    seen = set()
    parts = []
    for z in phases:
        if z in seen:
            continue
        orb = sorted({canon(op(complex(*z))) for op in ops if canon(op(complex(*z))) in phases})
        parts.append(orb)
        seen.update(orb)
    return parts


def orbit_weights(lt: int):
    parts = orbit_partition(lt)
    out = []
    for orb in parts:
        vals = []
        for x, y in orb:
            angle = math.atan2(y, x)
            vals.append(round(1.0 / (3.0 + math.sin(angle) ** 2), 15))
        out.append(sorted(set(vals)))
    return out


def test_source_note_scope_firewall():
    print("\n" + "=" * 78)
    print("PART 0: SOURCE NOTE SCOPE FIREWALL")
    print("=" * 78)

    note = NOTE_PATH.read_text(encoding="utf-8")
    required = [
        "narrowed from a P1+P2 scalar-generator selection claim",
        "P2 is removed from the load-bearing theorem surface",
        "This row no longer claims that the framework uniquely selects `W`",
        "This row does not claim scalar-generator selection from A1/A2",
        "This row does not claim P2",
        "No new axiom is introduced",
        "Comparator-Only Readout",
    ]
    forbidden = [
        "P1 and P2 stay admitted; the Tier-A portfolio is not extended.",
        "Given P1 (scalar additivity on independent subsystems) and P2",
        "conditional on the P1+P2 admitted scalar-selection surface",
    ]

    for phrase in required:
        check(f"source note carries repaired-scope phrase: {phrase}", phrase in note)
    for phrase in forbidden:
        check(f"source note excludes old conditional-scope phrase: {phrase}", phrase not in note)


def test_additive_scalar_generator():
    print("\n" + "=" * 78)
    print("PART 1: ADDITIVITY FORCES THE LOG-ABSDET GENERATOR")
    print("=" * 78)

    u0 = 0.9
    d2 = build_dirac_4d_apbc(2, 2, u0)
    d4 = build_dirac_4d_apbc(2, 4, u0)
    d_tot = block_diag(d2, d4)

    max_log_err = 0.0
    max_mult_err = 0.0
    raw_additivity_violation = 0.0

    for j in [1e-3, 1e-2, 5e-2, 1e-1]:
        s2 = j * np.eye(d2.shape[0], dtype=complex)
        s4 = j * np.eye(d4.shape[0], dtype=complex)
        s_tot = j * np.eye(d_tot.shape[0], dtype=complex)

        z2 = abs(np.linalg.det(d2 + s2))
        z4 = abs(np.linalg.det(d4 + s4))
        z_tot = abs(np.linalg.det(d_tot + s_tot))

        mult_err = abs(z_tot - z2 * z4) / (z2 * z4)
        log_err = abs(observable_generator(d_tot, s_tot) - (observable_generator(d2, s2) + observable_generator(d4, s4)))
        raw_gap = abs(z_tot - (z2 + z4)) / z_tot

        max_mult_err = max(max_mult_err, mult_err)
        max_log_err = max(max_log_err, log_err)
        raw_additivity_violation = max(raw_additivity_violation, raw_gap)
        print(
            f"  j={j:g}: |Z_tot|-mult rel={mult_err:.2e}, "
            f"log-add abs={log_err:.2e}, raw-add rel={raw_gap:.6f}"
        )

    check(
        "|Z| is exactly multiplicative on independent subsystems",
        max_mult_err < 1e-12,
        f"max relative multiplicativity error = {max_mult_err:.2e}",
    )
    check(
        "log|Z| is exactly additive on independent subsystems",
        max_log_err < 1e-12,
        f"max additive error = {max_log_err:.2e}",
    )
    check(
        "raw |Z| itself is not an additive scalar observable",
        raw_additivity_violation > 0.1,
        f"max raw additivity violation = {raw_additivity_violation:.6f}",
    )


def test_local_source_response_and_block_locality():
    print("\n" + "=" * 78)
    print("PART 2: LOCAL SOURCE RESPONSES ARE CONNECTED AND BLOCK-LOCAL")
    print("=" * 78)

    u0 = 0.9
    d2 = build_dirac_4d_apbc(2, 2, u0)
    d4 = build_dirac_4d_apbc(2, 4, u0)
    d_tot = block_diag(d2, d4)
    inv_tot = np.linalg.inv(d_tot)

    n1 = d2.shape[0]
    n2 = d4.shape[0]
    n_tot = d_tot.shape[0]
    p1 = np.zeros((n_tot, n_tot), dtype=complex)
    p1[:n1, :n1] = np.eye(n1, dtype=complex)
    p2 = np.zeros((n_tot, n_tot), dtype=complex)
    p2[n1:, n1:] = np.eye(n2, dtype=complex)

    mixed = -np.trace(inv_tot @ p1 @ inv_tot @ p2).real
    self_tot = -np.trace(inv_tot @ p1 @ inv_tot @ p1).real
    inv1 = np.linalg.inv(d2)
    self_1 = -np.trace(inv1 @ np.eye(n1, dtype=complex) @ inv1 @ np.eye(n1, dtype=complex)).real

    print(f"  mixed block curvature K_12 = {mixed:.3e}")
    print(f"  first-block local curvature from total = {self_tot:.12e}")
    print(f"  first-block local curvature standalone = {self_1:.12e}")

    check(
        "mixed local-source curvature vanishes across independent blocks",
        abs(mixed) < 1e-12,
        f"|K_12| = {abs(mixed):.2e}",
    )
    check(
        "local self-curvature is inherited exactly by the full block-diagonal system",
        abs(self_tot - self_1) < 1e-12,
        f"absolute difference = {abs(self_tot - self_1):.2e}",
    )


def test_uniform_scalar_generator_from_axiom():
    print("\n" + "=" * 78)
    print("PART 3: UNIFORM SCALAR SOURCE GIVES THE EXACT HIERARCHY GENERATOR")
    print("=" * 78)

    u0 = 0.9
    max_gen_err = 0.0
    max_even_err = 0.0
    max_pos_err = 0.0
    max_quad_err = 0.0

    for lt in [2, 4, 6, 8]:
        d = build_dirac_4d_apbc(2, lt, u0)
        n = d.shape[0]
        dd = d.conj().T @ d
        dd_inv = np.linalg.inv(dd)
        for j in [1e-4, 1e-3, 1e-2, 1e-1]:
            src = j * np.eye(n, dtype=complex)
            gen = observable_generator(d, src)
            gen_neg = observable_generator(d, -src)
            exact = exact_uniform_generator(lt, u0, j)
            pos = 0.5 * logabs_det(np.eye(n, dtype=complex) + (j**2) * dd_inv)
            if j <= 1e-3:
                quad = gen / (j**2)
                quad_exact = exact_uniform_coefficient_total(lt, u0)
                quad_err = abs(quad - quad_exact)
                max_quad_err = max(max_quad_err, quad_err)
            else:
                quad_err = float("nan")

            gen_err = abs(gen - exact)
            even_err = abs(gen - gen_neg)
            pos_err = abs(gen - pos)
            max_gen_err = max(max_gen_err, gen_err)
            max_even_err = max(max_even_err, even_err)
            max_pos_err = max(max_pos_err, pos_err)

            print(
                f"  Lt={lt}, j={j:g}: gen={gen:.12e}, exact={exact:.12e}, "
                f"pos_err={pos_err:.2e}, quad_err={quad_err:.2e}"
            )

    check(
        "uniform-source log|det| generator matches the exact Matsubara formula",
        max_gen_err < 1e-11,
        f"max absolute generator error = {max_gen_err:.2e}",
    )
    check(
        "the scalar generator is exactly bosonic/sign-blind: W(j) = W(-j)",
        max_even_err < 1e-12,
        f"max evenness error = {max_even_err:.2e}",
    )
    check(
        "the scalar generator is exactly the positive CPT-even log-det functional",
        max_pos_err < 1e-12,
        f"max positive-functional error = {max_pos_err:.2e}",
    )
    check(
        "the small-j curvature reproduces the exact total A(L_t) coefficient",
        max_quad_err < 5e-6,
        f"max quadratic-coefficient error = {max_quad_err:.2e}",
    )


def test_orbit_kernel_and_selector():
    print("\n" + "=" * 78)
    print("PART 4: THE SOURCE-CURVATURE KERNEL FORCES THE LT=4 SELECTOR")
    print("=" * 78)

    resolved = []
    for lt in range(2, 14, 2):
        parts = orbit_partition(lt)
        weights = orbit_weights(lt)
        sizes = [len(p) for p in parts]
        print(f"  Lt={lt:2d}: num_orbits={len(parts)}, sizes={sizes}, weights={weights}")
        if len(parts) == 1 and len(parts[0]) > 2:
            resolved.append(lt)

    check(
        "the curvature kernel depends only on sign/conjugation-invariant sin^2(omega)",
        orbit_weights(4) == [[0.285714285714286]],
        f"Lt=4 orbit weights = {orbit_weights(4)}",
    )
    check(
        "the unique minimal resolved Klein-four orbit is Lt = 4",
        resolved == [4],
        f"resolved single-orbit Lt values = {resolved}",
    )


def test_hierarchy_value_from_internal_observable_principle():
    print("\n" + "=" * 78)
    print("PART 5: OUT-OF-SCOPE HIERARCHY COMPARATOR (INFORMATIONAL ONLY)")
    print("=" * 78)

    c4 = (7.0 / 8.0) ** 0.25
    plaquette = CANONICAL_PLAQUETTE
    m_planck = 1.2209e19
    u0 = CANONICAL_U0
    alpha_bare = 1.0 / (4.0 * math.pi)
    alpha_lm = CANONICAL_ALPHA_LM
    baseline = m_planck * alpha_lm**16
    v_pred = baseline * c4
    v_meas = 246.22
    rel = (v_pred - v_meas) / v_meas

    print(f"  C_4 = {c4:.12f}")
    print(f"  baseline = M_Pl * alpha_LM^16 = {baseline:.12f} GeV")
    print(f"  v_pred = {v_pred:.12f} GeV")
    print(f"  v_meas = {v_meas:.12f} GeV")
    print(f"  relative error = {rel:.6%}")
    print("  INFO: comparator only; not counted as a theorem PASS check.")


def test_repaired_logdet_scope_shape():
    """Part 6 -- repaired exact log|det| scope verification.

    Per the 2026-05-29 scope repair recorded in
    `docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, the load-bearing claim is
    no longer conditional on P2 scalar-generator selection. The repaired claim
    explicitly supplies

      W[J] = log|det(D+J)| - log|det D|

    and proves the exact algebraic consequences of that supplied functional.

    This test verifies, as an empirical statement on the runner's finite
    lattice Dirac operator, that:

      - W is additive on direct sums, source-even, regular near zero source,
        and implements the baseline convention W(0) = 0;

      - raw |Z| is not additive, showing why this row must not be cited as a
        selection theorem for arbitrary scalar generators.

    This part does not attempt to derive P2 from retained primitives. It is a
    scope firewall for the repaired exact log|det| theorem.
    """
    print("\n" + "=" * 78)
    print("PART 6: REPAIRED EXACT LOG|DET| SCOPE VERIFICATION")
    print("=" * 78)

    u0 = 0.9
    d2 = build_dirac_4d_apbc(2, 2, u0)
    d4 = build_dirac_4d_apbc(2, 4, u0)
    d_tot = block_diag(d2, d4)
    n2 = d2.shape[0]
    n4 = d4.shape[0]
    n_tot = d_tot.shape[0]

    p1_max_err = 0.0
    for j in [1e-3, 1e-2, 5e-2]:
        s2 = j * np.eye(n2, dtype=complex)
        s4 = j * np.eye(n4, dtype=complex)
        s_tot = j * np.eye(n_tot, dtype=complex)
        w_tot = observable_generator(d_tot, s_tot)
        w_split = observable_generator(d2, s2) + observable_generator(d4, s4)
        p1_max_err = max(p1_max_err, abs(w_tot - w_split))

    p2_max_err = 0.0
    for lt in [2, 4]:
        d = build_dirac_4d_apbc(2, lt, u0)
        n = d.shape[0]
        for j in [1e-3, 1e-2, 5e-2]:
            src_pos = j * np.eye(n, dtype=complex)
            src_neg = -j * np.eye(n, dtype=complex)
            p2_max_err = max(
                p2_max_err,
                abs(observable_generator(d, src_pos) - observable_generator(d, src_neg)),
            )

    p3_max_err = 0.0
    p4_baseline_err = 0.0
    for lt in [2, 4]:
        d = build_dirac_4d_apbc(2, lt, u0)
        n = d.shape[0]
        zero_src = np.zeros((n, n), dtype=complex)
        p4_baseline_err = max(p4_baseline_err, abs(observable_generator(d, zero_src)))
        for j in [1e-5, 1e-4, 1e-3]:
            src = j * np.eye(n, dtype=complex)
            w = observable_generator(d, src)
            quad = exact_uniform_coefficient_total(lt, u0) * j**2
            p3_max_err = max(p3_max_err, abs(w - quad) / max(abs(quad), 1e-30))

    raw_violation = 0.0
    for j in [1e-2]:
        s2 = j * np.eye(n2, dtype=complex)
        s4 = j * np.eye(n4, dtype=complex)
        s_tot = j * np.eye(n_tot, dtype=complex)
        z2 = abs(np.linalg.det(d2 + s2))
        z4 = abs(np.linalg.det(d4 + s4))
        z_tot = abs(np.linalg.det(d_tot + s_tot))
        raw_violation = max(raw_violation, abs(z_tot - (z2 + z4)) / z_tot)

    check(
        "direct-sum additivity holds for supplied W = log|det(D+J)|",
        p1_max_err < 1e-12,
        f"max additivity error = {p1_max_err:.2e}",
    )
    check(
        "supplied W is source-even on the runner block, W(j) = W(-j)",
        p2_max_err < 1e-12,
        f"max evenness error = {p2_max_err:.2e}",
    )
    check(
        "candidate regularity: small-j behavior is stable for W",
        p3_max_err < 5e-3,
        f"max relative quadratic-coefficient consistency = {p3_max_err:.2e}",
    )
    check(
        "baseline convention is implemented by zero-source subtraction",
        p4_baseline_err < 1e-12,
        f"max zero-source baseline error = {p4_baseline_err:.2e}",
    )
    check(
        "scope firewall: raw |Z| violates additivity, so this is not a selection theorem",
        raw_violation > 0.1,
        f"raw |Z| additivity violation = {raw_violation:.4f}",
    )
    print(
        "  Note: this part verifies the repaired exact log|det| scope only. "
        "It does not derive P2 or claim that the framework uniquely selects W "
        "from all possible scalar-generator choices."
    )


def test_candidate_consistency_checks():
    """Part 7 -- runner-local consistency checks for the supplied W.

    Per the 2026-05-29 scope repair recorded in
    `docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, these checks verify
    structural behavior of the explicitly supplied log|det| functional on the
    registered staggered block:

      * source evenness: because D is real anti-Hermitian on the runner block,
        `|det(D + jI)| = |det(D - jI)|`, so the selected candidate W is even
        in the scalar source;

      * finite-block regularity: `j -> det(D + jI)` is a polynomial in `j`,
        and D is invertible on the checked block, so the candidate
        `log|det(D + jI)|` is regular near zero source;

      * baseline convention: the overall c=1 scale is a convention, while
        zero-source subtraction enforces `W(0) = 0`, and additive shifts do
        not change source-derivative observables.

    This part does not prove or assume a P2 scalar-generator classification
    theorem; it only checks the supplied W.
    """
    print("\n" + "=" * 78)
    print("PART 7: RUNNER-LOCAL CONSISTENCY CHECKS FOR SUPPLIED W")
    print("=" * 78)

    u0 = 0.9

    # Source-evenness check: D is real anti-Hermitian on the
    # staggered block.
    print("\n  Source-evenness check: D is real anti-Hermitian on the runner block.")
    real_d_imag_norm_max = 0.0
    anti_herm_residual_max = 0.0
    re_eig_max = 0.0
    for ls, lt in [(2, 2), (2, 4)]:
        d = build_dirac_4d_apbc(ls, lt, u0)
        real_d_imag_norm_max = max(real_d_imag_norm_max, float(np.linalg.norm(d.imag)))
        anti_herm_residual_max = max(
            anti_herm_residual_max, float(np.linalg.norm(d + d.conj().T))
        )
        eigs = np.linalg.eigvals(d)
        re_eig_max = max(re_eig_max, float(np.max(np.abs(eigs.real))))

    check(
        "D has identically zero imaginary part on the staggered block",
        real_d_imag_norm_max < 1e-12,
        f"max ||Im(D)||_F = {real_d_imag_norm_max:.2e}",
    )
    check(
        "D + D^dagger = 0 (anti-Hermitian) on the staggered block",
        anti_herm_residual_max < 1e-12,
        f"max ||D + D^dagger||_F = {anti_herm_residual_max:.2e}",
    )
    check(
        "Re(spec(D)) = 0 (purely imaginary spectrum) on the staggered block",
        re_eig_max < 1e-10,
        f"max |Re(eigenvalue(D))| = {re_eig_max:.2e}",
    )

    # Candidate source-evenness step: |det(D+J)| = |det(D-J)| is forced by
    # realness of D on the checked source family.
    source_even_err = 0.0
    for ls, lt in [(2, 2), (2, 4)]:
        d = build_dirac_4d_apbc(ls, lt, u0)
        n = d.shape[0]
        for j in [1e-3, 1e-2, 5e-2, 1e-1]:
            jp = j * np.eye(n, dtype=complex)
            zp = abs(np.linalg.det(d + jp))
            zm = abs(np.linalg.det(d - jp))
            source_even_err = max(source_even_err, abs(zp - zm))

    check(
        "source-evenness checked: |det(D + jI)| = |det(D - jI)| for supplied W",
        source_even_err < 1e-12,
        f"max |zp - zm| = {source_even_err:.2e}",
    )

    # Stronger statement: det(D + J) and det(D - J) are complex conjugates
    # for real-Hermitian J (here J = jI is real-symmetric).
    p2_conj_err = 0.0
    for ls, lt in [(2, 2), (2, 4)]:
        d = build_dirac_4d_apbc(ls, lt, u0)
        n = d.shape[0]
        for j in [1e-3, 1e-2, 5e-2]:
            jp = j * np.eye(n, dtype=complex)
            det_p = complex(np.linalg.det(d + jp))
            det_m = complex(np.linalg.det(d - jp))
            # det(D+J) = (det(D-J)).conj() when D is real anti-Hermitian and
            # J is real symmetric, since (D+J)^* = -D + J = -(D - J), and
            # det(-(D-J)) = (-1)^n det(D-J); on the runner blocks dim(D) = n
            # is even, so (-1)^n = 1.
            p2_conj_err = max(p2_conj_err, abs(det_p - det_m.conjugate()))

    check(
        "source-evenness checked (stronger): det(D + jI) = conj(det(D - jI)) on even-dim staggered block",
        p2_conj_err < 1e-9,
        f"max |det(D+J) - conj(det(D-J))| = {p2_conj_err:.2e}",
    )

    # Regularity check: j -> det(D + jI) is a polynomial in j of degree n;
    # log|det(D + jI)| is real-analytic on j-neighborhoods where the polynomial
    # is nonzero. The runner verifies via Taylor-coefficient stability and
    # via D being invertible (so j=0 is in the analyticity neighborhood).
    print("\n  Regularity check: finite-block analyticity of log|det(D + jI)|.")
    p3_d_invertible_err = 0.0
    for ls, lt in [(2, 2), (2, 4)]:
        d = build_dirac_4d_apbc(ls, lt, u0)
        # Smallest singular value bounds invertibility.
        smin = float(np.linalg.svd(d, compute_uv=False)[-1])
        p3_d_invertible_err = max(p3_d_invertible_err, 1.0 / max(smin, 1e-30))
        # Cap to avoid logging huge floats; we only need finiteness.
    check(
        "regularity checked: D is invertible on the runner block (smin > 0)",
        p3_d_invertible_err < 1e3,
        f"max 1/sigma_min(D) = {p3_d_invertible_err:.2e}",
    )

    # Quadratic stability of W(j) ~ A j^2 + O(j^4): verified by checking
    # the small-j ratio W(j) / j^2 converges to A as j -> 0. Analyticity of
    # j -> log|det(D + jI)| (in any neighborhood where det is nonzero) is
    # established structurally from det(D + jI) being a degree-n polynomial
    # in j; the Taylor-coefficient stability check below is a numerical
    # consistency probe (relative tolerance), not the analyticity proof
    # itself.
    p3_quadratic_stab_err = 0.0
    for lt in [2, 4]:
        d = build_dirac_4d_apbc(2, lt, u0)
        n = d.shape[0]
        a_exact = exact_uniform_coefficient_total(lt, u0)
        for j in [1e-3, 1e-2]:
            src = j * np.eye(n, dtype=complex)
            w = observable_generator(d, src)
            ratio = w / j**2
            rel = abs(ratio - a_exact) / max(abs(a_exact), 1e-30)
            p3_quadratic_stab_err = max(p3_quadratic_stab_err, rel)

    check(
        "regularity checked: small-j Taylor ratio W(j)/j^2 converges to A(L_t)",
        p3_quadratic_stab_err < 5e-3,
        f"max relative |W(j)/j^2 - A_exact| / A_exact = {p3_quadratic_stab_err:.2e}",
    )

    # Baseline convention check: c=1 is the chosen generator scale; zero-source
    # baseline fixes the additive convention setting W(0) = 0. Other additive
    # choices differ by a constant.
    print("\n  Baseline convention check: c=1 scale and zero-source subtraction.")
    p4_baseline_zero_err = 0.0
    p4_constant_invariance_err = 0.0
    for ls, lt in [(2, 2), (2, 4)]:
        d = build_dirac_4d_apbc(ls, lt, u0)
        n = d.shape[0]
        # W(0) = 0 by construction.
        p4_baseline_zero_err = max(
            p4_baseline_zero_err,
            abs(observable_generator(d, np.zeros((n, n), dtype=complex))),
        )
        # Source-derivative observables are invariant under an additive
        # constant shift in W (i.e., the convention does not propagate to
        # local observables): d/dj of a constant is zero.
        for j in [1e-3, 1e-2]:
            src = j * np.eye(n, dtype=complex)
            w_native = observable_generator(d, src)
            # Add an arbitrary global constant: simulate by reading W via
            # log|det(D+J)| - log|det D| + C for any C, then derivative
            # in j is unaffected. The scale c=1 is not tested here because
            # changing c would rescale the derivative observables.
            eps = 1e-5
            src_plus = (j + eps) * np.eye(n, dtype=complex)
            src_minus = (j - eps) * np.eye(n, dtype=complex)
            deriv_native = (
                observable_generator(d, src_plus) - observable_generator(d, src_minus)
            ) / (2 * eps)
            # Add an arbitrary constant C to W via a different baseline subtraction.
            c_alt = 17.5
            deriv_alt = (
                (logabs_det(d + src_plus) - logabs_det(d) + c_alt)
                - (logabs_det(d + src_minus) - logabs_det(d) + c_alt)
            ) / (2 * eps)
            p4_constant_invariance_err = max(
                p4_constant_invariance_err, abs(deriv_native - deriv_alt)
            )

    check(
        "baseline convention checked: W(0) = 0 enforced by zero-source subtraction",
        p4_baseline_zero_err < 1e-12,
        f"max |W(0)| = {p4_baseline_zero_err:.2e}",
    )
    check(
        "baseline convention checked: source-derivative observables invariant under additive constant in W",
        p4_constant_invariance_err < 1e-9,
        f"max |dW_native - dW_alt| = {p4_constant_invariance_err:.2e}",
    )

    print(
        "\n  Summary: the supplied log|det| functional passes source-evenness,\n"
        "  finite-block regularity, and additive-baseline invariance checks.\n"
        "  The c=1 scale is a representative normalization, not a derived\n"
        "  physical scale. These checks do not derive a P2 scalar-selection\n"
        "  theorem or promote any cited upstream row."
    )


def main():
    print("Hierarchy observable principle from the lattice axiom")
    print("=" * 78)
    test_source_note_scope_firewall()
    test_additive_scalar_generator()
    test_local_source_response_and_block_locality()
    test_uniform_scalar_generator_from_axiom()
    test_orbit_kernel_and_selector()
    test_hierarchy_value_from_internal_observable_principle()
    test_repaired_logdet_scope_shape()
    test_candidate_consistency_checks()
    print("\n" + "=" * 78)
    print(f"SCORECARD: {PASS_COUNT} pass, {FAIL_COUNT} fail out of {PASS_COUNT + FAIL_COUNT}")
    print("=" * 78)
    sys.exit(1 if FAIL_COUNT else 0)


if __name__ == "__main__":
    main()
