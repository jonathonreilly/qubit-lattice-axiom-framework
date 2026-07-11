# The First-Order Section Question — Tie-at-Weight vs Label-at-Outcome: the Landed Surface Constrains the Measure's Holomorphy and Each Cell's Arithmetic but Is Silent on the K-Reality Stage; the r=1 vs r=1/2 Binary Is Exactly That Stage (Bounded Residual-Localization Theorem)

**Date:** 2026-07-11
**Claim type:** bounded_theorem (exact residual-localization). This source
note does not set or predict an audit outcome, does not adopt any premise,
and does not edit any audit-lane-owned registry or data file.
**Primary runner:**
[`scripts/frontier_koide_first_order_section_question_2026_07_11.py`](../scripts/frontier_koide_first_order_section_question_2026_07_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_first_order_section_question_2026_07_11.txt`](../logs/runner-cache/frontier_koide_first_order_section_question_2026_07_11.txt)
(SCORECARD: PASS=16, FAIL=0)

> **Not claimed:** a derivation of `r = 1/2` or `r = 1`, adoption of any
> occupancy/weighting/reading-section rule, retirement of any admission,
> or any audit status. **Claimed (bounded):** on the staggered first-order
> surface, the decisive count-once/count-twice binary is *exactly* the
> binary "does K-reality act on the statistical WEIGHT (tie the section
> before the Berezin integral → count-twice → `r = 1`) or on the
> REGISTERED OUTCOMES (a reality condition on records after integration,
> weight staying first-power holomorphic → count-once → `r = 1/2`)". The
> landed constraints — the `|det M|²` r=1 wall and the reflection-
> positivity second-order wall — both act on the Hermitian/second-order
> *transfer* family; on the corner sector every spatial reflection is the
> identity, so reflection positivity's positivity content coincides with
> the complex-conjugation antiunitary that *is* this binary. Both cells
> are exhibited as lawful. The binary is therefore an **exact residual**,
> not a closed question, and it equals the custody note's already-admitted
> K-reality selector.

## Role — the sharpened open lead this executes

The supertrace/holomorphic open lead
([`SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md`](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md))
asked whether the generation fluctuation determinant counts the complex
doublet parameter `b` once (holomorphic → `r = 1/2`) or its two real
components separately (vector → `r = 1`). The staggered first-order block
([`KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md),
PR #3551) proved the measure side is first-order and localized count-twice
`|b|²` onto the K-reality restriction `c = conj(b)`. The channel-generality
companion
([`KOIDE_GENERATION_CHANNEL_SPACE_HOLOMORPHY_CHANNEL_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_GENERATION_CHANNEL_SPACE_HOLOMORPHY_CHANNEL_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-06-11.md))
proved holomorphy is channel-independent and count-twice arises exactly on
antiunitary-tied parameter sections. What remained was the *physical*
question those two notes deliberately left open: does the physical matter
action put the tie in the **weight**, or does K-reality act only as a
**label on registered outcomes**? This note does the exact computation and
answers it in the honest genre available: the landed surface does not
decide it, and the residual is named exactly.

## The four computed facts (runner, 16/16)

### A. The first-order determinant on the hw=1 corner triplet (reproduced)

The hw=1 corner triplet carries the generation `C_3` cycle `C` (`C³ = I`,
`C` not symmetric). The one-component staggered measure's coupling there is
the circulant `W = a·I + b·C + c·C²`. Computed by explicit exterior-algebra
expansion (nested single-generator Berezin integrals; **no determinant
identity assumed** at any point), the partition function is

```text
Z = det(W) = det3(a,b,c) = a³ + b³ + c³ − 3abc = lam0 · (lam_omega · lam_omegabar),
```

to the **first power** — `lam0 = a+b+c` the singlet, `lam_omega · lam_omegabar`
the doublet factor, one Berezin power each (checks 1–4). The measure does
not produce `|det|²`.

### B. Both sections, exactly

- **Untied holomorphic section** (`b, c` independent): the doublet weight
  `lam_omega · lam_omegabar` is a **holomorphic polynomial** in `(a,b,c)` —
  no conjugate, `∂/∂b̄ = 0` identically. The doublet is **one complex slot
  per K-orbit** (the ω/ω̄ pair is one K-orbit); count-once (check 5).
- **K-real tied section** `c = conj(b)`: the first-power weight becomes
  **non-holomorphic** — Wirtinger `∂²det3/∂b∂b̄ = −3a` (Laplacian `−12a`),
  the doublet weight depends on `|b|²`; count-twice enters **exactly and
  only** through the tie (check 6, PR #3551 localization reproven).
- **Fork-cell landing** (note 6 + the two realized-state equipartition
  laws, reproven; the ρ-map / Z-ratio arithmetic withdrawn by the
  2026-07-11 repairs is **not** used): the untied holomorphic section is
  the per-outcome-cell law `E_s = E_d` → `r = 1/2`, `Q = 2/3`; the tied
  section is the per-real-mode law `E_s = ε, E_d = 2ε` → `r = 1`, `Q = 1`
  (check 7, exact solves). This is exactly PR #3551's localization:
  count-twice **iff** the tie.

### C. Reflection positivity does not touch the first-order measure

- The RP wall
  ([`KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md))
  rejected the **bare first-order operator** `W_h = a·I + b·C` as a transfer
  object because it is non-self-adjoint for generic `b` (`Cᵀ = C² ≠ C`), and
  forced the second-order Hermitian corner Dirac `D = [[0,M],[M†,0]]` with
  `det D = −|det M|²` (checks 8–9, exact at a complex parameter point — the
  modulus is the count-twice content; the `−` is the odd-block sign recorded
  in the RP no-go). That is a statement about the **transfer family**, not
  the measure.
- The first-order **measure** `Z = det(D_stag + A)` is a *different* object:
  `D_stag` is the reflection-positive staggered kinetic (real antisymmetric)
  and the one-component measure gives `det` to the **first power**, not
  `|det|²` (check 10). The RP rejection of `W_h`-as-transfer does not touch
  this Grassmann weight.
- **The corner fact.** Every spatial lattice reflection `x_μ → −x_μ` acts as
  the **identity** on all 8 corner modes (each corner plane wave is
  2-torsion). So on the corner sector the Osterwalder–Schrader reflection
  reduces to complex conjugation of the coupling `A → conj(A)` — the **same
  antiunitary K** whose tied sections the fork already classifies (check 11).
  Reflection positivity adds **no independent closing constraint** beyond the
  K-reality selector: "RP forces the tie" and "K-reality forces the tie" are
  one antiunitary condition, and whether it acts on the weight or the
  outcome is precisely the residual.

### D. The finite discriminator and the adjudication

- **Discriminator I (conjugate-degree of the physical weight).** The untied
  doublet weight has `b̄`-degree `0` (holomorphic; `∂/∂b̄ = 0` → LABEL /
  outcome → `r = 1/2`); the `c = conj(b)` tied weight has `b̄`-degree `> 0`
  (non-holomorphic → TIE / weight → `r = 1`). A single finite invariant
  separates the two cells (check 12).
- **Discriminator II (reality stage of `Z`).** The untied first-power
  partition function is generically **complex**; on the tie it is **real**.
  So "at what stage does `Z` become real" is the discriminator: at the
  **weight** (tie, before integration) or at the **outcome** (label,
  reality of registered records after integration) (check 13).
- **Both cells are lawful.** Cell TIE reproduces the `r = 1` wall
  (`|det M|²`, Hermitian coupling, `arg det M` real at the weight). Cell
  LABEL is the one-component holomorphic measure whose **registered**
  spectrum is the same real `lam_k = a + 2|b|cos(δ + 2πk/3)`. Both cells
  share the **identical physical spectrum**; they differ only in the
  analytic type of the weight — i.e. in the mode count `r` (check 14).
- **Theta-structure consistency.** `arg det M` real holds in **both** cells:
  Cell TIE enforces it at the weight (Hermitian `M`), Cell LABEL at the
  outcome (real registered spectrum). The theta discharge consumed
  "`arg det M` real" as an **outcome** condition, so untying the weight
  (Cell LABEL) does **not** break the theta discharge's consumed structure
  (check 15).

## The result, named exactly

> On the staggered first-order surface the landed constraints **fix** two
> things — the one-component measure is holomorphic in the untied couplings
> (count-once), and the reflection-positive/Dirac transfer object is
> second-order (`|det M|²`, count-twice) — and fix each cell's internal
> `r`-arithmetic. They are **silent** on the one remaining step: whether the
> physical charged-lepton matter action puts K-reality in the **weight**
> (tie `c = conj(b)` before the Berezin integral → count-twice → `r = 1`) or
> in the **registered outcomes** (a reality condition on the ω/ω̄ K-orbit
> records after integration → count-once → `r = 1/2`). Both cells are
> lawful. The binary `r = 1` vs `r = 1/2` **equals** the binary "K-reality
> acts at the weight (tie the section `c = conj(b)` before the Berezin
> integral) vs at the outcome (K-orbit grouping of registered records after
> integration)", which **is** the custody note's already-admitted K-reality
> selector, not a landed derivation. (The Hermitian corner Dirac is the
> **tied-section realization** of the weight horn — the K-tied point of the
> holomorphic channel family, per the channel-space companion — not an
> independently forced distinct object.)

This converts the supertrace open lead from "an unevaluated candidate route"
into an **exact residual**: a single finite discriminator (the conjugate-
degree of the physical doublet weight, equivalently the reality stage of
`Z`) whose value is not fixed by any landed constraint, with **both** values
exhibited as lawful cells.

## Consistency checks (spelled out)

- **Against the r=1 wall**
  ([`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md)).
  Cell TIE reproduces that wall exactly (`|det M|²`, `r = 1`; the index a
  signed mode-count, the wrong functional type for a ½-reweight). That note
  is explicitly **bounded**: quoting it at claim scope — *"It does not prove
  `Q = 2/3` impossible — the signed / `U(1)_b` one-slot readout remains
  genuinely OPEN; this note closes only the index route on the realization."*
  Cell LABEL **is** that genuinely-open signed / one-slot readout, realized
  here as outcome-level K-labeling. No contradiction: this note does not
  re-open the index route (a signed mode-count is not an energy reweight);
  it locates the still-open readout as the weight-vs-outcome stage.

- **Against the RP second-order wall**
  ([`KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md)).
  Quoting it at claim scope — *"Non-tracial, chiral, finite-gap, explicit
  block-measure, supersymmetric/holomorphic-superpotential, or other
  physical readout routes remain outside this no-go,"* and its N6 lists
  *"explicit block-measure rule … could supply a separate selector."* The
  one-component staggered measure (Cell LABEL) is inside those declared-open
  routes. The RP row of that note constrains `W_h`-as-transfer; the corner-
  reflection computation (check 11) shows RP's corner content is the same
  antiunitary K, not an additional wall. No contradiction.

- **Against the theta structure.** The K-reality predicate `c = conj(b)` is
  shared with the retired theta mass-side reading (`arg det M` real). This
  note does **not** unconditionally untie the section: it exhibits **both**
  cells, and check 15 verifies that `arg det M` real holds in both — Cell
  TIE at the weight, Cell LABEL at the outcome. Because the theta discharge
  consumed `arg det M` real as an **outcome** condition (a reality of the
  registered determinant), Cell LABEL (untie the weight) places K-reality
  exactly where the theta discharge already lives and does not disturb it;
  Cell TIE trivially preserves it. The theta discharge is therefore
  **agnostic** to the tie/label binary — it constrains the outcome, not the
  stage — so it neither closes nor is broken by this residual.

## What this note does NOT claim

- **Not** a derivation of `r = 1/2` or `r = 1`; no occupancy, weighting, or
  reading-section rule is adopted or derived. Both cells are lawful.
- **Not** a re-opening of the index route or a contradiction of the landed
  `r = 1` walls; Cell TIE reproduces them, and the still-open one-slot
  readout is located, not established.
- **Not** a claim that reflection positivity is irrelevant — only that, as
  landed, it constrains the second-order transfer family and its corner-
  sector content coincides with the K-reality antiunitary, so it does not
  independently decide the stage.
- **Not** a claim beyond the bilinear one-component measure on the corner
  sector; interacting/beyond-bilinear actions, gauge-sector or measure-
  normalization contributions, and non-`C_3`-carrier couplings are out of
  scope (channel independence within the bilinear scope is the companion's
  result, cited).
- **Not** a Tier-A registry change, premise adoption, or audit verdict. The
  `AC_φλ` admission and its sub-residuals stand unchanged. No PDG value,
  fitted selector, or empirical comparator is consumed; `r = 1/2` and
  `r = 1` are named only as the landed fork cells.

## Consumed premises (quoted at claim scope)

- One Grassmann pair per site (the one-component measure) — consumed at the
  gate-note grade
  ([`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md),
  §5 residuals: kinetic-class premise, spin-statistics support tier,
  boundary-holonomy convention, `AC_φλ` labeling convention). These are
  inherited and printed by the runner.
- The C_3[111] rotation-channel circulant `W = a·I + b·C + c·C²` is a
  **declared probe coupling** (PR #3551), not a derived Yukawa; the
  channel-space companion establishes the holomorphy/tie split is channel-
  independent across the full `M₄ ⊕ M₂ ⊕ M₂` bilinear equivariant space.
- The K-reality selector `c = conj(b)` is the operative admitted input of
  [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md);
  the orbit-occupancy premise candidate is
  [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md).
  This note **locates** the physical binary onto that selector; it does not
  adopt or derive it.

## Reprove-and-cite ledger

- **Reproven here (runner):** the Grassmann/Berezin first-power identity by
  explicit exterior-algebra expansion; the hw=1 triplet circulant and its
  singlet/doublet factorization; the untied holomorphy (`∂/∂b̄ = 0`) and
  the tied Wirtinger `−3a` localization; the fork-cell arithmetic
  re-derived from the two equipartition-granularity laws (the withdrawn
  ρ-map is not used; see the 2026-07-11 repair companions); the `W_h`
  non-self-adjointness and the `|det M|²`
  second-order object at a complex point; the first-power measure `det(D+A)`;
  the corner-reflection triviality on all 8 modes; the two discriminators;
  both lawful cells with the shared real spectrum; the theta-structure
  outcome consistency.
- **Cited at declared grade:** PR #3551 and the channel-space companion's
  results; the gate-note premises; the landed `r = 1` and RP no-go scopes;
  the custody K-reality selector; the occupancy-atom independence.

## Verification

```bash
python3 scripts/frontier_koide_first_order_section_question_2026_07_11.py
```

Expected: 16 `[PASS]` lines, four `RESIDUAL (declared-open)` lines, then
`TOTAL: PASS=16 FAIL=0` and the verdict paragraph. Exit code 0 iff FAIL=0.

**Independent audit required.** This note asserts no effective-status change.
