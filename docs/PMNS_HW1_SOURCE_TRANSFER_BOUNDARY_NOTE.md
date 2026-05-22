# PMNS HW1 Source-Transfer Boundary

**Date:** 2026-04-16 (revised 2026-05-16: pack-to-retained-PMNS bridge made
explicit and proved against an independent Schur-complement certificate)
**Claim type:** bounded_theorem
**Status:** bounded source/transfer interface theorem: if the `hw=1` source/transfer pack is supplied, the retained-interface reconstruction checks close; this note does not derive that pack from `Cl(3)` on `Z^3` and does not promote a retained source law.
**Script:** `scripts/frontier_pmns_hw1_source_transfer_boundary.py`

## Question

Can a genuinely axiom-first `hw=1` source/transfer law on the retained lepton
triplet do better than the current sole-axiom free-profile boundary?

## Bottom line

Yes, conditional on supplying the source/transfer pack, at the retained-interface reconstruction level.

The supplied `hw=1` source-transfer package reconstructs the active/passive
interface data:

1. the active transfer shadow fixes the weak-axis seed pair
   `(xbar, ybar)`
2. the direct corner transport asymmetry fixes the branch bit
3. the active source-response columns fix the active kernel exactly
4. the passive source-response columns fix `q` and `a_i`
5. the combined source/transfer pack reconstructs the retained PMNS pair and
   the downstream Hermitian / PMNS data exactly, with the bridge from the
   supplied response-column pack to the retained `(D_0^trip, D_-^trip)`,
   `(H_nu, H_e)`, masses, and `|PMNS|` proved step-by-step against an
   independent Schur-complement certificate (Part 4 of the runner)

Within that supplied-pack boundary, the PMNS lane is not blocked by an
intrinsic ambiguity in the `hw=1` source/transfer observables themselves.

## Pack-to-retained-PMNS bridge theorem

**Statement.** Let `S_act` and `S_pass` be sector operators whose
3 x 3 supports carry the retained active and passive lepton blocks, and let
`(c_act_i)` and `(c_pass_i)` be the corresponding hw=1 source-response
columns at probe weights `lam_act, lam_pass` (defined as
`(I - lam * delta)^{-1} e_i` with `delta` the active or passive block in the
appropriate convention; see `pmns_lower_level_utils.py`,
`response_columns_from_block`). Define two lanes:

- **Lane A (response-column inversion).** Reconstruct the active and passive
  blocks from the response columns via
  `derive_active_block_from_response_columns` and
  `derive_passive_block_from_response_columns`, assemble the retained pair
  `(D_0^trip, D_-^trip)` from those blocks under the tau classification, and
  run `masses_and_pmns_from_pair` to get `(H_nu, H_e, m_nu, m_e, |PMNS|,
  branch, sheet)`. This is `close_from_lower_level_observables` in
  `scripts/frontier_pmns_lower_level_end_to_end_closure.py`.
- **Lane B (independent Schur certificate).** Take the same sector operators
  and form the retained active/passive blocks via the direct Schur-complement
  effective-block formula `effective_block_from_sector_operator` (no
  response-column helper involved). Assemble the retained pair from those
  blocks under the same tau bit Lane A derives from the columns (the tau
  step is a finite classifier on response-column moments and is shared, not
  re-derived), then run `masses_and_pmns_from_pair` on that pair.

**Claim.** Lane A and Lane B agree exactly (modulo floating-point) on the
retained pair `(D_0^trip, D_-^trip)`, the Hermitian data `(H_nu, H_e)`, the
masses `(m_nu, m_e)`, `|PMNS|`, and the branch/sheet labels.

**Proof sketch.** Lane A composes two operations:
(i) response-column kernel inversion `K = (I - lam * delta)^{-1}` followed
by `delta = (I - K^{-1}) / lam`, which is the algebraic inverse of the
column-build step `K e_i`, so it recovers the block `delta` exactly; and
(ii) the same `masses_and_pmns_from_pair` Hermitian eigen-closure that
Lane B applies. Lane B obtains `delta` instead by Schur complement of the
ambient sector operator on its 3 x 3 retained support. Both lanes therefore
target the same effective block on the retained support, so the downstream
closures agree.

**Certificate.** The equality is verified numerically in
`scripts/frontier_pmns_hw1_source_transfer_boundary.py`, Part 4 (9 checks
spanning `D_0^trip`, `D_-^trip`, `H_nu`, `H_e`, `m_nu`, `m_e`, `|PMNS|`,
branch, sheet, all at machine precision). The bridge step itself
(sector_operator -> retained 3x3 block) is computed by two structurally
disjoint code paths: Lane A composes
`active|passive_response_columns_from_sector_operator` (Schur to support,
then column lift) with `derive_active|passive_block_from_response_columns`
(column inversion to recover the block); Lane B applies
`effective_block_from_sector_operator` directly. Lane B does not call any
`*_response_columns_*` or `derive_*_block_*` helper, and Lane A does not
call `effective_block_from_sector_operator` after its initial column build.
Equality at machine precision on the retained pair is therefore an
independent cross-check of the column-inversion bridge, not a tautological
self-comparison of `close_from_lower_level_observables` against itself
(which was the auditor's flagged failure mode in the previous Part 4).
The downstream Hermitian eigen-closure (`masses_and_pmns_from_pair`) is
shared between the two lanes, so the equality on `(H_nu, H_e, m_nu, m_e,
|PMNS|, branch, sheet)` follows once the retained pair is shown to be the
same; the runner verifies all of them explicitly anyway.

## Exact boundary

The current exact bank still does **not** derive that source/transfer pack
from `Cl(3)` on `Z^3` alone.

In particular:

- transfer summaries alone are blind to the full 5-real active corner source
- two distinct off-seed active microscopic blocks can share the same transfer
  shadow while differing in the corner-breaking source
- the source-response columns are exactly what repair that blindness and fix
  the active kernel

So the remaining sole-axiom blocker is now sharply isolated:

- not a hidden PMNS-side value ambiguity
- not a branch-selection ambiguity on the retained pack
- not a passive monomial ambiguity

It is the derivation of the actual lower-level source/transfer observables
from `Cl(3)` on `Z^3` alone.

## Consequence

This boundary is the right one for review:

- if the `hw=1` source/transfer pack is supplied, the retained PMNS lane
  closes exactly
- if only the sole axiom is supplied, the current exact bank still does not
  select the nontrivial source/transfer pack

That is the sharpest honest state of the retained source/transfer attack.

## Verification

```bash
python3 scripts/frontier_pmns_hw1_source_transfer_boundary.py
```

## 2026-05-19 audit-conditional repair

**Retained scope narrowed to the bounded interface theorem.**

This note is retained as a `bounded_theorem` about a single, narrow interface
identity:

> **Bounded interface theorem (retained).** Given supplied sector operators
> `S_act, S_pass` carrying the retained active/passive lepton 3 x 3 supports,
> the Schur-complement effective block on the retained support equals the
> response-column reconstruction of that block. Equivalently, on the supplied
> sector operators, Lane A (response-column inversion) and Lane B
> (Schur-complement) agree at machine precision on
> `(D_0^trip, D_-^trip, H_nu, H_e, m_nu, m_e, |PMNS|, branch, sheet)`.
> This is the "Schur = response-column" identity, verified by Part 4 of
> `scripts/frontier_pmns_hw1_source_transfer_boundary.py` (9 checks).

That equality is a structural fact about Schur complements vs.
`(I - lam * delta)^{-1}` column inversion on the retained support. It is the
only claim retained at `bounded_theorem` strength by this note.

**Explicit admissions (audited_conditional).** The following are admitted
inputs to the bounded interface theorem and are **not** derived here from the
sole-axiom bank (`Cl(3)` on `Z^3`):

1. **Fixture-active operators admitted.** The active sector operator
   `S_act` (and equivalently its response columns `(c_act_i)` at probe weight
   `lam_act`, and the active block `delta_act` that the columns invert to) is
   supplied as a fixture. Its existence and value are not derived from the
   sole axiom in this note.
2. **Fixture-passive operators admitted.** The passive sector operator
   `S_pass` (and equivalently its response columns `(c_pass_i)` at probe
   weight `lam_pass`, and the passive block `delta_pass`) is supplied as a
   fixture, with the same admission status.
3. **Tau classifier admitted on the supplied columns.** The tau bit that
   labels which retained slot is active vs. passive is computed by a finite
   classifier on the response-column moments of the supplied fixtures; it is
   shared between Lane A and Lane B and is not re-derived from the sole
   axiom.
4. **Probe-weight conventions admitted.** The probe weights `lam_act` and
   `lam_pass` and the column convention
   `c_i = (I - lam * delta)^{-1} e_i` are conventions imported from the
   supplied pack, not derived here.

**What is explicitly NOT retained.** The following claims are removed from
the retained surface of this note and are now positioned as
audited-conditional / frontier-only:

- any "retained source law" that would derive `S_act, S_pass`,
  `(c_act_i), (c_pass_i)`, or `(delta_act, delta_pass)` from `Cl(3)` on
  `Z^3` alone;
- any retained claim that the `hw=1` source/transfer pack itself is
  axiom-first;
- any retained promotion of the full PMNS lane (`H_nu, H_e, m_nu, m_e,
  |PMNS|`, branch, sheet) to `bounded_theorem` strength on the sole-axiom
  bank. Those downstream values are retained only **conditional on the
  supplied fixtures above**, and the conditional path is exactly the bounded
  interface theorem.

**Effect on prior text.** Sections "Bottom line", "Pack-to-retained-PMNS
bridge theorem", "Exact boundary", and "Consequence" above are retained as
written, but are to be read as statements **about the bounded interface
theorem and its admitted fixtures**: each "fixes" / "reconstructs" /
"closes" clause is conditional on the four admissions in this repair block.
No claim above this block is promoted past `bounded_theorem` strength on the
retained surface by this note.

No hand-authored audit verdict or repo-wide authority surface change is
made by this repair. Promotion past `bounded_theorem` remains gated on
a separate, sole-axiom derivation of the source/transfer pack; generated
audit data is pipeline-owned after landing.
