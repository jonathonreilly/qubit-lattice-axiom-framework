# Orbit-Occupancy and the R-D Durability Bridge Are Extensionally Equivalent on the Registered Surface and Strictly Inequivalent Off It: the Standing Owner Decision Is One Decision with Two Formulations (Bounded Theorem)

**Date:** 2026-06-11
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. This source note
does not set or predict an audit outcome, does not adopt, draft, or route
any premise, and does not edit the audit-lane-owned Tier-A registry or any
audit data file.
**Primary runner:**
[`scripts/frontier_koide_oo_rd_premise_equivalence_2026_06_11.py`](../scripts/frontier_koide_oo_rd_premise_equivalence_2026_06_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_oo_rd_premise_equivalence_2026_06_11.txt`](../logs/runner-cache/frontier_koide_oo_rd_premise_equivalence_2026_06_11.txt)
(SCORECARD: PASS=9, FAIL=0)

> **Not claimed:** adoption of either premise, a logical implication between
> the premise *sentences*, or any audit status. **Claimed (bounded,
> consequence-level):** on the current registered surface the two named
> premise candidates for the Koide occupancy atom — **orbit-occupancy** (OO,
> static slot-counting) and the **R-D durability bridge** (dynamical
> records-flow invariance) — force the **identical registered
> configuration** `(r, Q, ρ, Z_d) = (1/2, 2/3, 1, π/g)` and the same
> registered spectrum; and they are **strictly inequivalent** off the side
> conditions, by two computed separation witnesses. Consequence: the
> standing owner decision is one decision with two formulations.

## The question this answers

The R-D chain note
([`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md))
named the open question: are R-D and the orbit-occupancy candidate of
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
equivalent, independent, or one-way related on the current surface? This
note computes the answer at the consequence (registered-configuration)
level — the level at which the owner decision actually consumes them.

## Results (runner, 9/9)

**R1 — both chains recomputed end to end.** The OO chain with the occupancy
note's orientation guard reproduced (both ρ-map orientations computed; the
landed one matches the landed cells, the inverted one is rejected):
`Z_d = π/g → ρ = 1 → r = 1/2 → Q = 2/3`. The R-D chain: stationary set
`{0, 1/2, ∞}`; registered `δ ≠ 0` content excludes 0; the unsigned branch
excludes ∞; the equal-power weight `|b|² = a²/2` is recovered at the forced
point (checks 1–2).

**R2 — extensional equivalence on the registered surface.** Both chains
force the identical tuple `(r, Q, ρ, Z_d/(π/g)) = (1/2, 2/3, 1, 1)`, and
the registered spectrum at the forced configuration (with the lane's
registered `|δ| = 2/9` content, which neither premise touches) is one and
the same — three distinct positive weights (checks 3–4). **Approving either
premise yields the identical downstream surface.**

**R3 — strict inequivalence off the side conditions.** Two computed
separation witnesses, both models of R-D's invariance and violations of
OO's forced value:

- **W1** (`δ` content dropped): the `r = 0` model — records-flow stationary
  (`f(0) = 0`) with the exactly degenerate spectrum (check 5).
- **W2** (signed branch): the `r = ∞` endpoint (`p_d = 1`, stationary) —
  exactly the signed/Brannen-branch endpoint, flagged and not consumed
  (check 6).

Conversely, **no witness exists in the other direction** given the Lüders
grounding: an OO registration is `p = (1/2, 1/2)`, the barycenter *fixed
point* of the records flow, so OO registrations automatically satisfy R-D's
invariance requirement (check 7). The consequence-level relation is
strictly one-way: OO is stronger unconditioned; R-D plus the
already-registered lane content delivers the identical configuration.

**R4 — decision corollary.** Both premise statements are interface-pinned
verbatim in their source notes (check 8), and the corollary is recorded as
a statement check (check 9): the standing owner decision is **one decision
with two formulations** — a single `AXIOM_MINIMALITY_POLICY.md` §6 proposal
can carry both, stating them as provably configuration-equivalent given the
registered content, with R-D the strictly weaker unconditioned content and
OO the static formulation. Nothing is drafted or routed by this note.

## Scope and honesty

- The comparison is at the **consequence level given the Lüders records-map
  grounding** (retained_bounded). OO does not itself assert the map; a
  registration theory with non-Lüders re-registration is outside this
  comparison (declared residual).
- The side conditions consumed are the lane's own registered content at its
  admitted statuses: the `δ ≠ 0` registration and the unsigned
  charged-lepton branch. No PDG value enters anywhere.
- Both chains consume the 2-sector partition prong (custody selector i) and
  the landed ρ-map orientation at their declared grades. The partition
  prong remains the irreducible admitted choice — this note relates the two
  candidate premises *for the remaining atom*; it does not shrink the
  partition prong itself.
- W2 connects the inequivalence to physics: under OO-everywhere no sector
  occupies the signed endpoint, while R-D permits it on the signed branch —
  a discriminator that the Brannen-branch program (named in the R-D note)
  could in principle test. Flagged only.

## Dependencies (citation-graph visible)

- [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
  (the OO premise statement, the landed cells and orientation guard)
- [`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  (the R-D premise statement and chain)
- [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
  (the records map and its retained_bounded grounding)
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  (the partition prong both chains consume)

## Reprove-and-cite ledger

- **Reproven here (runner):** both ρ-map orientations against the landed
  cells; the OO chain arithmetic; the stationary set; the degenerate and
  `Σλ = 3a` identities; the configuration tuples and their equality; the
  registered spectrum at the forced point; both separation witnesses; the
  barycenter fixed-point fact; the premise-statement interface pins.
- **Cited at declared grade:** the Lüders grounding; the custody partition
  prong; the registered `δ` content; the occupancy note's independence
  result (unchanged by this note: the atom is still not derivable — this
  note relates the two candidate *premises* for it).

## Verification

```bash
python3 scripts/frontier_koide_oo_rd_premise_equivalence_2026_06_11.py
```

Expected: 9 `[PASS]` lines, four `RESIDUAL (declared-open)` lines, then
`TOTAL: PASS=9 FAIL=0` and the verdict paragraph. Exit code 0 iff FAIL=0.

**Independent audit required.** This note asserts no effective-status
change.
