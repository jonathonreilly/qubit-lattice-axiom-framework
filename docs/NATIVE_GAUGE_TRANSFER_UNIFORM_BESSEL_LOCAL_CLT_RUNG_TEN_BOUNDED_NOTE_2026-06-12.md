# Native Gauge Transfer Uniform Bessel Local-CLT Rung Ten Bounded Note

**Date:** 2026-06-12
**Type:** source-side boundary declaration
**Claim type:** bounded_theorem

**Claim boundary:** this note derives the scalar modified-Bessel local-CLT
remainder needed by the native gauge-transfer half-line gap program, starting
from the scalar integral representation of the same `I_k` atoms already used
inside the repo's Wilson Bessel-determinant coefficient convention. It proves
the scalar expansion and an explicit derived remainder bound for integer
`k >= 0`, `t >= 1`, with `a = k / sqrt(t)`. It does not assemble the
`SU(3)` determinant, the determinant mode tail, the half-slice operator tail,
or the half-line gap theorem.

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

Primary runner:
[native_gauge_transfer_uniform_bessel_local_clt_rung_ten_bounded_2026_06_12.py](../scripts/native_gauge_transfer_uniform_bessel_local_clt_rung_ten_bounded_2026_06_12.py)

Runner cache:
[native_gauge_transfer_uniform_bessel_local_clt_rung_ten_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_uniform_bessel_local_clt_rung_ten_bounded_2026_06_12.txt)

No new axiom, literature asymptotic, fitted constant, rounded anchor,
target-fed value, proxy substitution, or comparator number is used. The runner
witnesses the derived bound numerically; it does not infer the bound from the
witness rows.

## Context and One-Hop Authority

- `NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md`
  is context only, not a proof dependency. It records the scalar target form
  and the fixed-index obstruction that this note addresses.
  Quote anchor:

```text
uniform expansion of the form
   `exp(-t) I_k(t) = (2 pi t)^(-1/2) exp[-k^2/(2t)]
   (1 + P_1(k/sqrt(t))/t + R_2(k,t))`, with an explicit bound on `R_2`
   for all determinant indices and with a summable tail for the mode `n`.
```

  Quote anchor:

```text
This is the correct type of input for the active window, but that
uniform remainder is not supplied by the retained material used here.
```

  Quote anchor for the failed fixed-index reading:

```text
This reading fails as a uniform active-window proof input. If
`k = 2 sqrt(t)`, then the displayed next factor is
`-1 + 1/(8t)`, negative for `t > 1/8`, while `I_k(t)` is positive.
```

- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  records the repo-native Bessel-determinant role of the scalar `I_k`
  entries. Quote anchor:

```text
`a_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1)^3
                    / (d_(p,q) c_(0,0)(beta))`,
```

- [frontier_su3_wilson_closed_form_fanout_2026_05_04.py](../scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py)
  supplies the exact code-level Wilson coefficient convention used by the
  existing Bessel-determinant runners. Quote anchor:

```text
c_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1..3)
```

The scalar integral representation used below is the requested source-side
definition of the same integer-order modified-Bessel atom:

```text
I_k(t) = (1/pi) int_0^pi exp(t cos theta) cos(k theta) d theta.
```

No special-function asymptotic is imported.

## Scalar Object

For integer `k >= 0`, `t >= 1`, and

```text
a = k / sqrt(t),
```

define the normalized scalar kernel by

```text
B_k(t) = exp(-t) I_k(t).
```

Then

```text
B_k(t)
 = (2 pi t)^(-1/2) exp(-a^2/2)
   * (1 + P_1(a)/t + R_2(a,t)),
```

where

```text
P_1(a) = (a^4 - 6 a^2 + 3) / 24.
```

The derived relative remainder bound is

```text
|R_2(a,t)| <= C(a) / t^2,
C(a) = C_0 exp(a^2/2),
```

with

```text
C_0 =
  105 sqrt(2) / 36864 * (24/11)^(9/2)
  + 1/48
  + 29/8
  + sqrt(2 pi) * (60/(11 e))^(5/2).
```

Equivalently, the scalar absolute error has the all-`a` bound

```text
|B_k(t)
 - (2 pi t)^(-1/2) exp(-a^2/2) * (1 + P_1(a)/t)|
 <= C_0 / (sqrt(2 pi t) t^2).
```

Both readings matter. The relative remainder bound is uniform after fixing an
active window `0 <= a <= A`, with `C_A = C_0 exp(A^2/2)`. The absolute scalar
error is uniform over all `a >= 0`; the Gaussian factor in the leading profile
cancels the `exp(a^2/2)` in the displayed relative constant.

## Derivation From The Integral Representation

Start with

```text
exp(-t) I_k(t)
 = (1/pi) int_0^pi exp[-t(1 - cos theta)] cos(k theta) d theta.
```

Substitute `theta = s / sqrt(t)`. Since `k = a sqrt(t)`, the oscillatory
factor is exact:

```text
cos(k theta) = cos(a s).
```

Thus

```text
exp(-t) I_k(t)
 = (1/(pi sqrt(t))) int_0^(pi sqrt(t))
     exp[-t(1 - cos(s/sqrt(t)))] cos(a s) ds.
```

On the core region `0 <= s <= sqrt(t)`, set

```text
u(s,t) = t [cos(s/sqrt(t)) - 1 + s^2/(2t)].
```

For `0 <= s/sqrt(t) <= 1`, the alternating cosine series gives the exact
inequalities

```text
0 <= u(s,t) <= s^4/(24t),
0 <= s^4/(24t) - u(s,t) <= s^6/(720t^2).
```

Therefore

```text
exp[-t(1 - cos(s/sqrt(t)))]
 = exp(-s^2/2) exp(u(s,t)).
```

Subtract the first-order core approximation:

```text
exp(-s^2/2) * (1 + s^4/(24t)).
```

Using `exp(u) - 1 - u <= u^2 exp(u)/2` and
`u <= s^4/(24t) <= s^2/24` on the core,

```text
| exp[-t(1 - cos(s/sqrt(t)))]
  - exp(-s^2/2) * (1 + s^4/(24t)) |
<= t^(-2) [
     s^8 exp(-11 s^2/24) / 1152
   + s^6 exp(-s^2/2) / 720
   ].
```

Integrating the absolute value over the core gives

```text
B_core =
  (1/1152) int_0^infty s^8 exp(-11s^2/24) ds
  + (1/720) int_0^infty s^6 exp(-s^2/2) ds.
```

The first omitted piece is the Gaussian approximation tail beyond
`s = sqrt(t)`:

```text
int_sqrt(t)^infty exp(-s^2/2) * (1 + s^4/(24t)) ds
 <= t^(-2) [
      int_0^infty s^4 exp(-s^2/2) ds
    + (1/24) int_0^infty s^6 exp(-s^2/2) ds
    ].
```

The second omitted piece is the actual integral tail `theta >= 1`. The
alternating cosine bound gives `cos(1) <= 13/24`, hence
`1 - cos(theta) >= 11/24` for `1 <= theta <= pi`, and

```text
int_sqrt(t)^(pi sqrt(t)) exp[-t(1 - cos(s/sqrt(t)))] ds
 <= pi sqrt(t) exp(-11t/24)
 <= pi * (60/(11e))^(5/2) * t^(-2).
```

Combining these three derived pieces yields an absolute integral remainder
`B_abs / t^2`, where

```text
B_abs =
  (1/1152) int_0^infty s^8 exp(-11s^2/24) ds
  + (1/720) int_0^infty s^6 exp(-s^2/2) ds
  + int_0^infty s^4 exp(-s^2/2) ds
  + (1/24) int_0^infty s^6 exp(-s^2/2) ds
  + pi * (60/(11e))^(5/2).
```

Evaluating the Gaussian moments gives

```text
sqrt(2/pi) B_abs = C_0.
```

This is the displayed `C_0`; no residual grid is used to choose it.

## The Next-Order Coefficient

The leading Gaussian integral is

```text
J_0(a) = int_0^infty exp(-s^2/2) cos(a s) ds
       = sqrt(pi/2) exp(-a^2/2).
```

The first correction is

```text
J_1(a) = (1/24) int_0^infty s^4 exp(-s^2/2) cos(a s) ds.
```

Since differentiating `cos(a s)` four times returns `s^4 cos(a s)`,

```text
int_0^infty s^4 exp(-s^2/2) cos(a s) ds
 = d^4/da^4 J_0(a)
 = (a^4 - 6a^2 + 3) J_0(a).
```

Thus

```text
P_1(a) = J_1(a) / J_0(a)
        = (a^4 - 6a^2 + 3) / 24.
```

This is the uniform local-CLT correction. It differs structurally from the
fixed-index Bessel correction because it keeps `k theta = a s` exact before
expanding the Laplace kernel.

## Falsifiers

Wrong scaling falsifier: if `k = a t` instead of `k = a sqrt(t)`, then the
Gaussian Fourier factor is

```text
exp(-a^2 t / 2),
```

not `exp(-a^2/2)`. At `a = 1`, `t = 64`, the wrong factor is
`exp(-32)`, while the correct active-window factor is `exp(-1/2)`.

Wrong expansion-order falsifier: if the `s^4/(24t)` term is omitted, then
`P_1(0)` is forced to `0` instead of the derived value

```text
P_1(0) = 1/8.
```

If the sign of the `s^4/(24t)` term is reversed, then at `a = 2` the
coefficient becomes `+5/24`, while the derived value is

```text
P_1(2) = -5/24.
```

Fixed-index falsifier inherited from W85: at `k = 2 sqrt(t)`, the fixed-index
next factor is negative for `t > 1/8`, whereas the local-CLT leading Gaussian
factor is positive:

```text
exp(-2) > 0.
```

These substitutions break the real scalar object before any `SU(3)`
determinant assembly is attempted.

## Runner Witnesses

The runner prints the symbolic formulas for `P_1(a)` and `C(a)`, then uses
`scipy.special.ive(k,t)` only as a witness for the true scaled value
`exp(-t) I_k(t)`. The worst witnessed relative-bound usage on the deterministic
grid is reported in the cache as a margin row. The margin is intentionally
loose; the proof is the integral derivation above.

The runner also reports the two falsifier values:

```text
wrong scaling, a=1, t=64: exp(-32) versus exp(-1/2)
wrong sign at a=2: +5/24 versus -5/24
```

## Outcome

Honest outcome: derived scalar local-CLT remainder with named scope.

What is new here versus W85/W86/rung eight:

- W85 named the scalar uniform Bessel object and showed the fixed-index route
  fails on the active window.
- Rung eight isolated the missing Wilson-to-saddle input as a determinant-level
  estimate.
- This note derives the scalar `I_k` local-CLT atom and explicit derived
  remainder constant from the integral representation.

What is restated:

- the Bessel-determinant role of `I_k` in the existing Wilson coefficient
  machinery;
- the active-window scaling `k = O(sqrt(t))`;
- the fact that finite numerical rows are witnesses, not proof inputs.

The next path this opens is determinant/tail assembly: insert this scalar atom
into the `SU(3)` Bessel determinant, control the determinant mode sum and
normalization, then feed the resulting Wilson diagonal bound into the already
separated operator-remainder surface. This note does not perform those steps.
