# Outcome-Factorization Statistics Atom (R-D Label G3): Not Forced by the Unraveled Step-Law Source Results

**Date:** 2026-07-11
**Claim type:** no_go (narrow)
**Status:** source-side bounded no-go; independent audit required.
**Status authority:** independent audit lane. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
registry, ledger, queue, or publication-status surfaces. The `no_go` label is a
source-side claim-boundary declaration, not an audit verdict.
**Primary runner:** `scripts/frontier_g3_outcome_factorization_unraveled_2026_07_11.py`
**Runner cache:** `logs/runner-cache/frontier_g3_outcome_factorization_unraveled_2026_07_11.txt`

## Boundary

This note proves a narrow negative boundary for the outcome-factorization
statistics atom (R-D label G3) of the R-D bridge anatomy. The unraveling-lane source-note results, quoted at their
declared claim scope (their current audit rows are `unaudited`), do **not** force
the two-registration outcome-factorization law

```text
m(j,k) = p_j p_k,   j,k in {s,d}
```

on the registered two-outcome quotient. The reason is structural: the source
notes characterize one edge's marginal trajectory law and explicitly leave
cross-edge independence untested. Couple two copies of that entire one-edge law
either independently or by a shared trajectory draw. Both couplings preserve
the complete one-edge marginal law, hence every statistic U1/U2/U4 actually
reports, while the shared-draw coupling is not cross-edge independent. On the
binary registered quotient this is instantiated by the correlated-stack witness
`rho_corr`, which shares both one-registration reduced states with
`rho_product` but violates factorization.

This is not a global no-go against future outcome independence. It prunes one
specific repair route — "read factorization off the landed unraveled step-law
source results" —
and re-aims the lane onto the one residual that would actually supply it.

## What the Outcome-Factorization Statistics Atom Needs

The R-D bridge anatomy note
`RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`
proves G1 (pinching is idempotent) and G2 (agreement-conditioned double
registration gives `x -> x^2`, i.e. `r -> 2r^2`), and names the remaining atom:

> "(G3) The remaining atom. Therefore the R-D bridge premise, 're-registration
> composes by a member of the retained flow family', reduces on this surface to
> one named statistics atom: independent composition of repeated registration on
> the weight bookkeeping."

The statistics-atom reduction note
`STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_BOUNDED_NOTE_2026-06-12.md`
records that its remaining premise is the quotient-level statement, not a
state-level product:

> "repeated registrations factor on the registered two-outcome quotient:
> `m(j,k)=p_j p_k` for `j,k in {s,d}`."

and names its framework home as the unraveling lane. This note answers the
question of whether that home, as currently proven, discharges the atom.

## The Wall This Note Must Not Contradict (consumed exactly)

The landed source-side no-go
`STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md`
shows, conditional on its one-copy Born-weight premise plus finite scalar
additivity, a one-parameter family of admissible two-registration joint laws
with fixed marginals `(p, 1-p)`:

```text
a = m(s,s),   m(s,d) = m(d,s) = p - a,   m(d,d) = 1 - 2p + a,
max(0, 2p - 1) <= a <= p.
```

The product law is the single interior point `a = p^2`. Its Born-realizable
correlated counterexample is

```text
rho_correlated = diag(p, 0, 0, 1-p)   on   C^2 tensor C^2,
```

which shares the one-copy marginal `diag(p, 1-p)` on both copies but has
`m(s,d) = 0`. This note **extends that witness**, not refutes it: the witness is
the binary quotient of a shared-draw coupling that preserves every one-edge
marginal trajectory statistic. If a downstream reader thinks
the unraveled step law selects the product point, this note exhibits exactly
where that reading fails.

The product-instance criterion bridge
`STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md`
supplies the exact discriminator: the registered quotient cumulant

```text
C_jk = m(j,k) - p_j p_k
```

vanishes iff the quotient factorizes (its P3), and same marginals do not suffice
(its P4). This note uses `C_jk` as the executable factorization discriminator
and confirms `C_jk = 0` is not implied by one-edge marginal information alone.

## The Unraveling Results, Quoted At Their Declared Source Scope

The two unraveling notes are the framework home named for this atom. Their
claim-scope statements are the load-bearing quotations here.

**U1 — exact single-edge unraveling (note
`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`,
result U1).**

> "For both named weak two-outcome instrument classes, the runner verifies Kraus
> completeness. The Born weights in the finite depth-five tree sum to `1` ... and
> the Born-weighted average of conditional states exactly reproduces the
> deterministic channel. This is unraveling consistency, not a new probability
> rule."

This is a property of one registration's instrument. It says nothing about the
joint law of two distinct registered outcomes.

**U2 — non-degenerate single-edge step distribution (same note, result U2).**

> "On the guarded generic full-rank domain ... both the color-blind and
> frame-naming weak instruments have strictly positive Born-weighted step spread."

The object is the **single-edge** induced-link increment
`dU = U_eff(n)U_eff(n-1)†`. Non-degeneracy of a single edge's spread is a
functional of that one edge's law.

**U3 — the four residuals, explicitly open (same note, result U3).** The note
names four inputs it does **not** deliver:

> "stationarity: increments are state-dependent; centrality: ... `E[dU]` is
> non-scalar ...; edge identity: the displayed edge laws differ at order one;
> many-edge structure: **cross-edge independence and convolution structure are
> not tested here**."

The claim-scope note is categorical: the note "does not supply ... a stationary
law, central increments, identical edge laws, cross-edge independence, a CLT, or
a new measure/weight premise."

**U4 — the bi-invariant quasi-stationarity split (note
`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`).**
This is a "retire-mode depth-scan probe ... finite-horizon, small-system, and
instance/seed-labeled; it is not a CLT premise, invariant-measure theorem,
asymptotic stationarity theorem, or new measure/weight premise." Its findings are
adverse to the ingredient factorization needs:

> "(S1) The link-level step mean `E[dU](n)` moves O(1) at every depth step ...:
> no Cauchy decay, no equilibration onset at this system size and horizon."

and what quasi-freezes is scoped tightly:

> "what is quasi-stationary is the bi-orbit-projected spectrum of the step *mean*
> ... — *not* the whole step law; the bi-orbit-quotient **law** remains the named
> open object."

So the one place the lane examines two-time structure, it (i) works on the
induced-link bi-frame, not the registered `{s,d}` quotient, and (ii) finds
non-stationarity, not independence.

## Theorem (narrow no-go)

Let `mu` denote the complete one-edge trajectory law on its finite outcome-tree
space `Omega`, including every depth needed by U4. For a two-edge law `Gamma`,
write `pi_i#Gamma` for its marginal on edge `i`. On the registered binary
quotient, write `sigma = Tr_2 rho = diag(p, 1-p)` and
`C_jk = m(j,k) - p_j p_k`.

**Lemma (one-edge marginal functionals are factorization-blind).** Form two
couplings of the same non-degenerate `mu`:

```text
Gamma_product(x,y) = mu(x) mu(y),
Gamma_shared(x,y)  = mu(x) 1[x=y].
```

Both have marginals `mu` on each edge. Therefore every functional of either
one-edge marginal law takes the same value on the two couplings, including
multi-depth statistics internal to one edge's trajectory. Yet the shared-draw
coupling is not independent whenever `mu` has at least two positive atoms. The
runner verifies this exactly on a three-atom law and verifies the binary quantum
instance `Tr_2 rho_product = Tr_2 rho_corr = sigma` on both copies.
**[checks B3, C1, C4]**

**T1 — the source-note results live at that marginal scope.** U1 and U2 are
computed from one edge's outcome tree and induced-link step distribution. U4 is
multi-time within that same edge, but its depth scan, step-mean spectra, and
second moment still belong to the complete one-edge trajectory law `mu`; they
are not a coupling law between two distinct edges. Most decisively, U3 states
verbatim that "cross-edge independence and convolution structure are not tested
here," while U4 says the quotient law remains open. Thus product and shared-draw
couplings preserve the complete source-note scope while differing on residual 4.
The runner uses exact generic coupling checks and source-text guards; it does not
substitute a made-up step or mean surrogate for the actual U2/U4 runner.
**[checks C1, C2, C3, C4, F1]**

**T2 — factorization is not such an `F`.** The discriminator
`G(rho) = m(s,d) - p_s p_d` takes the value `0` on `rho_product` and `-p(1-p)` on
`rho_corr`, two states with the *same* `sigma`. So `G` does not factor through
`Tr_2`; equivalently, it is a property of the coupling `Gamma`, not either
one-edge marginal `mu`. It lives strictly above the source-note scope.
**[check D1]**

**T3 — the witness is admissible and does real downstream work.** `rho_corr` is
PSD, trace one, and Born-realizable; at `p = 1/2` it is exactly the 2026-06-18
wall witness `diag(1/2, 0, 0, 1/2)`. Under agreement-conditioning it gives the
identity update `p_i' = p_i`, versus the G2 `x -> x^2` map
`p_i' = p_i^2/(p_s^2 + p_d^2)` that the product state gives. So the correlated
stack collapses the G2 flow; the atom is not a restatement of pinching
idempotence. **[checks A4, B1, B2, D2, F2]**

**Conclusion.** By T1–T3, the entire one-edge source-note law may be coupled
independently or by a shared trajectory draw without changing any one-edge
deliverable, while the two couplings disagree on factorization. The binary
`rho_product`/`rho_corr` pair is the registered-quotient instance and changes the
downstream agreement-conditioned flow. Therefore the declared U1/U2/U4 source
scopes do not force `m(j,k) = p_j p_k`; residual 4 remains the exact missing
cross-edge content. **[checks D1, F3, F4]**

## Escape Conditions (the exact repair set, re-aiming the lane)

Factorization on the registered quotient requires the two-registration joint law
to be

1. **cross-edge independent** — unraveling residual 4, "cross-edge independence
   and convolution structure are not tested here"; and
2. **identically distributed across the two registrations** — unraveling
   residuals 1 (stationarity) and 3 (edge identity), where the source notes find
   the step mean moving O(1) at every depth and edge laws differing at order one.

Together these conditions are sufficient for the equal-`p` target, and neither
condition supplies the other:

- With identical marginals fixed, imposing cross-edge independence as
  `C_ss = 0` solves to `a = p^2`, recovering the product point. So
  **residual 4 is the factorization-critical residual**: the missing coupling
  premise, and precisely the one the lane marks untested. **[check E1]**
- Without identical marginals the target is ill-posed: an unequal-marginal
  product witness (`p1 != p2`) is a valid single-registration law on each copy but
  has no single `p` for which `m(j,k) = p_j p_k` holds. Residuals 1+3 are the
  independent identical-marginal lever. **[check E2]**
- Cross-edge independence together with identical marginals gives the target law.
  **[check E3]**

This sharpens the earlier "four residuals" framing: for the statistics atom, the
decisive residual is residual 4 (cross-edge independence), with residuals 1+3 as
the identical-marginal prerequisite. A positive discharge of G3 must deliver a
cross-edge independence theorem on the registered quotient — not a single-edge
non-degeneracy or a bi-frame quasi-stationarity of the mean, both of which this
note shows are factorization-blind.

## What This Does Not Claim

- This does not refute future outcome independence; it prunes the route that
  reads factorization off the landed one-edge step-law source results.
- This does not assert that actual record dynamics is correlated; `rho_corr` is a
  witness for the insufficiency of the premises, not a model of the physics.
- This does not derive, discharge, or physically select the outcome-factorization
  premise.
- This does not adopt R-D, select an occupancy cell, fix `r`, or select the
  wave-9 tri-guise dictionary.
- This does not promote, demote, or set the audit status of the unraveling notes,
  the wall, the bridge, the R-D anatomy note, or any dependency.
- This does not add a probability axiom or a new Record axiom.
- This does not upgrade the unraveling lane's Born assembly chain. The binary
  density-matrix realization is an explicit conditional state-form/Born input;
  the cited Gleason/Busch source rows are currently `unaudited`.
- This does not import any unraveling `C^3` instrument value onto a derivation
  path. It consumes only the source notes' declared one-edge scope and explicit
  statement that cross-edge independence is untested. **[check F1]**

## No-Go Discipline Gate

**Status: PASS.** The claim is narrow: the declared U1/U2/U4 source scopes are
properties of one edge's complete marginal trajectory law and explicitly leave
cross-edge independence untested. They do not force quotient-level
two-registration factorization.

**N1 alternative routes.**

| route | attempt | disposition |
| --- | --- | --- |
| single-edge non-degeneracy (U2) | Read joint factorization off the non-degenerate single-edge step spread. | ATTEMPTED: the diagonal/shared-draw coupling preserves the entire one-edge law, including its non-degenerate spread, while changing the cross-edge coupling (checks C3-C4). |
| bi-frame quasi-stationarity (U4/S2) | Use the full depth-scan law, including the quasi-frozen bi-orbit-projected mean spectrum, as the joint-law selector. | ATTEMPTED: treating the whole one-edge trajectory as the coupled random variable preserves every U4 statistic under product and shared-draw couplings; U4 also says the quotient law remains open (checks C4, F1). |
| exchange symmetry | Add symmetry under swapping the two registrations. | ATTEMPTED: the correlated witness is swap-symmetric and non-factorized (check B4). |
| two-copy Born realization | Require a density-matrix witness on `C^2 tensor C^2`. | ATTEMPTED: both `rho_product` and `rho_corr` are constructed and realize the same marginals (checks B1-B4). |
| cross-edge independence (residual 4) | Supply the many-edge independence content directly. | ATTEMPTED: this succeeds only by adding the exact premise the source note marks "not tested here." With identical marginals fixed, `C_ss=0` forces `a=p^2` (check E1). This is the named escape, not a refutation of the scoped no-go. |
| identical marginals / edge identity | Supply residuals 1+3 so the two registrations share one `p`. | ATTEMPTED: identical marginals make the equal-`p` target well-posed but do not imply independence; `rho_corr` already has identical marginals (checks B3, E2). |

**N2 wall independence.** The no-go itself has one wall: one-edge marginal laws
do not determine their cross-edge coupling. The positive escape has two
conditions, whose pairwise audit is:

| pair | closing first closes second? | closing second closes first? | independent? |
| --- | --- | --- | --- |
| cross-edge independence / identical marginals | no — an unequal-marginal product law is independent | no — `rho_corr` has identical marginals but is correlated | yes |

The collapsed set therefore remains two conditions for the equal-`p` target,
with residual 4 the factorization-critical coupling condition once identical
marginals are fixed.

**N3 hidden-wall scan.** The phrases "supplied," "single-edge," "source-note
scope," and "Born-realizable" were checked. The two unraveling rows are
currently `unaudited`; no grade is imported from them. Their instrument values,
seeds, and measured spectra are not used. The proof consumes their explicit
one-edge scope and non-delivery statement, plus an explicit conditional
state-form/Born realization of the binary quotient (check F1).

**N4 residual matching.** Every witness citation was checked against the exact
residual:

| cited witness | residual attacked there | residual used here | match? |
| --- | --- | --- | --- |
| `STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS...` | fixed one-copy marginals leave the joint parameter `a` free | same marginals, differing joint; `rho_corr` specializes to its `p=1/2` witness | yes (check F2) |
| `STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE...` P3/P4 | `C_jk=0` iff quotient factorizes; same marginals do not suffice | executable discriminator for the same binary quotient | yes (check B5) |
| `UNRAVELED_RECORD_TRAJECTORIES...` U3 | cross-edge independence/convolution not tested | residual 4 is the missing coupling premise | yes (check F1) |
| `UNRAVELED_STEP_LAW_BI_INVARIANT...` | bi-orbit-quotient law remains open | no joint quotient law is inferred from its one-edge depth scan | yes (check F1) |

**N5 rhetoric audit.** The tested resolution is one-edge marginal trajectory
law versus a two-edge registered quotient coupling. Per-outcome and per-edge
marginals are preserved; the negative conclusion is only at the cross-edge
joint-law level. No per-site, all-mode, all-block, lattice-wide, or all-dynamics
impossibility is claimed. Future cross-edge-independence, stationarity/edge
identity, or reset theorems remain valid escapes.

**N6 partial-closure path scan.** The note does not say a new axiom or primitive
is required. The named closure is a framework-native cross-edge independence
theorem on the registered quotient (residual 4), plus an identical-marginal /
stationarity theorem (residuals 1+3). Approved future theorems are not treated as
bounded walls.

**N7 steelman.** Grant the strongest honest reading: take the complete actual
one-edge outcome-tree/trajectory law, not merely its U2 spread or U4 reported
moments. Couple two copies independently or by one shared trajectory draw. Both
couplings preserve the full one-edge law exactly, while the shared coupling is
not independent when the law is non-degenerate (checks C4, F3). Thus even the
strongest one-edge package does not fix the cross-edge coupling. A future
cross-edge-independence theorem would close the escape and would not contradict
this scoped no-go.

**N8 cross-cycle echo.** The 06-18 same-marginal wall remains live under the
whole-law coupling argument, while the 06-17 product-instance criterion names
the exact `C_jk` repair.
[`PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`](PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md)
already records residual 4 as untested rather than impossible. None has since
been retired by convention, primitive registration, or a new theorem. The
current note therefore preserves the prior wall and its positive repair route
instead of foreclosing it (check F4).

## Consequence For The Statistics Atom

After this note, the outcome-factorization statistics atom's open content is unchanged in substance but sharper
in aim: the missing premise is a **cross-edge independence theorem on the
registered two-outcome quotient** (unraveling residual 4), with an
identical-marginal / stationarity theorem (residuals 1+3) as prerequisite. The
landed source-note deliverables — single-edge non-degeneracy and bi-frame
quasi-stationarity of the step mean — are demonstrably factorization-blind and do
not discharge it. The two 2026-07-10 audits that named factorization as the
missing retained bridge are answered at source scope: the unraveling lane, as
currently stated, is not that bridge; residual 4 is where the bridge must be
built. Independent audit still owns every dependency grade.

## Dependencies

- [`RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`](RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md)
  — names the G3 atom this note attacks.
- [`STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_BOUNDED_NOTE_2026-06-12.md`](STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_BOUNDED_NOTE_2026-06-12.md)
  — the reduction whose remaining premise is `m(j,k)=p_j p_k`.
- [`STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md`](STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md)
  — the wall; this note extends its `rho_corr` witness through the unraveling
  premises.
- [`STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md`](STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md)
  — supplies the quotient cumulant `C_jk` used as the factorization discriminator.
- [`PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`](PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md)
  — records outcome factorization as the downstream premise and quotes
  cross-edge independence as untested.
- [`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — U1, U2, and the four residuals (residual 4 = cross-edge independence).
- [`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — U4; the bi-orbit-projected mean-spectrum readout and the S1 non-stationarity
  finding.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency, context note, premise, or bridge. The independent audit
lane is the only status authority. Quoted source prose is not treated as a
dependency grade.

## Verification

Run:

```bash
python3 scripts/frontier_g3_outcome_factorization_unraveled_2026_07_11.py
```

Expected:

```text
TOTAL: PASS=22 FAIL=0
VERDICT: narrow no-go passes. ...
```
