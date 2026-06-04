# Koide Fluctuation Modulus and Chirality: Route-Specific Correction

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (narrow route-specific correction).
**Source boundary:** this note retracts only the reading that the current
determinant-modulus / chirality route already supplies the `(1,1)` Koide
weighting `r = |b|^2/a^2 = 1/2`. The runner verifies that the tested
Hermitian `C_3` circulant modulus is non-holomorphic in `(Re b, Im b)`, has a
rank-2 doublet Hessian, and on the fixed-Frobenius-scale determinant branch has
its tested stationary ratio at `r = 1`, not `r = 1/2`.

This is a correction to the mechanism in
[SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md)
and
[KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md](KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md).
It does not close every holomorphic, chiral, Record, KMS/modular, or
off-circulant route to `r = 1/2`.

**Status authority:** independent audit lane only. This note does not set or
predict an audit outcome.
**Runner:** [scripts/audit_companion_koide_modulus_gives_r_one_chirality_is_phase_only_exact.py](../scripts/audit_companion_koide_modulus_gives_r_one_chirality_is_phase_only_exact.py)
**Runner cache:** [logs/runner-cache/audit_companion_koide_modulus_gives_r_one_chirality_is_phase_only_exact.txt](../logs/runner-cache/audit_companion_koide_modulus_gives_r_one_chirality_is_phase_only_exact.txt)

```yaml
target_claim_type: no_go
proposed_claim_type: no_go
trace_class: correction_and_negative_route_pruning
reachability_to_target: prunes_prior_modulus_chirality_mechanism
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## 1. Tested Statement

Let

```text
M = a I + b C + conjugate(b) C^2,        C^3 = I,
```

with `a` real and `b = Re b + i Im b`. The runner checks:

1. `M` is Hermitian, so the vector-mass determinant is real in the tested
   circulant class.
2. The modulus diagnostic `Tr log(M^dagger M)` depends on both `Re b` and
   `Im b`; the numerical doublet Hessian has rank 2 at the tested point.
3. On the fixed-Frobenius-scale determinant branch used by the prior corner
   determinant companion, the stationary ratio found by the symbolic check is
   `r = 1`, not `r = 1/2`.
4. A phase effect such as an eta-invariant would affect determinant phase /
   `arg(b)` in this framing, not the tested modulus ratio.
5. A rank-1 holomorphic count is a different conditional structure. It is not
   supplied by this determinant-modulus computation.

The result is therefore a route correction: the currently tested modulus route
does not turn chirality into the `(1,1)` magnitude weighting. It sends the
chiral question, if useful, toward a phase/eta-invariant computation rather
than toward a completed magnitude derivation.

## 2. Relation To Landed Notes

The parent open gate correctly identified a conditional algebraic fact:
counting the complex doublet parameter `b` once would give `(1,1)` and
`r = 1/2`, while counting `Re b, Im b` separately gives `(1,2)` and `r = 1`.
This correction says the tested determinant modulus is in the second class.

The Frobenius-Schur companion also remains useful as an algebraic
classification of the real/complex split. What is corrected is the stronger
interpretation that the current chiral/vector or supertrace surface had already
established the holomorphic determinant needed for `r = 1/2`.

The corner determinant companion
[CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
is the closest positive support for the modulus-side correction. This note does
not promote that route into a universal Koide verdict.

## 3. External Literature Boundary

Coleman-Weinberg, chiral determinant, holomorphy, Kähler-Dirac, Koide, Sumino,
and Rivero-Gsponer references are comparator context only. They are not used as
repo proof inputs, and this note imports no PDG values, fitted lepton masses,
or measured Koide comparator.

The repo-owned load-bearing content is the circulant calculation in the runner
and the markdown-linked prior source notes.

## 4. No-Go Discipline Gate

**N1 - Alternative route enumeration.**

| route | result | marker |
|---|---|---|
| Vector / real determinant modulus | Rank-2 doublet Hessian; tested fixed-scale branch gives `r = 1`, not `1/2`. | ATTEMPTED |
| Chiral determinant as modulus selector | Not supplied by the tested Hermitian circulant modulus; chiral information is treated here as phase-directed. | ATTEMPTED, NARROW |
| Holomorphic superpotential-style count | Would be a different conditional input; not derived by the current framework surface. | OUT OF SCOPE / OPEN |
| Staggered/Kähler-Dirac mass/Yukawa realization | Still a gated computation in the parent open-gate notes; this note does not compute it. | OPEN |
| Record/center-state block selector | Could choose `(1,1)` by a non-metric selector; not addressed by the modulus runner. | OPEN |
| KMS/modular or pole-vs-running mechanism | Separate possible selector/protection route; not addressed here. | OPEN |

**N2 - Wall independence.** The modulus rank, holomorphic determinant
condition, finite staggered mass/Yukawa realization, Record/center-state
selector, and KMS/modular selector are independent. Closing the modulus rank
calculation does not close the other routes.

**N3 - Hidden-wall scan.** Phrases such as "chiral", "holomorphic",
"standard QFT", and "superpotential" are not treated as imported authorities.
Where they appear, they mark comparator context or explicitly missing
conditions. The only load-bearing computation is the runner's circulant
modulus/rank/stationary-ratio check.

**N4 - Residual matching.** The residual corrected here is the
`(1,1)`-versus-`(1,2)` magnitude weighting for the current determinant-modulus
route. That matches the parent open-gate residual and the corner determinant
residual. It does not match phase, azimuth, empirical mass, or Record-selector
residuals, so those are not claimed closed.

**N5 - Rhetoric audit.** "Chirality is phase-only" is used only for the tested
modulus framing: the runner shows the Hermitian vector determinant is real and
that the tested modulus is rank 2. It is not a statement that no chiral
construction can ever select magnitude after additional structure is derived.

**N6 - Partial-closure scan.** A future theorem deriving a holomorphic
generation determinant, a Record/center-state selector, an off-circulant
operator deformation, or a KMS/modular selector could still retire the `r = 1/2`
residual without adding a new axiom. Approved axioms and primitives are not
bounded-status sources.

**N7 - Steelman.** A hostile reviewer would say: the open-gate notes never
claimed the plain Hermitian modulus was the holomorphic determinant; they named
a missing conditional. If a future staggered mass/Yukawa construction produces
a Pfaffian, holomorphic supertrace, or center-state record count, this correction
does not touch it. That steelman is accepted, which is why the landed claim is
only a route-specific correction.

**N8 - Cross-cycle echo.** The same block-weight residual appears in the
information-geometry, Frobenius-isotype, and corner-determinant notes. Prior
overbroad "route closed" language has been repaired by narrowing to the exact
tested route and preserving named open selectors; this note follows that
pattern.

**Gate result:** PASS for the narrowed correction only. The determinant-modulus
route does not establish `r = 1/2`; broader selector routes remain open.

## 5. What This Does Not Claim

- It does not derive `Q = 1` as the repo's final charged-lepton prediction.
- It does not prove `Q = 2/3` is impossible.
- It does not close the parent holomorphic open gate after its missing
  conditional is supplied.
- It does not use external literature as proof authority.
- It does not add an axiom, framework primitive, Tier-A admission, or audit
  verdict.

## 6. Trace Gate

```yaml
trace_class: correction_and_reframe
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: prunes_prior_modulus_chirality_mechanism
artifact_role: no_go
next_trace_action: "keep magnitude r=1/2 open for a derived holomorphic determinant, Record/center-state selector, off-circulant deformation, or KMS/modular route; separately test whether eta/chirality can govern arg(b)."
```

## 7. Cross-References

- [Holomorphic supertrace open gate](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md)
  - parent candidate route whose established-mechanism reading is corrected.
- [Frobenius-Schur chiral/vector open gate](KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md)
  - algebraic real/complex split retained as an open condition, not a
  completed selector.
- [Corner determinant route obstruction](CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  - fixed-scale determinant route already pruning `r = 1/2`.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-04.md)
  - Lattice + Quantum + Record baseline; not a bounded import and not a
  selector for the Koide magnitude.
