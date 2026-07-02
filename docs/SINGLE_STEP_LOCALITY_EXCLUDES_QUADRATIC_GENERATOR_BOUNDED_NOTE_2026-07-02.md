# Single-Step Locality Excludes Quadratic Generator -- Bounded Note

**Date:** 2026-07-02  
**Type:** bounded support (exact tension theorem)  
**Claim type:** bounded_theorem  
**Status:** source proposal / bounded-support artifact. This note does not set
an audit outcome, derive a Record bridge, or select an action.  
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.  
**Paired runner:**
[`scripts/frontier_single_step_locality_excludes_qgen_2026_07_02.py`](../scripts/frontier_single_step_locality_excludes_qgen_2026_07_02.py)  
**Cached output:**
[`outputs/frontier_single_step_locality_excludes_qgen_2026_07_02.txt`](../outputs/frontier_single_step_locality_excludes_qgen_2026_07_02.txt)

## Purpose

This sharpens Block09's `Q-gen` condition by showing that strict single-step
locality excludes it exactly on the constructed step-generated semigroup
classes.

Block09 named the broad semigroup class

```text
c_n(t) = exp(-t psi(n)).
```

Here a finite symmetric step-set generator has

```text
S = {+-s_1, ..., +-s_m},
w_j > 0,
psi(n) = sum_j w_j (1 - cos(n s_j)).
```

On `Z_N`, the angles are `s_j=2 pi k_j/N`. On `U(1)`, they are fixed real
angles. The distinction between infinite mode growth and finite-mode
bookkeeping is load-bearing below.

## T1 -- U(1) finite-step boundedness excludes Q-gen

For any finite step set on `U(1)` with finite total weight

```text
W = sum_j w_j,
```

the generator is uniformly bounded:

```text
0 <= psi(n)
   = sum_j w_j (1 - cos(n s_j))
   <= sum_j 2 w_j
   = 2W
```

for every integer mode `n`. By contrast, `Q-gen` requires

```text
psi(n) = s n^2
```

for some `s>0`, which is unbounded as `|n| -> infinity`. Therefore no
finite-step-set semigroup on `U(1)` satisfies `Q-gen`.

The paired runner records growing-mode witnesses where `s n^2` exceeds the
finite jump bound.

## T2 -- finite `Z_N` full-step bookkeeping

On `Z_N`, the mode set is finite. Use symmetric representatives

```text
r(n) in {-floor((N-1)/2), ..., floor(N/2)}
```

with `r(0)=0`. The finite vector

```text
q_N(n) = r(n)^2
```

is even and vanishes at zero. Consequently it lies in the finite span

```text
span{1 - cos(2 pi k n/N): k=1,...,floor(N/2)}.
```

Thus the full step set can match the `Q-gen` vector exactly as a finite linear
combination. This is a finite-group bookkeeping fact, not yet a positive-rate
step semigroup.

The exact full-step weights for `N=5`, with `q_N(1)=1` and `q_N(2)=4`, are

```text
w_1 = 1 + 3 sqrt(5)/5  > 0,
w_2 = 1 - 3 sqrt(5)/5  < 0.
```

So the full linear match exists, but not with all weights positive.

For `N=7`, one exact matching set is

```text
w_1 = -(4/7)(cos(2 pi/7) + 4 cos(4 pi/7) + 9 cos(6 pi/7)) > 0,
w_2 = -(4/7)(cos(4 pi/7) + 4 cos(8 pi/7) + 9 cos(12 pi/7)) < 0,
w_3 = -(4/7)(cos(6 pi/7) + 4 cos(12 pi/7) + 9 cos(18 pi/7)) > 0.
```

The paired runner checks `N=5,7,8,9,12`. In every tested case at least one
matching full-step weight is negative:

```text
N=5:  + -
N=7:  + - +
N=8:  + - + -
N=9:  + - + -
N=12: + - + - + -
```

This is the honest finite-group subtlety: exact full-basis matching on `Z_N`
does not automatically produce a positive jump semigroup. For the tested
values it instead exposes a signed-weight obstruction.

## T3 -- nearest-step locality excludes Q-gen on every finite `Z_N`

The nearest-step class uses only

```text
S = {+-2 pi/N}
```

with one positive weight `w`, hence

```text
psi(n) = w(1 - cos(2 pi n/N)).
```

The first `Q-gen` check is

```text
psi(2) / psi(1) = 4.
```

For the nearest-step class,

```text
psi(2) / psi(1)
= (1 - cos(4 pi/N)) / (1 - cos(2 pi/N))
= sin^2(2 pi/N) / sin^2(pi/N)
= 4 cos^2(pi/N).
```

This equals `4` only when `cos(pi/N)=1`, i.e. only in the limiting
`N -> infinity` sense. For every finite `N>=3`,

```text
4 - psi(2)/psi(1)
= 4 - 4 cos^2(pi/N)
= 4 sin^2(pi/N)
> 0.
```

Thus nearest-step locality fails `Q-gen` exactly for every finite `Z_N`. The
deficit tends to zero as `N -> infinity`; this is the many-modes/small-step
limit structure, not an authority premise used here.

## T4 -- dichotomy sharpened to a trichotomy

Combining T1-T3 with Block09:

If record-composition additivity is later bridged, and if the single-step
record kernel is strictly nearest-step local, then the realized semigroup is in
the jump class

```text
c_n(t) = exp(-t psi(n)),
```

and is not the heat-kernel `Q-gen` family on every finite `Z_N`; the first-level
deficit is exactly

```text
4 sin^2(pi/N).
```

Heat-kernel selection therefore requires one of the following exact horns on
the constructed classes:

1. Extended step sets, with the finite `Z_N` caveat from T2: full-basis matching
   is a linear-span fact and may require signed weights rather than positive
   jump rates.
2. A many-step/small-step limit. This is continuum-flavored and is in tension
   with the physical-lattice baseline as conditionally quoted in Block04 from
   the scoped relocation note; no continuum limit is used here as authority.
3. Rejection of the record-composition bridge, leaving Block04's T5 as only a
   named premise rather than a derived selector.

No horn is selected.

## What this note does NOT claim

- No action is selected.
- No Record bridge is proved.
- No horn of the trichotomy is chosen.
- T2's full-step matching is a finite-group bookkeeping fact, not a physical
  proposal.
- No continuum or many-step/small-step limit is used as authority.
- No new axiom or primitive is introduced.
- No literature imports are used.

## Load-bearing inputs

- Block09 sibling:
  [`SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02.md`](SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02.md).
  Role: supplies `Q-gen`, the jump-semigroup class
  `c_n(t)=exp(-t psi(n))`, and the correction that semigroup closure alone does
  not force the heat-kernel subfamily. This sibling is stacked and unaudited.
- Block04 sibling:
  [`ACTION_FAMILY_CHARACTER_SEMIGROUP_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md`](ACTION_FAMILY_CHARACTER_SEMIGROUP_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md).
  Role: supplies the three-candidate discriminator, the `T5`
  record-composition premise, and the quoted conditional relocation-note
  context used only to state the physical-lattice tension. This sibling is
  stacked and unaudited.

## Paired runner

The paired runner reports:

```text
SUMMARY PASS=52 FAIL=0 TOTAL=52
SUMMARY T2_full_ZN_signs=N5:+-;N7:+-+;N8:+-+-;N9:+-+-;N12:+-+-+-; positive_full_step_cases=none
SUMMARY status=PASS T1_U1_bound_witnesses=n=3,4,8,16 T3_deficit=4*sin(pi/N)^2 for N=3..12
```

The checks include the `U(1)` boundedness witnesses, exact finite `Z_N`
full-basis matching by discrete cosine inversion, exact sign reporting for
`N=5,7,8,9,12`, and the nearest-step ratio/deficit identity.
