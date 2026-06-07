# The Active-Sector Assignment (Large PMNS / Small CKM) is Grounded by the Mass-vs-|K| Dominant-Operator Sieve, Not the Refuted Position-Detection Story — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (conditional structural grounding; conditional on the energy-monitoring pointer principle)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/active_sector_mass_vs_k_sieve_grounding_runner.py`](../scripts/active_sector_mass_vs_k_sieve_grounding_runner.py)
**Cached output:** [`logs/runner-cache/active_sector_mass_vs_k_sieve_grounding_runner.txt`](../logs/runner-cache/active_sector_mass_vs_k_sieve_grounding_runner.txt)

## Audit context

[`CKM_SMALL_VS_PMNS_LARGE_FROM_RECORD_READOUT_CONTEXT_NARROW_THEOREM_NOTE_2026-06-06`](CKM_SMALL_VS_PMNS_LARGE_FROM_RECORD_READOUT_CONTEXT_NARROW_THEOREM_NOTE_2026-06-06.md)
established the **conditional** structure — *if* charged leptons/quarks are corner-diagonal and
the neutrino is `C3`-structured, then PMNS is large (a trimaximal column) and CKM is small
(`V_CKM = I`) — and **recorded the failure** of the natural position-detection grounding (the
corner basis is the *momentum* basis, which is generation-blind: a position-local observable has
identical expectation across all three generations). This note **supplies the grounding** that the
detection story could not: the active-sector assignment is the **mass-vs-`|K|` dominant-operator
(energy-monitored) predictability sieve**, which is generation-*dependent* and so dodges the exact
blindness that refuted detection.

## Safe statement

The `hw=1` generation triplet
([`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md),
`retained`) carries two competing operators: the **mass** `M`, diagonal in the **corner**
(position/BZ) basis, and the emergent `C3` coupling `K = |K|·(J − I)`, diagonal in the **`C3`**
(DFT) basis. The pointer/active basis is the eigenbasis of the **dominant** of `{M, K}`.

**Theorem (conditional on energy-monitored pointer selection).**

1. **The dominant operator sets a mass-graded pointer basis.** For `|K| ≪` the generation
   mass-split, the pointer is the **corner** basis (mass eigenbasis); for `|K| ≫` the split, it is
   the **`C3`/DFT** basis, which carries the `C3`-singlet `W = (1,1,1)/√3` and hence a **trimaximal**
   column.
2. **PMNS large.** Charged leptons (heavy, split `≫ |K|`) record in the corner basis (`U_e = I`);
   the neutrino (split `≪ |K|`) records in the `C3` basis. `PMNS = U_e† U_ν` then carries a
   trimaximal column (the recorded `C3`-singlet) and `O(1)` mixing.
3. **CKM small.** Both quark sectors are heavy (`split ≫ |K|`) → both corner-diagonal →
   `V_CKM = U_up† U_dn = I` (the identity element of the retained "shared-`C3` circulants commute ⇒
   `V_CKM` is a permutation" boundary,
   [`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28`](QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md),
   `retained_no_go`) — small / near-diagonal.
4. **The sieve dodges the detection-story blindness.** The mass operator has three **distinct**
   eigenvalues (it distinguishes all generations), whereas a `C3`-invariant (position-symmetric)
   observable has a **degenerate** doublet (generation-blind on the doublet — the detection story's
   fatal flaw). So the mass-vs-`|K|` competition *can* split the sectors where position-locality
   provably cannot.
5. **Monotone threshold.** The sector flips corner ↔ `C3` as its mass-split crosses `|K|`. With
   `|K|` the emergent `C3` coupling at the massless-gravity scale
   ([`DELTA_MAGNITUDE_REDUCES_TO_MASSLESS_GRAVITY_SCALE_NARROW_THEOREM_NOTE_2026-06-06`](DELTA_MAGNITUDE_REDUCES_TO_MASSLESS_GRAVITY_SCALE_NARROW_THEOREM_NOTE_2026-06-06.md)),
   the neutrino's **unique sub-`|K|`** mass-split is what makes **only it** `C3` — large PMNS — while
   every heavier sector is corner — small CKM. This is the
   [`PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26`](PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md)
   (`retained_bounded`) structure, now with the sector assignment grounded.

So the large-PMNS/small-CKM contrast follows from one generation-dependent fact: which of `{M, K}`
dominates the recorded energy in each sector.

## The genuine open piece (the residual)

The grounding is **conditional on the energy-monitoring pointer principle** — that the records
register the eigenbasis of the dominant (energy) operator. This is the einselection **monitor
identity**, the open slot named in
[`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
(`retained_bounded`). This note **replaces the refuted position-detection candidate with the
energy-monitored candidate** — which is generation-dependent and reproduces the pattern — but does
not derive monitor-identity from the minimal axioms. The advance is a *working* grounding where detection
*failed*, with a cleaner residual (energy-monitoring vs the contradicted position-locality).

## Boundary (honest)

- **Conditional, not unconditional.** It holds *given* energy-monitored pointer selection; that
  principle is the residual (the monitor slot).
- **No mass values forced.** The mass hierarchy (neutrino lightest) is the registered input; the
  sieve converts it into the active-sector assignment. No `r`/`Q`/Koide value is touched (this is
  about mixing angles, not mass ratios — it does **not** depend on the firewalled `r=1/2`).
- **No fitted mixing used as input.** The trimaximal column and `V_CKM = I` are *outputs* of the
  corner/`C3` competition; no PDG mixing value enters.
- **Supersedes a refuted grounding, doesn't re-derive it.** The position-detection story is
  recorded-failed in the companion note; this note does not revive it.

## Forbidden imports check

No new axiom. The corner/`C3` operator structure, the dominant-operator pointer, and the PMNS/CKM
matrix elements are exact arithmetic on the retained `hw=1` triplet. `|K|` is the emergent `C3`
coupling already characterized on `main`. The energy-monitoring pointer principle is the framework's
existing (open-slot) einselection mechanism, applied — flagged as the conditional, not imported as a
new axiom.

## Runner check breakdown

Class A: (1) the dominant operator sets a mass-graded pointer (corner for heavy split, `C3`/trimaximal
for light); (2) charged-corner + neutrino-`C3` → trimaximal PMNS column + large mixing; (3)
both-quark-corner → `V_CKM = I` (small); (4) mass has 3 distinct eigenvalues vs a `C3`-invariant
observable's degenerate doublet (generation-distinguishing vs blind); (5) monotone corner↔`C3`
threshold at split ~ `|K|`. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is exact linear algebra on the `hw=1` triplet: the eigenbasis of `M + |K|(J−I)`
is the corner (mass) basis when `M` dominates and the `C3` (DFT) basis when `|K|` dominates; the
latter carries the singlet `W` and yields a trimaximal column. Charged/quark sectors (heavy) land
corner → small near-identity CKM; the neutrino (sub-`|K|` split) lands `C3` → trimaximal PMNS column,
large mixing. The mass operator is generation-distinguishing where a `C3`-invariant position-symmetric
observable is not, so the sieve grounds the split exactly where the refuted detection story could not.
The result is **conditional on the energy-monitoring pointer principle** (the open monitor slot); it
forces no mass value and uses no fitted mixing. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/active_sector_mass_vs_k_sieve_grounding_runner.py
```
