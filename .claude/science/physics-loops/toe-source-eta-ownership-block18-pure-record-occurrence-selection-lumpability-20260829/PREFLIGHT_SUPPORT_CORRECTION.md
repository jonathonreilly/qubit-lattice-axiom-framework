# Preflight Support Correction

Status: frozen after preregistration commit `54f1d5c5e0` and before any
Block18 target runner, result cache, or target mutation was created or
executed.

An additional hostile theorem review returned

```text
REVISE-BEFORE-EXECUTION
```

The core process pair survived, but the review found a small-torus defect and
seven load-bearing scope/construction clarifications. This correction records
them rather than allowing a green runner to test the mistaken scope.

## 1. Periodic seed injectivity

The seed/lumpability rates require `Lambda_L` with `L>=6` and all five
neighbors of `y=c+2f` other than `c+f` blank in both full states. Then the
four rates are

```text
q0(S,y:f)=alpha/6,   q0(C,y:f)=2 alpha/7,
q1(S,y:f)=alpha/6,   q1(C,y:f)=alpha/3.
```

The mandatory wraparound falsifiers are:

| volume | exact failure of the nominal fixture |
|---|---|
| `L=3` | `c-2f=c+f`; `C` has two sites and one-site formation is only `O(t^2)`, while `S` gives `q0=2 alpha/7`, `q1=alpha/3`, and `C` gives `q0=4 alpha/9`, `q1=16 alpha/27` |
| `L=4` | `y=c-2f` is already recorded in `C`, so there is no tested append |
| `L=5` | both `c+f` and `c-2f` neighbor `y`; `p_y(f)=4/9`, `q0=4 alpha/9`, and `q1=16 alpha/27` |

The connected-incidence theorem remains valid for every `L>=3`. A generic
three-distinct-site source has total three already on `L=3`; the displayed
`C_(c,f)` geometry has three distinct sites only for `L>=4` and uses `L>=6`
in the lumpability test.

## 2. Local infinite-volume construction

The phrase “nonexplosive infinite-volume process” is replaced by locally or
cylinder nonexplosive. Infinitely blank initial data produce infinitely many
events globally in every positive time interval. The exact target is:

- an initial deterministic state or Borel law `mu` on the restricted
  seven-state product sector, independent of the proposal/key field;
- a measurable sample map built from finite backward clans at rational local
  queries and extended locally to cadlag paths;
- finitely many relevant Poisson points for each finite spacetime query; and
- fixed-exterior/periodic agreement whenever the shared clan avoids the
  boundary, with disagreement probability tending to zero.

The safe bound remains

```text
P(ancestor radius >= m)
  <= |A| sum_(k>=m) (14 alpha T)^k/k!.
```

It follows from seven predecessor choices, proposal rate `2 alpha`, and the
ordered-time volume `T^k/k!`. It does not imply a global jump chain.

## 3. Covariance versus invariance

Under a space-group element `g`, relabel the exponential keys by
`E'_(g f)(g x,t)=E_f(x,t)` and likewise relabel the proposal and uniform
fields. Apart from the probability-zero tie set, the sample map is
equivariant and

```text
g_* Law_mu = Law_(g_*mu).
```

The evolved law is invariant only if `mu` is invariant. Target tests must
reject fixed-label/tied-key implementations rather than treating covariance
as a distribution-only slogan.

## 4. Restricted-sector scope

“Arbitrary initial law” means arbitrary Borel law on the invariant seven-state
sector. This is logically adequate for the explicitly sector-scoped
underselection witness but is not an executed full-`M_2(C)` occurrence law.
A common full-domain extension is a live technical completion: count exact
`rho_f` neighbors in `m_f`, count every Record in `n_x`, append only supported
`rho_f` marks, and leave arbitrary pre-existing contents permanent. Its
availability is not a new-axiom wall and it is not claimed as executed here.

## 5. Formation as well as permanence

While a site is blank, both hazards obey `lambda_x>=alpha`. Proposals with
uniform key at most `1/2` form a rate-`alpha` baseline, so

```text
P(x remains blank at t) <= exp(-alpha t).
```

Every initially blank site therefore records eventually almost surely, and a
countable intersection gives this for all sites of `Z^3` on one probability-
one event. No common finite completion time is claimed. A zero-on-blank hazard
is a required hostile mutation.

## 6. Record-only dimensionless discriminator

The `t=0` derivative ratio remains a valid scale-free semigroup discriminator,
but the operational witness is strengthened. For

```text
U={x_0,x_6} union N(x_0)
```

let `tau_U` be the first new Record in `U`. Until `tau_U`, the tested hazards
stay `(alpha,alpha)` or `(alpha,2 alpha)`. For every `T>0`, conditional on
`tau_U<=T` and its site lying in `{x_0,x_6}`, the probability that `x_6` wins
is `1/2` or `2/3`. Every other local competitor contributes the same survival
factor to the two numerator densities. This is a local readable-Record order
statistic and is independent of absolute clock calibration.

The symbol `alpha` replaces the draft's `a` to avoid collision with the
registered lattice scale.

## 7. Histories and event arity

Equation (8) is conditional on `R_0`, has `t_0=0`, and is a density relative
to counting measure on sites/marks and Lebesgue measure on the ordered time
simplex. Summing/integrating over `k=0,...,#blanks(R_0)` gives one. Initially
occupied, repeated, illegal, recursively inconsistent, or non-time-ordered
histories have density zero; random initial states are mixed against `mu`.

The one-site `O(t^3)` statement assumes a uniform bound on total rates at the
three target sites. The compound linear coefficient equals `kappa/6` only if
the named jump is the sole direct transition into the cylinder and the local
generator supplies an `O(t^2)` remainder. Otherwise it is the sum of all
direct intensities into the cylinder.

## 8. Lumpability and source scope

The unequal row is decisive only for partitions that identify `R_S,R_C`, map
their `y:f` successors into one distinct common cell, and map no other outgoing
transition from either representative into that cell. A compensating
transition into the target cell must defeat the single-entry test.

For connected periodic cubic graphs over real currents,
`im B_L=1^perp` and `rank B_L=L^3-1`. Positive raw occupancy births are not
source-free divergences. A scalar reservoir debit restores global balance but
is not a local current without an explicit reservoir incidence. The result
therefore constrains only downstream joins that identify raw cumulative
Record occupancy with a conserved density; it is not a gravity no-go.

## Execution gate

The primary and independent workers acknowledged the pause before making any
worktree edit or executing any target. Execution may resume only after this
correction, the corresponding `GOAL.md`/`PREFLIGHT_WITNESSES.md` edits, and a
fresh hostile reread are committed and pushed. Every negative terminal still
requires the post-execution N1--N8 packet and five honest N5 lines.
