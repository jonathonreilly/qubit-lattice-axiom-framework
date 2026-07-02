# Exact Q-gen Is Not Positive on Tested Z_N; Wrapped Gaussian Correction -- Bounded Note

**Date:** 2026-07-02  
**Type:** bounded theorem (positivity lemma + exact incompatibility + certified corrections)  
**Claim type:** bounded_theorem  
**Status:** source proposal / bounded-theorem artifact. This note does not set
an audit outcome, derive a Record bridge, or select an action.  
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.  
**Paired runner:**
[`scripts/frontier_exact_qgen_wrapped_gaussian_correction_2026_07_02.py`](../scripts/frontier_exact_qgen_wrapped_gaussian_correction_2026_07_02.py)  
**Cached output:**
[`outputs/frontier_exact_qgen_wrapped_gaussian_correction_2026_07_02.txt`](../outputs/frontier_exact_qgen_wrapped_gaussian_correction_2026_07_02.txt)

## Purpose

Block10 showed that exact finite `Q-gen` matching on tested `Z_N` groups is a
signed full-basis fact, not a positive jump-rate construction. This note closes
the named positivity follow-up for the tested cases:

```text
exact character family exp(-t r(n)^2) on tested finite groups
  != positive convolution semigroup at small t.
```

The positive Gaussian-like object on `Z_N` is instead the wrapped Gaussian. It
is positive by construction, but its finite-group characters contain exact
theta corrections and are not the exact `exp(-s n^2)` family at the certified
sampled points below.

## T1 -- finite Markov positivity lemma

Let `L` be a real symmetric circulant matrix on finite `Z_N`, and set

```text
P_t = exp(tL).
```

At the level needed here, `P_t` is entrywise nonnegative for every `t>=0` iff
the off-diagonal entries of `L` are all nonnegative.

First assume the off-diagonal entries are nonnegative. Choose

```text
c >= max_i (-L_ii).
```

Then `L+cI` is entrywise nonnegative. For every `t>=0`,

```text
exp(tL) = exp(-ct) exp(t(L+cI)).
```

The scalar `exp(-ct)` is positive, and

```text
exp(t(L+cI)) = sum_{m>=0} t^m (L+cI)^m / m!
```

is a series of entrywise nonnegative matrices. Hence `P_t` is entrywise
nonnegative.

Conversely, suppose some off-diagonal entry has

```text
L_ij = -a < 0.
```

Let `B >= ||L||_infty`. For `0<tB<=1`,

```text
(P_t)_ij = t L_ij + R_ij,
R_ij = sum_{m>=2} t^m (L^m)_ij / m!,
```

and

```text
|R_ij| <= sum_{m>=2} (tB)^m / m!
       <= (e/2) t^2 B^2
       < 2 t^2 B^2.
```

Thus any rational `t` with

```text
0 < t <= 1/B,
t < a/(4B^2)
```

gives `(P_t)_ij < 0`. Therefore positivity for all `t>=0` forces every
off-diagonal entry of `L` to be nonnegative.

For a row-sum-zero convolution generator this is exactly the finite Metzler
condition for a positive finite Markov semigroup.

## T2 -- exact Q-gen fails positivity on tested Z_N

For odd `N`, write the exact finite `Q-gen` character exponent as

```text
psi(n) = r(n)^2,
r(n) in {-floor((N-1)/2), ..., floor((N-1)/2)}.
```

The generator is the circulant whose Fourier eigenvalues are `-psi(n)`.
Block10 computed the equivalent full-step weights for tested `N`. For `N=5`,

```text
w_1 = 1 + 3 sqrt(5)/5,
w_2 = 1 - 3 sqrt(5)/5 < 0.
```

The off-diagonal generator entry at displacement `2` is `w_2/2`, hence it is
negative. The runner certifies the concrete small-time witness with

```text
sqrt(5) > 223/100,
|L_2| > 169/1000,
||L||_infty <= sum_{r=-2}^2 r^2 = 10,
t_0 = 1/2000.
```

The remainder bound from T1 gives

```text
(exp(t_0 L))_{j+2,j}
<= -t_0 (169/1000) + 2 t_0^2 10^2
= -69/2000000
< 0.
```

For `N=7`, the exact quadratic generator has off-diagonal displacement-`2`
entry

```text
L_2 = - cos(2 pi/7) / (2 sin^2(2 pi/7)).
```

The runner certifies `cos(2 pi/7)>31/50` by using the exact polynomial for
`x=2 cos(2 pi/7)`,

```text
x^3 + x^2 - 2x - 1 = 0,
```

with the relevant root above `31/25`. Therefore `|L_2|>1/2`. With

```text
||L||_infty <= sum_{r=-3}^3 r^2 = 28,
t_0 = 1/5000,
```

T1 gives

```text
(exp(t_0 L))_{j+2,j}
<= -t_0 (1/2) + 2 t_0^2 28^2
= -233/6250000
< 0.
```

Therefore the exact `Q-gen` character family is not a positive convolution
semigroup on the tested finite groups `Z_5` and `Z_7`. In these tested physical
finite/discrete cases, exact heat-kernel quadraticity in the finite character
representatives is incompatible with positivity at small time.

## T3 -- positive wrapped Gaussian and exact corrections

Define the wrapped Gaussian on `Z_N` by

```text
theta_j = 2 pi j / N,
G_t(j) = sum_{m in Z} exp(-(theta_j + 2 pi m)^2/(2t)),
w_t(j) = G_t(j) / sum_{ell=0}^{N-1} G_t(ell).
```

Every term in every `G_t(j)` is positive for `t>0`, so `w_t` is a positive
probability kernel by construction.

Its character coefficient is

```text
c_n(t) = sum_{j=0}^{N-1} w_t(j) exp(i n theta_j).
```

Writing `ell=j+mN` turns the numerator into the theta sum

```text
sum_{ell in Z} exp(-(2 pi ell/N)^2/(2t)) exp(2 pi i n ell/N).
```

Using the Gaussian Fourier transform for this theta series, the common
normalizing constant cancels and gives the exact dual ratio

```text
c_n(t)
= [sum_{q in Z} exp(-t (n+qN)^2/2)]
 / [sum_{q in Z} exp(-t (qN)^2/2)].
```

If only the `q=0` terms were present, then `-log c_n(t)` would equal
`(t/2)n^2`. The other theta images are the exact finite-group corrections.

The paired runner certifies the following `N=5` intervals using truncated dual
theta sums with explicit Gaussian tail bounds. The maximum omitted tail bound
over the displayed samples is at most `2.000000000000E-95`.

```text
t=1/5, n=1:
  -log c_n(t) in [2.601180228207E-2, 2.601180228207E-2]
  (t/2)n^2    in [1.000000000000E-1, 1.000000000000E-1]
  difference  in [-7.398819771793E-2, -7.398819771793E-2]

t=1/5, n=2:
  -log c_n(t) in [6.958658342420E-2, 6.958658342420E-2]
  (t/2)n^2    in [4.000000000000E-1, 4.000000000000E-1]
  difference  in [-3.304134165758E-1, -3.304134165758E-1]

t=1, n=1:
  -log c_n(t) in [4.994544967071E-1, 4.994544967071E-1]
  (t/2)n^2    in [5.000000000000E-1, 5.000000000000E-1]
  difference  in [-5.455032929034E-4, -5.455032929034E-4]

t=1, n=2:
  -log c_n(t) in [1.921117718830E+0, 1.921117718830E+0]
  (t/2)n^2    in [2.000000000000E+0, 2.000000000000E+0]
  difference  in [-7.888228117042E-2, -7.888228117042E-2]

t=2, n=1:
  -log c_n(t) in [9.999996941255E-1, 9.999996941255E-1]
  (t/2)n^2    in [1.000000000000E+0, 1.000000000000E+0]
  difference  in [-3.058744984565E-7, -3.058744984565E-7]

t=2, n=2:
  -log c_n(t) in [3.993284651539E+0, 3.993284651539E+0]
  (t/2)n^2    in [4.000000000000E+0, 4.000000000000E+0]
  difference  in [-6.715348461342E-3, -6.715348461342E-3]
```

All displayed difference intervals are strictly negative, so the deviation
from exact quadraticity is certified nonzero at these rational sampled points.

Thus the positive Gaussian-like finite object has the structure

```text
psi_t(n) = -log c_n(t)
         = (t/2)n^2 + exact theta corrections,
```

not exact finite `Q-gen`.

## T4 -- consequence for the selection question

The action wall's heat-kernel candidate, transported to the physical
finite/discrete setting, bifurcates:

1. Exact `Q-gen`: satisfies the exact finite character quadratic condition, but
   fails positivity on the tested groups `Z_5` and `Z_7`.
2. Wrapped Gaussian: positive by construction, but only approximately
   quadratic, with exact computable theta corrections certified above for
   sampled rational times on `Z_5`.

Any future record-composition bridge must therefore name which object it
selects. Block10's trichotomy horn (a) sharpens from "extended step sets" to
the finite positivity distinction above. This note names the distinction only;
it does not select a horn.

## What this note does NOT claim

- No action is selected.
- No Record bridge is proved.
- No horn of the Block10 trichotomy is selected.
- No all-`N` theorem is claimed; exact `Q-gen` positivity failure is certified
  only for the tested groups `N=5` and `N=7`.
- Wrapped-Gaussian correction intervals are certified only for the displayed
  rational samples on `Z_5`.
- No new axiom or primitive is introduced.
- No literature imports are used.

## Load-bearing inputs

- Block10 sibling:
  [`SINGLE_STEP_LOCALITY_EXCLUDES_QUADRATIC_GENERATOR_BOUNDED_NOTE_2026-07-02.md`](SINGLE_STEP_LOCALITY_EXCLUDES_QUADRATIC_GENERATOR_BOUNDED_NOTE_2026-07-02.md).
  Role: supplies the exact finite full-step matching data and the signed-weight
  obstruction for tested `Z_N`. This sibling is stacked and unaudited.
- Block09 sibling:
  [`SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02.md`](SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02.md).
  Role: supplies the broad semigroup class `c_n(t)=exp(-t psi(n))` and the
  correction that semigroup closure alone does not force exact `Q-gen`. This
  sibling is stacked and unaudited.

## Paired runner

The paired runner reports:

```text
SUMMARY PASS=37 FAIL=0 TOTAL=37
SUMMARY T1_T2 exact_Qgen_not_positive N5:k=2,t0=1/2000,entry_upper=-69/2000000;N7:k=2,t0=1/5000,entry_upper=-233/6250000
SUMMARY T3 wrapped_gaussian_N5 t=1/5,n=1:neglog[2.601180228207E-2,2.601180228207E-2],quad[1.000000000000E-1,1.000000000000E-1],diff[-7.398819771793E-2,-7.398819771793E-2]|t=1/5,n=2:neglog[6.958658342420E-2,6.958658342420E-2],quad[4.000000000000E-1,4.000000000000E-1],diff[-3.304134165758E-1,-3.304134165758E-1]|t=1,n=1:neglog[4.994544967071E-1,4.994544967071E-1],quad[5.000000000000E-1,5.000000000000E-1],diff[-5.455032929034E-4,-5.455032929034E-4]|t=1,n=2:neglog[1.921117718830E+0,1.921117718830E+0],quad[2.000000000000E+0,2.000000000000E+0],diff[-7.888228117042E-2,-7.888228117042E-2]|t=2,n=1:neglog[9.999996941255E-1,9.999996941255E-1],quad[1.000000000000E+0,1.000000000000E+0],diff[-3.058744984565E-7,-3.058744984565E-7]|t=2,n=2:neglog[3.993284651539E+0,3.993284651539E+0],quad[4.000000000000E+0,4.000000000000E+0],diff[-6.715348461342E-3,-6.715348461342E-3];max_tail_bound=2.000000000000E-95;status=PASS
```
