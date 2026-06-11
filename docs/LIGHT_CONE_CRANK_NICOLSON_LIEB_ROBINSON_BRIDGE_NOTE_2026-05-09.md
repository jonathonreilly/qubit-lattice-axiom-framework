# Bounded Crank-Nicolson Light-Cone Bridge: Cone Inheritance with Quantified Step Defect

**Date:** 2026-05-09 (originally); 2026-06-11 (audit-failed repair: the
fixed-step quasilocal-generator claim is withdrawn as false; replaced
by the cone-inheritance theorem — see changelog)
**Type:** bounded_theorem
**Claim scope:** For a finite-dimensional finite-range Hermitian `H` on
a finite block, the Crank-Nicolson (Cayley) step
`U_CN = (I - i a_tau H/2)(I + i a_tau H/2)^(-1)` is unitary and equals
`exp(-i a_tau H_CN)` with `H_CN = (2/a_tau) arctan(a_tau H/2)` as a
**spectral identity**. The prior revision's claims that `H_CN` is
quasilocal in the weighted-overlap norm
(`W_mu(H_CN) <= (2/a_tau) artanh(x_mu)`) and that fixed-step CN
dynamics obeys the associated volume-independent fixed-`mu`
Lieb-Robinson envelope are **withdrawn as false** (the
submultiplicativity step `W_mu(H^n) <= W_mu(H)^n` fails;
see (CN-W)). The corrected load-bearing content is the
**cone-inheritance theorem (CN-C')**: on the subcritical surface
`y := a_tau ||H||/2 < 1`, each CN step differs from the exact step on
any local observable by at most
`zeta := a_tau ||[H, A]|| y^2/(1 - y^2)`; `n` steps differ by at most
`n zeta` (unitary telescoping, with `||[H, alpha_s(A)]|| = ||[H, A]||`
along the exact flow); hence the CN dynamics inherits the exact
evolution's Lieb-Robinson cone up to an explicit additive defect
`2 ||B|| n zeta = O(t a_tau^2)` at fixed `t = n a_tau`. The bridge to
the light-cone framing is therefore through the **exact** finite-range
LR bound plus a quantified integrator defect, not through any
volume-independent weighted-overlap quasilocality of `H_CN` (which
does not hold).
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome.
**Primary runner:** `scripts/light_cone_crank_nicolson_lr_2026_05_09.py`
(`TOTAL: PASS=27 FAIL=0`, deterministic, runtime well under one minute)
**Runner cache:** `logs/runner-cache/light_cone_crank_nicolson_lr_2026_05_09.txt`

## Changelog — audit-failed repair (2026-06-11)

The 2026-06-11 audit failed this row: "the current global Cayley
theorem is false as stated," with the chain explanation that "the key
weighted convolution step is not valid for powers of the global
Hamiltonian: products of disjoint local terms create disconnected
supports whose diameter includes arbitrary separation, so `W_mu(H^n)`
is not bounded by `W_mu(H)^n` in the stated support-diameter norm. A
commuting onsite Hamiltonian `H = sum_x Z_x` already makes
`H_CN = (2/a_tau) arctan(a_tau H/2)` contain nonlocal multi-site
terms." The audit suggested "a different Crank-Nicolson locality
theorem, such as a connected-cluster expansion with a valid
interaction norm or a localized/product CN scheme."

This revision:

1. **Withdraws (CN-B)'s quasilocality clause and (CN-C).** The
   submultiplicativity `W_mu(H^n) <= W_mu(H)^n` is false, and the
   failure is not repairable by sharper constants: the audit's
   commuting counterexample is made quantitative in (CN-W) below —
   for `H = Z_a + Z_b + Z_c` at ANY mutual distances, `H_CN` carries
   the three-site term `c_3(a_tau) Z_a Z_b Z_c` with the
   distance-independent coefficient
   `c_3 = (1/(2 a_tau)) [arctan(3 a_tau/2) - 3 arctan(a_tau/2)] != 0`,
   so `W_mu(H_CN) >= |c_3| e^{mu diam}` is unbounded in the diameter
   and the claimed `artanh` bound fails. The runner also exhibits the
   dynamical counterpart on a generic finite-range chain: at fixed
   `a_tau`, the one-step CN commutator tails are flat in distance at
   size `O(a_tau^3)` — there is no volume-independent fixed-`mu`,
   fixed-step envelope of the withdrawn (CN-C) weighted-overlap form.
2. **Replaces them with the cone-inheritance theorem (CN-C').** The
   valid interaction-norm route the audit asked for is realized at the
   level of the **defect generator**: with
   `D := H_CN - H = (2/a_tau) sum_{n>=1} (-1)^n (a_tau/2)^{2n+1}
   H^{2n+1}/(2n+1)` (convergent for `y < 1`), a Duhamel formula
   between the two conjugation flows plus the Leibniz expansion of
   `[H^m, B]` and the flow-invariance `||[H, alpha_s(A)]|| = ||[H,A]||`
   give the per-step defect bound `zeta` with **displayed constants**;
   telescoping (each increment evaluated on the exact orbit, where the
   `[H, .]` norm is conserved) gives the `n`-step bound; the triangle
   inequality then transfers the exact evolution's retained
   finite-range LR cone to the CN dynamics up to `2||B|| n zeta`.
   All three legs are verified numerically with margins, and the
   per-step bound is checked as an inequality, not assumed.
3. **Boundary honesty.** The proven constant carries `||H||` through
   `y` (extensive), so (CN-C') is a finite-block statement under the
   explicit subcriticality premise `y < 1`. The runner measures that
   the actual per-step defect is nearly volume-independent
   (`L = 8 -> 10` changes it by < 2x while the bound doubles), which
   the audit's connected-cluster route would explain; deriving the
   volume-independent sharpening is named follow-up work, not claimed.

## Setup

Let `H` be a finite-dimensional Hermitian Hamiltonian on a finite
block, with finite-range support family `H = sum_Z h_Z` (support size
`q`, diameter `R`, per-site overlap weight
`W = sup_x sum_{Z ni x} ||h_Z||`). The Crank-Nicolson step is the
Cayley transform

```text
    U_CN(a_tau) = (I - i a_tau H/2) (I + i a_tau H/2)^(-1).
```

Write `alpha_s(A) = e^{isH} A e^{-isH}` for the exact Heisenberg flow
and `alpha_CN(A) = U_CN^dagger A U_CN` for the CN step. Subcriticality
parameter:

```text
    y := a_tau ||H|| / 2 < 1        (declared premise of CN-C').
```

## Statements

**(CN-A) Cayley unitarity.** For Hermitian `H`, `U_CN(a_tau)` is
unitary (numerator and denominator are adjoints of each other and
commute as functions of `H`). Unchanged from the prior revision.

**(CN-B') Spectral generator identity.** As a spectral identity,

```text
    U_CN(a_tau) = exp(-i a_tau H_CN),
    H_CN := (2/a_tau) arctan(a_tau H/2),
```

i.e. each eigenvalue `E` of `H` contributes the eigenphase
`-2 arctan(a_tau E/2)`. **No locality property of `H_CN` is claimed.**

**(CN-W) Withdrawal (the prior quasilocality claim is false).** The
prior revision claimed `W_mu(H_CN) <= (2/a_tau) artanh(x_mu)` via
`W_mu(H^n) <= W_mu(H)^n`. That step is false: products of disjoint
local terms have disconnected supports whose diameters are set by the
separation of the factors, not by sums of factor diameters.
Quantitatively, for the commuting Hamiltonian `H = Z_a + Z_b + Z_c`
on three sites at arbitrary mutual distances,

```text
    H_CN = c_1 (Z_a + Z_b + Z_c) + c_3 Z_a Z_b Z_c,
    c_3 = (1/(2 a_tau)) [ arctan(3 a_tau/2) - 3 arctan(a_tau/2) ] != 0,
```

(odd spectral function of `Z_a + Z_b + Z_c`; the runner verifies the
decomposition exactly). Since `c_3` is independent of the site
positions, `W_mu(H_CN) >= |c_3| e^{mu diam}` grows without bound in
the configuration diameter, contradicting the claimed `artanh` bound
for every `mu > 0`. Dynamically, on a generic finite-range chain the
one-step CN commutator `||[alpha_CN(A_x), B_y]||` at fixed `a_tau` is
flat in `d(x,y)` at size `O(a_tau^3)` (runner block [W]); no bound of
the withdrawn (CN-C) form
`2||A|| ||B|| exp(-mu d + 4 W_CN,mu |t|)` with volume-independent
`W_CN,mu` can hold.

**(CN-C') Cone inheritance with quantified step defect (corrected
load-bearing statement).** Assume `y < 1`. For any local `A` define

```text
    zeta(A) := a_tau ||[H, A]|| y^2 / (1 - y^2).
```

Then:

- (a) per-step defect: `||alpha_CN(A) - alpha_{a_tau}(A)|| <= zeta(A)`;
- (b) n-step defect: `||alpha_CN^n(A) - alpha_{t}(A)|| <= n zeta(A)`
  at `t = n a_tau` (telescoping; each increment is evaluated on the
  exact orbit, where `||[H, alpha_s(A)]|| = ||[H, A]||` exactly);
- (c) cone inheritance: for any `B`,

```text
    ||[alpha_CN^n(A_x), B_y]||
      <= ||[alpha_t(A_x), B_y]|| + 2 ||B_y|| n zeta(A_x),
```

  where the first term obeys the exact finite-range Lieb-Robinson
  bound of the retained Hamiltonian-side authority (References), and
  the defect term is

```text
    n zeta(A) = t ||[H, A]|| y^2/(1 - y^2) = O(t a_tau^2 ||H||^2)
```

  at fixed `t`. The CN dynamics therefore inherits the exact light
  cone up to an explicit additive `O(t a_tau^2)` defect on the
  subcritical finite block.

**(CN-D) Continuum agreement.** Immediate from (CN-C'): at fixed `t`,
`alpha_CN^n -> alpha_t` at second order in `a_tau`, and the CN cone
converges to the exact LR cone at the same order. (This replaces the
prior (CN-D), which is preserved in content.)

## Proof

**(CN-A).** `I - i a_tau H/2` and `I + i a_tau H/2` are mutually
adjoint commuting normal operators; the Cayley quotient is unitary.

**(CN-B').** Diagonalize `H`; on each eigenvector with eigenvalue `E`,
`(1 - i a_tau E/2)/(1 + i a_tau E/2) = exp(-2 i arctan(a_tau E/2))`.

**(CN-W).** For commuting onsite `H` the spectral calculus acts on the
joint eigenbasis; an odd function `f(Z_a + Z_b + Z_c)` decomposes as
`c_1`-weight-one plus `c_3`-weight-three terms with
`c_3 = (1/4)[f(3) - 3 f(1)]` for `f(x) = (2/a_tau) arctan(a_tau x/2)`,
giving the displayed `c_3`. Strict concavity of `arctan` on `(0,inf)`
gives `arctan(3u) < 3 arctan(u)` for `u > 0`, so `c_3 != 0`. The
weight `e^{mu diam}` is unbounded over configurations at fixed `c_3`;
the claimed `artanh` bound fails. ∎

**(CN-C') (a).** `D := H_CN - H` has the norm-convergent series
`(2/a_tau) sum_{n>=1} (-1)^n (a_tau/2)^{2n+1} H^{2n+1}/(2n+1)` for
`y < 1`. Both maps are conjugation flows:
`alpha_CN = e^{i a_tau ad_{H_CN}}`, `alpha_{a_tau} = e^{i a_tau ad_H}`.
Interpolate `F(s) := e^{i s ad_{H_CN}} ( e^{i (a_tau - s) ad_H}(A) )`;
then `F(a_tau) - F(0) = alpha_CN(A) - alpha_{a_tau}(A)` and

```text
    F'(s) = i e^{i s ad_{H_CN}} ( [ D, alpha_{a_tau - s}(A) ] ),
```

so, with unitary invariance of the norm,

```text
    ||alpha_CN(A) - alpha_{a_tau}(A)||
      <= a_tau sup_{0<=s<=a_tau} ||[ D, alpha_s(A) ]||.
```

For each power, the Leibniz telescope
`[H^m, B] = sum_{k=0}^{m-1} H^k [H, B] H^{m-1-k}` gives
`||[H^m, B]|| <= m ||H||^{m-1} ||[H, B]||`. Since `H` commutes with
its own flow, `[H, alpha_s(A)] = alpha_s([H, A])`, so
`||[H, alpha_s(A)]|| = ||[H, A]||` exactly. Summing the series,

```text
    ||[D, alpha_s(A)]||
      <= ||[H, A]|| sum_{n>=1} (a_tau ||H||/2)^{2n}
      =  ||[H, A]|| y^2/(1 - y^2),
```

(the `1/(2n+1)` series coefficient cancels the `2n+1` Leibniz terms),
which gives (a). ∎

**(CN-C') (b).** Set `A_k := alpha_CN^k(A)` and `B_k := alpha_{k
a_tau}(A)`. Then
`A_n - B_n = alpha_CN(A_{n-1} - B_{n-1}) + (alpha_CN -
alpha_{a_tau})(B_{n-1})`, so by unitarity and (a) applied to
`B_{n-1}` — whose `[H, .]` norm equals `||[H, A]||` by flow
invariance — induction gives `||A_n - B_n|| <= n zeta(A)`. ∎

**(CN-C') (c).** Triangle inequality:
`||[A_n, B]|| <= ||[B_n, B]|| + 2 ||B|| ||A_n - B_n||`. The first term
is the exact evolution's commutator, bounded by the retained
finite-range LR authority; the second is (b). ∎

## Runner Coverage

`scripts/light_cone_crank_nicolson_lr_2026_05_09.py` (rewritten
2026-06-11; deterministic, numpy/scipy, runtime under a minute) checks:

- **[A]** Cayley unitarity and the spectral generator identity
  (eigenphase match to machine precision) on random finite-range
  chains.
- **[W]** the withdrawal witnesses: (i) the exact three-site commuting
  decomposition with the displayed distance-independent `c_3`,
  including the closed form
  `c_3 = (1/(2 a_tau))[arctan(3 a_tau/2) - 3 arctan(a_tau/2)]` and
  `c_3 != 0`; (ii) on a generic chain, a directly computed
  `W_mu(H_CN)` (Pauli-decomposition overlap weight on a small block)
  EXCEEDING the prior revision's claimed `(2/a_tau) artanh(x_mu)`
  bound — the old inequality is falsified numerically as well as
  analytically; (iii) flat one-step far tails: the `d = L-1`
  commutator is not exponentially small relative to mid-chain values
  at fixed `a_tau`, so the withdrawn volume-independent (CN-C)
  envelope is not available; the tail plateau scales like `a_tau^3`
  under step refinement.
- **[C']** the corrected theorem with margins: per-step defect
  `<= zeta` on an `(L, a_tau)` grid (inequality checked, not
  assumed); exact-orbit flow-invariance `||[H, alpha_s(A)]|| =
  ||[H,A]||`; `n`-step telescoping `<= n zeta`; the cone-transfer
  inequality at `n = 10`; and the `O(a_tau^2)` fixed-`t` convergence
  rate of the total defect.
- **[D]** small-step agreement between CN and continuous-time
  commutators (kept from the prior runner's scope).

## Hypothesis and Import Boundary

Load-bearing inputs:

- Bounded Hamiltonian-side action-support/J-budget context from
  [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  (the exact-evolution cone consumed by (CN-C')(c)).
- Hermiticity of the finite toy Hamiltonians built by the runner.
- Cayley-transform spectral calculus, the Duhamel interpolation
  between conjugation flows, the Leibniz telescope for `[H^m, B]`,
  and the geometric series on the subcritical surface `y < 1` — all
  displayed above.

Not imported as proof inputs: observed containment percentages, fitted
velocities, or a retained exact-H locality theorem. **Not claimed:**
any fixed-step quasilocality of `H_CN` (withdrawn, (CN-W)); any
volume-independent defect constant (measured smaller than the proven
bound; the connected-cluster sharpening is named follow-up work).

## Audit Boundary

This note now separates:

- what is true and proved: unitarity, the spectral generator identity,
  the withdrawal certificate (CN-W), and the cone-inheritance theorem
  (CN-C') with displayed constants on the subcritical finite block;
- what was withdrawn: the prior fixed-step quasilocal-generator claim
  and its LR envelope ((CN-B) locality clause and (CN-C));
- what remains open: a volume-independent (connected-cluster) defect
  constant, and an exact finite-range or quasilocal estimate for the
  framework's reconstructed Hamiltonian and its Crank-Nicolson kernel.

## References

- Hamiltonian-side bounded support and exact-evolution cone:
  [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
- Parent framing context, non-load-bearing here:
  `LIGHT_CONE_FRAMING_NOTE.md`
- Standard external theorem context:
  Lieb-Robinson 1972; Hastings 2004; Nachtergaele-Sims 2010; standard
  Padé/Crank-Nicolson second-order convergence; Duhamel-type
  comparison of one-parameter groups.
