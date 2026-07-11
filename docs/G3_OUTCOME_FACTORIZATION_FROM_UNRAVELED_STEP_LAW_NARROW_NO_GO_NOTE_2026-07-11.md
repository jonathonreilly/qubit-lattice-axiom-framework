# G3 Outcome Factorization Is Not Forced By The Audited Unraveled Step Law

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

This note proves a narrow negative boundary for the G3 statistics atom of the
R-D bridge anatomy. The unraveling-lane premises, quoted at their audited claim
scope, do **not** force the two-registration outcome-factorization law

```text
m(j,k) = p_j p_k,   j,k in {s,d}
```

on the registered two-outcome quotient. The reason is structural: every audited
unraveling deliverable is a **single-registration functional** — a functional
`F(rho) = f(Tr_2 rho)` that reads only the one-registration reduced state — and
the correlated-stack witness `rho_corr` (the 2026-06-18 wall's template,
extended) shares that reduced state with the product state `rho_product`. So the
witness reproduces every single-registration unraveling deliverable while
violating factorization.

This is not a global no-go against future outcome independence. It prunes one
specific repair route — "read factorization off the audited unraveled step law" —
and re-aims the lane onto the one residual that would actually supply it.

## What The G3 Atom Needs (context, at claim scope)

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

The landed no-go
`STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md`
proves that retained one-copy Born weights plus finite scalar additivity leave a
one-parameter family of admissible two-registration joint laws with fixed
marginals `(p, 1-p)`:

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
shown to survive every audited unraveling premise. If a downstream reader thinks
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
and confirms `C_jk = 0` is not implied by any single-registration functional.

## The Unraveling Premises, Quoted At Their Audited Claim Scope

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

Write `sigma = Tr_2 rho = diag(p, 1-p)` for the single-registration reduced
state, and `C_jk = m(j,k) - p_j p_k` for the factorization discriminator.

**Lemma (single-registration functionals are factorization-blind).** If a real
functional factors through the one-registration reduced state,
`F(rho) = f(Tr_2 rho)`, then `F(rho_product) = F(rho_corr)`, because
`Tr_2 rho_product = Tr_2 rho_corr = sigma`. This is exact: the two witnesses are
distinct two-registration states with a common reduced state. **[checks B3, C1]**

**T1 — every audited unraveling deliverable is such an `F`.** U1 (single-edge
unraveling consistency), U2 (single-edge step spread), and U4's readouts (the
step-mean spectrum and its per-depth motion) are all functionals of one edge's
law, hence of `sigma` on the registered quotient. The runner instantiates the
lemma with a random single-registration observable battery, the single-edge Born
weights, a labeled single-edge step-spread surrogate, and a labeled mean-spectrum
surrogate; all four coincide on `rho_product` and `rho_corr`, and the step
surrogate is non-degenerate for `p in (0,1)`. **[checks C1, C2, C3, C4]**

**T2 — factorization is not such an `F`.** The discriminator
`G(rho) = m(s,d) - p_s p_d` takes the value `0` on `rho_product` and `-p(1-p)` on
`rho_corr`, two states with the *same* `sigma`. So `G` does not factor through
`Tr_2`; it lives strictly above the single-registration scope the unraveling lane
occupies. **[check D1]**

**T3 — the witness is admissible and does real downstream work.** `rho_corr` is
PSD, trace one, and Born-realizable; at `p = 1/2` it is exactly the 2026-06-18
wall witness `diag(1/2, 0, 0, 1/2)`. Under agreement-conditioning it gives the
identity update `p_i' = p_i`, versus the retained `x -> x^2` map
`p_i' = p_i^2/(p_s^2 + p_d^2)` that the product state gives. So the correlated
stack collapses the G2 flow; the atom is not a restatement of pinching
idempotence. **[checks A4, B1, B2, D2, F2]**

**Conclusion.** By T1–T3, the audited unraveling premises U1, U2, U4 hold on
`rho_corr` exactly as on `rho_product`, yet `rho_corr` violates factorization.
Therefore the audited unraveling premises do not force `m(j,k) = p_j p_k`. On the
two-registration joint question the lane adds single-edge structure but no joint
content, so it remains at the one-copy-marginal level — exactly where the
2026-06-18 wall bites. **[checks D1, F3, F4]**

## Escape Conditions (the exact repair set, re-aiming the lane)

Factorization on the registered quotient requires the two-registration joint law
to be

1. **cross-edge independent** — unraveling residual 4, "cross-edge independence
   and convolution structure are not tested here"; and
2. **identically distributed across the two registrations** — unraveling
   residuals 1 (stationarity) and 3 (edge identity), where the audited lane finds
   the step mean moving O(1) at every depth and edge laws differing at order one.

These are exactly sufficient and each is independently necessary:

- Imposing cross-edge independence as `C_ss = 0` solves to `a = p^2`, recovering
  the product point. So **residual 4 is the factorization-critical residual**:
  the single premise whose delivery would discharge G3, and precisely the one the
  lane marks untested. **[check E1]**
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
  reads factorization off the audited single-edge step law.
- This does not assert that actual record dynamics is correlated; `rho_corr` is a
  witness for the insufficiency of the premises, not a model of the physics.
- This does not derive, discharge, or physically select the outcome-factorization
  premise.
- This does not adopt R-D, select an occupancy cell, fix `r`, or select the
  wave-9 tri-guise dictionary.
- This does not promote, demote, or set the audit status of the unraveling notes,
  the wall, the bridge, the R-D anatomy note, or any dependency.
- This does not add a probability axiom or a new Record axiom.
- This does not upgrade or consume the unraveling lane's Born assembly chain; the
  Born weights it uses are the retained Gleason/Busch surface, cited, not new.
- This does not import any unaudited unraveling `C^3` instrument value onto a
  derivation path; the witness's single-registration law is a function of `p`
  alone. **[check F1]**

## No-Go Discipline Gate

**Status: PASS.** The claim is narrow: the audited unraveling premises (U1, U2,
U4), being single-registration functionals, do not force quotient-level
two-registration factorization.

**N1 alternative routes.**

| route | attempt | disposition |
| --- | --- | --- |
| single-edge non-degeneracy (U2) | Read joint factorization off the non-degenerate single-edge step spread. | ATTEMPTED: U2 is a functional of one edge's law; it coincides on `rho_product` and `rho_corr` (check C3) and cannot separate them. |
| bi-frame quasi-stationarity (U4/S2) | Use the quasi-frozen bi-orbit-projected mean spectrum as the joint-law selector. | ATTEMPTED: U4's readout is a single-registration mean-spectrum functional (check C4); it also coincides on the two witnesses, and U4 itself finds stationarity failing (S1). |
| exchange symmetry | Add symmetry under swapping the two registrations. | RULED OUT BY PRIOR: the 06-18 correlated witness is already swap-symmetric and non-factorized. |
| two-copy Born realization | Require a density-matrix witness on `C^2 tensor C^2`. | RULED OUT BY PRIOR: both `rho_product` and `rho_corr` realize the same marginals (check B3). |
| cross-edge independence (residual 4) | Supply the many-edge independence content directly. | NOT A LANE THEOREM: note 4 marks residual 4 "not tested here"; note 5 leaves the bi-orbit-quotient law "the named open object". If supplied, `C_ss=0` forces `a=p^2` (check E1) — this is the honest escape, external to the audited premises. |

**N2 wall independence.** The collapsed wall set has one wall: the audited
unraveling premises are single-registration functionals and so cannot force a
two-registration joint property. No inflated independent wall count is asserted;
this is one wall, matched to the 06-18 wall's shape.

**N3 hidden-wall scan.** "Single-registration functional", "single-edge", and
"reduced state" name the scope of the audited premises, not a proof input that
supplies non-factorization. The witness's single-registration law is a function
of `p` only; no unaudited `C^3` instrument value or unraveling measurement sits on
a derivation path (check F1). The runner consumes only quotient probabilities and
`C^2 tensor C^2` Born weights.

**N4 residual matching.** This note's `rho_corr` specializes at `p = 1/2` to the
landed 06-18 wall witness `diag(1/2, 0, 0, 1/2)` (check F2); the residual role
matches exactly — same single-copy marginals, differing joint. The 06-17
cumulant `C_jk` is used with its proven meaning (P3), not repurposed.

**N5 rhetoric audit.** The note avoids global impossibility language. The tested
resolution is only the audited unraveling premises versus the supplied
two-outcome, two-registration quotient law. Future cross-edge-independence,
stationarity, or reset theorems are named as valid escapes.

**N6 partial-closure path scan.** The note does not say a new axiom or primitive
is required. The named closure is a framework-native cross-edge independence
theorem on the registered quotient (residual 4), plus an identical-marginal /
stationarity theorem (residuals 1+3). Approved future theorems are not treated as
bounded walls.

**N7 steelman.** Grant the strongest honest reading of the lane: U2
non-degeneracy AND U4's bi-orbit-projected mean-spectrum quasi-freeze both as
premises. The correlated stack satisfies both (checks C3, C4) and still violates
factorization (check F3). Even steelmanned, the audited lane does not force the
atom. A genuine future theorem that adds cross-edge independence would not
contradict this no-go, because it adds a source strictly beyond the audited
single-edge premises.

**N8 cross-cycle echo.** The 06-18 wall's shape — "not forced by these tested
inputs" — is preserved: adding the audited unraveling single-edge inputs to the
tested set leaves the wall standing (product still strictly interior; the
correlated stack still single-edge-indistinguishable and non-factorized)
(check F4). This note follows the repo pattern of pruning a false shortcut while
leaving the positive repair route open and named.

## Consequence For The Statistics Atom

After this note, the G3 atom's open content is unchanged in substance but sharper
in aim: the missing premise is a **cross-edge independence theorem on the
registered two-outcome quotient** (unraveling residual 4), with an
identical-marginal / stationarity theorem (residuals 1+3) as prerequisite. The
audited unraveling deliverables — single-edge non-degeneracy and bi-frame
quasi-stationarity of the step mean — are demonstrably factorization-blind and do
not discharge it. The two 2026-07-10 audits that named factorization as the
missing retained bridge are answered: the unraveling lane, as currently proven,
is not that bridge; residual 4 is where the bridge must be built.

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
- [`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — U1, U2, and the four residuals (residual 4 = cross-edge independence).
- [`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`](UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — U4; the bi-orbit-projected mean-spectrum readout and the S1 non-stationarity
  finding.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency, context note, premise, or bridge. The independent audit
lane is the only status authority. References to retained or retained-bounded
dependency surfaces are descriptive references to existing audit-ledger status,
not a status action by this note.

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
