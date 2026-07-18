# Gauge-Vacuum Plaquette Inverse-Coordinate Derivative Packet

**Date:** 2026-04-16
**Type:** bounded_theorem
**Status authority:** independent audit lane only
**Script:** `scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py`

## Load-bearing claim scope

This packet records the finite derivative identity that follows from the
defined inverse coordinate:

- [GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md](./GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md)
  proves the finite analytic/monotone premises and defines
  `beta_eff,L := P_1plaq^(-1) o P_L`; the resulting equality is a coordinate
  identity, not a reduction mechanism;
- [GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md](./GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
  separately supplies the imported first nonlinear coefficient used for an
  onset cross-check; this packet does not promote that source or attribute the
  coefficient to the inverse-coordinate theorem;
- the runner computes the one-plaquette Bessel sum directly inside this
  packet.

No staggered-Dirac realization, `g_bare` normalization, physical Wilson
coupling derivation, bridge-support stack, or beta-6 closed-form plaquette
value is a premise of this bounded theorem.

## Question

After defining the unique finite-volume inverse coordinate

`P_L(beta) = P_1plaq(beta_eff,L(beta))`,

does differentiating its coordinate identity determine the unknown Wilson
plaquette without already solving that response?

## Answer

No. Differentiation yields an exact identity but does not evaluate the unknown
susceptibility.

Differentiating the coordinate identity gives

`beta_eff,L'(beta) = chi_L(beta) / chi_1plaq(beta_eff,L(beta))`

where

- `chi_L(beta) = dP_L/d beta = Var_beta(S_L) / N_plaq`,
- `chi_1plaq(beta) = dP_1plaq/d beta = Var_beta(X)`.

Equivalently,

`P_L(beta) = integral_0^beta chi_L(s) ds`

and therefore

`beta_eff,L(beta) = P_1plaq^(-1)(integral_0^beta chi_L(s) ds)`.

This identity does not determine either susceptibility. The remaining object is

> independently derive the full connected Wilson plaquette susceptibility profile
> `chi_L(beta)` on the finite Wilson evaluation surface.

That would evaluate the coordinate; the derivative identity alone does not.

## Theorem 1: exact susceptibility identities

On a finite periodic Wilson `L^4` surface,

`P_L(beta) = (1/N_plaq) d/d beta log Z_L(beta)`

with

`Z_L(beta) = integral DU exp[beta S_L(U)]`

and

`S_L(U) = sum_p (1/3) Re Tr U_p`.

Differentiating once more gives

`chi_L(beta) = dP_L/d beta = Var_beta(S_L) / N_plaq`.

For the local one-plaquette block,

`P_1plaq(beta) = d/d beta log Z_1plaq(beta)`

with

`Z_1plaq(beta) = integral dU exp[beta X(U)]`

and

`X(U) = (1/3) Re Tr U`,

so

`chi_1plaq(beta) = dP_1plaq/d beta = Var_beta(X)`.

Because both observables are nonconstant and the densities are strictly
positive for finite `beta`, both susceptibilities are strictly positive on the
finite Wilson evaluation surface.

## Theorem 2: derivative identity for the defined `beta_eff,L`

The inverse-coordinate identity, true by definition,

`P_L(beta) = P_1plaq(beta_eff,L(beta))`

may now be differentiated exactly:

`chi_L(beta) = chi_1plaq(beta_eff,L(beta)) * beta_eff,L'(beta)`.

Therefore

`beta_eff,L'(beta) = chi_L(beta) / chi_1plaq(beta_eff,L(beta))`.

This is an exact derivative formula for the defined coordinate on every finite
periodic Wilson evaluation surface. It is not an independently derived
transport mechanism.

## Corollary 1: exact integral representation

Since `P_L(0) = 0`,

`P_L(beta) = integral_0^beta chi_L(s) ds`.

Substituting into the exact inverse relation yields

`beta_eff,L(beta) = P_1plaq^(-1)(integral_0^beta chi_L(s) ds)`.

Thus evaluating the coordinate requires the same full connected plaquette
susceptibility profile; the inverse-coordinate notation does not solve it.

## Imported onset cross-check

If the separately cited mixed-cumulant onset output is supplied,

`P_L(beta) - P_1plaq(beta) = beta^5 / 472392 + O(beta^6)`.

Differentiating gives the exact first nonlocal susceptibility correction:

`chi_L(beta) - chi_1plaq(beta) = 5 beta^4 / 472392 + O(beta^5)`.

Equivalently, from

`beta_eff,L(beta) = beta + beta^5 / 26244 + O(beta^6)`,

one gets

`beta_eff,L'(beta) = 1 + 5 beta^4 / 26244 + O(beta^5)`.

Using the exact common slope

`chi_1plaq(0) = chi_L(0) = 1/18`,

the first transport correction is

`chi_1plaq(0) * (beta_eff,L'(beta) - 1) = 5 beta^4 / 472392 + O(beta^5)`,

matching the differentiated mixed-cumulant theorem exactly.

## What this establishes

- the derivative and integral identities for the defined inverse coordinate;
- an algebraic cross-check of a separately imported onset coefficient;
- the boundary that the full susceptibility profile remains independent input
  to any explicit evaluation.

## What this does not close

- an explicit closed form for `chi_L(beta)` on the finite Wilson surface
- an explicit closed form for `beta_eff,L(beta)`
- analytic closure of `P(6)`
- repo-wide repinning of the canonical plaquette
- an independently specified reduction law or physical transport mechanism

## Source boundary

The inverse coordinate is exact as a definition and its derivative formula is
exact calculus. Neither statement characterizes the Wilson response at a
physical coupling. The imported mixed-cumulant coefficient remains sourced by
its own row, and no canonical plaquette or canonical inverse-coordinate value
is evidence in this packet.

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_susceptibility_flow_theorem.py
```

Expected summary:

- `THEOREM PASS=1 SUPPORT=5 FAIL=0`
