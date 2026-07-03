# Gauge-Vacuum Plaquette Source-Sector Reference Perron Solve

**Date:** 2026-04-30; bounded reference-solve boundary repair 2026-05-24;
one-plaquette/admissibility cleanup 2026-06-08; self-contained Schur
finite-volume subcheck repair 2026-06-08
**Type:** bounded_theorem
**Status:** support — explicit source-sector Perron solves at two
structural reference choices of the residual environment, plus a bounded no-go
for three enumerated local-input closure families for `rho_(p,q)(6)`, plus a
self-contained finite all-forward `L_s=2` Schur shortcut diagnostic.
The runner does NOT compute the physical
`rho_(p,q)(6)` for the actual 3D spatial Wilson environment; that 3D
Perron solve is the missing object.
**Claim boundary:** finite `NMAX = 7`, `MODE_MAX = 200` reference solves with
`rho` supplied as input (`rho = 1` and `rho = delta`), plus finite parametric
rho-sensitivity/no-go evidence inside the enumerated families, plus the finite
all-forward `L_s=2` PBC Schur shortcut computed directly by the runner. This
note does not claim the physical 3D spatial Wilson environment `rho`, the
untruncated tensor-transfer Perron solve, the thermodynamic-limit plaquette, or
canonical `P(6) = 0.5934`.
**Status authority:** independent audit lane only.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py`

## Question

Within the finite bounded packet audited here, the residual `beta = 6`
reference problem is represented by the source-sector operator

`T_src(6) = exp(3 J) D_6^loc C_(Z_6^env) exp(3 J)`

with three explicitly separated pieces:

- the explicit half-slice multiplier `exp(3 J)` for the source operator
  `J = (chi_(1,0) + chi_(0,1)) / 6`,
- the explicit local Wilson marked-link factor
  `D_6^loc chi_(p,q) = a_(p,q)(6)^4 chi_(p,q)`,
- the residual spatial-environment convolution
  `C_(Z_6^env) chi_(p,q) = rho_(p,q)(6) chi_(p,q)`.

For the bounded reference solves, the first two are explicitly computable from
`c_lambda(6)` (Bessel
determinant mode sum) and `SU(3)` intertwiners alone. The third is the
input diagonal `rho`. In the physical target problem, that third factor would
be the boundary character measure of the unmarked 3D spatial Wilson
environment with marked-plaquette boundary holonomy held fixed, but this note
does not compute or identify that physical measure.

Two questions:

1. Do the enumerated local-input families determine a unique
   `rho_(p,q)(6)` from the same local inputs?
2. Independently of (1), can the resulting Perron data — `P(6)`,
   `u_0 = P^(1/4)`, `alpha_s(v) = alpha_bare / u_0^2` — be computed as
   definite numbers from the local input class on at least some
   well-defined choices of the residual environment?

## Answer

(1) **No inside the enumerated families.** The local Wilson character
coefficients `c_lambda(6)` and the `SU(3)` intertwiner data, together
with the one-parameter families tested below, do not determine a unique
`rho_(p,q)(6)`. This is the bounded no-go in Theorem 3 below.

(2) **Yes for two structural reference choices,** as Theorems 1 and 2
below: `rho = 1` (Dirac-delta environment) and
`rho = delta_{(p,q),(0,0)}` (decoupled environment) each give a
fully explicit Perron solve.

The physical residual environment remains the missing object. It would
require the Perron eigenvector of the positive tensor-transfer operator
on the 3D unmarked spatial Wilson environment with one marked-plaquette
boundary, a non-perturbative `SU(3)` lattice gauge problem outside this
bounded reference-solve packet.

## Important caveat: rho is INPUT in the reference solves, not OUTPUT

In Theorems 1 and 2 the rho values (`rho = 1` and
`rho = delta_{(p,q),(0,0)}`) are the structural input that *defines*
each reference solve. They are not derived from any physical 3D Wilson
environment computation. What the runner computes from `c_lambda(6)`
and `SU(3)` intertwiners is the resulting Perron eigenvector and its
expectation value of `J`, *given* that input choice.

This note does not claim that either reference solve corresponds to the
physical 3D environment. It claims only that the Perron *machinery* is
explicit and gives definite numbers when fed an explicit rho.

The two reference choices are also NOT endpoints of the admissible rho
class. Admissible rho is unbounded above on non-trivial irreps: for
example, the one-plaquette environment ansatz at `beta_env = 6` already
gives `rho_(1,0) = 1.27 > 1`. The choices `rho = 1` and
`rho = delta` are simply natural structural reference points: the
maximally concentrated and the minimally concentrated environment in
the dominant-weight character basis.

## Setup

The finite bounded support packet already on `main` supplies the
following scoped inputs:

- the source-sector matrix-element factorization note
  [GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](./GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)
  supplies the source-sector matrix-element formula used here;
- the local/environment factorization note
  [GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md](./GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md)
  supplies the finite local Wilson coefficient packet used here;
- the residual-environment identification note
  [GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_IDENTIFICATION_THEOREM_NOTE.md](./GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_IDENTIFICATION_THEOREM_NOTE.md)
  names the remaining source-sector factor after stripping the local
  marked-link factor;
- the spatial-environment character-measure note
  [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md](./GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md)
  supplies the finite-box notation for a diagonal character-measure
  factor with eigenvalues `rho_(p,q)(beta)` and
  `rho_(0,0)(beta) = 1`;
- the spatial-environment structural transfer note
  [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md](./GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md)
  supplies a bounded transfer-operator carrier packet for that boundary
  class-function problem;
- the spatial-environment tensor-transfer note
  [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](./GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  supplies a finite tensor-transfer packet built from
  `c_lambda(beta)` and `SU(3)` intertwiners.

Thus the finite source-sector reference operator audited here is

`T_src(6) = exp(3 J) D_6^loc C_(Z_6^env) exp(3 J)`,

with the first two factors fully explicit and the third supplied as one
positive diagonal sequence `rho_(p,q)(6)`. The physical 3D spatial Wilson
environment sequence remains outside the bounded claim.

## Theorem 1: explicit reference Perron solve A (input rho = 1)

**Reference choice.** Set `rho_(p,q)(6) = 1` for every irrep,
equivalently `R_6^env = I` (identity on the marked class-function
sector). This corresponds to the structural choice
`Z_6^env(W) = sum d_(p,q) chi_(p,q)(W) = delta(W, e)`, i.e., the
spatial environment is treated as if it concentrates the marked
plaquette holonomy at the identity. This is a structural input, not a
derived value.

**Construction from local Wilson data.** With this rho choice, the
source-sector operator reduces to

`T_src,loc(6) = exp(3 J) D_6^loc exp(3 J)`,

where the only non-trivial pieces are:

- `J chi_(p,q) = (1/6)(chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
                       + chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q))`
  (the explicit `SU(3)` six-neighbor source recurrence);
- `a_(p,q)(beta) = sum_(n in Z) det[I_(n + lambda_j + i - j)(beta/3)]_(i,j=1)^3
                    / (d_(p,q) c_(0,0)(beta))`,
  `lambda = (p+q, q, 0)`,
  `d_(p,q) = (p+1)(q+1)(p+q+2)/2`.

Both are constructed entirely from `c_lambda(6)` (via the Bessel-
determinant mode sum) and `SU(3)` intertwiner data (via the dominant-
weight recurrence).

**Computed Perron data.** At `NMAX = 7` and `MODE_MAX = 200` the
runner reports:

- Perron eigenvalue: `3.812630482037`,
- `P_loc(6) = <psi_loc, J psi_loc> = 0.4524071590`,
- `u_0,loc = P_loc^(1/4) = 0.8201293744`,
- `alpha_s,loc(v) = alpha_bare / u_0,loc^2 = 1.4867408201`
  (for `alpha_bare = 1`).

## Theorem 2: explicit reference Perron solve B (input rho = delta)

**Reference choice.** Set
`rho_(p,q)(6) = delta_{(p,q),(0,0)}`, equivalently
`R_6^env = P_(0,0)` (projection onto `chi_(0,0)`). This corresponds
to `Z_6^env(W) = const`, i.e., a decoupled environment that does not
see the marked plaquette holonomy. This is again structural input.

**Computed Perron data.** The source-sector operator
`T_src,triv(6) = exp(3 J) D_6^loc P_(0,0) exp(3 J)` is rank-one with
image span `exp(3 J) chi_(0,0)`. The runner reports:

- Perron eigenvalue: `3.441440354984`,
- `P_triv(6) = 0.4225317396`,
- `u_0,triv = 0.8062409160`,
- `alpha_s,triv(v) = 1.5384037545`.

## Theorem 3: bounded no-go for enumerated `rho_(p,q)(6)` closures

Consider three explicit one-parameter families inside the admissible
class of residual data:

1. **Decay family.** `rho_(p,q)(6) = exp(-tau (p+q))` for `tau >= 0`.
   At `tau = 0`, recovers the Theorem 1 reference; as
   `tau -> infinity`, recovers the Theorem 2 reference.
2. **One-plaquette environment family.**
   `rho_(p,q)^(beta_env) = c_(p,q)(beta_env) / c_(0,0)(beta_env)` for
   `beta_env >= 0`. This gives a normalized nonnegative character-measure
   sequence; it is strictly positive for `beta_env > 0`, while the
   endpoint `beta_env = 0` degenerates to `rho = delta_{(p,q),(0,0)}`.
3. **Tube-power family.**
   `rho_k = (c_(p,q)(6) / c_(0,0)(6))^k` for integer `k >= 0`. At
   `k = 0`, recovers Theorem 1; as `k` grows, the rho values grow
   sharply for low `(p,q)` and decay for high `(p,q)`.

Each family uses only `c_lambda` and `SU(3)` intertwiners, plus a
single exogenous parameter `(tau, beta_env, k)`. The sampled sequences are
normalized, nonnegative, and conjugation-symmetric; strict positivity is
reserved for nondegenerate interior samples, not the `beta_env = 0` or
`rho = delta` endpoints. None of the nondegenerate sampled families is
canonically selected by the local data alone.

The runner reports the following Perron-value spreads:

- family 1 spread: `0.0297` over `tau in [0, 5]` (range `[0.4225, 0.4524]`);
- family 2 spread: `0.0653` over `beta_env in [0, 20]` (range
  `[0.4225, 0.4878]`);
- family 3 spread: `0.1638` over `k in [0, 20]` (range `[0.4524, 0.6163]`);
- combined spread: `>= 0.1937`.

In particular, distinct normalized rho choices, all built from the same
`c_lambda(6)` and `SU(3)` intertwiner data, produce strictly different
values of `P(6)`. **Therefore the tested 1-parameter local closures do
not fix a unique `rho_(p,q)(6)`.**

The canonical same-surface plaquette value `0.5934` lies inside the
combined admissible span (reached for example near `k = 12` in family
3), but no parameter choice within these 1-parameter families is
canonically picked out by the local input class. The runner does not
select a parameter to match `0.5934`; instead it sweeps the parameter
and reports the resulting `P(6)` sequence as evidence of non-uniqueness.

### Scope clarification (added 2026-05-04)

**Important narrowing.** The argument above explicitly enumerates THREE
specific 1-parameter families and shows none of them is canonically
picked out by `c_lambda(6)` + `SU(3)` intertwiners. The correct
conclusion that follows logically is:

> **No 1-parameter local family closes `rho_(p,q)(6)`.**

The original phrasing "Closed-form derivation of `rho_(p,q)(6)` from
those local inputs alone does not exist" is broader than what the
argument actually proves. It would also rule out **0-parameter
derivations** (derivations with no free parameter to fit), which the
3-family argument does NOT rule out.

In particular, the **Schur cube finite-volume calculation** is a
0-parameter calculation that uses `c_lambda(6)`, `SU(3)` intertwiners,
AND the explicit cube graph geometry. The present runner now computes this
finite calculation directly, rather than importing its value from a sibling
row. In the raw Bessel-coefficient convention of this note it computes:

```text
rho_Schur_(p,q)(6)
  = ((d_(p,q) c_(p,q)(6) / c_(0,0)(6))^N_plaq)
    × d_(p,q)^(N_components - N_links)
```

with `N_components` from the cyclic-index graph of the cube. For the `L_s=2`
PBC cube under the all-forward convention the runner reconstructs
`N_plaq = 12`, `N_links = 24`, `N_components = 8`, so after normalization this
is equivalently

```text
rho_Schur_(p,q)(6)
  = (c_(p,q)(6) / c_(0,0)(6))^12 d_(p,q)^(-4).
```

The self-contained runner subcheck gives
`rho_Schur_(1,0) = 0.212462403803`,
`rho_Schur_(1,1) = 0.005587932035`, and
`P_Schur,L2(6) = 0.429104996947`. The sibling
`SU3_CUBE_INDEX_GRAPH_SHORTCUT_OPEN_GATE_NOTE_2026-05-03.md` is now only
parallel context for the narrow shortcut no-go; it is not a load-bearing source
of this note's Schur value.

**Schur's `rho_Schur` is not in any of the 3 enumerated families** (it
has both `c/c_00` factors and `d^(...)` factors; the 3 families have
only one or the other). So Theorem 3's scope is **narrower** than its
title suggests.

**Updated honest scope of Theorem 3:**

- `rho_(p,q)(6)` is NOT fixed by any 1-parameter family of the 3 forms
  enumerated.
- `rho_(p,q)(6)` IS computed for the tested all-forward L_s=2 cube
  surface by this runner's Schur finite-volume calculation using cube graph
  topology in addition to `c_lambda` and intertwiners.
- The Schur calculation gives a SPECIFIC value (P = 0.4291 at L_s=2
  PBC cube), which does NOT match the canonical MC value 0.5934. This
  is a finite-volume candidate value, not a free parameter.
- For matching MC 0.5934 via L_s=2 cube: requires either an additional
  approved input or derivation beyond local data + cube geometry, OR a
  realization that the L_s=2 cube prediction is genuinely 0.4291 and
  the MC 0.5934 reflects finite-volume / thermodynamic-limit effects.
- For L_s ≥ 3 cube: the Schur derivation has not been done in this
  framework; this is a candidate for matching MC only if larger-L cubes
  give different rho and that larger-L computation is supplied.

The corrected no-go is therefore: `c_lambda(6)` + `SU(3)` intertwiners
+ any one of the three enumerated 1-parameter family choices does not
canonically determine rho.
Adding cube graph geometry gives a SPECIFIC all-forward L_s=2 finite-volume
rho but not the MC/thermodynamic value.

### No-go discipline gate for the enumerated local-family boundary

Status: PASS for the narrow boundary only: the three enumerated 1-parameter
local families do not canonically determine `rho_(p,q)(6)`.

**N1 alternative route enumeration.**

| Route | Attempt | Result |
|---|---|---|
| Constant reference | Use `rho = 1` as the canonical local closure. | ATTEMPTED: the runner computes a finite reference value, but this is an input choice, not selected by the local data. |
| Delta reference | Use `rho = delta_{(p,q),(0,0)}` as the canonical local closure. | ATTEMPTED: the runner computes a distinct finite reference value, again as an input choice. |
| Decay family | Let `rho = exp(-tau(p+q))` and hope the local data select `tau`. | ATTEMPTED: the sweep varies with `tau`; no canonical `tau` is selected. |
| One-plaquette environment family | Let `rho = c_(p,q)(beta_env)/c_(0,0)(beta_env)` and hope the local data select `beta_env`. | ATTEMPTED: the sweep varies with `beta_env`; no canonical `beta_env` is selected. |
| Tube-power family | Let `rho = (c_(p,q)(6)/c_(0,0)(6))^k` and hope the local data select `k`. | ATTEMPTED: the sweep varies with `k`; matching a comparator near one `k` is not a derivation of `k`. |
| Cube-graph Schur route | Add explicit all-forward `L_s=2` cube graph topology. | ATTEMPTED AS OUT-OF-SCOPE ROUTE: the runner now computes a definite finite value, but it is not one of the three local families and does not close the physical 3D/thermodynamic environment. |

**N2 wall independence.** The collapsed wall set is one finite-source-sector
wall: the enumerated local families do not supply a canonical parameter. The
physical 3D spatial Wilson environment, larger-`L_s` Schur cubes, and
thermodynamic-limit interpretation are open residuals, not walls claimed closed
here.

**N3 hidden-wall scan.** The finite runner uses `beta = 6`, the source-sector
operator, `MODE_MAX = 200`, `NMAX = 7`, and the all-forward `L_s=2` graph
definition as explicit finite inputs. The canonical `P(6) = 0.5934` value is a
comparator only. No axiom, approved primitive, Record readout rule, physical
3D environment, or thermodynamic limit is smuggled into the finite result.

**N4 residual matching.** The sibling Schur shortcut row is no longer used as
the source of the finite Schur value; it is parallel context only. The runner
computes the `L_s=2` graph counts, Schur rho, and Perron value directly.

**N5 rhetoric audit.** Phrases such as "does not close rho" mean only that the
three enumerated 1-parameter local families fail to canonically determine the
finite source-sector rho. They do not rule out 0-parameter cube-graph routes,
larger finite volumes, physical 3D Wilson-environment solves, or
thermodynamic-limit derivations.

**N6 partial-closure path scan.** The `L_s=2` Schur calculation is the live
partial-closure path and is now incorporated as a self-contained finite
subcheck. It partially improves the row by removing an imported value; it does
not retire the physical 3D/thermodynamic residual.

**N7 steelman.** A hostile reviewer can reasonably say that the right rho may
come from the uncomputed spatial Wilson environment, from larger-`L_s`
cube-graph Schur calculations, or from a separate boundary character-measure
derivation. This note accepts that steelman and therefore keeps the no-go
limited to the enumerated local families.

**N8 cross-cycle echo.** Earlier wording in this row was already narrowed from
"closed-form derivation does not exist" to the finite enumerated-family
boundary. This repair follows that pattern: internalize the finite Schur
subcheck, preserve the useful obstruction, and leave the broader physical
environment route open.

### 2026-06-08 repair: Schur shortcut no longer imported

The previous scope-clarification paragraph cited the `L_s=2` Schur shortcut
value from a sibling SU(3) row whose own note language still carried an
open-gate caveat. That made this row conditional even though the needed
calculation is finite and small. The primary runner now performs the complete
subcheck:

- enumerates the 12 all-forward `L_s=2` PBC plaquettes and 24 directed links;
- builds the 48-node cyclic-index graph and verifies 48 identifications with 8
  connected components;
- computes the raw-coefficient Schur rho formula above from the same
  `c_(p,q)(6)` Bessel determinants used elsewhere in this note;
- runs the source-sector Perron solve with that rho and verifies
  `P_Schur,L2(6) = 0.429104996947`.

This repair does not promote the shortcut to the physical answer. It only
removes the imported-value dependency for the finite `L_s=2` diagnostic and
keeps the actual 3D Wilson environment as the missing mathematical object.

## Theorem 4: NMAX truncation tail bound

The Wilson character coefficients on the dominant-weight box decay
super-polynomially with the rep size at fixed `beta`. The runner
verifies this empirically:

- successive truncation drifts decay geometrically:
  `|P(NMAX=7) - P(NMAX=6)| = 1.142e-9`,
  `|P(NMAX=6) - P(NMAX=5)| = 1.139e-7`,
  ratio of successive prior drifts `≈ 69`;
- the dominant-weight band sum at the truncation edge is below
  `1.0e-10`: `max_(p+q=NMAX) a_(p,q)(6)^4 = 2.54e-16`.

This is consistent with the Bessel-determinant structure of
`c_(p,q)(beta)` at fixed `beta`: the highest-weight triple
`(p+q, q, 0)` appears in the determinant index, and `I_n(beta/3)`
decays super-polynomially in `n` at fixed `beta`. The Peter-Weyl
character expansion of any positive central function on `SU(3)`
inherits this decay through the convolution structure, so finite-NMAX
truncation introduces an error that is super-polynomially small in
NMAX.

The runner reports a converged value at NMAX = 7 with truncation
residual `< 1e-9` inside the branch-local tolerance, and reports
the geometric drift ratio explicitly so a reviewer can independently
verify the super-polynomial decay claim.

`MODE_MAX` convergence is even faster: the runner reports
`|P(MODE_MAX=200) - P(MODE_MAX=160)| = 0` to working precision, again
consistent with the rapid decay of `I_n(2)` in `n`.

## 2026-06-08 cleanup: one-plaquette diagnostic and endpoint language

The runner's one-plaquette reference diagnostic is now explicitly the
Haar one-plaquette partition coefficient check

```text
P_1plaq(beta) = d/d beta log c_(0,0)(beta),
```

where `c_(0,0)` is computed by the same Bessel-determinant mode sum as the
local Wilson coefficients. It no longer differentiates a truncated
identity-evaluation sum over `d_lambda c_lambda`; that sum is not the
one-plaquette partition function and is not used in this scoped Perron solve.

The admissibility language is also tightened: the sampled rho families are
normalized nonnegative sequences, with strict positivity only for
nondegenerate interior samples. The structural `rho = delta` reference and
the `beta_env = 0` one-plaquette endpoint intentionally have zero
nontrivial coefficients and are described as degenerate normalized endpoints,
not strictly positive interior measures.

## Corollary 1: the missing mathematical object

The remaining object outside this bounded reference-solve packet is one
specific non-perturbative quantity:

> the boundary character measure `Z_6^env(W)` of the unmarked 3D
> spatial Wilson environment with the marked plaquette holonomy `W`
> held fixed,
> equivalently the Perron eigenvector of the explicit positive
> tensor-transfer operator built from `c_lambda(6)` and `SU(3)`
> intertwiners on a 3D `SU(3)` lattice gauge network with one
> marked-plaquette boundary.

The local Wilson character coefficients and `SU(3)` intertwiners
furnish only the local building blocks of that 3D tensor network. The
network's dominant-eigenvector solve is the missing input.

## Hostile-review section

This subsection records the explicit checks the runner performs to
guard against the four hostile-review failure modes flagged for this
PR (see `feedback_hostile_review_semantics.md`,
`feedback_consistency_vs_derivation_below_w2.md`, and
`feedback_retained_tier_purity_and_package_wiring.md`).

### Not a constant-lift ansatz

The Wilson character coefficients `a_(p,q)(6)` span the audited box
with extreme rep-dependence:

- `a_(0,0) = 1.000000`,
- `a_(1,0) = a_(0,1) = 0.422532`,
- `a_(1,1) = 0.162260`,
- `a_(2,2) = 5.84e-7` (in audited box),
- spread `max(a)/min(a) ≈ 7.32e9`.

A constant-lift effective coupling would produce
`a_(1,1) = a_(1,0)^2`. The actual ratio is
`a_(1,1) / a_(1,0)^2 = 0.9089`, not `1`. The runner explicitly checks
this and the constant-lift hypothesis is rejected.

The exact constant-lift obstruction theorem
[`GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md`](./GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md)
already on `main` rules out constant-lift altogether at the
strong-coupling slope level. The present note is consistent with that
obstruction and does not depend on it.

### No tuning, comparator isolated

The runner contains exactly one occurrence of the canonical
same-surface plaquette numeric, in a single named constant
`CANONICAL_COMPARATOR = 0.5934`. That constant is consumed only by the
hostile-review diagnostics that verify *neither* reference solve
matches it:

- `|P_loc - CANONICAL_COMPARATOR| = 0.1410`,
- `|P_triv - CANONICAL_COMPARATOR| = 0.1709`.

It is not used as input, initialization, or fit target anywhere in the
Perron solve, the parametric sweeps, or the convergence study. The
parametric sensitivity sweeps explicitly demonstrate that DIFFERENT
normalized rho choices produce DIFFERENT `P(6)`; the runner does not
select a particular rho to match the comparator. Specifically, family
3 reaches `0.5888` at `k = 12` and overshoots to `0.6163` at `k = 20`,
illustrating that no `k` value is canonically picked out.

### Not a renamed residual operator

The explicit local Wilson marked-link factor `D_6^loc` (eigenvalues
`a_(p,q)(6)^4`) and the trivial-projection `P_(0,0)` are operator-
distinct: `max|D_loc - P_(0,0)| = 0.0319`. They produce different
Perron values: `|P_loc - P_triv| = 0.0299`.

The residual environment operator `C_(Z_6^env)` is not a renaming of
`D_6^loc`. The local/environment factorization theorem cleanly
isolates `D_6^loc` as the trivial-channel-normalized mixed-kernel
local factor (finite one-link Wilson convolution to the fourth power),
while `C_(Z_6^env)` is the residual unmarked spatial environment
convolution after that local factor has already been stripped off. The
two operators play structurally different roles and produce different
Perron data when toggled.

### Truncation tail bounded, not extrapolated

The runner does not extrapolate the NMAX truncation. It reports
explicit truncation drift values and the dominant-weight band sum at
the truncation edge, both of which are super-polynomially small (see
Theorem 4). The reported `P_loc(6)` and `P_triv(6)` numbers are the
finite-NMAX values at `NMAX = 7`; the truncation residual is bounded
by the geometric drift sequence, with reported geometric ratio `≈ 69`
between successive drifts. This note makes no branch-local claim about
the strict infinite-NMAX limit beyond what the geometric decay supports.

### rho is INPUT in the reference solves, not OUTPUT

The two reference Perron solves use *chosen* rho values
(`rho = 1` and `rho = delta`) as structural input. The runner
computes the resulting Perron eigenvector and its expectation of `J`
from `c_lambda(6)` and `SU(3)` intertwiners. It does NOT claim that
either rho choice is derived from any physical 3D environment, and
the note explicitly disavows that interpretation.

The "computed `rho_(p,q)(6)`" reported by the runner is therefore the
INPUT definition of each reference solve, plus the explicit Perron
eigenvector content (which IS computed from local Wilson data). The
no-go in Theorem 3 makes this distinction explicit: the physical
`rho_(p,q)(6)` is not supplied by the enumerated local-input closures.

### Status purity

The note's `Status:` line is `support`. It does **not** claim
retained or promoted tier; it does **not** propagate retained status
through the audit ledger. The two reference Perron solves supply
explicit Perron data on a defined structural choice of the residual
environment, not the full residual operator. The ledger row is
correctly seeded as `unaudited` and queued for fresh-context audit.
The `Type:` line is bounded because the audited surface is finite and rho is
supplied as input.

## What this closes

- explicit reference-solve A Perron solve at `beta = 6` from
  `c_lambda(6)` and `SU(3)` intertwiners alone (with input choice
  `rho = 1`), with super-polynomial NMAX/MODE_MAX truncation tail
  bound
- explicit reference-solve B Perron solve at `beta = 6` from the same
  local inputs (with input choice `rho = delta_{(p,q),(0,0)}`)
- explicit reported Perron eigenvector content, `P(6)`, `u_0`, and
  `alpha_s(v)` numerical values for both reference solves
- bounded no-go (Theorem 3) that `c_lambda(6)` and `SU(3)`
  intertwiners, within three enumerated admissible parametric families,
  do not fix a unique `rho_(p,q)(6)` on the source sector
- self-contained finite all-forward `L_s=2` Schur shortcut subcheck:
  graph counts `12/24/48/48/8`, raw-coefficient Schur rho, and
  `P_Schur,L2(6) = 0.429104996947`
- scoped identification of the still-missing physical object as the 3D
  spatial Wilson Perron eigenvector, equivalent to the boundary
  character measure of the unmarked spatial environment with
  marked-plaquette boundary
- explicit hostile-review checks on constant-lift, tuning, renaming,
  truncation extrapolation, and one-plaquette partition-diagnostic concerns

## What this does not close

- explicit physical `rho_(p,q)(6)` for the actual 3D spatial Wilson
  environment
- analytic closure of canonical `P(6) = 0.5934`
- repo-wide repinning of the canonical plaquette
- full-volume tensor-transfer Perron solve in 3D

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py
```

Expected summary:

- `THEOREM PASS=9 SUPPORT=4 FAIL=0`
