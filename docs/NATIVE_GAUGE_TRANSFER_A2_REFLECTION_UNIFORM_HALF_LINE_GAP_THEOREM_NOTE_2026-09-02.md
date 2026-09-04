---
claim_id: native_gauge_transfer_a2_reflection_uniform_half_line_gap_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "For the exact SU(3) dominant-weight packet operator T_beta = exp((beta/2)J) diag(c_lambda(beta)/c_0(beta)) exp((beta/2)J), there is a delta > 0 such that lambda_1(T_beta)/lambda_0(T_beta) <= 1-delta for every beta >= 0; moreover, the displayed global Wilson-to-saddle multiplier error is < 19/beta for beta >= 128. This is conditional on the cited recurrence/coefficient identity and is not a physical Wilson-environment, continuum, confinement, or Clay mass-gap theorem."
upstream_dependencies:
  - gauge_vacuum_plaquette_transfer_operator_character_recurrence_note
  - native_gauge_transfer_wilson_to_saddle_uniform_rung_nine_bounded_note_2026-06-12
  - native_gauge_transfer_operator_norm_remainder_rung_eight_bounded_note_2026-06-12
  - native_gauge_transfer_c00_lower_bound_rung_twelve_bounded_note_2026-06-12
runner: scripts/native_gauge_transfer_a2_reflection_uniform_half_line_gap_2026_09_02.py
---

# Native Gauge Transfer Lie-Type A_2 Reflection Uniform Half-Line Gap Theorem Note

**Date:** 2026-09-02
**Claim type:** bounded_theorem

**Claim boundary.** This note proves a uniform half-line gap for the exact
repo-native `SU(3)` dominant-weight packet operator

```text
T_beta = exp((beta/2) J) diag(c_lambda(beta)/c_0(beta)) exp((beta/2) J),
beta >= 0.
```

More precisely, there is a `delta > 0` such that

```text
lambda_1(T_beta) / lambda_0(T_beta) <= 1 - delta
```

for every `beta >= 0`.  The proof does not fit `delta`, a limiting ratio, or a
large-beta threshold from spectral data.  It also proves the stronger global
coefficient estimate

```text
sup_(p,q >= 0)
| beta^(-3/2) c_(p,q)(beta)/c_(0,0)(beta)
  - beta^(-3/2) d_(p,q) exp[-3 C2(p,q)/beta] |
< 19 / beta
```

for every `beta >= 128`.  This is global in the representation label, rather
than restricted to `p,q <= A sqrt(beta)`, and is stronger than the registered
Wilson-to-saddle `O_A(beta^(-1/2))` target (historical obligation alias `W85`).

This is a theorem about the native discrete packet operator named above.  It is
not a theorem about the physical three-dimensional Wilson environment, a
four-dimensional continuum limit, confinement, or the Clay Yang-Mills mass
gap.  It does not select the Wilson action or a physical value of `beta`.
In particular, the packet multiplier is `c_lambda/c_0`; normalized physical
group convolution instead has eigenvalue `c_lambda/(d_lambda c_0)`.  Those
operators are not silently identified here.

Status authority remains the independent audit lane.  This source note does
not assign its own retained status or edit an audit ledger.

## Machine Status And Trace

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
claim_type_reason: "The shifted-chamber reflection identity, endpoint-uniform Fourier estimates with explicit constants, common-space trace-norm limit, and compactness/Perron completion prove the declared native-packet theorem, conditional on the cited recurrence/coefficient identity."
trace_class: direct_blocker_closure
target_claim_id: native_gauge_transfer_w85_finite_witness_open_gate_note_2026-06-12
target_blocker_text: "Replace the sampled table with a proof or domain-exhaustive certificate for the intended active window and tail."
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Run independent scientific audit of this claim and re-establish the current dependency chain before any effective retained use."
conditional_surface_status: "Exact only for the declared native SU(3) dominant-weight packet and conditional on the cited recurrence/coefficient identity; physical convolution, the three-dimensional Wilson environment, action selection, continuum Yang-Mills, confinement, and the Clay mass gap remain outside scope."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Primary verifier:
[native_gauge_transfer_a2_reflection_uniform_half_line_gap_2026_09_02.py](../scripts/native_gauge_transfer_a2_reflection_uniform_half_line_gap_2026_09_02.py)

Runner cache:
[native_gauge_transfer_a2_reflection_uniform_half_line_gap_2026_09_02.txt](../logs/runner-cache/native_gauge_transfer_a2_reflection_uniform_half_line_gap_2026_09_02.txt)

No new axiom, literature constant, external comparator, fitted constant,
rounded target anchor, or finite-packet substitution enters the proof.

## Import And Support Inventory

| Input | Role | Provenance | Open bridge/status boundary |
|---|---|---|---|
| Exact `SU(3)` character recurrence and `c_lambda(beta)=<lambda|exp(beta J)|0>` identity | load-bearing scientific premise | linked recurrence note below | its current audit-ledger row is unaudited; independent audit and dependency-chain re-establishment remain open before retained use |
| Registered Wilson-to-saddle and operator-remainder targets | target/context only; they state the prior residuals but supply no step of the new proof | linked Wilson-to-saddle and operator-remainder notes below | both current rows are unaudited; this theorem proposes source-side closure without assigning their audit disposition |
| Earlier `c_(0,0)` scale | context and cross-check only; the normalization used here is re-derived from the squared Weyl alternant | linked lower-bound note below | its current row is unaudited and is not used as a retained premise |
| [`frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py`](../scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py) | support-only Bessel-determinant comparison and finite-matrix utilities imported by the verifier | repository runner named in `AUDIT_INPUT_PATHS`; its exact read is cache-fingerprinted | no analytic proof step depends on its finite rows or physical-environment ansatz |
| Finite Weyl-group algebra, Fourier inversion on the two-torus, elementary trigonometric/Gaussian bounds, incomplete-gamma identities, Hilbert-Schmidt ideal estimates, compact self-adjoint spectral perturbation, and the displayed absolute-value Perron argument | mathematical machinery | textbook-level mathematics; every normalization and load-bearing constant used here is displayed or derived in Sections 1-5, with no external numerical value | no physical bridge is supplied by this machinery; correctness remains subject to independent audit |
| Python, NumPy, SymPy, mpmath, and SciPy | implementation support only | local runtime packages | no package output is promoted to a scientific premise |
| Axioms, observations, fitted values, literature measurements, external datasets, and sibling-branch results | empty input inventory | none | none imported |

The status statements in this inventory are a review-time snapshot against
`origin/main` at `a0eab00344ea6dca3c2e3adeb12bac6d2560e725`. Historical audit records
are provenance only and are not treated as current retained authority.

## One-Hop Authorities And Exact Target

- [GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)
  supplies the exact self-adjoint six-neighbor recurrence

  ```text
  J = (chi_(1,0) + chi_(0,1))/6.
  ```

- [NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md)
  registers the missing Wilson-to-saddle coefficient estimate (historical
  obligation alias `W85`).

- [NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)
  registers the scaled operator remainder and the limit

  ```text
  S_(1/2) M_[H exp(-Q)] S_(1/2).
  ```

- [NATIVE_GAUGE_TRANSFER_C00_LOWER_BOUND_RUNG_TWELVE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_C00_LOWER_BOUND_RUNG_TWELVE_BOUNDED_NOTE_2026-06-12.md)
  records the previously derived denominator scale.  The sharper asymptotic
  and normalization used below are re-derived here from the Weyl alternant.

The target is the exact infinite operator.  Finite shells and the previously
extrapolated value `0.1938058` are not proof inputs.

## 1. Exact Shifted-Chamber Reflection Formula

Let

```text
P = {(p,q): p,q >= 0},
rho = (1,1),
C_Z = {(a,b): a,b >= 1} = P + rho,
```

and let the full triangular-lattice step set be

```text
S = {(1,0), (-1,1), (0,-1), (0,1), (1,-1), (-1,0)}.
```

The simple Weyl reflections in these coordinates are

```text
s_1(a,b) = (-a,a+b),
s_2(a,b) = (a+b,-b).
```

The signed orbit of `rho` is

```text
(1,1)      +
(-1,2)     -
(2,-1)     -
(-2,1)     +
(1,-2)     +
(-1,-1)    -.
```

Write `A` for the full-lattice adjacency divided by six and

```text
q_t(z) = <z|exp[t(A-I)]|0>.
```

The killed chamber kernel `K_t = exp[t(J-I)]` obeys the exact reflection
identity

```text
K_t(p,r)
 = sum_(w in W) det(w)
     q_t((r+rho) - w(p+rho)).                       (1)
```

This can be proved without importing a reflection theorem.  The right side
satisfies the full heat equation in its second argument.  On either shifted
wall, Weyl images pair with opposite signs, so it vanishes.  At `t=0`, only
the identity image can map one strict-chamber point to another.  Uniqueness of
the bounded killed heat equation gives (1).  Equivalently, the equality holds
coefficient-by-coefficient in the exponential series.  The verifier checks
17,545 such exact integer identities from five distinct starting weights.

Since

```text
c_(p,q)(beta) = <(p,q)|exp(beta J)|(0,0)>
               = exp(beta) K_beta((0,0),(p,q)),     (2)
```

(1) is also an exact finite-Weyl formula for every Wilson coefficient.  It is
not a saddle approximation.

## 2. Fourier Alternant And Its Required Cancellation

The full symbol is

```text
phi(k_1,k_2)
 = [cos(k_1) + cos(k_2) + cos(k_1-k_2)]/3,
psi = 1 - phi.
```

For `y=(p+1,q+1)`, (1) becomes

```text
exp(-beta)c_(p,q)(beta)
 = (2 pi)^(-2) int_T
     exp[-beta psi(k)] exp[-i k.y] A_rho(k) dk,      (3)
T = [-pi,pi]^2,
```

where the Weyl alternant has the exact factorization

```text
A_rho(k)
 = sum_w det(w) exp[i k.w(rho)]
 = 8 i sin[(2k_1-k_2)/2]
       sin[(k_1-2k_2)/2]
       sin[(k_1+k_2)/2].                            (4)
```

Thus its first nonzero Taylor term is cubic:

```text
A_rho(k) = i Delta(k) + O(|k|^5),
Delta(k) = (2k_1-k_2)(k_1-2k_2)(k_1+k_2).           (5)
```

All signed moments of degree below three vanish, and the fourth-order term
also vanishes.  This cancellation is load-bearing.  Applying an absolute
scalar local CLT separately to the six images would leave six errors of order
`beta^(-1)` while the chamber return kernel is order `beta^(-4)`.

For the denominator, Weyl invariance must be used before taking absolute
values.  Averaging the endpoint orbit gives the exact positive identity

```text
exp(-beta)c_(0,0)(beta)
 = [6(2 pi)^2]^(-1) int_T
     exp[-beta psi(k)] |A_rho(k)|^2 dk.              (6)
```

The verifier checks (6) coefficient-by-coefficient for the first 25 path
orders.  Its sixth-order zero is what makes a relative denominator estimate
possible.

## 3. Endpoint-Uniform Local CLT With Explicit Bounds

Set

```text
R(z) = z_1^2 - z_1 z_2 + z_2^2,
Q(x) = x_1^2 + x_1 x_2 + x_2^2,
H(x) = x_1 x_2 (x_1+x_2)/2,
V(x) = H(x) exp[-Q(x)].
```

The one-step covariance and inverse are

```text
Sigma = [[ 2/3, -1/3], [-1/3, 2/3]],
Sigma^(-1) = [[2,1], [1,2]],
```

so the Gaussian exponent is exactly `Q`.  Put `x=y/sqrt(beta)`.  On the
low-frequency square `|k_1|,|k_2| <= 1`, the elementary cosine and sine
remainders give

```text
R(z)/3 - R(z)^2/(36 beta)
 <= beta psi(z/sqrt(beta)) <= R(z)/3,
beta psi(z/sqrt(beta)) >= R(z)/4,                   (7)

| beta^(3/2) A_rho(z/sqrt(beta)) - i Delta(z) |
 <= |Delta(z)| R(z)/(4 beta).                       (8)
```

The identities behind these constants are

```text
z_1^4 + z_2^4 + (z_1-z_2)^4 = 2 R(z)^2,

(z_1+z_2)^2 + (2z_1-z_2)^2 + (z_1-2z_2)^2
 = 6 R(z).
```

There is only one maximum of `phi` on the Fourier torus, at zero.  On the
complement of the low square,

```text
psi >= gamma,
gamma = 1 - [cos(1) + 2 cos(1/2)]/3
      > 0.234.                                      (9)
```

To see (9), if `|k_1|>=1`, then

```text
cos(k_2)+cos(k_1-k_2)
 = 2 cos(k_1/2) cos(k_2-k_1/2)
 <= 2 cos(|k_1|/2),
```

and `cos u+2cos(u/2)` decreases on `1<=u<=pi`; the case `|k_2|>=1`
is symmetric.  Thus no center or parity saddle shares the value at zero.

For detail on (7)-(8), use

```text
u^2/2-u^4/24 <= 1-cos u <= u^2/2
```

for the three arguments `k_1,k_2,k_1-k_2`.  On the low square
`R(z)<=3 beta`, so the lower expression in (7) is at least `R/4`.
Writing (4) as `i Delta` times three `sinc` factors and using
`0<=1-sinc u<=u^2/6` gives (8), because the three squared root forms
sum to `6R`.  These are inequalities on the whole declared low square,
not sampled Taylor rows.

Define the scaled numerator and denominator

```text
N_beta(y) = exp(-beta) beta^(5/2) c_(p,q)(beta),
D_beta    = exp(-beta) beta^4 c_(0,0)(beta).
```

Equations (3)-(9), followed by Gaussian radial integration, give bounds that
are uniform in every integer endpoint `y`:

```text
|N_beta(y) - D_inf V(y/sqrt(beta))| <= epsilon_N(beta),
|D_beta - D_inf|                    <= epsilon_D(beta),               (10)

D_inf = 27 sqrt(3)/pi,

epsilon_N(beta)
 = C_N/beta + 6 beta^(5/2) exp(-gamma beta) + G_N(beta),

epsilon_D(beta)
 = C_D/beta + 6 beta^4 exp(-gamma beta) + G_D(beta),

C_N = (460/3) sqrt[2/(3 pi)],
C_D = 38912 sqrt(3)/(27 pi),

G_N(beta) = (9 sqrt(2)/pi) Gamma(5/2,beta/4),
G_D(beta) = (9 sqrt(3)/(2 pi)) Gamma(4,beta/4).       (11)
```

Here `Gamma(s,a)` is the upper incomplete gamma function.  Nothing in these
constants is inferred from Wilson residual data.  For completeness, the
radial identities used to obtain them are

```text
int_(R^2) f(R(z)) dz = (2 pi/sqrt(3)) int_0^infinity f(u) du,

int exp(-aR) Delta^2 R^m dz
 = 8 pi sqrt(3) (4)_m a^(-4-m).
```

The key uniformity in (10) is simple but easy to lose: the endpoint appears
only in `exp[-ik.y]`, whose modulus is one.  The full Fourier `L^1` error is
therefore independent of `p,q`.  The Gaussian-extension tails in (11) follow
because leaving the scaled low square implies `R(z) >= 3 beta/4`.

Explicitly, on the low square the numerator integrand error is bounded by

```text
beta^(-1) exp(-R/4) |Delta| [R^2/36+R/4],
```

and `|Delta|<=(2R)^(3/2)`.  For the squared denominator it is bounded by

```text
beta^(-1) exp(-R/4) Delta^2 [R^2/36+R/2].
```

The two radial identities following (11) evaluate these majorants to `C_N`
and `C_D`.  On the high square complement, `|A_rho|<=6` together with (9)
gives the two polynomial-exponential terms.  Extending the leading Gaussian
from the scaled square to `R^2` gives exactly `G_N` and `G_D`.  This accounts
for every term in (10)-(11).

The following conservative enclosures follow directly from the displayed
closed expressions and the elementary bound
`erfc(u) <= exp(-u^2)/(sqrt(pi)u)`:

```text
14.88 < D_inf < 14.89,
C_N < 71,
C_D < 795,
sup_(x in R_+^2) V(x)
 = exp(-3/2)/(2 sqrt(2)) < 0.079.
```

These enclosures need no floating-point premise.  For example,
`cos(1)<13/24` and `cos(1/2)<337/384` give `gamma>15/64`, while
`1.732<sqrt(3)<1.7321` and `3.141<pi<3.142` enclose `D_inf`, `C_N`, and
`C_D` as displayed.  The positive Taylor sums for `exp(2)` and `exp(3)`
give `exp(2)>7` and `exp(3)>20`, hence `exp(-30)<20^(-10)` and
`exp(-32)<(7*20^10)^(-1)`.  Together with the closed half-integer and integer
incomplete-gamma formulas, these give at `beta=128`

```text
6 beta^(5/2) exp(-gamma beta) < 1.2e-7,
G_N(beta) < 1.3e-11,
6 beta^4 exp(-gamma beta) < 1.58e-4,
G_D(beta) < 1.4e-9.
```

At `beta=128`, (10)-(11) give

```text
epsilon_N < 0.552,
epsilon_D < 6.212,
D_beta > 14.88 - 6.212 > 14.89/2.
```

Every quantity `beta epsilon_N(beta)` and `beta epsilon_D(beta)` decreases
for `beta >= 128`.  Indeed, the two polynomial-exponential derivatives change
sign at `7/(2 gamma)<15` and `5/gamma<22`.  With `t=beta/4`, integration by
parts in `Gamma(s,t)` shows that the derivatives of
`beta Gamma(5/2,beta/4)` and `beta Gamma(4,beta/4)` are negative for
`t>=32`.  Consequently,

```text
sup_(p,q)
beta | beta^(-3/2)c_(p,q)/c_0 - V((p+rho)/sqrt(beta)) |
< (2/14.88) [71.001 + 0.079(795.021)]
< 17.985.                                            (12)
```

Finally, with `a=p+1`, `b=q+1`,

```text
d_(p,q) = ab(a+b)/2,
Q(p+rho) = 3 C2(p,q) + 3,
```

and therefore

```text
beta^(-3/2) d_(p,q) exp[-3 C2/beta]
 = V((p+rho)/sqrt(beta)) exp(3/beta).                (13)
```

Using `exp(u)-1<=u+u^2/[2(1-u)]` at `u=3/128`, the correction in (13),
multiplied by `beta`, is below `0.24` for `beta >= 128`.  Combining (12) and
(13) gives `<18.225/beta`, proving the advertised round proof-side constant
`19`.  The exact verifier additionally evaluates the closed expressions at 60
decimal digits and obtains `18.151462 < 19`; that evaluation reproduces the
proof arithmetic but does not choose or certify the constant.

This proves the estimate requested by the Wilson-to-saddle coefficient wall
(historical obligation alias `W85`).  It also
supplies the true multiplier tail: outside any scaled `Q`-ball the exact
multiplier is bounded by the Gaussian-polynomial tail of `V` plus `18/beta`.

## 4. A Common Hilbert Space And Operator-Norm Convergence

Let `h=beta^(-1/2)` and `C=(0,infinity)^2`.  For `p=(p_1,p_2)` define

```text
C_p = (h p_1, h(p_1+1)] x (h p_2, h(p_2+1)],
x_p = h(p+rho),
U_beta e_p = h^(-1) 1_(C_p).
```

Then `U_beta: ell^2(P) -> L^2(C)` is an isometry; the factor is forced because
each cell has area `h^2`.  Define

```text
E_beta = exp[(beta/2)(J-I)],
v_beta(p) = beta^(-3/2)c_p(beta)/c_0(beta),

A_beta = exp(-beta) beta^(-3/2) T_beta
       = E_beta M_(v_beta) E_beta.                   (14)
```

Positive scalar scaling does not change any eigenvalue ratio.  Let
`V_beta^pc` be the step function with value `V(x_p)` on `C_p`, and let

```text
F_beta = U_beta E_beta U_beta^*.
```

Equation (12) gives the genuine common-space estimate

```text
|| U_beta A_beta U_beta^*
   - F_beta M_(V_beta^pc) F_beta ||
< 18/beta.                                           (15)
```

Both `E_beta` factors are contractions, so no tail can amplify this error.

It remains to converge the saddle operator, without claiming that the bare
heat semigroups converge in operator norm.  Let

```text
L = (1/3)(partial_xx - partial_xy + partial_yy)
```

with Dirichlet boundary on `C`, and write `S_t=exp(tL)`.  The ordinary
full-walk Fourier argument, now without a Weyl alternant, gives the
endpoint-uniform local CLT

```text
sup_z | beta q_(beta t)(z)
        - [sqrt(3)/(2 pi t)] exp[-Q(z/sqrt(beta))/t] |
 -> 0                                                (16)
```

for fixed `t>0`.  Applying the six-image formula (1) gives

```text
beta K_(beta t)(p,r) -> s_t^C(x_p,x_r)               (17)
```

uniformly in the endpoints, where `s_t^C` is the finite-reflection Dirichlet
heat kernel of `L`.

Set

```text
B_beta = M_(sqrt(V_beta^pc)) F_beta,
B_infty = M_(sqrt(V)) S_(1/2).
```

These are Hilbert-Schmidt.  Exactly,

```text
||B_beta||_2^2
 = sum_p V(x_p) K_beta(p,p)
 = h^2 sum_p V(x_p) [beta K_beta(p,p)].              (18)
```

By (17), (18) is a Riemann sum for

```text
int_C V(x) s_1^C(x,x) dx = ||B_infty||_2^2.          (19)
```

The domination is explicit: killed return probability is no larger than the
full return probability, `beta q_beta(0)` is uniformly bounded by the Fourier
Gaussian estimate, and

```text
Q(x) - 3(x_1+x_2)^2/4 = (x_1-x_2)^2/4 >= 0.
```

Hence `V` is integrable and the Riemann-sum tails in (18) vanish uniformly.

On compactly supported continuous rank-one kernels, (17) makes `B_beta`
converge weakly in Hilbert-Schmidt space to `B_infty`.  Such kernels are
dense.  Equations (18)-(19) give convergence of the Hilbert-Schmidt norms, so
weak convergence upgrades to

```text
||B_beta-B_infty||_2 -> 0.                           (20)
```

Since

```text
F_beta M_(V_beta^pc)F_beta = B_beta^* B_beta,
T_infty = S_(1/2) M_V S_(1/2) = B_infty^* B_infty,
```

(20) yields trace-norm, hence operator-norm, convergence:

```text
||B_beta^*B_beta-B_infty^*B_infty||_1
 <= (||B_beta||_2+||B_infty||_2)||B_beta-B_infty||_2
 -> 0.                                               (21)
```

Combining (15) and (21) proves the registered common-space scaled operator
remainder.  No finite eigenvector tail and no fitted limiting eigenvalue enter
the argument.

## 5. Spectral Completion On The Whole Half-Line

For every finite `beta>0`:

1. Every `c_lambda(beta)` is strictly positive, because the connected chamber
   graph has a path from the origin to every weight and the exponential series
   has nonnegative coefficients.
2. `E_beta` has strictly positive matrix entries for the same reason.
3. `M_beta^native=diag(c_lambda/c_0)` is trace class.  Character evaluation
   at the identity gives

   ```text
   sum_lambda d_lambda c_lambda(beta) = exp(beta),
   ```

   and `d_lambda>=1`, hence `sum_lambda c_lambda<=exp(beta)`.
4. Therefore `T_beta` is compact, positive semidefinite, and entrywise
   positivity-improving in the character-coefficient cone.

The top eigenvalue is simple.  An elementary proof avoids a cone-typing
ambiguity: replacing a top eigenvector by its coordinatewise absolute value
cannot lower its Rayleigh quotient, and the inequality is strict if the vector
has both signs because every matrix entry is positive.  A second top
eigenvector orthogonal to the positive first one would have both signs, giving
a contradiction.  Thus

```text
lambda_1(T_beta) < lambda_0(T_beta)                  (22)
```

for every `beta>0`.  At `beta=0`, `T_0` is the rank-one projection onto the
trivial weight, so the ratio is zero.

The family is trace-norm continuous on finite beta intervals.  Each
coefficient is a nonnegative power series; on `[0,B]`, coefficient tails are
dominated by their tails at `B`, whose sum is finite by the identity above.
The denominator is positive and continuous, while `exp((beta/2)J)` is norm
continuous because `J` is bounded.  Therefore

```text
g(beta) = lambda_1(T_beta)/lambda_0(T_beta)
```

is continuous on every compact interval and is pointwise below one by (22).

The limit operator in (21) is nonzero, compact, and positive semidefinite.  Its
kernel is

```text
int_C s_(1/2)^C(x,z) V(z) s_(1/2)^C(z,y) dz,
```

which is strictly positive for interior `x,y`.  The same absolute-value
argument gives a simple top eigenvalue `mu_0>mu_1`.  Operator-norm convergence
then gives

```text
g(beta) -> mu_1/mu_0 < 1.                            (23)
```

Choose `B` large enough that (23) is bounded away from one on `[B,infinity)`.
On `[0,B]`, continuity and pointwise strictness make the maximum strictly less
than one.  The larger of those two bounds is `1-delta` for some `delta>0`.
This proves the uniform half-line theorem.

## 6. Falsifiers And Scope Firewalls

The verifier rejects all of the following:

- omitting the Weyl `rho` shift;
- replacing the reflection signs by plus signs;
- deleting one Weyl image;
- replacing the triangular walk by square-lattice covariance;
- using a fixed Taylor/path cutoff as `beta` grows;
- changing the dimension or shifted-Casimir identity;
- treating a finite packet gap as the infinite-operator proof.

Two additional typing failures are fenced in the proof itself:

1. setting the endpoint to `rho` in the generic numerator error is invalid,
   because an `O(beta^(-7/2))` error would swamp the `beta^(-4)` denominator;
   the squared-alternant identity (6) is required;
2. pointwise positivity of a group-convolution kernel is not used.  The native
   packet has a positive coefficient-basis matrix, while the physical
   convolution normalization has the extra `1/d_lambda`.

## 7. Promotion Value Gate

| Gate | Result | Reason |
|---|---|---|
| V1 current verdict-identified obstruction | FAIL | the matching live parent rows currently have no top-level `verdict_rationale`; historical audits name this residual, but do not satisfy the current gate |
| V2 materially new | PASS | prior rungs stopped at determinant cancellation, true tail, and common-space convergence |
| V3 current retained framework primitive essential | FAIL | the theorem is conditional on the native recurrence, whose live authority is currently unaudited; after that operator is supplied, the remaining steps are the displayed finite-reflection, Fourier, and operator-theory derivation |
| V4 substantial theorem/leverage | PASS | replaces finite extrapolation by an all-`beta`, infinite-operator theorem |
| V5 distinct mechanism | PASS | finite Weyl reflection plus endpoint-uniform Fourier `L^1` control replaces Bessel mode-by-mode assembly |

Mathematical result: the branch's exact native-packet target is solved.  The
automatic retained-promotion gate cannot establish V1 or V3 while the matching
parent verdict and recurrence authority are not current.  By explicit user
direction during the audit pause, this artifact enters an audit-pending science
PR rather than being suppressed by audit ordering.  It makes no retained-status
claim: effective obligation retirement and TOE percentage movement are both
zero until later independent audit and dependency-chain integration.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_a2_reflection_uniform_half_line_gap_2026_09_02.py
```

Expected final line:

```text
BREAKDOWN: THEOREM_PASS=21 SUPPORT_PASS=4
TOTAL: PASS=25 FAIL=0
```
