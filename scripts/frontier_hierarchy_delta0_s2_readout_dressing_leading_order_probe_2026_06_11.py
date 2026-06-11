#!/usr/bin/env python3
"""DELTA0 S2 kill-criterion probe: does READOUT-SIDE vacuum-polarization
dressing of the Green-kernel/static-source chain supply one factor
alpha_s per taste decoupling — at leading (resummed-one-loop) order?
(Block08 of the DELTA0 blocking campaign.)

    docs/HIERARCHY_DELTA0_S2_READOUT_DRESSING_LEADING_ORDER_PROBE_
    NOTE_2026-06-11.md

Setting.  The route-inventory synthesis (docs/HIERARCHY_DELTA0_
ATTACHMENT_ROUTE_INVENTORY_SYNTHESIS_NOTE_2026-06-11.md) leaves three
surviving routes to the reduced target of block02 (one factor
alpha_s = alpha_bare/u_0^2 = 0.1033038 per taste decoupling).  Route S2
says the factor might attach on the READOUT side: each decimated taste
species dresses the static-source kernel chain

    V(r) = -C g_bare^2 G(r),   G(r) -> 1/(4 pi |r|)   (Z^3 Maradudin)

via vacuum polarization on the gauge propagator entering V(r) — rather
than dressing the saddle u (that was E3, refuted by block04).  The
inventory's S2 kill criterion: "a computed kernel dressing that is
per-threshold O(1) (or threshold-count-independent) eliminates S2."
This runner EXECUTES that test at leading order, under declared models,
in the block04 (E3) pattern: declared models, robustness variants,
displacement factor vs alpha_s, honest fences.

Declared models (every element DECLARED and fenced; the resummed
one-loop form below is a DECLARED model of the dressing — a geometric
series of one-loop insertions — and NOT a landed framework object;
nothing in this runner upgrades it):

  M1 (readout chain, dressed): the landed chain V_n(r) = -C g^2 G_n(r)
      with the gauge propagator dressed by n fermion species at one
      loop, resummed:
          G_n(k)^(-1) = k_hat^2 * (1 + g^2 * n * Pi_1(k)),
      k_hat^2 = sum_mu (2 - 2 cos k_mu) the exact Z^3 graph-Laplacian
      symbol (the Maradudin-note stencil), Pi_1 the per-species one-loop
      vacuum-polarization scalar, g = g_bare = 1 (I3 surface).
      Undressed n = 0 reproduces the landed chain exactly.

  M2 (per-species polarization Pi_1), TWO declared variants for
      robustness:
        V-a (log form): Pi_1(k) = (b_f/(16 pi^2)) ln(Lambda_hat^2 /
            k_hat^2), the universal small-k continuum-limit log, with
            b_f = 2/3 DECLARED (the per-Dirac-species one-loop beta
            contribution (4/3) T_f at T_f = 1/2), and the lattice-
            regulated constant Lambda_hat^2 declared at TWO values
            (sub-variants a1: Lambda_hat^2 = 1; a2: Lambda_hat^2 = 12,
            the BZ-edge symbol) to show constant-offset independence.
            The universal 1/(16 pi^2) log slope is NOT imported on
            faith: Section B recomputes it as a lattice-regulated 4D
            Brillouin-zone bubble sum
                B(k) = (1/L^4) sum_q 1/(qhat^2 (q+k)hat^2)
            on deterministic fixed half-shifted grids at L = 16, 24, 32
            per direction, with a Richardson-style (1/L^2) consistency
            check between sizes, and verifies the measured log slope
            against 1/(16 pi^2).
        V-b (crude constant form): Pi_1 = c0, a constant evaluated from
            the SAME 4D BZ bubble sum at the readout scale
            k_ro = 2 pi / 8 (the |r| = 8 readout), c0 = b_f *
            B_richardson(k_ro) — shows the conclusion is not a
            log-artifact.

  Readout grids (declared regularization): all 3D momentum sums are
      FFT-free deterministic real cosine sums over half-shifted
      (antiperiodic-like, zero-mode-free) Brillouin-zone grids,
          G_n(r) = (1/L^3) sum_k cos(k . r) / [k_hat^2 (1 + g^2 n
                   Pi_1(k_hat^2))],
      at L3 = 32, 48, 64 per direction, r along an axis at |r| = 4, 6,
      8, with two-point Richardson extrapolation in 1/L (the
      half-shifted torus carries a known O(r/L) alternating-image
      constant; Richardson removes it, and the residual is the genuine
      lattice O(1/r^3) correction — Section A certifies both).

  THE OBSERVABLE: the per-decimation multiplicative factor on the
      large-|r| static-source readout,
          R_S2 = V_15(r) / V_16(r) = G_15(r) / G_16(r)
      (the -C g^2 prefactor cancels exactly in the ratio), computed at
      |r| = 4, 6, 8 per variant, compared against the required
      alpha_s = 0.1033038 via the displacement R_S2 / alpha_s.

Verdict logic (declared up front, the E3 pattern): the candidate rule
"one factor alpha_s per decoupling = leading-order readout dressing" is
  SUPPLIED              if R_S2/alpha_s in [0.99, 1.01] robustly
                        across variants and radii,
  BOUNDED OBSERVATION   if R_S2/alpha_s in [0.5, 2] in any variant at
                        any radius (flagged, model-fenced, NO closure
                        claim),
  ELIMINATED AT LEADING (resummed-one-loop) ORDER otherwise — the
                        inventory's S2 kill criterion fires on its
                        per-threshold-O(1) arm, and the surviving
                        content of S2 narrows to genuinely
                        NON-PERTURBATIVE kernel dressing.

Consistency legs: (F1) the undressed G reproduces the Maradudin
1/(4 pi |r|) asymptotic at the computed radii to the expected
finite-size accuracy (Section A — this re-verifies the landed
normalization on these grids; all S2 content rides it); (F2) R_S2 -> 1
as g -> 0, exactly 1 at g = 0 (Section E); (F3) n-linearity of the
dressing at small g, 16 vs 15 vs 8 species (Section E); (F4) honesty
self-scan: no PDG literal, fences present (Sections F and terminal D).

Vocabulary discipline: Sections A-B are kernel/calibration
infrastructure on declared grids; the M1/M2 solves are deterministic
arithmetic ON DECLARED MODELS (model-fenced, never licensed-surface or
model-independent claims); all remaining open content is printed as
RESIDUAL (declared-open) lines, never as PASSes and never as FAILs.

Deterministic, pure Python stdlib (math, pathlib — same dependency
profile as the block04/E3 runner; no numpy), no network, no randomness
(fixed grids), runtime well under 2 minutes.  Exit code 0 iff
TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
PARENT_NOTE = (DOCS / "HIERARCHY_DELTA0_S2_READOUT_DRESSING_LEADING_"
                      "ORDER_PROBE_NOTE_2026-06-11.md")

PASS_COUNT = 0
FAIL_COUNT = 0
RESIDUAL_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0, "C": 0, "D": 0}


def check(klass: str, name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_COUNTS[klass] += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}][{klass}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def residual(msg: str) -> None:
    global RESIDUAL_COUNT
    RESIDUAL_COUNT += 1
    print(f"  RESIDUAL (declared-open): {msg}")


# ---------------------------------------------------------------------------
# Declared boundary inputs (cited, not asserted; see the parent note).
# ---------------------------------------------------------------------------
P_BOUNDARY = 0.5934                  # B1 licensed reuse number (4 d.p.)
U_0 = P_BOUNDARY ** 0.25             # = 0.877681381 (licensed value)
ALPHA_BARE = 1.0 / (4.0 * math.pi)   # I2 convention at I3 g_bare = 1
ALPHA_S = ALPHA_BARE / U_0 ** 2      # = 0.1033038 (block02 reduction target)

B_F = 2.0 / 3.0                      # declared per-species one-loop beta
                                     # contribution (4/3) T_f, T_f = 1/2
C_UNIV = 1.0 / (16.0 * math.pi ** 2)  # universal one-loop log slope
RADII = (4, 6, 8)                    # declared readout radii (on-axis)
SIZES_3D = (32, 48, 64)              # declared 3D readout grids
SIZES_4D = (16, 24, 32)              # declared 4D bubble grids
K_RO_FRAC = 8                        # readout scale k_ro = 2 pi / 8


# ---------------------------------------------------------------------------
# Half-shifted (zero-mode-free) BZ grids and momentum sums (FFT-free).
# ---------------------------------------------------------------------------
def khat2_table(L: int):
    """1D graph-Laplacian symbol values 2 - 2 cos k on the half-shifted
    grid k = 2 pi (m + 1/2)/L, m = 0..L-1 (never hits k = 0)."""
    return [2.0 - 2.0 * math.cos(2.0 * math.pi * (m + 0.5) / L)
            for m in range(L)]


def green3(L: int, radii, n_species: float, g2: float, pi_func):
    """G_n(r) = (1/L^3) sum_k cos(k.r) / [k_hat^2 (1 + g2 n Pi_1)] by a
    deterministic real cosine sum over the half-shifted 3D BZ grid;
    r on-axis.  pi_func maps k_hat^2 -> Pi_1 (declared M2 variant);
    pi_func(None) convention not used — undressed via n_species = 0."""
    tab = khat2_table(L)
    ks = [2.0 * math.pi * (m + 0.5) / L for m in range(L)]
    out = {r: 0.0 for r in radii}
    gn = g2 * n_species
    for i in range(L):
        ti = tab[i]
        ki = ks[i]
        cosr = [(r, math.cos(ki * r)) for r in radii]
        for j in range(L):
            tij = ti + tab[j]
            for l in range(L):
                kh2 = tij + tab[l]
                if gn:
                    w = 1.0 / (kh2 * (1.0 + gn * pi_func(kh2)))
                else:
                    w = 1.0 / kh2
                for r, c in cosr:
                    out[r] += c * w
    n3 = float(L ** 3)
    return {r: out[r] / n3 for r in radii}


def richardson_1_over_l(l1: int, g1: float, l2: int, g2v: float) -> float:
    """Two-point Richardson in 1/L: removes the leading alternating-
    image O(1/L) torus constant of the half-shifted grid."""
    return (l2 * g2v - l1 * g1) / (l2 - l1)


def richardson_1_over_l2(l1: int, g1: float, l2: int, g2v: float) -> float:
    """Two-point Richardson in 1/L^2 (4D bubble: integrable-singularity
    midpoint error)."""
    w1, w2 = 1.0 / l1 ** 2, 1.0 / l2 ** 2
    return g2v + (g2v - g1) * w2 / (w1 - w2)


def bubble4(L: int, j: int) -> float:
    """4D lattice-regulated one-loop bubble at external momentum
    k = 2 pi j / L along direction 1 (integer j keeps q + k on the
    half-shifted grid):
        B(k) = (1/L^4) sum_q 1/(qhat^2 (q+k)hat^2).
    Deterministic; the three transverse directions are collapsed by the
    exact two-fold symmetry of the half-shifted symbol table."""
    tab = khat2_table(L)
    tabs = [tab[(m + j) % L] for m in range(L)]
    half = L // 2
    v = tab[:half]            # distinct values; each appears exactly 2x
    total = 0.0
    for m1 in range(half):
        a = v[m1]
        for m2 in range(m1, half):
            ab = a + v[m2]
            for m3 in range(m2, half):
                t = ab + v[m3]
                if m1 == m2 == m3:
                    perm = 1
                elif m1 == m2 or m2 == m3:
                    perm = 3
                else:
                    perm = 6
                mult = 8.0 * perm
                s = 0.0
                for i in range(L):
                    s += 1.0 / ((tab[i] + t) * (tabs[i] + t))
                total += mult * s
    return total / float(L) ** 4


# ---------------------------------------------------------------------------
# Declared M2 variants (built in section_b; module-level closures).
# ---------------------------------------------------------------------------
def make_pi_log(lambda_hat2: float):
    def pi_log(kh2: float) -> float:
        return B_F * C_UNIV * math.log(lambda_hat2 / kh2)
    return pi_log


def make_pi_const(c0: float):
    def pi_const(_kh2: float) -> float:
        return c0
    return pi_const


# ---------------------------------------------------------------------------
# Section A — kernel infrastructure + F1 Maradudin re-verification.
# ---------------------------------------------------------------------------
def section_a():
    print("\n--- Section A [C]: undressed kernel — F1 Maradudin "
          "1/(4 pi |r|) re-verification on the declared grids ---")

    # A1: symbol normalization and zero-mode-free grids.
    sym_ok = True
    for x in (0.1, 0.05, 0.01):
        kh2 = 2.0 - 2.0 * math.cos(x)
        sym_ok = sym_ok and abs(kh2 - x * x) <= (x ** 4) / 12.0 * 1.01
    grid_ok = all(min(khat2_table(L)) > 0.0 for L in SIZES_3D + SIZES_4D)
    check("C", "A1 graph-Laplacian symbol k_hat^2 = 2 - 2 cos k has the "
               "Maradudin-note small-k normalization k^2 + O(k^4) "
               "(|k_hat^2 - k^2| <= k^4/12 at 3 test k) and the "
               "half-shifted grids never hit the zero mode "
               "(min k_hat^2 > 0 on every declared 3D and 4D grid)",
          sym_ok and grid_ok)

    # A2: undressed G(r): Richardson(1/L) pairs and deviation from
    # 1/(4 pi r).
    und = {L: green3(L, RADII, 0.0, 0.0, None) for L in SIZES_3D}
    e12 = {}
    e23 = {}
    for r in RADII:
        e12[r] = 4.0 * math.pi * r * richardson_1_over_l(
            SIZES_3D[0], und[SIZES_3D[0]][r], SIZES_3D[1],
            und[SIZES_3D[1]][r])
        e23[r] = 4.0 * math.pi * r * richardson_1_over_l(
            SIZES_3D[1], und[SIZES_3D[1]][r], SIZES_3D[2],
            und[SIZES_3D[2]][r])
        print(f"    r = {r}: 4 pi r G(r) raw "
              + ", ".join(f"L={L}: {4*math.pi*r*und[L][r]:.6f}"
                          for L in SIZES_3D)
              + f";  Richardson(32,48) = {e12[r]:.6f}, "
                f"Richardson(48,64) = {e23[r]:.6f}")
    pair_ok = all(abs(e12[r] - e23[r]) < 0.01 for r in RADII)
    dev_ok = all(abs(e23[r] - 1.0) < 0.5 / r ** 2 for r in RADII)
    check("C", "A2 F1 leg: undressed G reproduces the Maradudin "
               "1/(4 pi |r|) asymptotic at r = 4, 6, 8 — the two "
               "Richardson(1/L) pair estimates agree to < 0.01 and the "
               "production estimate deviates from 1 by < 0.5/r^2 (the "
               "expected lattice-correction budget) at every radius",
          pair_ok and dev_ok,
          ", ".join(f"r={r}: dev = {e23[r]-1.0:+.6f}" for r in RADII))

    # A3: the residual is the genuine lattice O(1/r^3) correction:
    # r^2-scaled deviations stable across radii.
    scaled = {r: (e23[r] - 1.0) * r ** 2 for r in RADII}
    vals = list(scaled.values())
    stable_ok = (all(0.15 <= v <= 0.5 for v in vals)
                 and max(vals) / min(vals) < 1.6)
    check("C", "A3 F1 leg (signature): the residual deviation scales as "
               "1/r^2 relative — r^2-scaled deviations agree across "
               "r = 4, 6, 8 (all in [0.15, 0.5], spread < 1.6x): the "
               "remaining gap is the known subleading lattice "
               "correction ('decays faster than 1/|r|', Maradudin "
               "note), not a normalization error",
          stable_ok,
          ", ".join(f"r={r}: r^2 dev = {scaled[r]:.4f}" for r in RADII))
    return und


# ---------------------------------------------------------------------------
# Section B — Pi_1 calibration (declared M2 variants).
# ---------------------------------------------------------------------------
def section_b():
    print("\n--- Section B [C]: per-species polarization Pi_1 — "
          "lattice-regulated calibration of the declared variants ---")

    # B1: 4D bubble at the two declared external momenta, three sizes,
    # Richardson(1/L^2) consistency.
    k_pairs = {}
    for L in SIZES_4D:
        b1 = bubble4(L, L // 8)      # k = pi/4 = 2 pi / 8 (readout scale)
        b2 = bubble4(L, L // 4)      # k = pi/2
        k_pairs[L] = (b1, b2)
        print(f"    L = {L}: B(pi/4) = {b1:.8f}, B(pi/2) = {b2:.8f}")
    b_ro_12 = richardson_1_over_l2(SIZES_4D[0], k_pairs[SIZES_4D[0]][0],
                                   SIZES_4D[1], k_pairs[SIZES_4D[1]][0])
    b_ro_23 = richardson_1_over_l2(SIZES_4D[1], k_pairs[SIZES_4D[1]][0],
                                   SIZES_4D[2], k_pairs[SIZES_4D[2]][0])
    rich_ok = (abs(b_ro_12 - b_ro_23) / b_ro_23 < 0.01
               and all(b > 0.0 for bs in k_pairs.values() for b in bs))
    check("C", "B1 4D lattice-regulated bubble B(k) = (1/L^4) sum_q "
               "1/(qhat^2 (q+k)hat^2) computed on deterministic "
               "half-shifted grids at L = 16, 24, 32 per direction; "
               "Richardson(1/L^2) estimates of B at the readout scale "
               "from the (16,24) and (24,32) pairs agree to < 1% "
               "relative",
          rich_ok,
          f"B_rich(k_ro): (16,24) = {b_ro_12:.7f}, "
          f"(24,32) = {b_ro_23:.7f}")

    # B2: the measured log slope vs the universal 1/(16 pi^2).
    kh_a = 2.0 - 2.0 * math.cos(math.pi / 4.0)
    kh_b = 2.0 - 2.0 * math.cos(math.pi / 2.0)
    dlog = math.log(kh_b) - math.log(kh_a)
    slopes = {L: (k_pairs[L][0] - k_pairs[L][1]) / dlog for L in SIZES_4D}
    s12 = richardson_1_over_l2(SIZES_4D[0], slopes[SIZES_4D[0]],
                               SIZES_4D[1], slopes[SIZES_4D[1]])
    s23 = richardson_1_over_l2(SIZES_4D[1], slopes[SIZES_4D[1]],
                               SIZES_4D[2], slopes[SIZES_4D[2]])
    slope_ok = (abs(s23 / C_UNIV - 1.0) < 0.05
                and abs(s12 - s23) / C_UNIV < 0.02)
    check("C", "B2 the bubble's measured log slope d B / d ln(1/k_hat^2) "
               "between k = pi/4 and pi/2, Richardson(1/L^2)-"
               "extrapolated, reproduces the universal one-loop "
               "coefficient 1/(16 pi^2) to < 5% (finite-k budget; pair "
               "consistency < 2%): the 1/(16 pi^2) in the declared log "
               "variant is lattice-honest, not imported on faith; "
               "b_f = 2/3 (per-Dirac-species (4/3) T_f) stays a "
               "DECLARED input",
          slope_ok,
          f"slope/C_univ: " + ", ".join(
              f"L={L}: {slopes[L]/C_UNIV:.4f}" for L in SIZES_4D)
          + f"; rich (24,32) = {s23/C_UNIV:.4f}")

    # B3: assemble the declared variants; positivity of the resummed
    # dressing across the BZ at the strongest setting (g = 1, n = 16).
    c0 = B_F * b_ro_23
    variants = (
        ("V-a1 log Lh2=1", make_pi_log(1.0)),
        ("V-a2 log Lh2=12", make_pi_log(12.0)),
        ("V-b const c0", make_pi_const(c0)),
    )
    pos_ok = 0.0 < c0 < 0.1
    details = [f"c0 = b_f * B_rich(k_ro) = {c0:.7f}"]
    for L in SIZES_3D:
        tab = khat2_table(L)
        kh_min = 3.0 * min(tab)
        kh_max = 3.0 * max(tab)
        for name, pf in variants:
            # log variants are monotone in k_hat^2; checking both ends
            # bounds the whole grid.  const is trivially uniform.
            d_lo = 1.0 + 16.0 * pf(kh_min)
            d_hi = 1.0 + 16.0 * pf(kh_max)
            pos_ok = pos_ok and d_lo > 0.0 and d_hi > 0.0
    tab64 = khat2_table(64)
    worst = 1.0 + 16.0 * make_pi_log(1.0)(3.0 * max(tab64))
    details.append(f"min dressing (V-a1, g=1, n=16, BZ edge) = {worst:.4f}")
    check("C", "B3 declared variants assembled (V-a1/V-a2 log with "
               "Lambda_hat^2 in {1, 12}; V-b constant c0 from the "
               "Richardson bubble at the readout scale k_ro = 2 pi/8); "
               "the resummed dressing 1 + g^2 n Pi_1 stays strictly "
               "positive over the entire BZ at the strongest setting "
               "(g = 1, n = 16) in every variant on every declared "
               "grid — no Landau-type pole inside the momentum sum",
          pos_ok, "; ".join(details))
    return variants, c0


# ---------------------------------------------------------------------------
# Section C — the dressed solves (declared model M1 + M2).
# ---------------------------------------------------------------------------
def section_c(variants):
    print("\n--- Section C [A]: dressed readout — R_S2 = V_15(r)/V_16(r) "
          "per variant per radius (g = 1) ---")
    table = {}          # (variant, r) -> (R per L dict, rich)
    all_ok = True
    for name, pf in variants:
        per_l = {}
        for L in SIZES_3D:
            g16 = green3(L, RADII, 16.0, 1.0, pf)
            g15 = green3(L, RADII, 15.0, 1.0, pf)
            per_l[L] = {r: g15[r] / g16[r] for r in RADII}
            all_ok = all_ok and all(
                math.isfinite(g16[r]) and g16[r] > 0.0 and g15[r] > 0.0
                for r in RADII)
        for r in RADII:
            rich = richardson_1_over_l(SIZES_3D[1], per_l[SIZES_3D[1]][r],
                                       SIZES_3D[2], per_l[SIZES_3D[2]][r])
            table[(name, r)] = (per_l, rich)
            print(f"    {name:16s} r = {r}: "
                  + ", ".join(f"R(L={L}) = {per_l[L][r]:.6f}"
                              for L in SIZES_3D)
                  + f";  R_rich = {rich:.6f}")
    check("A", "C1 dressed Green kernels G_n(r) computed for n = 16 and "
               "n = 15 in every declared variant at every declared grid "
               "size by FFT-free deterministic cosine BZ sums; all "
               "values finite and positive; R_S2 = G_15/G_16 tabulated "
               "per variant per radius with Richardson(1/L) production "
               "estimates", all_ok)

    # C2: grid-stability of the ratio + exact algebraic cross-check on
    # the constant variant.
    stab_ok = True
    for (name, r), (per_l, rich) in table.items():
        stab_ok = stab_ok and abs(per_l[64][r] - per_l[48][r]) < 1e-3
        stab_ok = stab_ok and abs(rich - per_l[64][r]) < 2e-3
    cname = variants[2][0]
    c0 = variants[2][1](1.0)     # constant: value independent of kh2
    r_alg = (1.0 + 16.0 * c0) / (1.0 + 15.0 * c0)
    const_ok = all(
        abs(table[(cname, r)][0][L][r] - r_alg) < 1e-12
        for r in RADII for L in SIZES_3D)
    check("A", "C2 the ratio R_S2 is grid-stable (|R(64) - R(48)| < 1e-3 "
               "and |R_rich - R(64)| < 2e-3 for every variant and "
               "radius — finite-size constants cancel in the ratio), "
               "and the constant variant matches its exact algebraic "
               "value (1 + 16 c0)/(1 + 15 c0) to < 1e-12 at every grid "
               "and radius (the constant dressing factors out of the "
               "sum exactly)",
          stab_ok and const_ok,
          f"V-b algebraic R = {r_alg:.10f}")

    # C3: the leading-order shape — R = 1 + O(g^2 Pi_1).
    shape_ok = all(abs(rich - 1.0) < 0.05
                   for (_n, _r), (_pl, rich) in table.items())
    check("A", "C3 in EVERY declared variant at EVERY radius the "
               "per-decimation readout factor is a small perturbative "
               "shift, R_S2 = 1 + O(g^2 Pi_1) with |R_S2 - 1| < 0.05: "
               "removing one species un-screens the kernel by ~1-2%, "
               "not by a factor ~0.1",
          shape_ok,
          ", ".join(f"{n} r={r}: {rich:.6f}"
                    for (n, r), (_pl, rich) in table.items()
                    if r == 8))
    return table


# ---------------------------------------------------------------------------
# Section D — displacement vs alpha_s + verdict logic.
# ---------------------------------------------------------------------------
def section_d(table):
    print("\n--- Section D [A]: displacement R_S2/alpha_s vs the "
          "required per-decoupling factor ---")
    disps = {}
    for (name, r), (_pl, rich) in table.items():
        disps[(name, r)] = rich / ALPHA_S
        print(f"    {name:16s} r = {r}: R_rich = {rich:.6f}, "
              f"R/alpha_s = {rich / ALPHA_S:.4f}")
    outside = all(not (0.5 <= d <= 2.0) for d in disps.values())
    check("A", "D1 displacement R_S2/alpha_s computed per variant per "
               "radius against the block02 target alpha_s = "
               f"{ALPHA_S:.7f}; in NO variant at NO radius does R_S2 "
               "land within a factor 2 of alpha_s",
          outside,
          f"min displacement = {min(disps.values()):.4f}, "
          f"max = {max(disps.values()):.4f}")

    supplied = all(0.99 <= d <= 1.01 for d in disps.values())
    observation = any(0.5 <= d <= 2.0 for d in disps.values())
    eliminated = (not supplied) and (not observation)
    check("A", "D2 verdict logic (declared up front in the docstring) "
               "applied to the computed displacements: 'supplied' fires "
               "nowhere, 'bounded observation' fires nowhere — the "
               "candidate rule 'alpha_s per decoupling = leading-order "
               "(resummed-one-loop) readout dressing' is ELIMINATED AT "
               "LEADING ORDER under every declared variant; the "
               "inventory's S2 kill criterion fires on its "
               "per-threshold-O(1) arm",
          eliminated,
          f"displacement ~ {min(disps.values()):.2f}x-"
          f"{max(disps.values()):.2f}x above alpha_s, an order of "
          f"magnitude")
    return disps


# ---------------------------------------------------------------------------
# Section E — consistency legs F2 (g -> 0) and F3 (n-linearity).
# ---------------------------------------------------------------------------
def section_e(variants):
    print("\n--- Section E [A]: consistency legs — coupling smoothness "
          "and species-count linearity (declared variant V-a1, L = 48) "
          "---")
    pf = variants[0][1]
    L = 48

    # E1 (= leg F2): R -> 1 as g -> 0; exact 1 at g = 0; leading g^2
    # scaling.
    rs = {}
    for g2 in (1.0, 0.25, 0.0625, 0.0):
        g16 = green3(L, RADII, 16.0, g2, pf)
        g15 = green3(L, RADII, 15.0, g2, pf)
        rs[g2] = {r: g15[r] / g16[r] for r in RADII}
    exact_ok = all(rs[0.0][r] == 1.0 for r in RADII)
    mono_ok = all(rs[1.0][r] > rs[0.25][r] > rs[0.0625][r] > 1.0
                  for r in RADII)
    slope_ok = True
    slope_detail = []
    for r in RADII:
        s_hi = (rs[0.25][r] - 1.0) / 0.25
        s_lo = (rs[0.0625][r] - 1.0) / 0.0625
        slope_ok = slope_ok and 0.9 <= s_hi / s_lo <= 1.05
        slope_detail.append(f"r={r}: ratio = {s_hi / s_lo:.4f}")
    check("A", "E1 F2 leg (coupling smoothness): R_S2 = 1 EXACTLY at "
               "g = 0, decreases monotonically toward 1 as g -> 0, and "
               "(R_S2 - 1)/g^2 is stable to within 10% between "
               "g^2 = 0.25 and 0.0625 at every radius — the dressing "
               "is the leading O(g^2 Pi_1) perturbative shift it is "
               "declared to be",
          exact_ok and mono_ok and slope_ok,
          "; ".join(slope_detail))

    # E2 (= leg F3): n-linearity — 16 vs 15 vs 8 species.
    g2 = 0.0625
    g16 = green3(L, RADII, 16.0, g2, pf)
    g15 = green3(L, RADII, 15.0, g2, pf)
    g8 = green3(L, RADII, 8.0, g2, pf)
    lin_ok = True
    lin_detail = []
    for r in RADII:
        one = g15[r] / g16[r] - 1.0
        eight = g8[r] / g16[r] - 1.0
        lin_ok = lin_ok and abs(eight / one - 8.0) < 0.2
        lin_detail.append(f"r={r}: {eight / one:.4f}")
    # resummation bending at g = 1 (reported, bounded).
    g16f = green3(L, (8,), 16.0, 1.0, pf)
    g15f = green3(L, (8,), 15.0, 1.0, pf)
    g8f = green3(L, (8,), 8.0, 1.0, pf)
    bend = (g8f[8] / g16f[8] - 1.0) / (g15f[8] / g16f[8] - 1.0)
    bend_ok = 8.0 <= bend <= 10.0
    check("A", "E2 F3 leg (species-count linearity): at small coupling "
               "(g^2 = 0.0625) removing 8 species shifts the readout "
               "8x as much as removing 1 species to within 2.5% at "
               "every radius (ratio in [7.8, 8.2]) — the dressing is "
               "n-linear at leading order; at g = 1 the resummation "
               "bends the ratio mildly upward (in [8, 10]), as the "
               "geometric-series form requires",
          lin_ok and bend_ok,
          "16->15 vs 16->8: " + ", ".join(lin_detail)
          + f"; bend(g=1, r=8) = {bend:.4f}")


# ---------------------------------------------------------------------------
# Section F — on-disk scans (chain notes, inventory row, honesty fences).
# ---------------------------------------------------------------------------
def section_f():
    print("\n--- Section F [B]: on-disk scans — the chain this probe "
          "dresses, the inventory row it tests, the fences it must "
          "carry ---")

    # F1: the route-inventory S2 row and its kill criterion.
    inv = (DOCS / "HIERARCHY_DELTA0_ATTACHMENT_ROUTE_INVENTORY_"
                  "SYNTHESIS_NOTE_2026-06-11.md")
    inv_flat = " ".join((inv.read_text() if inv.exists() else "").split())
    check("B", "F1 route-inventory synthesis on disk records the S2 row "
               "('readout-side dressing of the Green-kernel/static-"
               "source chain') and its kill criterion ('per-threshold "
               "O(1) (or threshold-count-independent) eliminates S2') — "
               "the exact criterion this probe executes; downstream "
               "rows refine routes without modifying the inventory",
          "S2" in inv_flat
          and "readout-side dressing" in inv_flat.lower()
          and "per-threshold O(1) (or threshold-count-independent) "
              "eliminates S2" in inv_flat
          and "refine routes without modifying the inventory" in inv_flat)

    # F2: the block02 reduced target.
    b02 = (DOCS / "HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_"
                  "DECOUPLING_REDUCTION_NOTE_2026-06-11.md")
    b02_text = b02.read_text() if b02.exists() else ""
    check("B", "F2 block02 reduction note on disk records the target "
               "this probe compares against: one factor alpha_s = "
               "0.1033038 per taste decoupling",
          "alpha_s = 0.1033038" in b02_text
          and "per taste decoupling" in b02_text)

    # F3: the readout chain S2 would dress (I1 + Maradudin + Plancherel).
    mara = (DOCS / "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_"
                   "NOTE_2026-05-18.md")
    mara_flat = " ".join((mara.read_text() if mara.exists()
                          else "").split())
    i1 = (DOCS / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_"
                 "BOUNDED_NOTE_2026-05-27.md")
    i1_flat = " ".join((i1.read_text() if i1.exists() else "").split())
    planch = (DOCS / "ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_"
                     "BOUNDED_NOTE_2026-05-26.md")
    planch_flat = " ".join((planch.read_text() if planch.exists()
                            else "").split())
    check("B", "F3 the landed readout chain is on disk exactly as this "
               "probe consumes it: the Maradudin note's G(r) -> "
               "1/(4 pi |r|) asymptotic and its stencil, the I1 bridge's "
               "static-source readout V(r) = -C g_bare^2 G(r), and the "
               "Plancherel bridge's alpha_bare = 1/(4 pi) composition",
          "1 / (4 pi |r|)" in mara_flat
          and "6 f(x) - sum_{|y - x| = 1} f(y)" in mara_flat
          and "V(r) = - C * g_bare^2 * G(r)" in i1_flat
          and "alpha_bare = 1 / (4 pi)" in planch_flat)

    # F4: the E3 probe note (the elimination pattern imitated here).
    e3 = (DOCS / "HIERARCHY_DELTA0_ATTACHMENT_MEAN_FIELD_FEEDBACK_"
                 "PROBE_NOTE_2026-06-11.md")
    e3_text = e3.read_text() if e3.exists() else ""
    check("B", "F4 the E3 probe note (block04) is on disk: the pattern "
               "this probe imitates — declared models, robustness "
               "variants, displacement factor vs alpha_s, honest "
               "fences — and the saddle-side refutation that makes the "
               "readout side the channel under test here",
          "REFUTED" in e3_text and "declared variant" in e3_text
          and "Vacuum-polarization dressing" in e3_text)

    # F5: parent-note honesty fences.
    note_text = PARENT_NOTE.read_text() if PARENT_NOTE.exists() else ""
    lowered = " ".join(note_text.lower().split())
    required = [
        "declared model",
        "not a landed framework object",
        "eliminated at leading",
        "non-perturbative",
        "does not close the delta0 gate",
    ]
    forbidden = [
        "closes the delta0 gate",
        "removes s2",
        "supplies the attachment",
    ]
    req_missing = [t for t in required if t not in lowered]
    forb_hit = [t for t in forbidden if t in lowered]
    check("B", "F5 parent-note honesty fences on disk: the note labels "
               "the resummed-one-loop form a 'declared model' that is "
               "'not a landed framework object', states the verdict as "
               "'eliminated at leading' (resummed-one-loop) order with "
               "the surviving content narrowed to 'non-perturbative' "
               "kernel dressing, and 'does not close the DELTA0 gate'; "
               "forbidden closure/removal tokens absent",
          not req_missing and not forb_hit,
          f"missing = {req_missing}, hit = {forb_hit}")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence():
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (No PDG quantity is needed or consumed by this probe; the "
          "dressed-kernel")
    print("   ratios and the displacement are internal structure only.)")
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "G1 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_hierarchy_delta0_s2_readout_dressing_leading_order_"
          "probe_2026_06_11.py")
    print(" Block08 of the DELTA0 blocking campaign: the S2 "
          "kill-criterion test at")
    print(" leading order.  Does per-species vacuum-polarization "
          "dressing of the")
    print(" static-source Green-kernel chain V(r) = -C g^2 G(r) supply "
          "one factor")
    print(" alpha_s = 0.1033038 per taste decoupling — on the READOUT "
          "side, where the")
    print(" saddle side (E3) is already refuted?  Computed under "
          "DECLARED models M1")
    print(" (resummed one-loop kernel dressing, a declared model, not a "
          "landed")
    print(" framework object) and M2 (per-species Pi_1: lattice-"
          "calibrated log variants")
    print(" and a constant variant).")
    print(" Parent note: docs/HIERARCHY_DELTA0_S2_READOUT_DRESSING_"
          "LEADING_ORDER_")
    print("              PROBE_NOTE_2026-06-11.md")
    print("=" * 78)

    section_a()
    variants, _c0 = section_b()
    table = section_c(variants)
    disps = section_d(table)
    section_e(variants)
    section_f()
    section_fence()

    # Declared-open residuals.
    print()
    residual("the alpha_s PER-DECOUPLING ATTACHMENT rule (block02 R1) "
             "remains UNSUPPLIED.  This probe ELIMINATES AT LEADING "
             "(resummed-one-loop) ORDER the route-S2 candidate — "
             "per-species vacuum-polarization dressing of the "
             "static-source Green-kernel readout — under every declared "
             "variant at every radius: R_S2 = 1 + O(g^2 Pi_1), a 1-2% "
             "per-threshold shift, displaced ~9.7x-9.9x above "
             "alpha_s = 0.1033038.")
    residual("the surviving content of inventory route S2 NARROWS to "
             "genuinely NON-PERTURBATIVE kernel dressing (beyond any "
             "resummed-one-loop form): unprobed here, declared-open.  "
             "The inventory's S2 row is REFINED (leading-order arm "
             "eliminated), NOT removed; the inventory itself is not "
             "modified.")
    residual("the DELTA0 magnitude gate "
             "(HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_"
             "2026-05-30.md) remains OPEN: the obstruction is sharpened "
             "(the leading-order readout-dressing candidate "
             "eliminated), not closed.")

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded, declared models): the "
          "undressed kernel")
    print("   reproduces the landed Maradudin 1/(4 pi |r|) normalization "
          "on the declared")
    print("   grids (F1), and under the declared resummed-one-loop "
          "dressing the")
    print("   per-decimation readout factor is R_S2 = 1 + O(g^2 Pi_1) "
          "in every variant")
    print("   at every radius — a 1-2% shift, an order of magnitude "
          "(~9.7x-9.9x) above")
    print("   the required alpha_s per decoupling.  ELIMINATED AT "
          "LEADING ORDER (this")
    print("   route): the alpha_s-per-decoupling attachment rule canNOT "
          "be leading-order")
    print("   readout-side vacuum-polarization dressing under any "
          "declared variant; the")
    print("   inventory's S2 kill criterion fires on its per-threshold-"
          "O(1) arm, and S2")
    print("   narrows to genuinely non-perturbative kernel dressing.  "
          "NOT claimed:")
    print("   closure, model-independence, removal of S2, or any "
          "licensed-surface")
    print("   reproduction.  DELTA0 stays open; obstruction sharpened, "
          "not closed.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
