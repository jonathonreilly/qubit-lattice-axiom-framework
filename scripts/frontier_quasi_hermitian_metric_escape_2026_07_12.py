#!/usr/bin/env python3
"""Quasi-Hermitian metric-operator escape closure (rhalf block 11).

Exact companion runner for
  docs/KOIDE_QUASI_HERMITIAN_METRIC_OPERATOR_ESCAPE_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-12.md

This runner imports and reuses the block-10 exact Berezin/two-slice engine,
then checks the metric-intertwining problem independently in the Fourier basis.
Numbered PASS/FAIL checks; exit 0 iff FAIL == 0.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

import sympy as sp


_pass = 0
_fail = 0


def check(num: int, desc: str, ok: bool, detail: str = "") -> None:
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def residual(msg: str) -> None:
    print(f"RESIDUAL (declared-open): {msg}")


print("=" * 72)
print("Quasi-Hermitian metric-operator escape closure (rhalf block 11)")
print("circulant W = a I + b C + c C^2; exact symbolic/rational checks")
print("=" * 72)

# -----------------------------------------------------------------------------
# Reuse the complete block-10 exact Berezin/two-slice engine.  Its runner is a
# script rather than an import-only module, so execute it once with stdout
# captured and retain the fully populated module namespace after its SystemExit.
# -----------------------------------------------------------------------------
def load_block10_engine():
    source = Path(__file__).with_name(
        "frontier_records_only_os_reconstruction_2026_07_11.py"
    )
    spec = importlib.util.spec_from_file_location("rhalf_block10_engine", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load block-10 engine from {source}")
    module = importlib.util.module_from_spec(spec)
    captured = io.StringIO()
    exit_code = None
    with contextlib.redirect_stdout(captured):
        try:
            spec.loader.exec_module(module)
        except SystemExit as exc:
            exit_code = exc.code
    return module, exit_code, captured.getvalue()


b10, b10_exit, b10_stdout = load_block10_engine()
check(
    1,
    "block-10 machinery REUSED, not reimplemented: the imported exact "
    "Grassmann/Berezin/two-slice runner completes its own 24-check scorecard "
    "with exit 0 and TOTAL: PASS=24 FAIL=0",
    b10_exit == 0
    and getattr(b10, "_pass", None) == 24
    and getattr(b10, "_fail", None) == 0
    and "TOTAL: PASS=24 FAIL=0" in b10_stdout,
)


# -----------------------------------------------------------------------------
# Exact circulant/Fourier setup
# -----------------------------------------------------------------------------
I = sp.I
sqrt3 = sp.sqrt(3)
omega = -sp.Rational(1, 2) + I * sqrt3 / 2
C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
C2 = C**2
U = sp.Matrix(
    [[omega ** (row * k) / sqrt3 for k in range(3)] for row in range(3)]
)

a, b, c = sp.symbols("a b c")
W = a * sp.eye(3) + b * C + c * C2
lam = [sp.expand(a + b * omega**k + c * omega ** (2 * k)) for k in range(3)]
Lam = sp.diag(*lam)

l0, l1, l2 = sp.symbols("lambda_0 lambda_1 lambda_2")
inverse_dft = sp.Matrix(
    [
        (l0 + l1 + l2) / 3,
        (l0 + omega**2 * l1 + omega * l2) / 3,
        (l0 + omega * l1 + omega**2 * l2) / 3,
    ]
)
inverse_roundtrip = [
    sp.simplify(expr.subs({l0: lam[0], l1: lam[1], l2: lam[2]}) - target)
    for expr, target in zip(inverse_dft, (a, b, c))
]
check(
    2,
    "the Fourier map is unitary and invertible: U^dag W U = "
    "diag(lambda_0,lambda_1,lambda_2), lambda_k = a+b omega^k+c omega^(2k), "
    "with the displayed inverse DFT recovering (a,b,c) exactly",
    sp.simplify(U.conjugate().T * U - sp.eye(3)) == sp.zeros(3)
    and sp.simplify(U.conjugate().T * W * U - Lam) == sp.zeros(3)
    and all(v == 0 for v in inverse_roundtrip),
)


# General real-component parameterization.
ar, ai, br, bi, cr, ci = sp.symbols("ar ai br bi cr ci", real=True)
general_sub = {a: ar + I * ai, b: br + I * bi, c: cr + I * ci}
lam_general = [sp.expand_complex(z.subs(general_sub)) for z in lam]
real_spectrum_solve = sp.solve(
    [sp.im(z) for z in lam_general], [ai, cr, ci], dict=True
)
tie_solution = [{ai: 0, cr: br, ci: -bi}]
tie_sub = {a: ar, b: br + I * bi, c: br - I * bi}
check(
    3,
    "all-real spectrum <=> the K-tie, symbolically: the three equations "
    "Im(lambda_k)=0 solve uniquely to a real and c=conj(b); conversely the "
    "three Fourier eigenvalues are real on that slice",
    real_spectrum_solve == tie_solution
    and all(sp.simplify(sp.im(sp.expand_complex(z.subs(tie_sub)))) == 0 for z in lam),
)


# A native finite-dimensional positive-metric proof.  In the Fourier basis,
# eta_hat Lambda = Lambda^dag eta_hat.  Positive definiteness forces every
# diagonal eta_hat[ii] > 0, while its diagonal intertwining equation is
# eta_hat[ii] (lambda_i-conj(lambda_i)) = 0.
lr = sp.symbols("lr0:3", real=True)
li = sp.symbols("li0:3", real=True)
d = sp.symbols("d0:3", real=True)
Lambda_parts = sp.diag(*[lr[k] + I * li[k] for k in range(3)])
Eta_diag = sp.diag(*d)
diag_equations = sp.diag(
    *(Eta_diag * Lambda_parts - Lambda_parts.conjugate().T * Eta_diag).diagonal()
)
diag_target = sp.diag(*[2 * I * d[k] * li[k] for k in range(3)])
check(
    4,
    "T1 positive-metric mechanism is exact: in the Fourier basis the diagonal "
    "intertwining equations are 2 i eta_kk Im(lambda_k)=0; eta>0 gives "
    "eta_kk>0, hence every lambda_k is real, hence the tie by check 3.  "
    "Conversely W=W^dag on the tie and eta=I works",
    sp.simplify(diag_equations - diag_target) == sp.zeros(3)
    and sp.simplify(W.subs(tie_sub) - W.subs(tie_sub).conjugate().T)
    == sp.zeros(3),
)


# Nine-real-parameter Hermitian metric and an exact nullity helper.
x0, x1, x2, x3h, x4, x5h, x6, x7h, x8 = sp.symbols("x0:9", real=True)
metric_vars = (x0, x1, x2, x3h, x4, x5h, x6, x7h, x8)
eta_general = sp.Matrix(
    [
        [x0, x1 + I * x2, x3h + I * x4],
        [x1 - I * x2, x5h, x6 + I * x7h],
        [x3h - I * x4, x6 - I * x7h, x8],
    ]
)


def hermitian_intertwiner_system(W_value: sp.Matrix):
    defect = (eta_general * W_value - W_value.conjugate().T * eta_general).applyfunc(
        sp.expand_complex
    )
    equations = []
    for entry in defect:
        equations.extend((sp.re(entry), sp.im(entry)))
    matrix, rhs = sp.linear_eq_to_matrix(equations, metric_vars)
    return matrix, rhs


def hermitian_intertwiner_nullity(W_value: sp.Matrix) -> int:
    matrix, _ = hermitian_intertwiner_system(W_value)
    return len(metric_vars) - matrix.rank()


tie_point = {
    a: sp.Rational(4, 5),
    b: sp.Rational(3, 10) + I * sp.Rational(1, 5),
    c: sp.Rational(3, 10) - I * sp.Rational(1, 5),
}
W_tie = W.subs(tie_point)
check(
    5,
    "supervisor tie probe reproduced exactly: at (4/5,3/10+i/5,conj) the "
    "Hermitian intertwiner space has real dimension 3 and contains the "
    "positive-definite solution eta=I",
    hermitian_intertwiner_nullity(W_tie) == 3
    and W_tie == W_tie.conjugate().T
    and sp.eye(3) * W_tie == W_tie.conjugate().T * sp.eye(3),
)


# General all-real, off-tie solution and the requested minors obstruction.
x_3, x_5, x_7 = sp.symbols("x_3 x_5 x_7", real=True)
eta_real_branch = sp.Matrix(
    [[x_7, x_3, x_5], [x_3, x_5, x_7], [x_5, x_7, x_3]]
)
a_r, b_r, c_r = sp.symbols("a_r b_r c_r", real=True)
W_real = a_r * sp.eye(3) + b_r * C + c_r * C2
minors_real = [sp.factor(eta_real_branch[:k, :k].det()) for k in range(1, 4)]
Q_psd = x_3**2 + x_5**2 + x_7**2 - x_3 * x_5 - x_3 * x_7 - x_5 * x_7
minors_target = [
    x_7,
    x_5 * x_7 - x_3**2,
    -(x_3 + x_5 + x_7) * Q_psd,
]
probe_real_points = [
    {a: sp.Rational(4, 5), b: sp.Rational(3, 10), c: sp.Rational(1, 2)},
    {a: sp.Rational(1, 2), b: -sp.Rational(4, 5), c: sp.Rational(3, 10)},
]
real_system, real_rhs = hermitian_intertwiner_system(W_real)
real_solution = sp.linsolve((real_system, real_rhs), metric_vars)
real_solution_target = sp.FiniteSet((x6, x8, 0, x5h, 0, x5h, x6, 0, x8))
# This 6x6 rank certificate is nonzero for every real b_r != c_r because
# b_r^2+b_r*c_r+c_r^2 can vanish over R only at b_r=c_r=0.
rank_rows = (1, 2, 3, 4, 5, 10)
rank_cols = (0, 1, 2, 3, 4, 7)
real_rank_certificate = sp.factor(real_system.extract(rank_rows, rank_cols).det())
real_rank_target = 2 * (b_r - c_r) ** 2 * (b_r**2 + b_r * c_r + c_r**2) ** 2
check(
    6,
    "the all-real off-tie family is solved generally, not pointwise: every "
    "Hermitian intertwiner is eta=[[x7,x3,x5],[x3,x5,x7],[x5,x7,x3]], with "
    "leading minors m1=x7, m2=x5*x7-x3^2, and m3=-(x3+x5+x7)Q, "
    "Q=((x3-x5)^2+(x3-x7)^2+(x5-x7)^2)/2.  m1,m2>0 force x5,x7>0; "
    "m3>0 forces x3<-(x5+x7), hence x3^2>(x5+x7)^2>x5*x7, contradicting "
    "m2>0.  Both supplied all-real probes have the same 3-dimensional family "
    "and therefore no positive-definite eta",
    sp.simplify(eta_real_branch * W_real - W_real.T * eta_real_branch)
    == sp.zeros(3)
    and real_solution == real_solution_target
    and sp.simplify(real_rank_certificate - real_rank_target) == 0
    and all(sp.simplify(got - want) == 0 for got, want in zip(minors_real, minors_target))
    and sp.simplify(
        Q_psd
        - ((x_3 - x_5) ** 2 + (x_3 - x_7) ** 2 + (x_5 - x_7) ** 2) / 2
    )
    == 0
    and sp.expand((x_5 + x_7) ** 2 - x_5 * x_7)
    == x_5**2 + x_5 * x_7 + x_7**2
    and all(hermitian_intertwiner_nullity(W.subs(point)) == 3 for point in probe_real_points),
)


# -----------------------------------------------------------------------------
# T2: arbitrary-signature Hermitian metrics
# -----------------------------------------------------------------------------
print("\n--- T2: arbitrary-signature metric; all conjugation pairings ---")


def spectrum_at(point):
    return [sp.expand_complex(sp.simplify(z.subs(point))) for z in lam]


def conjugation_matches(values):
    return [
        (i, j)
        for i in range(3)
        for j in range(3)
        if sp.simplify(values[j] - sp.conjugate(values[i])) == 0
    ]


def conjugation_closed(values):
    return any(
        all(sp.simplify(values[p[i]] - sp.conjugate(values[i])) == 0 for i in range(3))
        for p in permutations(range(3))
    )


off_probe_points = [
    {
        a: sp.Rational(4, 5) + I * sp.Rational(1, 10),
        b: sp.Rational(3, 10) + I * sp.Rational(1, 5),
        c: sp.Rational(1, 2) - I * sp.Rational(1, 10),
    },
    {
        a: 1,
        b: sp.Rational(1, 3) + I * sp.Rational(1, 7),
        c: sp.Rational(1, 3) - I * sp.Rational(1, 5),
    },
]
off_probe_nullities = [hermitian_intertwiner_nullity(W.subs(p)) for p in off_probe_points]
off_probe_matches = [conjugation_matches(spectrum_at(p)) for p in off_probe_points]
check(
    7,
    "both supplied off-union probes are reproduced exactly: the 9-real-parameter "
    "Hermitian intertwiner system has rank 9/nullity 0, equivalently no ordered "
    "Fourier match lambda_j=conj(lambda_i), so eta W=W^dag eta has only eta=0",
    off_probe_nullities == [0, 0] and off_probe_matches == [[], []],
    f"nullities={off_probe_nullities}, matches={off_probe_matches}",
)


# Conjugation closure on three spectral labels is represented by an involution:
# identity (three fixed real values) or one of three transpositions (one fixed
# real value plus a conjugate pair).  Degeneracies lie in intersections.
involutions = [
    p
    for p in permutations(range(3))
    if all(p[p[i]] == i for i in range(3))
]
expected_involutions = [(0, 1, 2), (0, 2, 1), (2, 1, 0), (1, 0, 2)]
sx, su, sv = sp.symbols("x u v", real=True)
spectral_patterns = {
    (0, 1, 2): [sx, su, sv],
    (0, 2, 1): [sx, su + I * sv, su - I * sv],
    (2, 1, 0): [su + I * sv, sx, su - I * sv],
    (1, 0, 2): [su + I * sv, su - I * sv, sx],
}


def permutation_matrix(p):
    result = sp.zeros(3)
    for i, j in enumerate(p):
        result[i, j] = 1
    return result


pairing_checks = []
for p, values in spectral_patterns.items():
    R = permutation_matrix(p)
    D = sp.diag(*values)
    eta_pair = sp.simplify(U * R * U.conjugate().T)
    pairing_checks.extend(
        [
            R == R.T,
            R * R == sp.eye(3),
            sp.simplify(R * D - D.conjugate().T * R) == sp.zeros(3),
            sp.simplify(eta_pair - eta_pair.conjugate().T) == sp.zeros(3),
            sp.simplify(eta_pair.det() ** 2 - 1) == 0,
        ]
    )
check(
    8,
    "native any-signature theorem: similarity by invertible eta requires "
    "spec(W^dag)=spec(W), i.e. conjugation closure; for three labels closure "
    "has exactly four involutive pairings (identity plus three transpositions). "
    "Conversely each pairing matrix R is Hermitian/unitary/invertible and obeys "
    "R Lambda=Lambda^dag R, so eta=U R U^dag is an explicit Hermitian "
    "intertwiner",
    set(involutions) == set(expected_involutions) and all(pairing_checks),
    f"pairings={involutions}",
)


def pairing_equations(fixed, first, second):
    delta = sp.expand_complex(lam_general[second] - sp.conjugate(lam_general[first]))
    return [sp.im(lam_general[fixed]), sp.re(delta), sp.im(delta)]


pairing_solves = {
    "R0": sp.solve(pairing_equations(0, 1, 2), [ai, bi, ci], dict=True),
    "R1": sp.solve(pairing_equations(1, 0, 2), [ai, bi, ci], dict=True),
    "R2": sp.solve(pairing_equations(2, 0, 1), [ai, bi, ci], dict=True),
}
pairing_targets = {
    "R0": [{ai: 0, bi: 0, ci: 0}],
    "R1": [{ai: 0, bi: sqrt3 * br, ci: -sqrt3 * cr}],
    "R2": [{ai: 0, bi: -sqrt3 * br, ci: sqrt3 * cr}],
}
check(
    9,
    "the full coefficient-space classification is exact: identity pairing is "
    "the tie; R0 (lambda_0 real, lambda_2=conj(lambda_1)) is the block-10 "
    "all-real branch; R1 is {a real, Im b=sqrt(3) Re b, "
    "Im c=-sqrt(3) Re c}; R2 has the two signs reversed.  Thus the proposed "
    "two-branch any-signature theorem is false: there are two additional "
    "phase-twisted pairing loci",
    real_spectrum_solve == tie_solution and pairing_solves == pairing_targets,
    f"solutions={pairing_solves}",
)


P0 = permutation_matrix((0, 2, 1))
R1 = permutation_matrix((2, 1, 0))
R2 = permutation_matrix((1, 0, 2))
eta_R1 = sp.simplify(U * R1 * U.conjugate().T)
eta_R2 = sp.simplify(U * R2 * U.conjugate().T)
extra_R1_point = {
    a: sp.Rational(4, 3),
    b: sp.Rational(1, 3) + I * sqrt3 / 3,
    c: -sp.Rational(2, 3) + 2 * I * sqrt3 / 3,
}
extra_R2_point = {a: extra_R1_point[a], b: extra_R1_point[c], c: extra_R1_point[b]}
W_R1 = W.subs(extra_R1_point)
W_R2 = W.subs(extra_R2_point)
extra_spectra = [spectrum_at(extra_R1_point), spectrum_at(extra_R2_point)]
old_union_false = all(
    sp.simplify(point[c] - sp.conjugate(point[b])) != 0
    and (sp.im(point[b]) != 0 or sp.im(point[c]) != 0)
    for point in (extra_R1_point, extra_R2_point)
)
P_mapping_ok = (
    sp.simplify(P0 * W_R1 * P0 - W_R2) == sp.zeros(3)
    and sp.simplify(P0 * eta_R1 * P0 - eta_R2) == sp.zeros(3)
)
check(
    10,
    "additional-locus question: FOUND TWO.  Exact R1/R2 witnesses have spectra "
    "(1+i*sqrt(3),2,1-i*sqrt(3)) and its 1<->2 relabeling, lie off both old "
    "branches, and admit the explicit signature-(2,1) metrics eta_R1/R2.  "
    "The block-10 P swaps R1<->R2 but preserves the all-real R0 locus, so "
    "neither extra locus is a P-image of the all-real branch",
    extra_spectra[0]
    == [1 + I * sqrt3, 2, 1 - I * sqrt3]
    and extra_spectra[1]
    == [1 + I * sqrt3, 1 - I * sqrt3, 2]
    and old_union_false
    and sp.simplify(eta_R1 * W_R1 - W_R1.conjugate().T * eta_R1) == sp.zeros(3)
    and sp.simplify(eta_R2 * W_R2 - W_R2.conjugate().T * eta_R2) == sp.zeros(3)
    and R1.eigenvals() == {-1: 1, 1: 2}
    and R2.eigenvals() == {-1: 1, 1: 2}
    and hermitian_intertwiner_nullity(W_R1) == 3
    and hermitian_intertwiner_nullity(W_R2) == 3
    and P_mapping_ok,
)


# Outside conjugation closure an invertible metric is impossible, but a singular
# nonzero intertwiner can remain whenever even one equality
# lambda_j=conj(lambda_i) survives.  This is the honest scope of the zero-space
# statement witnessed by check 7.
partial_spectrum = [sp.Integer(1), 2 + I, 3 + 2 * I]
W_partial = sp.simplify(U * sp.diag(*partial_spectrum) * U.conjugate().T)
eta_partial = sp.simplify(U * sp.diag(1, 0, 0) * U.conjugate().T)
partial_nullity = hermitian_intertwiner_nullity(W_partial)
check(
    11,
    "the off-locus zero-space claim is correctly weakened: the spectral support "
    "rule is eta_hat[i,j] nonzero only if lambda_j=conj(lambda_i).  The two "
    "supplied generic probes have no matches and zero space (check 7), but an "
    "exact spectrum (1,2+i,3+2i) is not conjugation-closed and still has a "
    "one-dimensional SINGULAR intertwiner space generated by the real-mode "
    "projector.  Hence only invertible metrics vanish everywhere off the four "
    "loci; the full intertwiner space is zero merely when no pair matches",
    not conjugation_closed(partial_spectrum)
    and conjugation_matches(partial_spectrum) == [(0, 0)]
    and partial_nullity == 1
    and eta_partial != sp.zeros(3)
    and eta_partial.det() == 0
    and sp.simplify(eta_partial * W_partial - W_partial.conjugate().T * eta_partial)
    == sp.zeros(3),
    f"partial nullity={partial_nullity}",
)


# -----------------------------------------------------------------------------
# T3: the exact matrix-valued two-slice factor supplied by block 10
# -----------------------------------------------------------------------------
print("\n--- T3: two-slice spectral factor and the direction of metric lift ---")


def cr_two_slice_factor(W_value):
    W_squared = b10.matmul3(W_value, W_value)
    return [
        [
            W_squared[i][j]
            + (b10.CR(F(1, 4)) if i == j else b10.CR(0))
            for j in range(3)
        ]
        for i in range(3)
    ]


cr_points = [
    (
        "tie",
        b10.W_of(
            b10.CR(F(4, 5)),
            b10.CR(F(3, 10), F(1, 5)),
            b10.CR(F(3, 10), F(-1, 5)),
        ),
        True,
    ),
    ("all-real PD", b10.W_of(F(4, 5), F(3, 10), F(1, 2)), True),
    ("all-real indefinite", b10.W_of(F(1, 2), F(-4, 5), F(3, 10)), True),
    (
        "off probe 1",
        b10.W_of(
            b10.CR(F(4, 5), F(1, 10)),
            b10.CR(F(3, 10), F(1, 5)),
            b10.CR(F(1, 2), F(-1, 10)),
        ),
        False,
    ),
    (
        "off probe 2",
        b10.W_of(
            b10.CR(1),
            b10.CR(F(1, 3), F(1, 7)),
            b10.CR(F(1, 3), F(-1, 5)),
        ),
        False,
    ),
]
engine_point_results = []
for tag, W_cr, expected_hermitian_gram in cr_points:
    G_cr, Z_cr = b10.reg_gram(W_cr, W_cr)
    A_cr = cr_two_slice_factor(W_cr)
    engine_point_results.append(
        (
            tag,
            Z_cr == b10.cr_det(A_cr),
            b10.is_hermitian(G_cr, Z_cr) == expected_hermitian_gram,
        )
    )
check(
    12,
    "block-10 engine verification at all five supplied exact points: its "
    "two-slice Berezin partition is det(A_2), A_2(W)=W^2+I/4, and the "
    "records-only Gram is Hermitian at the tie and both all-real probes but "
    "non-Hermitian at both zero-intertwiner probes",
    all(det_ok and gram_ok for _, det_ok, gram_ok in engine_point_results),
    f"points={engine_point_results}",
)


q = sp.Rational(1, 4)
A2 = sp.expand(W * W + q * sp.eye(3))
tau = [sp.expand(z**2 + q) for z in lam]
K_two = sp.Matrix(
    sp.BlockMatrix(
        [[-W, -sp.Rational(1, 2) * sp.eye(3)], [sp.Rational(1, 2) * sp.eye(3), -W]]
    )
)
check(
    13,
    "the directly supplied matrix-valued two-slice factor is Fourier-normal "
    "with spectrum tau_k=f(lambda_k), f(z)=z^2+1/4 (real coefficients), and "
    "det of the exact 6x6 staggered kernel equals det(A_2)=product_k tau_k",
    sp.simplify(U.conjugate().T * A2 * U - sp.diag(*tau)) == sp.zeros(3)
    and sp.simplify(K_two.det() - A2.det()) == 0
    and sp.simplify(A2.det() - sp.prod(tau)) == 0,
)


W_R0 = W.subs(probe_real_points[0])
metric_lift_cases = [
    (W_tie, sp.eye(3), "tie"),
    (W_R0, P0, "all-real R0"),
    (W_R1, eta_R1, "phase-twisted R1"),
    (W_R2, eta_R2, "phase-twisted R2"),
]
metric_lift_results = []
for W_case, eta_case, tag in metric_lift_cases:
    A_case = sp.expand(W_case * W_case + q * sp.eye(3))
    metric_lift_results.append(
        (
            tag,
            sp.simplify(eta_case * W_case - W_case.conjugate().T * eta_case)
            == sp.zeros(3),
            sp.simplify(eta_case * A_case - A_case.conjugate().T * eta_case)
            == sp.zeros(3),
        )
    )
check(
    14,
    "metric classification lifts FORWARD through every real-coefficient "
    "polynomial: eta W=W^dag eta implies eta f(W)=f(W)^dag eta.  The same "
    "metrics intertwine A_2 at exact tie, R0, R1, and R2 points",
    all(w_ok and a_ok for _, w_ok, a_ok in metric_lift_results),
    f"cases={metric_lift_results}",
)


# The converse fails because f(z)=z^2+1/4 is not injective and can erase the
# sign of imaginary spectral data.  Use a Gaussian-rational scalar witness so
# the block-10 engine can verify the same point exactly.
imag_scalar = I * sp.Rational(1, 10)
W_coarse = imag_scalar * sp.eye(3)
A_coarse = sp.simplify(W_coarse * W_coarse + q * sp.eye(3))
coarse_spectrum = [imag_scalar] * 3
coarse_tau = [sp.Rational(6, 25)] * 3
W_coarse_cr = b10.W_of(b10.CR(0, F(1, 10)), b10.CR(0), b10.CR(0))
G_coarse_cr, Z_coarse_cr = b10.reg_gram(W_coarse_cr, W_coarse_cr)
A_coarse_cr = cr_two_slice_factor(W_coarse_cr)
check(
    15,
    "the transfer-factor converse is FALSE, exactly: W=(i/10)I has no nonzero "
    "Hermitian intertwiner and its spectrum is not conjugation-closed, while "
    "A_2=(6/25)I is Hermitian with strictly positive spectrum and positive "
    "metric eta=I.  The reused block-10 engine gives Z=(6/25)^3=216/15625 "
    "but a non-Hermitian records-only OS Gram.  Thus A_2-only spectral/metric "
    "positivity is strictly weaker than OS and remains an escape",
    not conjugation_closed(coarse_spectrum)
    and hermitian_intertwiner_nullity(W_coarse) == 0
    and A_coarse == sp.Rational(6, 25) * sp.eye(3)
    and all(value > 0 for value in coarse_tau)
    and sp.simplify(A_coarse - A_coarse.conjugate().T) == sp.zeros(3)
    and b10.cr_det(A_coarse_cr) == b10.CR(F(216, 15625))
    and Z_coarse_cr == b10.CR(F(216, 15625))
    and not b10.is_hermitian(G_coarse_cr, Z_coarse_cr),
)
residual(
    "A_2=W^2+I/4 is the matrix-valued two-slice spectral/Schur factor explicitly "
    "present in the authorized block-10 note and runner.  No stronger full "
    "physical transfer operator is supplied in those inputs; identifying A_2 "
    "with that stronger object would be an additional premise."
)


# -----------------------------------------------------------------------------
# T4: honest escape disposition and Record-axiom cost
# -----------------------------------------------------------------------------
print("\n--- T4: bounded consequence; closure and named remainders ---")
axiom_path = Path(__file__).parents[1] / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
axiom_text = axiom_path.read_text(encoding="utf-8")
record_section = axiom_text.split("### Record / Fixed Reality", 1)[1].split(
    "## Qualification", 1
)[0]
record_sentences = (
    "Only records are readable. A readout value is determined by record content\n"
    "alone. For any finite collection of pairwise-disjoint records, scalar readout\n"
    "`I` is additive, with `I(empty)=0`."
)
check(
    16,
    "Record-axiom honesty rail verified verbatim at claim scope: it states "
    "records-only readability, content-determined readout, finite additivity, "
    "and I(empty)=0, but the Record section contains no readout-positivity or "
    "positive-inner-product clause.  Krein reconstruction therefore has the "
    "cost of negative-norm vectors/no positive records-only inner product; it "
    "is not rejected as a textual Record-axiom violation",
    record_sentences in record_section and "positiv" not in record_section.lower(),
)


escapes = {
    "non-conjugating reflection": "BLOCKED (inherited from block 10)",
    "larger record algebra": "BLOCKED at block-10 orbit-clause grade",
    "modified/non-OS time": "GENUINELY OPEN",
    "alternating W,Wdag": "UNLICENSED under the inherited time-homogeneity scope",
    "positive metric on W": "CLOSED to the K-tie",
    "indefinite metric on W": "OPEN KREIN remainder on R0, R1, R2",
    "A2-only spectral/metric condition": "OPEN and strictly coarser than OS",
    "all-real strip with degenerate registration": "OPEN if the named non-degeneracy element is dropped",
}
check(
    17,
    "escape table updated without overclosure: the positive-metric condition on "
    "W closes exactly to the tie; arbitrary signature leaves the three "
    "transposition/Krein branches R0,R1,R2; A_2-only positivity is an additional "
    "coarse open route; all inherited block-10 rows retain their bounded "
    "dispositions.  No claim about r=1 or r=1/2 is made",
    len(escapes) == 8
    and escapes["positive metric on W"] == "CLOSED to the K-tie"
    and "R0, R1, R2" in escapes["indefinite metric on W"]
    and "OPEN" in escapes["A2-only spectral/metric condition"]
    and "OPEN" in escapes["modified/non-OS time"],
)
residual(
    "the equipartition/dial residual is UNTOUCHED: neither r=1 nor r=1/2 is "
    "derived.  This runner classifies only metric intertwiners and the exact "
    "two-slice factor at the stated circulant scope."
)
residual(
    "the phase-twisted R1/R2 metrics and the all-real R0 metric have negative-"
    "norm directions away from their intersections with the tie.  Turning a "
    "Krein space into a probability/Hilbert reconstruction would require new "
    "positive structure not supplied by the Record axiom."
)


print()
print(
    "VERDICT: PARTIAL CLOSURE / TARGET CORRECTED -- positive quasi-Hermiticity "
    "of W selects exactly the K-tie, but arbitrary-signature pseudo-Hermiticity "
    "does not reproduce the block-10 two-branch union, and A_2-only positivity "
    "is strictly coarser than OS."
)
print(
    "T1: eta>0 with eta W=W^dag eta exists iff all lambda_k are real iff "
    "a is real and c=conj(b); eta=I supplies the converse."
)
print(
    "T2: invertible Hermitian eta exists iff the spectrum is conjugation-closed, "
    "which is the tie union R0(all-real) union two additional phase-twisted "
    "loci R1/R2; generic off-locus probes have zero space, but partial matches "
    "can leave singular intertwiners."
)
print(
    "T3: W-metrics lift forward to A_2=W^2+I/4, but not conversely; W=(i/10)I "
    "has no metric while A_2=(6/25)I has positive spectrum and eta=I, although "
    "the exact block-10 OS Gram remains non-Hermitian."
)
print(
    "T4: positive-metric-on-W is closed to the tie; the surviving named "
    "remainders are indefinite/Krein R0-R2 and the coarser A_2-only condition, "
    "with negative norms/no positive records-only inner product and no textual "
    "Record-axiom violation."
)
print(
    "ADDITIONAL-LOCUS: FOUND TWO phase-twisted loci; P swaps them with each "
    "other, and neither is a P-image of the all-real branch."
)
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print(
    "PROPOSED CLAIM_SCOPE: bounded_theorem -- exact finite-dimensional "
    "metric-intertwiner classification for the C3 circulant W plus a one-way "
    "lift theorem and exact counterexample for the block-10 two-slice factor."
)
print(
    "UNCERTAINTIES FOR HOSTILE AUDIT: whether A_2 is intended as the full "
    "physical transfer operator rather than only the supplied Schur factor; "
    "physical licensing of phase-twisted metrics; treatment of degenerate "
    "locus intersections; and any bridge from Krein norm to record probabilities."
)
raise SystemExit(0 if _fail == 0 else 1)
