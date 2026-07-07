#!/usr/bin/env python3
"""Exact checks for matter-realization arena split preservation.

No floating point, no numpy/sympy.  Complex numbers are represented as
(Fraction(real), Fraction(imag)) pairs throughout the load-bearing algebra.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def C(re=0, im=0):
    return (Fraction(re), Fraction(im))


ZERO = C(0)
ONE = C(1)
IUNIT = C(0, 1)


def c_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def c_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def c_neg(a):
    return (-a[0], -a[1])


def c_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def c_conj(a):
    return (a[0], -a[1])


def c_div(a, b):
    den = b[0] * b[0] + b[1] * b[1]
    if den == 0:
        raise ZeroDivisionError("complex Fraction division by zero")
    num = c_mul(a, c_conj(b))
    return (num[0] / den, num[1] / den)


def c_scale(q, a):
    return (Fraction(q) * a[0], Fraction(q) * a[1])


def m_eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def m_zero(r, c):
    return [[ZERO for _ in range(c)] for _ in range(r)]


def m_shape(a):
    return (len(a), len(a[0]) if a else 0)


def m_add(a, b):
    return [[c_add(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def m_sub(a, b):
    return [[c_sub(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def m_scale(q, a):
    return [[c_scale(q, x) for x in row] for row in a]


def m_mul(a, b):
    ar, ac = m_shape(a)
    br, bc = m_shape(b)
    if ac != br:
        raise ValueError("matrix shape mismatch")
    out = m_zero(ar, bc)
    for i in range(ar):
        for j in range(bc):
            s = ZERO
            for k in range(ac):
                s = c_add(s, c_mul(a[i][k], b[k][j]))
            out[i][j] = s
    return out


def m_vec(a, v):
    return [sum_c(c_mul(aij, vj) for aij, vj in zip(row, v)) for row in a]


def sum_c(items):
    s = ZERO
    for item in items:
        s = c_add(s, item)
    return s


def v_sub(a, b):
    return [c_sub(x, y) for x, y in zip(a, b)]


def v_scale(q, v):
    return [c_scale(q, x) for x in v]


def m_eq(a, b):
    return m_shape(a) == m_shape(b) and all(
        a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a[0]))
    )


def v_eq(a, b):
    return len(a) == len(b) and all(x == y for x, y in zip(a, b))


def m_trace(a):
    return sum_c(a[i][i] for i in range(len(a)))


def m_comm(a, b):
    return m_sub(m_mul(a, b), m_mul(b, a))


def kron(a, b):
    ar, ac = m_shape(a)
    br, bc = m_shape(b)
    out = m_zero(ar * br, ac * bc)
    for i in range(ar):
        for j in range(ac):
            for k in range(br):
                for l in range(bc):
                    out[i * br + k][j * bc + l] = c_mul(a[i][j], b[k][l])
    return out


def m_rank(a):
    mat = [[x for x in row] for row in a]
    rows, cols = m_shape(mat)
    rank = 0
    for col in range(cols):
        pivot = None
        for r in range(rank, rows):
            if mat[r][col] != ZERO:
                pivot = r
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = c_div(ONE, mat[rank][col])
        mat[rank] = [c_mul(inv, x) for x in mat[rank]]
        for r in range(rows):
            if r == rank:
                continue
            factor = mat[r][col]
            if factor == ZERO:
                continue
            mat[r] = [c_sub(x, c_mul(factor, y)) for x, y in zip(mat[r], mat[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def e2(i, j):
    out = m_zero(2, 2)
    out[i][j] = ONE
    return out


SIGMA1 = [[ZERO, ONE], [ONE, ZERO]]
SIGMA2 = [[ZERO, c_neg(IUNIT)], [IUNIT, ZERO]]
SIGMA3 = [[ONE, ZERO], [ZERO, c_neg(ONE)]]
ID2 = m_eye(2)
ID4 = m_eye(4)
PAULI = [SIGMA1, SIGMA2, SIGMA3]


def pauli_power(sigma, n):
    return ID2 if n % 2 == 0 else sigma


def t_frame(x):
    x1, x2, x3 = x
    return m_mul(m_mul(pauli_power(SIGMA1, x1), pauli_power(SIGMA2, x2)), pauli_power(SIGMA3, x3))


def t_frame_inv(x):
    x1, x2, x3 = x
    return m_mul(m_mul(pauli_power(SIGMA3, x3), pauli_power(SIGMA2, x2)), pauli_power(SIGMA1, x1))


def eta(mu, x):
    x1, x2, _ = x
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if x1 % 2 else 1
    if mu == 2:
        return -1 if (x1 + x2) % 2 else 1
    raise ValueError("mu must be 0, 1, or 2")


def signed_matrix(sign, a):
    return m_scale(sign, a)


def swap4():
    out = m_zero(4, 4)
    for a in range(2):
        for b in range(2):
            out[b * 2 + a][a * 2 + b] = ONE
    return out


S = swap4()
P_SYM = m_scale(Fraction(1, 2), m_add(ID4, S))
P_ANTI = m_scale(Fraction(1, 2), m_sub(ID4, S))


class Checks:
    def __init__(self):
        self.pass_count = 0
        self.failures = []

    def check(self, cond, label):
        if cond:
            self.pass_count += 1
            print(f"[PASS] {label}")
        else:
            self.failures.append(label)
            print(f"[FAIL] {label}")


def norm_text(s):
    return " ".join(s.split())


SOURCE_QUOTES = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md": [
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.",
        "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration before use as a premise.",
    ],
    "docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md": [
        "P-SD: a *site-local unitary* scalarization `T(x)` is supplied; alternatives that bypass spin diagonalization (for example a 2-component naive operator) are outside this local theorem unless separately mapped into P-SD",
        "Under P-KIN the kinetic operator is `D = \u03a3_\u03bc \u03b3_\u03bc \u2297 \u2202_\u03bc` with `\u2202_\u03bc` the symmetric lattice difference.",
        "representative `\u03b7^0` of (6); a canonical solution of (4) is `T(x) = \u03b3_1^{x_1} \u03b3_2^{x_2} \u03b3_3^{x_3}` (on the Pauli realization, `T(x) = \u03c3_1^{x_1} \u03c3_2^{x_2} \u03c3_3^{x_3}`). [Lemma 4]",
        "Finite tori carry extra holonomy data: signs around non-contractible cycles (PBC/APBC and wrap-sign conventions) are boundary convention data, not local phase law; likewise lattice-axis permutation is coordinate-label gauge",
    ],
    "docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md": [
        "This note supplies a narrow rule-level selector on the licensed surface that was not available to the parent before the clarified variation clause.",
        "K1: phi=-1, representative eta0: eta0_1 = 1, eta0_2 = (-1)^{x1}, eta0_3 = (-1)^{x1+x2}",
        "and extracts the K1 `Gamma_mu` family from the eta0 signs rather than from target Pauli matrices.",
        "`Gamma_mu` family verifies the Dirac-square and anticommutation consequences.",
    ],
    "docs/COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md": [
        "Frame-relativity (load-bearing honesty): an INDEPENDENT per-site presentation change (`g tensor 1`) does not commute with `S` and moves the split; the runner exhibits this.",
        "The split is canonical relative to the shared presentation, and its stability group is the diagonal.",
        "Comparing presentations across sites is exactly the transport question left to later blocks; nothing here supplies it.",
        "R1 spin-coupling preservation: any downstream realization tying qubit generators to spatial axes must separately show the arena split survives -- open.",
    ],
}


def audit_quotes():
    missing = []
    for rel, quotes in SOURCE_QUOTES.items():
        text = norm_text((ROOT / rel).read_text())
        for quote in quotes:
            if norm_text(quote) not in text:
                missing.append((rel, quote))
    return missing


def elementary_pair_identity_holds():
    units = [e2(i, j) for i in range(2) for j in range(2)]
    for a in units:
        for b in units:
            lhs = m_mul(m_mul(S, kron(a, b)), S)
            rhs = kron(b, a)
            if not m_eq(lhs, rhs):
                return False
    return True


def diagonal_commutes_for_paulis():
    return all(m_eq(m_comm(S, kron(p, p)), m_zero(4, 4)) for p in PAULI)


def one_sided_moves_split():
    action = kron(SIGMA3, ID2)
    v_sym = [ZERO, ONE, ONE, ZERO]
    moved = m_vec(action, v_sym)
    anti_check = v_eq(m_vec(S, moved), v_scale(-1, moved))
    nonzero = any(x != ZERO for x in moved)
    comm_nonzero = not m_eq(m_comm(S, action), m_zero(4, 4))
    return anti_check and nonzero and comm_nonzero


def ks_relative_frame_checks():
    details = []
    ok = True
    for x1 in range(2):
        for x2 in range(2):
            for x3 in range(2):
                x = (x1, x2, x3)
                for mu in range(3):
                    xp = list(x)
                    xp[mu] += 1
                    rel = m_mul(t_frame(tuple(xp)), t_frame_inv(x))
                    expected = signed_matrix(eta(mu, x), PAULI[mu])
                    if not m_eq(rel, expected):
                        ok = False
                        details.append((x, mu + 1))
    return ok, details


def joint_dims_for_twist(mu):
    sigma = PAULI[mu]
    d = kron(sigma, sigma)
    sprime = m_mul(d, S)
    dims = {}
    for s_eig in (1, -1):
        for sp_eig in (1, -1):
            ps = m_scale(Fraction(1, 2), m_add(ID4, m_scale(s_eig, S)))
            psp = m_scale(Fraction(1, 2), m_add(ID4, m_scale(sp_eig, sprime)))
            proj = m_mul(ps, psp)
            tr = m_trace(proj)
            dims[(s_eig, sp_eig)] = tr
    return sprime, dims


def twisted_exchange_checks():
    expected = {
        (1, 1): C(2),
        (1, -1): C(1),
        (-1, 1): C(1),
        (-1, -1): C(0),
    }
    for mu in range(3):
        sprime, dims = joint_dims_for_twist(mu)
        if not m_eq(m_comm(sprime, S), m_zero(4, 4)):
            return False, mu + 1, dims
        if dims != expected:
            return False, mu + 1, dims
        if not m_eq(m_mul(sprime, sprime), ID4):
            return False, mu + 1, dims
    return True, None, expected


def split_projector_ranks_ok():
    return (
        m_eq(m_mul(S, S), ID4)
        and m_rank(P_SYM) == 3
        and m_rank(P_ANTI) == 1
        and m_eq(m_mul(P_SYM, P_SYM), P_SYM)
        and m_eq(m_mul(P_ANTI, P_ANTI), P_ANTI)
        and m_eq(m_mul(P_SYM, P_ANTI), m_zero(4, 4))
    )


def ast_self_scan():
    source = Path(__file__).read_text()
    tree = ast.parse(source)
    banned_import_roots = {"subprocess", "socket", "requests", "urllib", "http", "numpy", "sympy"}
    banned_calls = {"eval", "exec", "compile", "__import__"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in banned_import_roots:
                    return False
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in banned_import_roots:
                return False
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in banned_calls:
                return False
        elif isinstance(node, ast.Constant) and isinstance(node.value, float):
            return False
    return True


def main():
    checks = Checks()

    checks.check(not audit_quotes(), "text audits: every source quote from files 1-4 is present")
    checks.check(split_projector_ranks_ok(), "SWAP algebra and Sym/Anti projectors have exact ranks 3/1")
    checks.check(elementary_pair_identity_holds(), "16 elementary-pair identity S(A tensor B)S = B tensor A")
    checks.check(diagonal_commutes_for_paulis(), "diagonal Pauli lifts commute with SWAP")
    checks.check(one_sided_moves_split(), "one-sided sigma3 tensor I moves Sym into Anti by exact witness")

    ks_ok, ks_bad = ks_relative_frame_checks()
    checks.check(ks_ok and not ks_bad, "KS relative frames: T(x+mu)T(x)^-1 = eta_mu(x) sigma_mu")

    tw_ok, tw_mu, tw_dims = twisted_exchange_checks()
    checks.check(tw_ok, "twisted exchanges S'_mu commute with S and have joint dims 2,1,1,0")
    checks.check(ast_self_scan(), "AST self-scan: no banned imports/calls and no float constants")

    fail_count = len(checks.failures)
    if fail_count:
        print(f"DETAIL failures={checks.failures}; tw_mu={tw_mu}; tw_dims={tw_dims}; ks_bad={ks_bad}")
    else:
        print(
            "DECLARATION verdict=SPLIT_PRESERVATION_EXACT_FOR_EDGE_DIAG_CLASS; ks_frame_transport=IN_CLASS; open_bridge=KS-HOP-BRIDGE; "
            "condition=EDGE-DIAG; "
            "joint_dims={(S=+,S'=+):2,(+,-):1,(-,+):1,(-,-):0}; "
            "not_consumed=K1_audit,color_carrier,beyond_KS,dynamics_statistics"
        )
    print(f"TOTAL: PASS={checks.pass_count} FAIL={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
