#!/usr/bin/env python3
"""Exact checks for the graph-metric class and d=3 discharge note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/MICROCAUSALITY_GRAPH_METRIC_CLASS_AND_D3_SECOND_QUANTIZATION_"
    "DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-20.md"
)
BLOCK07_NOTE = ROOT / (
    "docs/MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK08_NOTE = ROOT / (
    "docs/MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK10_NOTE = ROOT / (
    "docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
DISPERSION_NOTE = ROOT / (
    "docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_"
    "NARROW_THEOREM_NOTE_2026-06-12.md"
)
RP_POS_NOTE = ROOT / (
    "docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_"
    "NOTE_2026-05-28.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_LABELS = [
    "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10",
    "G11", "G12", "G13",
    "N1", "N2", "N3", "N4", "N5", "N6", "N7",
]


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.labels = []

    def check(self, label, condition):
        ok = bool(condition)
        self.labels.append(label.split()[0])
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def needle(self, label, path, needles):
        haystack = normalized_whitespace(path.read_text(encoding="utf-8"))
        if isinstance(needles, str):
            needles = (needles,)
        self.check(
            label,
            all(normalized_whitespace(n) in haystack for n in needles),
        )

    def finish(self):
        if self.labels != EXPECTED_LABELS:
            print(
                "FAIL: gate-manifest drift: labels "
                f"{self.labels} != expected {EXPECTED_LABELS}"
            )
            self.failed += 1
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def cyc(a, L):
    a = a % L
    return min(a, L - a)


def torus_l1(z, L):
    return sum(cyc(a, L) for a in z)


def torus_linf(z, L):
    return max(cyc(a, L) for a in z)


def main():
    checks = CheckRunner()

    # G1 -- torus l1 spheres on (Z/6)^3 vs Z^3.
    L = 6
    pts = list(itertools.product(range(L), repeat=3))
    l1_counts = {}
    for z in pts:
        r = torus_l1(z, L)
        l1_counts[r] = l1_counts.get(r, 0) + 1
    z3_l1 = {1: 6, 2: 18, 3: 38}
    checks.check(
        "G1 torus l1 spheres on (Z/6)^3: 6, 18, 35 vs Z^3's 6, 18, 38 "
        "(equality below L/2; first deficit exactly at r = 3 = L/2)",
        l1_counts.get(1) == 6
        and l1_counts.get(2) == 18
        and l1_counts.get(3) == 35
        and l1_counts[1] == z3_l1[1]
        and l1_counts[2] == z3_l1[2]
        and l1_counts[3] < z3_l1[3],
    )

    # G2 -- torus l_inf spheres on (Z/6)^3 and (Z/8)^3.
    def linf_counts(Lv):
        cnt = {}
        for z in itertools.product(range(Lv), repeat=3):
            r = torus_linf(z, Lv)
            cnt[r] = cnt.get(r, 0) + 1
        return cnt

    c6 = linf_counts(6)
    c8 = linf_counts(8)
    checks.check(
        "G2 torus l_inf spheres: (Z/6)^3 gives 26, 98, 91 (deficit at "
        "r = 3 = L/2); (Z/8)^3 gives 26, 98, 218 = 24r^2+2 below L/2",
        c6.get(1) == 26
        and c6.get(2) == 98
        and c6.get(3) == 91
        and c8.get(1) == 26
        and c8.get(2) == 98
        and c8.get(3) == 218
        and all(24 * r * r + 2 >= c8.get(r, 0) for r in (1, 2, 3)),
    )

    # G3 -- conversion and domination on the torus; seam bond diameter.
    conv_ok = all(
        torus_l1(z, 6) <= 3 * torus_linf(z, 6)
        for z in itertools.product(range(6), repeat=3)
        if any(a % 6 for a in z)
    )
    dom_ok = all(
        cyc(a, 6) <= abs(a) for a in range(-6, 7)
    )
    seam = torus_l1((5 - 0, 0, 0), 6)
    checks.check(
        "G3 torus conversion d1 <= 3 d_inf (enumerated), coordinatewise "
        "|a|_L <= |a| (instances), and the periodic seam bond has torus "
        "diameter 1 (not L-1)",
        conv_ok and dom_ok and seam == 1,
    )

    # G4 -- chain-lemma reach on the 6-cycle with mixed-size supports.
    ring_sets = []
    for a in range(6):
        for ln in (1, 2):
            ring_sets.append(tuple((a + j) % 6 for j in range(ln + 1)))

    def ring_diam(S):
        return max(cyc(u - v, 6) for u in S for v in S)

    reach_ok = True
    for S1 in ring_sets:
        if 0 not in S1:
            continue
        for S2 in ring_sets:
            if not set(S2) & set(S1):
                continue
            total = ring_diam(S1) + ring_diam(S2)
            far = max(cyc(v, 6) for v in S2)
            if far > total:
                reach_ok = False
    checks.check(
        "G4 chain lemma on the 6-cycle (instance illustration, not the "
        "general lemma): reach <= sum of torus diameters for all "
        "mixed-size two-step chains from X = {0}",
        reach_ok,
    )

    # G5 -- d = 3 radicand monotonicity and positivity window.
    m_s, s1, s2, s3 = sp.symbols("m_s s1 s2 s3", positive=True)
    radicand_gap = sp.simplify(
        (m_s**2 + s1**2 + s2**2 + s3**2) - m_s**2
    )
    arc_m = sp.asinh(sp.Rational(1, 2))
    e3_inst = sp.asinh(sp.sqrt(sp.Rational(1, 4) + 3 * sp.Rational(1, 4)))
    t_top = sp.exp(-2 * arc_m)
    checks.check(
        "G5 d = 3 radicand m^2 + sum sin^2 >= m^2 (symbolic, three "
        "terms), E_3 >= arcsinh(m) with a strict instance, and "
        "0 < t <= e^{-2 arcsinh(m)} < 1",
        radicand_gap == s1**2 + s2**2 + s3**2
        and sp.simplify(e3_inst - arc_m).is_positive is True
        and sp.simplify(1 - t_top).is_positive is True
        and sp.simplify(t_top).is_positive is True,
    )

    # G6 -- taste degeneracy.
    k_s = sp.Symbol("k_s", real=True)
    checks.check(
        "G6 taste degeneracy sin^2(k + pi) = sin^2(k) (symbolic)",
        sp.simplify(sp.sin(k_s + sp.pi) ** 2 - sp.sin(k_s) ** 2) == 0,
    )

    # G7 -- per-mode composition, d-blind factor.
    I2 = sp.eye(2)
    ANN = sp.Matrix([[0, 1], [0, 0]])
    SZ = sp.Matrix([[1, 0], [0, -1]])

    def kron(*mats):
        out = mats[0]
        for m in mats[1:]:
            out = sp.Matrix(sp.kronecker_product(out, m))
        return out

    c0 = kron(ANN, I2)
    c1 = kron(SZ, ANN)
    cd0, cd1 = c0.H, c1.H

    def dGamma(X):
        T = sp.zeros(4, 4)
        ops = [(cd0, c0), (cd1, c1)]
        for a in range(2):
            for b in range(2):
                T += X[a, b] * ops[a][0] * ops[b][1]
        return T

    E1, E2, at = sp.symbols("E1 E2 a_tau", positive=True)
    L_sym, d_mode = sp.symbols("L_sym d_mode", positive=True)
    h_diag = sp.diag(E1, E2)
    lnt = sp.diag(-2 * at * E1, -2 * at * E2)
    G_t = sp.simplify(sp.exp(dGamma(lnt)))
    log_G = sp.Matrix(
        4, 4, lambda i, j: sp.simplify(sp.log(G_t[i, i])) if i == j else 0
    )
    H_MB = sp.simplify(-log_G / (2 * at))
    checks.check(
        "G7 per-mode composition -log Gamma(e^{-2 a_tau E})/(2 a_tau) = "
        "dGamma(E) with the 2 a_tau factor independent of the E "
        "argument's dimension content (symbolic two-mode exemplar), and "
        "the mode count (L/2)^d 2^d = L^d (symbolic)",
        sp.simplify(H_MB - dGamma(h_diag)) == sp.zeros(4, 4)
        and sp.simplify(
            (L_sym / 2) ** d_mode * 2**d_mode - L_sym**d_mode
        )
        == 0,
    )

    # G8 -- C_d values and d-monotonicity.
    eta_s = sp.Symbol("eta_s", positive=True)
    d_sym = sp.Symbol("d_sym", positive=True, integer=True)
    C_d_sq = m_s**2 + (d_sym - 1) + sp.cosh(eta_s) ** 2
    c3_inst = sp.sqrt(
        sp.Rational(1, 4) + 2 + sp.cosh(sp.Rational(1, 4)) ** 2
    )
    checks.check(
        "G8 kernel constant: C_d^2 = m^2 + (d-1) + cosh^2(eta), "
        "d-monotone (C_3 > C_1 by the +2), instance C_3(1/4, 1/2) exact",
        sp.simplify(
            C_d_sq.subs(d_sym, 3) - C_d_sq.subs(d_sym, 1) - 2
        )
        == 0
        and sp.simplify(
            c3_inst**2
            - (sp.Rational(9, 4) + sp.cosh(sp.Rational(1, 4)) ** 2)
        )
        == 0
        and sp.simplify(c3_inst).is_positive is True,
    )

    # G9 -- the block08 feed re-gate in C_3 units.
    x = sp.Symbol("x", positive=True)
    numer = sp.expand(24 * x * (1 + x) + 2 * x * (1 - x) ** 2)
    envelope = 1 + 8 * x * (13 + 10 * x + x**2) / (1 - x) ** 3
    checks.check(
        "G9 feed re-gate: numerator 24x(1+x)+2x(1-x)^2 = 2x(13+10x+x^2) "
        "and the envelope evaluates to 585 (in C_3 units) at x = 1/2",
        sp.simplify(numer - 2 * x * (13 + 10 * x + x**2)) == 0
        and sp.simplify(envelope.subs(x, sp.Rational(1, 2)) - 585) == 0,
    )

    # G10 -- thresholds are PER CHOSEN eta (no universal mu): interior
    # instance, rejector, and the false-universal exhibit.
    arcm = sp.asinh(sp.Rational(1, 2))
    eta_int = arcm / 4          # interior of the eta window
    mu_ok = eta_int / 6         # obeys mu < eta/3 for THIS eta
    mu_bad = eta_int / 2        # violates mu < eta/3 for THIS eta
    r3 = arcm / 6
    checks.check(
        "G10 threshold is per-chosen-eta: mu = eta/6 admissible and "
        "mu = eta/2 rejected at eta = arcsinh(m)/4; the false universal "
        "claim exhibited (arcsinh(m)/6 > eta/3 at this eta); r_3 > 0",
        sp.simplify(eta_int / 3 - mu_ok).is_positive is True
        and sp.simplify(eta_int / 3 - mu_bad).is_positive is not True
        and sp.simplify(arcm / 6 - eta_int / 3).is_positive is True
        and sp.simplify(r3).is_positive is True,
    )

    # G11 -- the alias law on a finite-support toy symbol (exact):
    # torus DFT kernel equals the alias sum of the infinite-lattice
    # kernel, and DIFFERS from the naive restriction.
    Lt = 6
    z_var = sp.Symbol("z_var", integer=True)
    h6 = {}
    for z in range(Lt):
        val = sp.Rational(0)
        for mm in range(Lt):
            k = 2 * sp.pi * mm / Lt
            val += sp.cos(4 * k) * sp.exp(sp.I * k * z)
        h6[z] = sp.simplify(sp.expand_complex(val / Lt))
    # infinite-lattice kernel of cos(4k): 1/2 at z = +-4, else 0
    alias = {z: sp.Rational(0) for z in range(Lt)}
    alias[4 % Lt] += sp.Rational(1, 2)
    alias[(-4) % Lt] += sp.Rational(1, 2)
    naive = {z: sp.Rational(0) for z in range(Lt)}  # |z| <= 3 window: no support
    checks.check(
        "G11 alias law (exact toy, d = 1, L = 6, symbol cos 4k): the "
        "torus DFT kernel equals the alias sum sum_n h(z + nL) at every "
        "z, and the naive infinite-lattice restriction is WRONG at "
        "z = 2, 4 (the aliasing exhibit)",
        all(sp.simplify(h6[z] - alias[z]) == 0 for z in range(Lt))
        and h6[2] == sp.Rational(1, 2)
        and h6[4] == sp.Rational(1, 2)
        and any(sp.simplify(h6[z] - naive[z]) != 0 for z in range(Lt)),
    )

    # G12 -- the alias-transfer geometry and the closed-form alias
    # constants A_d(beta).
    geom_ok = True
    Lg = 6
    for z in itertools.product(range(-Lg // 2 + 1, Lg // 2 + 1), repeat=2):
        for n in itertools.product(range(-2, 3), repeat=2):
            if all(c == 0 for c in n):
                continue
            shifted = max(abs(z[i] + n[i] * Lg) for i in range(2))
            ninf = max(abs(c) for c in n)
            zmin = max(min(abs(z[i]) % Lg, Lg - abs(z[i]) % Lg)
                       for i in range(2))
            if shifted < Lg * ninf - Lg // 2 or shifted < zmin:
                geom_ok = False
    u = sp.Symbol("u", positive=True)
    NN = 12
    tel1 = sp.expand(
        (1 - u) * sum(u**jj for jj in range(1, NN + 1)) - (u - u**(NN + 1))
    )
    tel2 = sp.expand(
        (1 - u) ** 3 * sum(jj**2 * u**jj for jj in range(1, NN + 1))
        - u * (1 + u)
    )
    tail2_ok = tel2 != 0 and min(
        sp.degree(mono, u) for mono in tel2.as_ordered_terms()
    ) >= NN + 1
    rational_id = sp.simplify(
        24 * u * (1 + u) / (1 - u) ** 3
        + 2 * u / (1 - u)
        - 2 * u * (13 + 10 * u + u**2) / (1 - u) ** 3
    )
    A3 = 1 + 2 * sp.sqrt(u) * (13 + 10 * u + u**2) / (1 - u) ** 3
    checks.check(
        "G12 alias transfer: ||z + nL||_inf >= max(L||n||_inf - L/2, "
        "||z||_inf,L) enumerated (d = 2, L = 6, ||n||_inf <= 2); shell "
        "sums by finite-N telescoping (geometric exact, j^2 remainder "
        "of degree >= N+1) with the note-carried limit; the rational "
        "identity 24 u(1+u)/(1-u)^3 + 2u/(1-u) = 2u(13+10u+u^2)/(1-u)^3; "
        "A_3(0) = 1",
        geom_ok
        and tel1 == 0
        and tail2_ok
        and rational_id == 0
        and sp.simplify(A3.subs(u, 0) - 1) == 0,
    )

    # G13 -- end-to-end d = 1 torus-kernel instance with the ACTUAL
    # dispersion symbol (m = 1/2, L = 6): exact DFT, exact parity
    # zeros, and the alias-corrected bound C_1 A_1 e^{-eta' d_L(z)}
    # checked at 50 digits (instance gate, not a proof).
    mval = sp.Rational(1, 2)
    Evals = {}
    for mm in range(6):
        k = 2 * sp.pi * mm / 6
        Evals[mm] = sp.asinh(sp.sqrt(mval**2 + sp.sin(k) ** 2))
    hL = {}
    for z in range(6):
        val = sp.Rational(0)
        for mm in range(6):
            k = 2 * sp.pi * mm / 6
            val += Evals[mm] * sp.exp(sp.I * k * z)
        hL[z] = sp.simplify(val / 6)
    eta_full = sp.Rational(3, 4) * sp.asinh(sp.Rational(1, 2))
    eta_half = eta_full / 2
    beta = (eta_full - eta_half) * 6
    uval = sp.exp(-beta)
    A1 = 1 + 2 * sp.sqrt(uval) / (1 - uval)
    C1 = sp.sqrt(sp.Rational(1, 4) + sp.cosh(eta_full) ** 2)
    margins_ok = True
    for z in range(6):
        dL = min(z, 6 - z)
        bound = C1 * A1 * sp.exp(-eta_half * dL)
        margin = sp.N(bound, 50) - sp.Abs(sp.N(hL[z], 50))
        if not margin > sp.Float("1e-30", 50):
            margins_ok = False
    checks.check(
        "G13 end-to-end d = 1 torus instance (m = 1/2, L = 6, eta = "
        "(3/4) arcsinh(1/2), eta' = eta/2): exact parity zeros h_L(1) = "
        "h_L(3) = h_L(5) = 0, and |h_L(z)| <= C_1 A_1 e^{-eta' d_L(z)} "
        "at every z (50-digit instance margins)",
        sp.simplify(hL[1]) == 0
        and sp.simplify(hL[3]) == 0
        and sp.simplify(hL[5]) == 0
        and margins_ok,
    )

    # Needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 block07 audited step sentences (activity display, chain "
        "lemma, disconnected supports, meeting bound, constants) — the "
        "steps the extension carries",
        BLOCK07_NOTE,
        (
            "0 < κ := sup_x Σ_{S∋x} ||h_S|| |S| exp(μ diam(S)) < ∞",
            "choose an overlap point at every step.  The triangle "
            "inequality and the definition of ambient diameter give",
            "This remains true for disconnected supports.",
            "≤ Σ_{x∈S} Σ_{S'∋x} w*(S') ≤ |S|κ",
            "Its constants depend on the family only through the "
            "declared inputs.",
        ),
    )
    checks.needle(
        "N2 dispersion note: E_d display, C_d bound, taste-corner "
        "degeneracy sentence, corner parameterization p_r = k + pi r, "
        "even periods, one-particle boundary, r_d remark",
        DISPERSION_NOTE,
        (
            "E_d(p) = arcsinh(sqrt(m^2 + sum_{mu=1}^d sin^2 p_mu))",
            "C_d(eta, m) = sqrt(m^2 + (d-1) + cosh^2 eta)",
            "taste-degenerate across the `2^d` two-site-cell corners",
            "p_r = k + pi r",
            "even\nspatial periods",
            "one-particle",
            "r_d(m) = arcsinh(m)/(2d) > 0",
        ),
    )
    checks.needle(
        "N3 the landed corner-note's named-open locality feed (the two "
        "prerequisites this note supplies) and its functor authorities",
        BLOCK10_NOTE,
        (
            "this note proves no spatial kernel envelope and makes no "
            "open-chain or periodic-chain activity claim",
            "A one-particle locality estimate cannot be fed into a "
            "many-body bound until the operator identification and "
            "boundary convention are both supplied.",
            "Gamma(A) a^dag(f) = a^dag(Af) Gamma(A)",
            "-log Gamma(t) = dGamma(-log t)",
        ),
    )
    checks.needle(
        "N4 RP-positivity intertwiner (the functor authority)",
        RP_POS_NOTE,
        "Gamma(K) |vac> = |vac>,    Gamma(K) a_p^dag = lambda_p "
        "a_p^dag Gamma(K).",
    )
    checks.needle(
        "N5 block08 feed authority (the Z^3 shell chain consumed: "
        "display, numerator identity, threshold, shell count)",
        BLOCK08_NOTE,
        (
            "= K + 8K q(13+10q+q^2)/(1-q)^3 =: κ_bar",
            "24q(1+q)+2q(1-q)^2=2q(13+10q+q^2)",
            "0 < μ < η/3",
            "#{z:||z||_∞=r}=(2r+1)^3-(2r-1)^3=24r^2+2",
        ),
    )
    checks.needle(
        "N6 axiom memo supplies no dynamics",
        AXIOM_NOTE,
        (
            "Admissibility is not a dynamics axiom.",
            "choose a Hamiltonian or transfer operator",
        ),
    )
    checks.needle(
        "N7 self-pin needles (anti-drift for the target note; NOT "
        "independent evidence)",
        TARGET_NOTE,
        (
            "microcausality_graph_metric_class_and_d3_second_"
            "quantization_discharge_bounded_theorem_note_2026-07-20",
            "REFUTED — block07's incidence-ladder exhibit",
            "the boundary convention the landed corner-note names as "
            "unsupplied",
            "no\n`d`-dependent factor anywhere",
            "**Status: PASS**",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
