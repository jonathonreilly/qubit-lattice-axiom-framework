# Gauge-Vacuum Plaquette Finite Connected-Hierarchy Projection Theorem

**Date:** 2026-04-16
**Type:** positive_theorem
**Status:** source-note positive finite-volume theorem for the common-source
connected-cumulant hierarchy, its shell-summed projections, and the exact
derivative transport route for the Wilson plaquette reduction law; audit and
effective status remain pipeline-owned
**Primary runner:**
[`scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py`](../scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py)
**Cache:**
[`logs/runner-cache/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.txt)

## Claim scope

On a finite periodic Wilson evaluation surface, the common plaquette coupling
is a uniform source shift. This gives an exact connected-cumulant derivative
hierarchy. Its first shell-summed projections are the plaquette susceptibility
and its derivative, and the exact `beta_eff` transport equations use those
projections successively.

The onset input

`P_L(beta) - P_1plaq(beta) = beta^5 / 472392 + O(beta^6)`

then fixes the complete full-versus-one-plaquette three-point relation

`sum_(r,s) C_3(p_0,r,s;beta)
 = chi_1plaq'(beta) + 5 beta^3 / 118098 + O(beta^4)`.

This is a positive projection theorem. A direct explicit formula for `P_L` or
`beta_eff` may determine the shell-summed projections without separately
resolving every position-dependent cumulant.

## Setup

Let

`X_p(U) = (1/3) Re Tr U_p`

and introduce independent plaquette sources on a finite Wilson surface:

`Z_L[J;beta]
 = integral DU exp[beta sum_p X_p(U) + sum_p J_p X_p(U)]`,

`W_L[J;beta] = log Z_L[J;beta]`.

The connected `n`-point plaquette cumulants are

`C_n(p_1,...,p_n;beta)
 = d_(J_p1) ... d_(J_pn) W_L[J;beta] |_(J=0)`.

Fix a plaquette `p_0` on the symmetric finite surface and write

`P_L(beta) = C_1(p_0;beta)`.

## Theorem 1: finite Wilson common-source shift

Set

`y_p = beta + J_p`.

The exponent in `Z_L[J;beta]` is `sum_p y_p X_p(U)`, so for a finite plaquette
set there is a function `W_tilde_L` such that

`W_L[J;beta] = W_tilde_L({beta + J_p}_p)`.

The ordinary multivariable chain rule therefore gives the exact operator
identity

`d/d beta = sum_r d/d y_r = sum_r d/d J_r`.

No volume limit or perturbative expansion is used.

## Corollary 1: connected-cumulant hierarchy

Finite source derivatives commute. Applying the common-source identity after
`n` source derivatives gives

`d/d beta C_n(p_1,...,p_n;beta)
 = sum_r C_(n+1)(p_1,...,p_n,r;beta)`.

The first shell-summed projections are consequently

- `P_L(beta) = C_1(p_0;beta)`;
- `chi_L(beta) = P_L'(beta) = sum_r C_2(p_0,r;beta)`;
- `chi_L'(beta) = P_L''(beta)
   = sum_(r,s) C_3(p_0,r,s;beta)`.

These equations identify scalar shell sums. They do not assert separate
closure of every position-resolved member of `C_2`, `C_3`, or the higher
hierarchy.

## Corollary 2: positive derivative transport route for `beta_eff`

On the exact finite reduction map

`P_L(beta) = P_1plaq(beta_eff(beta))`,

write `chi_1plaq = P_1plaq'`. One differentiation gives

`beta_eff'(beta)
 = [sum_r C_2(p_0,r;beta)]
   / chi_1plaq(beta_eff(beta))`.

Differentiating again gives

`beta_eff''(beta)
 = [sum_(r,s) C_3(p_0,r,s;beta)]
   / chi_1plaq(beta_eff(beta))
   - [chi_1plaq'(beta_eff(beta))
      / chi_1plaq(beta_eff(beta))]
     * (beta_eff'(beta))^2`.

Thus this transport/Taylor route determines successive derivatives through the
corresponding shell-summed hierarchy projections: the first derivative uses
the shell-summed two-point projection, the second uses the shell-summed
three-point projection, and repeated differentiation consumes successive
shell sums. Other exact representations of `P_L` or `beta_eff` lie outside
this route statement.

## Corollary 3: corrected three-point onset

The supplied onset theorem gives

`P_L(beta) - P_1plaq(beta)
 = beta^5 / 472392 + O(beta^6)`.

Twice differentiating yields

`P_L''(beta) - P_1plaq''(beta)
 = 20 beta^3 / 472392 + O(beta^4)
 = 5 beta^3 / 118098 + O(beta^4)`.

Since

`P_L''(beta) = sum_(r,s) C_3(p_0,r,s;beta)`

and

`P_1plaq''(beta) = chi_1plaq'(beta)`,

the exact onset statement is

`sum_(r,s) C_3(p_0,r,s;beta)
 = chi_1plaq'(beta) + 5 beta^3 / 118098 + O(beta^4)`.

Equivalently,

`sum_(r,s) C_3(p_0,r,s;beta) - chi_1plaq'(beta)
 = 5 beta^3 / 118098 + O(beta^4)`.

The same coefficient follows independently from the reduction-map onset.
For a generic analytic local series

`P_1plaq(x) = c_1 x + c_2 x^2 + c_3 x^3 + ...`,

with `c_1 = chi_1plaq(0) = 1/18`, compose it with

`beta_eff(beta) = beta + beta^5 / 26244 + O(beta^6)`.

Only the linear local coefficient can contribute to the order-`beta^5`
difference:

`P_1plaq(beta_eff(beta)) - P_1plaq(beta)
 = [chi_1plaq(0) / 26244] beta^5 + O(beta^6)`.

After two derivatives, the order-`beta^3` coefficient is therefore

`20 chi_1plaq(0) / 26244
 = 20 / (18 * 26244)
 = 5 / 118098`,

independent of every higher coefficient `c_2,c_3,...`. The local
`chi_1plaq'(beta)` term is the baseline in the full three-point sum.

## Source boundary

The two exact onset inputs used above are supplied by the
[`Gauge-Vacuum Plaquette Mixed-Cumulant Audit and First Nonlinear Coefficient`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
packet. The implicit finite reduction map and its first derivative transport
are supplied by the
[`Gauge-Vacuum Plaquette Reduction Existence and Uniqueness Theorem`](GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md)
and the
[`Gauge-Vacuum Plaquette Susceptibility-Flow Finite Packet`](GAUGE_VACUUM_PLAQUETTE_SUSCEPTIBILITY_FLOW_THEOREM_NOTE.md),
respectively.

No new axiom, admission, primitive, carrier, convention, imported value, fit,
or physical-observable identification is introduced here. The frozen Lattice,
Qubit, Admissibility, and Record axioms are unchanged and are not used to
enlarge this finite Wilson theorem.

## What this closes

- the exact finite Wilson common-source identity;
- the exact connected-cumulant derivative hierarchy;
- the first shell-summed two- and three-point projections;
- the exact first- and second-derivative `beta_eff` transport formulas;
- the corrected full-versus-one-plaquette three-point onset relation;
- the limited statement that this derivative route consumes successive
  shell-summed hierarchy projections.

## Outside this claim

- an explicit nonperturbative formula for `P_L(beta)` or `beta_eff(beta)`;
- a position-resolved solution for every member of the connected hierarchy;
- restrictions on other exact representations outside the displayed route;
- analytic evaluation of the framework-point plaquette.

## Command

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py
```

Expected summary:

- `THEOREM PASS=6 SUPPORT=4 FAIL=0`
