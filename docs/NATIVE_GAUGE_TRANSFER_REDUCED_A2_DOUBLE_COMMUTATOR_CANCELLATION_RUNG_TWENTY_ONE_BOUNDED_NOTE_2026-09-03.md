# Native Gauge Transfer Reduced-A2 Double-Commutator Cancellation Rung Twenty-One Bounded Note

**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Boundary:** exact second-order cancellation for the reduced saddle correction,
under the displayed self-adjoint perturbation hypotheses. This does not derive
the total second-order sign, a uniform half-line gap, a continuum limit, or a
physical Yang–Mills mass gap.

Status authority: independent audit lane only. This source note does not set or
predict an audit outcome. Parent-chain status classifies this result but does
not govern whether the result is preserved.

**Recovery provenance:** the original temporary `RUNG_21` artifact reported
in campaign memory was not located. This package independently reconstructs
the narrow exact cancellation from the surviving Rung-Twenty identity; it is
not represented as a byte-identical copy of the missing artifact.

**Primary runner:**
[scripts/native_gauge_transfer_reduced_a2_double_commutator_cancellation_rung_twenty_one_2026_09_03.py](../scripts/native_gauge_transfer_reduced_a2_double_commutator_cancellation_rung_twenty_one_2026_09_03.py)

**Runner cache:**
[logs/runner-cache/native_gauge_transfer_reduced_a2_double_commutator_cancellation_rung_twenty_one_2026_09_03.txt](../logs/runner-cache/native_gauge_transfer_reduced_a2_double_commutator_cancellation_rung_twenty_one_2026_09_03.txt)

## One-hop authority

[NATIVE_GAUGE_TRANSFER_REDUCED_A2_EIGENVALUE_RATIO_EPS_CANCELLATION_RUNG_TWENTY_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_EIGENVALUE_RATIO_EPS_CANCELLATION_RUNG_TWENTY_BOUNDED_NOTE_2026-06-12.md)
and its
[runner](../scripts/native_gauge_transfer_reduced_a2_eigenvalue_ratio_eps_cancellation_rung_twenty_bounded_2026_06_12.py)
define and check the reduced saddle data

```text
T_0 = S M_[H exp(-Q)] S,
R = partial_x + partial_y,
T_1 = [R,T_0],
P_2 exp(-Q) = (1/2) R^2[H exp(-Q)] + 3 H exp(-Q).
```

It derived the first-order eigenvalue-ratio cancellation and left the
second-order sign as computed support. The identity in its last line contains a
separate exact cancellation that was reported in campaign memory but never
given its own remote review surface.

## Exact operator identity

Write

```text
H = x y (x+y)/2,
Q = x^2 + xy + y^2,
W = H exp(-Q),
L = (1/3)(partial_xx - partial_xy + partial_yy),
S = exp(L/2),
R = partial_x + partial_y.
```

Because `R` and `L` are constant-coefficient differential operators,
`[R,S]=0`. For any multiplier `f`,
`[R,M_f]=M_[Rf]`; therefore

```text
[R,T_0]       = S M_[R W] S,
[R,[R,T_0]]  = S M_[R^2 W] S.
```

The exact polynomial identity from Rung Twenty is

```text
P_2 exp(-Q) = (1/2) R^2 W + 3 W.
```

Hence the saddle second-order operator is

```text
T_2^sad = (1/2)[R,[R,T_0]] + 3 T_0.                 (1)
```

This is an operator identity. It does not depend on a fitted coefficient or on
the numerical eigenfunctions of `T_0`.

## Exact perturbative cancellation

Use a finite self-adjoint realization in which `T_0` is real symmetric with a
positive simple eigenpair `T_0 Phi_i = mu_i Phi_i`, `R` is real
skew-symmetric, and

```text
T(eps) = T_0 + eps [R,T_0] + eps^2 T_2^sad + O(eps^3).
```

The ordinary second-order eigenvalue coefficient is

```text
mu_i^(2) =
  <Phi_i|T_2^sad|Phi_i>
  + sum_(k != i) |<Phi_k|[R,T_0]|Phi_i>|^2/(mu_i-mu_k).
```

In the eigenbasis of `T_0`,

```text
<Phi_k|[R,T_0]|Phi_i> = (mu_i-mu_k) R_ki,
```

and skew-symmetry gives

```text
sum_(k != i) |<Phi_k|[R,T_0]|Phi_i>|^2/(mu_i-mu_k)
  = -(1/2)<Phi_i|[R,[R,T_0]]|Phi_i>.
```

Substituting (1), the double-commutator contribution cancels exactly:

```text
mu_i^(2) = 3 mu_i,
mu_i^(2)/mu_i = 3
```

for every simple eigenstate. Therefore its contribution to the second-order
coefficient of any log eigenvalue ratio is zero:

```text
mu_1^(2)/mu_1 - mu_0^(2)/mu_0 = 0.                 (2)
```

Equivalently, through second order the displayed saddle terms are the expansion
of an orthogonal similarity transform of `T_0`, multiplied by the common
scalar `1+3 eps^2`. Similarity preserves eigenvalues and the common scalar
cancels from their ratio.

## What this corrects

Campaign memory records an earlier estimate
`a_2^dcomm approximately -0.19`. Equations (1)–(2) refute that estimate: the
double-commutator piece contributes exactly zero to the log-ratio coefficient
once the Rayleigh–Schrödinger mixing term and the explicit second-order operator
are combined.

This changes the bookkeeping of the remaining second-order coefficient. It
does not, by itself, establish that the full coefficient is positive. The
Rung-Twenty decomposition still leaves the heat/Dirichlet and local-CLT pieces,
and their fully a-priori sign remains outside this theorem.

## Scope and falsifiers

The load-bearing hypotheses are:

1. the Rung-Twenty polynomial identity for `P_2`;
2. `[R,L]=0`, so the translation generator passes through `S`;
3. a self-adjoint perturbation realization, represented here by symmetric
   `T_0,T_1,T_2` and skew-symmetric `R`;
4. a simple eigenvalue for the displayed non-degenerate perturbation formula.

The runner checks all algebra symbolically over exact rationals. It also checks
a nonuniform second-order diagonal perturbation as a falsifier: once the
`3T_0` remainder is replaced by a state-dependent relative correction, the
log-ratio cancellation fails.

Not claimed:

- positivity or a value for the complete `a_2`;
- a boundary/domain theorem transferring the formal differential identity to
  every continuum realization;
- a uniform-in-`beta` spectral gap;
- an infinite-volume or continuum Yang–Mills result;
- any audit grade or TOE-score movement.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_reduced_a2_double_commutator_cancellation_rung_twenty_one_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=25 FAIL=0
```
