# CAR From Transfer Positivity Neutrality No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Runner:** `scripts/car_from_positivity.py`

This note tests a narrow route: whether finite transfer-operator positivity,
reflection-style Gram positivity in the tested two-slice toy surface, or the
Stone readout from `T = exp(-tau H)` selects cross-site CAR over the hard-core
boson frame. It does not. In the tested finite hopping models, positivity sees
the transfer operator and its spectrum, while the statistics sign lives in the
Jordan-Wigner generator frame or in a closed-loop boundary datum.

The framework baseline is
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md): Lattice supplies
the lattice carrier, Quantum supplies the one-qubit local algebra, and Record is
irrelevant to this statistics question. This note does not add a statistics
primitive, graded-locality rule, or owner-approved superselection principle.

## Result

The runner compares hard-core-boson ladders and Jordan-Wigner dressed ladders on
finite qubit tensor products.

On the open `L = 4` chain, the number-conserving nearest-neighbor hopping
Hamiltonians are identical matrices in the tested basis:

```text
||H_hard_core_boson - H_Jordan_Wigner|| = 0
```

Consequently `T = exp(-tau H)` is the same positive transfer operator in both
frames, and the Stone generator readout has the same spectrum. Transfer
positivity therefore has no frame difference to detect on that local open-chain
surface.

The statistics sign is still real. The runner verifies that no inner
`*`-automorphism sends the commuting hard-core-boson generator pair to the CAR
generator pair. It also verifies that a bare two-point value can sign-flip across
frames, while the parity-even density correlator agrees. On a closed ring the
wrap-around Jordan-Wigner string changes the spectrum, so the sign is a genuine
closed-loop datum. But both ring Hamiltonians remain Hermitian and bounded below,
so both produce positive transfer operators. The loop distinguishes two
statistics choices; positivity alone does not rank them.

## Scope

This is not a no-go against fermions on the lattice. It is not a full theorem
about every possible reflection-positive Euclidean measure. It only closes the
tested route: finite transfer positivity, the associated Stone spectrum, and the
simple reflected Gram witness do not force CAR over the hard-core boson frame.

A future graded-locality theorem, fermion-parity superselection principle, or
continuum spin-statistics derivation remains open. Such a selector would be new
science or an owner-approved admission, not a consequence of the positivity
checks here.

## No-Go Discipline Gate

This gate applies only to the route above: deriving cross-site CAR from the
tested finite transfer-positivity and Stone-readout structures.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Open-chain transfer positivity | Select the frame whose `T = exp(-tau H)` is positive. | The open-chain Hamiltonians are identical matrices, so `T` is identical and positive in both frames. |
| Stone spectrum route | Read the statistics from the reconstructed generator spectrum. | The tested generators have identical spectra; the spectral readout is blind to the frame sign. |
| Reflected Gram route | Use a two-slice reflected Gram matrix to separate the frames. | The tested half-space Gram witness has the same positivity verdict in both frames. |
| Bare correlator route | Treat a sign-flipping one-particle correlator as the positivity witness. | The sign flip is not a transfer-positivity certificate; the parity-even density correlator agrees. |
| Closed-loop positivity route | Use the ring, where the sign is physical, to select one frame by positivity. | Ring spectra differ, but both ring Hamiltonians remain bounded and give positive transfer operators. |
| Inner-gauge erasure | Dissolve the distinction by a unitary change of generators. | The intertwiner space is zero-dimensional; the generator-level distinction is real. |

### N2 - Wall Independence

The collapsed wall is a single selector wall: finite transfer positivity does not
supply graded locality or fermion-parity superselection. The open-chain, Stone,
Gram, correlator, and ring checks are probes of that same wall, not independent
premises.

### N3 - Hidden-Wall Scan

"Positivity" means the finite transfer operator and the explicitly constructed
Gram witness in the runner. "Statistics" means the cross-site commutation versus
CAR generator relation. No graded-locality rule, superselection principle, or
continuum spin-statistics theorem is hidden in those words.

### N4 - Residual Matching

The residual is cross-site statistics selection. It is not the existence of
fermion representations, the equality of ungraded matrix algebras, or the
closed-loop spectral split. The runner leaves those facts visible so the
negative statement does not overrun its route.

### N5 - Rhetoric Audit

"Neutral" means neutral for the tested positivity route. It does not mean the
two frames are the same theory, that the sign is unphysical, or that no future
principle can select CAR.

### N6 - Partial-Closure Path Scan

Two live closure paths remain: an owner-approved or derived graded-locality /
fermion-parity principle on closed loops, and a continuum spin-statistics route.
The ring ground-state split is a concrete witness for either future selector.

### N7 - Steelman

A hostile reviewer can argue that a full reflection-positive fermion measure is
not exhausted by this finite transfer-operator check and might include boundary
or graded-locality data that selects CAR. That objection is correct against any
global positivity no-go. It does not break this route-local result, because the
runner only claims neutrality for the finite transfer objects it constructs.

### N8 - Cross-Cycle Echo

Adjacent statistics notes separate local one-qubit structure from cross-site
statistics selection. This note adds the positivity-route witness: positivity is
compatible with both frames on the tested surfaces, while closed-loop statistics
remains a real target for future selection work.

**Gate result:** pass for the finite transfer-positivity route only.

## Validation

The runner checks exact finite-matrix facts:

- hard-core-boson ladders commute cross-site, while Jordan-Wigner ladders satisfy
  CAR;
- both generator sets span the same ungraded full matrix algebra;
- the parity operator built from number operators is shared by both frames;
- the tested two-slice reflected Gram witness has the same positivity verdict in
  both frames;
- no inner `*`-automorphism maps the commuting generator pair to the CAR
  generator pair;
- the open-chain hopping Hamiltonians are identical matrices, so the transfer
  operator is identical and positive in both frames;
- bare two-point values can sign-flip while the parity-even density correlator
  agrees;
- ring spectra differ, but both ring transfer operators remain positive.
