#!/usr/bin/env python3
"""Verify root-SU2 scale transport on the graph-first V3 gauge carrier."""

from itertools import permutations
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent.parent

NOTE = ROOT / "docs" / "GBARE_ROOT_SU2_SCALE_TRANSPORT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md"
GRAPH_FIRST_SU3_NOTE = ROOT / "docs" / "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md"
NATIVE_GAUGE_NOTE = ROOT / "docs" / "NATIVE_GAUGE_CLOSURE_NOTE.md"
TRACE_BRIDGE_NOTE = ROOT / "docs" / "STAGGERED_GBARE_TRACE_SURFACE_BRIDGE_NOTE_2026-06-06.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label, ok, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title):
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def squashed(path):
    return " ".join(path.read_text(encoding="utf-8").split())


def has_all(text, snippets):
    return all(" ".join(snippet.split()) in text for snippet in snippets)


def close(a, b, tol=1e-10):
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) < tol


def comm(a, b):
    return a @ b - b @ a


def gram(gens):
    return np.array([[np.trace(a @ b).real for b in gens] for a in gens])


def E(i, j, n=3):
    out = np.zeros((n, n), dtype=complex)
    out[i, j] = 1
    return out


def root_su2(i, j):
    jx = (E(i, j) + E(j, i)) / 2
    jy = (-1j * E(i, j) + 1j * E(j, i)) / 2
    jz = (E(i, i) - E(j, j)) / 2
    return [jx, jy, jz]


def pauli_half():
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return [sx / 2, sy / 2, sz / 2]


def active_subblock(mat, i, j):
    return mat[np.ix_([i, j], [i, j])]


def exp_diag_from_diag_entries(entries, theta):
    return np.diag(np.exp(1j * theta * np.array(entries, dtype=float)))


section("Part 1: source surfaces and boundaries")

for path in [NOTE, GRAPH_FIRST_SU3_NOTE, NATIVE_GAUGE_NOTE, TRACE_BRIDGE_NOTE]:
    check(f"source file exists: {path.relative_to(ROOT)}", path.exists())

note_text = squashed(NOTE)
graph_text = squashed(GRAPH_FIRST_SU3_NOTE)
native_text = squashed(NATIVE_GAUGE_NOTE)
bridge_text = squashed(TRACE_BRIDGE_NOTE)

note_snippets = [
    "does not apply an audit verdict",
    "does not promote a parent `g_bare` claim",
    "root `SU(2)` subgroup of the compact unitary `SU(3)` representation",
    "not another root `su(2)` embedding with the same bracket",
    "Species-label bijections remain irrelevant",
]
for snippet in note_snippets:
    check(f"note contains: {snippet}", has_all(note_text, [snippet]))

graph_snippets = [
    "embedded Gell-Mann generators close to `su(3)`",
    "closes the structural graph-first route to `su(3)`",
    "retained graph-first surface",
]
for snippet in graph_snippets:
    check(f"graph-first source contains: {snippet}", has_all(graph_text, [snippet]))

native_snippets = [
    "native cubic Cl(3) / su(2)  plus  graph-first structural su(3)",
    "Wilson gauge dynamics",
    "phenomenology",
]
for snippet in native_snippets:
    check(f"native-gauge source contains: {snippet}", has_all(native_text, [snippet]))

bridge_snippets = [
    "per-site-to-gauge SU(2) normalization transport remains the actual scale gate",
    "not load-bearing for this trace-normalization statement",
    "Physical-color and EW matching claims remain outside",
]
for snippet in bridge_snippets:
    check(f"trace bridge source contains: {snippet}", has_all(bridge_text, [snippet]))

section("Part 2: per-site Pauli/2 spin-double-cover scale")

P = pauli_half()
zero2 = np.zeros((2, 2), dtype=complex)
ident2 = np.eye(2, dtype=complex)
for idx, gen in enumerate(P):
    check(f"Pauli/2 generator {idx + 1} is Hermitian", close(gen, gen.conj().T))

check("[sx/2, sy/2] = i sz/2", close(comm(P[0], P[1]), 1j * P[2]))
check("[sy/2, sz/2] = i sx/2", close(comm(P[1], P[2]), 1j * P[0]))
check("[sz/2, sx/2] = i sy/2", close(comm(P[2], P[0]), 1j * P[1]))
check("Pauli/2 Gram is 1/2 delta", close(gram(P), 0.5 * np.eye(3)))

pauli_jz_entries = [0.5, -0.5]
check("per-site exp(4 pi i Jz) = I", close(exp_diag_from_diag_entries(pauli_jz_entries, 4 * np.pi), ident2))
check("per-site exp(2 pi i Jz) is nontrivial", not close(exp_diag_from_diag_entries(pauli_jz_entries, 2 * np.pi), ident2))

section("Part 3: root SU(2) subgroups inside V3")

root_pairs = [(0, 1), (1, 2), (0, 2)]
for i, j in root_pairs:
    gens = root_su2(i, j)
    jx, jy, jz = gens
    label = f"root ({i},{j})"

    for idx, gen in enumerate(gens):
        check(f"{label} generator {idx + 1} is Hermitian", close(gen, gen.conj().T))

    check(f"{label}: [Jx,Jy] = i Jz", close(comm(jx, jy), 1j * jz))
    check(f"{label}: [Jy,Jz] = i Jx", close(comm(jy, jz), 1j * jx))
    check(f"{label}: [Jz,Jx] = i Jy", close(comm(jz, jx), 1j * jy))
    check(f"{label}: trace Gram is 1/2 delta", close(gram(gens), 0.5 * np.eye(3)))

    eigs = sorted(round(x.real, 10) for x in np.linalg.eigvals(jz))
    check(f"{label}: Jz spectrum is -1/2, 0, +1/2", eigs == [-0.5, 0.0, 0.5], detail=str(eigs))

    diag_entries = np.diag(jz).real
    check(f"{label}: exp(4 pi i Jz) = I_3", close(exp_diag_from_diag_entries(diag_entries, 4 * np.pi), np.eye(3)))
    check(f"{label}: exp(2 pi i Jz) is nontrivial", not close(exp_diag_from_diag_entries(diag_entries, 2 * np.pi), np.eye(3)))

    for idx, expected in enumerate(P):
        check(
            f"{label}: active two-plane generator {idx + 1} is Pauli/2",
            close(active_subblock(gens[idx], i, j), expected),
        )

    for c in [1.0, 0.5, 2.0, 3.0]:
        scaled = [c * g for g in gens]
        bracket_ok = close(comm(scaled[0], scaled[1]), 1j * scaled[2])
        expected = c == 1.0
        check(
            f"{label}: positive scaling c={c:g} preserves unit su2 bracket iff c=1",
            bracket_ok == expected,
        )

section("Part 4: conjugacy and trace-surface controls")

T01 = root_su2(0, 1)
all_perm_ok = True
for perm in permutations(range(3)):
    Q = np.zeros((3, 3), dtype=complex)
    for row, col in enumerate(perm):
        Q[row, col] = 1
    conj_gens = [Q @ g @ Q.conj().T for g in T01]
    ok = close(gram(conj_gens), 0.5 * np.eye(3))
    all_perm_ok = all_perm_ok and ok
    check(f"permutation {perm} preserves root SU2 trace scale", ok)

check("all graph label permutations preserve the root SU2 scale", all_perm_ok)

full_trace_gens = [np.kron(g, np.eye(2)) for g in T01]
check("full matter tensor trace doubles the gauge trace", close(gram(full_trace_gens), np.eye(3)))
check("V3 gauge trace is half the full matter trace", close(gram(T01), 0.5 * gram(full_trace_gens)))

section("Part 5: lane conclusion")

scale_transport_closed_in_this_packet = all_perm_ok and all(
    close(active_subblock(root_su2(i, j)[k], i, j), P[k])
    for i, j in root_pairs
    for k in range(3)
)
parent_promotion_claimed = "parent `g_bare = 1` theorem" in note_text and "does not claim" in note_text

check("root SU2 scale transport closes inside the finite V3 packet", scale_transport_closed_in_this_packet)
check("packet does not claim parent g_bare promotion", parent_promotion_claimed)
check("physical color naming is outside the proof", has_all(note_text, ["physical-color naming", "is derived here"]))
check("Wilson and beta claims are outside the proof", has_all(note_text, ["No Wilson action, beta=6", "is derived here"]))

print("\n" + "=" * 88)
print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
print("=" * 88)

sys.exit(1 if FAIL_COUNT else 0)
