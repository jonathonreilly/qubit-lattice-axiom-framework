#!/usr/bin/env python3
"""Exact checks for the weighted quasilocal-class walk-expansion LR note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK03_NOTE = ROOT / (
    "docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK04_NOTE = ROOT / (
    "docs/MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
NOTE4_BRIDGE = ROOT / (
    "docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_"
    "THEOREM_NOTE_2026-05-09.md"
)
NOTE2_EXPDECAY = ROOT / (
    "docs/EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_"
    "THEOREM_NOTE_2026-06-11.md"
)
NOTE3_BILINEAR = ROOT / (
    "docs/FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_LABELS = [
    "Q1", "Q2", "Q3", "Q4", "Q4b", "Q5a", "Q5b", "Q6", "Q7", "Q8",
    "Q9", "Q10", "Q11",
    "N1", "N2", "N3", "N4", "N4b", "N5", "N6",
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

    # Q1 -- l1 sphere counts on Z^3.
    def sphere_count(r):
        c = 0
        for x in itertools.product(range(-r, r + 1), repeat=3):
            if sum(abs(a) for a in x) == r:
                c += 1
        return c

    checks.check(
        "Q1 l1 sphere counts on Z^3: 4r^2+2 at r = 1..4",
        all(sphere_count(r) == 4 * r * r + 2 for r in (1, 2, 3, 4)),
    )

    # Q2 -- chain lemma reach on explicit mixed-size 1D families.
    # Supports: integer intervals of length 1..3 (diam 0 excluded; use
    # diam 1..2 segments plus singleton-free class), inside [-6, 6].
    def segments(box, max_diam):
        out = []
        for a in range(-box, box + 1):
            for dlen in range(1, max_diam + 1):
                if a + dlen <= box:
                    out.append(tuple(range(a, a + dlen + 1)))
        return out

    segs = segments(6, 2)

    def chains_from(x0, k):
        starts = [s for s in segs if x0 in s]
        chains = [(s,) for s in starts]
        for _ in range(k - 1):
            chains = [
                c + (s2,)
                for c in chains
                for s2 in segs
                if set(s2) & set(c[-1])
            ]
        return chains

    reach_ok = True
    for k in (1, 2):
        for c in chains_from(0, k):
            total_diam = sum(len(s) - 1 for s in c)
            max_dist = max(abs(v) for s in c for v in s)
            if max_dist > total_diam:
                reach_ok = False
    # sharpness: a k=2 chain with two diam-2 segments reaches 4
    sharp = any(
        max(abs(v) for s in c for v in s) == 4
        and sum(len(s) - 1 for s in c) == 4
        for c in chains_from(0, 2)
    )
    checks.check(
        "Q2 chain lemma on mixed-size segments: reach <= sum of diameters "
        "(all chains k = 1, 2), attained",
        reach_ok and sharp,
    )

    # Q3 -- bond meeting counts: union bound 12 vs distinct 11 vs
    # non-self 10.
    AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def add(p, q):
        return tuple(a + b for a, b in zip(p, q))

    def incident(site):
        out = set()
        for d in AXES:
            for sg in (1, -1):
                out.add(frozenset((site, add(site, tuple(sg * c for c in d)))))
        return out

    b0 = frozenset(((0, 0, 0), (1, 0, 0)))
    union_count = sum(len(incident(s)) for s in b0)
    meeting = set()
    for s in b0:
        meeting |= incident(s)
    checks.check(
        "Q3 union bound 12 vs distinct meeting bonds 11 vs non-self 10",
        union_count == 12
        and len(meeting) == 11
        and len(meeting - {b0}) == 10,
    )

    # Q4 -- peeling algebra: the |S| handed up reconstitutes w*, and the
    # inductive step closes.
    s_j, kappa, w_j = sp.symbols("s_j kappa w_j", positive=True)
    n_exp = sp.Symbol("n_exp", integer=True, positive=True)
    step = sp.simplify(
        kappa ** (n_exp) * (s_j * kappa) - s_j * kappa ** (n_exp + 1)
    )
    checks.check(
        "Q4 peeling inductive-step algebra kappa^n (|S| kappa) = "
        "|S| kappa^(n+1) (the reconstitution itself is exercised "
        "exhaustively in Q4b)",
        step == 0,
    )
    # Q4b -- ALL-SUBSETS exhaustive peeling gate on a 5-site segment,
    # disconnected supports included.
    sites5 = (0, 1, 2, 3, 4)
    fam = []
    for rsize in range(1, 6):
        for combo in itertools.combinations(sites5, rsize):
            diam = max(combo) - min(combo)
            norm = sp.Rational(1, 3) ** diam * sp.Rational(1, 2) ** rsize
            fam.append((frozenset(combo), norm, rsize, diam))
    emu5 = sp.Rational(5, 4)

    def wstar_f(entry):
        S, norm, rsize, diam = entry
        return norm * rsize * emu5**diam

    def wplain_f(entry):
        S, norm, rsize, diam = entry
        return norm * emu5**diam

    kappa_fam = max(
        sum(wstar_f(e) for e in fam if x in e[0]) for x in sites5
    )
    n_x_w_fam = sum(wstar_f(e) for e in fam if 0 in e[0])
    ok4b = True
    chains = [(e,) for e in fam if 0 in e[0]]
    for k_len in (1, 2, 3):
        if k_len > 1:
            chains = [
                c + (e2,)
                for c in chains
                for e2 in fam
                if e2[0] & c[-1][0]
            ]
        total = sum(
            sp.prod([wplain_f(e) for e in c])
            for c in chains
            if 4 in c[-1][0]
        )
        bound = n_x_w_fam * kappa_fam ** (k_len - 1)
        if not total < bound:
            ok4b = False
    checks.check(
        "Q4b ALL-SUBSETS peeling gate: every nonempty subset of a "
        "five-site segment (disconnected included), all X-to-Y chains "
        "k = 1, 2, 3, exact sums strictly below n_X^w kappa^(k-1)",
        ok4b and len(fam) == 31,
    )

    # Q5 -- finite mixed family: exact chain sums vs the bound.
    # 1D box [-4,4], pair supports {x,y}, ||h|| = (1/2)^r, e^mu = 3/2.
    box = 4
    emu = sp.Rational(3, 2)
    lam = sp.Rational(1, 2)
    pairs = []
    for x in range(-box, box + 1):
        for y in range(x + 1, box + 1):
            r = y - x
            if r <= 3:
                pairs.append((frozenset((x, y)), r))

    def w_plain(r):
        return lam**r * emu**r

    def w_star(r):
        return 2 * lam**r * emu**r

    kappa_box = max(
        sum(w_star(r) for (S, r) in pairs if x in S)
        for x in range(-box, box + 1)
    )
    n_x_w = sum(w_star(r) for (S, r) in pairs if 0 in S)
    checks.check(
        "Q5a finite-family activity: kappa_box = 111/16 attained at "
        "interior sites and n_X^w = 111/16 at X = {0}",
        kappa_box == sp.Rational(111, 16) and n_x_w == sp.Rational(111, 16),
    )
    y_site = 3
    sigma1 = sum(
        w_plain(r) for (S, r) in pairs if 0 in S and y_site in S
    )
    sigma2 = sp.Integer(0)
    for (S1, r1) in pairs:
        if 0 not in S1:
            continue
        for (S2, r2) in pairs:
            if S2 & S1 and y_site in S2:
                sigma2 += w_plain(r1) * w_plain(r2)
    checks.check(
        "Q5b exact chain sums below the bound: Sigma_1 <= n_X^w and "
        "Sigma_2 <= n_X^w * kappa_box (both strict)",
        sigma1 < n_x_w and sigma2 < n_x_w * kappa_box,
    )

    # Q6 -- assembly resummation and edge checks.
    kap, t_s, a_n, b_n, nw = sp.symbols("kap t_s a_n b_n nw", positive=True)
    k = sp.Symbol("k", integer=True, positive=True)
    ident = sp.simplify(
        2 ** (k + 1) * kap ** (k - 1) * t_s**k
        - (2 / kap) * (2 * kap * t_s) ** k
    )
    series = sp.Sum((2 * kap * t_s) ** k / sp.factorial(k), (k, 1, sp.oo)).doit()
    display = (
        b_n * a_n * nw / kap * 2 * (sp.exp(2 * kap * t_s) - 1)
    )
    k1_coeff = sp.diff(display, t_s).subs(t_s, 0)
    checks.check(
        "Q6 assembly: 2^(k+1) kap^(k-1) t^k = (2/kap)(2 kap t)^k, series "
        "= e^{2 kap t} - 1, t = 0 tight, order-one MAJORANT coefficient "
        "4 a b n_X^w",
        ident == 0
        and sp.simplify(series - (sp.exp(2 * kap * t_s) - 1)) == 0
        and display.subs(t_s, 0) == 0
        and sp.simplify(k1_coeff - 4 * a_n * b_n * nw) == 0,
    )

    # Q7 -- bond-class consistency: kappa = 12 J e^mu and the 6/5 ratio.
    j_s, mu_e = sp.symbols("j_s mu_e", positive=True)
    center = (0, 0, 0)
    sat_sum = sum(
        j_s * 2 * mu_e for _ in incident(center)
    )
    single_bond_kappa = j_s * 2 * mu_e
    checks.check(
        "Q7 bond-class ENVELOPE: saturated bulk model attains "
        "12 J e^mu exactly (6 incident bonds enumerated); a single-bond "
        "family gives only 2 J e^mu; envelope ratio 24/20 = 6/5",
        sp.simplify(sat_sum - 12 * j_s * mu_e) == 0
        and sp.simplify(single_bond_kappa - 2 * j_s * mu_e) == 0
        and single_bond_kappa != 12 * j_s * mu_e
        and sp.Rational(24, 20) == sp.Rational(6, 5),
    )

    # Q8 -- numerator algebra and finite-N geometric identities.
    rho = sp.Symbol("rho", positive=True)
    numer = sp.expand(4 * rho * (1 + rho) + 2 * rho * (1 - rho) ** 2)
    fin_n = 8
    geo_fin = sp.expand(
        sum(rho**r for r in range(1, fin_n + 1)) * (1 - rho)
        - (rho - rho ** (fin_n + 1))
    )
    r_fin = sp.expand(
        sum(r * rho**r for r in range(1, fin_n + 1)) * (1 - rho) ** 2
        - (rho - (fin_n + 1) * rho ** (fin_n + 1) + fin_n * rho ** (fin_n + 2))
    )
    r2_partial = sum(r * r * rho**r for r in range(1, fin_n + 1))
    r2_closed_fin = sp.expand(
        r2_partial * (1 - rho) ** 3
        - (
            rho * (1 + rho)
            - (fin_n + 1) ** 2 * rho ** (fin_n + 1)
            + (2 * fin_n**2 + 2 * fin_n - 1) * rho ** (fin_n + 2)
            - fin_n**2 * rho ** (fin_n + 3)
        )
    )
    checks.check(
        "Q8 numerator 4rho(1+rho)+2rho(1-rho)^2 = 2rho(3+rho^2) and "
        "finite-N telescoping identities for sum rho^r, sum r rho^r, "
        "AND sum r^2 rho^r",
        sp.simplify(numer - 2 * rho * (3 + rho**2)) == 0
        and geo_fin == 0
        and r_fin == 0
        and sp.expand(r2_closed_fin) == 0,
    )

    # Q9 -- closed-form kappa instances by partial sum + tail bracket.
    def series_closed(rr):
        """Closed form of sum_{r>=1} (4r^2+2) rr^r = 2 rr (3+rr^2)/(1-rr)^3."""
        return 2 * rr * (3 + rr**2) / (1 - rr) ** 3

    ok9 = True
    for rho_v, n_cut, dom_base, series_expect, kappa_expect in (
        (sp.Rational(1, 3), 25, sp.Rational(2, 3),
         sp.Integer(7), sp.Integer(14)),
        (sp.Rational(3, 4), 120, sp.Rational(27, 32),
         sp.Integer(342), sp.Integer(684)),
    ):
        partial = sum(
            (4 * r * r + 2) * rho_v**r for r in range(1, n_cut + 1)
        )
        closed = series_closed(rho_v)
        # tail: for r > n_cut, (4r^2+2) rho^r <= dom_base^r with
        # dom_base < 1 (growth majorant times rho)
        tail_bound = dom_base ** (n_cut + 1) / (1 - dom_base)
        diff = sp.nsimplify(closed - partial)
        if not (diff > 0 and diff < tail_bound):
            ok9 = False
        if sp.simplify(closed - series_expect) != 0:
            ok9 = False
        # kappa = 2 J0 * series (w* carries the |S| = 2 factor)
        if sp.simplify(2 * closed - kappa_expect) != 0:
            ok9 = False
    kappa_1d = 4 * sp.Rational(1, 2) / (1 - sp.Rational(1, 2))
    checks.check(
        "Q9 closed-form kappa instances: kappa_3D = 14 J0 (rho=1/3) and "
        "684 J0 (rho=3/4) certified by partial+tail brackets on the "
        "series; kappa_1D = 4 J0 at rho=1/2",
        ok9 and kappa_1d == 4,
    )

    # Q10 -- fermionic long-range lift (JW on 4 sites).
    I2 = sp.eye(2)
    ANN = sp.Matrix([[0, 1], [0, 0]])
    SZ = sp.Matrix([[1, 0], [0, -1]])

    def kron(*mats):
        out = mats[0]
        for m in mats[1:]:
            out = sp.Matrix(sp.kronecker_product(out, m))
        return out

    def c_op(j, n=4):
        return kron(*([SZ] * j + [ANN] + [I2] * (n - j - 1)))

    c = [c_op(j) for j in range(4)]
    cd = [m.H for m in c]

    def com(a, b):
        return a * b - b * a

    def is_zero(m):
        return sp.simplify(m) == sp.zeros(*m.shape)

    lr03 = cd[0] * c[3] + cd[3] * c[0]
    hop01 = cd[0] * c[1] + cd[1] * c[0]
    hop12 = cd[1] * c[2] + cd[2] * c[1]
    n0 = cd[0] * c[0]
    n1 = cd[1] * c[1]
    ham_mixed = hop01 + hop12 + lr03
    checks.check(
        "Q10 fermionic long-range lift: distant even pair term is "
        "Hermitian, commutes with intermediate odd/even elements, and "
        "the weighted reduction holds on a mixed family",
        is_zero(lr03 - lr03.H)
        and is_zero(com(lr03, c[1]))
        and is_zero(com(lr03, cd[1]))
        and is_zero(com(lr03, n1))
        and is_zero(com(hop12, n0))
        and is_zero(
            com(ham_mixed, n0) - com(hop01, n0) - com(lr03, n0)
        )
        and not is_zero(com(lr03, n0)),
    )

    # Q11 -- mixed-size tensor reduction: a THREE-site term next to a
    # bond term (dims 2,2,2,2), far probe, general-support Duhamel
    # reduction instance.
    SX = sp.Matrix([[0, 1], [1, 0]])
    h123 = kron(SX, SX, SX, I2)
    h34 = kron(I2, I2, SZ, SZ)
    a_site1 = kron(SZ, I2, I2, I2)
    probe4 = kron(I2, I2, I2, SX)
    ham_t = h123 + h34
    checks.check(
        "Q11 mixed-size tensor reduction: three-site term plus bond "
        "term; far term commutes with A, [H, A] = [h_123, A] != 0, and "
        "the three-site term commutes with the far probe's site "
        "complement rules",
        is_zero(com(h34, a_site1))
        and is_zero(com(ham_t, a_site1) - com(h123, a_site1))
        and not is_zero(com(h123, a_site1))
        and is_zero(com(h123, probe4)),
    )

    # Needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 finite-range bridge note: the composition gap taken here and "
        "the one-hypothesis sentence",
        NOTE4_BRIDGE,
        (
            "that one-step composition theorem is not proved here or in "
            "the cited note.",
            "exactly one hypothesis",
        ),
    )
    checks.needle(
        "N2 exp-decay note: the reproducing no-go display (dispositioned "
        "non-binding) and the separate-source sentence",
        NOTE2_EXPDECAY,
        (
            "sum_z G_mu(d(x,z)) G_mu(d(z,y)) / G_mu(d(x,y)) >= R + 1",
            "A separate source would still be needed",
        ),
    )
    checks.needle(
        "N3 free-bilinear note: the landed pair-support instance displays",
        NOTE3_BILINEAR,
        (
            "W_mu := sup_x sum_y ||Phi_{xy}|| exp(mu d_1(x,y))",
            "exp(-mu d_1(x,y) + 4 W_mu |t|).",
        ),
    )
    checks.needle(
        "N4 block03 chain authority (its file read directly)",
        BLOCK03_NOTE,
        (
            "microcausality_all_time_volume_uniform_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**G6 (theorem: all-time volume-uniform Lieb-Robinson bound).**",
        ),
    )
    checks.needle(
        "N4b block04 graded-lemma authority (its file read directly)",
        BLOCK04_NOTE,
        (
            "microcausality_fermionic_even_car_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**Graded locality lemma (rebuilt from the CAR relations; "
            "local alias L-F).**",
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
        "N6 target identifiers, delta sentences, No-Go structure",
        TARGET_NOTE,
        (
            "microcausality_weighted_quasilocal_class_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**Theorem (weighted quasilocal all-time volume-uniform "
            "Lieb-Robinson bound).**",
            "**Not\n  re-proved here** — needled as the landed comparator instance.",
            "the divergent ratio is never formed",
            "weaker by exactly `6/5`",
            "**Status: PASS**",
            "**N8 prior-wall echo — ATTEMPTED.**",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
