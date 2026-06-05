# KS Eta Versus Jordan-Wigner String CAR Locality No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Runner:** `scripts/ks_eta_vs_jw_string_car_locality.py`

This note tests a narrow algebraic route: whether matter-attachment locality
plus the Kogut-Susskind staggered construction forces cross-site CAR
anticommutation. The answer is no. The staggered `eta_mu(x)` signs are
Dirac/taste c-number link coefficients. The Jordan-Wigner string is the
operator-valued statistics object. They are orthogonal.

The framework baseline is
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md): Lattice supplies
`Z^3`, Quantum supplies the one-qubit local algebra, and Record is irrelevant to
this statistics question. The tested route does not add a new primitive,
statistics rule, or owner-approved admission.

## Result

On a `2 x 2 x 2` `Z^3` qubit patch, the runner builds the same staggered
hopping coefficients in two realizations:

- hard-core boson ladders `b_x = sigma_+^(x)`, which are single-site,
  nilpotent, single-occupancy operators and commute across sites;
- Jordan-Wigner dressed operators `c_x = S_x sigma_+^(x)`, which satisfy CAR
  because of the string `S_x = product_{y < x} sigma_3^(y)`.

Both realizations carry the same Kogut-Susskind `eta_mu(x)` link signs. The
decisive counterfactuals are:

```text
keep eta, drop the string  -> CAR fails
drop eta, keep the string  -> CAR holds
```

So the staggered eta signs neither supply nor are needed for CAR. Locality also
does not supply the string: the maximally local ladder has no string, while any
Jordan-Wigner order on the patch has a nearest-neighbor link with a nontrivial
tail.

## Scope

This is not a no-go against fermions on `Z^3`. The Jordan-Wigner frame exists.
The claim is only that the tested locality-plus-KS route does not force it over
the hard-core-boson frame. A future graded-locality rule, fermion-parity
superselection principle, or lattice-native statistics derivation remains open
and would need explicit owner approval or an independent derivation.

## No-Go Discipline Gate

This gate applies only to the route above: deriving cross-site CAR from the
staggered eta signs plus locality.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Eta-as-statistics | Treat `eta_mu(x)` as the CAR sign. | Counterfactuals show CAR rides the string, not eta. |
| Locality-generates-string | Require matter operators to be local and infer the string. | The single-site hard-core boson is more local and is not CAR. |
| Single-valuedness | Use single-valued fields to select the graded frame. | Both hard-core boson and Jordan-Wigner frames are single-valued. |
| Per-site nilpotency | Upgrade `b_x^2=0` to cross-site anticommutation. | The hard-core boson has nilpotency without cross-site CAR. |
| Same-algebra route | Use the shared ungraded matrix algebra to claim CAR is forced. | Same ungraded algebra means the graded frame is not selected. |
| Order-choice route | Choose a total order that removes all strings on nearest-neighbor links. | The patch bandwidth check leaves a nontrivial tail. |
| Graded-locality route | Add fermion-parity superselection. | This is a real external selector, not a consequence of KS eta signs. |

### N2 - Wall Independence

The collapsed wall is the graded statistics selector. Eta signs supply
Dirac/taste structure; a separate string or graded-locality principle supplies
statistics.

### N3 - Hidden-Wall Scan

"Locality" means support on the tested lattice sites. "Eta" means a c-number
coefficient in the hopping term. No graded locality, superselection rule, or
total-order selection is hidden in those words.

### N4 - Residual Matching

The residual is cross-site CAR selection. It is not the per-site nilpotency
residual, the staggered Dirac/taste residual, or the existence of a compatible
fermion representation.

### N5 - Rhetoric Audit

The negative statement is route-local. It does not say CAR is impossible, only
that KS eta plus locality does not force it.

### N6 - Partial-Closure Path Scan

An owner-approved graded-locality primitive, a fermion-parity superselection
admission, or a lattice-native statistics theorem could close the residual.
This note leaves those paths open.

### N7 - Steelman

A hostile reviewer can argue that physical locality should be graded locality
rather than ungraded tensor locality. That would supply CAR directly, but it is
an added statistics rule; it is not derived from the eta coefficients.

### N8 - Cross-Cycle Echo

Other carrier notes separate the one-qubit state space from the cross-site
statistics frame. This note adds the Kogut-Susskind eta-specific test of that
split.

**Gate result:** pass for the narrow eta-versus-string route only.

## Validation

The runner checks 23 exact finite-matrix facts:

- eta signs are c-number Kawamoto-Smit phases;
- hard-core boson and Jordan-Wigner hopping use the same eta coefficients;
- hard-core boson ladders are nilpotent and local but not CAR;
- Jordan-Wigner dressing gives CAR;
- eta and the string pass the two counterfactual tests above;
- on a three-site subpatch, both frames generate the same ungraded matrix
  algebra;
- the patch order has a nontrivial nearest-neighbor string tail.
