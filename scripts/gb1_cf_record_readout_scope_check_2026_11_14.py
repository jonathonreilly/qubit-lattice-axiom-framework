#!/usr/bin/env python3
"""Checks built to refute the statements of
docs/SU2_NEIGHBORHOOD_PROPAGATION_RECORD_READOUT_SCOPE_CHECK_2026-11-08.md.

The scope note states: a conditional record relay along a supplied path; an
adjacent-gate electric instrument that works on the whole active link code,
with external entanglement, and commutes with the endpoint gauge action;
and two record-first counterexamples (the two phase states J0, J1 have equal
computational-basis record ensembles but opposite electric values; dephased
J3 has code overlap one half).

This runner rebuilds those statements with dense numpy state vectors, apart
from the exact-rational implementation in
scripts/gb1_cf_neighborhood_record_readout_exact_2026_11_08.py. It does not
re-implement that runner's controlled-reversal experiment or its two-work-qubit
decoder; the scope note cites them there.

Each control perturbs one statement and must make its check fail. The run
exits 1 if any check fails or any control's mutant passes.
"""
from __future__ import annotations

import itertools
import sys

import numpy as np

AUDIT_TIMEOUT_SEC = 120

TOL = 1e-12
PASS = 0
FAIL = 0
N_SITES = 5  # site 0 is the fresh output; sites 1..4 carry the link code


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
    check(f"control rejects mutant: {name}", not mutant_holds, detail)


# --- states on sites 0..4 --------------------------------------------------

def basis(bits: str) -> np.ndarray:
    """bits[s] is the value at site s, for sites 0..len(bits)-1."""
    v = np.zeros(2 ** len(bits), dtype=complex)
    v[int(bits, 2)] = 1.0
    return v


def data_word(word: str) -> np.ndarray:
    return basis(word)


R2 = 1 / np.sqrt(2)


def code_columns() -> list[np.ndarray]:
    e1, e2, e3, e4 = (data_word(w) for w in ("1000", "0100", "0010", "0001"))
    return [
        R2 * (e1 + e4),
        R2 * (e1 - e4),
        R2 * (e2 - e3),
        R2 * (data_word("1100") - data_word("0011")),
        R2 * (e2 + e3),
    ]


def with_output(bit: str, data: np.ndarray) -> np.ndarray:
    return np.kron(basis(bit), data)


# --- gates ----------------------------------------------------------------

X1 = np.array([[0, 1], [1, 0]], dtype=complex)
H1 = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
V1 = (np.eye(2) + X1) / 2 + 1j * (np.eye(2) - X1) / 2


def onsite(U: np.ndarray, s: int, n: int = N_SITES) -> np.ndarray:
    out = np.array([[1.0 + 0j]])
    for k in range(n):
        out = np.kron(out, U if k == s else np.eye(2))
    return out


def permutation_gate(f, n: int = N_SITES) -> np.ndarray:
    dim = 2 ** n
    M = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        bits = [int(b) for b in format(i, f"0{n}b")]
        M[int("".join(map(str, f(bits))), 2), i] = 1.0
    return M


def swap(a: int, b: int) -> np.ndarray:
    def f(bits):
        bits = bits[:]
        bits[a], bits[b] = bits[b], bits[a]
        return bits
    return permutation_gate(f)


def cx(c: int, t: int) -> np.ndarray:
    def f(bits):
        bits = bits[:]
        bits[t] ^= bits[c]
        return bits
    return permutation_gate(f)


def controlled(U: np.ndarray, c: int, t: int, n: int = N_SITES) -> np.ndarray:
    P0 = np.array([[1, 0], [0, 0]], dtype=complex)
    P1 = np.array([[0, 0], [0, 1]], dtype=complex)
    a = np.array([[1.0 + 0j]])
    b = np.array([[1.0 + 0j]])
    for k in range(n):
        a = np.kron(a, P0 if k == c else np.eye(2))
        b = np.kron(b, P1 if k == c else (U if k == t else np.eye(2)))
    return a + b


def gate_matrix(g) -> np.ndarray:
    kind = g[0]
    if kind == "S":
        return swap(g[1], g[2])
    if kind == "CX":
        return cx(g[1], g[2])
    if kind == "CV":
        return controlled(V1, g[1], g[2])
    if kind == "CVd":
        return controlled(V1.conj().T, g[1], g[2])
    if kind == "H":
        return onsite(H1, g[1])
    if kind == "X":
        return onsite(X1, g[1])
    raise ValueError(g)


W = [("S", 3, 4), ("S", 2, 3), ("CX", 1, 2), ("H", 1), ("CX", 3, 4)]
W_DAGGER = [("CX", 3, 4), ("H", 1), ("CX", 1, 2), ("S", 2, 3), ("S", 3, 4)]
TOFFOLI_120 = [("CV", 1, 0), ("CX", 2, 1), ("CVd", 1, 0), ("CX", 2, 1),
               ("S", 2, 1), ("CV", 1, 0), ("S", 2, 1)]
COPY = ([("X", 1), ("X", 4), ("S", 3, 4), ("S", 2, 3)] + TOFFOLI_120
        + [("S", 2, 3), ("S", 3, 4), ("X", 1), ("X", 4), ("X", 0)])
CIRCUIT = W + COPY + W_DAGGER


def unitary(gates) -> np.ndarray:
    U = np.eye(2 ** N_SITES, dtype=complex)
    for g in gates:
        U = gate_matrix(g) @ U
    return U


def instrument_holds(gates) -> bool:
    U = unitary(gates)
    for mu, col in enumerate(code_columns()):
        want = with_output("0" if mu == 0 else "1", col)
        if not np.allclose(U @ with_output("0", col), want, atol=TOL):
            return False
    return True


# --- endpoint gauge action on the five-state link --------------------------

SIG = [X1, np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]


def su2(rng) -> np.ndarray:
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    return q[3] * np.eye(2) + 1j * sum(q[a] * SIG[a] for a in range(3))


def coords(g: np.ndarray) -> np.ndarray:
    """g = x4 I + i sum_a x_a sigma_a -> (x1, x2, x3, x4)."""
    x4 = np.trace(g).real / 2
    xa = [(np.trace(SIG[a] @ g) / 2j).real for a in range(3)]
    return np.array(xa + [x4])


def endpoint_action(hl: np.ndarray, hr: np.ndarray) -> np.ndarray:
    """Matrix of x -> coords(hl g(x) hr^dagger) on R^4, embedded as 1 + R on the link."""
    R = np.zeros((4, 4))
    for k in range(4):
        x = np.zeros(4)
        x[k] = 1.0
        g = x[3] * np.eye(2) + 1j * sum(x[a] * SIG[a] for a in range(3))
        R[:, k] = coords(hl @ g @ hr.conj().T)
    T = np.eye(5)
    T[1:, 1:] = R
    return T


# --- permanent-record relay ------------------------------------------------

NEIGHBORS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def relay(path, extra=None):
    """Return, for each formed site, the distribution of the copy law."""
    records = {path[0]: "P"}
    if extra:
        records.update(extra)
    laws = []
    for x in path[1:]:
        nbrs = [tuple(x[i] + d[i] for i in range(3)) for d in NEIGHBORS]
        labels = [records[y] for y in nbrs if y in records]
        if not labels:
            raise ValueError("path step with no recorded neighbor")
        law = {lab: labels.count(lab) / len(labels) for lab in set(labels)}
        laws.append(law)
        records[x] = max(law, key=law.get) if len(law) == 1 else "mixed"
    return laws


def main() -> int:
    print("=" * 78)
    print("Scope check: neighborhood record relay and electric record readout")
    print("=" * 78)

    cols = code_columns()
    G = np.array([[np.vdot(a, b) for b in cols] for a in cols])
    check("five code columns are orthonormal in C^16", np.allclose(G, np.eye(5), atol=TOL))

    print("\nA. Electric instrument on the active code (scope N1 lines 3-4, N5 per element and per site)")
    pairs = [g for g in CIRCUIT if len(g) == 3]
    single = [g for g in CIRCUIT if len(g) == 2]
    check("19 pair gates and 7 onsite gates", len(pairs) == 19 and len(single) == 7, f"{len(pairs)} + {len(single)}")
    check("every pair gate acts on adjacent sites", all(abs(g[1] - g[2]) == 1 for g in pairs))
    check("the three TOFFOLI_120 lines equal Toffoli(controls 1,2; target 0)",
          np.allclose(unitary(TOFFOLI_120),
                      permutation_gate(lambda b: [b[0] ^ (b[1] & b[2])] + b[1:]), atol=TOL))
    check("circuit maps |0>_out J|mu> to |b>_out J|mu>, b = 0 for mu = 0 and 1 otherwise",
          instrument_holds(CIRCUIT))
    rng = np.random.default_rng(20261114)
    U = unitary(CIRCUIT)
    r = rng.normal(size=(5, 2)) + 1j * rng.normal(size=(5, 2))
    inp = sum(np.kron(with_output("0", cols[m]), r[m]) for m in range(5))
    out = np.kron(U, np.eye(2)) @ inp
    want = np.kron(with_output("0", cols[0]), r[0]) + sum(
        np.kron(with_output("1", cols[m]), r[m]) for m in range(1, 5))
    check("with an entangled external qubit the output is |0>J|0>r0 + |1> sum_mu J|mu> r_mu",
          np.allclose(out, want, atol=TOL))
    control("dropping the last CX of the decoder W",
            instrument_holds(W[:-1] + COPY + W_DAGGER))
    control("replacing CV-dagger by CV inside the Toffoli",
            instrument_holds(W + [("CV", 1, 0) if g[0] == "CVd" else g for g in COPY] + W_DAGGER))

    print("\nB. Endpoint gauge action (scope N5, per block)")
    P0 = np.diag([1.0, 0, 0, 0, 0])
    P1 = np.eye(5) - P0
    ok, orth = True, True
    worst_single = 0.0
    single_proj = np.diag([0, 1.0, 0, 0, 0])
    for _ in range(20):
        T = endpoint_action(su2(rng), su2(rng))
        orth &= np.allclose(T.T @ T, np.eye(5), atol=1e-10) and abs(np.linalg.det(T) - 1) < 1e-10
        ok &= np.allclose(T @ P0, P0 @ T, atol=1e-10) and np.allclose(T @ P1, P1 @ T, atol=1e-10)
        worst_single = max(worst_single, np.abs(T @ single_proj - single_proj @ T).max())
    check("endpoint actions act as 1 + SO(4) on the link", orth)
    check("P0 and P1 commute with 20 random endpoint actions", ok)
    control("the projector onto |1> alone commutes with the same actions", worst_single < 1e-6,
            f"largest commutator entry {worst_single:.3f}")

    print("\nC. Record-first counterexamples (scope N1 lines 5-6)")
    e1, e4 = data_word("1000"), data_word("0001")
    q0 = np.outer(cols[0], cols[0].conj())
    all_ok_pop, all_ok_prob = True, True
    for phi in np.linspace(0, 2 * np.pi, 7)[:-1]:
        psi = R2 * (e1 + np.exp(1j * phi) * e4)
        all_ok_pop &= np.allclose(np.abs(psi) ** 2, np.abs(cols[0]) ** 2, atol=TOL)
        p_live = np.vdot(psi, q0 @ psi).real
        p_circ = np.linalg.norm((U @ with_output("0", psi))[:16]) ** 2
        all_ok_prob &= abs(p_live - (1 + np.cos(phi)) / 2) < TOL and abs(p_circ - p_live) < TOL
    check("psi_phi has the same computational populations for six phases", all_ok_pop)
    check("Pr(E^2 = 0) = (1 + cos phi)/2, from Q0 and from the circuit's output", all_ok_prob)
    p0 = np.vdot(cols[0], q0 @ cols[0]).real
    p1 = np.vdot(cols[1], q0 @ cols[1]).real
    check("J0 and J1 give opposite certain electric values", abs(p0 - 1) < TOL and abs(p1) < TOL, f"{p0:.15f}, {p1:.15f}")
    deph = [np.diag(np.abs(c) ** 2) for c in cols]
    check("after computational-basis recording, J0 and J1 have the same density matrix",
          np.allclose(deph[0], deph[1], atol=TOL))
    Uo = U
    rho_out = Uo @ np.kron(np.diag([1.0, 0]), deph[0]) @ Uo.conj().T
    check("the circuit applied to that recorded ensemble gives output odds 1/2 : 1/2",
          abs(np.trace(rho_out[:16, :16]).real - 0.5) < TOL)
    control("without recording, J0 and J1 already share their density matrix",
            np.allclose(np.outer(cols[0], cols[0].conj()), np.outer(cols[1], cols[1].conj()), atol=TOL))
    Q = sum(np.outer(c, c.conj()) for c in cols)
    overlap = np.trace(Q @ deph[3]).real
    check("dephased J3 has code overlap Tr(Q rho) = 1/2", abs(overlap - 0.5) < TOL, f"{overlap:.15f}")
    partner = R2 * (data_word("1100") + data_word("0011"))
    check("the symmetric partner (1100 + 0011)/sqrt2 is orthogonal to the code",
          np.allclose(Q @ partner, 0, atol=TOL))
    control("live J3 also has code overlap 1/2",
            abs(np.vdot(cols[3], Q @ cols[3]).real - 0.5) < TOL)

    print("\nD. Conditional record relay (scope N1 line 1, N5 lattice-wide)")
    path = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 2, 0), (1, 2, 0), (2, 2, 0),
            (2, 2, 1), (2, 1, 1), (2, 0, 1), (2, 0, 2), (3, 0, 2), (4, 0, 2), (5, 0, 2)]
    check("test path is self-avoiding and adjacent", len(set(path)) == len(path) and all(
        sum(abs(a - b) for a, b in zip(p, q)) == 1 for p, q in zip(path, path[1:])))
    check("some step has two recorded neighbors (the path approaches itself)",
          any(sum(tuple(x[i] + d[i] for i in range(3)) in set(path[:k]) for d in NEIGHBORS) > 1
              for k, x in enumerate(path[1:], start=1)))
    laws = relay(path)
    check("every formed site has law delta_P, so P is copied along all 13 steps", all(l == {"P": 1.0} for l in laws))
    rot = lambda v: (-v[1], v[0], v[2])
    moved = [tuple(a + b for a, b in zip(rot(p), (7, -3, 2))) for p in path]
    check("the same holds after a cubic rotation and a translation of the experiment",
          all(l == {"P": 1.0} for l in relay(moved)))
    control("with a second initial record Q beside the path the relay still copies only P",
            all(l == {"P": 1.0} for l in relay(path, extra={(1, -1, 0): "Q"})))

    print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL}")
    print("Scope: double-precision checks of finite statements; the exact proofs are in the theorem note."
          " The controlled-reversal experiment and the two-work-qubit decoder are checked only by"
          " scripts/gb1_cf_neighborhood_record_readout_exact_2026_11_08.py.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
