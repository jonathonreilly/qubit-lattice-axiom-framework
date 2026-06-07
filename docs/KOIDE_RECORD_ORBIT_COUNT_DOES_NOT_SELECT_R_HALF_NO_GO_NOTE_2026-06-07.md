# Koide r: Record K/CPT-Orbit Counting Does Not Select r=1/2 (Refuted Re-Walk)

**Date:** 2026-06-07
**Claim type:** no_go (closes a re-walk-prone orbit-count route; relocates the open atom)
**Scope:** route-pruning no-go
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_record_orbit_count_does_not_select_r_half_2026_06_07.py`](../scripts/frontier_koide_record_orbit_count_does_not_select_r_half_2026_06_07.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_record_orbit_count_does_not_select_r_half_2026_06_07.txt`](../logs/runner-cache/frontier_koide_record_orbit_count_does_not_select_r_half_2026_06_07.txt)

---

## Role

The highest-leverage Tier-A admission is **AC_φλ** (the generation mass-pattern input,
leverage 41); its no-go portfolio is entirely Koide. This note tests the
highest-leverage sub-atom — the charged-lepton Koide `r = |b|²/a²` (empirically `1/2`
→ `Q = 2/3`, vs the framework's clean-dynamics `r = 1`) — with the methodological lens
the Lorentz arc sharpened: *audit whether an imported verdict rests on a premise that
does not hold for the framework's actual (Record) observable.*

The lens correctly identifies that the framework's `r = 1` rests on the
**Coleman–Weinberg effective-potential modulus** `Tr log M†M` (an *imported* QFT
object), and that the CW note
([`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md))
explicitly leaves the **"Record/center-state selector -> could choose (1,1)"** route
OPEN. So the candidate: does the framework's actual observable — the **Record**
(realized outcome = the K/CPT **orbit** of the central sector) — give the
orbit/multiplicity count `(1,1)` → `r = 1/2`?

**Answer (verified + adversarially checked vs the landed refutations): no.** The
K/CPT orbit count is not a weighting rule and does not select `(1,1)` by itself. If one
adds the retained tracial/dimension block readout, the same central-sector split gives
`(1,2)` and hence `r = 1`; that is a comparator calculation, not a new consequence of the
Record axiom. The note closes the Record-orbit-count route and **relocates** the genuine
open atom. Runner **9 PASS / 0 FAIL**. No new axiom.

## The argument (and why the lens does not crack it here)

### Orbit-count temptation
`C₃` irreps `{1, ω, ω̄}`; `K`/CPT (~ complex conjugation) gives exactly **2 orbits**:
`{1}` and the conjugate pair `{ω, ω̄}`. An *orbit/multiplicity* count weights the
doublet once → `(1,1)` → `r = 1/2`. This is what the lens reaches for.

### With a supplied tracial/dimension readout, the comparator gives r=1
The Record axiom itself supplies no weighting rule. Under the separate retained
tracial/Born block measure, `ρ = I/3` gives block weights `(1/3, 2/3) = (1,2)`
(dimension) → `r = 1` → `Q = 1`. The PMNS record-central-sector note states the same
boundary: the tracial/dimension measure weights blocks by dimension, while the `r=1/2`
weight is a separate harder gap. Therefore the orbit count does **not** license
`r=1/2`; the dimension-weight comparator lands on `r=1` only after adding that separate
readout convention.

### (C) The category error (asserted, not derived)
`K`/CPT acts on irrep **labels** `{ω, ω̄}`. But the lepton masses are **three real
eigenvalues** of the **K-real** Hermitian `M` (`K(M)=M`): `K` does **not** identify
`μ` with `τ` — they are three distinct realized states. "The doublet is one complex
mode `b`" is a property of the **operator**, not of the **readout**. The slide from
"`K` swaps `ω↔ω̄` as labels" to "the readout counts the doublet once" is the asserted
step — the same *assert-not-derive* error that sank the prior `det_C` reframe.

### (D) The det_C inversion (the same trap)
The landed Berezin fork
([`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md))
has **K-real/Majorana = 2 real slots → r=1**; holomorphic = 1 complex slot → r=1/2. A
`K`/CPT-**orbit** (i.e. **K-real**) argument aligns with the **r=1** (Majorana) column
— so, tracked honestly, the orbit/reality framing lands on `r=1`, the inversion that
refuted the prior reframe.

### (E) Static structure is measure-neutral
The static chiral structure (`ε`, `J_cs`) is an `SO(2)` rotation that preserves **both**
`det_R` (`r=1`) and `|det_C|` (`r=1/2`). So static structure does **not** select the
readout; the orbit-vs-mode choice is a **dynamics** question.

## Verdict and relocation

- **The Record-orbit-count route to `r=1/2` is a refuted re-walk:** the orbit-count is
  not a weighting rule; with the separate tracial/dimension readout it weights by
  dimension -> `r=1`, and a K-real orbit argument hits the `det_C` inversion -> `r=1`.
- **The genuine open atom is relocated, precisely:** `r=1/2` requires the
  **operator/action** to be **holomorphic** — a *first-order* Dirac/Berezin **index**
  count (weights `b` once → `(1,1)`) rather than a *second-order* modulus (weights
  `Re b, Im b` → `(1,2)`). That is the **gated staggered-Dirac mass/Yukawa structure**
  (AC_φλ substep-4), a **dynamics** question, and it is **measure-neutral to static
  structure** (E). It is **not** a Record-readout question.

## Methodological note (the lens, honestly)

The lens — *audit whether the imported "r=1" premise (the CW modulus) holds for the
framework's Record observable* — correctly flagged that `r=1` rests on an imported QFT
object. But the adversarial check found that the Record-orbit alternative does **not**
supply the missing `(1,1)` weighting, while the separate tracial/dimension readout gives
`r=1`. So unlike the Lorentz case (where the imported Collins verdict genuinely
mis-applied to the fixed theory), here the lens does **not** crack the wall: the orbit
route is not a weighting rule, and the dimension-readout comparator is not `r=1/2`. The
residual is the **operator-dynamics gate** (holomorphy of the staggered-Dirac mass determinant),
not the readout. This closes the Record-orbit route (preventing a future re-walk) and
sharpens AC_φλ to the first-order-index-vs-second-order-modulus dynamics question.

## What this note does NOT claim

- It does **not** prove `Q=2/3` impossible — the operator-holomorphy route (first-order
  Dirac/Berezin index on the gated staggered-Dirac corner) remains genuinely OPEN.
- It does **not** claim `Q=1` is the framework's final charged-lepton prediction; it
  closes only the **Record-orbit-count** sub-route and relocates the atom.
- It does **not** treat Record as a source of weights, probabilities, occupancy, or
  within-sector data.
- **No** new axiom, primitive, repo vocabulary, or class tag; the landed Koide/PMNS/
  Berezin notes and literature (Coleman–Weinberg; Rivero–Gsponer) are comparator only.
  It sets **no** audit status.

## No-go discipline (N1–N8 summary)

- **N1:** routes — (1) orbit-count `K`/CPT labels -> `(1,1)`: **ATTEMPTED, ruled out**
  because orbit count is not a weighting rule; (2) tracial/dimension readout -> `(1,2)`:
  **ATTEMPTED comparator**, gives `r=1` only after a separate readout convention; (3) CW
  modulus -> `r=1`: **RULED OUT as the `r=1/2` source** by the landed modulus note; (4)
  operator-holomorphy/first-order-index -> `r=1/2`: **OPEN**, relocated as the live route;
  (5) static `ε/J_cs` structure: **ATTEMPTED**, measure-neutral. **N2:** the orbit-count,
  dimension-readout, CW-modulus, and holomorphy walls are independent. **N3/N5:** no
  phrase says Record itself supplies weights; the no-go is scoped to the orbit-count
  route. **N7 steelman:** the open-gate note never claimed the readout was holomorphic —
  accepted; that is exactly why this closes only the orbit-count sub-route.

## Reprove-and-cite ledger

- **Reproven here** (runner): the `C₃` K/CPT 2-orbit structure; the separate
  tracial/dimension readout weights `(1/3, 2/3) = (1,2)` -> `r=1`; the 3-distinct-real-eigenvalue K-real
  Hermitian `M`; the `SO(2)` measure-neutrality (`det_R`, `|det_C|` both preserved).
- **Cited** (comparator only): the landed CW-modulus, supertrace-index open-gate,
  Berezin det_C/det_R fork, corner-determinant, PMNS record-central-sector, and
  readout-lane notes; Coleman–Weinberg, Rivero–Gsponer.

## Audit dependency repair links

- [SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md)
- [KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md](KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md)
- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

### Source-note boundary

**Hypothesis set:** (1) the Record axiom (realized outcome = K/CPT orbit of the central
sector; finite additive scalar; supplies no weighting/within-sector data); (2) the
`C₃` circulant generation model `M = aI + bC + b̄C²`; (3) the landed `(1,1)`/`(1,2)`
fork and the separate retained tracial/Born block measure. The result is the verified
statement that Record-orbit counting does not select `r=1/2`; the comparator
dimension-readout gives `r=1`; and the open atom relocates to operator holomorphy on the
AC_φλ gate.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (K/CPT orbit, irrep multiplicity vs dimension, tracial/Born measure,
holomorphic vs real determinant, Dirac/Berezin index). No PDG/fitted lepton mass or
measured Koide comparator consumed as a derivation input.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of the CW-modulus, supertrace, Berezin, PMNS, or AC_φλ rows. The audit lane is
the only status authority.
