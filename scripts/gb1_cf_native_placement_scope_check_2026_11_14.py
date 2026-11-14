#!/usr/bin/env python3
"""Checks built to refute the statements of
docs/SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_SCOPE_CHECK_2026-11-08.md.

The scope note states two finite capacity counterexamples under ordinary
tensor composition, a four-qubit realization of the five-state link, and
per-cell counts of the spacing-five placement. This runner recomputes each
one by a path separate from scripts/gb1_cf_native_placement_exact_2026_11_08.py:
dense numpy linear algebra for the code and for brute-force Gauss
invariants on small graphs, a character (Catalan) count, and GF(2)
elimination for the cycle rank of the two cubes.

Each control perturbs one statement and must make its check fail. The run
exits 1 if any check fails or any control's mutant passes.
"""
from __future__ import annotations

import itertools
import sys
from math import comb

import numpy as np

AUDIT_TIMEOUT_SEC = 120

TOL = 1e-10
PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: object = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail != "" else ""))
    return ok


def control(name: str, mutant_holds: bool, detail: object = "") -> None:
    """A control passes when the perturbed statement is rejected."""
    check(f"control rejects mutant: {name}", not mutant_holds, detail)


# --- four-qubit link code --------------------------------------------------

def ket(bits: str) -> np.ndarray:
    v = np.zeros(16)
    v[int(bits, 2)] = 1.0
    return v


def code_matrix(j3_sign: float = -1.0) -> np.ndarray:
    """Columns J|0>..J|4> in C^16, positions ordered along the link."""
    e1, e2, e3, e4 = ket("1000"), ket("0100"), ket("0010"), ket("0001")
    r = 1 / np.sqrt(2)
    cols = [
        r * (e1 + e4),
        r * (e1 - e4),
        r * (e2 - e3),
        r * (ket("1100") + j3_sign * ket("0011")),
        r * (e2 + e3),
    ]
    return np.stack(cols, axis=1)


def reversal_permutation() -> np.ndarray:
    F = np.zeros((16, 16))
    for i in range(16):
        bits = format(i, "04b")
        F[int(bits[::-1], 2), i] = 1.0
    return F


K = np.diag([1.0, -1.0, -1.0, -1.0, 1.0])


def code_statements(J: np.ndarray) -> dict[str, bool]:
    F = reversal_permutation()
    Q = J @ J.T
    return {
        "isometry": np.allclose(J.T @ J, np.eye(5), atol=TOL),
        "reversal": np.allclose(F @ J, J @ K, atol=TOL),
        "vacuum_outside": np.allclose(Q @ ket("0000"), 0, atol=TOL),
    }


# --- graphs, GF(2) rank, Gauss invariants ---------------------------------

def open_cube(n: int = 3):
    verts = list(itertools.product(range(n), repeat=3))
    index = {v: i for i, v in enumerate(verts)}
    edges = []
    for v in verts:
        for d in range(3):
            w = list(v)
            w[d] += 1
            if w[d] < n:
                edges.append((index[v], index[tuple(w)]))
    return len(verts), edges


def periodic_cube(n: int = 3):
    verts = list(itertools.product(range(n), repeat=3))
    index = {v: i for i, v in enumerate(verts)}
    edges = []
    for v in verts:
        for d in range(3):
            w = list(v)
            w[d] = (w[d] + 1) % n
            edges.append((index[v], index[tuple(w)]))
    return len(verts), edges


def path_graph(V: int):
    return V, [(i, i + 1) for i in range(V - 1)]


def gf2_rank(rows: list[int]) -> int:
    rank = 0
    rows = [r for r in rows if r]
    while rows:
        pivot = rows.pop()
        rank += 1
        low = pivot & -pivot
        rows = [r ^ pivot if r & low else r for r in rows]
        rows = [r for r in rows if r]
    return rank


def incidence_rank(V: int, edges) -> int:
    rows = [0] * V
    for k, (a, b) in enumerate(edges):
        rows[a] ^= 1 << k
        rows[b] ^= 1 << k
    return gf2_rank(rows)


def connected(V: int, edges) -> bool:
    adj = {i: set() for i in range(V)}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen, todo = {0}, [0]
    while todo:
        x = todo.pop()
        for y in adj[x] - seen:
            seen.add(y)
            todo.append(y)
    return len(seen) == V


def catalan(m: int) -> int:
    return comb(2 * m, m) // (m + 1)


def character_count(V: int, edges) -> int:
    """sum over edge subsets S of prod_v c(deg_S v), c(k)=Catalan(k/2), 0 if k odd."""
    total = 0
    for mask in range(1 << len(edges)):
        deg = [0] * V
        for k, (a, b) in enumerate(edges):
            if mask >> k & 1:
                deg[a] += 1
                deg[b] += 1
        term = 1
        for d in deg:
            if d % 2:
                term = 0
                break
            term *= catalan(d // 2)
        total += term
    return total


def even_subgraphs(V: int, edges) -> int:
    count = 0
    for mask in range(1 << len(edges)):
        deg = [0] * V
        for k, (a, b) in enumerate(edges):
            if mask >> k & 1:
                deg[a] += 1
                deg[b] += 1
        count += all(d % 2 == 0 for d in deg)
    return count


SIGMA = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]


def end_generators():
    """su(2) generators on one five-state link, at its source and its target.

    Basis: index 0 is the scalar; index 1 + 2a + b is g_{ab}. The source acts
    on a by the spin-1/2 representation, the target on b by its dual.
    """
    src, tgt = [], []
    for s in SIGMA:
        A = np.zeros((5, 5), dtype=complex)
        B = np.zeros((5, 5), dtype=complex)
        A[1:, 1:] = np.kron(s / 2, np.eye(2))
        B[1:, 1:] = np.kron(np.eye(2), -s.T / 2)
        src.append(A)
        tgt.append(B)
    return src, tgt


def embed(op: np.ndarray, slot: int, E: int) -> np.ndarray:
    out = np.array([[1.0 + 0j]])
    for k in range(E):
        out = np.kron(out, op if k == slot else np.eye(5))
    return out


def gauss_invariant_dimension(V: int, edges) -> int:
    E = len(edges)
    src, tgt = end_generators()
    M = np.zeros((5 ** E, 5 ** E), dtype=complex)
    for v in range(V):
        for k in range(3):
            G = np.zeros_like(M)
            for slot, (a, b) in enumerate(edges):
                if a == v:
                    G += embed(src[k], slot, E)
                if b == v:
                    G += embed(tgt[k], slot, E)
            M += G.conj().T @ G
    eig = np.linalg.eigvalsh(M)
    return int(np.sum(eig < 1e-8))


def spin_half_invariants(legs: int) -> int:
    dim = 2 ** legs
    M = np.zeros((dim, dim), dtype=complex)
    for s in SIGMA:
        G = np.zeros((dim, dim), dtype=complex)
        for leg in range(legs):
            op = np.array([[1.0 + 0j]])
            for k in range(legs):
                op = np.kron(op, s / 2 if k == leg else np.eye(2))
            G += op
        M += G.conj().T @ G
    return int(np.sum(np.linalg.eigvalsh(M) < 1e-8))


def main() -> int:
    print("=" * 78)
    print("Scope check: native SU(2) placement, finite capacity witnesses")
    print("=" * 78)

    print("\nA. Four-qubit realization of the five-state link (scope N1, row 1)")
    st = code_statements(code_matrix())
    check("J is an isometry from C^5 into C^16 (J^T J = I_5)", st["isometry"])
    check("reversing the four positions realizes K: F J = J K", st["reversal"])
    check("Q = J J^T annihilates |0000>", st["vacuum_outside"])
    mutant = code_statements(code_matrix(j3_sign=+1.0))
    control("J3 = (1100 + 0011)/sqrt2 still satisfies F J = J K", mutant["reversal"])

    print("\nB. Gauss-singlet lower bound, brute force on small graphs")
    small = {
        "double edge (V=2,E=2)": (2, [(0, 1), (0, 1)]),
        "theta (V=2,E=3)": (2, [(0, 1), (0, 1), (0, 1)]),
        "square (V=4,E=4)": (4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
    }
    for name, (V, edges) in small.items():
        E = len(edges)
        brute = gauss_invariant_dimension(V, edges)
        char = character_count(V, edges)
        even = even_subgraphs(V, edges)
        cyc = E - incidence_rank(V, edges)
        check(f"{name}: brute-force invariant dimension equals character count", brute == char, f"{brute} vs {char}")
        check(f"{name}: even subgraphs number 2^(E-V+1) = 2^{cyc}", even == 2 ** cyc == 2 ** (E - V + 1), even)
        check(f"{name}: invariant dimension >= 2^(E-V+1)", brute >= 2 ** (E - V + 1), f"{brute} >= {2 ** (E - V + 1)}")
    check("four spin-1/2 legs carry Catalan(2) = 2 invariants (degree-4 vertex weight)",
          spin_half_invariants(4) == catalan(2) == 2, spin_half_invariants(4))
    V, edges = small["theta (V=2,E=3)"]
    control("bound exponent E-V+2 still below the exact theta count",
            2 ** (len(edges) - V + 2) <= gauss_invariant_dimension(V, edges),
            f"2^{len(edges) - V + 2} vs {gauss_invariant_dimension(V, edges)}")

    print("\nC. The two capacity counterexamples (scope N1, row 2; theorem section 6)")
    for name, (V, edges), expect_E in [
        ("open 3x3x3 cube", open_cube(), 54),
        ("periodic 3x3x3 cube", periodic_cube(), 81),
    ]:
        E = len(edges)
        r = incidence_rank(V, edges)
        cyc = E - r
        check(f"{name}: V = 27 and E = {expect_E}, so the link space has dimension 5^{expect_E}",
              V == 27 and E == expect_E, f"V={V}, E={E}")
        check(f"{name}: connected, GF(2) incidence rank V-1 = 26", connected(V, edges) and r == V - 1, r)
        check(f"{name}: Gauss sector >= 2^{cyc} > 2^27 = dim of 27 site qubits", 2 ** cyc > 2 ** 27, f"cycle rank {cyc}")
    V, edges = path_graph(27)
    control("a 27-vertex tree also exceeds 27 site qubits",
            2 ** (len(edges) - incidence_rank(V, edges)) > 2 ** V, f"cycle rank {len(edges) - incidence_rank(V, edges)}")

    print("\nD. Spacing-five placement counts (scope N5, per block)")
    residues = list(itertools.product(range(5), repeat=3))
    check("125 phase residues (Z/5)^3", len(residues) == 125)
    cell = set(itertools.product(range(5), repeat=3))
    active = {tuple(t if k == d else 0 for k in range(3)) for d in range(3) for t in range(1, 5)}
    check("the three outgoing coarse edges of a cell have 12 interior sites, all in the cell",
          len(active) == 12 and active <= cell)
    check("113 spectators among the 125 native sites of a cell", len(cell - active) == 113)

    print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
    print("Scope: finite counts and small-graph brute force. The general lower bound is the theorem's"
          " proof; this run checks its instances and cannot test restricted sectors or other composition rules.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
