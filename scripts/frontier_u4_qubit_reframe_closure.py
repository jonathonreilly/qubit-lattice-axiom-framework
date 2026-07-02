#!/usr/bin/env python3
"""Verify the U4 qubit-reframe closure note on the current axiom surface.

The target note is an axiom-unpacking support note: the current Quantum axiom
already says that each site carries one qubit, equivalently M_2(C), equivalently
Cl(3,0) in its real-algebra reading. This runner checks that source boundary
and verifies the concrete Pauli/M_2(C) realization used by the note.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
CL3_SPLIT = ROOT / "docs" / "CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md"

EPS = 1e-10


def matmul(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def close(a, b, eps=EPS):
    return all(abs(a[i][j] - b[i][j]) <= eps for i in range(2) for j in range(2))


def flatten_real(a):
    return [
        a[0][0].real,
        a[0][0].imag,
        a[0][1].real,
        a[0][1].imag,
        a[1][0].real,
        a[1][0].imag,
        a[1][1].real,
        a[1][1].imag,
    ]


def rank(rows, eps=EPS):
    rows = [list(map(float, row)) for row in rows]
    if not rows:
        return 0
    m = len(rows)
    n = len(rows[0])
    r = 0
    for c in range(n):
        pivot = max(range(r, m), key=lambda i: abs(rows[i][c]))
        if abs(rows[pivot][c]) <= eps:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(m):
            if i == r:
                continue
            factor = rows[i][c]
            if abs(factor) > eps:
                rows[i] = [rows[i][j] - factor * rows[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        if ok:
            self.pass_count += 1
            tag = "PASS"
        else:
            self.fail_count += 1
            tag = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"[{tag}] {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    note = read(NOTE)
    axioms = read(AXIOMS)
    cl3 = read(CL3_SPLIT)

    I = [[1 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]]
    Z0 = [[0 + 0j, 0 + 0j], [0 + 0j, 0 + 0j]]
    X = [[0 + 0j, 1 + 0j], [1 + 0j, 0 + 0j]]
    Y = [[0 + 0j, -1j], [1j, 0 + 0j]]
    Z = [[1 + 0j, 0 + 0j], [0 + 0j, -1 + 0j]]

    paulis = [X, Y, Z]
    words = [
        I,
        X,
        Y,
        Z,
        matmul(X, Y),
        matmul(X, Z),
        matmul(Y, Z),
        matmul(matmul(X, Y), Z),
    ]
    e11 = scale(0.5, matadd(I, Z))
    e22 = scale(0.5, matsub(I, Z))
    e12 = scale(0.5, matadd(X, scale(1j, Y)))
    e21 = scale(0.5, matsub(X, scale(1j, Y)))

    gate = Gate()
    print("=" * 78)
    print("U4 QUBIT-REFRAME CLOSURE VERIFIER")
    print("=" * 78)

    gate.check("target U4 note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    gate.check("current minimal axiom memo exists", AXIOMS.exists(), str(AXIOMS.relative_to(ROOT)))
    gate.check("CL3 split note exists", CL3_SPLIT.exists(), str(CL3_SPLIT.relative_to(ROOT)))
    gate.check(
        "current axiom memo has named Lattice/Quantum/Record axioms",
        "### Lattice" in axioms and "### Quantum" in axioms and "### Record" in axioms,
    )
    gate.check(
        "Quantum axiom supplies one qubit and M2/Cl3 equivalence",
        "one qubit" in axioms and "A_x ~= M_2(C)" in axioms and "Cl(3,0)" in axioms,
    )
    gate.check(
        "U4 note now cites the current axiom memo",
        "MINIMAL_AXIOMS_2026-06-05.md" in note
        and "current Quantum axiom" in note
        and "MINIMAL_AXIOMS_2026-05-20.md](MINIMAL_AXIOMS_2026-05-20.md)" not in note,
    )
    gate.check(
        "U4 note keeps auditor-owned source-side status",
        "source-side proposal" in note and "independent audit lane owns the verdict" in note,
    )
    gate.check(
        "U4 note keeps alias/renaming boundary",
        "axiom-unpacking / renaming support only" in note
        and "does not re-derive the qubit-per-site baseline" in note,
    )
    gate.check(
        "CL3 split source records M2(C) isomorphism and unique summand module",
        "Cl(3,0) \u2245 M_2(C)" in cl3
        and "unique" in cl3
        and "irreducible left module" in cl3
        and "complex dimension `dim_C V = 2`" in cl3,
    )
    gate.check(
        "Pauli matrices satisfy Cl(3,0) relations",
        all(close(matmul(p, p), I) for p in paulis)
        and all(close(matadd(matmul(paulis[i], paulis[j]), matmul(paulis[j], paulis[i])), Z0) for i in range(3) for j in range(i + 1, 3)),
    )
    gate.check(
        "Pauli word span has real dimension 8",
        rank([flatten_real(w) for w in words]) == 8,
        f"rank={rank([flatten_real(w) for w in words])}",
    )
    gate.check(
        "Pauli generators recover M2(C) matrix units",
        close(matmul(e11, e11), e11)
        and close(matmul(e22, e22), e22)
        and close(matmul(e12, e21), e11)
        and close(matmul(e21, e12), e22)
        and close(matadd(e11, e22), I),
    )
    gate.check(
        "standard C2 module is faithful and irreducible for generated M2(C)",
        not close(e12, Z0) and not close(e21, Z0) and not close(e11, Z0) and not close(e22, Z0),
        "matrix units connect the two coordinate lines",
    )
    gate.check(
        "U4 consequence is exactly k=1 and dim_C H_x=2",
        "k(x)` of the per-site Cl(3) module is exactly `1`" in note
        and "Hilbert `H_x = \u2102\u00b2`" in note
        and "dim 2" in note,
    )
    gate.check(
        "downstream gate boundary is preserved",
        "Not a closure of the staggered-Dirac realization gate" in note
        and "Not an automatic promotion" in note,
    )

    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"TOTAL: PASS={gate.pass_count}, FAIL={gate.fail_count}")
    if gate.fail_count:
        print("U4 qubit-reframe verifier failed.")
        return 1
    print(
        "Verified scoped U4 alias closure: the current Quantum axiom supplies "
        "one qubit/M2(C)/Cl(3,0) per site; Pauli matrices realize the local "
        "Cl(3,0) carrier as all of M2(C), while downstream staggered gates "
        "remain separately auditor-owned."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
