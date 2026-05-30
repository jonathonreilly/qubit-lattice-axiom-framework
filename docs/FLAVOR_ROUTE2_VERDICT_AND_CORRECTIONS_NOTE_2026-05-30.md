# Flavor — Route 2 refuted; corrections to moves 4 & 6; value cleanly relocated

**Date:** 2026-05-30
**Claim type:** full-court-press verdict + rigorous self-correction. Imports nothing.
**Runner:** `scripts/flavor_route2_verdict_and_corrections_2026_05_30.py` (+ cache).
**Source:** 7-angle Route-2 press (`wf_4e4fcccb`, 0 derivable forcings survived) +
independent verification (all to machine precision).

## Route 2 (dynamical chiral criticality → a_VEV→0 → Q=2/3, import-free)?
**Verdict: refuted as a route to the value — with one genuine new positive.**

### Kill 1 — the chiral-critical endpoint does not give 2/3
In the physical signed-eigenvalue (Brannen) readout, `M=aI+b(J−I)` has √-masses
`{a+2b, a−b, a−b}` (sum `=3a`). As `a→0` the signed sum → 0 and
`Q = Σm/(Σ√m)² → ∞` (verified: `a=1e−4, b=1/√2 → Q≈3e7`). **`Q=2/3` sits at the
finite interior ratio `b/a=1/√2`** (`r=1/2`), which no chiral symmetry protects.

### Kill 2 — Q is scale-invariant
`Q(c·m)=Q(m)` for all `c` (verified across `10⁻²⁰…10¹⁰`). Lepton **lightness** is
an overall-scale fact (`m_e/M_Pl~10⁻²³`) and **cannot move Q at all.**

### Positive (genuinely new) — native staggered chiral structure
The framework's native fermion operator is **staggered**, not Wilson: it carries
the exact spacetime sublattice chiral grading `ε(x)=(−1)^{x+y+z}` with `{ε,D}=0`
(retained `cpt_exact_note`) + emergent `γ₅` at `d=3+1` (retained
`clifford_volume_chirality`). The native staggered condensate is **exactly odd in
the mass** (chiral-critical at `m=0`, no tuning); the Wilson condensate has an
additive piece. This chiral symmetry is **spacetime** (native), genuinely
**distinct from** the generation-`Γ_χ` import — so Route 2 is import-free *on the
chirality axis*. But `ε` is generation-**blind** (S₃-invariant on the hw=1 orbit),
so it cannot split the C₃ orbit to select `a` vs `b`; and (Kill 1) the value isn't
at the critical endpoint anyway.

## Corrections to this session (rigorous self-correction)
- **Move 4 (`FLAVOR_LOOP_PRESERVES_BLOCK_COUNT`) — "leptons light → fluctuation-
  dominated → Q→2/3" is RETRACTED** (Kill 2: Q is scale-invariant). What survives:
  the one-loop bubble preserves the covariant block-count *measure* (`Π_X ∝ Tr(X²)`)
  — a measure/RG statement, not a lightness mechanism.
- **Move 6 (`FLAVOR_AVEV_FORCING_CAPSTONE`) — "a_VEV=0 ⇒ exact Q=2/3" is RETRACTED**
  (Kill 1). The error was a **conflation of two decompositions**: `a_VEV=0 ⇒ Q=2/3`
  holds only where `a` is the zero-*mean* chiral order parameter (`a=(1/3)Tr M`,
  gated by the generation `Γ_χ` import), **not** where `a` is the uniform √-mass
  (eigenvalue readout, where `a→0` gives `Q→∞`).
- **Methodological flag:** this session's three "vacuum → Q=1/3" computations
  (gap-equation, competing-orders, effective-potential) used the **Wilson**
  propagator (the wrong, chiral-breaking operator class). They should be **re-run on
  the native staggered operator** before any broken-phase no-go stands.

## What stands (the surviving core)
- **Move 1:** `b` is native (S₃-symmetric double-shift sum = `J−I`).
- **Move 2:** `Q=2/3 ⟺ b/a=1/√2`, RP-bounded `[−1/2,1]`.
- **Move 3:** the covariant `Tr(M²)` matrix-field measure realizes the **sector /
  block-count** measure → `r=1/2`. This is a measure statement — and it is the live
  native lean on the *real* gate.
- **Move 5:** quark cross-sector retraction (still valid).

## The clean relocation (value question, sharpest form yet)
`Q=2/3` **is** the interior ratio `b/a=1/√2 = r=1/2`, and **lightness, criticality,
and the uniform VEV are all red herrings** (Q is scale-invariant; criticality gives
`Q→∞`). The *only* thing that sets the value is whether mass generation weights the
C₃ isotypes by **trace** (→ Q=1) or **sector-count** (→ Q=2/3) at the operator
level. **Move 3 is exactly a native lean on this gate** (covariant matrix-field
measure → sector → 2/3) and is untouched by the corrections.

## Status / next paths (not a closure)
1. **Re-run the condensate on the native staggered operator** (ε grading, no Wilson
   `r`-term) at `g_bare=1` — does the staggered lepton sector give `a_VEV=0`
   (symmetric) or broken, and does the off-diagonal `b` co-condense? (Tests whether
   the 3 Wilson-based `Q=1/3` verdicts survive.)
2. **Pin `b/a=1/√2` (`r=1/2`) as a fixed point** = settle trace-vs-sector measure at
   the operator level. Move 3 is the opening; the question is whether the covariant
   (sector) measure is *forced* over the trace (dimension) one for the mass operator.

No false closure. The press refuted Route 2 *and* trimmed two erroneous moves —
leaving the value question sharper and import-free: it is the single trace-vs-sector
measure choice, with move 3 the live native argument for sector (→ 2/3).
