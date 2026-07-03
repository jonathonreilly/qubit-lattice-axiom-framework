# Record Prior Stability Selector

**Date:** 2026-06-05
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
apply audit verdicts, does not edit audit data, and does not assert package
promotion.
**Primary runner:**
[`scripts/frontier_record_prior_stability_selector_2026_06_05.py`](../scripts/frontier_record_prior_stability_selector_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_prior_stability_selector_2026_06_05.txt`](../logs/runner-cache/frontier_record_prior_stability_selector_2026_06_05.txt)
(`PASS=37 FAIL=0`).

**Depends on:**

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md`](RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md)
- [`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`](GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md)
- the supplied two-sector generation readout with real dimensions `(1, 2)`.

---

## Result

The Record typing theorem made the selector question legal:

```text
post-record object = realized atom / label
probability       = separate state over possible atoms
selector          = choice of prior or stable target over those atoms
```

This note proves the finite selector boundary:

1. **Post-record atom symmetry selects the equal-letter endpoint.** If the
   dynamics on a finite post-record alphabet is invariant under permutations of
   record atoms and has a unique stable prior, the prior is uniform over record
   atoms. For the supplied generation two-sector alphabet, this is
   `(1/2, 1/2)`, the `s=0` endpoint.
2. **Pre-record microstate symmetry selects the dimension endpoint.** If the
   symmetry is instead uniformity over one singlet microstate and two doublet
   microstates, coarse-graining gives `(1/3, 2/3)`, the `s=1` endpoint.
3. **Stability alone does not choose the endpoint.** For every fixed dial
   position `s`, the finite Markov update

   ```text
   p_{t+1} = (1 - alpha) p_t + alpha pi_s,    0 < alpha < 1
   ```

   has `pi_s` as a unique attracting fixed point. Therefore "stable" must be
   paired with the invariance granularity or target prior; it is not by itself
   a selector.

This is the answer to the dynamics concern: **Koide is not forced**. The
equal-letter/Koide-side point is a stable setting on the dial under a named
post-record atom-symmetric information dynamics. The dimension/Born point is a
different stable setting under a named pre-record/microstate symmetry.

## Dial statement

Let a finite record alphabet have atoms `o_i` and positive multiplicities or
dimensions `d_i`. Define the record-prior dial

```text
pi_s(o_i) = d_i^s / sum_j d_j^s.
```

For the supplied two generation sectors, `d = (1, 2)`, so

```text
pi_s = (1/(1 + 2^s), 2^s/(1 + 2^s)).
```

The doublet/singlet prior odds are `2^s`. In the generation-weight dial, the
doublet sector power is `2|b|^2`, while the singlet sector power is `a^2`.
Thus the amplitude ratio is

```text
r(s) = (doublet/singlet odds) / 2 = 2^(s-1),
```

matching `GENERATION_WEIGHT_DIAL_STRUCTURE`.

Endpoints:

| Dial position | Prior over record atoms | Dynamics/invariance reading | Generation ratio |
|---|---:|---|---:|
| `s=0` | `(1/2, 1/2)` | post-record atom / block symmetry | `r=1/2` |
| `s=1` | `(1/3, 2/3)` | pre-record microstate / dimension symmetry | `r=1` |

The theorem supplies a stable selector grammar over this dial. It does not
derive the physical value of `s`.

## Proof

### 1. Atom-permutation selector

For a two-atom record alphabet with prior `(x, y)`, normalization gives

```text
x + y = 1.
```

Invariance under the nontrivial atom swap gives

```text
x = y.
```

The unique solution is `(1/2, 1/2)`. For an `n`-atom alphabet, invariance under
all finite atom permutations similarly forces all coordinates equal, hence
`pi_i = 1/n`.

This is a post-record principle: once the durable record has erased within-sector
microstate data and the dynamics acts only on record letters, atom symmetry
selects the equal-letter prior.

### 2. Microstate/dimension selector

For the supplied generation two-sector decomposition, the singlet has one real
microstate and the doublet has two real microstates. Uniformity over the three
microstates gives

```text
(1/3, 1/3, 1/3).
```

Coarse-graining the two doublet microstates into the doublet atom gives

```text
(1/3, 2/3).
```

This is the dimension/Born endpoint. It is natural on a pre-record or unresolved
microstate surface, but it is not the same principle as post-record atom
symmetry.

### 3. Stable dynamics for each dial point

For a fixed `s`, define the finite update

```text
Phi_{s,alpha}(p) = (1 - alpha) p + alpha pi_s,    0 < alpha < 1.
```

Equivalently, as a row-stochastic Markov matrix,

```text
P_s(i,j) = (1 - alpha) delta_ij + alpha pi_s(j).
```

Then:

- `pi_s P_s = pi_s`;
- `pi_s(i) P_s(i,j) = pi_s(j) P_s(j,i)`, so the chain satisfies detailed
  balance with target `pi_s`;
- for every initial probability vector `p`,

  ```text
  Phi_{s,alpha}(p) - pi_s = (1 - alpha)(p - pi_s),
  ```

  so deviations contract exactly by `1 - alpha`.

Thus every fixed `s` has a simple stable information dynamics. Stability is
not enough to select `s`; the selected `s` comes from the target prior or the
invariance principle used to define it.

## Dynamics implication

The user's pre-record/post-record distinction is load-bearing:

```text
pre-record qubit state
  -> instrument/readout probabilities
  -> realized durable record atom
  -> post-record label/count dynamics
```

If the dynamics is defined before record formation or over unresolved
microstates, the natural symmetry can be microstate/dimension symmetry, giving
the `s=1` endpoint.

If the dynamics is defined after durable record formation and only sees record
letters, the natural symmetry can be atom permutation symmetry, giving the
`s=0` endpoint.

Those are different typed surfaces. Mixing them was the category error the
Record typing firewall removed. This note says how to use that firewall:
choose the dynamics surface first, then the stable prior follows from the
corresponding invariance.

## What this unlocks for bounded/conditional lanes

This theorem gives audit and follow-up science work a decision tree:

| Row needs | New split |
|---|---|
| only a finite realized record alphabet | cite the Record typing theorem |
| equal-letter/block prior | require post-record atom symmetry or an equivalent stable target |
| dimension/Born prior | require pre-record microstate symmetry, Born/instrument structure, or an equivalent stable target |
| only "a stable prior" | keep a dial; stability alone is underdetermined |
| physical arrow or production dynamics | still needs a dynamics theorem |

So the unlock is not an automatic verdict change. It is a reusable selector
grammar for the 13 audited-conditional `selector_split_after_type` rows surfaced
by `RECORD_TYPING_AUDIT_UNLOCK_MAP_2026-06-05.md`: they can now be narrowed to
the exact missing premise instead of mixing Record, probability, weighting, and
dynamics in one blocker.

## Axiom verdict

This should not be added as a new axiom on the current surface.

The finite theorem is derived once two ingredients are supplied:

1. a finite record alphabet with positive atom multiplicities/dimensions;
2. an invariance or stable-target principle for the dynamics surface being
   used.

Record supplies the atom type, not the selector. Adding "the physical selector
is `s=0`" as an axiom would be stronger than this theorem and would bypass the
dynamics question. The cleaner route is to derive `s=0` from a post-record
atom-symmetric information dynamics if that dynamics is accepted, or to leave
the dial open when it is not.

## Boundaries

- Does not force Koide or close the charged-lepton value.
- Does not derive the physical `s`.
- Does not derive record-production dynamics, decoherence, Born frequencies, a
  heat-kernel arrow, or a native beta law.
- Does not contradict the existing sharpening/thermalizing notes: those are
  named maps on `r`, while this note classifies stable priors by invariance
  granularity.
- Does not apply audit verdicts or update audit data.

## Runner summary

The runner verifies:

- `pi_s` normalization and `r(s)=2^(s-1)`;
- endpoint priors `s=0 -> (1/2,1/2)` and `s=1 -> (1/3,2/3)`;
- atom-swap invariance selects the uniform atom prior;
- microstate uniformity coarse-grains to the dimension prior;
- reset/thermalizing Markov chains for `s=0`, `s=1`, and `s=1/2` are
  row-stochastic, detailed-balanced, stationary at `pi_s`, and contracting;
- two chains with the same stability form can select different fixed priors;
- `Q(s)` has endpoint values `2/3` and `1`, so the theorem does not force a
  single Koide-side value.

Scorecard: `PASS=37 FAIL=0`.
