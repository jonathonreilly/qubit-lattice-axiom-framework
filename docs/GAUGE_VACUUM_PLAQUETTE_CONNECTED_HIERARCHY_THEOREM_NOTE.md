# Gauge-Vacuum Plaquette Finite Connected-Hierarchy Projection Theorem

**Date:** 2026-04-16
**Type:** positive_theorem
**Status:** source-note positive finite-volume theorem for the common-source
connected-cumulant hierarchy, its shell-summed projections, and the derivative
identities for the defined Wilson plaquette inverse coordinate; audit and
effective status remain pipeline-owned
**Primary runner:**
[`scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py`](../scripts/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.py)
**Cache:**
[`logs/runner-cache/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_connected_hierarchy_theorem.txt)

## Claim scope

On a finite periodic Wilson evaluation surface, the common plaquette coupling
is a uniform source shift. This gives an exact connected-cumulant derivative
hierarchy. Its first shell-summed projections are the plaquette susceptibility
and its derivative, and the defined-coordinate derivative identities use those
projections successively.

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

## Corollary 2: derivative identities for the defined `beta_eff`

For the defined finite inverse coordinate

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

Thus repeated differentiation of the coordinate identity expresses successive
coordinate derivatives through the corresponding shell-summed hierarchy
projections. The first derivative uses the shell-summed two-point projection,
the second uses the shell-summed three-point projection, and higher derivatives
consume successive shell sums. These are coordinate identities, not a Wilson
reduction mechanism or an evaluation of any shell sum.

## Source boundary

The defined finite inverse coordinate and its first derivative identity are
supplied by the
[`Finite-Volume Wilson Plaquette Inverse-Coordinate Theorem`](GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md)
and the
[`Gauge-Vacuum Plaquette Susceptibility-Flow Finite Packet`](GAUGE_VACUUM_PLAQUETTE_SUSCEPTIBILITY_FLOW_THEOREM_NOTE.md),
respectively.

The composed plaquette equality and its differentiated forms are coordinate
identities, not an independently derived reduction mechanism. The connected
cumulant and shell-summed projection mathematics in this note is supplied by
its own source algebra. No higher-onset coefficient is imported or promoted.

No new axiom, admission, primitive, carrier, convention, imported value, fit,
or physical-observable identification is introduced here. The frozen Lattice,
Qubit, Admissibility, and Record axioms are unchanged and are not used to
enlarge this finite Wilson theorem.

## What this closes

- the exact finite Wilson common-source identity;
- the exact connected-cumulant derivative hierarchy;
- the first shell-summed two- and three-point projections;
- the exact first- and second-derivative identities for the defined `beta_eff`;
- the limited statement that these coordinate identities consume successive
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

- `THEOREM PASS=2 SUPPORT=2 FAIL=0`
