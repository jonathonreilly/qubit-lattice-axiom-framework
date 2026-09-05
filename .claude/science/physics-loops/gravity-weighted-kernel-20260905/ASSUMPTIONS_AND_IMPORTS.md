# Assumptions and imports — block 213

## A_min and approved primitives
Lattice, Qubit, Admissibility, Record (docs/MINIMAL_AXIOMS_2026-06-29.md, epochs
2026-08-05 and 2026-08-13 in force). Approved primitives per
docs/audit/data/axiom_premise_nodes.json: scale_reference (units only),
kinetic_isotropy (structural OS0 c_t = c_s only), realized_state (pointwise
specialization only). Registry check (PRIMITIVE_REGISTRY_CHECK.md) is run
before any wall statement in this pack.

## Supplied objects the block inherits from its chain (not derived here)
- The Block-201 covariant rule identification: the lane kernel as the
  spin-diagonalised shadow of one site-independent Clifford rule; the cell
  geometry as that rule's unique covariant form up to one located sign.
- The Block-211 six-face-compatible moduli family and its PD classification.
- The bench conventions: periodic (4,4) and (4,2,2) tori, the landed staggered
  grading, exact roots of unity.
All are unlanded-in-review chain content (PRs #7745, #7752): this block stacks
on them and re-establishes inside its own runner every identity it uses
(self-containment rule, conformance spec section 1).

## Counterfactual pass (implicit choices, each with the direction it opens)
1. Periodic benches at even extents — the odd-direction wrap structure (R5's
   (4,2,2)) is a required edge case; anti-periodic seams would change the
   symbol's allowed k-set, not its form.
2. Plane-wave diagonalization assumes translation covariance of K(moduli) —
   the per-offset moduli are translation-invariant by construction; if the
   curved cell breaks covariance the symbol is a matrix-valued symbol over the
   period-2 cell (handle explicitly).
3. "The cell metric g(moduli)" — the identification of the cell form's
   quadratic data with a metric is the P2d/Schur law (the plane restriction of
   the covariance object IS marginalization); if the symbol's principal part
   is NOT the inverse of that object, the discrepancy is the finding.
4. Shear entering the symbol — see GOAL planning constraint (#7970 tension).
5. Float-free exactness — every reported identity is exact rational or
   symbolic; floats appear only as displays.

## Forbidden imports
Observed values, fitted selectors, continuum limits presented as lattice facts,
any new axiom/primitive, literature dispersion formulas as proof inputs.
