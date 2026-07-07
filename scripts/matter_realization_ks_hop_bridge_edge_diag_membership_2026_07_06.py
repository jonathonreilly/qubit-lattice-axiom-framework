#!/usr/bin/env python3
"""Exact KS-HOP-BRIDGE EDGE-DIAG membership check."""

from __future__ import annotations

import ast
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def z(re=0, im=0):
    return (Fraction(re), Fraction(im))


ZERO = z()
ONE = z(1)
NEG_ONE = z(-1)
I = z(0, 1)
NEG_I = z(0, -1)


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cneg(a):
    return (-a[0], -a[1])


def csub(a, b):
    return cadd(a, cneg(b))


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


def cscale(a, q):
    return (a[0] * q, a[1] * q)


def zero_matrix(rows, cols):
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def eye(n):
    out = zero_matrix(n, n)
    for i in range(n):
        out[i][i] = ONE
    return out


def mat_add(*mats):
    rows = len(mats[0])
    cols = len(mats[0][0])
    out = zero_matrix(rows, cols)
    for mat in mats:
        for i in range(rows):
            for j in range(cols):
                out[i][j] = cadd(out[i][j], mat[i][j])
    return out


def mat_neg(mat):
    return [[cneg(cell) for cell in row] for row in mat]


def mat_sub(a, b):
    return mat_add(a, mat_neg(b))


def mat_scalar(mat, scalar):
    return [[cmul(scalar, cell) for cell in row] for row in mat]


def mat_mul(a, b):
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    out = zero_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            total = ZERO
            for k in range(inner):
                total = cadd(total, cmul(a[i][k], b[k][j]))
            out[i][j] = total
    return out


def adjoint(mat):
    rows = len(mat)
    cols = len(mat[0])
    out = zero_matrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            out[j][i] = cconj(mat[i][j])
    return out


def kron(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    out = zero_matrix(rows_a * rows_b, cols_a * cols_b)
    for ia in range(rows_a):
        for ja in range(cols_a):
            for ib in range(rows_b):
                for jb in range(cols_b):
                    out[ia * rows_b + ib][ja * cols_b + jb] = cmul(
                        a[ia][ja], b[ib][jb]
                    )
    return out


def mat_eq(a, b):
    return a == b


def commutator(a, b):
    return mat_sub(mat_mul(a, b), mat_mul(b, a))


def is_zero(mat):
    return all(cell == ZERO for row in mat for cell in row)


def swap_matrix_two_qubits():
    out = zero_matrix(4, 4)
    for a, b in product(range(2), repeat=2):
        src = 2 * a + b
        dst = 2 * b + a
        out[dst][src] = ONE
    return out


I2 = eye(2)
SIGMA_1 = [[ZERO, ONE], [ONE, ZERO]]
SIGMA_2 = [[ZERO, NEG_I], [I, ZERO]]
SIGMA_3 = [[ONE, ZERO], [ZERO, NEG_ONE]]
SIGMA_PLUS = [[ZERO, ONE], [ZERO, ZERO]]
SIGMA_MINUS = [[ZERO, ZERO], [ONE, ZERO]]
S = swap_matrix_two_qubits()
PAULI = {1: SIGMA_1, 2: SIGMA_2, 3: SIGMA_3}


def mat_pow_pauli(mat, n):
    return mat if n % 2 else I2


def t_frame(x):
    out = I2
    for axis in (1, 2, 3):
        out = mat_mul(out, mat_pow_pauli(PAULI[axis], x[axis - 1]))
    return out


def eta(mu, x):
    if mu == 1:
        return 1
    if mu == 2:
        return -1 if x[0] % 2 else 1
    if mu == 3:
        return -1 if (x[0] + x[1]) % 2 else 1
    raise ValueError(mu)


def label_matrix(mat):
    h0 = mat_add(kron(SIGMA_PLUS, SIGMA_MINUS), kron(SIGMA_MINUS, SIGMA_PLUS))
    pair = mat_add(kron(SIGMA_PLUS, SIGMA_PLUS), kron(SIGMA_MINUS, SIGMA_MINUS))
    labels = [
        ("h0", h0),
        ("-h0", mat_neg(h0)),
        ("pair_same+", pair),
        ("pair_same-", mat_neg(pair)),
    ]
    for label, candidate in labels:
        if mat_eq(mat, candidate):
            return label
    return "unclassified"


def edge_diag_member(mat):
    return is_zero(commutator(mat, S))


def u(text):
    return text.encode("ascii").decode("unicode_escape")


SOURCE_QUOTES = {
    "docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md": [
        u(
            r"Under P-KIN the kinetic operator is `D = \u03a3_\u03bc "
            r"\u03b3_\u03bc \u2297 \u2202_\u03bc` with `\u2202_\u03bc` the\n"
            r"symmetric lattice difference. P-SD supplies the site-local unitary\n"
            r"scalarization map `T(x)` per site, `\u03c7(x) := T(x) "
            r"\u03c8(x)`, with the\n**scalarization condition**"
        ),
        u(
            r"The canonical Kawamoto-Smit phases\n\n```\n"
            r"\u03b7^0_1(x) = 1,  \u03b7^0_2(x) = (\u22121)^{x_1},  "
            r"\u03b7^0_3(x) = (\u22121)^{x_1+x_2}        (6)\n```\n\n"
            r"satisfy (8) (for `\u03bc < \u03bd`, shifting by `\u03bc` flips "
            r"`\u03b7^0_\u03bd` while shifting"
        ),
        u(
            r"is **exactly one** local gauge class, the class of the Kawamoto-Smit\n"
            r"representative `\u03b7^0` of (6); a canonical solution of (4) is\n"
            r"`T(x) = \u03b3_1^{x_1} \u03b3_2^{x_2} "
            r"\u03b3_3^{x_3}` (on the Pauli realization,\n"
            r"`T(x) = \u03c3_1^{x_1} \u03c3_2^{x_2} "
            r"\u03c3_3^{x_3}`). [Lemma 4]\n\n"
            r"Hence the staggered kinetic operator\n\n```\n"
            r"D_staggered = (1/2) \u03a3_{x, \u03bc} \u03b7_\u03bc(x) "
            r"\xb7 (\u03c7\u0304_{x+\u03bc\u0302} \u03c7_x \u2212 "
            r"\u03c7\u0304_x \u03c7_{x+\u03bc\u0302})\n```"
        ),
    ],
    "docs/STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md": [
        u(
            r"Grassmann candidate (G) exactly; within the\n"
            r"declared two-candidate canonical-pair surface, (G) is the unique\n"
            r"surviving matter-generator measure, and it carries the Berezin\n"
            r"finite-determinant partition readout. This is collapse **within the\n"
            r"two-candidate surface only**: it is NOT a statistics-forcing "
            r"theorem \u2014\n"
            r"the hard-core-boson frame ties with (G) on every readout checked here,\n"
            r"and the statistics-selection input (S2/FS) remains open (\xa78)."
        ),
        u(
            r"  on the Berezin determinant identity. Per-site state space: the\n"
            r"  Berezin function space `F_x := \u039b[\u03c7\u0304_x] = "
            r"\u2102\xb71 \u2295 \u2102\xb7\u03c7\u0304_x` (complex\n"
            r"  dimension `2` by nilpotency `\u03c7\u0304_x\xb2 = 0`), carrying the\n"
            r"  multiplication operator `c\u0304_x := (\u03c7\u0304_x \xb7)` and the "
            r"Berezin\n"
            r"  derivative `c_x := \u2202/\u2202\u03c7\u0304_x` (the operation of the "
            r"per-site integral\n"
            r"  `(B2)`). On `F_x` these satisfy `c_x\xb2 = c\u0304_x\xb2 = 0` and\n"
            r"  `{c_x, c\u0304_x} = 1` (derived in \xa75.2), so `F_x` is the "
            r"two-state\n"
            r"  raising/lowering module with vacuum `|0\u27e9_x := 1` and "
            r"one-particle"
        ),
        u(
            r"**Raising/lowering structure (derived, not assumed).** Two operators\n"
            r"act on `F_x`: the multiplication operator `c\u0304_x := "
            r"(\u03c7\u0304_x \xb7)` and the\n"
            r"Berezin derivative `c_x := \u2202/\u2202\u03c7\u0304_x`, defined by "
            r"`\u2202(1) = 0`,\n"
            r"`\u2202(\u03c7\u0304_x) = 1` \u2014 the same operation as the per-site "
            r"Berezin integral\n"
            r"`(B2)`. On the basis `(1, \u03c7\u0304_x)`:\n\n```text\n"
            r"c\u0304_x : 1 \u21a6 \u03c7\u0304_x,   \u03c7\u0304_x \u21a6 "
            r"\u03c7\u0304_x\xb2 = 0    (raising),\n"
            r"c_x  : 1 \u21a6 0,     \u03c7\u0304_x \u21a6 1            (lowering)."
        ),
        u(
            r"Direct evaluation on the basis gives `c_x\xb2 = c\u0304_x\xb2 = 0` "
            r"and the\ncanonical anticommutation relation **as operators on `F_x`**:\n\n"
            r"```text\n{c_x, c\u0304_x}(1)    = \u2202(\u03c7\u0304_x\xb71) + "
            r"\u03c7\u0304_x\xb7\u2202(1)    = 1 + 0    = 1\xb71,\n"
            r"{c_x, c\u0304_x}(\u03c7\u0304_x) = \u2202(\u03c7\u0304_x\xb2)  + "
            r"\u03c7\u0304_x\xb7\u2202(\u03c7\u0304_x) = 0 + \u03c7\u0304_x = "
            r"1\xb7\u03c7\u0304_x,\n```\n\n"
            r"so `{c_x, c\u0304_x} = 1` on `F_x`. This is the graded Leibniz rule "
            r"of the\nexterior calculus \u2014 a **derived** property of the\n"
            r"multiplication/derivative pair, not an additional premise on the"
        ),
    ],
    (
        "docs/"
        "MATTER_REALIZATION_ARENA_SPLIT_PRESERVATION_UNDER_AXIS_COUPLED_FRAMES_"
        "BOUNDED_THEOREM_NOTE_2026-07-06.md"
    ): [
        u(
            r"Definition (EDGE-DIAG, precise): an edge operator `O` on "
            r"`C^2 tensor C^2`\n"
            r"is in the EDGE-DIAG class iff `[O, S] = 0`. Split preservation for "
            r"this\nclass is then exact and immediate: commuting with `S` is "
            r"equivalent to\npreserving both `S`-eigenspaces, i.e. being block "
            r"diagonal with respect to\n`P_sym + P_anti`."
        ),
        u(
            r"What is PROVEN here about the KS structure: the relative frame "
            r"transport is\nin class -- `[S'_mu, S] = 0` for all three directions, "
            r"and every diagonal\nlift `g tensor g` is in class (T1). What is NOT "
            r"proven here: that the\nbonded-pair edge operator induced by the "
            r"actual KS hopping term lies in\nEDGE-DIAG. That step is the named "
            r"open bridge KS-HOP-BRIDGE: deriving, from\nthe retained KS note's "
            r"scalarization structure, the explicit bonded-pair\noperator the "
            r"hopping induces on `C^2 tensor C^2` and checking its membership."
        ),
    ],
}


def text_audits():
    checks = []
    for rel_path, quotes in SOURCE_QUOTES.items():
        text = (ROOT / rel_path).read_text()
        for quote in quotes:
            checks.append((rel_path, quote in text))
    return checks


def ast_self_scan():
    source = Path(__file__).read_text()
    source.encode("ascii")
    tree = ast.parse(source)
    banned_imports = {"numpy", "sympy", "cmath", "random"}
    banned_calls = {"float", "complex", "eval", "exec"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in banned_imports:
                    return False, f"banned import {alias.name}"
        if isinstance(node, ast.ImportFrom) and node.module:
            root = node.module.split(".")[0]
            if root in banned_imports:
                return False, f"banned import {node.module}"
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in banned_calls:
                return False, f"banned call {node.func.id}"
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            return False, "non-exact numeric literal"
    return True, "ascii_ast_exact_arithmetic_scan"


def conjugate(unitary, operator):
    return mat_mul(mat_mul(unitary, operator), adjoint(unitary))


def main():
    checks = []

    h0 = mat_add(kron(SIGMA_PLUS, SIGMA_MINUS), kron(SIGMA_MINUS, SIGMA_PLUS))
    h_left_term = kron(mat_mul(SIGMA_PLUS, SIGMA_3), SIGMA_MINUS)
    h_jw_left = mat_add(h_left_term, adjoint(h_left_term))
    h_right_term = kron(SIGMA_PLUS, mat_mul(SIGMA_3, SIGMA_MINUS))
    h_jw_right = mat_add(h_right_term, adjoint(h_right_term))
    # Antisymmetrized lattice-difference combinations (panel-required): the
    # retained KS edge is quoted as an antisymmetric difference; check the
    # minus combinations exactly alongside the plus ones.
    a_term = kron(SIGMA_PLUS, SIGMA_MINUS)
    h_minus = mat_sub(a_term, adjoint(a_term))
    h_left_minus = mat_sub(h_left_term, adjoint(h_left_term))
    h_right_minus = mat_sub(h_right_term, adjoint(h_right_term))
    candidates = {
        "h0": h0,
        "hJW_left": h_jw_left,
        "hJW_right": h_jw_right,
        "h0_minus": h_minus,
        "hJW_left_minus": h_left_minus,
        "hJW_right_minus": h_right_minus,
    }
    # Exact anticommutation structure of the minus combination: S h S = -h,
    # so h maps Sym into Anti and Anti into Sym (an exact intertwiner).
    checks_pre = []
    checks_pre.append((
        "minus_combination_anticommutes_with_swap",
        mat_eq(mat_mul(mat_mul(S, h_minus), S), mat_neg(h_minus)),
    ))
    p_sym = mat_scalar(mat_add(eye(4), S), (Fraction(1, 2), Fraction(0)))
    p_anti = mat_scalar(mat_sub(eye(4), S), (Fraction(1, 2), Fraction(0)))
    checks_pre.append((
        "minus_combination_intertwines_sym_anti",
        mat_eq(mat_mul(mat_mul(p_anti, h_minus), p_sym),
               mat_mul(h_minus, p_sym))
        and mat_eq(mat_mul(mat_mul(p_sym, h_minus), p_anti),
                   mat_mul(h_minus, p_anti)),
    ))

    checks.extend(checks_pre)
    checks.append(("swap_square", mat_eq(mat_mul(S, S), eye(4))))
    checks.append(
        ("sigma_plus_sigma_z", mat_eq(mat_mul(SIGMA_PLUS, SIGMA_3), mat_neg(SIGMA_PLUS)))
    )
    checks.append(
        ("sigma_z_sigma_minus", mat_eq(mat_mul(SIGMA_3, SIGMA_MINUS), mat_neg(SIGMA_MINUS)))
    )

    for a, b in product(range(2), repeat=2):
        for c, d in product(range(2), repeat=2):
            e_ab = zero_matrix(2, 2)
            e_cd = zero_matrix(2, 2)
            e_ab[a][b] = ONE
            e_cd[c][d] = ONE
            lhs = mat_mul(mat_mul(S, kron(e_ab, e_cd)), S)
            rhs = kron(e_cd, e_ab)
            checks.append((f"swap_identity_{a}{b}_{c}{d}", mat_eq(lhs, rhs)))

    t1_rows = []
    for name, operator in candidates.items():
        label = label_matrix(operator)
        in_class = edge_diag_member(operator)
        swap_label = label_matrix(mat_mul(mat_mul(S, operator), S))
        expected_membership_t1 = {
            "h0": True, "hJW_left": True, "hJW_right": True,
            "h0_minus": False, "hJW_left_minus": False, "hJW_right_minus": False,
        }
        checks.append((
            f"t1_{name}_edge_diag",
            in_class == expected_membership_t1[name],
        ))
        checks.append((f"t1_{name}_swap_label", label == swap_label))
        t1_rows.append((name, label, in_class))

    expected_t1 = {"h0": "h0", "hJW_left": "-h0", "hJW_right": "-h0"}
    for name, expected in expected_t1.items():
        checks.append((f"t1_{name}_expected_label", label_matrix(candidates[name]) == expected))

    hks_rows = []
    for name, operator in candidates.items():
        for mu in (1, 2, 3):
            labels = set()
            verdicts = set()
            rel_ok = True
            for x in product((0, 1), repeat=3):
                y = tuple(x[i] + (1 if i == mu - 1 else 0) for i in range(3))
                tx = t_frame(x)
                ty = t_frame(y)
                rel = mat_scalar(mat_mul(PAULI[mu], tx), z(eta(mu, x)))
                rel_ok = rel_ok and mat_eq(ty, rel)
                unitary = kron(tx, ty)
                dressed = conjugate(unitary, operator)
                labels.add(label_matrix(dressed))
                verdicts.add(edge_diag_member(dressed))
            checks.append((f"hks_{name}_mu{mu}_relative_frame", rel_ok))
            checks.append((f"hks_{name}_mu{mu}_single_label", len(labels) == 1))
            # Expected membership map (computed structure): plus-forms are IN
            # everywhere; minus-forms are IN under transverse twists (mu=1,2)
            # and OUT under the ladder-axis-aligned twist (mu=3) -- the
            # pattern tracks the edge twist's orientation relative to the
            # LADDER-PRES axis, so minus-form membership is presentation-
            # relative, not invariant.
            minus = name.endswith("_minus")
            expected_all = (not minus) or (mu in (1, 2))
            checks.append((
                f"hks_{name}_mu{mu}_all_edge_diag",
                verdicts == {expected_all},
            ))
            hks_rows.append((name, mu, sorted(labels)[0], verdicts == {True}))

    quote_checks = text_audits()
    checks.extend((f"text_{idx}_{rel}", ok) for idx, (rel, ok) in enumerate(quote_checks))
    ast_ok, ast_detail = ast_self_scan()
    checks.append(("ast_self_scan", ast_ok))

    failed = [name for name, ok in checks if not ok]
    quote_counts = {}
    for rel_path, ok in quote_checks:
        quote_counts.setdefault(rel_path, [0, 0])
        quote_counts[rel_path][0] += 1
        quote_counts[rel_path][1] += 1 if ok else 0

    print(
        "TEXT-AUDIT "
        + ";".join(
            f"{Path(path).name}:{passed}/{total}" for path, (total, passed) in quote_counts.items()
        )
    )
    print(f"AST-SCAN {'PASS' if ast_ok else 'FAIL'} detail={ast_detail}")
    for name, label, in_class in t1_rows:
        verdict = "IN" if in_class else "OUT"
        print(f"T1 {name}: label={label}; EDGE-DIAG={verdict}; swap_image={label}")
    for name, mu, label, in_class in hks_rows:
        verdict = "IN" if in_class else "OUT"
        print(
            f"HKS {name} mu={mu}: endpoint_parities=8; label={label}; "
            f"EDGE-DIAG={verdict}"
        )

    hks_summary = {}
    for name, mu, label, in_class in hks_rows:
        hks_summary.setdefault(name, []).append(
            f"mu{mu}:{label}:{'IN' if in_class else 'OUT'}"
        )
    summary = ";".join(
        f"{name}[" + ",".join(parts) + "]" for name, parts in hks_summary.items()
    )
    t1_summary = ",".join(
        f"{name}:{label}:{'IN' if in_class else 'OUT'}" for name, label, in_class in t1_rows
    )
    print(
        "DECLARATION "
        f"T1={t1_summary}; HKS_all_8_endpoint_parities={summary}; "
        "not_consumed_or_claimed=statistics_selection,dynamics,weights,"
        "color_carrier,SUPPLIED-C3,K1_audit,Tier-A_content,audit_verdicts"
    )
    print(f"TOTAL: PASS={len(checks) - len(failed)} FAIL={len(failed)}")
    if failed:
        for name in failed:
            print(f"FAIL: {name}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
