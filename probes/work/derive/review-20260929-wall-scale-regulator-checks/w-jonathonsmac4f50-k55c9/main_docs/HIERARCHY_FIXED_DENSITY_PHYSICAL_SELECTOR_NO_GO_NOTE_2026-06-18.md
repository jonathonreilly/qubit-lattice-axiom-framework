# Fixed positive quartic equations: restricted non-identification boundary

**Date:** 2026-06-18
**Type:** no_go
**Claim type:** no_go
**Scope:** restricted algebraic non-identification; physical no-go unestablished
**Primary runner:** [finite scalar examples](../scripts/frontier_hierarchy_fixed_density_physical_selector_no_go_2026_06_18.py)

## Exact hypotheses and conclusion

Fix a nonempty finite index set `I` and supplied coefficients `A_i>0`. The only equations
under discussion are `rho=A_i v_i^4`, with `rho>0` and every `v_i>0`.
Do not silently add an unspecified physical dynamics, minimization rule, target,
or authority contract to these equations.

For any **specified numerical** `rho`, the unique solution is
`v_i=(rho/A_i)^(1/4)` for every `i`. This follows by the positive-root argument
in the [conditional coefficient bridge](HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md); positivity and uniqueness
can also be checked from `(y^4-x^4)=(y-x)(y+x)(y^2+x^2)>0` for `0<x<y`.
Therefore it would be false to claim that a supplied numerical `rho` leaves
the absolute scales undetermined.

When only positivity of `rho` is specified, the complete positive solution
family is parameterized by `rho in (0,infinity)`. For any `lambda>0`,
`(rho,v_i) -> (lambda^4 rho, lambda v_i)` preserves the equations and all
ratios `v_i/v_j=(A_j/A_i)^(1/4)`. This is an algebraic scaling freedom under
these hypotheses, not a physical symmetry or impossibility theorem.

A distinguished endpoint tag `s in I`, if introduced, appears in none of the
equations. For the same coefficients, density and solution, every tag is
compatible. If `|I| >= 2`, at least two distinct tags are compatible, so these
equations alone do not determine that tag. If `|I| = 1`, the tag is uniquely
determined by membership in `I`; only the unspecified-density scaling freedom
remains. An actual
physical selector may supply an additional relation, boundary condition or
dynamics. The argument neither refutes such a relation nor establishes its
absence in a wider theory. It does not prune future positive routes.

## Finite examples and their limits

The runner supplies `A2=1/8`, `A4=1/7`, `Ainf=1/(4 sqrt(3))` at `u0=1`.
`Ainf` is the historical variable name for the angular-average coefficient
in the bridge, not an executed infinite lattice. The runner preserves the
nine numerical gates: three coefficient checks, two ratio checks, two scaling
checks at `rho=11`, `lambda=3.7`, and two reference-normalization checks.

Normalizing each endpoint to `v_selected=1` changes `rho` to its corresponding
coefficient. The resulting distinct triples are examples at **different**
densities, not multiple solutions for a single specified numerical density.
The tag argument above is separate and does not rely on that numerical example.
No finite check certifies physical route exhaustion or an absolute EW prediction.

The [parent diagnostic](HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md) has not identified its condensate ratio
with a physical density coefficient. The [formal EW coordinate bridge](HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md)
proves a vector identity under supplied definitions; it does not provide that
physical identification. These are genuine open hypotheses, not negative results.

## No-Go Discipline Gate

The restricted algebraic statement has the proof above. A broader physical
selector no-go is **not established**. This section records limitations rather
than asserting N1-N8 PASS or a completed route-exhaustion packet.

- N1, alternative routes tested: the actual finite examples vary the density
  and reference convention within one supplied scalar-law family. They are not
  five independent physical attack families. A physical no-go packet remains
  incomplete; no artificial additional families are counted.
- N2, wall independence: scaling freedom depends on leaving the numerical
  density unspecified on a nonempty index set; tag freedom additionally needs
  `|I| >= 2` and omission of a tag-selection rule.
  These hypotheses are explicit, not primitive restrictions on future physics.
- N3, hidden-wall scan: positive coefficients/coordinates and the quartic law
  are supplied. A specified density removes scaling freedom. Extra physical
  information can select a tag. No general physical exclusion follows.
- N4, residual matching: the missing coefficient-to-Higgs-density identification
  and absolute physical scale remain open. The proof resolves only what the
  stated equations do and do not determine.
- N5, resolution: the runner uses three scalar coefficients and scalar readouts.
  No element, site, mode, finite matrix or lattice is instantiated. Two finite
  coefficient labels and one supplied angular average are evaluated. There is
  no executed infinite-volume or continuum test.
- N6, rhetoric audit: earlier physical no-go and lattice-wide obstruction
  narration is withdrawn from current applicability, not claimed refuted.
- N7, partial-closure path: a specified density, independently justified physical
  readout, or independent selector relation remains a positive route.
- N8, cross-cycle echo: old cache counts and ledger statuses do not establish
  new source correctness or physical impossibility. Independent source review
  and a fresh bounded capture are pending.

## Recovery and execution

Complete original note/runner/cache bytes are preserved at
`6919e7f72cc95c3df7d6a4e9aa1f43ab6d449dff` and in external recovery inventory
`repair-9849-dimensional-readers/original-identities.json`. No old negative
finding, failure or stronger argument is discarded. The old canonical cache is
not fresh evidence for this revision. Documentary checks below bind scope
statements only; they are not proof or audit verdicts. No observed EW target,
fitted selector or replacement ledger enters the current equations.
