# Wick Rotation Compact-Spin(4) to Lorentzian Dirac Doubling: Finite-Algebra Orientation

**Date:** 2026-06-07
**Claim type:** bounded_theorem
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.py`](../scripts/wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.py)
**Cached output:** [`logs/runner-cache/wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.txt`](../logs/runner-cache/wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.txt)

## Scope

This note salvages the finite-dimensional algebra content from the rejected
emergent-time massive-Dirac-doubling overclaim. The salvage is intentionally
narrow:

- it checks that a standard Wick rotation maps compact Euclidean `Spin(4)`
  mixed generators to non-compact Lorentzian boosts;
- it checks that the resulting Lorentzian gamma matrices satisfy signature
  `(+---)`;
- it checks that the `Cl(3,0) -> Cl(3,1)` `e_4` direction is compatible with
  the `C^4` Dirac bispinor doubling and massive on-shell projector.

It does **not** claim that the framework's Record axiom supplies a time axis,
that records or a record count realize `e_4`, that the lattice dynamics performs
this Wick rotation, that positive energy or CAR are delivered, or that the
Koide Sec. 6 residual is closed.

## Relation to existing retained endpoints

This is an orientation between already separated surfaces:

- [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  records the compact Euclidean `SO(4)`/`Spin(4)` endpoint.
- [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md)
  records the finite Clifford-algebra extension `Cl(3,0) -> Cl(3,1)` with
  `e_4^2=-1`.
- [`FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md)
  records bounded support for the Lorentzian free massive Dirac/Poincare
  endpoint.
- [`KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02.md`](KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02.md)
  names the remaining massive partner-chirality/doubling residual.

This note does not connect those endpoints to a framework-native time
realization. It only records that the standard finite algebra is coherent at the
interface.

## Finite-Algebra Statement

Let `gamma^E_1,...,gamma^E_4` be Hermitian Euclidean gamma matrices and

```text
Sigma^E_mn = (1/4)[gamma^E_m,gamma^E_n].
```

Then all `Sigma^E_mn` are anti-Hermitian, so the mixed Euclidean generators
`Sigma^E_4j` exponentiate to unitary compact `Spin(4)` rotations.

Define Lorentzian gamma matrices by

```text
gamma^0 = gamma^E_4,
gamma^j = i gamma^E_j.
```

They satisfy `{gamma^mu,gamma^nu}=2 eta^{mu nu}` with
`eta=diag(+,-,-,-)`. The Wick-rotated boost generators

```text
K_j = (1/4)[gamma^0,gamma^j] = (i/4)[gamma^E_4,gamma^E_j]
```

are Hermitian, their exponentials are non-unitary, and the Lorentzian brackets
have the non-compact sign

```text
[K_i,K_j] = -J_k,      [J_i,J_j] = +J_k
```

in the `1/4[gamma,gamma]` convention. Finally, the Lorentzian `C^4` space has
two chiral sectors, `tr P_+ = tr P_- = 2`, and the massive on-shell projector
`(p_slash+m)/(2m)` is idempotent on `C^4` with nonzero cross-chiral blocks.

## Boundary

This is not an emergent-time theorem. It supplies no readout context, time
metric, record count, record dynamics, sector-generation rule, positive-energy
reconstruction, CAR selection, or interacting-field claim. It is a finite
algebra orientation that says the standard compact-to-Lorentzian Wick map is
compatible with the already-recorded Clifford/Dirac endpoints.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.py
```

Expected result: `SCORECARD PASS=6 FAIL=0`.
