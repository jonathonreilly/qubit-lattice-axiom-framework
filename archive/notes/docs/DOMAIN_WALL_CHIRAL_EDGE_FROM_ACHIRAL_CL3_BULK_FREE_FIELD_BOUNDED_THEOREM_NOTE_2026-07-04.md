# Domain-Wall Chiral Edge from Achiral Cl(3,0) Bulk: Free-Field Bounded Theorem

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim scope:** a finite free-field linear-algebra diagnostic. The native
spatial operator built from the one-site `Cl(3,0)` Pauli generators is
Nielsen-Ninomiya doubled; direct Wilson lifting breaks chiral
anticommutation; an explicitly imposed record-time mass domain wall in the
higher-dimensional Wilson-Dirac diagnostic localizes one chiral Weyl species
on the wall and the opposite species on the anti-wall. This is evidence that
the record-time domain-wall route is live at free-field level. It is not a
gauge-coupled, interacting, or dynamical-origin theorem, and it does not derive
the higher-dimensional regulator from the framework axioms.
**Status authority:** independent audit lane only. This note does not set,
predict, or request an audit status.
**Primary runner:** [`scripts/domain_wall_chiral_edge_from_achiral_cl3_bulk_2026_07_04.py`](../scripts/domain_wall_chiral_edge_from_achiral_cl3_bulk_2026_07_04.py)
**Runner cache:** [`logs/runner-cache/domain_wall_chiral_edge_from_achiral_cl3_bulk_2026_07_04.txt`](../logs/runner-cache/domain_wall_chiral_edge_from_achiral_cl3_bulk_2026_07_04.txt)
**Framework authority:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

## Statement

Use the current axiom surface as the spatial input, and make every extra
diagnostic ingredient explicit:

- the physical lattice is the `Z^3` lattice of
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md);
- the one-site algebra is the axiom memo's `M_2(C)`, equivalently the
  `Cl(3,0)` Pauli presentation with generators `sigma_1, sigma_2, sigma_3`;
- the admissibility Qualification in the same memo says a law may not depend
  on an unfixed choice unless that choice is supplied by derivation, bridge,
  explicit admission, or approved primitive registration;
- record-time is treated as the extra domain-wall coordinate in this
  free-field diagnostic;
- the four-component chiral embedding and Wilson-Dirac domain-wall regulator
  are diagnostic constructions implemented by the runner, not new axioms,
  primitives, or retained framework imports.

The runner verifies:

1. **Naive doubling is present.** For
   `D(p) = i sum_i sigma_i sin(p_i)`, the zero set on the Brillouin
   torus is exactly `p_i in {0, pi}`. The eight Weyl-node winding signs
   are four positive and four negative, so the net chirality is zero.
2. **Direct Wilson lifting is chiral-breaking.** In the four-component
   chiral embedding with `Gamma_i = tau_1 tensor sigma_i` and
   `gamma_5 = tau_3 tensor I`, the massless operator anticommutes with
   `gamma_5`. Adding `W(p)=r sum_i(1-cos p_i)` lifts seven corners but
   gives a nonzero `{gamma_5, D+W}`. This is the direct Wilson-lifting
   contrast computed in this diagnostic.
3. **Record-time domain wall localizes a chiral edge species.** The
   finite periodic record-time Hamiltonian is

   ```text
   H(p) =
       sum_i sin(p_i) Gamma_i
       + K_s Gamma_s
       + [m(s) + r sum_i(1-cos p_i) + r_s L_s] Gamma_m,
   ```

   with `Gamma_s = tau_2 tensor I`, `Gamma_m = tau_3 tensor I`,
   `m(s)=+M` on half the record-time circle and `m(s)=-M` on the other
   half. The periodic circle therefore has one wall and one anti-wall.
   The edge chirality measured in the computed light subspace is
   `chi_edge = i Gamma_s Gamma_m`.
4. **Index/count matches the wall structure.** The wall carries one
   two-component Weyl species of one chirality; the anti-wall carries one
   two-component Weyl species of the opposite chirality. The torus net is
   zero, while each wall has a definite local chirality.

The domain-wall Hamiltonian uses the explicit higher-dimensional Wilson-Dirac
regulator implemented in the runner to isolate the single physical
Brillouin-zone corner in the free-field diagnostic. This does not promote a
direct three-dimensional Wilson-removal step to a derived admissible chiral
law; the direct Wilson contrast remains chiral-breaking, and the chiral mode is
localized on a defect in record-time rather than selected by an achiral spatial
bulk law.

## Computed checks

The runner's PASS/FAIL checks are not tautological. They compute:

- the eight naive zeros by scanning the Brillouin grid;
- the Weyl-node chirality signs from the Jacobian
  `det(d sin(p_i)/d p_j) = product_i cos(p_i)`;
- the Wilson anticommutator norm against `gamma_5`;
- the finite record-time wall spectrum by diagonalizing the actual matrix;
- the wall and anti-wall subspaces by diagonalizing localization windows
  inside the computed low eigenspace;
- the exponential localization length from the measured profile;
- the edge chirality expectation value;
- the projected spatial velocity matrices, verifying one `Cl(3,0)` Weyl
  cone on each wall and opposite handedness on the anti-wall;
- the contrast with uniform record-time bulk masses, which remain gapped by
  `|M|` and have no light wall modes;
- the Brillouin-corner contrast, where only the physical `p=0` corner
  carries the light domain-wall species.

With `N_s=64`, `M=0.8`, `r=r_s=1`, the wall and anti-wall one-sided
localization lengths are measured from the eigenvector profiles, and
flipping `M` flips the measured wall chiralities.

## What is shown

At free-field level:

- the achiral `Cl(3,0)` spatial Pauli bulk falls under the
  Nielsen-Ninomiya doubling pattern;
- direct Wilson lifting removes the seven extra Brillouin-corner zeros only
  by breaking chiral anticommutation;
- the record-time domain-wall construction localizes one definite chiral
  Weyl species on the wall and the opposite species on the anti-wall;
- the wall/anti-wall pair has zero net chirality on the periodic circle, but
  each wall carries one local chiral edge species;
- the uniform bulk is gapped, so the light chirality is a wall effect rather
  than a bulk mode.

This is the first concrete free-field evidence in this package that
chiral-from-achiral via record-time domain walls is a live route in the
native `Cl(3,0)`/`Z^3` architecture.

## What is not shown

- No gauge coupling is included.
- No anomaly matching is proven.
- The record-time mass profile is imposed by hand; the runner does not show
  that record-time dynamically supplies the wall.
- The four-component chiral embedding and Wilson-Dirac regulator are not
  derived from the framework axioms.
- The full electroweak chiral structure is not derived.
- Interactions are not included.
- No strong-CP, theta, or Koide consequence is claimed.
- No new framework import, primitive, or axiom is added.
- No audit status is set.

## Validation

Run:

```bash
python3 scripts/domain_wall_chiral_edge_from_achiral_cl3_bulk_2026_07_04.py
```

Expected terminal summary:

```text
TOTAL: PASS=19 FAIL=0
```
