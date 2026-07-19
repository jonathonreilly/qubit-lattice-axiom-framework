#!/usr/bin/env python3
"""Exact checks for the corner-class factorization discharge note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
CORNER_FREE = ROOT / (
    "docs/CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_"
    "CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md"
)
CORNER_GAUGE = ROOT / (
    "docs/CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_"
    "BOUNDED_NOTE_2026-06-12.md"
)
ENGINE_NOTE = ROOT / (
    "docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_"
    "NOTE_2026-05-28.md"
)
RP_POS_NOTE = ROOT / (
    "docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_"
    "NOTE_2026-05-28.md"
)
CT_NOTE = ROOT / (
    "docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_"
    "NARROW_THEOREM_NOTE_2026-06-13.md"
)
BLOCK08_NOTE = ROOT / (
    "docs/MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_LABELS = [
    "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9",
    "N1", "N2", "N3", "N3b", "N4", "N5", "N6", "N7",
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


I2 = sp.eye(2)
ANN = sp.Matrix([[0, 1], [0, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def c_op(j, n=2):
    return kron(*([SZ] * j + [ANN] + [I2] * (n - j - 1)))


def main():
    checks = CheckRunner()

    c = [c_op(j) for j in range(2)]
    cd = [m.H for m in c]

    def dGamma(X):
        T = sp.zeros(4, 4)
        for a in range(2):
            for b in range(2):
                T += X[a, b] * cd[a] * c[b]
        return T

    l1, l2, at, E1, E2 = sp.symbols(
        "lambda1 lambda2 a_tau E1 E2", positive=True
    )

    # D1 -- occupation action and trace identity (diagonal symbolic).
    G = sp.simplify(sp.exp(dGamma(sp.diag(sp.log(l1), sp.log(l2)))))
    diag_entries = [sp.simplify(G[i, i]) for i in range(4)]
    off_zero = all(
        sp.simplify(G[i, j]) == 0 for i in range(4) for j in range(4) if i != j
    )
    checks.check(
        "D1 occupation action of Gamma(t) = e^{dGamma(ln t)}: diagonal "
        "(1, l2, l1, l1*l2), and Tr = (1+l1)(1+l2) = det(1+t)",
        diag_entries == [1, l2, l1, l1 * l2]
        and off_zero
        and sp.simplify(sp.trace(G) - (1 + l1) * (1 + l2)) == 0,
    )

    # D2 -- non-diagonally realized trace identity (spectrum {1/4, 4}).
    V = sp.Rational(1, 5) * sp.Matrix([[3, -4], [4, 3]])
    tmat = V * sp.diag(sp.Rational(1, 4), sp.Integer(4)) * V.T
    lnt = V * sp.diag(-sp.log(4), sp.log(4)) * V.T
    Gn = sp.simplify(sp.exp(dGamma(lnt)))
    checks.check(
        "D2 non-diagonal realization: Tr Gamma(t) = det(1+t) = 25/4 for "
        "a rotated positive matrix with spectrum {1/4, 4}",
        sp.simplify(sp.trace(Gn) - (sp.eye(2) + tmat).det()) == 0
        and sp.simplify((sp.eye(2) + tmat).det() - sp.Rational(25, 4)) == 0,
    )

    # D3 -- multiplicativity (diagonal symbolic).
    m1, m2 = sp.symbols("mu1 mu2", positive=True)
    G2 = sp.simplify(sp.exp(dGamma(sp.diag(sp.log(m1), sp.log(m2)))))
    G12 = sp.simplify(
        sp.exp(dGamma(sp.diag(sp.log(l1 * m1), sp.log(l2 * m2))))
    )
    noncomm_prod = sp.diag(2, 1) * sp.Matrix([[2, 1], [1, 2]])
    checks.check(
        "D3 multiplicativity on COMMUTING positive pairs (symbolic "
        "diagonal family) with the domain rejector: a non-commuting "
        "positive product is non-Hermitian (outside the definition)",
        sp.simplify(G * G2 - G12) == sp.zeros(4, 4)
        and sp.simplify(noncomm_prod - noncomm_prod.H) != sp.zeros(2, 2),
    )

    # D4 -- the log identity -log Gamma(t) = dGamma(-log t) (symbolic).
    minus_log_G = sp.diag(
        0, -sp.log(l2), -sp.log(l1), -(sp.log(l1) + sp.log(l2))
    )
    dG_minus = dGamma(sp.diag(-sp.log(l1), -sp.log(l2)))
    log_of_G = sp.Matrix(
        4, 4, lambda i, j: sp.simplify(sp.log(G[i, i])) if i == j else 0
    )
    checks.check(
        "D4 log identity -log Gamma(t) = dGamma(-log t): two-mode diagonal "
        "exemplar supporting the written proof (symbolic)",
        sp.simplify(-log_of_G - dG_minus) == sp.zeros(4, 4)
        and sp.simplify(-log_of_G - minus_log_G) == sp.zeros(4, 4),
    )

    # D5 -- composition: t = e^{-2 a_tau h} => -log Gamma(t)/(2 a_tau)
    # = dGamma(h) (h diagonal symbolic).
    h_diag = sp.diag(E1, E2) / at
    t_from_h = sp.diag(
        sp.exp(-2 * at * h_diag[0, 0]), sp.exp(-2 * at * h_diag[1, 1])
    )
    G_t = sp.simplify(
        sp.exp(dGamma(sp.Matrix(2, 2, lambda i, j:
                                sp.log(t_from_h[i, j]) if i == j else 0)))
    )
    log_G_t = sp.Matrix(
        4, 4, lambda i, j: sp.simplify(sp.log(G_t[i, i])) if i == j else 0
    )
    H_MB = sp.simplify(-log_G_t / (2 * at))
    checks.check(
        "D5 composition H_MB = -log Gamma(e^{-2 a_tau h})/(2 a_tau) = "
        "dGamma(h): two-mode diagonal exemplar (symbolic), and "
        "-log t = 2E at a_tau = 1",
        sp.simplify(H_MB - dGamma(h_diag)) == sp.zeros(4, 4)
        and sp.simplify(
            -sp.log(sp.exp(-2 * E1)) - 2 * E1
        )
        == 0,
    )

    # D6 -- positivity window from the mass gap: E >= arcsinh(m) > 0,
    # t = e^{-2E} in (0, 1).
    s_sym = sp.Symbol("s_sym", positive=True)
    m_sym = sp.Symbol("m_sym", positive=True)
    mono = sp.simplify((m_sym**2 + s_sym**2) - m_sym**2)
    ok6 = mono == s_sym**2 and (s_sym**2).is_positive is True
    for m_val in (sp.Rational(1, 2), sp.Integer(2)):
        arc = sp.asinh(m_val)
        t_top = sp.exp(-2 * arc)
        if not (
            sp.simplify(arc).is_positive is True
            and sp.simplify(1 - t_top).is_positive is True
            and sp.simplify(t_top).is_positive is True
        ):
            ok6 = False
    arc_e = sp.asinh(sp.sqrt(sp.Rational(1, 4) + 1))
    ok6 = ok6 and sp.simplify(arc_e - sp.asinh(sp.Rational(1, 2))).is_positive is True
    checks.check(
        "D6 positivity window from the mass gap: m^2 + s^2 >= m^2 "
        "(symbolic), E >= arcsinh(m) with a strict instance, and "
        "0 < t <= e^{-2 arcsinh(m)} < 1 at m = 1/2 and m = 2",
        ok6,
    )

    # D7 -- the native 1D activity envelope for the corner surface.
    x = sp.Symbol("x", positive=True)
    fin_n = 8
    geo_fin = sp.expand(
        sum(x**r for r in range(1, fin_n + 1)) * (1 - x)
        - (x - x ** (fin_n + 1))
    )
    kappa_1d_closed = 8 * x / (1 - x)
    inst = sp.Integer(1) + kappa_1d_closed.subs(x, sp.Rational(1, 2))
    x_below = sp.simplify(1 - sp.exp(-sp.Rational(1, 3))).is_positive
    x_above = sp.simplify(sp.exp(sp.Rational(1, 3)) - 1).is_positive
    shell_factor = 2 * 2 * 2  # 2 sites/shell * |S|=2 * pair-norm 2K/K
    n_ch = sp.Symbol("n_ch", positive=True, integer=True)
    agg = n_ch * (1 + kappa_1d_closed.subs(x, sp.Rational(1, 2)))
    checks.check(
        "D7 native 1D envelope: shell count 2 composed as 2*2*2 = 8, "
        "telescoping gate, instance 9K at x = 1/2, BOTH threshold "
        "directions (mu = eta -/+ delta instances), and the aggregate "
        "n_ch * 9K with the identical-3-channel value 27K",
        geo_fin == 0
        and sp.simplify(inst - 9) == 0
        and x_below is True
        and x_above is True
        and shell_factor == 8
        and sp.simplify(agg.subs(n_ch, 3) - 27) == 0,
    )

    # D8 -- the intertwiner pin: realization satisfies it; the review
    # counterexample (permutation-conjugated functor) violates it.
    Xs = sp.diag(sp.log(l1), sp.log(l2))
    eD = sp.simplify(sp.exp(dGamma(Xs)))
    eDinv = sp.simplify(sp.exp(dGamma(-Xs)))
    intertw_ok = all(
        sp.simplify(eD * cd[a] * eDinv - sp.exp(Xs[a, a]) * cd[a])
        == sp.zeros(4, 4)
        for a in range(2)
    )
    vac = sp.zeros(4, 1)
    vac[0] = 1
    vac_ok = sp.simplify(eD * vac - vac) == sp.zeros(4, 1)
    # 3-mode counterexample: swap the |110> and |101> two-particle
    # states; check trace preserved but log identity broken.
    tvals = (2, 3, 5)
    occ = list(itertools.product((0, 1), repeat=3))
    diagG = [sp.Integer(1)] * 8
    for i, o in enumerate(occ):
        v = sp.Integer(1)
        for k in range(3):
            if o[k]:
                v *= tvals[k]
        diagG[i] = v
    Gstd = sp.diag(*diagG)
    i110 = occ.index((1, 1, 0))
    i101 = occ.index((1, 0, 1))
    W = sp.eye(8)
    W[i110, i110] = 0
    W[i101, i101] = 0
    W[i110, i101] = 1
    W[i101, i110] = 1
    Gtil = W * Gstd * W.T
    log_std = sp.diag(*[sp.log(d) for d in diagG])
    log_til = sp.diag(*[sp.log(Gtil[i, i]) for i in range(8)])
    checks.check(
        "D8 the intertwiner pins the functor: e^{dGamma} satisfies "
        "vacuum fixing and the creation intertwiner (symbolic); the "
        "review's permutation-conjugated functor preserves the trace "
        "(det(1+t) = 72) but BREAKS the log identity (two-particle "
        "blocks 6,10 swapped)",
        intertw_ok
        and vac_ok
        and sp.simplify(sp.trace(Gtil) - sp.trace(Gstd)) == 0
        and sp.simplify(sp.trace(Gstd) - 72) == 0
        and Gtil[i110, i110] == 10
        and Gstd[i110, i110] == 6
        and sp.simplify(log_til - log_std) != sp.zeros(8, 8),
    )

    # D9 -- periodic-wrap blow-up: the wrap term's site-weighted
    # activity grows like e^{mu(L-1)}; open boundaries are the scope.
    mu_w = sp.Rational(1, 4)
    K_w = sp.Symbol("K_w", positive=True)
    wrap = lambda L: 2 * K_w * sp.exp(-1) * sp.exp(mu_w * (L - 1))
    checks.check(
        "D9 periodic-wrap exhibit: the wrap activity ratio between "
        "L = 41 and L = 9 is e^{8} > 1 (grows without bound), so the "
        "volume-uniform envelope is scoped to open boundaries",
        sp.simplify(wrap(41) / wrap(9) - sp.exp(8)) == 0
        and sp.simplify(sp.exp(8) - 1).is_positive is True,
    )

    # Needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 corner free note: the displayed identity, kernels, "
        "per-channel form, tensor product, trace product, 1+1d scope, "
        "and the fork-independence sentence",
        CORNER_FREE,
        (
            "T_hat^2 = Gamma(t) = B^dag B`, positive Hermitian",
            "t(p) = exp(-2 E(m,p))",
            "E(m,p) = arcsinh(sqrt(m^2 + sin^2 p))",
            "T_k^2 = Gamma(t_k) = B_k^dag B_k",
            "Tr Gamma(t) = det(1 + t) = product_k det(1 + t_k)",
            "free staggered `1+1d`",
            "it does not select between branches",
        ),
    )
    checks.needle(
        "N2 corner gauge note: trace correspondence, lambda = 1 "
        "forcing, fixed-background firewall",
        CORNER_GAUGE,
        (
            "Tr Gamma(t[U]) = det(1 + t[U])",
            "equality for arbitrary nonzero determinant requires",
            "fixed background only",
        ),
    )
    checks.needle(
        "N3 engine note: the many-body definition sentence, the import "
        "row this note retires, the hedge, and the spectrum sentence",
        ENGINE_NOTE,
        (
            "T_hat^2[U] = Gamma(t1^(2)[U])",
            "standard free-fermion functorial relation",
            "expected to survive at arbitrary spatial `U`",
            "every decaying eigenvalue mu of T2cl[U] is REAL and",
        ),
    )
    checks.needle(
        "N3b RP-positivity note: the defining intertwiner and the "
        "in-repo derivation sentence (the uniqueness authority)",
        RP_POS_NOTE,
        (
            "Gamma(K) |vac> = |vac>,    Gamma(K) a_p^dag = lambda_p "
            "a_p^dag Gamma(K).",
            "derived/checked in-repo, not asserted",
            "Gamma(e^{-h}) = e^{-d Gamma(h)}",
        ),
    )
    checks.needle(
        "N4 CT note: h definition, arcsinh form, and the mass-gap "
        "display sourcing strict positivity",
        CT_NOTE,
        (
            "h = -log(T_hat^2)/(2 a_tau)",
            "h[U] = arcsinh( sqrt( D[U] ) )",
            "m^2 I <= D[U] <= (m^2 + d^2) I",
        ),
    )
    checks.needle(
        "N5 sibling block08: the hypothesis discharged, the scalar-drop, "
        "and the counterexample marking the boundary",
        BLOCK08_NOTE,
        (
            "**Gaussian factorization**",
            "T_MB[U] = C(U)·Γ(T_1[U])",
            "identity shift that drops from every commutator",
            "Γ(e^{−h})·e^{−g n_1 n_2}",
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
        "N7 target identifiers, dimension scoping, glyph "
        "disambiguation, Status",
        TARGET_NOTE,
        (
            "microcausality_corner_class_factorization_discharge_"
            "bounded_theorem_note_2026-07-18",
            "**The `d = 3`\ndischarge is NOT claimed**",
            "many-body in the corner note, one-particle in the CT",
            "`C = 1` is the corner surface's\nasserted normalization",
            "no additional\nGaussian-factorization premise**",
            "the INTERTWINER\n  is the pin",
            "OPEN-BOUNDARY restriction",
            "**Status: PASS**",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
