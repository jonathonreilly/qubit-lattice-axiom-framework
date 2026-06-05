# Beta=6 Plaquette Tensor-Network Route: Finite Irrep Support and Recoupling Wall

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Review provenance:** source theorem candidate; post-landing review decides the
ledger grade. This note introduces no axiom, primitive, fitted selector, or
beta=6 plaquette closure.
**Primary runner:** `scripts/frontier_beta6_plaquette_tensor_network_2026_06_04.py`
(SCORECARD PASS=9)

## Scope

This note records a bounded support result for the character-expansion /
tensor-network route to the SU(3) plaquette at `beta=6`.

It establishes three source-level facts:

1. The single-link character coefficients `a_lambda(6)` are computed by
   independent Haar routes that agree on the tested irreps.
2. A finite Casimir-cutoff sample shows strong decay of
   `a_lambda(6)/a_(0,0)(6)`, giving a practical single-link truncation scale.
3. The exactly solvable two-dimensional plaquette value is reproduced by the
   character machinery.

It also records the honest wall: the three-dimensional and four-dimensional
contraction is not the naive delta-link irrep contraction. It requires the
non-abelian link recoupling/intertwiner network, which is the same treewidth
wall already present in the beta=6 environment problem. Related source surfaces:
[PLAQUETTE_C6_DERIVATION_FRAMEWORK_SU3_NARROW_THEOREM_NOTE_2026-05-27.md](PLAQUETTE_C6_DERIVATION_FRAMEWORK_SU3_NARROW_THEOREM_NOTE_2026-05-27.md)
records the remaining SU(3) 6j-symbol contraction, and
[SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md](SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md)
records the four-plaquette link-integration primitive.

## Result

The runner verifies the following bounded facts.

- The singlet coefficient from the add-a-box multiplicity series matches the
  framework `J(beta)` recurrence through the checked order.
- The multiplicity table satisfies
  `sum_lambda m_lambda(P,Q) dim(lambda) = 3^(P+Q)` on the checked boxes.
- The add-a-box singlet multiplicity matches the exact Haar projector trace on
  the checked boxes.
- The Schur-Weyl/Bessel determinant values agree with the multiplicity-series
  values for the tested irreps at `beta=6`.
- Direct Weyl-torus integration agrees with the Bessel determinant to the
  runner tolerance for the tested irreps.
- The finite cutoff sample has a negative fitted slope versus quadratic Casimir,
  with the relative coefficient dropping below `1e-3` at a finite cutoff.
- The two-dimensional plaquette value from the character formula equals
  `d log J / d beta` at `beta=6`.
- The controlled character output reported here is the two-dimensional /
  isolated-plaquette value; no converged `D>=3` plaquette value is claimed.

These facts support the tensor-network route as a viable finite-coefficient
tool, but they do not compute the recoupled `D>=3` network and do not derive the
observed infinite-volume comparator.

## Boundary

This note does not claim:

- a converged three-dimensional or four-dimensional plaquette value;
- a beta=6 closure;
- that finite sampled decay is a proof of all-tail convergence for the
  recoupled network;
- that the naive delta-link contraction is valid outside two dimensions;
- any use of the Monte-Carlo comparator as an input.

The open compute path is a bounded-bond-dimension TRG/HOTRG-style contraction of
the recoupled non-abelian network.

## Wall Discipline Gate

This bounded note is not a no-go result. It states which parts of the
character route are checked and which recoupled computation remains. Status:
PASS for the scoped wall wording below.

- N1 alternative routes: order-in-beta strong-coupling truncation is not used
  as closure at `beta=6`; single-link character coefficients are checked but do
  not contract the `D>=3` network; the exact two-dimensional plaquette check
  validates the machinery but does not lift across recoupled links; the naive
  delta-link contraction is exact only in two dimensions; bounded-bond TRG/HOTRG
  remains the live compute path.
- N2 wall independence: the only named wall here is the `D>=3` non-abelian
  recoupling/treewidth computation. There is no inflated independent-wall set.
- N3 hidden-wall scan: the Monte-Carlo plaquette is comparator-only; SciPy is
  numerical tooling for Bessel values, cross-checked by multiplicity and
  Weyl-torus routes; no lattice axiom, primitive, fitted selector, or beta=6
  closure is consumed.
- N4 residual matching: the residual named here is exactly the recoupled
  `D>=3` tensor-network contraction, not the single-link coefficients, the
  two-dimensional plaquette, or the finite Casimir-cutoff sample.
- N5 rhetoric audit: every negative phrase is scoped to one of three
  resolutions: exact two-dimensional plaquette, single-link coefficient sample,
  or recoupled `D>=3` network. No lattice-wide beta=6 value is denied or
  derived.
- N6 partial-closure path scan: bounded-bond tensor contraction, improved
  contraction ordering, and explicit SU(3) 6j implementation are valid closure
  paths; none is reclassified as a new axiom or primitive.
- N7 steelman: a hostile reviewer could argue that exponential coefficient
  decay plus a good recoupling contractor may already make the tensor route
  numerically practical. This note accepts that route as live and therefore
  avoids an all-routes-negative claim.
- N8 cross-cycle echo: prior plaquette packets already narrowed the remaining
  work to SU(3) Wigner-Racah / treewidth computation. This note follows that
  narrowing and does not turn it into a broader obstruction.

## Imports

The character coefficients are Haar integrals computed by multiplicity,
Bessel-determinant, and Weyl-torus routes. The Monte-Carlo plaquette values are
comparators only; they are not inputs to the calculation.

## Command

```bash
python3 scripts/frontier_beta6_plaquette_tensor_network_2026_06_04.py
```

Expected output: `SCORECARD: PASS=9 FAIL=0`.
