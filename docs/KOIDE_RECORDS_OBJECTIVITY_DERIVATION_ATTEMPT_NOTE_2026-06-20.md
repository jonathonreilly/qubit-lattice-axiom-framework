# Koide Records-Objectivity Derivation Attempt — Equal-Block Measure and Objectivity Selector Are Independent of A_min (Block01 Synthesis)

**Date:** 2026-06-20
**Type:** no_go (independence synthesis over three derivation routes)
**Claim type:** no_go
**Status:** named_premise / independent-of-A_min (the conditional row does NOT flip to unconditional; both named inputs are confirmed independent of the scoped baseline by an explicit countermodel family)
**proposal_allowed:** false
**audit_required_before_effective_retained:** true
**Status authority:** independent audit lane only. This synthesis records three derivation attempts and their honest results; it does not set or change any audit verdict and introduces no new axiom or primitive.
**Scope:** A_min = {Lattice, Quantum, Record} plus the four approved primitives
(`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`).
**Target re-audited:** [`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`](KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md)
(bounded_theorem; `r=1/2`, `Q=2/3` conditional on two named inputs).

## Authority disclaimer

This is a derivation-attempt synthesis note. It characterizes precisely which
inputs derived, which stayed named premises, and the independence status of
`r=1/2`. The independent audit lane is the sole authority for any retained /
bounded / conditional grade. Nothing here is bare-retained or bare-promoted.

## Goal

The cited conditional note states `r=1/2` (hence `Q=(1+2r)/3=2/3`) follows from
TWO named inputs that the note itself flags as separate and not derived:

1. the **equal-block `(1,1)` metric** for the C3 singlet/doublet split
   (atom/share weighting over rank/Born `(1,2)` weighting); and
2. a **records/objectivity maximization selector** (objectivity functional as the
   physical readout criterion rather than the dephasing/trace fixed point).

The general maximizer is `r* = w_p/(2 w_s)`; equal weights give `r=1/2`,
rank/dimension weights give `r=1`. Block01 attempted to DERIVE these two inputs
from the framework baseline (Record axiom + dephasing/decoherence structure) so
the row could flip from conditional to unconditional retained-grade.

Hard guard honored throughout: `r` and `Q` are OUTPUTS of the selectors; the
empirical Koide value (`Q=2/3` / `r=1/2`) is never imported as a premise. Each
runner re-derives `Q=1` from the dimension/rank branch using identical machinery
as a non-circularity check.

## Three routes and their outcomes

| Route | Target input | Method | Outcome | Derives input? |
|-------|--------------|--------|---------|----------------|
| R1 | (1) equal-block measure | dephasing fixed point + block-exchange invariance | named_premise split | neither |
| R2 | (2) objectivity selector | SBS / quantum-Darwinism objectivity functional | named_premise split | neither |
| R3 | independence probe on `r=1/2` | explicit Record-compatible countermodel family | **no_go (independent)** | neither |

All three runners are real numpy/sympy computations with explicit residuals and a
`TOTAL: PASS=.. FAIL=..` line, reproduced on 2026-06-20:

- R1 `scripts/koide_records_objectivity_block_exchange_dephasing_2026_06_20.py` — `TOTAL: PASS=17 FAIL=0`
  (cache `logs/runner-cache/koide_records_objectivity_block_exchange_dephasing_2026_06_20.txt`)
- R2 `scripts/frontier_koide_objectivity_selector_record_derivation_2026_06_20.py` — `TOTAL: PASS=15 FAIL=0`
  (cache `logs/runner-cache/frontier_koide_objectivity_selector_record_derivation_2026_06_20.txt`)
- R3 `scripts/koide_records_objectivity_independence_probe_R3_2026_06_20.py` — `TOTAL: PASS=17 FAIL=0`
  (cache `logs/runner-cache/koide_records_objectivity_independence_probe_R3_2026_06_20.txt`)

Per-route sections:
[R1](../.claude/science/physics-loops/koide-records-objectivity/block01_section_R1.md),
[R2](../.claude/science/physics-loops/koide-records-objectivity/block01_section_R2.md),
[R3](../.claude/science/physics-loops/koide-records-objectivity/block01_section_R3.md).

## R1 — Input (1), equal-block measure: NOT derived (named premise)

The runner builds the dephasing channel `D` on 3x3 density operators (full
decoherence in the C-eigen/Fourier basis), verifies CPTP / idempotent / fixed-set
(residuals 1e-16), and asks whether a block-exchange invariance of the Record
readout *forces* equal block weights.

**Wall.** Equal-block `(1,1)` is a **dimension-blind, isotype-LABEL-counting
measure**: uniform over the two isotype labels {singlet, doublet}, ignoring that
the blocks have dimensions 1 and 2. A_min's dephasing/decoherence structure
supplies only **dimension-aware** (trace / Plancherel) measures: its
maximally-symmetric fixed point is `I/3`, whose block probabilities are the
rank/dimension measure `(1/3, 2/3) = (1,2)`, and the matching capacity branch
peaks at `r=1`, i.e. **`Q=1`, not `Q=2/3`**.

The candidate forcing symmetry — block-exchange invariance — **cannot exist** in
A_min: the singlet (dim 1) and doublet (dim 2) blocks are non-isomorphic, so no
`*`-automorphism / unitary swaps them (verified: 200 random unitaries cannot map
the rank-1 singlet projector onto the rank-2 doublet projector, best similarity
0.286 < 1). Block-exchange therefore cannot force `w_s = w_p`. This independently
re-derives, from channel fixed-point structure, the freedom left open by
[`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md).

**Closure path named precisely.** To force equal weighting, A_min would need a
readout that registers one scalar per isotype LABEL with equal a-priori weight
independent of block dimension — a counting measure on {singlet, doublet}, not a
state-trace on the Hilbert space. The Record axiom registers additive scalar
outcomes in a *supplied* readout context but supplies neither that context, nor
the sector-generation rule, nor the per-label weight. The equal-block input is an
**additional named readout-context premise**.

## R2 — Input (2), objectivity selector: NOT derived (named premise)

The runner builds the ideal spectrum-broadcast (SBS / quantum-Darwinism) state
`rho = sum_i p_i |i><i|_S (x) rho_{E1,i} (x) ... (x) rho_{EN,i}` over the 2-symbol
K/CPT sector alphabet (singlet rank 1, doublet rank 2) on N=4 environment
fragments, with per-sector fragment states orthogonal (ideal objective
broadcast), and tests whether maximizing objectivity selects `r=1/2` WITHOUT
assuming equal sector weights. Per-fragment recovered information and the
redundancy plateau are computed by exact partial traces + von Neumann / mutual
information.

**Wall (two computed reasons).**

1. **SBS objectivity is WEIGHT-BLIND.** For every weight the broadcast is fully
   objective: each single fragment recovers `I(S:E1) = H(p)` exactly and a second
   fragment adds nothing (`I(S:E1E2) = I(S:E1)`, the redundancy plateau), verified
   at `(1/2,1/2)`, `(1/3,2/3)`, `(0.2,0.8)`, `(0.9,0.1)`. Objectivity holds at
   `r=1/2`, at `r=1`, and at every interior `r` — it fixes the sector BASIS, not
   the weight. Independently reproduces
   `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02`.
2. **The only functional peaking at `r=1/2` is `H(weights)`, an indifference
   rule.** The plateau VALUE `H(p(r))` has argmax `r=1/2` (value log 2, second
   derivative < 0), but that is the Shannon entropy of the supplied weights;
   maximizing it is the max-entropy / equal-a-priori (indifference) rule over
   sector LABELS, NOT a broadcast/redundancy property. The genuine Darwinism
   observable — redundancy multiplicity — is weight-independent (constant 4) and
   does not peak at uniform.

So "objectivity-maximization → `r=1/2`" decomposes into (a) an SBS /
local-observability readout-context bridge — itself an open premise over
{Lattice, Quantum, Record} per
`DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05` — and
(b) a max-entropy / indifference selector over sector labels. Record's finite
additive scalar `I` is blind to the weight (`I(empty)=0`; relabelled disjoint
records give identical `I`); the `realized_state_primitive` bans typical/generic
weighting and marks any weight-contingent `r` as registered DATA. Neither half is
in {Lattice, Quantum, Record} + the four primitives. Input (2) is a **separate
admitted readout-context premise** — the same readout-context bridge A_min
withholds (the T1-d `observable_principle` wall).

## R3 — Independence probe: `r=1/2` is INDEPENDENT of A_min (clean no-go)

R3 attacks the conditional from the model-theory side, mirroring the
`W = log det + eps*Tr` countermodel style used on T1-d. On the Hermitian circulant
mass operator `H = a I + b C + conj(b) C^2` over Z^3 (Lattice + Quantum), the
`{I, C, C^2}` operator basis is Hilbert-Schmidt-orthogonal, so the energy splits
cleanly into the two C3 isotypes (HS operator-basis projection, residuals 1e-12):
scalar/singlet `E_+ = 3 a^2`, traceless/doublet `E_perp = 6 |b|^2`, with
`r := |b|^2/a^2` and `E_perp/E_+ = 2r`. Define the one-parameter family of
selectors

```
W_t = w_s log E_+ + w_p log E_perp,    t := w_p / w_s in (0, inf).
```

This is exactly the Ad-invariant isotype bilinear of
`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS` (scalar weight `w_s = alpha+3beta`,
traceless weight `w_p = alpha`), whose positive-definite region is `w_s, w_p > 0`.

**Result.** The constrained extremum is `r*(t) = t/2` (sympy, exact), continuous
and non-constant in `t`: `t=1 → r=1/2, Q=2/3`; `t=2` (rank/dim) `→ r=1, Q=1`;
`t=1/2 → r=1/4, Q=1/2`. EVERY member of the family is admissible under the
baseline — C-infinity continuity on the open energy cone; exactly two log
channels (block-additive, matching the 2-block Record pointer); a finitely
additive durable scalar readout `I_t` with `I_t(empty)=0` for UNEQUAL weights;
PD + Ad-invariant. The pin-test enumerates every constraint supplied by Lattice,
Quantum, Record (additivity + durability), PD, Ad-invariance, and the three
state-side primitives, and checks each at `t=2` (the rank member, `r=1`, `Q=1`):
ALL are satisfied. No predicate in A_min + the four primitives forces `t=1`.

**Conclusion.** `r=1/2` is FREE, not pinned. An explicit continuum of
equally-Record-compatible selectors gives `r*(t)=t/2` for all `t>0`, so no
derivation route inside A_min + the four approved primitives can pin `r`. The
load-bearing wall is the **isotype block-weight ratio `t = w_p/w_s`**, classified
as realized-state DATA by the `realized_state_primitive` register (item 4:
`r in {0, 1/2, 1}` are sector data, never forced). R3 is the model-theoretic dual
of R1's and R2's named-premise splits: not a gap in one attempt but a genuine
independence.

## Synthesis verdict — where the row stands

**Neither input derives. `r=1/2` (hence `Q=2/3`) is INDEPENDENT of A_min + the
four approved primitives — a clean no-go for closure of THIS conditional.** The
row stays conditional / named-premise. This is NOT a no-go against the framework:
a future RETAINED authority could still supply an objectivity-max / equal-weight
axiom, or select the rank/trace (`Q=1`) route.

The two named inputs are now characterized precisely:

- **Input (1) — equal-block measure** = a **dimension-blind isotype-label-counting
  readout measure** (uniform over the 2 isotype labels). A_min's intrinsic
  measures on the C3 grading are dimension-weighted (trace/Plancherel fixed point
  `I/3 → (1,2) → Q=1`). Block-exchange invariance is ruled out as a forcing
  symmetry (unequal block dimensions 1 vs 2 are a hard obstruction).
- **Input (2) — objectivity selector** = a two-part premise: (a) an
  SBS / local-observability readout-context bridge (itself open per the Darwinism
  gate) plus (b) a max-entropy / equal-a-priori indifference selector over the two
  K/CPT sector labels. SBS objectivity alone is weight-blind (fixes basis, not
  `r`); the `r=1/2`-selecting half is the indifference half.

Both inputs reduce to the SAME single auditable object: a **dimension-blind,
label-counting (equal-a-priori) readout context** over the singlet/doublet sector
alphabet. A_min supplies only dimension-aware measures, whose every realization
points to `Q=1`. The conditional sufficient route `(1,1) + objectivity-max → Q=2/3`
remains valid and useful; it is not a Record-axiom derivation.

## Non-import / non-circularity guard

In all three runners `r=1/2` and `Q=2/3` appear only as solved OUTPUTS. The
`(1,2)` / `t=2` dimension branch yields `Q=1` from identical machinery, confirming
the pipeline does not smuggle in the empirical value. The empirical `Q=2/3` enters
only as a read-only post-hoc LABEL (R3 F5), never as a selector.

## No-Go Discipline Gate

**N1 — Alternative routes.** Three independent routes ran (R1 derive input 1, R2
derive input 2, R3 independence probe), plus the five routes already enumerated in
the cited conditional note. All fail to derive either input; R3 exhibits an
explicit countermodel continuum.

**N2 — Wall independence.** The two inputs are independent of A_min and of each
other (matches the conditional note's N2). Equal-block does not imply
objectivity-max; objectivity-max is weight-blind and does not choose equal over
rank weighting absent the indifference selector.

**N3 — Hidden-wall scan.** The independence rests only on the explicit isotype
block-weight ratio `t`, the dephasing fixed-point measure, and the SBS objectivity
functional. "Objectivity" and "equal-block" are kept as named inputs, never as
hidden theorems. No empirical mass ratio is a hidden premise.

**N4 — Residual matching.** The residual matches the block-weight frontier `(1,1)`
vs `(1,2)`, the isotype-split uniqueness freedom, and the D3 record-degeneracy
residual (two atoms available, measure unselected). R1/R2/R3 upgrade these from
citation to direct construction.

**N5 — Rhetoric audit.** "Not derived" / "independent" is scoped to A_min + the
four approved primitives. The conditional sufficient route remains positive and
available if the named inputs are supplied or admitted.

**N6 — Partial-closure path.** The closure path is precisely named: derive or
admit a dimension-blind, label-counting (equal-a-priori) readout context as an
independently audited structure. This note does not call for a new axiom.

**N7 — Steelman.** Strongest pro-conditional argument: objectivity should be the
physical selector in a records lane, making atom-counting the right measure. R2
grants the SBS objectivity property but shows it is weight-blind, so the steelman
still needs the separate indifference selector.

**N8 — Cross-cycle echo.** Same residual tracked by the block-weight frontier,
readout demarcation, isotype-split uniqueness, and D3 pointer-degeneracy notes,
and by the Darwinism-bridge / QD-basis-not-weight residuals. This note records an
independence result rather than duplicating the residual as a closure.

## Load-Bearing Authorities

[KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md](KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md)
[KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
[KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md)
[PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)

## Recommendation

The row stays conditional / named-premise. R3 sharpens it to a clean independence:
`r=1/2` is provably free under A_min + the four approved primitives. No flip to
unconditional retained-grade. Any future positive work must supply the
dimension-blind label-counting (equal-a-priori) readout context as an
independently audited structure — A_min's intrinsic measures are dimension-weighted
and point to `Q=1`. The independent audit lane is the sole authority for the final
grade.
