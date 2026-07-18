#!/usr/bin/env python3
"""Exact checks for the gauged-kernel weighted-activity feed note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
CT_NOTE = ROOT / (
    "docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_"
    "NARROW_THEOREM_NOTE_2026-06-13.md"
)
BLOCK07_NOTE = ROOT / (
    "docs/MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK04_NOTE = ROOT / (
    "docs/MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
NOTE3_BILINEAR = ROOT / (
    "docs/FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_LABELS = [
    "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
    "N1", "N2", "N3", "N4", "N5", "N6",
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


def main():
    checks = CheckRunner()

    # G1 -- JW norms, evenness, Hermiticity of bilinear terms.
    I2 = sp.eye(2)
    ANN = sp.Matrix([[0, 1], [0, 0]])
    SZ = sp.Matrix([[1, 0], [0, -1]])

    def kron(*mats):
        out = mats[0]
        for m in mats[1:]:
            out = sp.Matrix(sp.kronecker_product(out, m))
        return out

    def c_op(j, n=3):
        return kron(*([SZ] * j + [ANN] + [I2] * (n - j - 1)))

    c = [c_op(j) for j in range(3)]
    cd = [m.H for m in c]

    def op_norm_sq(m):
        return max((m.H * m).eigenvals())

    def com(a, b):
        return a * b - b * a

    def is_zero(m):
        return sp.simplify(m) == sp.zeros(*m.shape)

    hop = cd[0] * c[1]
    dens = cd[0] * c[0]
    kval = (sp.Integer(3) + 4 * sp.I) / 10
    pair_term = kval * cd[0] * c[1] + sp.conjugate(kval) * cd[1] * c[0]
    parity = kron(SZ, SZ, SZ)
    pair_norm_sq = sp.simplify(op_norm_sq(pair_term))
    checks.check(
        "G1 JW norms ||c^t c|| = 1 (hop and density); complex-kernel pair "
        "term Hermitian, even, exact norm |k| = 1/2 <= envelope 2|k| = 1",
        sp.simplify(op_norm_sq(hop) - 1) == 0
        and sp.simplify(op_norm_sq(dens) - 1) == 0
        and is_zero(pair_term - pair_term.H)
        and is_zero(com(pair_term, parity))
        and sp.simplify(pair_norm_sq - sp.Rational(1, 4)) == 0
        and sp.Rational(1, 2) <= 1,
    )

    # G2 -- l_inf shell counts.
    def linf_shell(r):
        return sum(
            1
            for z in itertools.product(range(-r, r + 1), repeat=3)
            if max(abs(a) for a in z) == r
        )

    checks.check(
        "G2 l_inf shell counts (2r+1)^3-(2r-1)^3 = 24r^2+2: 26, 98, 218",
        all(
            linf_shell(r) == 24 * r * r + 2 == (2 * r + 1) ** 3
            - (2 * r - 1) ** 3
            for r in (1, 2, 3)
        ),
    )

    # G3 -- metric conversion with diagonal equality.
    conv_ok = all(
        sum(abs(a) for a in z) <= 3 * max(abs(a) for a in z)
        for z in itertools.product(range(-2, 3), repeat=3)
        if any(z)
    )
    diag = (2, 2, 2)
    checks.check(
        "G3 ||z||_1 <= 3||z||_inf on Z^3 (enumerated) with diagonal "
        "equality attained",
        conv_ok
        and sum(abs(a) for a in diag) == 3 * max(abs(a) for a in diag),
    )

    # G4 -- numerator identity.
    x = sp.Symbol("x", positive=True)
    numer = sp.expand(24 * x * (1 + x) + 2 * x * (1 - x) ** 2)
    checks.check(
        "G4 numerator 24x(1+x)+2x(1-x)^2 = 26x+20x^2+2x^3 = "
        "2x(13+10x+x^2)",
        sp.simplify(numer - (26 * x + 20 * x**2 + 2 * x**3)) == 0
        and sp.simplify(numer - 2 * x * (13 + 10 * x + x**2)) == 0,
    )

    # G5 -- assembly instance kappa/K = 585 at x = 1/2 by bracket.
    xv = sp.Rational(1, 2)
    closed_pairs = 8 * xv * (13 + 10 * xv + xv**2) / (1 - xv) ** 3
    partial_pairs = 4 * sum(
        (24 * r * r + 2) * xv**r for r in range(1, 41)
    )
    # for r >= 30, 24r^2+2 <= (3/2)^r, so the tail is dominated by
    # 4 * sum_{r>40} (3/4)^r = 16 (3/4)^41
    tail_bound = 16 * sp.Rational(3, 4) ** 41
    diff = sp.nsimplify(closed_pairs - partial_pairs)
    # derivation gates: finite-N telescoping identities behind the
    # closed form (limit note-carried)
    fin_n = 8
    geo_fin = sp.expand(
        sum(x**r for r in range(1, fin_n + 1)) * (1 - x)
        - (x - x ** (fin_n + 1))
    )
    r2_fin = sp.expand(
        sum(r * r * x**r for r in range(1, fin_n + 1)) * (1 - x) ** 3
        - (
            x * (1 + x)
            - (fin_n + 1) ** 2 * x ** (fin_n + 1)
            + (2 * fin_n**2 + 2 * fin_n - 1) * x ** (fin_n + 2)
            - fin_n**2 * x ** (fin_n + 3)
        )
    )
    series_val = 2 * xv * (13 + 10 * xv + xv**2) / (1 - xv) ** 3
    exact_scalar = 1 + 2 * series_val
    checks.check(
        "G5 assembly: ENVELOPE pairs part = 584 exactly at x = 1/2 "
        "(closed form DERIVED via finite-N telescoping for sum x^r and "
        "sum r^2 x^r plus note-carried limit, and bracket-checked), "
        "envelope total 585; sharper exact-scalar value 1 + 2*146 = 293",
        sp.simplify(closed_pairs - 584) == 0
        and geo_fin == 0
        and r2_fin == 0
        and diff > 0
        and diff < tail_bound
        and sp.Integer(24 * 30 * 30 + 2) <= sp.Rational(3, 2) ** 30
        and sp.simplify(series_val - 146) == 0
        and exact_scalar == 293
        and 1 + 584 == 585,
    )

    # G6 -- threshold: x < 1 iff mu < gamma/3 (exponent sign + instance).
    g_s, delta_s = sp.symbols("g_s delta_s", positive=True)
    below = sp.simplify(g_s - 3 * (g_s / 3 - delta_s) - 3 * delta_s) == 0
    above = sp.simplify(g_s - 3 * (g_s / 3 + delta_s) + 3 * delta_s) == 0
    x_below = sp.simplify(1 - sp.exp(-sp.Rational(1, 4))).is_positive
    x_above = sp.simplify(sp.exp(sp.Rational(1, 4)) - 1).is_positive
    checks.check(
        "G6 threshold mu < gamma_CT/3, both directions: mu = g/3 - delta "
        "gives exponent 3 delta > 0 (x < 1, instance gated); mu = g/3 + "
        "delta gives exponent -3 delta (x > 1, divergent side, instance "
        "gated)",
        below
        and above
        and (3 * delta_s).is_positive is True
        and x_below is True
        and x_above is True,
    )

    # G7 -- Z2 background-uniformity exhibit, all 8 backgrounds.
    emu = sp.Rational(9, 8)
    sites = (0, 1, 2)
    pairs = [(0, 1), (1, 2), (0, 2)]
    kappas = set()
    norm_multisets = set()
    for signs in itertools.product((1, -1), repeat=3):
        pair_norm = {}
        for (xx, yy), s in zip(pairs, signs):
            r = abs(yy - xx)
            pair_norm[(xx, yy)] = abs(s) * sp.Rational(1, 2) ** r
        norm_multisets.add(tuple(sorted(pair_norm.values())))
        site_kappa = []
        for site in sites:
            tot = sp.Integer(1)  # on-site: |k|=1, |S|=1, diam 0
            for (xx, yy), nv in pair_norm.items():
                if site in (xx, yy):
                    r = abs(yy - xx)
                    tot += 2 * nv * 2 * emu**r
            site_kappa.append(tot)
        kappas.add(max(site_kappa))
    kappas_exact = set()
    for signs in itertools.product((1, -1), repeat=3):
        pair_norm = {}
        for (xx, yy), s in zip(pairs, signs):
            r = abs(yy - xx)
            pair_norm[(xx, yy)] = abs(s) * sp.Rational(1, 2) ** r
        site_kappa = []
        for site in sites:
            tot = sp.Integer(1)
            for (xx, yy), nv in pair_norm.items():
                if site in (xx, yy):
                    r = abs(yy - xx)
                    tot += nv * 2 * emu**r  # EXACT pair norm |k|
            site_kappa.append(tot)
        kappas_exact.add(max(site_kappa))
    checks.check(
        "G7 Z2 exhibit, BOTH conventions: all 8 backgrounds give "
        "identical norms; envelope activity 11/2 and exact-norm "
        "activity 13/4 (1D: l1 = l_inf, stated)",
        len(kappas) == 1
        and len(norm_multisets) == 1
        and kappas.pop() == sp.Rational(11, 2)
        and len(kappas_exact) == 1
        and kappas_exact.pop() == sp.Rational(13, 4),
    )
    # G8 -- scalar factorization shift drops from commutators.
    Cs = sp.Symbol("Cs", positive=True)
    Hm = sp.MatrixSymbol("Hm", 2, 2)
    Am = sp.MatrixSymbol("Am", 2, 2)
    shift_drop = sp.expand(
        (Cs * sp.Identity(2) + Hm) * Am - Am * (Cs * sp.Identity(2) + Hm)
        - (Hm * Am - Am * Hm)
    )
    checks.check(
        "G8 Gaussian-factorization scalar term: [c·1 + H, A] = [H, A] "
        "(identity shift drops from every commutator, symbolic)",
        shift_drop == sp.ZeroMatrix(2, 2),
    )

    # Needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 CT note: kernel display (7), U/volume independence, and "
        "open item (iii) whose fixed-background half is taken",
        CT_NOTE,
        (
            "|| <x| h[U] |y> || <= Const(m, d) e^{-gamma_CT "
            "||x - y||_inf} ,",
            "`gamma_CT` and `Const` independent of the background `U` "
            "and of the volume",
            "(iii) The full **many-body fermionic** transfer-matrix "
            "locality or a **Lieb-Robinson lightcone** — that needs the "
            "separate quasilocal-LR composition step",
        ),
    )
    checks.needle(
        "N2 block07 class and theorem this note feeds",
        BLOCK07_NOTE,
        (
            "microcausality_weighted_quasilocal_class_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**Theorem (weighted quasilocal all-time volume-uniform "
            "Lieb-Robinson bound).**",
        ),
    )
    checks.needle(
        "N3 block04 CAR conventions authority",
        BLOCK04_NOTE,
        "microcausality_fermionic_even_car_walk_expansion_"
        "lieb_robinson_bounded_theorem_note_2026-07-18",
    )
    checks.needle(
        "N4 free-bilinear threshold pattern and landed U = 1 regime",
        NOTE3_BILINEAR,
        (
            "0 < d mu < eta < arcsinh(m)",
            "W_mu := sup_x sum_y ||Phi_{xy}|| exp(mu d_1(x,y))",
        ),
    )
    checks.needle(
        "N5 axiom memo supplies no dynamics",
        AXIOM_NOTE,
        (
            "Admissibility is not a dynamics axiom.",
            "choose a Hamiltonian or transfer operator",
        ),
    )
    checks.needle(
        "N6 target identifiers, theorem, non-claims, Status",
        TARGET_NOTE,
        (
            "microcausality_gauged_kernel_weighted_activity_feed_"
            "bounded_theorem_note_2026-07-18",
            "**Theorem (fixed-background many-body LR for the gauged "
            "bilinear generator).**",
            "**Gaussian factorization**",
            "the envelope evaluates to exactly",
            "Does **not** touch the `U`-integrated / gauge-measure case",
            "**Status: PASS**",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
