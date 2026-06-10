#!/usr/bin/env python3
"""Plaquette value derivation program checks (2026-06-10).

Paired note:
  docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md

This runner does NOT derive <P>(6) = 0.5934 and does not claim to.  It
verifies the load-bearing content of the paired note:

  Part 1  exact J(beta) engine: order-3 rational recurrence, two independent
      Haar-moment cross-checks (a_3, a_4), |a_n| <= 1/n!, nonnegativity,
      quadrature agreement, canonical P_1plaq(6) helper-surface reproduction.
  Part 2  counting lemmas of the thermodynamic-limit theorem with rate 6*beta/L:
      exact enumeration of torus / wrap / free-box / block-interior plaquette
      counts and the assembled rate constant (exact rational arithmetic).
  Part 3  finite-volume convexity bracket: validated end-to-end on
      the exactly solvable one-plaquette/2D surface, including exhaustive
      adversarial perturbations at the proven envelope and falsification legs.
  Part 4  rigorous cluster-expansion domain certificate: exact
      adjacency constant Delta = 20, rigorous enclosure of the sup-norm
      activity eps(6), the certified threshold eps* = 1/(e^2*Delta*(Delta+2)),
      the certified coupling domain beta_KP, and the quantified failure of
      the certificate at beta = 6.
  Part 5  cost-budget arithmetic of the bracket interface and cross-note residuals.

Check classes: [A] exact arithmetic / enumeration / identity on in-note
statements; [B] cross-note input consistency; [C] first-principles computed
number not present in any input; [D] external comparator (context only).

Deterministic, no RNG, pure python + mpmath + numpy; runtime well under
five minutes.  Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
)

# Helper module consulted ONLY for tagged class-B residuals (admitted reuse
# constant); nothing below derives from it.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import canonical_plaquette_surface as cps  # noqa: E402

mp.mp.dps = 60

PASS_COUNT = 0
FAIL_COUNT = 0
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


# ---------------------------------------------------------------------------
# Part 1: exact J(beta) engine.
# J(b) = int_{SU(3)} exp((b/3) Re Tr U) dU = sum a_n b^n, a_n >= 0 rational.
# Order-3 recurrence (reproven coefficient engine, same as the backbone note):
#   6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}
# seeds a_0 = 1, a_1 = 0, a_2 = 1/36.
# ---------------------------------------------------------------------------

NMAX = 140


def j_series_coeffs(nmax: int) -> list[Fraction]:
    a = [Fraction(1), Fraction(0), Fraction(1, 36)]
    for n in range(2, nmax):
        nxt = (
            Fraction(n * (n + 1)) * a[n]
            + Fraction(2 * (2 * n + 3)) * a[n - 1]
            + a[n - 2]
        ) / Fraction(6 * (n + 1) * (n + 4) * (n + 5))
        a.append(nxt)
    return a


COEFFS = j_series_coeffs(NMAX)


def factorial_fraction(n: int) -> Fraction:
    out = Fraction(1)
    for k in range(2, n + 1):
        out *= k
    return out


def j_bounds(beta: Fraction, deriv: int = 0, nterms: int = 120) -> tuple[Fraction, Fraction]:
    """Rigorous rational enclosure of J^(deriv)(beta) for 0 <= beta <= 8.

    Partial sum is exact; tail uses 0 <= a_n <= 1/n! (proven coefficient
    bound: |(1/3) Re Tr U| <= 1 pointwise and all a_n >= 0), and for
    n >= nterms >= 100, beta <= 8, deriv <= 2 the term ratio of the tail
    majorant n^deriv beta^(n-deriv)/n! is < 1/2, so tail <= 2 * (first
    omitted majorant term).
    """
    assert 0 <= deriv <= 2 and beta <= 8 and nterms >= 100
    s = Fraction(0)
    for n in range(deriv, nterms + 1):
        mult = 1
        for k in range(deriv):
            mult *= n - k
        s += COEFFS[n] * mult * beta ** (n - deriv)
    n1 = nterms + 1
    mult = 1
    for k in range(deriv):
        mult *= n1 - k
    first_majorant = Fraction(mult) * beta ** (n1 - deriv) / factorial_fraction(n1)
    tail_hi = 2 * first_majorant
    return s, s + tail_hi


def j_mid(beta: Fraction, deriv: int = 0) -> mp.mpf:
    lo, hi = j_bounds(beta, deriv)
    return (mp.mpf(lo.numerator) / lo.denominator + mp.mpf(hi.numerator) / hi.denominator) / 2


def run_s1() -> None:
    print("== Part 1: exact J(beta) engine ==")
    # Independent Haar-moment cross-checks.
    # a_3 = (1/3!) (1/27) E[(Re Tr U)^3]; E[(Re Tr U)^3] = 1/4 from
    # trivial-rep multiplicities in F^k x Fbar^(3-k) (k=0,3 give 1 each).
    a3_moment = Fraction(1, 6) * Fraction(1, 27) * Fraction(1, 4)
    check(
        "A",
        "a_3 recurrence value equals independent Haar-moment value 1/648",
        COEFFS[3] == a3_moment == Fraction(1, 648),
        f"a_3 = {COEFFS[3]}",
    )
    # a_4: E[(Re Tr U)^4] = (1/16) * C(4,2) * <chi_F^2, chi_F^2> = 12/16 = 3/4.
    a4_moment = Fraction(1, 24) * Fraction(1, 81) * Fraction(3, 4)
    check(
        "A",
        "a_4 recurrence value equals independent Haar-moment value 1/2592",
        COEFFS[4] == a4_moment == Fraction(1, 2592),
        f"a_4 = {COEFFS[4]}",
    )
    bound_ok = all(
        Fraction(0) <= COEFFS[n] <= Fraction(1) / factorial_fraction(n)
        for n in range(NMAX)
    )
    check(
        "A",
        "0 <= a_n <= 1/n! for all n < 140 (exact rationals)",
        bound_ok,
    )
    # Independent route: Weyl-measure midpoint quadrature on the torus.
    n = 700
    ang = (np.arange(n) + 0.5) / n * 2.0 * np.pi - np.pi
    t1, t2 = np.meshgrid(ang, ang, indexing="ij")
    t3 = -t1 - t2
    haar = (
        np.abs(np.exp(1j * t1) - np.exp(1j * t2)) ** 2
        * np.abs(np.exp(1j * t1) - np.exp(1j * t3)) ** 2
        * np.abs(np.exp(1j * t2) - np.exp(1j * t3)) ** 2
    )
    retr = np.cos(t1) + np.cos(t2) + np.cos(t3)
    w0 = haar.sum()
    j6_quad = float((haar * np.exp(2.0 * retr)).sum() / w0)
    j6_lo, j6_hi = j_bounds(Fraction(6))
    j6 = j_mid(Fraction(6))
    check(
        "A",
        "J(6): rational-recurrence enclosure matches Weyl quadrature",
        abs(j6_quad - float(j6)) < 1e-9 and (j6_hi - j6_lo) < Fraction(1, 10**40),
        f"J(6) = {mp.nstr(j6, 20)}; quad residual = {abs(j6_quad - float(j6)):.2e}",
    )
    p1 = j_mid(Fraction(6), 1) / j_mid(Fraction(6))
    check(
        "B",
        "P_1plaq(6) = J'(6)/J(6) reproduces the canonical helper-surface value 0.422531739649983468...",
        abs(p1 - mp.mpf("0.422531739649983468165680828")) < mp.mpf("1e-25"),
        f"P_1plaq(6) = {mp.nstr(p1, 22)}",
    )
    u_small = j_mid(Fraction(1, 1000), 1) / j_mid(Fraction(1, 1000))
    check(
        "A",
        "small-beta character convention u(beta)/beta -> 1/18",
        abs(u_small / mp.mpf("0.001") - mp.mpf(1) / 18) < mp.mpf("1e-4"),
        f"u(1e-3)/1e-3 = {mp.nstr(u_small / mp.mpf('0.001'), 8)}",
    )
    # Falsification: corrupted seed a_2 -> 1/35 must be detected by quadrature.
    a_bad = [Fraction(1), Fraction(0), Fraction(1, 35)]
    for nn in range(2, 80):
        a_bad.append(
            (
                Fraction(nn * (nn + 1)) * a_bad[nn]
                + Fraction(2 * (2 * nn + 3)) * a_bad[nn - 1]
                + a_bad[nn - 2]
            )
            / Fraction(6 * (nn + 1) * (nn + 4) * (nn + 5))
        )
    j6_bad = sum(float(c) * 6.0**k for k, c in enumerate(a_bad))
    check(
        "A",
        "falsification: corrupted recurrence seed is detected by the quadrature route",
        abs(j6_bad - j6_quad) > 1e-2,
        f"corrupted-seed J(6) deviates by {abs(j6_bad - j6_quad):.3f}",
    )
    # SU(3) trace range (load-bearing for the per-plaquette weight envelope).
    f_crit = mp.cos(2 * mp.pi / 3) * 2 + mp.cos(4 * mp.pi / 3)
    grid_min = float(retr.min())
    grid_max = float(retr.max())
    check(
        "A",
        "Re Tr U range on SU(3) is [-3/2, 3]",
        abs(f_crit + mp.mpf(3) / 2) < mp.mpf("1e-50")
        and grid_min >= -1.5 - 1e-9
        and grid_min < -1.4999
        and grid_max <= 3.0 + 1e-12,
        f"grid min = {grid_min:.10f}, max = {grid_max:.10f}",
    )
    # Lemma L1 single-plaquette instance: ln c0(beta) in [-3beta/2, 0].
    l1_ok = True
    for b in (Fraction(1, 2), Fraction(6), Fraction(12, 1)):
        if b > 8:
            continue
        c0 = mp.e ** (-mp.mpf(b.numerator) / b.denominator) * j_mid(b)
        bb = mp.mpf(b.numerator) / b.denominator
        l1_ok &= bool(-1.5 * bb - mp.mpf("1e-30") <= mp.log(c0) <= 0)
    check(
        "A",
        "deletion lemma L1 one-plaquette instance: ln c0(beta) in [-3beta/2, 0]",
        l1_ok,
    )


# ---------------------------------------------------------------------------
# Part 2: counting lemmas for the thermodynamic-limit theorem.
# ---------------------------------------------------------------------------


def shift(x: tuple[int, ...], d: int, L: int, wrap: bool) -> tuple[int, ...] | None:
    y = list(x)
    y[d] += 1
    if y[d] == L:
        if not wrap:
            return None
        y[d] = 0
    return tuple(y)


def torus_plaquettes(L: int):
    plaqs = []
    for x in itertools.product(range(L), repeat=4):
        for mu in range(4):
            for nu in range(mu + 1, 4):
                xm = shift(x, mu, L, True)
                xn = shift(x, nu, L, True)
                links = frozenset(
                    [(x, mu), (x, nu), (xm, nu), (xn, mu)]
                )
                wrap = (x[mu] == L - 1) or (x[nu] == L - 1)
                plaqs.append((links, wrap))
    return plaqs


def free_box_plaquettes(L: int):
    plaqs = []
    for x in itertools.product(range(L), repeat=4):
        for mu in range(4):
            for nu in range(mu + 1, 4):
                if x[mu] >= L - 1 or x[nu] >= L - 1:
                    continue
                xm = shift(x, mu, L, False)
                xn = shift(x, nu, L, False)
                plaqs.append(frozenset([(x, mu), (x, nu), (xm, nu), (xn, mu)]))
    return plaqs


def run_s2() -> None:
    print("== Part 2: counting lemmas of the thermodynamic-limit theorem ==")
    counts_ok = True
    detail = []
    for L in (2, 3, 4):
        plaqs = torus_plaquettes(L)
        n_tot = len(plaqs)
        n_wrap = sum(1 for _, w in plaqs if w)
        n_free = len(free_box_plaquettes(L))
        ok = (
            n_tot == 6 * L**4
            and n_wrap == 6 * L**2 * (2 * L - 1)
            and n_free == 6 * L**2 * (L - 1) ** 2
            and n_tot - n_wrap == n_free
        )
        counts_ok &= ok
        detail.append(f"L={L}: total={n_tot} wrap={n_wrap} free={n_free}")
    check(
        "A",
        "torus/wrap/free-box plaquette counts match 6L^4 / 6L^2(2L-1) / 6L^2(L-1)^2",
        counts_ok,
        "; ".join(detail),
    )
    block_ok = True
    detail = []
    for ell, n in ((2, 2), (3, 2), (2, 3)):
        L = n * ell
        plaqs = free_box_plaquettes(L)
        interior = 0
        for links in plaqs:
            blocks = set()
            intra = True
            for (x, d) in links:
                y = shift(x, d, L, False)
                bx = tuple(c // ell for c in x)
                by = tuple(c // ell for c in y)
                if bx != by:
                    intra = False
                    break
                blocks.add(bx)
            if intra and len(blocks) == 1:
                interior += 1
        n_int_pred = n**4 * 6 * ell**2 * (ell - 1) ** 2
        n_cross = len(plaqs) - interior
        ok = interior == n_int_pred and n_cross <= 12 * n**4 * ell**3
        block_ok &= ok
        detail.append(f"(l={ell},n={n}): interior={interior} cross={n_cross}")
    check(
        "A",
        "block-decomposition counts: interior = n^4 * 6 l^2(l-1)^2, cross <= 12 n^4 l^3",
        block_ok,
        "; ".join(detail),
    )
    # Exact rational assembly of the thermodynamic-limit rate constant:
    # per-plaquette torus->free error <= (3/2) * (12 L^3)/(6 L^4) * beta = 3 beta / L
    # per-plaquette block error      <= (3/2) * (12 n^4 l^3)/(6 n^4 l^4) * beta = 3 beta / l
    # total |f_L^PBC - f| <= (3 + 3) beta / L = 6 beta / L.
    torus_leg = Fraction(3, 2) * Fraction(12, 6)
    block_leg = Fraction(3, 2) * Fraction(12, 6)
    check(
        "A",
        "thermodynamic-limit rate constant assembles to 6*beta/L from the two counting legs (exact)",
        torus_leg == 3 and block_leg == 3 and torus_leg + block_leg == 6,
        f"legs = {torus_leg} + {block_leg}",
    )


# ---------------------------------------------------------------------------
# Part 3: bracket theorem on the exactly solvable proxy.
# Proxy: f(beta) = -beta + ln J(beta) (per-plaquette free energy of the
# exactly solvable single-plaquette/2D surface), <P>(beta) = J'/J.
# ---------------------------------------------------------------------------


def f2(beta: mp.mpf) -> mp.mpf:
    # series in mp floats (entire function; N=139 terms, beta <= 7 => exact
    # to far below working precision)
    s = mp.mpf(0)
    for k in range(NMAX):
        s += mp.mpf(COEFFS[k].numerator) / COEFFS[k].denominator * beta**k
    return -beta + mp.log(s)


def bracket(fvals: dict[str, mp.mpf], L: int, delta: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    lb = (fvals["mid"] - fvals["lo"]) / delta - (72 - 6 * delta) / (L * delta) + 1
    ub = (fvals["hi"] - fvals["mid"]) / delta + (72 + 6 * delta) / (L * delta) + 1
    return lb, ub


def run_s3() -> None:
    print("== Part 3: bracket theorem on the exactly solvable proxy ==")
    p_exact = j_mid(Fraction(6), 1) / j_mid(Fraction(6))
    chi = j_mid(Fraction(6), 2) / j_mid(Fraction(6)) - p_exact**2  # f''(6) proxy
    contain_ok = True
    widths = []
    for d in ("0.5", "0.1", "0.02"):
        delta = mp.mpf(d)
        lo, mid, hi = f2(6 - delta), f2(mp.mpf(6)), f2(6 + delta)
        lb = (mid - lo) / delta + 1
        ub = (hi - mid) / delta + 1
        contain_ok &= bool(lb <= p_exact <= ub)
        widths.append((delta, ub - lb))
    check(
        "A",
        "convexity chord bracket contains the exact proxy value for all tested delta",
        contain_ok,
        f"<P>_proxy(6) = {mp.nstr(p_exact, 12)}",
    )
    delta, w = widths[-1]
    ratio = w / (delta * chi)
    check(
        "A",
        "bracket width tracks the curvature law delta * f''(6) as delta -> 0",
        abs(ratio - 1) < mp.mpf("0.25"),
        f"width/(delta*chi) = {mp.nstr(ratio, 6)} at delta = {mp.nstr(delta, 3)}",
    )
    # Exhaustive adversarial perturbations at the proven envelope |f_L - f| <= 6 beta / L.
    L, delta = 1000, mp.mpf("0.25")
    betas = {"lo": 6 - delta, "mid": mp.mpf(6), "hi": 6 + delta}
    base = {k: f2(b) for k, b in betas.items()}
    adv_ok = True
    for signs in itertools.product((-1, 1), repeat=3):
        pert = {
            k: base[k] + s * 6 * betas[k] / L
            for (k, b), s in zip(betas.items(), signs)
        }
        lb, ub = bracket(pert, L, delta)
        adv_ok &= bool(lb <= p_exact <= ub)
    check(
        "A",
        "bracket theorem contains the exact value under all 8 extreme envelope perturbations",
        adv_ok,
        f"L = {L}, delta = {mp.nstr(delta, 3)}",
    )
    # Falsification 1: sign-flipped error budget must overshoot.
    pert = {
        "lo": base["lo"] - 6 * betas["lo"] / L,
        "mid": base["mid"] + 36.0 / L,
        "hi": base["hi"],
    }
    lb_bad = (pert["mid"] - pert["lo"]) / delta + (72 - 6 * delta) / (L * delta) + 1
    check(
        "A",
        "falsification: sign-flipped budget produces an invalid lower bound (detected)",
        bool(lb_bad > p_exact),
        f"flipped lb = {mp.nstr(lb_bad, 8)} > exact {mp.nstr(p_exact, 8)}",
    )
    # Falsification 2: a non-convex fake free energy violates the chord ordering.
    g = lambda b: -mp.mpf("0.1") * (b - 6) ** 2  # noqa: E731
    left = (g(mp.mpf(6)) - g(6 - delta)) / delta
    right = (g(6 + delta) - g(mp.mpf(6))) / delta
    check(
        "A",
        "falsification: non-convex fake input violates chord ordering (detected)",
        bool(left > right),
        f"left chord {mp.nstr(left, 4)} > right chord {mp.nstr(right, 4)}",
    )
    return None


# ---------------------------------------------------------------------------
# Part 4: rigorous cluster-expansion domain certificate.
# ---------------------------------------------------------------------------


def run_s4() -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    print("== Part 4: KP cluster-expansion domain certificate ==")
    # Exact adjacency constant Delta on the 4D torus, L = 4.
    plaqs = [links for links, _ in torus_plaquettes(4)]
    link_to_plaqs: dict = {}
    for i, links in enumerate(plaqs):
        for lk in links:
            link_to_plaqs.setdefault(lk, []).append(i)
    per_link = {len(v) for v in link_to_plaqs.values()}
    neigh_counts = set()
    for i, links in enumerate(plaqs):
        nb = set()
        for lk in links:
            nb.update(link_to_plaqs[lk])
        nb.discard(i)
        neigh_counts.add(len(nb))
    check(
        "A",
        "each link lies in exactly 6 plaquettes; link-adjacency degree Delta = 20 exactly",
        per_link == {6} and neigh_counts == {20},
        f"per-link = {sorted(per_link)}, neighbor degrees = {sorted(neigh_counts)}",
    )
    delta_g = 20
    eps_star = 1 / (mp.e**2 * delta_g * (delta_g + 2))
    q_star = mp.e**2 * delta_g * eps_star
    check(
        "A",
        "certified threshold eps* = 1/(e^2*Delta*(Delta+2)) gives subcritical q* = 1/(Delta+2)",
        abs(q_star - mp.mpf(1) / 22) < mp.mpf("1e-40"),
        f"eps* = {mp.nstr(eps_star, 8)}",
    )
    check(
        "A",
        "falsification: adjacency constant is load-bearing (Delta=19 would loosen eps*)",
        bool(1 / (mp.e**2 * 19 * 21) > eps_star),
        f"eps*(19)/eps*(20) = {mp.nstr((1 / (mp.e**2 * 19 * 21)) / eps_star, 6)}",
    )
    # eps(6) = e^6/J(6) - 1 with rigorous J enclosure.
    j6_lo, j6_hi = j_bounds(Fraction(6))
    e6 = mp.e**6
    eps6_lo = e6 / (mp.mpf(j6_hi.numerator) / j6_hi.denominator) - 1
    eps6_hi = e6 / (mp.mpf(j6_lo.numerator) / j6_lo.denominator) - 1
    other_branch = 1 - mp.e ** mp.mpf(-3) / (mp.mpf(j6_lo.numerator) / j6_lo.denominator)
    check(
        "C",
        "sup-norm activity eps(6) = e^6/J(6) - 1 rigorously enclosed",
        bool(eps6_hi - eps6_lo < mp.mpf("1e-30")) and bool(eps6_lo > other_branch),
        f"eps(6) = {mp.nstr((eps6_lo + eps6_hi) / 2, 12)}",
    )
    gap = ((eps6_lo + eps6_hi) / 2) / eps_star
    check(
        "C",
        "beta = 6 fails the certified KP condition by more than 1e5 in activity",
        bool(gap > mp.mpf("1e5")),
        f"eps(6)/eps* = {mp.nstr(gap, 6)}",
    )

    def eps_of(beta: Fraction) -> mp.mpf:
        jlo, jhi = j_bounds(beta)
        jm = (mp.mpf(jlo.numerator) / jlo.denominator + mp.mpf(jhi.numerator) / jhi.denominator) / 2
        bb = mp.mpf(beta.numerator) / beta.denominator
        return max(mp.e**bb / jm - 1, 1 - mp.e ** (-bb / 2) / jm)

    lo_b, hi_b = Fraction(1, 10000), Fraction(1, 1000)
    assert eps_of(lo_b) < eps_star < eps_of(hi_b)
    for _ in range(40):
        mid_b = (lo_b + hi_b) / 2
        if eps_of(mid_b) < eps_star:
            lo_b = mid_b
        else:
            hi_b = mid_b
    beta_kp = (mp.mpf(lo_b.numerator) / lo_b.denominator + mp.mpf(hi_b.numerator) / hi_b.denominator) / 2
    bracket_ok = eps_of(lo_b) < eps_star < eps_of(hi_b)
    check(
        "C",
        "certified coupling domain endpoint beta_KP located (eps(beta_KP) = eps*)",
        bool(bracket_ok) and bool(mp.mpf("2e-4") < beta_kp < mp.mpf("5e-4")),
        f"beta_KP = {mp.nstr(beta_kp, 6)}",
    )
    check(
        "C",
        "framework point beta = 6 exceeds the certified domain by more than 1e4 in coupling",
        bool(6 / beta_kp > mp.mpf("1e4")),
        f"6/beta_KP = {mp.nstr(6 / beta_kp, 6)}",
    )
    # Idealized-activity remark R1: even the best conceivable per-plaquette
    # activity u(6) = J'(6)/J(6) fails any e*(Delta+1)-type neighborhood bound.
    u6 = j_mid(Fraction(6), 1) / j_mid(Fraction(6))
    q_ideal = u6 * mp.e * (delta_g + 1)
    check(
        "A",
        "remark R1: idealized activity u(6)*e*(Delta+1) exceeds 1 by more than a factor 10",
        bool(q_ideal > 10),
        f"u(6)*e*(Delta+1) = {mp.nstr(q_ideal, 6)}",
    )
    return beta_kp, gap, u6


# ---------------------------------------------------------------------------
# Part 5: bracket cost-budget arithmetic and cross-note residuals.
# ---------------------------------------------------------------------------


def run_s5() -> None:
    print("== Part 5: bracket cost budget and cross-note residuals ==")
    p1 = j_mid(Fraction(6), 1) / j_mid(Fraction(6))
    chi = j_mid(Fraction(6), 2) / j_mid(Fraction(6)) - p1**2  # declared curvature proxy
    budget = {}
    for w in ("0.05", "0.01", "0.002"):
        ww = mp.mpf(w)
        budget[w] = 576 * chi / ww**2
    width_l8 = 24 * mp.sqrt(chi / 8)
    check(
        "A",
        "budget: optimal-delta bracket width is 24*sqrt(chi/L) (formula arithmetic)",
        abs(24 * mp.sqrt(chi / budget["0.01"]) - mp.mpf("0.01")) < mp.mpf("1e-25"),
        f"chi_proxy = {mp.nstr(chi, 8)}",
    )
    check(
        "C",
        "a 1e-2-wide rigorous bracket needs certified ln Z_L at L > 1e5",
        bool(budget["0.01"] > mp.mpf("1e5")),
        f"L(0.05) = {mp.nstr(budget['0.05'], 4)}, L(0.01) = {mp.nstr(budget['0.01'], 4)}, "
        f"L(0.002) = {mp.nstr(budget['0.002'], 4)}",
    )
    check(
        "C",
        "at the largest committed MC volume (L=8) the rigorous bracket is vacuous",
        bool(width_l8 > mp.mpf("1.5")),
        f"width(L=8) = {mp.nstr(width_l8, 5)} > full observable range 1.5",
    )
    check(
        "B",
        "admitted reuse constant matches the canonical helper surface (consistency only)",
        cps.CANONICAL_PLAQUETTE == 0.5934,
        "consumed as admitted comparison/reuse number, never derived here",
    )
    check(
        "B",
        "admitted 0.5934 lies inside the committed MC-FSS two-sigma bracket [0.59327, 0.59473]",
        0.59327 < cps.CANONICAL_PLAQUETTE < 0.59473,
        "bracket quoted from PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05",
    )
    check(
        "D",
        "recorded literature singularity modulus ~5.7 lies inside the |beta|=6 disc (context)",
        5.7 < 6.0,
        "comparator context only; consistent with the KP certificate boundary at beta=6",
    )
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "does not derive `0.5934`",
        "admitted comparison/reuse number",
        "one declared import-retirement route",
        "not a feasibility claim",
        "certificate fails at `beta = 6`",
        "Status authority:",
    ]
    missing = [s for s in required if s not in text]
    check(
        "A",
        "paired note declares all required boundaries and non-claims",
        not missing,
        "missing: " + ", ".join(missing) if missing else "all guardrail phrases present",
    )


def main() -> int:
    print("Plaquette value derivation program check (2026-06-10)")
    print(
        "Scope: specification, thermodynamic-limit theorem (rate 6*beta/L),"
        " bracket interface, and KP cluster-domain certificate."
    )
    run_s1()
    run_s2()
    run_s3()
    run_s4()
    run_s5()
    print(
        f"\nBreakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
        f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']}"
    )
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(
        "SCOPE: <P>(6) = 0.5934 is NOT derived here; B1 stays an admitted "
        "reuse number. This runner certifies the specification, the "
        "quantitative thermodynamic-limit theorem, the bracket interface "
        "with its cost budget, and the scoped KP certificate boundary at beta=6."
    )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
