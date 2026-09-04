# Action-Family Character Semigroup Discriminator — Bounded Note

**Date:** 2026-07-02  
**Type:** bounded support (finite-beta discriminator + exact characterization)  
**Claim type:** bounded_theorem  
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Paired runner:**
[`scripts/frontier_action_family_character_semigroup_discriminator_2026_07_02.py`](../scripts/frontier_action_family_character_semigroup_discriminator_2026_07_02.py)  
**Cached output:**
[`logs/runner-cache/frontier_action_family_character_semigroup_discriminator_2026_07_02.txt`](../logs/runner-cache/frontier_action_family_character_semigroup_discriminator_2026_07_02.txt)

## Purpose

This note isolates an exact U(1) single-plaquette character discriminator for
the Wilson, heat-kernel, and principal-angle Manton action families at finite
coupling. The discriminator is the heat-kernel character law

```text
c_n = c_1^(n^2),  c_0 = 1,
```

and its convolution-semigroup reading.

The result is deliberately bounded. It proves an exact characterization and
finite-beta separations. It does **not** bridge the framework's Record axiom to
record-composition additivity, does **not** select an action, and does **not**
choose a beta value.

## Setting and normalizations

For a U(1) plaquette variable `theta in (-pi, pi]`, a bi-invariant
single-plaquette weight has character coefficients

```text
c_n = (1 / 2pi) integral_{-pi}^{pi} w(theta) exp(-i n theta) dtheta.
```

This note uses the state normalization convention `c_0 = 1`. Thus the Wilson
coefficients are ratios `c_n(W,beta)=I_n(beta)/I_0(beta)`.

The candidate families are:

- **Wilson:** `w_W(theta)` proportional to `exp(beta cos theta)`, with
  normalized coefficients `I_n(beta)/I_0(beta)`. The paired runner defines
  `I_n(beta)` in-runner by the everywhere-convergent series
  `sum_{m>=0} (beta/2)^(n+2m)/(m!(n+m)!)` and certifies truncation by the
  ratio-test bound `tail <= next_term/(1-q)`.
- **Heat-kernel:** defined here by character coefficients
  `c_n(HK,t)=exp(-n^2 t/2)`. This is a definition of the U(1) character family
  used in this note, not a literature import. The coupling normalization is
  `t = 2 N_c / beta`; at `N_c=1`, `t=2/beta`, so `c_n(HK,beta)=exp(-n^2/beta)`.
- **Manton:** the finite-beta discriminator uses the principal-angle
  single-plaquette action proportional to `exp(-beta theta^2/2)` on the
  fundamental interval `(-pi, pi]`, normalized to `c_0=1`. The paired runner
  certifies finite-window Fourier integrals by rational interval arithmetic:
  exact polynomial moment identities in `pi^2`, a Machin-certified rational
  enclosure of `pi`, a Taylor/Lagrange remainder for `exp(-theta^2/2)`, and a
  finite Gaussian-tail sign certificate for the `n=1` lower bound. A fully
  image-periodized Gaussian has pure Gaussian character coefficients and is
  therefore not the finite-window Manton witness used for T3.

Conditional source context from the unaudited
[`ACTION_FORM_NO_GO_EQUIVALENCE_PREMISE_CONTINUUM_REMOVAL_SCOPED_RELOCATION_NOTE_2026-06-08.md`](ACTION_FORM_NO_GO_EQUIVALENCE_PREMISE_CONTINUUM_REMOVAL_SCOPED_RELOCATION_NOTE_2026-06-08.md):
it records the normalization line **"(`t = 2N_c/β`, Manton coefficient =
Wilson's small-field coefficient)"** and scopes the older no-go by saying the
verdict is **"scoped to the regulator reading"** and that action selection is a
**"well-posed open physical question"**. It also states the load-bearing open
question: **"Whether it is the framework's emergent-time generator (RECORD
axiom: time = monotone record accumulation) is the load-bearing open question,
not asserted here."**

## T1 — the n^2-law characterizes the HK parameterization

For the heat-kernel definition,

```text
c_n(t) = exp(-n^2 t/2)
```

so `c_n(t)=c_1(t)^(n^2)` for every integer `n`, and in particular
`c_2(t)=c_1(t)^4`. Conversely, if a positive character family is parameterized
by one number `c_1` with `0 < c_1 < 1` and satisfies the all-mode law
`c_n=c_1^(n^2)` for every `n`, then setting `s=-log(c_1)>0` gives
`c_n=exp(-n^2 s)`. This is pure algebra; no continuum limit is used.

The paired runner checks the symbolic heat-kernel semigroup and first
nontrivial identity:

```text
PASS T4_HK_semigroup_symbolic
PASS T1_HK_first_nontrivial_symbolic
PASS T1_n2_parameterization_symbolic
```

The equality `c_2=c_1^4` is a first nontrivial discriminator for the named
families, not by itself a complete characterization of arbitrary families; see
the hostile witness below.

## T2 — Wilson violates the n^2-law at certified finite beta

For Wilson, `c_2=c_1^4` is equivalent to

```text
I_2(beta) I_0(beta)^3 = I_1(beta)^4.
```

The paired runner certifies disjoint rational intervals at `beta=1` and
`beta=2`:

```text
beta=1:
I2*I0^3 = [0.275487117914280655, 0.275487117914280655]
I1^4    = [0.102019434456149222, 0.102019434456149222]
c2      = [0.107220068206930988, 0.107220068206930988]
c1^4    = [0.0397061423548103198, 0.0397061423548103198]

beta=2:
I2*I0^3 = [8.16120469086310329, 8.16120469086310329]
I1^4    = [6.40153556862870587, 6.40153556862870587]
c2      = [0.302225342035991995, 0.302225342035991995]
c1^4    = [0.237061359207223959, 0.237061359207223959]
```

Thus Wilson is not the heat-kernel character semigroup at these finite beta
points. The continuum fact that the ratio tends toward heat-kernel agreement as
`beta -> infinity` is exactly the continuum-equivalence issue that the
conditional, unaudited relocation note scoped away from the physical finite
evaluation point.

## T3 — principal-angle Manton violates the n^2-law at certified finite beta

At `beta=1`, the runner certifies

```text
c2(Manton) = [0.134238338599399043, 0.134289739470289049]
exp(-2)    = [0.135335283236612702, 0.135335283236612702].
```

For the principal-angle Manton window, the runner certifies that the `n=1`
outside-tail cosine integral is non-positive: the lower bound on the first
negative slice `[pi,4pi/3]` exceeds the upper bound on all later positive tail
mass from `[3pi/2,infinity)`. Therefore the finite-window `c_1` is at least the
full-line Gaussian value `exp(-1/2)`, so `c_1^4 >= exp(-2)`. The certified
intervals give

```text
c_2(Manton,beta=1) < exp(-2) <= c_1(Manton,beta=1)^4.
```

Hence `c_2 != c_1^4` for the principal-angle Manton finite-window action at
`beta=1`.

## T4 — semigroup reading and Wilson non-closure

For heat-kernel coefficients,

```text
c_n(t1)c_n(t2)
= exp(-n^2 t1/2) exp(-n^2 t2/2)
= exp(-n^2 (t1+t2)/2)
= c_n(t1+t2).
```

Thus the `n^2` law is the character form of one-parameter convolution-semigroup
closure.

The Wilson family is not closed under plaquette convolution. The runner uses
the two-invariant fingerprint `(c_1,c_2)`. It first brackets the unique Wilson
parameter `beta'` whose `c_1` could match the convolution of two `beta=1`
Wilson weights:

```text
beta' = [0.406712089560935075, 0.406712089560935297]
c1(W,beta') = [0.19926400165310923, 0.199264001653109341]
c1(W,1)^2  = [0.19926400165310923, 0.19926400165310923]
```

Then it certifies the `c_2` mismatch:

```text
c2(W,beta') = [0.0201225546640418813, 0.0201225546640419056]
c2(W,1)^2  = [0.0114961430262989321, 0.0114961430262989321].
```

So the convolution-square of a Wilson plaquette weight at `beta=1` is not any
Wilson plaquette weight.

## T5 — record-side naming only

**Named selection premise only; the record-composition bridge is not established
here.** If a future bridge establishes that two successive plaquette-record
accumulations compose to a single accumulation with an additive parameter, then
the corresponding action kernel must form a one-parameter convolution semigroup.
Among the three candidates treated here, T1-T4 leave the heat-kernel family as
the qualifying semigroup family and rule out finite-beta Wilson and
principal-angle Manton witnesses.

This is only a named next-attack premise. It is tied to the conditional,
unaudited relocation note's open question about whether the heat semigroup is
the framework's emergent-time generator. It is also tied to the minimal-axiom
boundary: the Record axiom has finite scalar additivity over disjoint records,
but it does not provide record-production dynamics, a time metric, or a
plaquette-action kernel.

## Hostile witnesses

A pointwise first-level coincidence is possible without a heat-kernel family.
Let

```text
w(theta)=1 + 2e cos(theta) + 2e^4 cos(2theta) + 2b cos(3theta),
e=1/10, b=1/100.
```

Then `c_0=1`, `c_1=e`, `c_2=e^4=c_1^4`, but
`c_3=b=1/100 != c_1^9=1/1000000000`. The runner also certifies positivity of
the weight by the crude bound

```text
w(theta) >= 1 - 2(e + e^4 + b) = 3899/5000 > 0.
```

Therefore a single beta-point equality `c_2=c_1^4` is only a fingerprint
against specified action families. The actual characterization needs the
all-mode law or the semigroup property.

## What this note does NOT claim

- No action is selected.
- No beta value is selected.
- No emergent-time bridge is proved.
- T5 is a named selection premise only; the record-composition bridge is not
  established here.
- The relocation note is unaudited; its well-posedness verdict is cited only
  conditionally.
- The ADM-2/global-SU(3) reduction note is unaudited; it is cited only as
  conditional context for the bi-invariant action-form class.
- No literature imports are used. Inequalities are certified in-runner at the
  named rational beta points.
- No new axiom or primitive is introduced.
- The finite-window Manton witness is not the fully image-periodized Gaussian
  character family; the latter obeys a Gaussian `n^2` law by definition and is
  not the T3 discriminator used here.

## Load-bearing inputs

Minimal axiom boundary, quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> "When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent."

> "Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`."

The same source states that Admissibility "does not choose a Hamiltonian or
transfer operator, supply transition probabilities or weights, select a scalar
or nonzero kinetic branch, assert a Dirac-square carrier, define a time metric,
or provide a record-production process."

The open-gates list keeps the needed bridge outside the axioms, including:

> "arrow, record-production dynamics, physical persistence dynamics, time
> metric, and local observability of records;"

Conditional bi-invariant context from the unaudited
[`ADM2_GLOBAL_SU3_SYMMETRY_REDUCES_ACTION_FORM_BI_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-08.md`](ADM2_GLOBAL_SU3_SYMMETRY_REDUCES_ACTION_FORM_BI_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-08.md):

> "Therefore ADM-2 (action-form) ⟸ ADM-2′ = global-SU(3)-equivariance of the
> gauge dynamics, in the annealed (fast-equivariant-neighbour) regime."

This is used only as conditional context for why a bi-invariant action-form
class is a natural place to test the semigroup discriminator. It is not used as
a retained premise, does not close ADM-2, and does not supply the missing
record-composition bridge.

## Paired runner

The paired runner reports:

```text
SUMMARY PASS=14 FAIL=0 TOTAL=14
SUMMARY certified=Fraction intervals for Bessel, exp, pi, Gaussian tails, and Wilson fingerprint bracketing
SUMMARY status=PASS
```

Every certified-disjoint-interval claim in T2-T4 corresponds to a named runner
check. The Manton T3 comparison uses a certified finite-window `c_2` interval
and a one-sided `c_1^4 >= exp(-2)` bound from the finite Gaussian-tail sign
certificate.
