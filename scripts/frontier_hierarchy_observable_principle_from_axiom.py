#!/usr/bin/env python3
"""
Hierarchy observable principle with a declared finite readout boundary.

Goal:
  Replace the imported "effective-action order parameter" language with a
  framework-internal conditional statement on the exact Grassmann Gaussian:

      Z[J] = det(D + J)

  The selection of the scalar generator is a five-input chain (Theorem 1 of
  the parent note, inputs T1-a..T1-e):

    T1-a (computed):       Berezin determinant + exact block factorization
                           Z[J_1 (+) J_2] = Z_1[J_1] Z_2[J_2]   (Part 1)
    T1-b (lemma, recomputed): det(D+J) in R_{>0} on the positive source cone
                           and local invertible derivative patch, facts L1/L2
                           of the det-positivity lemma, recomputed here on the
                           actual runner blocks                  (Part 8)
    T1-c (axiom premise):  Record finite scalar additivity over disjoint
                           record collections (MINIMAL_AXIOMS_2026-06-05)
    T1-d (declared bridge premise -- the Boundary): the readout-identification
                           bridge: W is a continuous function of
                           Z = det(D+J) alone on all of R_{>0}, and disjoint
                           independent source blocks register as disjoint
                           records. NOT derivable from the axiom memo, which
                           excludes source/action and physical-observable
                           identification from Record content.
    T1-e (lemma fact L3):  Cauchy uniqueness on R_{>0}: the continuous
                           additive solutions are exactly the family
                           {W_c = c log r : c in R}; c = 1 is conventional.

  The Cauchy family includes the degenerate c=0 null readout. The source-
  response and selector checks below use the conventional nonzero c=1
  representative with zero-source baseline. With that representative, local
  scalar observables are the source-response coefficients of log|Z|
  (equivalently log Z = Re Log Z on the positive branch). Part 2 residual-
  checks the Theorem-2 trace formulas (first, mixed-second, and same-site-
  second source derivatives) against central finite differences on a
  non-uniform positive-cone source.

  On the minimal hierarchy block this reproduces the exact dimension-4
  effective-potential coefficient A(L_t) (Part 3, verified at u0 = 0.9 and
  u0 = 1.17 together with the exact spectral multiset and pair-product
  determinant identity), and the resulting temporal kernel is exactly the
  bosonic sign/conjugation-closed orbit kernel that selects L_t = 4 -- now by
  an exact counting argument (Klein-four orbits have at most 4 elements, the
  APBC circle has L_t phases, so any L_t > 4 splits), not by scan alone
  (Part 4).

  The out-of-scope Part 5 comparator imports the canonical plaquette-surface
  constants locally inside its own function; the load-bearing Parts 1-4 and
  6-8 are import-free of that helper and Part 5 contributes zero PASS gates.
"""

from __future__ import annotations

import cmath
import math
import sys

import numpy as np

np.set_printoptions(precision=10, linewidth=120, suppress=True)
# Determinant products in the comparison checks can transiently under/overflow;
# the explicit pass/fail tolerances below are the authoritative gates.
np.seterr(over="ignore", under="ignore", divide="ignore", invalid="ignore")

PASS_COUNT = 0
FAIL_COUNT = 0


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

    # Theorem-2 residual checks: the trace formulas
    #   dW/dj_x       =  Re Tr[(D+J)^{-1} P_x]
    #   d2W/dj_x dj_y = -Re Tr[(D+J)^{-1} P_x (D+J)^{-1} P_y]
    # are the actual observable-principle map, so they are verified against
    # central finite differences of W = log|det(D+J)| - log|det D| on a
    # NON-UNIFORM positive-cone source (deterministic fixed seed).
    print("\n  Theorem-2 residual checks: trace formulas vs central finite differences")
    rng = np.random.default_rng(20260610)
    d = build_dirac_4d_apbc(2, 4, 0.9)
    n = d.shape[0]
    j_vec = rng.uniform(0.02, 0.08, size=n)
    src = np.diag(j_vec).astype(complex)
    inv = np.linalg.inv(d + src)
    x_site, y_site = 3, 17
    px = projector(n, x_site)
    py = projector(n, y_site)

    def w_at(extra: np.ndarray) -> float:
        return observable_generator(d, src + extra)

    # First derivative (central difference, eps = 1e-5).
    eps1 = 1e-5
    fd_first = (w_at(eps1 * px) - w_at(-eps1 * px)) / (2.0 * eps1)
    tr_first = float(np.trace(inv @ px).real)
    res_first = abs(fd_first - tr_first)

    # Mixed second derivative (central 4-point stencil, eps = 1e-3).
    eps2 = 1e-3
    fd_mixed = (
        w_at(eps2 * px + eps2 * py)
        - w_at(eps2 * px - eps2 * py)
        - w_at(-eps2 * px + eps2 * py)
        + w_at(-eps2 * px - eps2 * py)
    ) / (4.0 * eps2**2)
    tr_mixed = float(-np.trace(inv @ px @ inv @ py).real)
    res_mixed = abs(fd_mixed - tr_mixed)

    # Same-site second derivative (central 3-point stencil, eps = 1e-3).
    fd_same = (w_at(eps2 * px) - 2.0 * w_at(0.0 * px) + w_at(-eps2 * px)) / eps2**2
    tr_same = float(-np.trace(inv @ px @ inv @ px).real)
    res_same = abs(fd_same - tr_same)

    print(f"  first:        FD={fd_first:.12e}, trace={tr_first:.12e}, residual={res_first:.2e}")
    print(f"  mixed-second: FD={fd_mixed:.12e}, trace={tr_mixed:.12e}, residual={res_mixed:.2e}")
    print(f"  same-second:  FD={fd_same:.12e}, trace={tr_same:.12e}, residual={res_same:.2e}")

    check(
        "Theorem-2 first-derivative trace formula matches central finite difference",
        res_first < 1e-8,
        f"residual = {res_first:.2e} (non-uniform positive-cone source, eps = {eps1:g})",
    )
    check(
        "Theorem-2 mixed-second-derivative trace formula matches central finite difference",
        res_mixed < 1e-4,
        f"residual = {res_mixed:.2e} (non-uniform positive-cone source, eps = {eps2:g})",
    )
    check(
        "Theorem-2 same-site-second-derivative trace formula matches central finite difference",
        res_same < 1e-4,
        f"residual = {res_same:.2e} (non-uniform positive-cone source, eps = {eps2:g})",
    )


def test_uniform_scalar_generator_from_boundary_chain():
    print("\n" + "=" * 78)
    print("PART 3: UNIFORM SCALAR SOURCE GIVES THE EXACT HIERARCHY GENERATOR")
    print("=" * 78)

    max_gen_err = 0.0
    max_even_err = 0.0
    max_pos_err = 0.0
    max_quad_err = 0.0
    max_spec_err = 0.0
    max_pair_err = 0.0

    # Two distinct couplings: u0 = 0.9 (legacy single point) and u0 = 1.17,
    # so the closed-form identity is checked as an identity in u0, not a
    # single-point coincidence.
    for u0 in [0.9, 1.17]:
        print(f"\n  -- coupling u0 = {u0:g} --")
        for lt in [2, 4, 6, 8]:
            d = build_dirac_4d_apbc(2, lt, u0)
            n = d.shape[0]
            dd = d.conj().T @ d
            dd_inv = np.linalg.inv(dd)

            # Spectral multiset check: spec(D) = {+-i u0 sqrt(3 + sin^2 w)},
            # each temporal mode w with multiplicity 4 (= L_s^3 / 2 spatial
            # doublers per sign), totalling 8 Lt = dim(D) eigenvalues.
            eigs = np.linalg.eigvals(d)
            pred = []
            for w in temporal_modes(lt):
                lam = u0 * math.sqrt(3.0 + math.sin(w) ** 2)
                pred.extend([lam] * 4)
                pred.extend([-lam] * 4)
            # spec(D) is purely imaginary (real anti-Hermitian D), so the
            # multiset comparison is on sorted imaginary parts, with the
            # real parts bounded separately.
            spec_err = max(
                float(np.max(np.abs(eigs.real))),
                float(np.max(np.abs(np.sort(eigs.imag) - np.sort(np.array(pred))))),
            )
            max_spec_err = max(max_spec_err, spec_err)

            for j in [1e-4, 1e-3, 1e-2, 1e-1]:
                src = j * np.eye(n, dtype=complex)
                gen = observable_generator(d, src)
                gen_neg = observable_generator(d, -src)
                exact = exact_uniform_generator(lt, u0, j)
                pos = 0.5 * logabs_det(np.eye(n, dtype=complex) + (j**2) * dd_inv)

                # Pair-product determinant identity:
                # log|det(D + jI)| = 4 sum_w log(j^2 + u0^2 (3 + sin^2 w)),
                # each conjugate pair contributing j^2 + u0^2 (3 + sin^2 w).
                pair = 4.0 * sum(
                    math.log(j**2 + u0**2 * (3.0 + math.sin(w) ** 2))
                    for w in temporal_modes(lt)
                )
                pair_err = abs(logabs_det(d + src) - pair)
                max_pair_err = max(max_pair_err, pair_err)

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
        "uniform-source log|det| generator matches the exact Matsubara formula (u0 = 0.9 and 1.17)",
        max_gen_err < 1e-11,
        f"max absolute generator error = {max_gen_err:.2e}",
    )
    check(
        "spec(D) equals the exact multiset {+-i u0 sqrt(3 + sin^2 omega)} x4 per mode",
        max_spec_err < 1e-10,
        f"max eigenvalue multiset error = {max_spec_err:.2e}",
    )
    check(
        "pair-product determinant identity: log|det(D+jI)| = 4 sum_w log(j^2 + u0^2(3+sin^2 w))",
        max_pair_err < 1e-10,
        f"max pair-product identity error = {max_pair_err:.2e}",
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
    print("PART 4: THE SOURCE-CURVATURE KERNEL CERTIFIES THE LT=4 SELECTOR")
    print("=" * 78)

    resolved = []
    max_orbit_size = 0
    counting_ok = True
    for lt in range(2, 14, 2):
        parts = orbit_partition(lt)
        weights = orbit_weights(lt)
        sizes = [len(p) for p in parts]
        max_orbit_size = max(max_orbit_size, max(sizes))
        # Exact counting inequality: with |orbit| <= |V| = 4 and Lt distinct
        # APBC phases, the number of orbits is >= ceil(Lt / 4).
        if len(parts) < -(-lt // 4):
            counting_ok = False
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

    # Exact counting argument (not scan-only): the Klein-four group
    # V = {z, -z, conj(z), -conj(z)} has order 4, so every orbit has at most
    # 4 elements. The APBC temporal circle for Lt carries exactly Lt distinct
    # phases exp(i (2n+1) pi / Lt). Hence a single-orbit kernel requires
    # Lt <= 4 for EVERY Lt, not just the scanned range: any Lt > 4 has
    # >= ceil(Lt/4) >= 2 orbits and splits. Lt = 2 gives the unresolved
    # sign pair {+-i} (orbit size 2); Lt = 4 is the unique resolved
    # single orbit (size 4).
    check(
        "Klein-four orbits never exceed the group-order bound |orbit| <= 4",
        max_orbit_size <= 4,
        f"max orbit size over the scan = {max_orbit_size} (group order = 4)",
    )
    check(
        "exact counting: num_orbits >= ceil(Lt/4), so every Lt > 4 splits and Lt = 4 is unique for all Lt",
        counting_ok and len(orbit_partition(2)[0]) == 2 and len(orbit_partition(4)[0]) == 4,
        "counting inequality holds on scan; Lt=2 orbit size 2 (unresolved sign pair), Lt=4 orbit size 4",
    )


def test_hierarchy_value_from_internal_observable_principle():
    print("\n" + "=" * 78)
    print("PART 5: OUT-OF-SCOPE HIERARCHY COMPARATOR (INFORMATIONAL ONLY)")
    print("=" * 78)

    # Imported locally so the load-bearing Parts 1-4 and 6-8 are import-free
    # of the hard-coded canonical-surface helper; this out-of-scope comparator
    # contributes zero PASS gates.
    from canonical_plaquette_surface import CANONICAL_ALPHA_LM, CANONICAL_PLAQUETTE, CANONICAL_U0

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


def test_conditional_scope_shape():
    """Part 6 -- repaired source-scope verification.

    Per the 2026-06-04 Record repair and 2026-06-06 positive-source-cone
    repair recorded in `docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, the
    load-bearing claim of the parent note is on the Record/P1 finite
    real-positive source surface:

      Record/P1: finite scalar additivity on independent disjoint record
          collections
          (W[J_1 (+) J_2] = W[J_1] + W[J_2])
      Source branch: D is real antisymmetric and the in-scope scalar sources
          keep det(D+J) in R_{>0}, so no determinant phase is present.

    The canonical c=1 generator normalization and zero-source baseline are
    fixed conventionally; finite-block regularity and source-evenness are
    checked as source-branch consistency properties, not as a global
    phase-blindness theorem for arbitrary complex sources.

    This test verifies, *as an empirical statement on the runner's lattice
    Dirac operator*, that:

      - if the candidate generator W = log|det(D+J)| - log|det D| is adopted
        on the Record/P1 real-positive source branch, it is additive on direct
        sums, source-even,
        regular near zero source, and implements the baseline convention
        W(0) = 0;

      - any candidate that violates Record/P1 additivity (e.g. raw |Z|)
        fails to be a unique additive scalar generator, confirming additivity
        is a load-bearing filter rather than a redundant assumption.

    This part does NOT attempt to derive global/off-sector P2. It verifies the
    repaired finite source shape on the runner's block so reviewers can
    independently check that the runner's PASS count matches the source note.
    """
    print("\n" + "=" * 78)
    print("PART 6: REPAIRED SOURCE-SCOPE VERIFICATION (RECORD/P1 + PHASE-FREE SOURCE)")
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
        "Record/P1 additivity holds for the candidate generator W = log|det(D+J)|",
        p1_max_err < 1e-12,
        f"max additivity error = {p1_max_err:.2e}",
    )
    check(
        "source-branch consistency: real-positive candidate is source-even, W(j) = W(-j)",
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
        "Record/P1 is non-vacuous: raw |Z| violates additivity",
        raw_violation > 0.1,
        f"raw |Z| additivity violation = {raw_violation:.4f}",
    )
    print(
        "  Note: this part verifies the repaired finite source shape only "
        "(Record/P1 plus the phase-free real-positive source branch select the "
        "candidate W with the canonical c=1 convention). It does NOT derive "
        "global/off-sector P2; arbitrary complex source phases remain out of "
        "scope for this parent row."
    )


def test_candidate_consistency_checks():
    """Part 7 -- runner-local consistency checks for the selected candidate.

    Per the 2026-05-25 narrowing and 2026-06-06 source-cone repair recorded in
    `docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` §"Runner-local
    consistency checks for source regularity and normalization", these checks
    verify that the selected real-positive source generator has the expected
    structural behavior on the registered staggered block:

      * source evenness: because D is real anti-Hermitian on the runner block,
        `|det(D + jI)| = |det(D - jI)|`, so the selected candidate W is even
        in the scalar source;

      * finite-block regularity: `j -> det(D + jI)` is a polynomial in `j`,
        and D is invertible on the checked block, so the candidate
        `log|det(D + jI)|` is regular near zero source;

      * baseline convention: the overall c=1 scale is a convention, while
        zero-source subtraction enforces `W(0) = 0`, and additive shifts do
        not change source-derivative observables.

    Record/P1 is supplied by the Record axiom only in the narrow finite
    scalar-additivity sense; that premise support is not a bounded-status
    source. Global/off-sector phase-blindness remains out of scope. This part
    does not promote `CPT_EXACT_NOTE` or any cited upstream row; it only checks
    the candidate on the repaired source surface.
    """
    print("\n" + "=" * 78)
    print("PART 7: RUNNER-LOCAL CONSISTENCY CHECKS FOR THE SELECTED CANDIDATE")
    print("=" * 78)

    u0 = 0.9

    # Candidate source-evenness check: D is real anti-Hermitian on the
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
        "source-evenness checked: |det(D + jI)| = |det(D - jI)| for the candidate",
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

    # Candidate regularity check: j -> det(D + jI) is a polynomial in j of degree n;
    # log|det(D + jI)| is real-analytic on j-neighborhoods where the polynomial
    # is nonzero. The runner verifies via Taylor-coefficient stability and
    # via D being invertible (so j=0 is in the analyticity neighborhood).
    print("\n  Candidate regularity check: finite-block analyticity of log|det(D + jI)|.")
    p3_d_invertible_err = 0.0
    for ls, lt in [(2, 2), (2, 4)]:
        d = build_dirac_4d_apbc(ls, lt, u0)
        # Smallest singular value bounds invertibility.
        smin = float(np.linalg.svd(d, compute_uv=False)[-1])
        p3_d_invertible_err = max(p3_d_invertible_err, 1.0 / max(smin, 1e-30))
        # Cap to avoid logging huge floats; we only need finiteness.
    check(
        "candidate regularity checked: D is invertible on the runner block (smin > 0)",
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
        "candidate regularity checked: small-j Taylor ratio W(j)/j^2 converges to A(L_t)",
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
        "\n  Summary: the selected Record/P1 real-positive source candidate passes source-evenness,\n"
        "  finite-block regularity, and additive-baseline invariance checks.\n"
        "  The c=1 scale is a representative normalization, not a derived\n"
        "  physical scale. These checks do not derive global/off-sector P2\n"
        "  or promote any cited upstream row."
    )


def test_lemma_facts_recomputed_on_runner_blocks():
    """Part 8 -- recompute the consumed det-positivity lemma facts (T1-b).

    The five-input chain of Theorem 1 consumes facts L1/L2 of
    `docs/REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md`.
    Citing the lemma is class (B); this part RECOMPUTES the facts on the
    actual runner blocks so the positivity input is verified where it is
    used, including:

      * L1 cone positivity: slogdet sign = +1 for non-uniform positive
        diagonal sources S (deterministic fixed seed), not just uniform jI;
      * L1 mechanism: B = S^{-1/2} D S^{-1/2} is real antisymmetric and
        det(I + B) = prod_k (1 + lambda_k^2) >= 1, so det(S + D) =
        det(S) det(I + B) > 0;
      * L2 hypothesis: ||D^{-1} J||_2 < 1 for EVERY source magnitude this
        runner differentiates or evaluates (uniform |j| <= 0.1 across all
        blocks/couplings used, plus the Part-2 non-uniform patch sources),
        so the Neumann sign-constancy patch actually covers the consumed
        source surface;
      * L2 patch positivity: slogdet sign = +1 for signed (not cone-
        restricted) diagonal sources inside the Neumann patch.
    """
    print("\n" + "=" * 78)
    print("PART 8: DET-POSITIVITY LEMMA FACTS L1/L2 RECOMPUTED ON THE RUNNER BLOCKS")
    print("=" * 78)

    rng = np.random.default_rng(20260610)

    # --- L1 cone positivity + mechanism on non-uniform positive sources ---
    cone_sign_ok = True
    cone_min_logdet = float("inf")
    b_antisym_max = 0.0
    mech_max_err = 0.0
    mech_min_logdet_ipb = float("inf")
    for ls, lt in [(2, 2), (2, 4)]:
        d = build_dirac_4d_apbc(ls, lt, 0.9)
        n = d.shape[0]
        d_real = d.real  # ||Im(D)|| = 0 is checked in Part 7
        for _ in range(3):
            s_diag = rng.uniform(0.02, 0.5, size=n)
            s = np.diag(s_diag)
            sign, logdet = np.linalg.slogdet(s + d_real)
            cone_sign_ok = cone_sign_ok and sign == 1.0
            cone_min_logdet = min(cone_min_logdet, logdet)

            s_inv_half = np.diag(1.0 / np.sqrt(s_diag))
            b = s_inv_half @ d_real @ s_inv_half
            b_antisym_max = max(b_antisym_max, float(np.linalg.norm(b.T + b)))
            lam = np.linalg.eigvals(b).imag
            lam_pos = np.sort(lam[lam > 0])
            # det(I + B) = prod_k (1 + lambda_k^2) >= 1 (compared in log form).
            sign_ipb, logdet_ipb = np.linalg.slogdet(np.eye(n) + b)
            prod_log = float(np.sum(np.log1p(lam_pos**2)))
            mech_max_err = max(
                mech_max_err, abs(logdet_ipb - prod_log) + (0.0 if sign_ipb == 1.0 else 1.0)
            )
            mech_min_logdet_ipb = min(mech_min_logdet_ipb, logdet_ipb)

    check(
        "L1 cone positivity recomputed: slogdet sign = +1 on non-uniform positive diagonal sources",
        cone_sign_ok and math.isfinite(cone_min_logdet),
        f"all signs +1; min log det(S+D) = {cone_min_logdet:.6f}",
    )
    check(
        "L1 mechanism recomputed: B = S^(-1/2) D S^(-1/2) is real antisymmetric",
        b_antisym_max < 1e-12,
        f"max ||B^T + B||_F = {b_antisym_max:.2e}",
    )
    check(
        "L1 mechanism recomputed: det(I+B) = prod(1 + lambda_k^2) >= 1",
        mech_max_err < 1e-9 and mech_min_logdet_ipb >= -1e-12,
        f"max |log det(I+B) - sum log(1+lambda^2)| = {mech_max_err:.2e}, "
        f"min log det(I+B) = {mech_min_logdet_ipb:.6f} (>= 0)",
    )

    # --- L2 hypothesis: ||D^{-1} J|| < 1 for every source magnitude used ---
    j_max_uniform = 0.1  # largest uniform |j| used anywhere in Parts 1, 3, 6, 7
    neumann_max = 0.0
    for u0 in [0.9, 1.17]:
        for lt in [2, 4, 6, 8]:
            d = build_dirac_4d_apbc(2, lt, u0)
            smin = float(np.linalg.svd(d, compute_uv=False)[-1])
            # For diagonal J with max entry j_max: ||D^{-1} J||_2 <= j_max / sigma_min(D).
            neumann_max = max(neumann_max, j_max_uniform / smin)
    # Part-2 non-uniform patch source on the (2,4), u0=0.9 block (entries <= 0.08
    # plus FD stencil offsets <= 1e-3 on single sites).
    d24 = build_dirac_4d_apbc(2, 4, 0.9)
    smin24 = float(np.linalg.svd(d24, compute_uv=False)[-1])
    neumann_max = max(neumann_max, (0.08 + 1e-3) / smin24)

    check(
        "L2 hypothesis recomputed: ||D^-1 J|| < 1 for every source magnitude used in this runner",
        neumann_max < 1.0,
        f"max ||D^-1 J||_2 bound = {neumann_max:.6f} (< 1, Neumann patch covers the consumed sources)",
    )

    # --- L2 patch positivity: signed sources inside the Neumann patch ---
    patch_sign_ok = True
    patch_min_logdet = float("inf")
    for ls, lt in [(2, 2), (2, 4)]:
        d = build_dirac_4d_apbc(ls, lt, 0.9)
        n = d.shape[0]
        d_real = d.real
        smin = float(np.linalg.svd(d_real, compute_uv=False)[-1])
        for _ in range(3):
            j_diag = rng.uniform(-0.08, 0.08, size=n)
            assert float(np.max(np.abs(j_diag))) / smin < 1.0  # inside the patch
            sign, logdet = np.linalg.slogdet(d_real + np.diag(j_diag))
            patch_sign_ok = patch_sign_ok and sign == 1.0
            patch_min_logdet = min(patch_min_logdet, logdet)

    check(
        "L2 patch positivity recomputed: slogdet sign = +1 for signed sources in the Neumann patch",
        patch_sign_ok and math.isfinite(patch_min_logdet),
        f"all signs +1; min log det(D+J) = {patch_min_logdet:.6f}",
    )

    print(
        "\n  Summary: the lemma facts this note consumes (L1 cone positivity and\n"
        "  mechanism, L2 Neumann hypothesis and patch positivity) are recomputed\n"
        "  on the runner's own blocks, so T1-b is runner-verified rather than\n"
        "  citation-only. The Cauchy-uniqueness fact L3 remains cited from the\n"
        "  lemma; its continuity-on-R_{>0} hypothesis is part of the declared\n"
        "  readout-identification bridge premise (the Boundary, T1-d)."
    )


def test_t1d_independence_guardrail():
    """Part 9 -- source guardrail for the T1-d independence no-go.

    The parent row remains conditional on the readout-identification Boundary.
    The 2026-06-16 companion no-go proves this is not a cosmetic caveat:
    Record additivity plus determinant block factorization admits additive
    source readouts that are not determinant-only.
    """
    print("\n" + "=" * 78)
    print("PART 9: T1-D READOUT-INDEPENDENCE GUARDRAIL")
    print("=" * 78)

    repo = sys.path[0] if sys.path[0].endswith("scripts") else "scripts"
    root = repo[:-len("scripts")] if repo.endswith("scripts") else "."
    note_path = root + "docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"
    no_go_path = (
        root
        + "docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md"
    )
    with open(note_path, "r", encoding="utf-8") as handle:
        parent = handle.read()
    with open(no_go_path, "r", encoding="utf-8") as handle:
        no_go = handle.read()

    check(
        "parent cites the T1-d determinant-readout independence no-go",
        "OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md"
        in parent,
    )
    check(
        "parent still declares T1-d as a Boundary, not an axiom-derived theorem",
        "Boundary (declared bridge premise, T1-d)" in parent
        and "not a consequence of `minimal_axioms`" in parent,
    )
    check(
        "companion no-go states the determinant-only quotient is not Record-derived",
        "must not treat T1-d as Record-derived" in no_go
        and "does not add a new axiom" in no_go,
    )


def main():
    print("Hierarchy observable principle with declared finite readout boundary")
    print("=" * 78)
    test_additive_scalar_generator()
    test_local_source_response_and_block_locality()
    test_uniform_scalar_generator_from_boundary_chain()
    test_orbit_kernel_and_selector()
    test_hierarchy_value_from_internal_observable_principle()
    test_conditional_scope_shape()
    test_candidate_consistency_checks()
    test_lemma_facts_recomputed_on_runner_blocks()
    test_t1d_independence_guardrail()
    print("\n" + "=" * 78)
    print(f"SCORECARD: {PASS_COUNT} pass, {FAIL_COUNT} fail out of {PASS_COUNT + FAIL_COUNT}")
    print("=" * 78)
    sys.exit(1 if FAIL_COUNT else 0)


if __name__ == "__main__":
    main()
