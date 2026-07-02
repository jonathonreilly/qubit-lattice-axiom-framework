# Equivariant Wilson-Eta Densities Vanish on the Tested Window - Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome and does not edit the audit-lane-owned registry, ledger, queue, or publication-status surface.
**Source-note proposal disclaimer:** this note is a source-note proposal; audit verdict and downstream status are set only by the independent audit lane.
**Runner:** scripts/frontier_equivariant_wilson_eta_densities_vanish_2026_06_12.py

## Boundary

This note proves the following scoped facts on the tested free bulk window only:

- spatial sizes `L in {2,3,4,6,8}` for the K-odd identity checks;
- density-tail sequences over `L in {3,4,6,8}`;
- temporal sizes `L_t in {4,8}`;
- Wilson parameters `r in {0.5,1}`;
- masses `m in {-2.5,-1.5,-0.5,0.5}`;
- both Wilson-mass variants described in the supplied surface.

It does not probe boundary geometries, does not settle the R-eta question in either direction, and does not claim large-L limits beyond the tested sizes. The phrase "tested window" is load-bearing throughout.

FIREWALL: no R-eta claim is made either way. No delta appears anywhere as an input on this surface; that is the probe's design point. No readings/cells are introduced. The scan varies `r`, but r is never fixed as a physical value.

## The supplied surface

Use only per-momentum-mode closed-form dispersions, never dense position-space operators. The antiperiodic mode convention used by the runner is

```text
k_mu = 2 pi (n_mu + 1/2) / L,    n_mu = 0,...,L-1
w    = 2 pi (n_t  + 1/2) / L_t,  n_t  = 0,...,L_t-1.
```

For each mode, the two signed branches are

```text
lambda_pm(k,w) = M_W(k,w) +/- sqrt(sum_mu sin(k_mu)^2 + sin(w)^2).
```

The two tested Wilson-mass variants are:

```text
spatial Wilson:
M_W = m + r sum_mu (1 - cos(k_mu))

spatial + temporal Wilson:
M_W = m + r sum_mu (1 - cos(k_mu)) + r (1 - cos(w)).
```

The `C_3[111]` action cyclically permutes `(k_x,k_y,k_z)`. Momentum modes are grouped into `C_3` spatial orbits. A size-three orbit carries the regular character content `{1, omega, omega2}` once each; a fixed orbit `k_x = k_y = k_z` carries only the singlet. This is the whole sector accounting used here.

## Theorem

**Sector-zero baseline.** At `r = 0`, `m = 0`, every character-sector eta vanishes exactly on the tested sizes, for both Wilson-mass variants. This is the landed bulk-vanishing lemma refined to the `C_3` character-sector decomposition. The runner checks both raw sign eta and tanh-smoothed eta at `eps in {0.1,0.01}` and prints the maximum absolute sector value.

**Check tag:** `sector_zero_raw_and_smoothed`.

**K-odd sector cancellation.** For every tested point
`r in {0.5,1}`, `m in {-2.5,-1.5,-0.5,0.5}`, `L in {2,3,4,6,8}`,
`L_t in {4,8}`, and for both Wilson-mass variants,

```text
eta_omega - eta_omega2 = 0.
```

The equivariant Wilson eta carries no K-odd content on this free surface. This is consistent with the registrable-parity structure described in the context notes `SCALAR_I_AND_REAL_GENERATION_STRUCTURE_K_PARITY_SEPARATION_BOUNDED_NOTE_2026-06-08.md`, `ETA_HOLONOMY_BASE_FLUX_SCOPE_BOUNDARY_NOTE_2026-06-06.md`, and `KOIDE_EMERGENT_TIME_ETA_CONJUGATION_PARITY_BOUNDED_NOTE_2026-05-30.md`.

**Check tag:** `k_odd_identically_zero`.

**Tested-window density decay.** The doublet-vs-singlet eta asymmetry density is

```text
rho_mode  = |eta_1 - eta_omega| / (L^3 L_t)
rho_orbit = |eta_1 - eta_omega| / (# C_3 spatial-orbits times L_t).
```

The runner prints full density tables for each `(r,m,L_t,variant)` over
`L = 3,4,6,8`, including the tail delta `|rho_mode(L=8)-rho_mode(L=6)|` and the last-three range over `L=4,6,8`. The benchmark example is reproduced on the spatial-Wilson, `L_t = 4`, `(r,m) = (0.5,-2.5)` row:

```text
rho_mode = 0.148148, 0.062500, 0.018519, 0.007812
```

Across the tested window, the tail densities are sub-extensive and no parameter point yields evidence for a converging nonzero density. The finite raw scan includes one zero-crossing tail, spatial-Wilson `L_t=8`, `(r,m)=(1,-2.5)`, where the sequence is `0.074074, 0, 0, 0.003906`; this is explicitly scoped as a finite zero-crossing guard, not read as a nonzero limit. At `L=8`, no candidate comes within `0.05` of the fixed-locus density `2/9`.

The exact-looking `2/9` that can be misread in this scan is only the distance of the zero candidate from the fixed-locus density:

```text
candidate = 0; distance = 2/9 -- not a hit.
```

The fixed-locus comparison lives in `KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`; it is comparison only, not an input or a target hit.

**Check tags:** `density_tables`, `no_L8_near_2_over_9`, `misread_guard`.

**Scoped free-bulk boundary with next paths.** The named boundary is the tested-window free-bulk Wilson-eta density boundary. On this tested free bulk window, sector-resolved Wilson-eta asymmetries are sub-extensive: bulk sector counting supplies no fixed-locus-density angle.

This does not close the APS program, does not close R-eta, and does not exhaust alternatives. The mechanism classes intentionally left open here are the next paths:

- boundary-localized spectral structure: manifold-with-boundary geometry, spectral flow, and residue-style corrections, inherited from the bulk-vanishing note's own opens;
- the direct multiset-to-geometry equation.

Both remain open and neither is probed here. No delta appears anywhere as input on this surface; that no-delta condition is structural, not an after-the-fact deletion.

**Check tag:** `free_bulk_boundary_and_next_paths`.

## No-Go Discipline Gate

This gate applies only to the narrowed negative boundary above: on the tested free bulk Wilson-eta surface, sector counting does not supply the fixed-locus-density angle. It is not a global R-eta no-go.

**N1 - alternative routes.** The tested routes are: sector-zero character eta, witnessed by `sector_zero_raw_and_smoothed`; K-odd character content, witnessed by `k_odd_identically_zero`; density-tail behavior, witnessed by `density_tables`; fixed-locus-density matching, witnessed by `no_L8_near_2_over_9`; and hidden delta insertion, witnessed by the runner's AST check. Boundary-localized spectral structure and the direct multiset-to-geometry equation are not tested routes here and remain open.

**N2 - wall independence.** The collapsed wall set has one member: the tested free-bulk Wilson-eta sector-counting boundary. No independent multi-wall claim is made.

**N3 - hidden-wall scan.** Phrases such as "supplied surface", "consistent with", and "next paths" are non-load-bearing context. The only load-bearing inputs are the displayed finite window, the closed-form dispersion, and the markdown-linked dependencies below.

**N4 - residual matching.** The inherited residual from the bulk-vanishing source is the free bulk eta/counting route. The R-eta and APS-boundary residuals are explicitly not claimed closed.

**N5 - rhetoric audit.** The claim is made at the finite free-bulk sector-counting resolution tested by the runner. It is not a boundary-geometry, large-L, per-history, or direct mass-multiset statement.

**N6 - partial-closure scan.** No new axiom, primitive, Tier-A admission, selector, probability rule, or realized-state value is introduced. A future boundary spectral theorem or direct multiset-to-geometry equation could still close the broader route without changing this note.

**N7 - steelman.** A hostile reviewer should object that boundary-localized spectral flow, residue corrections, or a direct multiset-to-geometry equation could bypass the free-bulk sector count entirely. That objection is accepted as the open remainder and is why this note is only a tested-window free-bulk boundary.

**N8 - cross-cycle echo.** The bulk-vanishing source already names boundary geometry, spectral flow, and residue-style corrections as opens. This note preserves those opens and only narrows the free-bulk counting route.

**Gate result:** PASS for the narrowed tested-window free-bulk boundary only.

## The next paths

The next paths are boundary-localized spectral corrections and the direct multiset-to-geometry equation. For the first path, the concrete opens are manifold-with-boundary geometry, spectral flow, and residue-style corrections. For the second path, the missing object is a direct equation taking the unordered mass multiset into the relevant geometry rather than through this free bulk sector count.

Context only, not dependencies: `UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md` and `ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md` name adjacent R-eta and multiset surfaces. This note does not consume them.

## Does NOT list

- Does not probe boundary geometries.
- Does not settle the R-eta question in either direction.
- Does not derive, assume, or input delta.
- Does not introduce readings/cells.
- Does not fix `r`.
- Does not claim a large-L result beyond the tested window.
- Does not turn the fixed-locus `2/9` density into a bulk Wilson-eta density.
- Does not close the direct multiset-to-geometry equation.
- Does not promote, demote, or set audit status for any row.

## Dependencies

- [`HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md`](HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md) - the dispersion surface, the bulk-vanishing lemma this refines, and the named opens preserved here.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) - current minimal axiom memo; cited only for baseline framework context.

**No-promotion statement:** this note does not promote, demote, or set the audit status of any dependency or companion. The independent audit lane is the only status authority.
