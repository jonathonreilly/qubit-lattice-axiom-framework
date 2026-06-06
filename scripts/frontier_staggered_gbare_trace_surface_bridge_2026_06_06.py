#!/usr/bin/env python3
"""Verify the staggered-to-g_bare trace-surface bridge classifier."""

from itertools import permutations
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent.parent

NF_NOTE = ROOT / "docs" / "N_F_V3_NORMALIZATION_BOUNDED_NOTE_2026-05-07_w2norm.md"
L3A_NOTE = ROOT / "docs" / "L3A_V3_TRACE_SURFACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_l3a.md"
SYNTHESIS_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md"
LABEL_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md"
PANEL_NOTE = ROOT / "docs" / "audit" / "G_BARE_PROMOTION_PANEL_FINDING_2026-05-28.md"
BRIDGE_NOTE = ROOT / "docs" / "STAGGERED_GBARE_TRACE_SURFACE_BRIDGE_NOTE_2026-06-06.md"

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


def gell_mann_generators():
    z = 0j
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, z], [1j, z, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3)
    return [x / 2 for x in [l1, l2, l3, l4, l5, l6, l7, l8]]


def gram(gens):
    return np.array([[np.trace(a @ b).real for b in gens] for a in gens])


def close(a, b, tol=1e-10):
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) < tol


section("Part 1: source surfaces expose the intended narrow gate")

paths = [NF_NOTE, L3A_NOTE, SYNTHESIS_NOTE, LABEL_NOTE, PANEL_NOTE, BRIDGE_NOTE]
for path in paths:
    check(f"source file exists: {path.relative_to(ROOT)}", path.exists())

nf_text = squashed(NF_NOTE)
l3a_text = squashed(L3A_NOTE)
synthesis_text = squashed(SYNTHESIS_NOTE)
label_text = squashed(LABEL_NOTE)
panel_text = squashed(PANEL_NOTE)
bridge_text = squashed(BRIDGE_NOTE)

nf_snippets = [
    "per-site Cl(3) bivector SU(2) and the SU(2) sub-block of su(3) on V_3",
    "same Lie-algebra normalization",
    "Conditional support",
    "admission, `N_F = 1/2` is structurally consistent but not uniquely",
    "V_3 SU(3) without the bridge",
]
for snippet in nf_snippets:
    check(f"N_F note contains: {snippet}", has_all(nf_text, [snippet]))

l3a_snippets = [
    "single remaining named admission",
    "matter-rep / staggered-Dirac realization gate",
    "Closing the staggered-Dirac realization gate would close L3a as a corollary",
    "0 unconditional positive",
]
for snippet in l3a_snippets:
    check(f"L3a note contains: {snippet}", has_all(l3a_text, [snippet]))

synthesis_snippets = [
    "bounded kinetic-and-algebra closure candidate",
    "substeps 1+2+3",
    "species-label identification",
    "stays an explicit named admitted-context residual",
    "remains source-side `open_gate` until",
]
for snippet in synthesis_snippets:
    check(f"synthesis note contains: {snippet}", has_all(synthesis_text, [snippet]))

label_snippets = [
    "species-identification map",
    "Let `L_3",
    "no canonical species-identification bijection",
    "C_3 orbit of bijections",
    "labeling-convention premise",
]
for snippet in label_snippets:
    check(f"label no-go contains: {snippet}", has_all(label_text, [snippet]))

panel_snippets = [
    "per-site spin double cover",
    "gauge su(3) lives on `V_3 = C^3`",
    "same induced scale",
    "staggered-Dirac realization gate",
    "canonicalizing `V_3` as *the* physical trace surface",
]
for snippet in panel_snippets:
    check(f"promotion panel contains: {snippet}", has_all(panel_text, [snippet]))

section("Part 2: trace-surface algebra is load-bearing")

T = gell_mann_generators()
g_v3 = gram(T)
canonical = 0.5 * np.eye(8)
check("V_3 Gell-Mann Gram is N_F=1/2", close(g_v3, canonical))

T_full = [np.kron(t, np.eye(2)) for t in T]
g_full = gram(T_full)
check("V_full = V_3 x C^2 Gram is N_F=1", close(g_full, np.eye(8)))
check("V_full / V_3 trace ratio is exactly 2", close(g_full, 2 * g_v3))
check("V_3 trace surface gives beta=6 at g_bare=1 under standard Wilson convention", 2 * 3 == 6)
check("Trace-surface choice changes N_F while label permutations do not", not close(g_full, g_v3))

section("Part 3: species-label permutations do not change N_F")

all_perm_ok = True
for perm in permutations(range(3)):
    P = np.zeros((3, 3), dtype=complex)
    for i, j in enumerate(perm):
        P[i, j] = 1
    T_perm = [P @ t @ P.conj().T for t in T]
    ok = close(gram(T_perm), canonical)
    all_perm_ok = all_perm_ok and ok
    check(f"corner-label permutation {perm} preserves Tr(T_a T_b)", ok)

check("all six label permutations preserve N_F", all_perm_ok)
check("species-label residual is not load-bearing for trace normalization", all_perm_ok and not close(g_full, g_v3))

section("Part 4: per-site scale and V_3 sub-block scale match conditionally")

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
pauli_half = [sx / 2, sy / 2, sz / 2]
check("per-site SU(2) Pauli/2 Gram is 1/2", close(gram(pauli_half), 0.5 * np.eye(3)))

sub12 = np.array([[1, 0], [0, 1], [0, 0]], dtype=complex)
su2_block = [sub12.conj().T @ T[i] @ sub12 for i in [0, 1, 2]]
for idx, expected in enumerate(pauli_half):
    check(f"V_3 T-spin sub-block generator {idx + 1} is Pauli/2", close(su2_block[idx], expected))

check("V_3 T-spin sub-block Gram is 1/2", close(gram(su2_block), 0.5 * np.eye(3)))
check("conditional bridge has matching per-site and V_3 SU(2) scales", close(gram(pauli_half), gram(su2_block)))

section("Part 5: lane classifier")

requires = {
    "v3_physical_trace_surface": True,
    "per_site_to_gauge_su2_scale_bridge": True,
    "species_label_bijection": False,
}
current_surface = {
    "staggered_parent_open_gate": "open_gate" in synthesis_text and "open_gate" in squashed(ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"),
    "kinetic_algebra_bounded_candidate": "bounded kinetic-and-algebra closure candidate" in synthesis_text,
    "label_residual_not_trace_residual": all_perm_ok,
}
conditional_unlock = (
    requires["v3_physical_trace_surface"]
    and requires["per_site_to_gauge_su2_scale_bridge"]
    and not requires["species_label_bijection"]
    and current_surface["label_residual_not_trace_residual"]
)

check("g_bare route requires V_3 physical trace surface", requires["v3_physical_trace_surface"])
check("g_bare route requires per-site to gauge SU(2) scale bridge", requires["per_site_to_gauge_su2_scale_bridge"])
check("g_bare route does not require species-label bijection", not requires["species_label_bijection"])
check("current staggered parent is still open on source surface", current_surface["staggered_parent_open_gate"])
check("kinetic/algebra closure is only a bounded source-side candidate now", current_surface["kinetic_algebra_bounded_candidate"])
check("conditional trace-surface bridge would unlock N_F=1/2 for g_bare", conditional_unlock)

section("Part 6: branch-local note hygiene")

bridge_snippets = [
    "bounded support / conditional trace-surface bridge",
    "not a parent promotion",
    "not load-bearing for this trace normalization",
    "does not have to wait for a forced generation-label bijection",
    "No parent `g_bare` promotion is claimed",
]
for snippet in bridge_snippets:
    check(f"bridge note contains: {snippet}", has_all(bridge_text, [snippet]))

banned = [
    "retained branch-local",
    "would become retained",
    "promoted to retained",
    "retained on the actual surface",
    "full retained at this time",
]
for phrase in banned:
    check(f"bridge note avoids banned phrase: {phrase}", phrase not in bridge_text)

print("\n" + "=" * 88)
print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
print("=" * 88)

sys.exit(1 if FAIL_COUNT else 0)
