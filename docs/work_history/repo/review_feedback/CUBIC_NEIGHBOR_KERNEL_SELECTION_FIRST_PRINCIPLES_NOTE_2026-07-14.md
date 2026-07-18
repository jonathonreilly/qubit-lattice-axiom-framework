# Cubic Neighbor-Kernel Selection From First Principles

**Date:** 2026-07-14

**Type:** meta

**Scope:** exact finite symmetry, counting, refinement, and coarse-graining
controls for local binary record kernels

**Authority:** none. This is a bounded selection probe, not the physical law,
an axiom proposal, an audit verdict, or a retained theorem. It changes no live
foundation surface.

## Result In Plain Language

The current symmetries do not select a probability rule, even in the smallest
binary six-neighbor problem. They leave more freedom than the earlier
one-parameter sampled-law pair displayed.

There are 64 binary colorings of a cubic site's six neighbors. Proper cubic
rotations reduce them to ten geometric types. Requiring that the two outcome
names be physically interchangeable and that a unanimous neighborhood copy
its only available value still leaves **three independent exact probability
values**. One of them distinguishes two same-count arrangements: two equal
neighbors opposite one another versus two equal neighbors around a corner.

Adding the stronger statement that only the number of each label matters,
not their arrangement, removes that geometric freedom but still leaves two
probability values free. Uniformity, maximum entropy, and proportional
refinement do not close them, because each depends on what is being counted.
Uniform over two outcome labels gives `1/2` on every mixed menu. Uniform over
six causal input channels and then coarse-graining by label gives incidence
weights such as `2/6=1/3`. Both are symmetric; they use different physical
sample spaces.

One clean principle does force the incidence rule:

> Treat the causal input channels as disjoint elementary alternatives, assign
> them a finite-additive nonnegative weight, and obtain an outcome by
> coarse-graining the channels carrying that outcome.

With equal elementary channel weight `c`, additivity gives
`w(n+1)=w(n)+c`, hence `w(n)=nc` and

```text
P(r) = n_r / sum_s n_s.
```

That is a derivation, but only after the law has said that the neighbors are
elementary mutually exclusive causal channels and that formation weight is
additive over their union. The existing Record axiom's additive **readout of
already formed disjoint records** does not say this. Every inequivalent kernel
in the probe shares the same additive record readout.

This removes the proposed generic counting sentence from the likely axiom
update. Counting becomes a theorem when the exact microscopic law supplies a
physical channel decomposition and additive instrument; without that law,
the sentence merely chooses a sample-space quotient without explaining why it
is physical.

## Exact Orbit Inventory

The six directed nearest-neighbor positions form one orbit under the 24
proper cubic rotations. Their **colored configurations** do not. The exact
rotation-orbit sizes are

```text
1, 1, 3, 3, 6, 6, 8, 12, 12, 12,
```

which sum to all 64 binary configurations.

Global outcome-label exchange pairs the ten spatial orbits into six
complement classes. Two three-versus-three geometry types are mapped to
themselves and therefore have probability `1/2`. Homogeneous-zero and
homogeneous-one form one pair fixed by singleton-copy behavior. Three paired
orbit classes retain one free probability apiece:

- one-versus-five;
- an opposite two-versus-four geometry; and
- an adjacent two-versus-four geometry.

Thus translation and full proper-cubic covariance, no privileged outcome
name, normalization, full mixed support, and homogeneous copying do not fix a
local transcript law.

## Four Exact Surviving Kernels

Let `k` of six recorded causal inputs carry label `1`. The runner verifies four
normalized, label-equivariant, proper-cubic-covariant, homogeneous-copy,
full-mixed-support kernels:

1. **incidence:** `p=k/6`;
2. **outcome-label uniform:** `p=1/2` whenever both labels occur;
3. **quadratic channel weight:** `p=k^2/(k^2+(6-k)^2)`; and
4. **shape-sensitive:** different exact weights for an opposite pair and an
   adjacent pair, with complement weights fixed by label exchange.

At one label-`1` input and five label-`0` inputs, the first three give

```text
1/6, 1/2, 1/26.
```

The shape-sensitive model gives `1/4` for two opposite label-`1` inputs and
`1/3` for two adjacent ones. Both configurations have the same counts. This
is an exact reminder that lattice covariance does not mean arbitrary
permutation invariance of a neighborhood.

## Why Common Selection Slogans Do Not Close It

### No privileged possibility

This forces outcome-name equivariance. It does not say whether physical
alternatives are outcome labels, causal links, microscopic paths, or
operational equivalence classes.

### Maximum entropy or indifference

Entropy requires a sample space. Equal weight on the two labels gives the
label-uniform kernel. Equal weight on six causal channels gives incidence.
Choosing the sample space is the unresolved physical quotient, so maximum
entropy cannot choose it first.

### Replication or refinement invariance

For any positive integer `alpha`,

```text
p_alpha(n_1,n_0)
  = n_1^alpha / (n_1^alpha+n_0^alpha)
```

is unchanged when both counts are multiplied by the same factor. The runner
checks `alpha=1,2,3,4`; all obey proportional refinement and give different
answers at `2:1`.

### Record readout additivity

The live Record statement adds scalar values over pairwise-disjoint records
after they exist. It does not add unnormalized formation propensities over
candidate causal inputs. The runner attaches the identical additive content
readout to all four inequivalent kernels. Reusing that axiom for probability
would cross an unproved semantic bridge.

## The Positive Derivation Route

Suppose an exact microscopic instrument identifies a finite disjoint set of
elementary causal channels. Suppose every elementary channel has equal weight
because those channels are related by the law's declared physical symmetry,
and suppose weights add when disjoint channel events are joined. Then, on the
nonnegative integers,

```text
w(0)=0,
w(1)=c,
w(m+n)=w(m)+w(n)
```

forces `w(n)=nc` by induction. Coarse-graining channel identities into record
content labels gives the incidence kernel.

This is the right place for the old “one ticket per physical possibility”
intuition to live: as a theorem about the exact law's elementary instrument
events and their operational quotient. It should not be a freestanding axiom
sentence until the theory has independently identified those events as the
physical alternatives.

The same logic scales toward a Born representation. Finite additivity on the
law's physical effect algebra can force a trace-form frame weight under the
known dimension/context hypotheses. It still does not identify the prepared
state, select an actual result, or prove that the exact microscopic law has
the required effect algebra. Those remain separate jobs.

## Constitutional Consequence

No additional “records are counted by...” sentence is presently justified.
It would either be too weak to determine a kernel or would silently choose the
very causal-channel quotient that needs derivation.

The acceptance test for the canonical law is instead:

> The exact referent must identify its elementary physical event/effect
> algebra and its operational coarse-graining strongly enough that finite
> record-transcript weights are invariant under mere presentation changes.

If that exact structure has finite additivity, counting follows. If it does
not, the law must give a different exact kernel and expose why. Either route
belongs inside one law referent and downstream theorems, not as a generic
Record axiom.

## No-Go Discipline: Narrow Claim

The licensed negative claim is:

> Binary nearest-neighbor covariance under the current cubic group, outcome
> label exchange, normalization, full mixed support, and homogeneous copying
> do not entail a unique local outcome kernel.

No claim is made that an exact deeper quantum law cannot select one.

### N1 — Alternative-route enumeration

| route | status | result |
|---|---|---|
| cubic and translation covariance | `EXHAUSTIVE FINITE TEST` | leaves three exact orbit-pair parameters |
| arbitrary neighbor permutation symmetry | `CONDITIONAL` | reduces geometry dependence but leaves two count parameters |
| label-space indifference | `SELECTS A LAW` | gives `1/2` on mixed support; sample-space choice supplied |
| causal-channel indifference | `SELECTS A LAW` | gives incidence; physical channel quotient supplied |
| proportional refinement | `ATTEMPTED` | every tested homogeneous power kernel survives |
| finite channel additivity | `POSITIVE` | forces linear weights once elementary disjoint channels are supplied |
| all-effects frame additivity | `LIVE POSITIVE ROUTE` | can derive trace representation under its own exact hypotheses |
| exact coherent instrument | `LIVE` | may derive channel/effect additivity and retire separate kernel prose |
| deterministic/global-history law | `LIVE` | may derive frequencies without a local sampled kernel |

### N2 — Wall-independence audit

All candidate kernels use the same lattice, outcome labels, rotation group,
support, homogeneous behavior, record append semantics, and readout. Only the
extensional mixed-profile weights—or geometry quotient—change.

### N3 — Hidden-wall scan

Arbitrary permutation symmetry, elementary-channel identity, mutual
exclusivity, equal channel weight, additivity of propensities, and the
coarse-graining map are each named. None is credited to cubic covariance or
Record readout additivity.

### N4 — Exact residual matching

The `1/6`, `1/2`, `1/26` discriminator tests the weight rule. The
opposite-versus-adjacent discriminator tests the geometry quotient. Neither
tests actuality, causal scheduling, coherent dynamics, clock, matter, or
gravity.

### N5 — Resolution and rhetoric audit

All 64 configurations and all 24 proper rotations are enumerated exactly.
All weights are rational. The conclusion is non-entailment from the listed
finite constraints, not a universal impossibility result.

### N6 — Partial-closure paths

Finite channel additivity positively derives incidence. A law-generated
effect algebra could positively derive a trace representation. Both paths are
retained rather than replaced by a proposed axiom sentence.

### N7 — Strongest steelman

A unique exact local quantum instrument could generate its own elementary
effects, prove their operational equivalences and additivity, identify the
prepared predictive state from records, and thereby derive all transcript
weights. This probe says exactly what that construction must add; it does not
rule it out.

### N8 — Cross-cycle echo

The complete sampled-law pair already established one weight fork. This probe
does not count that fact again. It closes two previously untested escape
routes: exhaustive proper-cubic orbit reduction and proportional-refinement
selection. It also supplies the positive additive-channel derivation.

## Verification

Run:

```bash
python3 scripts/cubic_neighbor_kernel_selection_first_principles_probe_2026_07_14.py
```

Expected terminal line:

```text
RESULT PASS=52 FAIL=0
```

The PASS count includes related checks and is not a count of independent
scientific facts.
