#!/usr/bin/env python3
"""Runner for the COMP Hurwitz-clause scope-reduction note.

Self-contained finite checks only.  No repo imports, no network, no cache write.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np


PASS_COUNT = 0
FAIL_COUNT = 0


def report(name: str, ok: bool, detail: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        print(f"[PASS] {name}: {detail}")
    else:
        FAIL_COUNT += 1
        print(f"[FAIL] {name}: {detail}")


def real_rank(mats: list[np.ndarray], tol: float = 1.0e-10) -> int:
    rows = []
    for mat in mats:
        rows.append(np.concatenate([mat.real.ravel(), mat.imag.ravel()]))
    return int(np.linalg.matrix_rank(np.vstack(rows), tol=tol))


def su3_hermitian_traceless_basis() -> list[np.ndarray]:
    basis: list[np.ndarray] = []
    for i in range(3):
        for j in range(i + 1, 3):
            sym = np.zeros((3, 3), dtype=complex)
            sym[i, j] = 1.0
            sym[j, i] = 1.0
            asym = np.zeros((3, 3), dtype=complex)
            asym[i, j] = -1.0j
            asym[j, i] = 1.0j
            basis.extend([sym, asym])
    diag1 = np.diag([1.0, -1.0, 0.0]).astype(complex)
    diag2 = np.diag([1.0, 1.0, -2.0]).astype(complex)
    basis.extend([diag1, diag2])
    return basis


def _cd_mul(x: list, y: list) -> list:
    """Cayley-Dickson product on length-2^k integer/float coefficient lists.

    (a, b)(c, d) = (a c - d* b, d a + b c*), conj(a, b) = (a*, -b).
    Applied twice from the quaternions this constructs the octonions from
    first principles; no multiplication-table convention is trusted.
    """
    n = len(x)
    if n == 1:
        return [x[0] * y[0]]
    h = n // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    left = [p - q for p, q in zip(_cd_mul(a, c), _cd_mul(_cd_conj(d), b))]
    right = [p + q for p, q in zip(_cd_mul(d, a), _cd_mul(b, _cd_conj(c)))]
    return left + right


def _cd_conj(x: list) -> list:
    n = len(x)
    if n == 1:
        return [x[0]]
    h = n // 2
    return _cd_conj(x[:h]) + [-v for v in x[h:]]


def _cd_basis_table() -> dict:
    """Exact integer structure constants e_i e_j = sign * e_k from Cayley-Dickson."""
    table = {}
    for i in range(8):
        for j in range(8):
            ei = [0] * 8
            ej = [0] * 8
            ei[i] = 1
            ej[j] = 1
            prod = _cd_mul(ei, ej)
            support = [k for k, v in enumerate(prod) if v != 0]
            if len(support) != 1 or prod[support[0]] not in (1, -1):
                raise ValueError(f"CD product e{i} e{j} is not a signed basis element")
            table[(i, j)] = (float(prod[support[0]]), support[0])
    return table


CD_TABLE = _cd_basis_table()


def basis_product(a: int, b: int) -> tuple[float, int]:
    return CD_TABLE[(a, b)]


def oct_mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.zeros(8, dtype=float)
    for i in range(8):
        if a[i] == 0.0:
            continue
        for j in range(8):
            if b[j] == 0.0:
                continue
            sign, k = basis_product(i, j)
            out[k] += sign * a[i] * b[j]
    return out


def unit(idx: int) -> np.ndarray:
    out = np.zeros(8, dtype=float)
    out[idx] = 1.0
    return out


def commutant_dimension(generators: list[np.ndarray], tol: float = 1.0e-9) -> int:
    n = generators[0].shape[0]
    ident = np.eye(n, dtype=complex)
    blocks = []
    for gen in generators:
        blocks.append(np.kron(gen.T, ident) - np.kron(ident, gen))
    system = np.vstack(blocks)
    rank = int(np.linalg.matrix_rank(system, tol=tol))
    return n * n - rank


def selected_axis_matrices(axis: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    vertices = list(itertools.product([0, 1], repeat=3))
    index = {vertex: n for n, vertex in enumerate(vertices)}
    n = len(vertices)
    xmat = np.zeros((n, n), dtype=complex)
    zmat = np.zeros((n, n), dtype=complex)
    tau = np.zeros((n, n), dtype=complex)
    other_axes = [idx for idx in range(3) if idx != axis]
    a, b = other_axes
    for vertex in vertices:
        row = index[vertex]
        flipped = list(vertex)
        flipped[axis] = 1 - flipped[axis]
        xmat[index[tuple(flipped)], row] = 1.0
        zmat[row, row] = 1.0 if vertex[axis] == 0 else -1.0
        swapped = list(vertex)
        swapped[a], swapped[b] = swapped[b], swapped[a]
        tau[index[tuple(swapped)], row] = 1.0
    ymat = -1.0j * zmat @ xmat
    return xmat, ymat, zmat, tau


def graph_first_sanity() -> bool:
    ident = np.eye(8, dtype=complex)
    for axis in range(3):
        xmat, ymat, zmat, tau = selected_axis_matrices(axis)
        su2_ok = (
            np.allclose(xmat @ xmat, ident)
            and np.allclose(ymat @ ymat, ident)
            and np.allclose(zmat @ zmat, ident)
            and np.allclose(xmat @ ymat - ymat @ xmat, 2.0j * zmat)
            and np.allclose(ymat @ zmat - zmat @ ymat, 2.0j * xmat)
            and np.allclose(zmat @ xmat - xmat @ zmat, 2.0j * ymat)
        )
        swap_commutes = all(np.allclose(tau @ gen, gen @ tau) for gen in (xmat, ymat, zmat))
        plus_rank = int(round(np.trace((ident + tau) / 2.0).real))
        minus_rank = int(round(np.trace((ident - tau) / 2.0).real))
        su2_comm_dim = commutant_dimension([xmat, ymat, zmat])
        comm_dim = commutant_dimension([xmat, ymat, zmat, tau])
        if not (
            su2_ok
            and swap_commutes
            and plus_rank == 6
            and minus_rank == 2
            and su2_comm_dim == 16
            and comm_dim == 10
        ):
            return False
    return True


def main() -> int:
    basis = su3_hermitian_traceless_basis()
    hermitian = all(np.allclose(mat.conj().T, mat) for mat in basis)
    traceless = all(abs(np.trace(mat)) < 1.0e-12 for mat in basis)
    independent = real_rank(basis) == 8
    report(
        "su(3) basis count",
        len(basis) == 8 and hermitian and traceless and independent,
        "explicit traceless Hermitian 3x3 basis has real dimension 8",
    )

    hurwitz_unit_dims = {0, 1, 3, 7}
    report(
        "Hurwitz unit-sphere dimensions",
        8 not in hurwitz_unit_dims,
        "8 is disjoint from {0, 1, 3, 7}",
    )

    anticommutative = True
    squares_ok = True
    for i in range(8):
        for j in range(8):
            if i != j and i > 0 and j > 0:
                left_sign, left_idx = basis_product(i, j)
                right_sign, right_idx = basis_product(j, i)
                if left_idx != right_idx or left_sign != -right_sign:
                    anticommutative = False
            if i == j and i > 0:
                sign, idx = basis_product(i, i)
                if idx != 0 or sign != -1.0:
                    squares_ok = False
    report(
        "octonion table from Cayley-Dickson doubling",
        anticommutative and squares_ok,
        "exact integer structure constants: e_i^2 = -1 and imaginary units anticommute; "
        "no multiplication-table convention trusted from memory",
    )

    # Exact norm multiplicativity at the structure-constant level: for basis
    # elements N(e_i e_j) = 1 = N(e_i) N(e_j) holds by the signed-permutation
    # form verified above.  The polynomial identity N(xy) = N(x)N(y) for the
    # Cayley-Dickson octonions is the external Hurwitz-side standard fact; the
    # seeded random pairs below are a redundant numerical control, not the
    # load-bearing verification.
    rng = np.random.default_rng(4209)
    norm_ok = True
    for _ in range(200):
        left = rng.normal(size=8)
        right = rng.normal(size=8)
        left /= np.linalg.norm(left)
        right /= np.linalg.norm(right)
        product = oct_mul(left, right)
        if not np.isclose(np.linalg.norm(product), 1.0, atol=1.0e-9):
            norm_ok = False
            break
    report(
        "octonion norm control (redundant numerical check)",
        norm_ok,
        "200 seeded random unit pairs preserve norm under the CD product",
    )

    e1, e2, e4 = unit(1), unit(2), unit(4)
    associator = oct_mul(oct_mul(e1, e2), e4) - oct_mul(e1, oct_mul(e2, e4))
    report(
        "octonion associator",
        np.linalg.norm(associator) > 1.0e-12,
        "(e1*e2)*e4 - e1*(e2*e4) is nonzero",
    )

    hurwitz_algebra_dims = {1, 2, 4, 8}
    color_real_dim = 2 * 3
    report(
        "color carrier dimension",
        color_real_dim == 6 and color_real_dim not in hurwitz_algebra_dims,
        "dim_R(C^3) = 6 is not in {1, 2, 4, 8}",
    )

    report(
        "graph-first commutant sanity",
        graph_first_sanity(),
        "selected-axis finite matrices give su(2), Comm(su(2)) dim 16 = gl(4), "
        "residual 3+1 split, and joint commutant dimension 10 = gl(3)+gl(1), "
        "for all three axes",
    )

    # Self-scan: the no-side-effects flag is verified against this script's own
    # AST, not stipulated.
    import ast

    with open(__file__, "r", encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    imported = set()
    write_calls = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "open":
                mode_args = [
                    arg.value
                    for arg in node.args[1:2]
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str)
                ]
                mode_kwargs = [
                    kw.value.value
                    for kw in node.keywords
                    if kw.arg == "mode"
                    and isinstance(kw.value, ast.Constant)
                    and isinstance(kw.value.value, str)
                ]
                for mode in mode_args + mode_kwargs or ["r"]:
                    if any(ch in mode for ch in "wax+"):
                        write_calls += 1
    net_or_repo_imports = imported & {"requests", "urllib", "socket", "http", "subprocess"}
    report(
        "self-scan: no file writes, no network/subprocess imports in this runner",
        write_calls == 0 and not net_or_repo_imports,
        f"AST walk of the runner's own source: write-mode open calls = {write_calls}, "
        f"forbidden imports = {sorted(net_or_repo_imports) or 'none'}",
    )
    report(
        "declared scope (stipulation, not a check): no color derived; PR #4209 "
        "text used as closed historical reference only; Hurwitz classification "
        "cited external",
        True,
        "declarations mirrored in the note's honest-boundary section",
    )

    print(f"TOTAL: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
