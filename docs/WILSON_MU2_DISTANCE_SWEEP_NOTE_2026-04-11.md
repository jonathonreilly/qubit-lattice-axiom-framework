# One-Component Directed-Hopping `mu2` Parameter Sweep Note

**Date:** 2026-04-11; formal-model repair 2026-07-31
**Status:** bounded formal-model computation and finite comparator certificate
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only
**Primary runner:** [scripts/frontier_wilson_mu2_distance_sweep.py](../scripts/frontier_wilson_mu2_distance_sweep.py)

## Claim scope and naming boundary

This note makes two exact claims about supplied, dimensionless finite matrices
and post-processing rules.

1. On the declared open cubic graphs with `side in {11,13,15}`, source-coupling
   coefficient `5`, separations `d in {3,4,5,6}`, and operator-shift
   coefficient `mu2 in {0.22,0.05,0.01,0.005,0.001}`, all `60/60`
   shared-minus-self separation-curvature means are negative and meet the
   declared stability threshold. The five log-log fits increase strictly from
   `alpha=-3.315` to `alpha=-1.871`.
2. On the separate declared `4 x 4` coefficient grid at `side=15`, source
   coupling `5`, operator shift `0.001`, and separation `5`, one formal
   centroid-velocity proxy does not satisfy its declared slice-linearity,
   grid-normalization, or signed-comparator criteria.

The repository path and linked runner filenames retain historical
`wilson`/`newton`/`mass` names for discoverability. Those names are not physical
identifications. In this note, `G`, `mu2`, `MASS`, `M_A`, and `M_B` are only
dimensionless code coefficients; `P_A` and `P_B` are only post-processed
centroid-velocity proxies. Nothing here identifies a Wilson-Dirac operator,
gravitating or inertial mass, gravitational coupling or potential, physical
screening mass, momentum, force, distance, time, or Newton law.

## Executable evidence

The complete evidence surfaces are:

- the [primary runner](../scripts/frontier_wilson_mu2_distance_sweep.py) and
  its [complete cache](../logs/runner-cache/frontier_wilson_mu2_distance_sweep.txt);
- the historical-name [directed-hopping helper](../scripts/frontier_wilson_two_body_open.py);
- the [two-coefficient runner](../scripts/frontier_newton_both_masses.py) and
  its [complete cache](../logs/runner-cache/frontier_newton_both_masses.txt).

Each cache header pins the exact source hash and, where applicable, the helper
input fingerprint. Both cache bodies fit the audit transport without clipping.
The primary certificate has six executable checks; the two-coefficient
certificate has nine. Their `PASS` totals certify source/output consistency,
not the physical truth of a supplied interpretation.

## Exact formal model

Let the vertices be the sites of an open `side^3` cubic graph, indexed
lexicographically, and let `deg(i)` be the graph degree. The negative graph
Laplacian used by both runners is

```text
L_ii = -deg(i),    L_ij = 1 for nearest neighbors,    L_ij = 0 otherwise.
```

For a supplied source array `rho`, the real field array is the numerical
solution of

```text
[L - (mu2 + REG) I] phi = -4 pi G rho.
```

For each unordered nearest-neighbor pair enumerated as `i < j`, the
one-component Hermitian hopping matrix is

```text
H_ij = r/2 - i/2,                  H_ji = r/2 + i/2,
H_ii = c + phi_i + (r/2) deg(i).
```

Here `c` is a constant diagonal coefficient: `0.30` in the primary helper and
`M_A` or `M_B` in the two-coefficient runner. There is one complex scalar
amplitude per site and no spinor or gamma-matrix structure. The lexicographic
orientation is load-bearing: on the periodic bulk analogue,
`E(k)=c+3r+r sum_i cos(k_i)+sum_i sin(k_i)`, so the band has gradient
`(1,1,1)` at `k=0`, Hessian `-r I`, and is not reflection-symmetric. Reversing
the hopping orientation or the sign of the `phi` coupling reverses the sampled
separation-curvature sign. The negative rows below are therefore formal sign
observations under the displayed convention, not derived attraction.

The primary helper uses exact sparse exponential evolution for `20` steps and
renormalizes each packet after each step. The two-coefficient runner uses
Crank--Nicolson evolution for `18` steps and likewise renormalizes. For odd
separations, the integer placements are centered on a half-integer rather than
the central lattice site: the two-coefficient run places `A@x=5`, `B@x=10` on
`0..14`, with midpoint `7.5`. No exact reflection-control claim is made.

## Complete supplied-input ledger

None of the following choices is derived from the framework or measured from
nature. They define the finite computation.

Supplied model and protocol choices (`35`):

1. open three-dimensional cubic geometry;
2. the negative nearest-neighbor graph Laplacian above;
3. one complex scalar amplitude per site;
4. the lexicographically oriented complex hopping above;
5. the diagonal degree term `(r/2) deg(i)`;
6. the field-equation sign and `4 pi` normalization;
7. the `+phi` diagonal coupling;
8. normalized zero-phase Gaussian packets with `sigma=1`;
9. per-step wavefunction renormalization;
10. the `SHARED` versus `SELF_ONLY` subtraction protocol;
11. centroid/separation finite differences as the reported observables;
12. primary sides `{11,13,15}`;
13. primary separations `{3,4,5,6}`;
14. operator shifts `{0.22,0.05,0.01,0.005,0.001}`;
15. source-coupling coefficient `5`;
16. primary constant diagonal coefficient `0.30`;
17. hopping coefficient `r=1`;
18. time-step coefficient `DT=0.08`;
19. primary regularizer `1e-3`;
20. primary duration of `20` steps;
21. primary unit source weights;
22. primary early-window indices `2..10`;
23. pooled log-space ordinary least squares over three sides and four repeated
    separations;
24. two-coefficient side `15`;
25. two-coefficient separation `5` and positions `x=5,10`;
26. coefficient grid `{0.5,1,2,3}`;
27. each coefficient as its packet's field-source weight;
28. each coefficient as its packet's constant diagonal offset;
29. two-coefficient regularizer `1e-6`;
30. two-coefficient duration of `18` steps;
31. Crank--Nicolson rather than exact exponential evolution;
32. two-coefficient early-window indices `2..7`;
33. the inward-positive B convention and coefficient-multiplied velocity proxy;
34. anchor slices `M_A=1` and `M_B=1` with a free intercept; and
35. population-standard-deviation conventions and numerical denominator floors.

Supplied reporting/comparator choices (`7`):

1. a negative row means `mean < -1e-6`;
2. a stable row means `SNR > 2` (`MARGINAL` means `SNR > 1`);
3. the primary three-/four-decimal regression pins;
4. both anchor fits must have `R^2 > 0.95`;
5. both normalized grids must have `CV < 15%`;
6. row comparator bands at `10%` and `25%`, with aggregate mean/max cutoffs;
7. the hard-coded two-coefficient output/nonpass regression pins.

The following `11` physical-semantic bridges remain explicitly open and are
not asserted: scalar hopping to Wilson matter; source coefficient to
gravitating mass; constant diagonal coefficient to inertial mass; `phi` to
gravitational potential; `G` to gravitational coupling; `mu2` to physical
screening mass; lattice separation to physical distance; `DT` and step index
to physical time or acceleration; centroid curvature to force or attraction;
coefficient-times-velocity difference to momentum or impulse; and the signed
proxy comparator to action-reaction or Newton closure. There are zero
framework-derived physical inputs, observational inputs, literature constants,
or Planck/absolute-scale identifications in this packet.

## Primary finite sweep

For each row, the helper places two Gaussian packets, solves the supplied field
equation, evolves `SHARED` and `SELF_ONLY` modes, forms the difference between
their separation-curvature arrays, and averages indices `2..10`. It reports

```text
SNR = |mean(curvature proxy)| / [std(curvature proxy) + 1e-12].
```

For each operator shift, the primary runner fits all twelve stable negative
rows by ordinary least squares:

```text
log |curvature proxy| = alpha log(separation) + intercept.
```

| operator shift | fitted `alpha` | `R^2` | negative | stable | minimum SNR |
|---:|---:|---:|---:|---:|---:|
| 0.22 | -3.315 | 0.9960 | 12/12 | 12/12 | 8.12 |
| 0.05 | -2.392 | 0.9978 | 12/12 | 12/12 | 6.13 |
| 0.01 | -1.992 | 0.9984 | 12/12 | 12/12 | 5.67 |
| 0.005 | -1.927 | 0.9985 | 12/12 | 12/12 | 5.61 |
| 0.001 | -1.871 | 0.9986 | 12/12 | 12/12 | 5.56 |

The sampled exponents increase strictly:

```text
-3.315 < -2.392 < -1.992 < -1.927 < -1.871.
```

This is finite parameter dependence of a formal proxy. It is not an
asymptotic, continuum, or physical distance-law result.

## Two-coefficient finite comparator

The formal inward-positive proxies are

```text
P_A = M_A <v_A_shared - v_A_self>
P_B_in = M_B <v_B_self - v_B_shared>
signed comparator = P_A - P_B_in.
```

The constant diagonal coefficient would contribute only a global phase under
exact unitary evolution; its parameter dependence here is specific to the
finite-step Crank--Nicolson update. Multiplication by `M_A` or `M_B` is imposed
by definition and is not a momentum operator.

| diagnostic | computed result | declared criterion | outcome |
|---|---:|---:|---|
| `P_A` vs `M_B` at `M_A=1` | `R^2=0.944530` | both anchor `R^2>0.95` | nonpass |
| `P_B_in` vs `M_A` at `M_B=1` | `R^2=0.940033` | both anchor `R^2>0.95` | nonpass |
| `P_A/M_B` over the grid | `CV=35.382%` | both CVs `<15%` | nonpass |
| `P_B_in/M_A` over the grid | `CV=37.501%` | both CVs `<15%` | nonpass |
| `|P_A-P_B_in|/(|P_A|+|P_B_in|)` | `0/16` pass; mean/max `100%` | mean `<10%`, max `<25%` | nonpass |

Every sampled row has `P_A < 0` and `P_B_in > 0`; the displayed `100%` follows
from that coordinate convention. It is not a conservation test. The anchor
nonpass is also threshold-fragile: every leave-one-out three-point anchor fit
has `R^2 > 0.95` (A: `0.962987, 0.956240, 0.965706, 0.976408`; B:
`0.961343, 0.953859, 0.961661, 0.973262`). The exact four-point nonpass remains
true, but it is not a stable obstruction.

## Negative-claim boundary

The only negative content is failure of the displayed finite comparator on the
declared grid. No physical no-go, route exhaustion, independent wall set,
hidden-premise clearance, witness match, alternate-observable exclusion,
continuum exclusion, or universality claim is made. Other matrices, sign
conventions, observables, parameter windows, volumes, continuum sequences, and
current/flux constructions remain open.

## Conclusion

The complete executable packet preserves two bounded formal-model facts: the
five sampled separation-proxy exponents increase from `-3.315` to `-1.871`
while all `60` rows remain negative and stable, and one separate finite
two-coefficient proxy misses its declared criteria. Cite this only as a
dimensionless directed-hopping calculation, never as Wilson, gravity, force,
momentum, Newton-law, or no-go evidence.
