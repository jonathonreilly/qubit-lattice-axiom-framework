#!/usr/bin/env python3
"""Exact runner for the 2026-07-06 factor-preservation draft note."""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


F = Fraction
C0 = (F(0), F(0))
C1 = (F(1), F(0))
CI = (F(0), F(1))

SCRIPT = Path(__file__).resolve()
ROOT = SCRIPT.parents[1]

SOURCE_1 = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SOURCE_2 = ROOT / "docs" / "GAUGE_FACTOR_LOCAL_SELECTOR_NORMALIZER_THEOREM_NOTE_2026-06-18.md"
SOURCE_3 = ROOT / "docs" / "GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md"

QUOTES_SOURCE_1 = [
    "Only records are readable. A readout value is determined by record content alone.",
    "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration before use as a premise.",
]

QUOTES_SOURCE_2 = [
    "It proves the exact finite statement that, once a factor-algebra preservation rule is supplied on the same `C^3(base) x C^2(fiber)` carrier, the algebraic normalizer is uniquely the factorwise `su(3) + su(2) + u(1)` surface rather than full `u(6)`.",
    "This note proves its consequence; it does not make that rule an axiom or a retained primitive.",
    "The finite normalizer theorem is blind to vector versus left-handed weak coupling.",
]

QUOTES_SOURCE_3 = [
    "Thus any selector depending only on conjugation-invariant algebraic data of the carrier, or on irreducibility/scalar-commutant criteria, cannot select the specific factorwise `su(3)+su(2)+u(1)` embedding.",
    "Selecting it requires additional non-invariant structure: the factorization/gauging principle, `MR_color`, and the chiral weak-coupling bridge.",
    "This is not a broad no-go against deriving gauge selection. It leaves live:",
    "Factor-locality or operator-Schmidt rank could distinguish the embedding, but only by consuming the supplied `C^3 x C^2` tensor split, which is exactly the extra structure the route was trying not to import.",
    "A future local-dynamics theorem could privilege a tensor factor, a link representation, or a chiral coupling by non-conjugation-invariant structure.",
    "a future retained theorem deriving chiral `su(2)_L`",
]


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cneg(a):
    return (-a[0], -a[1])


def csub(a, b):
    return cadd(a, cneg(b))


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cscale(q, a):
    return (q * a[0], q * a[1])


def zero_matrix(rows, cols):
    return [[C0 for _ in range(cols)] for _ in range(rows)]


def eye(n):
    out = zero_matrix(n, n)
    for i in range(n):
        out[i][i] = C1
    return out


def mat_add(a, b):
    return [[cadd(a[r][c], b[r][c]) for c in range(len(a[0]))] for r in range(len(a))]


def mat_sub(a, b):
    return [[csub(a[r][c], b[r][c]) for c in range(len(a[0]))] for r in range(len(a))]


def mat_scale(q, a):
    return [[cscale(q, a[r][c]) for c in range(len(a[0]))] for r in range(len(a))]


def mat_mul(a, b):
    rows, mid, cols = len(a), len(b), len(b[0])
    out = zero_matrix(rows, cols)
    for r in range(rows):
        for c in range(cols):
            total = C0
            for k in range(mid):
                total = cadd(total, cmul(a[r][k], b[k][c]))
            out[r][c] = total
    return out


def comm(a, b):
    return mat_sub(mat_mul(a, b), mat_mul(b, a))


def tensor(a, b):
    ar, ac = len(a), len(a[0])
    br, bc = len(b), len(b[0])
    out = zero_matrix(ar * br, ac * bc)
    for i in range(ar):
        for j in range(ac):
            for p in range(br):
                for q in range(bc):
                    out[i * br + p][j * bc + q] = cmul(a[i][j], b[p][q])
    return out


def matrix_unit(n, r, c):
    out = zero_matrix(n, n)
    out[r][c] = C1
    return out


def vectorize_re_im(a):
    out = []
    for row in a:
        for z in row:
            out.extend([z[0], z[1]])
    return out


def trace(a):
    total = C0
    for i in range(len(a)):
        total = cadd(total, a[i][i])
    return total


def is_zero_matrix(a):
    return all(z == C0 for row in a for z in row)


def lincomb(coeffs, basis):
    out = zero_matrix(len(basis[0]), len(basis[0][0]))
    for q, b in zip(coeffs, basis):
        if q:
            out = mat_add(out, mat_scale(q, b))
    return out


def u_basis(n):
    basis = []
    for r in range(n):
        m = zero_matrix(n, n)
        m[r][r] = CI
        basis.append(m)
    for r in range(n):
        for c in range(r + 1, n):
            real_skew = zero_matrix(n, n)
            real_skew[r][c] = C1
            real_skew[c][r] = (-F(1), F(0))
            imag_sym = zero_matrix(n, n)
            imag_sym[r][c] = CI
            imag_sym[c][r] = CI
            basis.extend([real_skew, imag_sym])
    return basis


def su_basis(n):
    basis = []
    for r in range(n - 1):
        m = zero_matrix(n, n)
        m[r][r] = CI
        m[r + 1][r + 1] = cneg(CI)
        basis.append(m)
    for r in range(n):
        for c in range(r + 1, n):
            real_skew = zero_matrix(n, n)
            real_skew[r][c] = C1
            real_skew[c][r] = (-F(1), F(0))
            imag_sym = zero_matrix(n, n)
            imag_sym[r][c] = CI
            imag_sym[c][r] = CI
            basis.extend([real_skew, imag_sym])
    return basis


def rref(rows, ncols=None):
    if ncols is None:
        ncols = len(rows[0]) if rows else 0
    mat = [[F(x) for x in row] for row in rows if any(x != 0 for x in row)]
    pivots = []
    r = 0
    for c in range(ncols):
        pivot = None
        for i in range(r, len(mat)):
            if mat[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        factor = mat[r][c]
        mat[r] = [x / factor for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                scale = mat[i][c]
                mat[i] = [x - scale * y for x, y in zip(mat[i], mat[r])]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    return mat, pivots


def rank(rows, ncols=None):
    return len(rref(rows, ncols)[1])


def nullspace(rows, ncols):
    reduced, pivots = rref(rows, ncols)
    pivot_set = set(pivots)
    free_cols = [c for c in range(ncols) if c not in pivot_set]
    basis = []
    for free in free_cols:
        vec = [F(0) for _ in range(ncols)]
        vec[free] = F(1)
        for row_index, pivot_col in enumerate(pivots):
            vec[pivot_col] = -reduced[row_index][free]
        basis.append(vec)
    return basis


def idx(base, fiber):
    return 2 * base + fiber


def constraints_in_m3_tensor_i2(m):
    vals = []
    for p in range(3):
        for q in range(3):
            vals.append(m[idx(p, 0)][idx(q, 1)])
            vals.append(m[idx(p, 1)][idx(q, 0)])
            vals.append(csub(m[idx(p, 0)][idx(q, 0)], m[idx(p, 1)][idx(q, 1)]))
    return vals


def constraints_in_i3_tensor_m2(m):
    vals = []
    for p in range(3):
        for q in range(3):
            if p == q:
                continue
            for a in range(2):
                for b in range(2):
                    vals.append(m[idx(p, a)][idx(q, b)])
    for p in (1, 2):
        for a in range(2):
            for b in range(2):
                vals.append(csub(m[idx(p, a)][idx(p, b)], m[idx(0, a)][idx(0, b)]))
    return vals


I2 = eye(2)
I3 = eye(3)
I6 = eye(6)

M3_GENERATORS = [tensor(matrix_unit(3, r, c), I2) for r in range(3) for c in range(3)]
M2_GENERATORS = [tensor(I3, matrix_unit(2, r, c)) for r in range(2) for c in range(2)]


def stabilizer_equation_rows(u6):
    rows = []
    for y in M3_GENERATORS:
        columns = [constraints_in_m3_tensor_i2(comm(x, y)) for x in u6]
        for k in range(len(columns[0])):
            rows.append([col[k][0] for col in columns])
            rows.append([col[k][1] for col in columns])
    for y in M2_GENERATORS:
        columns = [constraints_in_i3_tensor_m2(comm(x, y)) for x in u6]
        for k in range(len(columns[0])):
            rows.append([col[k][0] for col in columns])
            rows.append([col[k][1] for col in columns])
    return rows


def preserves_factor_split(x):
    for y in M3_GENERATORS:
        if any(z != C0 for z in constraints_in_m3_tensor_i2(comm(x, y))):
            return False
    for y in M2_GENERATORS:
        if any(z != C0 for z in constraints_in_i3_tensor_m2(comm(x, y))):
            return False
    return True


def normalize_text(text):
    return " ".join(text.split())


def quote_audit():
    source1 = normalize_text(SOURCE_1.read_text(encoding="utf-8"))
    source2 = normalize_text(SOURCE_2.read_text(encoding="utf-8"))
    source3 = normalize_text(SOURCE_3.read_text(encoding="utf-8"))
    ok1 = all(normalize_text(q) in source1 for q in QUOTES_SOURCE_1)
    ok2 = all(normalize_text(q) in source2 for q in QUOTES_SOURCE_2)
    ok3 = all(normalize_text(q) in source3 for q in QUOTES_SOURCE_3)
    return ok1 and ok2 and ok3


def ast_self_scan():
    tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
    forbidden_imports = {"subprocess", "socket", "requests", "urllib", "http", "ftplib"}
    forbidden_calls = {"system", "popen", "spawnl", "spawnlp", "spawnv", "spawnvp", "execv", "execve"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in forbidden_imports:
                    return False
        if isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in forbidden_imports:
                return False
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in {"eval", "exec", "compile"}:
                return False
            if isinstance(node.func, ast.Name) and node.func.id == "open":
                if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
                    if any(flag in str(node.args[1].value) for flag in ("w", "a", "+", "x")):
                        return False
            if isinstance(node.func, ast.Attribute):
                if node.func.attr in forbidden_calls or node.func.attr in {"write_text", "write_bytes"}:
                    return False
    return True


def main():
    checks = []

    u6 = u_basis(6)
    u3 = u_basis(3)
    u2 = u_basis(2)
    su3 = su_basis(3)
    su2 = su_basis(2)

    u6_rank = rank([vectorize_re_im(x) for x in u6])
    checks.append(("u6_dim_36_exact", len(u6) == 36 and u6_rank == 36))

    factor_basis = [tensor(a, I2) for a in u3] + [tensor(I3, b) for b in u2]
    factor_vectors = [vectorize_re_im(x) for x in factor_basis]
    factor_rank = rank(factor_vectors)
    center_kernel_dim = len(factor_basis) - factor_rank
    left_center = tensor([[CI if r == c else C0 for c in range(3)] for r in range(3)], I2)
    right_center = tensor(I3, [[CI if r == c else C0 for c in range(2)] for r in range(2)])
    center_overlap_ok = is_zero_matrix(mat_sub(left_center, right_center))
    checks.append(("factorwise_dim_12_center_overlap", factor_rank == 12 and center_kernel_dim == 1 and center_overlap_ok))

    equations = stabilizer_equation_rows(u6)
    equation_rank = rank(equations, len(u6))
    stabilizer_nullity = len(u6) - equation_rank
    stabilizer_coeffs = nullspace(equations, len(u6))
    stabilizer_basis = [lincomb(coeffs, u6) for coeffs in stabilizer_coeffs]
    stabilizer_vectors = [vectorize_re_im(x) for x in stabilizer_basis]
    combined_rank = rank(factor_vectors + stabilizer_vectors)
    factor_subset = all(preserves_factor_split(x) for x in factor_basis)
    checks.append((
        "stabilizer_equals_factorwise_both_containments",
        stabilizer_nullity == 12 and factor_subset and combined_rank == 12,
    ))

    su3_lift = [tensor(a, I2) for a in su3]
    su2_lift = [tensor(I3, b) for b in su2]
    semisimple_rank = rank([vectorize_re_im(x) for x in su3_lift + su2_lift])
    global_u1_rank = rank([vectorize_re_im(left_center)])
    relative_identity_image_zero = is_zero_matrix(mat_sub(left_center, right_center))
    traceless_semisimple = all(trace(x) == C0 for x in su3_lift + su2_lift)
    global_trace = trace(left_center)
    checks.append((
        "decomposition_bookkeeping_exact",
        rank([vectorize_re_im(x) for x in su3_lift]) == 8
        and rank([vectorize_re_im(x) for x in su2_lift]) == 3
        and semisimple_rank == 11
        and global_u1_rank == 1
        and relative_identity_image_zero
        and traceless_semisimple
        and global_trace == (F(0), F(6)),
    ))

    # Structure verification (panel-required): brackets, direct sum, Killing.
    basis11 = su3_lift + su2_lift
    vec11 = [vectorize_re_im(x) for x in basis11]
    base_rank = rank(vec11)

    def solve_coords(mat):
        # exact coordinates of mat in span(basis11), or None
        rows = [list(v) for v in vec11]
        target = list(vectorize_re_im(mat))
        n = len(rows)
        m = len(target)
        aug = [[rows[i][j] for i in range(n)] + [target[j]] for j in range(m)]
        # Gaussian elimination over Q on the m x (n+1) system
        pivots = []
        r = 0
        for c in range(n):
            piv = None
            for rr in range(r, m):
                if aug[rr][c] != 0:
                    piv = rr
                    break
            if piv is None:
                continue
            aug[r], aug[piv] = aug[piv], aug[r]
            pv = aug[r][c]
            aug[r] = [x / pv for x in aug[r]]
            for rr in range(m):
                if rr != r and aug[rr][c] != 0:
                    f = aug[rr][c]
                    aug[rr] = [x - f * y for x, y in zip(aug[rr], aug[r])]
            pivots.append(c)
            r += 1
        coords = [F(0)] * n
        for idx, c in enumerate(pivots):
            coords[c] = aug[idx][n]
        # consistency: rows beyond pivots must be zero
        for rr in range(r, m):
            if aug[rr][n] != 0:
                return None
        # verify reconstruction exactly
        recon = lincomb(coords, basis11)
        if not is_zero_matrix(mat_sub(recon, mat)):
            return None
        return coords

    closure_ok = True
    cross_zero_ok = True
    struct = {}
    for i, x in enumerate(basis11):
        for j, y in enumerate(basis11):
            b = comm(x, y)
            coords = solve_coords(b)
            if coords is None:
                closure_ok = False
            else:
                struct[(i, j)] = coords
            if i < 8 <= j or j < 8 <= i:
                if not is_zero_matrix(b):
                    cross_zero_ok = False
    abelian_commutes = all(is_zero_matrix(comm(left_center, x)) for x in basis11)
    checks.append((
        "lie_structure_closure_cross_zero_abelian_central",
        closure_ok and cross_zero_ok and abelian_commutes and base_rank == 11,
    ))

    # Killing form K(X,Y) = tr(ad_X ad_Y) on the 11-dim traceless part,
    # exact over Q; nondegeneracy by exact determinant.
    def ad_matrix(i):
        return [[struct[(i, j)][k] for j in range(11)] for k in range(11)]

    ads = [ad_matrix(i) for i in range(11)]

    def qmat_mul(a, b):
        return [[sum(a[r][t] * b[t][c] for t in range(11)) for c in range(11)] for r in range(11)]

    def qtrace(a):
        return sum(a[i][i] for i in range(11))

    killing = [[qtrace(qmat_mul(ads[i], ads[j])) for j in range(11)] for i in range(11)]

    def qdet(m):
        m = [row[:] for row in m]
        n = len(m)
        det = F(1)
        for c in range(n):
            piv = None
            for r in range(c, n):
                if m[r][c] != 0:
                    piv = r
                    break
            if piv is None:
                return F(0)
            if piv != c:
                m[c], m[piv] = m[piv], m[c]
                det = -det
            det *= m[c][c]
            pv = m[c][c]
            m[c] = [x / pv for x in m[c]]
            for r in range(c + 1, n):
                if m[r][c] != 0:
                    f = m[r][c]
                    m[r] = [x - f * y for x, y in zip(m[r], m[c])]
        return det

    killing_det = qdet(killing)
    killing_cross_zero = all(killing[i][j] == 0 for i in range(8) for j in range(8, 11))
    checks.append((
        "killing_form_nondegenerate_block_diagonal",
        killing_det != 0 and killing_cross_zero,
    ))

    checks.append(("quoted_source_sentences_text_audit", quote_audit()))
    checks.append(("ast_self_scan_readonly_no_network_no_subprocess", ast_self_scan()))

    passed = sum(1 for _, ok in checks if ok)
    failed = len(checks) - passed
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(
        "DECLARATION premises=minimal_axioms_context; "
        "REGISTERED-FACTOR(named conditional, not axiom content); "
        "supplied C^3 tensor C^2 model surface; exact finite matrix algebra"
    )
    print(
        "DIMENSIONS u6=36 factorwise=12 stabilizer=12 "
        "su3=8 su2=3 semisimple=11 abelian_image=1 relative_identity_kernel=1"
    )
    print(f"TOTAL PASS={passed} FAIL={failed}")
    raise SystemExit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
