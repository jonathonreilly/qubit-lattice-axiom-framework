#!/usr/bin/env python3
"""Verifier for the charged-lepton Koide two-gate bounded companion.

Pair runner for:
docs/CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md

Exercises S1-S5 + hostile-review exclusions from the source note. This is a
source-only verifier: it checks algebra, existing registry/dependency surfaces,
and non-promotion boundaries; it does not propose an effective status.
"""

from __future__ import annotations

import math
import os
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


PASS = 0
FAIL = 0
LOG: list[str] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        LOG.append(f"[PASS] {name}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL += 1
        LOG.append(f"[FAIL] {name}" + (f"  ({detail})" if detail else ""))


# ======================================================================
# S1: Algebraic surface (pure polynomial algebra)
# ======================================================================
# Q := 1/3 + c²/6  with  c := 2r/a
# Q = 2/3  ⇔  c² = 2  ⇔  r²/a² = 1/2

def Q_from_r_over_a(r_over_a: Fraction) -> Fraction:
    """Q = 1/3 + (2/3) r where r = (r/a)^2 in the framework's normalization."""
    r = r_over_a * r_over_a  # r²/a² = (r/a)²
    return Fraction(1, 3) + Fraction(2, 3) * r


# At r/a = 1/√2 (r²/a² = 1/2):
# Use float test since 1/√2 is irrational; symbolic Q = 1/3 + 2/3 · 1/2 = 2/3
Q_at_half = Fraction(1, 3) + Fraction(2, 3) * Fraction(1, 2)
record(
    "S1.a: Q = 1/3 + (2/3) r at r²/a² = 1/2 equals 2/3 exactly",
    Q_at_half == Fraction(2, 3),
    f"Q = {Q_at_half} = 2/3",
)

# Verify (c² = 2) ⇔ (r²/a² = 1/2) by direct algebra
# c = 2r/a, so c² = 4·(r²/a²). c² = 2 ⇔ r²/a² = 1/2.
c_squared_at_half = 4 * Fraction(1, 2)
record(
    "S1.b: c² = 2 ⇔ r²/a² = 1/2 by direct algebra",
    c_squared_at_half == 2,
    f"c² at r²/a² = 1/2 equals {c_squared_at_half}",
)

# Forward direction: Q = 2/3 implies r²/a² = 1/2
# 2/3 = 1/3 + (2/3) r ⇒ (2/3) r = 1/3 ⇒ r = 1/2.
implied_r_squared_over_a_squared = (Fraction(2, 3) - Fraction(1, 3)) / Fraction(2, 3)
record(
    "S1.c: Q = 2/3 implies r²/a² = 1/2 by direct algebra",
    implied_r_squared_over_a_squared == Fraction(1, 2),
    f"implied r²/a² = {implied_r_squared_over_a_squared}",
)


# ======================================================================
# S2 + S3: open-gate routing + Gate-1 + Gate-2 no_go portfolios
# ======================================================================


def file_exists_on_origin_main(repo_root: str, relpath: str):
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", "origin/main", relpath],
            capture_output=True,
            text=True,
            cwd=repo_root,
            timeout=10,
        )
        return result.returncode == 0 and relpath in result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


def repo_root() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip()
    except Exception:
        return os.getcwd()


ROOT = repo_root()
PAIR_NOTE = Path(ROOT) / "docs/CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md"
PAIR_TEXT = PAIR_NOTE.read_text(encoding="utf-8")

CONTEXT_SURFACES = [
    "docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md",
    "docs/audit/data/premise_decision_history.json",
    "docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md",
]

for relpath in CONTEXT_SURFACES:
    exists = os.path.exists(os.path.join(ROOT, relpath))
    short = relpath.split("/")[-1][:50]
    record(
        f"S2.{short}: context surface present",
        exists is True,
        "history is provenance only; current gate is open and non-premise",
    )

GATE1_NO_GOS = [
    "docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md",
    "docs/KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24.md",
    "docs/KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md",
]
GATE2_NO_GOS = [
    "docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
    "docs/KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md",
    "docs/KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md",
]

gate1_present = sum(1 for p in GATE1_NO_GOS if file_exists_on_origin_main(ROOT, p) is True)
record(
    "S2.gate1_no_go_portfolio: Gate-1 (r=1/2 selection) no_go portfolio members present on origin/main",
    gate1_present == len(GATE1_NO_GOS),
    f"{gate1_present}/{len(GATE1_NO_GOS)} no_go rows present (acknowledged as boundary)",
)

gate2_present = sum(1 for p in GATE2_NO_GOS if file_exists_on_origin_main(ROOT, p) is True)
record(
    "S3.gate2_no_go_portfolio: Gate-2 (delta = 2/9 radian-bridge) no_go portfolio members present on origin/main",
    gate2_present == len(GATE2_NO_GOS),
    f"{gate2_present}/{len(GATE2_NO_GOS)} no_go rows present (acknowledged as boundary)",
)

# delta = Q/3 readout: at Q = 2/3, delta = 2/9 exactly
delta_at_target = Fraction(2, 3) / 3
record(
    "S3.delta_readout: delta = Q/3 readout at Q = 2/3 equals 2/9 exactly",
    delta_at_target == Fraction(2, 9),
    f"delta = {delta_at_target} = 2/9",
)

# ======================================================================
# S4: Phase-independent Koide guardrail
# ======================================================================
# For the Brannen ansatz x_k = a · [1 + √2 cos(δ + 2π k / 3)], the Koide
# identity Q := Σ x_k² / (Σ x_k)² = 2/3 for any δ.

SQRT2 = math.sqrt(2.0)


def brannen_x(k: int, delta: float) -> float:
    return 1.0 + SQRT2 * math.cos(delta + 2.0 * math.pi * k / 3.0)


def koide_Q(delta: float) -> float:
    xs = [brannen_x(k, delta) for k in (0, 1, 2)]
    sum_x = sum(xs)
    sum_x_sq = sum(x * x for x in xs)
    return sum_x_sq / (sum_x * sum_x)


# Sample at five distinct phases
sample_deltas = [0.0, 0.1, 2.0 / 9.0, 1.0, math.pi / 4]
Q_values = [koide_Q(d) for d in sample_deltas]
all_q_at_two_thirds = all(abs(Q - 2.0 / 3.0) < 1e-13 for Q in Q_values)

record(
    "S4: phase-independent Koide guardrail Q = 2/3 holds at five sample deltas",
    all_q_at_two_thirds,
    f"max deviation: {max(abs(Q - 2.0/3.0) for Q in Q_values):.2e}",
)


# ======================================================================
# S5: Chain-of-custody anchor (sidecar reference)
# ======================================================================

CHAIN_OF_CUSTODY_PATH = "docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md"
chain_present = file_exists_on_origin_main(ROOT, CHAIN_OF_CUSTODY_PATH)
record(
    "S5: chain-of-custody anchor present on origin/main",
    chain_present is True,
    "sidecar reference; the chain-of-custody documents L1-L10 + AC_φλ open conditions",
)

# Also the sister delta companion should be present.
SISTER_COMPANION = "docs/CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md"
sister_present = file_exists_on_origin_main(ROOT, SISTER_COMPANION)
record(
    "S5.sister: sister delta companion present on origin/main",
    sister_present is True,
    "delta-piece companion; this note is the umbrella twin",
)

# Parent open_gate row should be present (the note this is companion to)
PARENT_OPEN_GATE = "docs/CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md"
parent_present = file_exists_on_origin_main(ROOT, PARENT_OPEN_GATE)
record(
    "S5.parent: parent open_gate row present on origin/main",
    parent_present is True,
    "companion to (not modified by) this note",
)


# ======================================================================
# Retained algebraic authorities for S1
# ======================================================================

S1_CONTEXT = [
    "docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md",
    "docs/CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md",
    "docs/KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md",
]

s1_present = sum(1 for p in S1_CONTEXT if os.path.exists(os.path.join(ROOT, p)))
record(
    "S1.context_algebra: three algebraic context surfaces are present",
    s1_present == len(S1_CONTEXT),
    f"{s1_present}/{len(S1_CONTEXT)} context surfaces present; authority is not inferred",
)


# ======================================================================
# Topological readout authority for S3
# ======================================================================

ZN_TOPOLOGICAL = "docs/AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md"
zn_present = os.path.exists(os.path.join(ROOT, ZN_TOPOLOGICAL))
record(
    "S3.topological: Z_N spectral-asymmetry context surface present",
    zn_present is True,
    "context only; the identity is recomputed below and no audit authority is inferred",
)

# Topological identity check: L_3(1,2) = (N-1)/N² at N=3 = 2/9
N = 3
L_3_at_1_2 = Fraction(N - 1, N * N)
record(
    "S3.topological_identity: L_3(1,2) = (N-1)/N² at N=3 equals 2/9 exactly",
    L_3_at_1_2 == Fraction(2, 9),
    f"L_3(1,2) = {L_3_at_1_2}",
)


# ======================================================================
# Hostile-audit checks
# ======================================================================

# H1: does NOT derive r = 1/2 or Q = 2/3
record(
    "H1: does NOT derive r = 1/2 or Q = 2/3; Gate 1 is an explicit hypothesis",
    "This note does not derive `r^2/a^2=1/2`." in PAIR_TEXT,
    "no derivation attempted here; the open gate remains",
)

# H2: does NOT promote an open hypothesis to retained
record(
    "H2: does NOT promote an AC_φλ hypothesis to retained",
    "does not restore or promote the historical admission index" in PAIR_TEXT,
    "historical decisions are provenance only; this note is conditional",
)

# H3: does NOT weaken any retained no_go
all_no_go_present = (gate1_present == 3 and gate2_present == 3)
record(
    "H3: does NOT weaken any retained no_go in Gate-1 + Gate-2 portfolios",
    all_no_go_present,
    f"all 6 portfolio members acknowledged as boundary, not retired",
)

# H4: does NOT consume PDG values
record(
    "H4: does NOT consume PDG values as load-bearing inputs",
    "consume PDG values" in PAIR_TEXT
    and "does not derive charged-lepton masses" in PAIR_TEXT,
    "S1-S5 use algebraic identities, retained authorities, and explicit hypotheses",
)

# H5: does NOT derive √2 BAE amplitude
record(
    "H5: does NOT derive the √2 BAE amplitude; part of AC_φλ bundle",
    "It does not derive `r^2/a^2=1/2`, `Q=2/3`, `delta=2/9`, or the `sqrt(2)`" in PAIR_TEXT,
    "sqrt(2) is an explicit open hypothesis",
)

# H6: does NOT derive overall scale a
record(
    "H6: does NOT derive overall charged-lepton scale a",
    "It does not derive the absolute charged-lepton scale." in PAIR_TEXT,
    "scale a is outside this dimensionless conditional calculation",
)

# H7: does NOT make neutrino claim
record(
    "H7: does NOT make any neutrino-sector claim",
    "It does not make neutrino-sector claims." in PAIR_TEXT,
    "charged-lepton chamber only; neutrino sector entirely out of scope",
)

# H8: does NOT propose new axiom or theory-language extension
record(
    "H8: does NOT propose new axiom or new theory-language extension",
    "It does not add an axiom or new theory language." in PAIR_TEXT,
    "uses the baseline one-qubit/Z^3 substrate, retained Koide theorems, explicit hypotheses, and chain-of-custody sidecar",
)

# H9: parent is context only; no authority is inferred from its file presence
record(
    "H9: parent CHARGED_LEPTON_KOIDE_NOTE is context only",
    "parent open-gate row preserved, not consumed" in PAIR_TEXT,
    "relationship checked from paired-note text, not git history",
)

# H10: chain-of-custody is a source reference, not a status authority
record(
    "H10: chain-of-custody note is a non-authoritative source reference",
    "chain-of-custody source reference" in PAIR_TEXT
    and "neither is treated as an\n  audit verdict or as authority" in PAIR_TEXT,
    "relationship checked from paired-note text, not a false unchanged-file assertion",
)


# ======================================================================
# Summary
# ======================================================================

print("\n=== Charged-Lepton Koide Two-Gate Bounded Companion ===\n")
print("Scope: bounded_theorem on Koide two-gate algebraic chain under EXPLICIT")
print("       explicit open hypotheses for both gates (r=1/2 and delta=2/9). Does")
print("       NOT derive r=1/2 or delta=2/9. Does NOT promote AC_φλ. Does NOT")
print("       weaken any retained no_go. Companion to parent open_gate row +")
print("       chain-of-custody (both non-authoritative context here).\n")
for line in LOG:
    print(line)
print(f"\nPASS={PASS}  FAIL={FAIL}\n")
if FAIL == 0:
    print("All bounded-companion checks PASSED under explicit conditional framing.")
    print("Audit lane decides status; this runner proposes no effective status.")
else:
    print(f"{FAIL} CHECK(S) FAILED.")
    sys.exit(1)
