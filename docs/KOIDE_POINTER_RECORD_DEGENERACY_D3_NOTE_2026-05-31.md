---
claim_id: koide_pointer_record_degeneracy_d3_note_2026-05-31
claim_type_author_hint: positive_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Native pointer record-degeneracy (D3): the C₃ sector record is 2-outcome, which sharpens but does not force the Koide block-count weight

**Date:** 2026-05-31
**Claim type:** positive linear-algebra theorem (D3) + narrow demarcation of its
reach. The positive fact is zero-dependency and names no state. The demarcation
half adds no axiom and no import and sets no audit outcome.
**Status authority:** independent audit lane only.
**Primary runner:**
`scripts/frontier_koide_pointer_record_degeneracy_d3.py`
with cache
`logs/runner-cache/frontier_koide_pointer_record_degeneracy_d3.txt`
(25/25 checks).

## Setting

The charged-lepton Koide value reduces
([`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md))
to `Q = (1+2r)/3`, `r = |b|²/a²`, so `Q = 2/3 ⟺ r = 1/2` — the `(1,1)`
block-count isotype weight — versus `Q = 1 ⟺ r = 1`, the `(1,2)` dimension
weight. Two retained no-gos
([`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md),
[`ACTION_NORMALIZATION_NOTE.md`](ACTION_NORMALIZATION_NOTE.md)) decline to rank
`(1,1)` vs `(1,2)`, and the readout-lane note
([`KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30.md`](KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30.md))
showed the native mass readout supplies the formula but not the weight,
localizing the pin to the `F1` (equal-block) vs `F3` (dimension) selection.

This note records a new native fact about the **records** side of that
selection and demarcates exactly how far it reaches.

## The positive fact (D3)

The native `C₃` sector pointer is `S = C + C² = J − I` on the `Z₃` regular
representation (`C` the cyclic shift, `C³ = I`). Direct computation:

- **`S` has exactly two distinct eigenvalues:** `+2` (singlet, rank-1
  projector) and `−1` (doublet, rank-2 projector). Spectrum `{+2, −1, −1}`.
- Therefore a **sharp / projective record of `S` is intrinsically a 2-outcome
  record**, and the doublet's two micro-states share one rank-2 eigenprojector:
  they are **record-degenerate** under a sharp `S`-measurement (the sharp record
  returns the single value `−1` on the entire 2-dimensional doublet eigenspace).
- This uses only `C` (`C³ = I`, retained order relation) and the definition
  `S := C + C²`. It **names no state** — no `I/3`, no reference density matrix —
  so it is independent of the demoted pre-record tracial identification (see
  Scope below).

The degeneracy is **relative to the choice of `S`**, not absolute. The
conjugate native pointer `A = i(C − C²)` is Hermitian, commutes with `S`
(`[S,A] = 0`, both functions of the normal `C`), and has **three distinct
eigenvalues** `{0, ±√3}` — so `A` resolves the doublet into three outcomes.

## What D3 contributes to the Koide weight

D3 converts the previously vague "maximize objectivity" handle for the `(1,1)`
reading into a **crisp, well-motivated bit**: under a sharp sector record the
doublet is **one record atom**, so the records-native question is whether to
weight that atom by

- **count** (one objective symbol → atoms `(1/2, 1/2)` → block `(1,1)` →
  `r = 1/2` → `Q = 2/3`), or
- **projector rank / Born** (the atom carries rank `2` → `(1/3, 2/3)` →
  dimension `(1,2)` → `r = 1` → `Q = 1`).

D3 supplies the **outcome-merge half** of the `(1,1)` reading (there genuinely
are two record atoms, singlet and doublet), and it answers a prior objection
that the equal-weight was a smuggled metric: the binary structure is **forced**
by `S` having exactly two distinct eigenvalues, not chosen. The budget-free
record objectivity — Shannon `H₂` of the atom-share, and the genuine
quantum-Darwinism per-fragment mutual information of the 2-symbol record through
a binary-symmetric channel — is strictly maximized at the **balanced atoms**,
i.e. `r = 1/2 → Q = 2/3`, **fidelity-independently** (runner §D).

**Honest functional correction.** The unconstrained log-capacity
`F1 = log E₊ + log E⊥` (`E₊ = 3a²`, `E⊥ = 6|b|²`) is **monotone** in `r` (its
argmax is at the boundary, not `r = 1/2`); only the **budget-free** atom-share
`H₂` / per-fragment mutual information peaks at `r = 1/2`. A prior statement that
"log-capacity peaks at `r = 1/2`" was correct only under a fixed-energy budget;
the conclusion stands on the budget-free share functional, which is the
appropriate objectivity measure (runner §D, first check).

## What this does NOT establish (the collapse fails — three prongs)

D3 fixes the record **σ-algebra** (two atoms) but is **silent on the measure**
over those atoms. It does not force counting-on-atoms `(1,1)` over rank/dimension
`(1,2)`, for three independent verified reasons:

1. **Category mismatch (P1).** `Q = (Σ λ²)/(Σ λ)²` is built from the
   **eigenvalue sum of the mass operator** `H = aI + bC + b̄C²`, in which the
   doublet enters as its **two distinct eigenvalues summed separately** — the
   dimension `(1,2)` reading is baked into `Q`'s definition. `[H, S] = 0`, but a
   sharp `S`-record coarse-grains the two doublet masses (`μ, τ`), and D3 says
   nothing about whether they are summed once or twice. (Runner §E P1: a generic
   `H` has three distinct eigenvalues.)
2. **The native ensemble stands (P2).** The dephasing fixed point `ρ → I/3`,
   pushed through the sharp-`S` projectors, gives Born weights `(1/3, 2/3)` =
   projector-rank-weighted = dimension `(1,2)` → `Q = 1`. The doublet letter's
   physical weight `Tr(P_doublet ρ)` carries rank `2`; "the record is 2-lettered"
   does not make the doublet letter's weight equal the singlet's.
3. **Equal-rank non-transport (P3).** The retained sharp-record tangent theorem
   ([`SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md))
   gives the balanced reference `(1/2, 1/2)` only for **equal-rank** binary
   records. `dim = 3` is **odd**, so no `Z₂` observable on `ℂ³` has `(3/2, 3/2)`
   eigenspaces; the `S`-split `(1, 2)` is forced **unequal**, and `(1/2, 1/2)`
   is not inherited — counting-on-atoms must be **postulated**.

Consequently the records-native count via the **actually recorded** observables
(the mass spectrum `H`, the conjugate pointer `A`, and the retained
three-generation pattern records — see Relation) is `2`, not `1`; the doublet
micro-states `μ, τ` are genuinely distinct recorded masses.

## The residual (one crisp bit)

> Weight the two `S`-pointer outcomes by **count** (singlet : doublet = `1 : 1`
> → `r = 1/2` → `Q = 2/3`), **not** by Born-probability / projector rank
> (`1 : 2` → `r = 1` → `Q = 1`). D3 fixes that there are two outcomes — not how
> to weight the doublet atom.

This surviving bit is the same single counting-measure bit isolated by the
signed-vs-singular-value / `det_R`-vs-`det_C` analysis (one complex slot vs two
real slots) and formalized by the retained no-go
`koide_frobenius_isotype_split_uniqueness` (scalar/traceless sector weight
permitted, not forced; `β ≠ 0` allowed). D3 **sharpens** it and supplies one of
its two components; it does not eliminate it. Selecting counting-on-atoms is the
quantum-Darwinism objectivity premise expressed in records language — currently
an import (zero corpus occurrences), not a theorem of `A1 + A2 + retained`.

## Non-circularity

`r = |b|²/a²` is the free scan variable throughout the runner; `r = 1/2` and
`Q = 2/3` are never assumed — they emerge only as solved outputs
(`Q = (1+2r)/3`, `dQ/dr = 2/3` with no stationarity at `r = 1/2`). The block
energies, the atom-share maximizer, and the three prongs are all computed
forward from `(a, b)`.

## Scope and the demoted admission

D3 invokes **no** state object, so it does not depend on the physical
identification of the unique tracial state `I/3` with a pre-record reference —
the step explicitly **demoted to a separate open admission** in
[`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)
(only the unique-tracial-state characterization is retained). The ensemble prong
P2 cites `ρ = I/3` only as the `C`-invariant maximally-mixed reference whose
rank-pushforward is `(1/3, 2/3)`; that computation is admission-independent.

## Boundary (the next path this opens)

This closes no route. The residual is a single crisply-stated counting-measure /
sector-weight selection on the (necessarily unequal-rank, since `dim = 3` is odd)
`S`-record. Live forward handles — none supplied by D3, each an opening:

- a records-native principle that **derives** (rather than postulates)
  privileging counting-on-objective-symbols over rank/Born weighting — exactly
  what `koide_frobenius_isotype_split_uniqueness` leaves open;
- a retained `SO(2)/U(1)_b` doublet-frame complex-structure quotient `J`
  reducing the two doublet `H`-eigenvalue modes to one Koide slot (note the
  continuous `U(1)_b` rephasing is incompatible with `C³ = I` as an algebra
  symmetry, leaving readout-functional factorization as the live handle);
- the signed-vs-singular-value readout-class dimension (the Brannen closure
  load-bears on the signed `√m`), which is orthogonal to the counting bit;
- whether the `T`-parity privilege of `S` (`T`-even) over `A` (`T`-odd) under
  `K = `conjugation can be parlayed past the rank obstruction — note
  `rank(P_doublet) = 2` is `T`-parity invariant, so this alone is insufficient.

## Relation to retained surface

The conjugate pointer `A` and the retained three-generation pattern records
(`three_generation_observable`,
`three_generation_hw1_distinct_translation_characters`) both **resolve** the
doublet into distinct generations, which is why the record-native count is `2`
(prong P3 / runner §E). D3 is consistent with, and sharpens, the
`KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30` result: the readout supplies the
formula, the records supply the 2-atom σ-algebra, and the **weight** on the
doublet atom remains the single unforced bit handed to the dynamics /
selection-principle lane.

## No-Go Discipline Gate (demarcation half)

**N1 — Alternative routes.** Three records-native routes to `(1,1)` were tested:
(a) record-degeneracy → atom-count `(1,1)` — fixes the σ-algebra, not the
measure; (b) "observed = sharp record, not ensemble" made sufficient by D3 —
fails P1/P2 (the recorded mass operator resolves the doublet); (c) equal-rank
balanced reference transport — fails P3 (`dim 3` odd). None forces `(1,1)`.

**N2 — Wall-independence.** The three prongs are independent (category, ensemble,
rank-parity); closing any one leaves the residual counting bit intact. The bit
is the same one the two retained no-gos already decline to rank.

**N3 — Hidden-wall scan.** "Record-degenerate" is grounded in the rank-2 doublet
eigenprojector of `S`; "the mass record resolves the doublet" in the three
distinct `H`-eigenvalues; the ensemble prong's `I/3` is the `C`-invariant
maximally-mixed state, used admission-independently.

**N4 — Residual matching.** D3 attacks the record-count component; it leaves the
weight/measure component (the `(1,1)`-vs-`(1,2)` bit) untouched. The
`koide_frobenius_isotype_split_uniqueness` and `action_normalization` no-go rows
are cited only for the known absence of an in-repo ranking principle.

**N5 — Rhetoric audit.** "D3 does not force `(1,1)`" means the doublet
record-degeneracy of the sharp `S`-instrument does not fix the sector weight that
enters `Q`. It does not mean no future records-native principle, doublet-frame
quotient, or readout-class theorem can supply it.

**N6 — Partial-closure path.** The Boundary lists four open forward handles; this
note requires no new axiom and does not foreclose import retirement by a later
bounded theorem.

**N7 — Steelman.** A hostile reviewer privileging `S` as the `T`-even
einselected static pointer is granted the point — but `rank(P_doublet) = 2` is
`T`-parity invariant, and a 2-outcome `S`-record yields outcome probabilities,
not the `√m` amplitudes that build `Q`; so even with `S`-privilege the weighting
stays unfixed.

**N8 — Cross-cycle echo.** The same `(1,1)`-vs-`(1,2)` bit appears in the
readout demarcation note, the `det_R`-vs-`det_C` analysis, and the two retained
no-go rows. D3 sharpens its statement without relabeling it as an axiom gap.
