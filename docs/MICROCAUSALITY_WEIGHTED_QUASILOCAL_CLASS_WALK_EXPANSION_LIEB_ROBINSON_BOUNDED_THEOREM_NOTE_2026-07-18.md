---
claim_id: microcausality_weighted_quasilocal_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional extension of the family chain to the weighted quasilocal class (axioms supply no dynamics; the interaction family, the weighted-norm bound, and the finite region are supplied objects; same Heisenberg convention and declared ODE context as the siblings; ambient l1 graph metric declared throughout), stated with an explicitly named delta over the landed quasilocal notes: (Q1) the supplied class — H = Σ_S h_S over finite NONEMPTY supports S of arbitrary size (connectedness retired in review as irrelevant: the ambient max-pairwise diameter satisfies the needed inequality by definition), set-indexed (same-support terms summed), each h_S Hermitian, with the supplied weighted activity kappa := sup_x Σ_{S∋x} ||h_S|| |S| e^{mu diam S}, 0 < kappa < ∞, for a supplied mu > 0, diam = ambient l1 graph diameter, volume-uniformity meaning dependence on Λ only through kappa, on either the tensor class or the even-CAR class; (Q2) the chain lemma Σ_j diam(S_j) ≥ d for X-to-Y chains of consecutively overlapping supports, and the weight split Π||h_j|| ≤ e^{−mu d} Π(||h_j||e^{mu diam_j}); (Q3) the single-step meeting bound Σ_{S'∩S≠∅} ||h_{S'}|| |S'| e^{mu diam S'} ≤ |S| kappa and the back-to-front peeling in which each |S_j| handed up reconstitutes exactly the site-weighted summand for the next step — the |S|-weight bookkeeping that makes arbitrary support sizes work under THIS hypothesis form — the delta over the landed quasilocal notes is the hypothesis form and its pure-exponential output, NOT arbitrary-support coverage per se (the exp-decay note covers arbitrary finite supports in its polynomial-corrected weight; no uniqueness is claimed); (Q4) the theorem: ||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A||||B|| (n_X^w/kappa) e^{−mu d} (e^{2 kappa |t|} − 1) with n_X^w := Σ_{S∩X≠∅} ||h_S|| |S| e^{mu diam S} ≤ |X| kappa, all t, volume-uniform, velocity readout v ≤ 2 kappa/mu, zeroth term vanishing on the tensor class and on the even sector of the CAR class (block04 convention for odd-odd pairs); (Q5) the consistency reduction — strict bonds give the ENVELOPE kappa ≤ 12 J e^{mu}, attained exactly by the saturated bulk model (gated), so the worst-case rate is 24 J e^{mu} versus the direct sibling's 20 J e^{mu}, an envelope ratio of exactly 6/5, with the slack ladder 12→11→10 exhibited by enumeration — the direct finite-range siblings remain sharper on their classes and are not modified; (Q6) exact instance families with closed-form kappa: pair interactions J0 lambda^{|x−y|} give kappa_3D = 4 J0 rho(3+rho^2)/(1−rho)^3 and kappa_1D = 4 J0 rho/(1−rho) at rho = lambda e^{mu} < 1 (l1 sphere count 4r^2+2 gated; rational instances 14 J0 and 684 J0 and 4 J0 gated by partial-sum-plus-tail brackets); (Q7) the honest-delta and disposition layer: the landed free-bilinear note ALREADY proves the U = 1 scalar-bilinear instance of this shape under the corrected map kappa = 2 W_mu — rates matching exactly as 2 kappa = 4 W_mu (its W_mu and exp(−mu d + 4 W_mu|t|) displays needled as the landed comparator, not re-proved; the factor-2 correction is a review repair); the landed exp-decay note's reproducing-weight no-go (ratio ≥ R+1) binds the reproducing METHOD only and not this route (e^{−mu d} is extracted BEFORE any convolution; the divergent ratio is never formed — dispositioned with its display needled); the fermionic instantiation lifts the block04 sibling's nearest-neighbor restriction to weighted long-range even supports via its graded lemma, re-gated on a long-range instance. The transfer/log-generator instantiation (whose first step is feeding the CT note's fixed-background kernel into kappa) is NOT attempted and is named as the candidate next step; the U-integrated measure side and sharp constants (subsuming mu-optimization) are outside scope; disconnected supports ARE covered; nothing physical is selected."
upstream_dependencies:
  - minimal_axioms
  - microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - microcausality_fermionic_even_car_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09
  - exp_decay_lieb_robinson_quasilocal_bridge_theorem_note_2026-06-11
  - free_bilinear_quasilocal_lr_bridge_theorem_note_2026-06-10
runner: scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py
---

# Microcausality: Weighted Quasilocal-Class Walk-Expansion Lieb-Robinson Bound

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; supplied weighted quasilocal class
(arbitrary-size supports, connectedness not required, supplied `κ > 0`); ambient `l1` graph
metric declared; the axioms supply no dynamics; same conventions and
declared ODE context as the siblings.
**Audit-status authority:** independent audit lane only. This note sets
no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py`](../scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.txt`](../logs/runner-cache/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.txt)

## Purpose, with the delta named up front

The family's bounds so far require strict finite range (bonds; bonds
and faces). The log-transfer generators the lane ultimately cares about
are not finite-range — they are quasilocal, with exponentially decaying
terms. The repo already carries three landed quasilocal results, and
this note's value is only honest if its delta over them is stated
plainly:

- [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
  already proves the `U = 1` scalar-bilinear instance end-to-end: for
  an unordered pair family its
  `W_mu := sup_x sum_y ||Phi_{xy}|| exp(mu d_1(x,y))` maps to this
  note's activity as `κ = 2·W_mu` (the `|S| = 2` weight), so the RATES
  agree exactly — `2κ = 4W_mu`, matching its bound
  `≤ 2||A_x||||B_y|| exp(−mu d_1(x,y) + 4 W_mu|t|)` — a nontrivial
  factor-for-factor consistency check (an earlier draft claimed the
  identification without the factor 2; corrected in review). **Not
  re-proved here** — needled as the landed comparator instance.
- [`EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md`](EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md)
  proves a many-body LR bound in a polynomial-corrected weight, and —
  crucially — a no-go: the pure-exponential **reproducing** constant is
  unbounded (`≥ R + 1`). That no-go binds the reproducing-weight
  METHOD. This note's route never forms that ratio (the decay factor is
  extracted before any convolution), which is why a pure-exponential
  weight is admissible here. Dispositioned in full below.
- [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  supplies the finite-range chain-count skeleton this note upgrades,
  and names the composition gap this note takes: "that one-step
  composition theorem is not proved here or in the cited note."

**The delta, precisely (narrowed in review):** the exp-decay note's
many-body theorem already covers terms over arbitrary finite sets — in
its polynomial-corrected weight. What is new here is **the hypothesis
form and what it buys**: (i) a different, stronger activity criterion —
the site-summed `|S|`-weighted PURE-exponential norm `κ` — under which
the peeling bookkeeping (each step's `|S_j|` factor consumed exactly to
reconstitute the site-weighted summand of the next step) yields a
pure-exponential `e^{−μd}` decay with explicit constants
(`n_X^w/κ`, rate `2κ`), where the landed route pays a polynomial
correction; (ii) the **set-supported even-CAR formulation** (the
landed quasilocal notes are tensor/commuting-mode; the block04 graded
lemma is support-size-blind, so its nearest-neighbor restriction lifts
for free — re-gated on a long-range instance); (iii) the **disposition
layer** connecting the three landed notes coherently, including the
factor-2 `κ = 2W_mu` map above. No uniqueness of the family form is
claimed. The gauged-kernel identification (the CT note's
fixed-background kernel fed into `κ`) is **not attempted** — it is the
named candidate next step.

## Hypotheses (all supplied, none derived)

A finite region `Λ ⊂ Z^3` with the ambient `l1` graph metric `d(·,·)`
(declared once, used everywhere: `diam(S) := max_{u,v∈S} d(u,v)` is the
**ambient** diameter). A supplied set-indexed interaction family: for
finite nonempty `S ⊆ Λ` (**no connectedness is required** — the chain
lemma uses only the ambient max-pairwise diameter, which satisfies
`d(u,v) ≤ diam(S)` by definition for any set; an earlier draft's
connectedness hypothesis was retired in review as irrelevant),
Hermitian `h_S` (same-support terms summed into one `h_S` before norms
are taken), `H = Σ_S h_S`, with the supplied weighted activity

> `κ := sup_x Σ_{S∋x} ||h_S|| · |S| · e^{μ·diam(S)} < ∞`

for a supplied `μ > 0`, and `κ > 0` (at `κ = 0` every `h_S = 0`, `H = 0`,
and every statement is trivial — excluded by convention as in the
siblings). Volume-uniformity of the final constants means exactly this:
they depend on `κ` and not otherwise on `Λ`, so a FAMILY of regions
shares the bound iff it is supplied with a common `κ` (e.g.
translation-invariant-bounded families). The `|S|` weight is
load-bearing: it is what
absorbs the contact-site choice in the peeling below. Observables `A`,
`B` on disjoint supports `X`, `Y` (`d = d(X,Y) ≥ 1`, the standing
scoping hypothesis), on either the tensor-product class (arbitrary
finite site dimensions, as in the plaquette sibling) or the even-CAR
class (even Hermitian `h_S`; block04 conventions, including the
explicit odd-odd zeroth term). Heisenberg convention, the declared
finite-matrix ODE context, and directed time with the `H → −H`
extension, all unchanged from the siblings; the Duhamel layer (Jacobi,
boundary reduction with **consecutive** overlap — each iterate's
reduced generator sums over supports meeting the *previous term only*,
which is exactly the siblings' per-term re-derivation — self-drop, norm
transport, iterated integrals `|t|^k/k!`) is cited to the siblings
where natively gated and consumed here as the unrolled series. The
axioms supply no dynamics (needled). No literature statement is
load-bearing. Workhorse disclosure: this block used two Opus 4.8
max-effort workers (scout and math build) under the workhorse skill's
substitution clause; both were graded against supervisor derivations
recorded in the loop pack **before** reading worker output, and every
load-bearing fact below is gated natively in the runner.

## Results

**Chain lemma (rebuilt).** For a chain `(S_1, …, S_k)` with
`S_1 ∩ X ≠ ∅`, `S_{j+1} ∩ S_j ≠ ∅`, `S_k ∩ Y ≠ ∅`: by induction every
site of `S_j` lies within `Σ_{i≤j} diam(S_i)` of `X` (anchor in the
overlap, triangle inequality, ambient diameter), so

> `Σ_{j=1}^{k} diam(S_j) ≥ d`.

Gated by enumeration on explicit mixed-size families. Hence the weight
split: `Π_j ||h_{S_j}|| ≤ e^{−μd} · Π_j (||h_{S_j}|| e^{μ diam S_j})`.

**Single-step meeting bound and the peeling (the `|S|` bookkeeping).**
For a fixed `S`, summing the site-weighted value
`w*(S') := ||h_{S'}|| |S'| e^{μ diam S'}` over all `S'` meeting `S`:

> `Σ_{S'∩S≠∅} w*(S') ≤ Σ_{x∈S} Σ_{S'∋x} w*(S') ≤ |S| · κ`,

with strict inequality whenever some `S'` with `w*(S') > 0` meets `S`
in two or more sites (the union bound counts it once per contact site — this exact
slack is exhibited below on bonds: `12` versus the true `11`). The
back-to-front peeling then bounds the full chain sum: the innermost
tail obeys `U_k(S_{k−1}) ≤ |S_{k−1}| κ`, and at each outward step the
`|S_j|` handed up combines with the plain weight
`w(S_j) = ||h_{S_j}||e^{μ diam S_j}` to reconstitute exactly
`w*(S_j) = |S_j| w(S_j)` — the object the meeting bound knows how to
sum. No `|S|` factor is created or lost; by downward induction

> `Σ_chains Π_j w(S_j) ≤ n_X^w · κ^{k−1} ≤ |X| · κ^k`,
> `n_X^w := Σ_{S∩X≠∅} w*(S) ≤ |X|κ`,

and with the weight split, the plain-norm chain sum obeys
`Σ_chains Π_j ||h_{S_j}|| ≤ e^{−μd} n_X^w κ^{k−1}`. Gated two ways: the
reconstitution identity symbolically, and the full chain sum versus the
bound by exact enumeration on a finite mixed family.

**Theorem (weighted quasilocal all-time volume-uniform Lieb-Robinson
bound).** Feeding the counting layer into the siblings' unrolled series
(prefactor `2||A||`, interior `2^{k−1}`, base `2||h_{S_k}||||B||` —
total `2^{k+1}` at order `k`, cross-checked by two groupings) and
resumming exactly (`2^{k+1}κ^{k−1}|t|^k = (2/κ)(2κ|t|)^k`):

> `||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| ||B|| (n_X^w/κ) · e^{−μd} ·
> (e^{2κ|t|} − 1)`
> `≤ ||[A, B]|| + 2||A|| ||B|| |X| · e^{−μd} · (e^{2κ|t|} − 1)`,

for all `t` and every finite `Λ`, with constants depending only on
`||A||`, `||B||`, `n_X^w ≤ |X|κ`, `κ`, `μ`, `d` — not on `|Λ|` and not
on the site dimensions. `||[A, B]|| = 0` on the tensor class and on the
even sector of the CAR class; for odd-odd CAR pairs the zeroth term is
kept exactly as in the block04 sibling. Sanity, gated: at `t = 0` the
bound is tight (`e^0 − 1 = 0`); the `k = 1` series coefficient matches
the direct order-1 term. Velocity readout: `v ≤ 2κ/μ` — **not claimed
sharp** (see the slack ladder below), and for odd-odd CAR pairs it
controls the dynamical tail only: the zeroth term `||[A, B]||` is `t`-
and distance-independent, exactly as the block04 sibling states.

**Consistency reduction and the slack ladder (worst-case envelope,
enumerated).** On the strict bond class (`||h_b|| ≤ J`): the hypothesis
gives `κ ≤ 12Je^μ` (`6` bonds per site × `|b| = 2` × `e^μ`), with
EQUALITY exactly for the saturated bulk model (a region with an
interior site whose six incident bonds all carry norm `J` — gated);
a smaller family has smaller `κ` (a single bond gives `2Je^μ`). At the
envelope, the rate is `24Je^μ` versus the direct sibling's `20Je^μ` —
the worst-case comparison is **weaker by exactly `6/5`**, same shape.
The slack decomposes exactly and is gated by enumeration: the meeting
bound's union count gives `12` where the true count of distinct bonds
meeting a bond is `11` (self double-counted at both endpoints), and the
sibling's Duhamel self-drop removes the self term for `10`. The direct
finite-range siblings remain sharper on their classes and are not
modified; this theorem's value is the class, not the constant.

**Instance families with closed-form `κ` (exact).** Pair interactions
`h_{x,y} = J_0 λ^{|x−y|} K` (`K` a fixed two-site Hermitian of norm 1,
`λ` rational, `ρ := λe^μ < 1`): with the `l1` sphere count on `Z^3`
`N_3(r) = 4r^2 + 2` (gated by enumeration at two radii),

> `κ_3D = 4J_0 · ρ(3 + ρ^2)/(1 − ρ)^3`,  `κ_1D = 4J_0 · ρ/(1 − ρ)`,

via the geometric identities `Σ r ρ^r = ρ/(1−ρ)^2`,
`Σ r^2 ρ^r = ρ(1+ρ)/(1−ρ)^3` and the exact numerator algebra
`4ρ(1+ρ) + 2ρ(1−ρ)^2 = 2ρ(3+ρ^2)` (gated symbolically); rational
instances gated by partial-sum-plus-tail brackets: `κ_3D = 14J_0` at
`ρ = 1/3`, `κ_3D = 684J_0` at `ρ = 3/4`, `κ_1D = 4J_0` at `ρ = 1/2`.
Pair supports `{x, y}` at distance `r ≥ 2` are disconnected sets —
admissible, since connectedness was retired. The landed free-bilinear
note's `W_mu` bound is the pair-support instance of this shape at
`U = 1` under the map `κ = 2W_mu` (rates matching as `2κ = 4W_mu`) —
needled as landed, not re-proved.

**Fermionic lift (nearest-neighbor restriction removed).** The block04
sibling's graded locality lemma is support-size-blind: even elements of
disjoint support commute regardless of range. Hence the boundary
reduction and base-term vanishing hold verbatim for weighted long-range
even families, and the theorem's CAR form follows with no new algebra.
Re-gated on a long-range instance: the distant even pair term
`c_0^† c_3 + c_3^† c_0` commutes exactly with the intermediate odd
generators and even density, and the weighted reduction
`[H, n_0] = [Σ_{S∋0} h_S, n_0]` holds on a mixed NN-plus-long-range
family.

**Disposition of the pure-exponential no-go (load-bearing).** The
exp-decay note proves: the reproducing ratio
`Σ_z G_μ(d(x,z))G_μ(d(z,y))/G_μ(d(x,y)) ≥ R + 1` — pure-exponential
weights have no finite reproducing constant, and its own many-body
bound therefore uses a polynomial-corrected weight. **That obstruction
does not bind this note's route:** here the decay `e^{−μd}` is
extracted from each chain **before** any summation over intermediate
supports (the weight split), and the peeling sums only the site-weighted
activity per step — the reproducing ratio is never formed. The
free-bilinear note's landed pure-exponential bound is the existing
instance of exactly this move. This disposition is the reason a
pure-exponential `|S|`-weighted hypothesis is admissible where the
reproducing method fails; both of that note's relevant displays are
needled.

## No-Go Discipline Gate

- **N1 route inventory (attacks ATTEMPTED and answered; review-sourced
  attacks folded in).** (1) hidden spatial convolution — ATTEMPTED and
  REFUTED: the peeling sums a single-center activity after the per-chain
  extraction of `e^{−μd}`; no two-point convolution ratio is formed
  (the load-bearing disposition, gated by needle and by the route
  itself); (2) contact-site multiplicity — ATTEMPTED: the union bound
  over-counts (safe direction), quantified exactly on bonds
  (`12`/`11`/`10`, gated); (3) disconnected supports — ATTEMPTED and
  ABSORBED: the chain lemma never uses connectedness (the hypothesis
  was retired; the exhaustive all-subsets gate includes disconnected
  supports); (4) pair normalization — ATTEMPTED and CORRECTED: the
  free-bilinear map is `κ = 2W_mu`, rates matching as `2κ = 4W_mu`
  (gated); (5) finite-volume uniformity — ATTEMPTED and CLARIFIED: the
  constants depend on `Λ` only through the supplied `κ` (stated in
  Hypotheses); (6) `κ = 0` — ATTEMPTED and EXCLUDED by convention
  (trivial case); (7) CAR long-range locality — ATTEMPTED and
  CONFIRMED: the graded lemma is support-size-blind (gated on the
  distant pair). Not attempted, not smuggled: the gauged-kernel /
  log-transfer-generator instantiation (one item — the kernel feed is
  its first step), the `U`-integrated measure side, and sharp
  constants (which subsume `μ`-optimization).
- **N2 hypothesis independence (pairwise) — ATTEMPTED, walls
  corrected in review.** Load-bearing hypotheses after the review
  round: Hermiticity (norm transport only, via the cited chain),
  `κ ∈ (0, ∞)` (summability and nontriviality), the `|S|` weight
  inside `κ` (peeling only), and the metric declaration (chain lemma
  only). Retired as walls: connectedness (irrelevant — proof never
  uses it) and `d ≥ 1` as anything beyond the zeroth-term convention.
  Each remaining pair separates at the named proof steps; the
  loop-pack mutation battery flips each runner gate separately (the
  runner performs no mutations).
- **N3 hidden-wall scan — ATTEMPTED.** Conditions surfaced in review
  and now explicit: `κ > 0`; volume-uniformity means dependence on `Λ`
  only through `κ`; the exact instance constants are
  infinite-family/uniform-restriction values (finite boxes have
  smaller activity — the finite-family gate computes its own exact
  `κ_box`). The metric is declared once (`l1` ambient); the landed
  notes disagree on conventions and the identification step will pay
  any conversion, not this note. The Duhamel layer is consumed with
  CONSECUTIVE overlap (the siblings' construction; the peeling
  requires it and says so).
- **N4 dependency roles with residual match, per citation —
  ATTEMPTED.**
  - [`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    supplies the Duhamel/norm-transport chain and the unrolled series
    (residual: its walk counting is bond-specific; replaced here by
    the peeling — the general-support reduction instances are re-gated
    natively). Its `20Je^μ` is the envelope comparator.
  - [`MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    the graded lemma and zeroth-term convention (residual: its NN
    class restriction — lifted here, long-range instance gated).
  - [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md):
    the chain-count skeleton and the named composition gap (residual:
    exactly the one-step composition theorem — taken here at the
    class level; needled).
  - [`EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md`](EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md):
    residual match made precise in review: its no-go is the failure of
    a pure-exponential REPRODUCING constant — not of this route's
    activity-norm criterion; its own many-body theorem covers
    arbitrary supports in the polynomial-corrected weight and is the
    comparator this note's delta is measured against (both displays
    needled).
  - [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md):
    the landed `U = 1` pair instance under `κ = 2W_mu` (rates match
    exactly; needled; not re-proved).
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only.
  - Loop-pack worker analyses (`worker_b07_*`): disclosed scaffolding,
    graded against prior supervisor ground truth; not executed or
    cited by the runner.
- **N5 rhetoric audit — ATTEMPTED, tightened in review.** Removed as
  too broad: "arbitrary-size supports are new", "the family form is
  new", the unqualified "exactly 6/5", and the unqualified CAR
  velocity reading. Present tense: the delta is the hypothesis form
  and its pure-exponential output plus the CAR formulation; the `6/5`
  is a worst-case envelope; the CAR velocity controls the dynamical
  tail only; nothing is called sharp; every landed overlap is cited
  as landed.
- **N6 partial-closure scan — ATTEMPTED.** Closed here: the weighted
  quasilocal class under the stated activity criterion, at the
  family's bar, with the finite-range bridge note's composition gap
  taken at the class level. Still open, named: the transfer/
  log-generator instantiation (whose first step is the gauged-kernel
  feed into `κ` — one item, not two), the `U`-integrated measure
  side, and sharp constants (subsuming `μ`-optimization).
- **N7 steelman (strongest counterarguments, answered) — ATTEMPTED.**
  (a) "A correct standard weighted-incidence LR proof whose novelty
  claims were too broad." Accepted in part: the review round removed
  the uniqueness claims; what remains claimed is the hypothesis form,
  its pure-exponential output with explicit constants, the CAR
  formulation, and the dispositions — each gated or needled. (b)
  "Pure-exponential weights are forbidden by the landed no-go." The
  no-go binds the reproducing method; the ratio is never formed here
  (the cross-family lens confirmed the disposition and its own
  exhaustive enumeration passed). (c) "The bond equality was false."
  Correct as found; repaired to the envelope statement with the
  saturated-model equality gated. (d) "The pair map missed a factor
  2." Correct as found; repaired, and the corrected map makes the
  rates agree exactly — strengthening the consistency story.
- **N8 prior-wall echo — ATTEMPTED.** The relevant prior walls are
  quoted and dispositioned in the body: the reproducing no-go
  (non-binding here — confirmed by the cross-family lens), the
  finite-range note's composition gap (taken), the exp-decay note's
  "separate source" sentence (partially answered at the class level;
  the transfer-generator instantiation remains open), and the block04
  NN restriction (lifted). No landed no-go forbids a supplied
  activity-norm hypothesis; the family's exhibit-pair discipline is
  repeated (tight `t = 0`; envelope ladder enumerated; union-bound
  strictness exhibited).

**Status: PASS** (recomputed after the review round: the four review
majors — bond equality, delta overstatement with the factor-2 map,
`κ = 0`, and runner gate strength — are repaired in text and gates;
the review's exhaustive disconnected-support enumeration is now a
native runner gate).

## Non-Claims

- Does **not** re-prove the landed `U = 1` scalar-bilinear bound (the
  free-bilinear note owns it; needled as the pair-support instance).
- Does **not** perform the gauged-kernel identification, the
  log-transfer-generator instantiation, or any `U`-integrated
  statement — all named open.
- Does **not** claim sharp constants (the `6/5` bond-class ladder is
  the worst-case-envelope slack; the direct finite-range siblings stay
  sharper on their classes and are unmodified), and does **not** claim
  the bond-class envelope `κ ≤ 12Je^μ` is attained off the saturated
  bulk model.
- Does **not** cover non-Hermitian terms or metrics other than the
  declared ambient `l1` (disconnected supports ARE covered — the
  connectedness hypothesis was retired in review as irrelevant).
- Does **not** claim uniqueness of the family form or of the
  arbitrary-support coverage (the exp-decay note covers arbitrary
  finite supports in its polynomial-corrected weight; the delta is the
  hypothesis form and its pure-exponential output).
- Does **not** cover `d = 0` (standing scoping hypothesis; zeroth-term
  conventions as in the siblings).
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py`](../scripts/microcausality_weighted_quasilocal_class_walk_expansion_2026_07_18.py)
— exact throughout. Gate kinds, honestly distinguished: **exhaustive
finite gates** (the `l1` sphere counts at `r = 1..4`; the bond meeting
counts `12`/`11`/`10`; chain-lemma reach on mixed-size segment
families; the ALL-SUBSETS peeling gate — every nonempty subset of a
five-site segment as a support, disconnected ones included, all chains
at `k = 1, 2, 3` summed exactly against the bound; the finite
pair-family chain sums with their own exact `κ_box`), **symbolic
identity gates** (the inductive-step algebra; the numerator identity;
the finite-`N` telescoping identities for BOTH `Σ r ρ^r` and
`Σ r² ρ^r`; the `2^{k+1}κ^{k−1} = (2/κ)(2κ)^k` resummation with the
series identity; the order-one majorant coefficient and `t = 0`
tightness), **bracket gates** (closed-form `κ` instance values
certified by exact partial sums plus geometric tail bounds — the
brackets certify the VALUES; the closed forms' derivation is the
telescoping identities plus a note-carried limit), **exact
representation gates** (the long-range even-CAR instance; a
mixed-size tensor reduction instance with a three-site term; the
saturated-bulk bond model attaining the envelope `12Je^μ`), and
**presence needles** (the quoted sentences of the five cited notes
and the axiom memo — presence checks, not correctness oracles; the
sibling needles read both the block03 and block04 files). The gate
sequence is enforced against an ordered label manifest. The runner
prints one `PASS`/`FAIL` line per gate and a final total; the cached
transcript is committed at the path in the header at landing time.
