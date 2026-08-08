# The self-consistent beta has no far field to extrapolate, so the finite-size caveat cannot defend it, given the parent note's own construction and diagnostic

**Type:** demotion packet
**Claim type:** `no_go` for the parent note's finite-size caveat, scoped to the tested construction
**Status:** demotion — removes the sole defence of the parent note's Bounded Claim 1

```yaml
actual_current_surface_status: demotion
target_claim_type: no_go
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >
  Cycle 710 (PR #5656) emptied the parent note's two operator discriminators and
  named this extrapolation the highest-value open follow-up, because the parent
  note ran its continuum argument for Poisson alone. This cycle runs it for every
  operator and identifies why it cannot succeed for any of them. The negative
  content is confined to the caveat and the diagnostic; it is not a claim about
  the field equation of the lane.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Runner: `scripts/physical_poisson_beta_has_no_continuum_limit_cycle711_2026_07_26.py`
(8 PASS / 0 FAIL)

## What is being tested

Parent: `self_consistency_forces_poisson_note` — `criticality: critical`,
`deps: []` (a root), `direct_in_degree: 17`, `transitive_descendants: 727`,
`load_bearing_score: 18.092`.

Its first caveat is the sole defence of Bounded Claim 1 against the fact that its
measured exponent is `1.28` rather than the Newtonian `1.0`:

> "**Finite-size beta**: The measured beta ~ 1.28 exceeds the target 1.0 due to
> Dirichlet BC on small lattices (N=20). The distance-law closure script
> demonstrates beta -> 1.0 in the continuum limit via extrapolation from larger
> lattices (up to 96^3)."

The operator is fixed across the self-consistent iterations while only the
right-hand side changes, so each operator is factorized once per lattice size with
`splu` and reused. That is what makes `N = 48` reachable for the biharmonic rival.
`N = 12` is excluded because `check_field_physics` fits radii `2..N//2-3`, fewer
than the three points its own mask requires, and returns `nan`.

## A. Poisson's exponent does not extrapolate to 1.0

Both extrapolation families — the repo's own distance-law script reports several
rather than selecting one, and this follows that convention (S1):

| | Poisson | biharmonic | local |
|---|---|---|---|
| `beta` at N=48 | `1.2550` | `0.8182` | `26.53` |
| `b_inf` from `b + c/N` | `1.2747 ± 0.0177` | `0.7958 ± 0.0088` | `38.12` |
| `b_inf` from `b + c/N + d/N^2` | `1.1578 ± 0.0012` | `0.7381 ± 0.0034` | `50.47` |

The caveat asserts `1.0`. Neither family lands near it. Over the doubling from
N=24 to N=48 Poisson's `beta` moves `+0.0311` — at that rate reaching `1.0` would
need roughly eight further doublings.

## B. The ranking is indeterminate, which confirms cycle 710's refusal

`gap = abs(beta_poisson - 1) - abs(beta_biharmonic - 1)`, positive meaning
biharmonic is closer to the target (S2, S3):

| N | 16 | 20 | 24 | 28 | 32 | 40 | 48 |
|---|---|---|---|---|---|---|---|
| gap | `+0.1339` | `+0.1562` | `+0.1530` | `+0.1416` | `+0.1276` | `+0.0991` | `+0.0732` |

The gap shrinks monotonically from N=20, so the biharmonic advantage cycle 710
measured at N=20/24 is a finite-size effect that dissolves. Extrapolated, **the
two families disagree on the sign**: `+0.0706` (biharmonic closer) from the `1/N`
family, and the opposite sign from the `1/N + 1/N^2` family. This evidence does
not determine a continuum ranking either way.

That is an independent confirmation of cycle 710's R16, which measured the gap as
inside the finite-size budget and refused to claim any rival is the better
operator. Had cycle 710 taken the stronger reading, this cycle would have refuted
it.

## C. Why none of this can work: the source is scale-locked to the box

The parent propagator normalizes total density to `1` and every layer to exactly
`1/N` (cycle 710 R7). So the self-consistent source is not a localized mass (S5):

| N | 16 | 20 | 24 | 32 | 40 | 48 |
|---|---|---|---|---|---|---|
| total mass | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| source RMS radius | `5.449` | `6.546` | `7.657` | `9.909` | `12.182` | `14.467` |
| RMS / N | `0.3406` | `0.3273` | `0.3190` | `0.3096` | `0.3046` | `0.3014` |

`RMS/N` is essentially constant. The source is a fixed *fraction* of the box, so
there is no limit in which it becomes a point source and a `1/r` far field could
appear.

And `check_field_physics` fits radii `2..N//2-3`, which lies **inside** that
source — with the enclosed mass fraction *increasing* with lattice size (S6):

| N | 16 | 20 | 24 | 32 | 40 | 48 |
|---|---|---|---|---|---|---|
| max fit radius | `5` | `7` | `9` | `13` | `17` | `21` |
| source mass inside the fit window | `0.5067` | `0.6160` | `0.6841` | `0.7643` | `0.8117` | `0.8449` |

**Enlarging the lattice moves this diagnostic further from a far-field
measurement, not closer.** That inverts the caveat's premise, and it explains S4:
the power-law fit quality degrades monotonically for both operators — Poisson
`R^2` from `0.9490` at N=16 to `0.8446` at N=48, biharmonic from `0.9117` to
`0.6910` — because the profile inside a spreading cloud is progressively less
power-law-like.

## D. The caveat cites a different observable

The script the caveat names, `scripts/frontier_distance_law_definitive.py`, states
its own convention:

> "Convention: deflection delta(b) ~ 1/b^alpha => alpha = -1.0 for Newtonian
> gravity."

and cross-checks against "a point source `f = s/r`". It measures **ray deflection
in a prescribed field**, and the string `self_consistent` does not occur in it at
all (S7). That is a different observable in a different field from the
self-consistent `beta` the caveat is defending.

## Claim ledger

| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
|---|---|---|---|---|---|
| **thesis** | The parent note's finite-size caveat cannot defend its Bounded Claim 1, because the self-consistent `beta` has no far field to extrapolate: the source is scale-locked to the box, the fit window lies inside it and increasingly so with size, Poisson's exponent extrapolates to `1.16`–`1.27` rather than `1.0`, and the continuum ranking is indeterminate. | S1, S3, S4, S5, S6, S7 | the parent note's parameters `k=5.0, G=0.5, sigma=2.0, mixing=0.3, tol=1e-4, max_iter=30` **[supplied]**; the parent note's `check_field_physics` `beta` diagnostic and its `2..N//2-3` fit window **[supplied]**; two extrapolation families, `1/N` and `1/N + 1/N^2`, following the repo's own distance-law script **[supplied]**; lattice sizes 16..48 **[satisfied]** | Shown: `b_inf` of `1.2747 ± 0.0177` and `1.1578 ± 0.0012`, neither near 1.0; `RMS/N` constant at `0.30`; enclosed mass fraction rising `0.51 -> 0.84`; fit `R^2` falling for both; the cited script measuring deflection in a prescribed field. Claimed: the caveat cannot defend Bounded Claim 1 on this construction. Not claimed: that the lane's field equation is not Poisson, that any rival operator is better, or that a differently-constructed source would fail. | either extrapolation family landing within 0.05 of 1.0, or the enclosed mass fraction decreasing with N |
| S1 | Poisson's self-consistent `beta` does not extrapolate to 1.0 under either family. | S1 | the parent note's parameters `k=5.0, G=0.5, sigma=2.0, mixing=0.3, tol=1e-4, max_iter=30` **[supplied]**; the parent note's `check_field_physics` `beta` diagnostic and its `2..N//2-3` fit window **[supplied]**; lattice sizes 16..48 **[satisfied]**; two extrapolation families, `1/N` and `1/N + 1/N^2`, following the repo's own distance-law script **[supplied]**; least squares as the estimator **[supplied]** | Shown: `1.2747 ± 0.0177` and `1.1578 ± 0.0012`. Claimed: the same. Not claimed: that no extrapolation family could reach 1.0 — only that these two, which the repo's own script uses, do not. | either family within 0.05 of 1.0 |
| S2 | The biharmonic rival's exponent moves monotonically away from 1.0 as the lattice grows. | S2 | the parent note's parameters `k=5.0, G=0.5, sigma=2.0, mixing=0.3, tol=1e-4, max_iter=30` **[supplied]**; the parent note's `check_field_physics` `beta` diagnostic and its `2..N//2-3` fit window **[supplied]**; lattice sizes 16..48 **[satisfied]**; per-operator source-sign normalization from cycle 710 R10 **[satisfied]** | Shown: `abs(beta-1)` rising `0.1170 -> 0.1818` across sizes 16..48, monotone. Claimed: the biharmonic advantage at N=20/24 is a finite-size effect. | a monotone approach to 1.0 |
| S3 | The continuum ranking is indeterminate: the two extrapolation families disagree on the sign of the gap. | S3 | the parent note's parameters `k=5.0, G=0.5, sigma=2.0, mixing=0.3, tol=1e-4, max_iter=30` **[supplied]**; the parent note's `check_field_physics` `beta` diagnostic and its `2..N//2-3` fit window **[supplied]**; lattice sizes 16..48 **[satisfied]**; exactly two extrapolation families are tested, not a survey of all families **[supplied]** | Shown: `+0.0706` from the `1/N` family, opposite sign from the `1/N + 1/N^2` family. Claimed: this evidence does not determine a continuum ranking. Not claimed: that no ranking exists. | both families agreeing on the sign |
| S4 | The power-law fit quality degrades monotonically with lattice size for both operators. | S4 | the parent note's parameters `k=5.0, G=0.5, sigma=2.0, mixing=0.3, tol=1e-4, max_iter=30` **[supplied]**; the parent note's `check_field_physics` `beta` diagnostic and its `2..N//2-3` fit window **[supplied]**; lattice sizes 16..48 **[satisfied]**; `R^2` of the log-log linear fit as the quality measure, which is the parent diagnostic's own **[supplied]** | Shown: Poisson `R^2` `0.9490 -> 0.8446`, biharmonic `0.9117 -> 0.6910`, both monotone. Claimed: the fitted exponent means less at larger N, not more. | `R^2` improving with N |
| S5 | The self-consistent source never localizes: total mass is pinned to 1 and its RMS radius is a fixed fraction of the box. | S5, cycle 710 R7 | per-layer mass pinned to `1/N` by the parent propagator, established in cycle 710 R7 **[satisfied]**; the flat-field density `phi = 0` as the source probed **[supplied]**; `sigma = 2.0` wavepacket width held fixed as N grows **[supplied]**; lattice sizes 16..48 **[satisfied]** | Shown: total mass `1.000000` to `1e-12` at all sizes; `RMS/N` within `[0.3014, 0.3406]`. Claimed: there is no limit in which the source becomes a point source. | the RMS radius saturating at a fixed value |
| S6 | The `beta` fit window lies inside the source and the enclosed mass fraction increases with lattice size. | S6 | the fit window `2..N//2-3` is the parent diagnostic's own, at its lines 387 and 405 **[satisfied]** | Shown: enclosed fraction rising `0.5067 -> 0.8449`, monotone. Claimed: enlarging the lattice moves the diagnostic further from a far-field measurement. Not claimed: that the field itself has no far field, only that this window does not sample one. | the enclosed fraction decreasing with N |
| S7 | The script the caveat cites measures ray deflection in a prescribed `f = s/r` field and never touches the self-consistent construction. | S7 | string presence in the cited file at this commit **[satisfied]** | Shown: the file states the deflection convention, cross-checks a prescribed point source, and contains no occurrence of `self_consistent`. Claimed: the caveat cites a different observable in a different field. Not claimed: that the cited script is itself wrong about deflection. | the script fitting the self-consistent `beta` |
| S8 | The `local` operator diverges under the same scaling, so its exclusion is independent of everything above. | S8 | the parent note's parameters `k=5.0, G=0.5, sigma=2.0, mixing=0.3, tol=1e-4, max_iter=30` **[supplied]**; the parent note's `check_field_physics` `beta` diagnostic and its `2..N//2-3` fit window **[supplied]**; lattice sizes 16..48 **[satisfied]**; two extrapolation families, `1/N` and `1/N + 1/N^2` **[supplied]** | Shown: extrapolated `b_inf` of `38.12` and `50.47`. Claimed: cycle 710's exclusion of `local` on the decay exponent survives this analysis. | a finite extrapolated exponent near 1.0 |

## The strongest objection, and how it lands

> "Your `beta` is measured on the self-consistent field, whose source is a
> box-filling cloud by construction. There is no reason for that quantity to have
> a continuum limit at all, so extrapolating it is meaningless. Citing a
> fixed-source deflection script is the *right* move precisely because it holds
> the source fixed."

This is correct as physics, and S5/S6 are the proof of its first half. It does not
rescue the caveat — it strengthens the demotion. Either way the defence fails:

- if the self-consistent `beta` does have a continuum limit, it is `1.16`–`1.27`,
  not `1.0` (S1); or
- if it has none, because the source never localizes (S5, S6), then there is no
  continuum value for the caveat to appeal to, and a fixed-source deflection
  extrapolation cannot supply one for a different observable (S7).

The objection selects which of the two readings is right. It does not produce a
third in which Bounded Claim 1 survives. What it does identify is the constructive
repair, recorded below.

## Scope, and what this cycle does not claim

- Every row is scoped to the tested construction at the parent note's parameters
  and the stated lattice sizes.
- Not a claim that the lane's field equation is not Poisson.
- Not a claim that any rival operator is better — S3 says the opposite, that the
  continuum ranking is indeterminate on this evidence.
- Not a claim that no extrapolation family could reach 1.0; only that the two the
  repo's own distance-law script uses do not.
- S6 does not say the field has no far field. It says this fit window does not
  sample one.

## What survives in the parent note

- **Test 1** (convergence) stands, as in cycle 710.
- **Test 4** (screened sweep) stands, by cycle 710 R13.
- The parent note's other caveats — "this is not a uniqueness theorem",
  "lattice-level result", "linear response regime" — remain accurate.
- The cited distance-law script is not impugned. It measures what it says it
  measures; it simply does not measure the quantity the caveat needs.

## Proposed revision to the parent note

Recorded for the review process; this cycle does not edit the parent note or any
audit-lane surface.

- **Caveat 1** — withdraw the sentence "The distance-law closure script
  demonstrates beta -> 1.0 in the continuum limit via extrapolation from larger
  lattices (up to 96^3)." It cites a different observable in a different field
  (S7), and the self-consistent `beta` does not extrapolate to 1.0 (S1).
- **Bounded Claim 1** — with cycle 710 emptying the attractiveness half of its
  ground and this cycle removing its finite-size defence, the claim has no
  surviving support at any tested lattice size. Narrow to the screened family,
  where cycle 710 R13 leaves it intact.
- **The `beta` diagnostic itself** — record that its fit window lies inside the
  self-consistent source, with the enclosed fraction rising with N (S6), so it is
  not a far-field exponent at any tested size.

## The constructive repair this cycle points to

The diagnostic fails because the source is scale-locked. The repair is to hold a
source fixed while the box grows: a localized source of fixed extent and fixed
total mass, with the exponent fitted at radii **outside** it. That is measurable on
this same construction and it is the natural successor. It requires giving up the
parent propagator's per-layer normalization for the source-construction step,
which cycle 710 R6 showed does not by itself repair the response kernel — so the
two repairs are independent and both would be needed.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: self_consistency_forces_poisson_note
target_blocker_text: >
  "Finite-size beta: The measured beta ~ 1.28 exceeds the target 1.0 due to
  Dirichlet BC on small lattices (N=20). The distance-law closure script
  demonstrates beta -> 1.0 in the continuum limit via extrapolation from larger
  lattices (up to 96^3)."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: no_go
next_trace_action: >
  The extrapolation cycle 710 named as the highest-value open follow-up is
  performed for every operator, and the reason it cannot succeed for any of them
  is identified. The successor is the fixed-source repair described above: a
  localized source of fixed extent and mass, exponent fitted outside it. Until
  that is run, no exponent from this construction should be read as a far-field
  decay law.
```
