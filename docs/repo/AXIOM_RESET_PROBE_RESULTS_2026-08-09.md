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

---

## 1. Verdict

**Three of the four claims tested hold. The fourth fails, and it fails in the
place that matters most.**

The reset's cheap repairs — chirality via exponential locality, and the Born
form via an effect menu — are confirmed decisively and are not in doubt. Model
existence is discharged. But **positivity under order reversal, the clause the
proposal itself named as its main technical risk, does not hold on the
substrate the reset exists to enable.**

The failure has a specific shape, and the shape is the finding:

> Order-reversal positivity **holds on a regular causal order** and **fails on a
> sprinkled one**, for every non-degenerate action in the family tested. But a
> regular causal order has a preferred frame, exactly like a lattice. Sprinkling
> is what buys Lorentz invariance. So within this test, **the reset cannot have
> both Lorentz invariance and the positivity clause that was supposed to deliver
> the Hilbert space.**

That is a direct tension between two of the proposal's headline claims, and it
was not visible from the text.

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

**The tension is structural, not incidental.** Lorentz invariance was the entire
reason to prefer an order-theoretic substrate, and it requires the sprinkling,
because a regular causal order carries a preferred frame just as a lattice does.
The probes place positivity on the regular side of that divide. Either a wider
action class recovers positivity on sprinklings, or the reset must give up one
of the two things it was designed to deliver.

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
- **The literature's natural candidate was not tested.** The Benincasa–Dowker
  causal-set d'Alembertian is the obvious action to try next, and is not in the
  scanned family. **This is the single most valuable follow-up probe**, and until
  it is run the negative should be read as "the natural family fails" rather than
  "no action works."

## 6. Recommendation

Unchanged for the three cheap repairs: take them, they are confirmed.

Changed for the substrate: **do not treat the Hilbert-space payoff as available.**
Before the substrate change can be argued on its merits, obligation 4 needs
either a wider action class that restores positivity on sprinklings — starting
with the Benincasa–Dowker operator — or an explicit admission that the reset
delivers Lorentz invariance *or* a reconstruction theorem, but not both.
