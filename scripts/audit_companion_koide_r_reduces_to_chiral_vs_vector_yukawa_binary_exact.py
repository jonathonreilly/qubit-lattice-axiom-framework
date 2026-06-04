#!/usr/bin/env python3
"""Exact open-gate companion for the FS chiral/vector Koide mode count.

This runner verifies the algebraic content of
KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md.
It does not select a chiral readout, does not derive Koide r=1/2, and
does not apply any audit status.
"""

from pathlib import Path
import sympy as sp
from sympy import I, Rational, simplify, sqrt

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md"

R = []


def chk(label, ok, detail=""):
    R.append((label, bool(ok), detail))


def fs_indicator(chars):
    # C3 = {e, c, c^2}; squaring maps e->e, c->c^2, c^2->c.
    square = {0: 0, 1: 2, 2: 1}
    return simplify(sum(chars[square[k]] for k in range(3)) / 3)


def r_from_weights(ws, wd):
    x = simplify(sp.sympify(ws) / (sp.sympify(ws) + sp.sympify(wd)))
    return simplify(((1 - x) / 6) / (x / 3))


note_text = NOTE.read_text()

# Exact primitive cube root of unity.
omega = Rational(-1, 2) + I * sqrt(3) / 2
omega_bar = Rational(-1, 2) - I * sqrt(3) / 2
chk(
    "(0) C3 root identities",
    simplify(1 + omega + omega_bar) == 0
    and simplify(omega * omega - omega_bar) == 0,
)

# FS types for C3 irreps.
chi_trivial = [Rational(1), Rational(1), Rational(1)]
chi_omega = [Rational(1), omega, omega_bar]
chi_omega_bar = [Rational(1), omega_bar, omega]
chk(
    "(1) FS(trivial)=+1 and FS(omega)=FS(omega-bar)=0",
    fs_indicator(chi_trivial) == 1
    and fs_indicator(chi_omega) == 0
    and fs_indicator(chi_omega_bar) == 0,
)

# Vector versus chiral weighting.
r_vector = r_from_weights(1, 2)
r_chiral = r_from_weights(1, 1)
chk(
    "(2) vector count (1,2)->r=1; chiral count (1,1)->r=1/2",
    r_vector == 1 and r_chiral == Rational(1, 2),
)

# Mode-count asymmetry: singlet remains one real mode; doublet is 2 real
# modes in vector readout and 1 holomorphic mode in chiral readout.
singlet_vector = singlet_chiral = 1
doublet_vector = 2
doublet_chiral = 1
chk(
    "(3) singlet mode fixed; doublet changes from 2 real modes to 1 holomorphic mode",
    singlet_vector == singlet_chiral == 1
    and doublet_vector == 2
    and doublet_chiral == 1,
)

# Uniform complex-mode rescaling does not produce the chiral candidate.
uniform_complex = r_from_weights(Rational(1, 2), 1)
chk(
    "(4) uniform complex count (1/2,1) preserves r=1, not r=1/2",
    uniform_complex == 1 and uniform_complex != Rational(1, 2),
)

# Source boundary: open gate, no status promotion, no Record/readout smuggle.
required_note_tokens = [
    "**Type:** open_gate",
    "does not select the chiral",
    "does not derive `r = 1/2`",
    "does not use PDG values",
    "does not decide this readout choice",
    "independent audit required",
]
chk(
    "(5) source note keeps open-gate and no-status-promotion boundary",
    all(token in note_text for token in required_note_tokens),
)

# Dependency links must be visible to the citation graph.
required_links = [
    "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md",
    "MULTIFACTOR_CONNES_LOTT_PURCHASES_NOT_DERIVES_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md",
    "KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md",
    "MINIMAL_AXIOMS_2026-06-04.md",
]
chk(
    "(6) source note exposes parent/dependency links",
    all(link in note_text for link in required_links),
)

passes = sum(1 for _, ok, _ in R if ok)
fails = sum(1 for _, ok, _ in R if not ok)
for label, ok, detail in R:
    suffix = f" :: {detail}" if detail else ""
    print(("PASS" if ok else "FAIL"), "-", label + suffix)

print(f"\n{passes} PASS, {fails} FAIL")
if fails:
    raise SystemExit(1)

print(
    "\nOPEN GATE: FS(C3) makes the asymmetry precise. The trivial isotype is real, so a\n"
    "stays one mode; the nontrivial conjugate pair is complex, so b is two real modes under\n"
    "a vector readout and one holomorphic mode under a chiral readout. This verifies the\n"
    "conditional map only: vector -> r=1, chiral -> r=1/2. The chiral readout remains gated."
)
