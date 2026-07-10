---
claim_id: gauge_vacuum_plaquette_residual_environment_geometry_dependence_no_go_note_2026-07-10
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Residual Wilson Environment Geometry-Dependence No-Go

**Date:** 2026-07-10
**Type:** no_go
**Status:** exact negative boundary for a geometry-free residual environment
coefficient sequence; source-side proposal only.
**Runner:**
`scripts/frontier_gauge_vacuum_plaquette_environment_geometry_dependence_no_go_2026_07_10.py`
**Output:**
`outputs/frontier_gauge_vacuum_plaquette_environment_geometry_dependence_no_go_2026_07_10.txt`

## Claim-status fields

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "this exact obstruction sharpens the target but does not compute the geometry-indexed beta=6 environment"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target and result

The finite Wilson surface follows the explicit one-clock construction in
[`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md).
The parent residual-environment note asks for one sequence
`rho_(p,q)(6)` after stripping marked and local factors. Its Wilson transfer
parent, however, is `T_(L_s,beta)`: the unmarked environment changes between
the two tested finite spatial sizes. A boundary condition is also part of the
definition of each finite measure, but fixed-`L_s` boundary-condition
dependence is not claimed here.

This note proves an exact obstruction to suppressing `L_s` across the two
tested PBC sizes. For the
standard periodic spatial Wilson complex with one marked plaquette removed
from the environment action, the fundamental environment coefficient has
different first allowed strong-coupling orders:

```text
L_s = 2 PBC:  rho_(1,0)^(env,L_s)(beta) = C_2 beta^3 + O(beta^4),
L_s = 3 PBC:  rho_(1,0)^(env,L_s)(beta) = O(beta^5),
```

with `C_2 > 0`. Therefore no single geometry-free analytic
function `rho_(1,0)^env(beta)` is the actual unmarked Wilson environment for
both accepted finite transfer surfaces. The residual must at least carry
`L_s`. Because the boundary condition must be named to specify a finite
measure, we write the fully specified object as

```text
R_(L_s,beta,BC)^env,
rho_(p,q)^(env,L_s,BC)(beta).
```

This does not say that a geometry-indexed coefficient cannot be computed. It
prunes only the route that treats the single-link packet or one finite cube
packet as a universal environment across the two tested PBC sizes. It does
not establish fixed-`L_s` boundary-condition dependence.

## Exact environment coefficient before compression

Let `Lambda_(L_s,BC)` be a finite oriented spatial Wilson complex, `m` a
marked plaquette, and `U_m` its holonomy. Remove only the marked plaquette
Boltzmann factor and define

```text
dnu_(L_s,beta,BC)(U)
  = Z_env^(-1) exp[(beta/3) sum_(p != m) Re tr U_p]
    product_(links e) dU_e.
```

The pushforward of this measure by `U -> U_m` is central. Its normalized
convolution eigenvalue is exactly

```text
rho_lambda^(env,L_s,BC)(beta)
  = (1/d_lambda) int chi_lambda(U_m)^* dnu_(L_s,beta,BC)(U).       (1)
```

Equation (1) is an actual unmarked-DOF Wilson integral. It contains no
positive diagonal witness and no identification of a single-link Wilson
coefficient with the multi-link environment. Disintegration of the finite
product Haar measure over the marked-holonomy map gives the equivalent
boundary-class-function form.

Equation (1) is not yet the full source-sector stripping theorem: the parent
local-factor note still leaves open whether the temporal mixed kernel reduces
to exactly the advertised four marked-link factors. This note therefore does
not claim that inserting (1) into the current source-sector package closes
that separate mixed-kernel bridge.

## Triality filling theorem

Expand the numerator of (1) at `beta=0`. Every active plaquette insertion is

```text
Re tr U_p = (chi_(1,0)(U_p) + chi_(0,1)(U_p))/2.
```

At each integrated link, invariance under the local center transformation
`U_e -> omega U_e`, `omega^3=1`, forces total incident triality zero. If `A`
is the oriented link-plaquette incidence matrix and `b_m` is the marked
boundary column, an order-`n` monomial can contribute to the fundamental
coefficient only if a signed active plaquette chain `x` satisfies

```text
A x = -b_m  (mod 3),        ||x||_0 <= n.                         (2)
```

Thus the minimum signed-support weight solving (2) is an exact lower bound on
the first nonzero Taylor order. Repetition cannot lower it: two equal
fundamental insertions on one plaquette are triality-equivalent to one
antifundamental insertion at smaller order, while opposite insertions cancel.

The runner exhausts signed supports through weight two for `L_s=2` and through
weight four for `L_s=3`, using an exact meet-in-the-middle syndrome search. It
finds none. It also enumerates the order-three `L_s=2` solutions and finds the
oriented periodic-plane complement is unique.

The lower bounds are attained over the integers:

- at `L_s=2`, the three other plaquettes in the periodic `2 x 2` marked plane
  form an oriented sheet whose boundary is minus the marked boundary;
- at `L_s=3`, the other five faces of one elementary cube form an oriented
  cap whose boundary is minus the marked boundary.

In each attaining surface every used link occurs once in each orientation.
Successive one-link identity

```text
int_SU(3) U_(ij) conjugate(U_(kl)) dU = delta_(ik) delta_(jl) / 3
```

therefore reduces the selected closed fundamental sheet to a strictly
positive finite contraction. At `L_s=2` this is the unique order-three
monomial, so its positive contribution cannot cancel and `C_2 > 0`. At
`L_s=3` the explicit cube cap proves that order five is allowed; no
no-cancellation assertion at that order is needed for the geometry mismatch.
The explicit coefficient values are not needed.

## Forbidden imports

The proof and runner do not use:

- an observed plaquette or Monte Carlo target value;
- a fitted selector or fitted `rho`;
- a generic positive witness;
- the normalized single-link Wilson coefficient packet as environment data;
- the L_s=2 all-forward candidate-rho ansatz;
- the L_s=3 link-orbit-tied diagnostic quotient.

## Exact scope

This result closes only the `L_s`-suppressed route across the two tested PBC
sizes:

> one residual environment sequence with suppressed `L_s` cannot be the actual
> environment on both standard `L_s=2` PBC and `L_s=3` PBC transfer surfaces.

Stating `BC` in the fully specified notation is definition hygiene, not a
separate no-go claim about fixed-`L_s` boundary-condition dependence.

It does not close:

- `rho_(p,q)^(env,L_s,BC)(6)` for any selected geometry;
- the temporal marked/non-marked mixed-kernel compression theorem;
- the thermodynamic or large-`L_s` limit;
- the full source-sector Perron data or the numerical plaquette.

## No-Go Discipline Gate

The negative is restricted to suppression of `L_s` across the two tested PBC
sizes. Boundary-condition naming is definition hygiene only. The result passes
the N1--N8 review gate summarized here:

- six distinct counter-routes were tested, including fixed-geometry,
  normalization, single-link, thermodynamic, APBC, and temporal-stripping
  routes;
- the exact negative has one collapsed wall, while geometry selection and
  temporal stripping are independent positive repair conditions;
- no hidden physical selector or observation is used;
- the new incidence runner matches the finite-geometry residual exactly;
- the rhetoric is limited to two named finite PBC blocks;
- fixed-geometry, APBC, controlled-limit, and temporal-compression paths stay
  open;
- the strongest steelman (the parent intended one implicit fixed geometry) is
  accepted and defines the scope boundary;
- earlier cube-encoder overclaims are handled by the same geometry-naming
  repair rather than generalized into a global no-go.

Gate outcome: `PASS` for the narrow geometry-free no-go only.

## Verification

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_environment_geometry_dependence_no_go_2026_07_10.py
```

Expected summary:

```text
SUMMARY: PASS=11 FAIL=0
```
