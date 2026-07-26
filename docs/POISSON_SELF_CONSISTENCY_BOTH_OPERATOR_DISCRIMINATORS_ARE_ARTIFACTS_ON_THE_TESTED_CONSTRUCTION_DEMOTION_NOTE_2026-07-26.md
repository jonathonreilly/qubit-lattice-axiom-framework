# Both operator discriminators in the self-consistency Poisson note are artifacts, under the parent note's own parameters and its own decay diagnostic

**Type:** demotion packet
**Claim type:** `no_go` for the two named discriminators, scoped to the tested construction
**Status:** demotion — narrows three Bounded Claims of the parent note

```yaml
actual_current_surface_status: demotion
target_claim_type: no_go
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >
  The parent row's re-audit note names two computations and a scope revision.
  This cycle performs both computations on the parent runner's own imported
  operators and propagator, and reports the resulting scope. The negative
  content is confined to the two named discriminators at the parent note's own
  working point; it is not a claim about the field equation of the lane.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Runner: `scripts/physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py`
(13 PASS / 0 FAIL)

## What the parent row asked for

Parent: `self_consistency_forces_poisson_note`
(`docs/audit/data/ledger/se/self_consistency_forces_poisson_note.json`) —
`criticality: critical`, `deps: []` (a root), `direct_in_degree: 17`,
`transitive_descendants: 727`, `load_bearing_score: 18.092`.

`notes_for_re_audit_if_any`:

> "missing_bridge_theorem: compare susceptibility with the matched
> point-to-point inverse-Laplacian kernel, normalize alternative-operator
> source signs consistently, and revise the note to the resulting finite
> numerical scope before re-audit."

`chain_closure_explanation`:

> "The runner genuinely computes the reported finite-case outputs, but it does
> not establish that the transfer propagator's response kernel is the inverse
> graph Laplacian. Its susceptibility scalar is correlated with the
> domain-integrated Green-function norm for sources moved toward the boundary,
> rather than with a matched point-to-point Poisson profile."

`verdict_rationale`:

> "the attraction comparison uses the same negative source with operators of
> different sign definiteness, making the
> Poisson-versus-biharmonic/local/random sign discriminator
> convention-dependent; moreover, the measured susceptibility decays as
> r^(-2.805), despite the claimed Poisson-kernel interpretation."

Both computations are performed below. Every operator and the propagator are
imported from `scripts/frontier_self_consistent_field_equation.py`, so the
object under test is the parent note's actual construction. R1 verifies
bit-identity between the runner's switchable propagator and the parent
runner's, so the one row that varies the propagator varies exactly one step.

## A. The matched point-to-point kernel: the response kernel is sign-indefinite

The response kernel is `K(x, y) = d rho(x) / d phi(y)`, obtained from
single-site field perturbations. The parent note's step 4 asserts

> "On a graph with nearest-neighbor coupling, the propagator's Green's function
> IS the inverse of the graph Laplacian."

and reads that as licensing `K` proportional to `(-Laplacian)^-1`. On the
tested construction it is not, and the obstruction is a sign structure rather
than a normalization:

| quantity | inverse Dirichlet graph Laplacian `G` | response kernel `K` |
|---|---|---|
| interior sign structure | single-signed, `frac(G>0) = 1.000000` (R2) | sign-indefinite, `frac(K>0) = 0.14..0.21`, `frac(K<0) = 0.70..0.78` (R3) |
| best scalar match | — | relative residual `0.9987..0.9996` (R4) |
| `corr(K, G)`, matched point-to-point | — | `-0.058, -0.048, -0.031` (R4) |

A single-signed kernel cannot be a nonzero scalar multiple of a sign-indefinite
one, so no scalar `c` gives `K = c*G`. R4 computes the least-squares `c` and its
residual rather than arguing from the sign structure alone.

The contrast with the parent note's reported statistic is the whole finding:
**0.93 by the parent note's comparison, `-0.06` by the comparison the re-audit
note asks for.**

Two ways this could have been a regime artifact, both tested and both negative:

- **Weak coupling (R5).** `corr(K, G)` stays within `[-0.13, +0.01]` across
  `k` in `[0.05, 10]`, four decades. There is no small-`k` regime in which the
  identification holds. This row is the steelman for the parent note and it
  does not survive.
- **Per-layer renormalization (R6).** The parent propagator renormalizes each
  layer, which forces per-layer mass to exactly `1/N` for every field (R7) and
  hence makes the signed response sum exactly zero. Removing that step does
  **not** produce a match — the residual stays at `1.0000`. This falsifies the
  natural repair hypothesis. The reason is that the field enters only as a
  phase (`|amp| = 1/L`, independent of `phi`), so the density response is an
  interference kernel with or without renormalization.

R7 also identifies why the parent statistic is nonzero at all: with per-layer
mass pinned to `1/N`, the signed response sums to `4.2e-17`, so the absolute
value at line 489 of the parent runner is load-bearing. The parent statistic is
a total-variation reshaping measure and carries no response amplitude.

## B. The 0.93 shape correlation has no discriminating power

Reproducing the parent note's Test 3 on its own radii (R8):

| quantity | value |
|---|---|
| `corr(chi, G_poisson)` | `0.920038` (parent note reports `0.93`, "strong match") |
| `chi(r)` log-log slope | `-2.2420` |
| `G_poisson(r)` log-log slope | `-1.5666` |
| `chi/G` ratio across radii 1..7 | `6.35 .. 67.8`, a spread factor of `10.7x` |

A matched profile has a constant ratio. The high correlation coexists with a
10.7-fold shape disagreement, because Pearson correlation between two positive
monotone-decreasing profiles sampled at seven radii is dominated by the shared
trend.

R9 quantifies that directly: on these radii, `corr(r^-1, r^-p) >= 0.93` for all
`p` up to `4.57`. The threshold does not exclude `p = 2.805` (`corr = 0.959`),
the exponent the parent row's verdict rationale reports, nor `p = 8.637`
(`corr = 0.917`), the exponent of the operator the parent note lists as
unphysical, which misses the threshold by `0.013`.

## C. Source-sign normalization inverts the operator ranking

The parent runner's `self_consistent_iterate` hardcodes
`rho_source = -G * rho` (line 296) for every operator. The Laplacian is
negative definite on the Dirichlet interior; the biharmonic, local, and `1/r^2`
kernels are positive. So Poisson's fundamental solution has the opposite sign
to all three rivals (R10) and one fixed source sign yields an attractive well
for Poisson and a repulsive hill for each rival — which is the entire content
of the parent note's "Attractive?" column.

Normalizing the source sign per operator, as the re-audit note asks, and
rerunning with the parent note's own parameters and its own `beta` diagnostic
(R11):

| rank by `abs(beta-1)` | operator | `beta` (N=20) | `beta` (N=24) | attractive | monotone |
|---|---|---|---|---|---|
| 1 | biharmonic | `0.8762` | `0.8669` | yes | yes |
| 2 | `1/r^2` kernel | `1.2109` | `1.2415` | yes | yes |
| 3 | **poisson** | `1.2799` | `1.2861` | yes | yes |
| 4 | local | `8.6371` | `12.2852` | yes | yes |

All four are positive throughout the interior after normalization, not merely at
the source (R12), so the source-point sign read the parent note uses carries no
content beyond the convention. What survives as a genuine discriminator is the
decay exponent alone — and on that, Poisson ranks **third of four** at both
lattice sizes, behind biharmonic and the `1/r^2` kernel.

## Claim ledger

| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
|---|---|---|---|---|---|
| **thesis** | Both operator discriminators the parent note reports — the attractiveness comparison and the 0.93 shape correlation — are artifacts on its own tested construction: the density response kernel is sign-indefinite where the inverse Dirichlet Laplacian is single-signed, and the operator ranking inverts once the source sign is normalized per operator. | R2, R3, R4, R10, R11, R12 | Tested construction, parameters, and lattice sizes as stated in each row **[satisfied]**; the parent note's own `beta` diagnostic as the decay measure **[supplied]**; Dirichlet boundary conditions **[satisfied]** | Shown: on this construction `K` is sign-indefinite and no scalar matches it to `G`, and the sign-normalized `beta` ranking places Poisson third at N=20 and N=24. Claimed: the two discriminators are artifacts of this construction. Not claimed: that the field equation of the lane is not Poisson, nor anything about the continuum limit. | `K` single-signed at any tested site, or Poisson ranking first under sign normalization at either lattice size |
| L1 | The inverse Dirichlet graph Laplacian is single-signed on the interior at N=10 and N=12. | R2 | Dirichlet boundary conditions on a connected cubic interior **[satisfied]** | Shown: `frac(G>0) = 1.000000`, `min abs(G) > 0` at both sizes. Claimed: the same. | any interior sign change or exact zero |
| L2 | The response kernel `d rho / d phi(y)` is sign-indefinite at the three tested perturbation sites, N=10. | R3 | Single-site perturbation, `delta_phi = 1e-3` **[supplied]**; N=10, k=5.0 **[satisfied]** | Shown: both sign fractions exceed 5% at all three sites. Claimed: the same, at those sites and that size. | either sign fraction below 5% |
| L3 | No scalar `c` makes `K = c*G` at the tested sites. | R4 (least-squares `c`, residual > 0.9), L1, L2 | Dirichlet boundary conditions on a connected cubic interior **[satisfied]**; single-site perturbation at `delta_phi = 1e-3` **[supplied]**; N=10 and k=5.0 **[satisfied]**; least squares as the matching criterion **[supplied]** | Shown: best-fit residual `0.9987..0.9996`, `corr` in `[-0.058, -0.031]`. Claimed: no scalar match at these sites. Not claimed: that no operator-valued relation exists between them. | a small residual at any tested site |
| L4 | The mismatch is not a weak-coupling artifact. | R5 | `k` sampled at seven values in `[0.05, 10]` **[supplied]** — a grid, not a proof of all `k` | Shown: `abs(corr) < 0.25` at all seven. Claimed: no weak-coupling regime among the sampled `k`. Not claimed: a statement about every real `k`. | `corr` approaching 1 at any sampled `k` |
| L5 | The per-layer renormalization is not the cause of the mismatch. | R6, R1 (bit-identity), R7 | renormalization removed and nothing else changed, established by R1 **[satisfied]** | Shown: residual stays `1.0000` with renormalization off. Claimed: this repair hypothesis is false. | a small residual with renormalization off |
| L6 | Per-layer mass is exactly `1/N` independent of `phi`, so the parent statistic's absolute value is load-bearing. | R7 | five distinct fields including uniform and large-amplitude random **[supplied]** | Shown: `max abs(layer mass - 1/N) < 2.8e-17` for all five; signed response sum `4.2e-17` against absolute sum `5.2e-2`. Claimed: the same. | layer mass varying with `phi`, or a nonzero signed sum |
| L7 | On the parent note's own radii, its 0.93 statistic coexists with a 10.7-fold shape disagreement and does not exclude exponents up to 4.57. | R8, R9 | the parent note's radius set 1..7 at N=20 **[satisfied]**; Pearson correlation as the statistic, which is the parent note's choice **[supplied]** | Shown: `corr = 0.920` with slopes `-2.242` vs `-1.567` and ratio spread `10.7x`; threshold band extends to `p = 4.57`. Claimed: the statistic has no discriminating power across the parent note's own tested exponents. Not claimed: that `chi` and `G` are unrelated. | a near-constant `chi/G` ratio, or a band excluding 2.805 |
| L8 | Poisson's fundamental solution has the opposite sign to all three rivals, and the parent runner feeds all four the same source sign. | R10, parent runner line 296 | unit positive point source **[satisfied]** | Shown: signs `-1` for Poisson, `+1` for biharmonic, local, `1/r^2`. Claimed: the attractiveness column's content is this one bit. | the signs agreeing |
| L9 | Under per-operator sign normalization, Poisson ranks third of four by `abs(beta-1)` at N=20 and N=24. | R11, R12 | the parent note's parameters `k=5.0, G=0.5, sigma=2.0, mixing=0.3, tol=1e-4, max_iter=30` **[supplied]**; the parent note's `check_field_physics` `beta` diagnostic **[supplied]**; four operators feasible at these sizes **[satisfied]** | Shown: biharmonic `0.876/0.867`, `1/r^2` `1.211/1.242`, Poisson `1.280/1.286`, all attractive and monotone. Claimed: Poisson is not the best operator in the tested family at these sizes. Not claimed: a continuum-limit ranking; the parent note ran its continuum extrapolation for Poisson only. | Poisson ranking first at either size |
| L10 | The screened-Poisson family shares Poisson's definiteness, so the parent note's Test 4 is unaffected. | R13 | `mu^2 >= 0` **[satisfied]** | Shown: `max eig(Laplacian - mu^2 I) < 0` for all six tested `mu^2`. Claimed: the sign defect does not reach Test 4. | a nonnegative eigenvalue |

## Scope, and what this cycle does not claim

- Every numerical row is scoped to the tested 3D Dirichlet cubic-lattice
  transfer-propagator construction at the parent note's parameters and the
  lattice sizes stated per row. No row is a continuum-limit claim.
- This is **not** a claim that the lane's field equation is not Poisson. It is a
  claim that the parent note's two operator discriminators do not support
  Poisson on the construction the parent note tests.
- L9 does not say biharmonic is the lane's field operator. It says the parent
  note's ranking inverts under the normalization the re-audit note requested, so
  the ranking is not evidence for Poisson. The parent note's continuum
  extrapolation was run for Poisson only, so no tested lattice size supports
  the tested-family preference it claims.
- L4 is a seven-point grid in `k`, not a statement about all `k`.
- Measured but not claimed: the parent note's "linear response regime" caveat
  holds. The statistic `sum|rho_p - rho_0|` scales as `delta_phi^1.124` over
  `delta_phi` in `[0.0125, 0.2]` at `r = 3`, N=12 — approximately linear. This
  cycle looked for a linearity failure and did not find one.

## The strongest objection to this cycle, and why the demotion still stands

Stated in hostile-reviewer voice, because it is a good objection:

> "You measured `d rho / d phi` for a propagator whose field coupling is a pure
> phase, and found an oscillatory kernel. Of course you did. The parent note's
> step 4 is a statement about the *amplitude* propagator's resolvent — the object
> that satisfies a lattice Helmholtz equation — and its Green's function
> genuinely is Laplacian-related. You compared the wrong object, then used the
> mismatch to demote a row. The density response of an interfering amplitude was
> never the thing anyone claimed was the inverse Laplacian."

As physics this is largely right, and it is the same point as the last bullet of
the proposed revision below: step 4 conflates two different objects. It does not
rescue the parent note, for one reason — the parent note's Test 3 measures the
**density** response, `rho_p - rho_0` at line 489 of its runner, and reports the
resulting correlation as

> "This confirms that the propagator's own structure selects the inverse
> Laplacian as its natural response kernel."

The object tested here is the object the parent note tested. What is demoted is
the evidence the parent note actually offers, not a strawman of it. The objection
therefore sharpens the conclusion — the conflation is the defect — rather than
defeating it, and it names the right next target: what the density response
kernel of a phase-only coupling actually is. That is recorded in the trace gate
as the open question this cycle exposes and does not answer.

## What survives in the parent note

- **Test 1** (Poisson self-consistent iteration converges to an attractive
  monotone field) stands. Convergence is not disputed.
- **Test 4** (screened sweep; `mu^2 = 0` closest to `beta = 1` within the
  screened family) stands, by R13.
- The parent note's own caveats ("this is not a uniqueness theorem",
  "finite-size beta", "lattice-level result") are accurate and this cycle
  strengthens rather than contradicts them.

## Proposed revision to the parent note

Recorded here for the review process; this cycle does not edit the parent note
or any audit-lane surface.

- **Bounded Claim 1** — "unscreened Poisson is the best-supported operator in
  the tested family and the only tested one that stays close to the Newtonian
  target": not supported at N=20 or N=24 under per-operator sign normalization
  (L9). Narrow to the screened family, where R13 leaves it intact.
- **Bounded Claim 2** — Poisson "preferred over biharmonic, local,
  random-kernel, and screened variants": the preference over biharmonic and the
  `1/r^2` kernel is a source-sign convention (L8, L9). The preference over
  `local` survives on the decay exponent alone.
- **Bounded Claim 3** — the `r = 0.93` susceptibility correlation as
  "supportive evidence that the inverse Laplacian is a natural response
  kernel": the matched point-to-point comparison gives `corr = -0.06` and no
  scalar match (L3), and the 0.93 statistic does not discriminate (L7).
  Withdraw.
- **Step 4 of the self-consistency argument** conflates the amplitude
  propagator's resolvent with the density response kernel to a phase-only field
  coupling. These are different objects on this construction (L2, L3, L5).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: self_consistency_forces_poisson_note
target_blocker_text: >
  "missing_bridge_theorem: compare susceptibility with the matched
  point-to-point inverse-Laplacian kernel, normalize alternative-operator
  source signs consistently, and revise the note to the resulting finite
  numerical scope before re-audit."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: no_go
next_trace_action: >
  The re-audit note's three asks are performed and the resulting scope is
  stated. The parent row's re-audit can proceed against this packet. The
  downstream question this cycle exposes and does not answer: what the density
  response kernel of a phase-only field coupling actually is, given that R3/R5
  show it is sign-indefinite at every sampled coupling strength. That is the
  object the lane needs if the field equation is to be derived rather than
  selected by a numerical sweep.
```
