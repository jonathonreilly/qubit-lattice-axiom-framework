# Record-Occupancy Front as a Diagnostic Domain Wall: Free-Field Bounded Theorem

**Date:** 2026-07-05
**Type:** bounded_theorem
**Claim scope:** free-field finite linear algebra for the prior record-time
domain-wall diagnostic, replacing that diagnostic's hand-imposed sign wall by
an explicit monotone record-occupancy front under the stated occupancy-to-mass
map. The map is a motivated model/bridge, not a derivation from full
record-production dynamics. No gauge coupling, interacting anomaly calculation,
Standard Model content, framework import, primitive, new axiom, or audit status
is claimed.
**Status authority:** independent audit lane only. This note does not set,
predict, or request an audit status.
**Primary runner:** [`scripts/record_formation_front_chiral_edge_2026_07_05.py`](../scripts/record_formation_front_chiral_edge_2026_07_05.py)
**Runner cache:** [`logs/runner-cache/record_formation_front_chiral_edge_2026_07_05.txt`](../logs/runner-cache/record_formation_front_chiral_edge_2026_07_05.txt)

## Statement

The prior free-field diagnostic
[`DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md`](DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md)
used an imposed record-time wall `m(s)=M sign(s-s0)`. This note tests a
modeled free-field replacement:

```text
m(s) = M * (2 theta(s) - 1),
```

where `theta(s)` is an explicit record-occupancy profile. On the finite
periodic record-time circle used by the runner, a rising formation front is
paired with a falling anti-front. The load-bearing checks are made at the
rising front; the anti-front is used as an opposite-chirality contrast.

The runner verifies:

1. For front widths `w in {0.75, 1.5, 3, 5, 8}`, diagonalization finds a
   near-zero edge subspace localized at the occupancy midpoint `theta=1/2`.
   The profile is exponentially localized and the localization length is
   measured for each width.
2. The edge chirality is fixed by the occupancy-gradient sign. Reversing the
   front from `0 -> 1` to `1 -> 0` flips the measured chirality.
3. Uniform empty/full occupancy has no front and no light chiral edge; the
   constant-mass bulk remains gapped.
4. The projected front-edge velocity operators obey the Cl(3,0) Pauli
   anticommutation algebra, so the front mode is a genuine Weyl cone in the
   same free-field sense as the prior diagnostic.

## Computed Witness

The runner first builds the same finite operator in two independent ways:
one vectorized construction and one explicit block assembly. They agree at
the operator level; the agreement magnitudes are pure rounding noise, so the
runner reports them as bound checks:

- `max|theta_A-theta_B| < 1e-14` (satisfied)
- `||H_A-H_B||_F < 1e-12` (satisfied)

At the spatial momentum used, the finite operator is exactly
sigma-degenerate, so the eigensolver's basis inside the low edge doublet is
BLAS/LAPACK-build-dependent. All localization witnesses below are therefore
computed from the basis-invariant two-state subspace marginal (the site
diagonal of the rank-2 low-subspace projector): peak sites are reported
tie-aware (every site within relative margin `1e-10` of the marginal
maximum; measured ties sit at `<= 5e-14` and resolved neighbors at
`>= 1.8e-8`), and the exponential tail is fitted from the deterministic
anchor site (the tie site nearest the occupancy midpoint).

The measured front-width table is:

| width `w` | gradient at front | midpoint site | peak sites (tie-aware) | chirality | probability `xi` | fit `R^2` |
|---:|---:|---:|---|---|---:|---:|
| 0.75 | +0.870062 | 32 | `[31, 32]` | `[-1, -1]` | 0.723996 | 0.999958 |
| 1.5 | +0.582783 | 32 | `[31, 32]` | `[-1, -1]` | 0.736150 | 0.999235 |
| 3 | +0.321513 | 32 | `[31, 32]` | `[-1, -1]` | 0.780902 | 0.994960 |
| 5 | +0.197375 | 32 | `[32]` | `[-1, -1]` | 0.785808 | 0.994213 |
| 8 | +0.124350 | 32 | `[32]` | `[-1, -1]` | 0.818263 | 0.991020 |

The chirality flip check at `w=3` gives:

```text
forward gradient  = +0.321513, forward chirality = -1.0
reverse gradient  = -0.321513, reverse chirality = +1.0
anti-front gradient = -0.321513, anti-front chirality = +1.0
```

The uniform contrast gives:

```text
gap_empty = 1.000000000000
gap_full  = 1.000000000000
```

The projected Weyl-cone check gives:

```text
max projected-velocity Clifford anticommutator error < 1e-10 (bound check)
projected velocity eigenvalues = [-1,+1] for each of the three Cl(3,0) axes
```

All quantities above are computed from diagonalizing the finite operator and
projecting inside the measured low eigenspace. The chirality is measured as an
expectation value of the record-time extended chirality operator; it is not
inserted as a per-site Cl(3,0) chirality. Rounding-noise magnitudes (the
construction agreements and the projected anticommutator error) are reported
as satisfied bounds rather than digits because their trailing digits are
BLAS-build-dependent.

## What Is Shown

At free-field level and under the stated occupancy-to-mass bridge, a monotone
record-occupancy front can play the role of the prior diagnostic's record-time
mass wall. The chiral edge localizes at the occupancy midpoint, and its
handedness follows the sign of the formation gradient. This models the
previously imposed wall sign by a formation-direction parameter: `0 -> 1` gives
the opposite chirality from `1 -> 0`.

The uniform-occupancy contrast shows that the light chiral mode is a front
effect, not a generic feature of the massive record-time bulk. The projected
velocity algebra shows that the localized front mode is still the Cl(3,0)
Weyl cone found in Step 1.

## What Is Not Shown

This note does not derive the occupancy-to-mass map from the Record axiom. The
map `m(s)=M(2 theta(s)-1)` is a motivated bridge used to test whether a
formation front has the right free-field domain-wall behavior. The current
minimal axiom surface names fixed records and readout; record-production
dynamics, a time metric, and physical persistence dynamics remain downstream
content.

This note also does not show gauge coupling, anomaly matching, Callan-Harvey
inflow, Standard Model chiral content, interactions, a Strong-CP result, or a
theta result. It does not set audit status and does not add a framework import,
primitive, or axiom.

## Dependencies and Consistency

- Prior free-field domain-wall diagnostic:
  [`DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md`](DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md)
  and its paired runner supply the Cl(3,0) gammas, record-time Hamiltonian
  form, low-subspace localization method, and projected Weyl-cone test.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the `Z^3` lattice, one-site `M_2(C)` / Cl(3,0) algebra, and Record
  boundary. It does not by itself derive the mass map used here.
- `ANOMALY_FORCES_TIME_NOTE_2026-05-16.md` and
  `ANOMALY_FORCES_TIME_THEOREM.md` are provenance context for treating
  record-time/chirality claims cautiously and keeping anomaly/time premises
  separate; they are not load-bearing dependencies of this free-field
  occupancy-front diagnostic.

## Validation

Run:

```bash
python3 scripts/record_formation_front_chiral_edge_2026_07_05.py
```

Observed:

```text
TOTAL: PASS=13 FAIL=0
```
