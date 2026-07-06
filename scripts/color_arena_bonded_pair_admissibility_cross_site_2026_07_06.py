#!/usr/bin/env python3
"""Finite checks for the bonded-pair admissibility arena note.

Self-contained: numpy plus standard-library AST/path reading only.
"""

import ast
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AXIOM_FILE = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
JUNE8_FILE = (
    ROOT
    / "docs"
    / "EDGE_TWO_SITE_FRAMING_SUPPLIES_NO_NATIVE_COLOR_ROUTE_RECORD_TEXT_NARROW_NO_GO_NOTE_2026-06-08.md"
)
TOL = 1.0e-10

passes = 0
fails = 0


def record(label, condition, detail=""):
    global passes, fails
    if condition:
        passes += 1
        print(f"[PASS] {label}")
    else:
        fails += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def close(a, b, tol=TOL):
    return np.linalg.norm(a - b) <= tol


def read_text_file(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def contains_sentence(text, sentence):
    if sentence in text:
        return True
    return " ".join(sentence.split()) in " ".join(text.split())


def su2_from_axis(axis, theta):
    ident = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    pauli = {"x": sx, "y": sy, "z": sz}[axis]
    return np.cos(theta / 2.0) * ident - 1j * np.sin(theta / 2.0) * pauli


def random_su2(rng):
    q = rng.normal(size=4)
    q = q / np.linalg.norm(q)
    a = q[0] + 1j * q[1]
    b = q[2] + 1j * q[3]
    return np.array([[a, b], [-np.conj(b), np.conj(a)]], dtype=complex)


def commutant_dimension(ops, tol=1.0e-9):
    n = ops[0].shape[0]
    columns = []
    for i in range(n):
        for j in range(n):
            basis = np.zeros((n, n), dtype=complex)
            basis[i, j] = 1.0
            columns.append(np.concatenate([(basis @ op - op @ basis).reshape(-1) for op in ops]))
    system = np.stack(columns, axis=1)
    singular = np.linalg.svd(system, compute_uv=False)
    rank = int(np.sum(singular > tol))
    return n * n - rank, singular


def ast_self_scan():
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    disallowed_imports = {
        "socket",
        "subprocess",
        "requests",
        "urllib",
        "http",
        "ftplib",
        "paramiko",
        "shutil",
    }
    bad_imports = []
    bad_opens = []
    bad_writes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in disallowed_imports:
                    bad_imports.append(alias.name)
        if isinstance(node, ast.ImportFrom) and node.module:
            root = node.module.split(".")[0]
            if root in disallowed_imports:
                bad_imports.append(node.module)
        if isinstance(node, ast.Call):
            func = node.func
            name = func.id if isinstance(func, ast.Name) else None
            attr = func.attr if isinstance(func, ast.Attribute) else None
            if name == "open" or attr == "open":
                mode = "r"
                if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(flag in mode for flag in ("w", "a", "x", "+")):
                    bad_opens.append((node.lineno, mode))
            if attr in {"write_text", "write_bytes"}:
                bad_writes.append((node.lineno, attr))
    record("AST self-scan: no network/subprocess imports", not bad_imports, repr(bad_imports))
    record("AST self-scan: no write-mode open calls", not bad_opens, repr(bad_opens))
    record("AST self-scan: no Path write helpers", not bad_writes, repr(bad_writes))


def main():
    ident2 = np.eye(2, dtype=complex)
    ident4 = np.eye(4, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    swap = np.array(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],
        dtype=complex,
    )
    p_sym = 0.5 * (ident4 + swap)
    p_anti = 0.5 * (ident4 - swap)

    record("SWAP squares to identity", close(swap @ swap, ident4))
    record("SWAP is transpose-self", close(swap, swap.T))
    record("SWAP is adjoint-self", close(swap, swap.conj().T))
    record("Sym projector is idempotent", close(p_sym @ p_sym, p_sym))
    record("Anti projector is idempotent", close(p_anti @ p_anti, p_anti))
    record("Sym/Anti projectors are orthogonal", close(p_sym @ p_anti, np.zeros((4, 4))))
    record("Sym projector has complex rank 3", np.linalg.matrix_rank(p_sym, tol=TOL) == 3)
    record("Anti projector has complex rank 1", np.linalg.matrix_rank(p_anti, tol=TOL) == 1)
    record("Sym block has real dimension 6", 2 * np.linalg.matrix_rank(p_sym, tol=TOL) == 6)

    # Exact, exhaustive form of the diagonal-commutation fact.  The identity
    # S (A tensor B) S = B tensor A is LINEAR in A and in B separately, so
    # verifying it on all 16 pairs of elementary 2x2 matrices proves it for
    # all A, B in End(C^2) exactly -- in particular S (g tensor g) =
    # (g tensor g) S for EVERY g in End(C^2), including all of GL(2), with no
    # sampling and no unitarity assumption.
    exact_flip_ok = True
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    e_ab = np.zeros((2, 2), dtype=complex)
                    e_ab[a, b] = 1.0
                    e_cd = np.zeros((2, 2), dtype=complex)
                    e_cd[c, d] = 1.0
                    lhs = swap @ np.kron(e_ab, e_cd) @ swap
                    rhs = np.kron(e_cd, e_ab)
                    if not np.array_equal(lhs, rhs):
                        exact_flip_ok = False
    record(
        "EXACT: S (A tensor B) S = B tensor A on all 16 elementary pairs "
        "(hence S commutes with g tensor g for every g in End(C^2), by bilinearity)",
        exact_flip_ok,
    )

    rng = np.random.default_rng(20260706)
    for idx in range(3):
        g = random_su2(rng)
        u = np.kron(g, g)
        record(f"control: SWAP commutes with seeded SU(2) sample {idx + 1}", close(swap @ u, u @ swap))
        record(f"control: Sym projector stable for seeded SU(2) sample {idx + 1}", close(u @ p_sym @ u.conj().T, p_sym))

    # Frame-relativity exhibit (load-bearing honesty, not a failure): an
    # INDEPENDENT one-site presentation change g tensor 1 does NOT preserve
    # the split.  The split is canonical relative to the shared presentation;
    # comparing frames across sites is exactly the downstream transport
    # question.
    g_flip = np.array([[0, 1], [1, 0]], dtype=complex)
    h_mix = np.array([[1, 1], [0, 1]], dtype=complex)
    u_one_sided = np.kron(h_mix, ident2)
    moved = np.linalg.norm(u_one_sided @ swap - swap @ u_one_sided) > 1.0e-6
    inv = np.linalg.inv(u_one_sided)
    moved_split = np.linalg.norm(u_one_sided @ p_sym @ inv - p_sym) > 1.0e-6
    record(
        "frame-relativity exhibit: an independent one-site change (g tensor 1) "
        "fails to commute with S and moves the split",
        moved and moved_split,
    )
    record(
        "frame-relativity control: the same g applied diagonally (g tensor g) "
        "preserves the split",
        close(np.kron(g_flip, g_flip) @ p_sym @ np.kron(g_flip, g_flip).conj().T, p_sym),
    )

    e00 = np.array([1, 0, 0, 0], dtype=complex)
    e01p10 = np.array([0, 1 / np.sqrt(2), 1 / np.sqrt(2), 0], dtype=complex)
    e11 = np.array([0, 0, 0, 1], dtype=complex)
    sym_basis = np.stack([e00, e01p10, e11], axis=1)
    record("Sym basis is orthonormal", close(sym_basis.conj().T @ sym_basis, np.eye(3)))
    record("Sym basis lies in +1 SWAP eigenspace", close(swap @ sym_basis, sym_basis))

    jx = 0.5 * (np.kron(sx, ident2) + np.kron(ident2, sx))
    jy = 0.5 * (np.kron(sy, ident2) + np.kron(ident2, sy))
    jz = 0.5 * (np.kron(sz, ident2) + np.kron(ident2, sz))
    j_sym = [sym_basis.conj().T @ op @ sym_basis for op in (jx, jy, jz)]
    casimir = j_sym[0] @ j_sym[0] + j_sym[1] @ j_sym[1] + j_sym[2] @ j_sym[2]
    record("Sym restriction has spin-1 Casimir J^2=2I", close(casimir, 2.0 * np.eye(3)))
    record("Spin generators preserve the Sym block", all(close((ident4 - p_sym) @ op @ sym_basis, np.zeros((4, 3))) for op in (jx, jy, jz)))
    dim_comm, singular = commutant_dimension(j_sym)
    sorted_sv = np.sort(singular)
    gap_ratio = float(sorted_sv[1] / max(sorted_sv[0], 1.0e-300)) if len(sorted_sv) > 1 else float("inf")
    record(
        "Spin-axis negative control commutant has complex dimension 1 (numerical)",
        dim_comm == 1 and (sorted_sv[0] < 1.0e-12) and gap_ratio > 1.0e6,
        f"smallest sv={sorted_sv[0]:.2e}, gap ratio={gap_ratio:.2e}",
    )

    # EXACT commutant for the isomorphism class: the complexified vector
    # representation of so(3) is given by the integer antisymmetric matrices
    # L_x, L_y, L_z.  Exact Gaussian elimination over Q[i] (Python Fractions)
    # computes the commutant dimension with no floating tolerance.  The Sym
    # restriction belongs to this isomorphism class (dimension 3, Casimir 2I
    # above), and commutant dimension is an isomorphism invariant.
    from fractions import Fraction

    lx = [[0, 0, 0], [0, 0, -1], [0, 1, 0]]
    ly = [[0, 0, 1], [0, 0, 0], [-1, 0, 0]]
    lz = [[0, -1, 0], [1, 0, 0], [0, 0, 0]]

    def q_rank(rows):
        # rows: list of length-9 vectors of (Fraction, Fraction) = re, im.
        mat = [list(r) for r in rows]
        rank = 0
        cols = len(mat[0]) if mat else 0
        row_i = 0
        for col in range(cols):
            piv = None
            for r in range(row_i, len(mat)):
                re, im = mat[r][col]
                if re != 0 or im != 0:
                    piv = r
                    break
            if piv is None:
                continue
            mat[row_i], mat[piv] = mat[piv], mat[row_i]
            pre, pim = mat[row_i][col]
            denom = pre * pre + pim * pim
            for r in range(len(mat)):
                if r == row_i:
                    continue
                re, im = mat[r][col]
                if re == 0 and im == 0:
                    continue
                # factor = (re + i im) / (pre + i pim)
                fre = (re * pre + im * pim) / denom
                fim = (im * pre - re * pim) / denom
                for c in range(cols):
                    are, aim = mat[row_i][c]
                    bre, bim = mat[r][c]
                    mat[r][c] = (bre - (fre * are - fim * aim), bim - (fre * aim + fim * are))
            row_i += 1
            rank += 1
            if row_i == len(mat):
                break
        return rank

    constraint_rows = []
    for gen in (lx, ly, lz):
        # [M, L] = 0 gives 9 linear equations in the 9 complex entries of M.
        for i in range(3):
            for j in range(3):
                row = []
                for a in range(3):
                    for b in range(3):
                        # coefficient of M[a][b] in (M L - L M)[i][j]
                        coeff = 0
                        if a == i:
                            coeff += gen[b][j]
                        if b == j:
                            coeff -= gen[i][a]
                        row.append((Fraction(coeff), Fraction(0)))
                constraint_rows.append(row)
    exact_rank = q_rank(constraint_rows)
    record(
        "EXACT: commutant of the integer vector rep of so(3) on C^3 has "
        "complex dimension 1 (Gaussian elimination over Q[i], no tolerances)",
        9 - exact_rank == 1,
        f"exact rank={exact_rank}",
    )

    # T3a consistency witness: a proper cubic rotation about a site acts on
    # the six incident edge arenas by relabeling, with the identity on each
    # internal factor.  Under this action every internal Sym/Anti split is
    # preserved and the internal blocks carry the trivial spatial
    # representation.  The witness exhibits axiom-compatibility; it does not
    # claim the axioms force this action.
    rot_z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])  # proper rotation, order 4
    edges = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    record(
        "witness: rotation matrix is a proper cubic rotation (integer, det +1, order 4)",
        int(round(np.linalg.det(rot_z))) == 1
        and np.array_equal(np.linalg.matrix_power(rot_z, 4), np.eye(3, dtype=int))
        and rot_z.dtype.kind in "il",
    )
    perm = {}
    for e in edges:
        image = tuple(int(v) for v in rot_z @ np.array(e))
        perm[e] = image
    record(
        "witness: the rotation permutes the six incident edges",
        sorted(perm.values()) == sorted(edges),
    )
    # Internal action is the identity on each edge arena by construction; the
    # stacked split projectors are therefore carried edgewise onto the
    # relabeled edges unchanged, and the spatial representation on each
    # internal Sym block is trivial.
    block_diag = {e: p_sym for e in edges}
    carried = {perm[e]: block_diag[e] for e in edges}
    record(
        "witness: the Sym/Anti split is preserved edgewise under relabeling "
        "with trivial internal action",
        all(np.array_equal(carried[e], p_sym) for e in edges),
    )

    axiom_text = read_text_file(AXIOM_FILE)
    june8_text = read_text_file(JUNE8_FILE)
    admissibility_sentence = (
        "For each site, the available possibilities are determined by, and vary with, "
        "the nearest-neighbor conditions."
    )
    reopening_sentence = (
        "A future retained theorem deriving genuine cross-site structure from the axioms "
        "would re-open the framing; the demotion is scoped to the current surface."
    )
    baseline_sentence = (
        "The current Lattice + Quantum + Record baseline and approved primitives do not "
        "supply that content."
    )
    record("Text audit: Admissibility sentence present", contains_sentence(axiom_text, admissibility_sentence))
    record("Text audit: June-8 re-opening residual present", contains_sentence(june8_text, reopening_sentence))
    record("Text audit: June-8 N6 baseline sentence present", contains_sentence(june8_text, baseline_sentence))

    ast_self_scan()

    if fails:
        print(f"TOTAL: {passes} PASS / {fails} FAIL")
        print("DECLARATION: bounded bonded-pair arena check failed; no color, carrier, transport, dynamics, or global obstruction discharge is certified.")
        return 1
    print(f"TOTAL: {passes} PASS / 0 FAIL")
    print("DECLARATION: bounded bonded-pair arena verified; no color, carrier, transport, dynamics, or global obstruction discharge is claimed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
