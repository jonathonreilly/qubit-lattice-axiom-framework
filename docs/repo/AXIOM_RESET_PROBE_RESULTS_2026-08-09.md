# Axiom Reset Probe Results

**Date:** 2026-08-09
**Type:** meta
**Document class:** F — orientation memo. This memo carries
**no premise or interpretive weight**. It is citable for orientation and scope
discipline only, never as a premise, and it sets, predicts, and requests no
audit status.

**Subject:** computational probes of the drafted reset in
[`AXIOM_RESET_PROPOSAL_2026-08-09.md`](../AXIOM_RESET_PROPOSAL_2026-08-09.md).

**Runners.** All four are reproducible from a clean checkout:

- `scripts/probe_axiom_reset_substrate_model_existence_2026_08_09.py` — 17 PASS / 0 FAIL
- `scripts/probe_axiom_reset_locality_chirality_2026_08_09.py` — 10 PASS / 0 FAIL
- `scripts/probe_axiom_reset_born_effect_menu_2026_08_09.py` — 6 PASS / 0 FAIL
- `scripts/probe_axiom_reset_order_reversal_positivity_2026_08_09.py` — **5 PASS / 3 FAIL**

Round two, following up the negative:

- `scripts/probe_axiom_reset_bd_dalembertian_positivity_2026_08_09.py` — **0 PASS / 4 FAIL**
- `scripts/probe_axiom_reset_positivity_confound_2026_08_09.py` — **1 PASS / 8 FAIL**

---

> **SUPERSEDED IN PART, 2026-08-09.** An adversarial pass
> ([`AXIOM_RESET_ADVERSARIAL_REVIEW_2026-08-09.md`](AXIOM_RESET_ADVERSARIAL_REVIEW_2026-08-09.md))
> found that the positivity clause tested below was mis-drafted: reflection
> positivity is Euclidean and has no motivation on a Lorentzian causal set. The
> Lorentzian condition is Wightman positivity, and the Sorkin-Johnston
> construction realises it on the same sprinkled causal sets where the tests
> below fail (`min eig(W) = -2.5e-15`, commutator reproduced to `3.3e-15`,
> non-degenerate GNS rank scaling as ~N/2). **The "Lorentz invariance or a
> Hilbert space, not both" conclusion in sections 1, 3 and 4 is WITHDRAWN.**
> Sections 2.1 to 2.3 — model existence, the Nielsen-Ninomiya removal, and the
> Born form — are unaffected and stand.

## 1. Verdict

**Three of the four claims tested hold. The fourth fails, and it fails in the
place that matters most.**

The reset's cheap repairs — chirality via exponential locality, and the Born
form via an effect menu — are confirmed decisively and are not in doubt. Model
existence is discharged. But **positivity under order reversal, the clause the
proposal itself named as its main technical risk, does not hold on the
substrate the reset exists to enable.**

The failure has a specific shape, and the shape is the finding:

> Order-reversal positivity is a **knife-edge** property. It holds on an exactly
> regular causal order with a reflection-symmetric interface layer, and fails —
> immediately, and at essentially full magnitude — for any departure from
> regularity, down to the smallest perturbation tested. A Poisson sprinkling is
> what supplies Lorentz invariance, and it is maximally far from regular.

So within these tests, **the reset cannot have both Lorentz invariance and the
positivity clause that was supposed to deliver the Hilbert space** — and there is
no compromise position between them, because the transition is discontinuous
rather than gradual.

That is a direct tension between two of the proposal's headline claims, and it
was not visible from the text.

**Round two corrects round one on the mechanism.** The first pass reported
"positivity holds on a regular causal order and fails on a sprinkled one." That
is true as far as it goes, but it conflated two variables — the regular case
also carried an interface layer that the sprinkled case lacked — and it implied
a gradient where there is a step. Section 3.2 gives the corrected account.

## 2. What holds

### 2.1 The axiom set has models (obligations 1, 2, 3 — discharged)

`Z^3 × Z` under the light-cone order `(x,t) ≼ (y,s) ⟺ s - t ≥ |y-x|_1` was
verified to be a partial order over a 625-event window, with all 390 625 pairs
and compositions checked, and every order interval finite and bounded by its
causal span. **Existing lattice work therefore has a recovery path**: the
lattice is a model of the drafted Substrate axiom, not something it discards.

A 120-event Poisson sprinkling was verified to be a partial order, and interval
cardinality was found to track interval spacetime volume with correlation
0.9794 and fitted slope 61.7 against a sprinkling density of 60.0 — a ratio of
1.028. The "number = volume" property is measured, not assumed.

An explicit model of all four drafted axioms was constructed on a six-event
causal set: isotony, commutation at order-unrelatedness, and generation of
unions from parts all verified on the region algebras; the amplitude verified
invariant under both order automorphisms, local through links only, and
non-factorizing over events (residual 3.28 against the single-event span), which
discharges non-triviality.

**One caveat is recorded in the runner output rather than buried:** the model is
kinematic. In a tensor-product assignment *all* disjoint regions commute, so the
locality axiom is satisfied but not stressed. Existence is established;
existence of a *dynamically interesting* model is not.

### 2.2 Exponential locality really does buy chirality

This is the sharpest positive result, and it confirms the "one word" claim
exactly. In two dimensions, measured rather than assumed:

| Operator | Support radius | Species | Chiral relation |
|---|---|---|---|
| naive | 1 (strictly nearest-neighbour) | **4** = 2^d | exact, `max abs{γ5,D} = 0` |
| Wilson | 1 (strictly nearest-neighbour) | 1 | **broken**, `max abs{γ5,D} = 8.0` |
| overlap | **24** (not compact) | **1** | **exact Ginsparg–Wilson**, residual `1.4e-15` |

The two strictly nearest-neighbour operators exhibit the Nielsen–Ninomiya
trade in both directions: keep exact chiral symmetry and you get four species;
keep one species and chiral symmetry breaks. The overlap operator escapes the
trade, and the measurement of *how* is the point — its position-space profile
decays as `exp(-0.904·|x|_1)` with `R² = 0.9893`, falling by a factor `2.6e4`
between `|x|_1 = 1` and `12`, with support radius 24 rather than 1.

So the operator that escapes doubling is **exactly** the one that is local but
not nearest-neighbour. The drafted change from "nearest-neighbour" to "local"
is precisely the hypothesis being paid for, and nothing more.

One honesty note: the Ginsparg–Wilson residual of `1.4e-15` is algebraically
automatic for `D = 1 + γ5·sign(H)`, so it confirms the construction rather than
providing independent evidence. The load-bearing measurements are the species
counts and the decay profile.

### 2.3 The effect menu really does close the Born form

All three legs confirmed, with solution-space dimensions computed from null
spaces:

**Gleason fails in dimension two.** The function `f(n) = 1/2 + 0.4·n_z³` is a
valid frame function on every qubit basis — `max abs(f(n) + f(-n) - 1) = 1.1e-16`
over 4000 bases — takes legitimate probability values in `[0.103, 0.900]`, and
is **not** a trace form: the best affine fit leaves a residual of 0.166. So an
additivity axiom over a projection menu cannot force Born at dimension two.

**Gleason holds in dimension three.** Searching all even harmonics up to degree
6 (function-space rank 28), the frame condition `Σᵢ f(nᵢ) = 1` over orthonormal
triples leaves a solution space of dimension **exactly 5**, and that space
coincides with the traceless quadratics — the `ℓ = 2` sector, joint span 5.
The solutions are exactly `f(n) = nᵀρn`.

**Busch closes dimension two.** Imposing additivity over the full effect menu
instead, and searching polynomials to degree 3 in `(a, b)` (basis size 35), the
solution space collapses to dimension **exactly 4**, coinciding with the linear
forms — that is, exactly `μ(E) = Tr(ρE)`. The dimension-two counterexample
above is killed by the effect menu, violating additivity by 0.149.

**This directly validates the proposal's cheapest recommendation.** Stating
readout additivity over an effect menu rather than over disjoint records closes
the Born form at dimension two, and it does so without any substrate change.

## 3. What fails

### 3.1 Order-reversal positivity (obligation 4 — NOT discharged)

The machinery was validated first. On a `12 × 8` lattice with a free scalar and
`m² = 0.5`, both link reflection and site reflection are positive
(`min eig ≈ -3e-17`, i.e. zero to machine precision), and order reversal about a
slice was verified to be the same map as time reflection — so on a lattice the
order-theoretic form inherits the standard result exactly.

It does not survive the move off the lattice.

On twelve sprinkled causal sets of 28 events each, carrying a verified
order-reversing involution, the order-local quadratic action
`K = I − λ·A_sym/deg` gives:

| λ | positive / total | min eigenvalue range | mean ‖M‖_F |
|---|---|---|---|
| 0.05 | 1 / 12 | `[-1.58e-02, -1.0e-18]` | 3.83e-02 |
| 0.10 | 1 / 12 | `[-3.14e-02, -4.8e-18]` | 7.69e-02 |
| 0.20 | 1 / 12 | `[-6.22e-02, -1.7e-17]` | 1.56e-01 |
| 0.30 | 1 / 12 | `[-9.44e-02, -3.3e-17]` | 2.38e-01 |
| 0.45 | 1 / 12 | `[-1.48e-01, -8.9e-18]` | 3.75e-01 |

The violations are **not marginal**: the negative eigenvalues are the same order
of magnitude as the positive ones and as the Gram matrix norm, and they grow
linearly with coupling.

**Two follow-ups localize the cause.**

*It is not sprinkling irregularity being pathological in general.* On a
**regular** 1+1 light-cone causal set treated purely as a poset — no lattice
geometry used, only the order and its reversal — the same action is positive at
every coupling tested (`min eig` from `-2.5e-22` to `-1.3e-18`, with
non-degenerate Gram matrices, `‖M‖_F` from `1.1e-03` to `1.1e-01`). Regular
order passes where sprinkling fails.

*It is not one unlucky action.* A 625-point scan over a two-parameter family of
order-local quadratic actions, built from both the link matrix and the full
causal matrix and required to stay positive-definite and order-reversal
symmetric, found **zero** non-degenerate members satisfying positivity across
all sampled causal sets. The best worst-case minimum eigenvalue over the whole
scan was `-5.14e-03`.

The initial version of this scan reported one apparent success. It was
**degenerate**: at zero coupling the Gram matrix is identically zero
(`‖M‖_F = 0.0`), hence trivially positive semi-definite and physically empty.
Rejecting degenerate Gram matrices removes it, and the corrected count is zero.

## 3.2 Round two: isolating the mechanism

**A confound in round one.** The regular test used a causal set containing a
`t = 0` layer, with the positive half taken to be `t > 0`; the sprinkled test
used a mirrored construction with no such layer. Regularity and interface
presence were varied together. A 2x2 with one construction, one action and one
test separates them:

| link action, λ=0.2 | interface | no interface |
|---|---|---|
| **regular** | **PASS** — violation `0.0000` | FAIL — `0.1489` |
| **sprinkled** | FAIL — `0.6337` | FAIL — `0.3445` |

Neither clean diagnosis survives. It is not the interface alone — sprinkled with
an interface fails, and fails *worse* than without one. It is not regularity
alone — regular without an interface fails. **Positivity requires the
conjunction**, and round one's regular case passed because it happened to have
both.

**The Benincasa-Dowker action fails everywhere, including on a regular order.**
This was the named follow-up, the literature's natural causal-set action, and
the one clearly outside round one's scanned family. Symmetrised and given a mass
term large enough to make the kernel positive-definite, it is negative in every
configuration tested — `0.6153` on a regular order with an interface, `0.5288`
sprinkled with an interface, and `-1.410` worst min eigenvalue on mirrored
sprinklings. At smaller masses the kernel is not positive-definite at all and
the Gaussian is not normalisable. **The named escape route is closed.**

**The violation is not a finite-size effect.** Sweeping the sprinkled system from
12 to 50 events, the violation normalised by the Gram matrix scale runs
`0.152 → 0.256 → 0.282 → 0.291 → 0.274 → 0.260` — a log-log slope against `N` of
**+0.332**. It saturates around 0.26–0.29 rather than washing out.

**There is no neighbourhood of regularity.** This is the sharpest result. Taking
the one passing cell — regular order, interface present, violation exactly
`0.0000` — and jittering the event positions:

| jitter | 0.0 | 0.001 | 0.005 | 0.02 | 0.05 | 0.15 | 0.40 |
|---|---|---|---|---|---|---|---|
| violation | **0.0000** | 0.4068 | 0.3759 | 0.3536 | 0.4075 | 0.4134 | 0.3617 |

Positivity breaks at the smallest perturbation tested, and the violation jumps
straight to roughly its fully-sprinkled magnitude. It does not degrade
gracefully. **Order-reversal positivity, in these action families, is a
measure-zero property of the exactly regular configuration.**

Since exact regularity is precisely what carries a preferred frame, and Poisson
randomness is precisely what removes one, the two requirements are not merely in
tension — they are separated by a discontinuity with nothing in between.

## 4. What this means for the proposal

**The three cheap repairs are confirmed and should be treated as safe.**
Exponential locality, the effect menu, and naming the kernel are unaffected by
the negative result — none of them depends on the substrate change or on
positivity. The proposal's recommendation to take those three first now has
direct computational support.

**The substrate change is in worse shape than the proposal claimed.** The draft
asserts that positivity under order reversal "supplies, as consequences rather
than as axioms, the Hilbert space, unitary dynamics, and positive energy." On a
sprinkled substrate, these probes do not support that. The clause is not merely
unproven there — the natural order-local action family appears to be
**incompatible** with it.

**The tension is structural, not incidental, and round two makes it sharp.**
Lorentz invariance was the entire reason to prefer an order-theoretic substrate,
and it requires the sprinkling, because a regular causal order carries a
preferred frame just as a lattice does. Positivity sits on the exactly-regular
point and nowhere near it. Across two action families, two interface
configurations, six system sizes and a jitter sweep, **exactly one configuration
out of everything tested was positive, and it was the fully regular one.**

The proposal's own recommendation — take the three cheap repairs, treat the
substrate change as an owner call — survives. What does not survive is the
reason given for the substrate change being attractive. As drafted, the Law
axiom's positivity clause does not deliver a Hilbert space on a frame-free
substrate, and no tested action makes it do so.

## 5. Limits of these probes

Stated so the negative is not over-read:

- **One action family.** Two-parameter, order-local, quadratic. A failure across
  it does not prove impossibility over all amplitude assignments.
- **Linear functionals only.** Positivity of the Gram matrix on linear
  functionals is a *necessary* condition for reflection positivity, so the
  observed failures are genuine failures — but the regular-causal-set passes are
  correspondingly not proofs of full positivity.
- **Small systems.** 24–28 events for the sprinklings, 169 for the regular
  causal set. Finite-size effects are not excluded.
- **One construction of the involution.** The mirrored sprinkling is one way to
  obtain an order-reversing symmetry; others may behave differently, and links
  crossing the mirror directly may be atypical.
- **Two action families now, not one.** The Benincasa–Dowker operator has been
  tested and fails. That closes the named follow-up, but two families are still
  not all families — in particular, non-Gaussian amplitudes and non-quadratic
  actions remain untested, as do higher-dimensional causal sets.
- **The interface construction is one choice among several.** A `t = 0` layer of
  θ-fixed events is the natural analogue of lattice site reflection; a link-type
  reflection with no fixed events is the other, and both were tested. Other
  antichain choices for the reflection surface were not.

## 6. Recommendation

Unchanged for the three cheap repairs: take them, they are confirmed.

Hardened for the substrate: **the Hilbert-space payoff should be treated as
unavailable, not merely unproven.** The named escape route is now closed, the
violation is not finite-size, and there is no neighbourhood of regularity to
retreat to. Obligation 4 would need a qualitatively different amplitude class —
non-Gaussian, or a different notion of positivity altogether — and the honest
statement in the meantime is that the drafted reset delivers Lorentz invariance
*or* a reconstruction theorem, but not both.

This does not sink the reset. It relocates it: the three non-substrate repairs
stand on their own evidence, and the substrate change should be argued, if at
all, on background independence and the frame problem rather than on a
Hilbert-space payoff it does not currently deliver.
