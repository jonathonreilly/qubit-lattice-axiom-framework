#!/usr/bin/env python3
"""Koide reduced-carrier physical-identification obstruction.

This runner checks the source-side repair for the audited-conditional
`koide_q_reduced_observable_restriction_theorem_2026-04-22` row.

It does not re-audit the row and does not apply a verdict. It verifies the
current science boundary: the two-slot reduced determinant algebra is exact
once a reduced scalar carrier and normalized source coordinates are supplied,
but the current retained inputs do not derive that reduced scalar carrier as
the physical charged-lepton readout, nor do they force the absolute
`D_red = I_2` normalization.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"

PASS = 0
FAIL = 0


def read_doc(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


# A. Current authority boundaries.
minimal_axioms = read_doc("MINIMAL_AXIOMS_2026-06-05.md")
three_gen = read_doc("THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md")
readout_factor = read_doc("KOIDE_Q_READOUT_FACTORIZATION_THEOREM_2026-04-22.md")
selector = read_doc("KOIDE_Q_MINIMAL_SCALE_FREE_SELECTOR_NOTE_2026-04-22.md")
selector_flat = " ".join(selector.split())
op_real_d = read_doc("OBSERVABLE_PRINCIPLE_REAL_D_BLOCK_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md")
flavor_gate = read_doc("FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md")
parent = read_doc("KOIDE_Q_REDUCED_OBSERVABLE_RESTRICTION_THEOREM_2026-04-22.md")

check(
    "Record axiom does not supply the missing readout context",
    "record supplies no readout context" in minimal_axioms
    and "decomposition" in minimal_axioms
    and "normalization" in minimal_axioms
    and "within-sector data" in minimal_axioms,
    "Record is additive only after a readout context is supplied.",
)
check(
    "Quantum axiom does not supply a physical observable bridge",
    "physical observable bridge" in minimal_axioms,
    "The one-site algebra is not a charged-lepton readout theorem.",
)
check(
    "retained C3 generation theorem excludes physical-species/readout scope",
    "Physical species" in three_gen
    and "physical-species semantics" in three_gen
    and "out of scope" in three_gen,
    "Finite M3(C) algebra is retained; physical flavor semantics are separate.",
)
check(
    "readout factorization note keeps admissibility-to-carrier as conditional",
    "Conditional extension" in readout_factor
    and "does not claim that local bosonic first-live species-resolving" in readout_factor
    and "does not by itself prove that the physical charged-lepton selector" in readout_factor,
    "Rank/kernel quotient is retained-bounded; physical selector remains open.",
)
check(
    "minimal selector note starts after the carrier is admitted",
    "physical identification with the staggered-Dirac second-order returned mass carrier remains a separate bridge" in selector_flat
    and "does not force `r = 1/2`" in selector_flat,
    "Selector-variable uniqueness is not carrier identification.",
)
check(
    "real-D uniqueness note admits the strengthened generator class",
    "Does **not** derive the strengthened admissibility class" in op_real_d
    and "Does **not** identify `D` with any specific physical Hamiltonian" in op_real_d,
    "Log-det uniqueness applies after its block-family class is supplied.",
)
check(
    "flavor gate audit identifies the readout/carrier step as a gate, not a derivation",
    "not a closure" in flavor_gate
    and "same single gate" in flavor_gate
    and "not by a type-rule" in flavor_gate,
    "The readout gate equals the carrier/basepoint identification gate.",
)

# B. Algebraic non-injectivity of the two-slot scalar compression.
u, v, w = sp.symbols("u v w", real=True)
r0 = u + v + w
norm2 = u**2 + v**2 + w**2
centered_norm2 = sp.simplify(norm2 - r0**2 / 3)

x = {u: 1, v: 2, w: 3}
y = {u: 1, v: 3, w: 2}
same_two_slot_data = (
    sp.simplify(r0.subs(x) - r0.subs(y)) == 0
    and sp.simplify(centered_norm2.subs(x) - centered_norm2.subs(y)) == 0
)
distinct_diag = (x[u], x[v], x[w]) != (y[u], y[v], y[w])
check(
    "two-slot scalar compression is not the full C3 diagonal carrier",
    same_two_slot_data and distinct_diag,
    f"(1,2,3) and (1,3,2) share sum/centered norm but differ as diagonal triples.",
)

# The pair is also not related by a cyclic rotation, so this loss is not only
# quotienting by the retained C3 action.
cyclic_orbit_x = [(1, 2, 3), (3, 1, 2), (2, 3, 1)]
check(
    "compression also loses reflection/orientation data not removed by C3",
    (1, 3, 2) not in cyclic_orbit_x,
    "Same scalar data, different C3 orbit.",
)

# C. D_red = I_2 is a normalized coordinate choice unless the source units are
# fixed by an independent readout theorem.
d1, d2, j1, j2 = sp.symbols("d1 d2 j1 j2", positive=True)
D = sp.diag(d1, d2)
J = sp.diag(j1, j2)
W = sp.simplify(sp.log((D + J).det()) - sp.log(D.det()))
W_norm = sp.log(1 + j1 / d1) + sp.log(1 + j2 / d2)
check(
    "arbitrary positive diagonal baseline normalizes to I2 after rescaling sources",
    sp.simplify(W - W_norm) == 0,
    "D_red=I2 follows after choosing normalized source coordinates j_i/d_i.",
)
check(
    "absolute D_red=I2 still needs source-unit/readout normalization",
    "D_red = I_2" in parent and "imports" in parent and "physical identification" in parent,
    "The parent source already treats this as the audit-named missing bridge.",
)
check(
    "parent exact reduced determinant support is preserved",
    "W_red(K)" in parent
    and "log det(I_2 + K)" in parent
    and "exact determinant" in parent,
    "The repair does not retract the algebraic support theorem.",
)

# D. Parent note records the new companion as a bridge-state obstruction.
check(
    "parent note records this companion without promotion",
    "KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md" in parent
    and "promote this row" in parent,
    "Source-side repair is graph-bookkeeping plus an open-gate boundary.",
)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)

print(
    "OBSTRUCTION RESULT: the reduced two-slot determinant law remains exact "
    "support on a supplied scalar carrier, but the current retained inputs do "
    "not derive that carrier as the physical charged-lepton readout or force "
    "the absolute D_red=I2 normalization. The missing bridge is a real "
    "readout/coarse-graining theorem, not a stale algebra check."
)
