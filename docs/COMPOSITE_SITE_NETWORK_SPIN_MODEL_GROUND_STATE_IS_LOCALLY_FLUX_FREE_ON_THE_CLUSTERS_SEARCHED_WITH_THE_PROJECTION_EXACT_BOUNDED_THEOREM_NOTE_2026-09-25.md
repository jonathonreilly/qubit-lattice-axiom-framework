---
claim_id: composite_site_network_spin_model_ground_state_is_locally_flux_free_on_the_clusters_searched_with_the_projection_exact_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied colored periodic network of composite sites of the landed network note, bonds J_lam (tau^lam tau^lam)(sigma.sigma) and the three-site odd term kappa in the runner's sign convention, in the fixed-parity six-Majorana representation, on periodic clusters of 8, 32, 64 and 256 sites. Exact: the per-sector reduction to three identical free-Majorana copies, and a projection rule giving the product of all local constraints on a sector's free ground state; the rule is checked against exact diagonalization of the full 16-qubit spin model on 8 sites for three coupling sets (every sector's assigned lowest physical level is an exact eigenvalue; the lowest is the exact ground energy). Finite diagnostics: on 32 sites, all 131072 gauge-inequivalent sectors with physical energies place the ground state in the locally flux-free sector at kappa = 0 for isotropic couplings (flux gap 0.426) and J_z = 2.5 (0.273); annealing on 64 and 256 sites at kappa = 0 and 0.3 finds no fluxed sector below the physical flux-free energy (margins 0.48-0.69); the 32-site cluster at kappa = +-0.3 is an exception, where all sectors put a half-fluxed sector 0.824 lower, identically for both signs of kappa. No thermodynamic-limit flux theorem, phase, physical identification or new premise."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
runner: scripts/composite_site_network_ground_flux_sector_with_exact_projection_2026_09_25.py
---

# The composite-site network's spin model has its ground state in the locally flux-free sector on the clusters searched, with the projection exact

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied model with finite-cluster searches; unaudited.

## Result

The landed network note
`THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`
computed Majorana bands in the chosen sector with every bond variable `+1`,
and listed the spin model's ground flux sector and the projection onto
physical states as separate work. This note does both on finite clusters.

- **Exact (Theorem 1).** In each sector of conserved bond variables the spin
  model is three identical copies of one free-Majorana problem, and the
  product of all local constraints on the sector's free ground state is a
  closed formula in the bond variables and the determinant of the matrix
  that brings the hopping matrix to canonical form. When it is `−1`, the
  lowest physical state of that sector carries one excitation at the lowest
  level.
- **The rule matches exact diagonalization.** On 8 sites (16 qubits), for
  three coupling sets, every sector's lowest physical level as the rule
  assigns it is an exact eigenvalue of the full spin model, and the lowest
  of them is the exact ground energy to `10⁻⁶`.
- **Locally flux-free on 32 sites, all sectors.** With physical energies,
  all 131072 gauge-inequivalent sectors of the 32-site cluster place the
  ground state where every ten-site loop has flux `+1`, at `κ = 0` for
  isotropic couplings (lowest fluxed sector `0.426` higher) and for
  `J_z = 2.5` (`0.273` higher).
- **Annealing on 64 and 256 sites.** At `κ = 0` and `0.3`, annealing over all
  bond configurations finds no sector below the locally flux-free one, and
  the physical flux-free energy lies below every fluxed sector found, by
  `0.48–0.69`; every single-bond flip costs energy.
- **One exception.** On the 32-site cluster with the odd term on, a sector
  with half of its loops fluxed lies lower. All 131072 sectors at
  `κ = ±0.3` put the physical ground there, `0.824` below the lowest locally
  flux-free sector, with every sector's physical energy the same for both
  signs of the odd term. The 64- and 256-site clusters searched do not repeat
  it.

Finite clusters only. No thermodynamic-limit statement follows from them,
and no flux-selection theorem is imported.

## Setting and decision points

- **D-network, D-bonds, D-odd (supplied, landed).** The explicit site and
  flavour rules of the landed network note, reproduced in the runner; bonds
  `J_λ (τ_i^λ τ_j^λ)(σ_i·σ_j)`; the three-site odd term of strength `κ`, in the
  runner's sign convention. The network note records that its spectra do not
  fix the odd term's sign; this note computes both signs on 32 sites.
- **D-majorana (supplied, landed).** The fixed-parity six-Majorana
  representation of
  `COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md`:
  per site `b^x, b^y, b^z, c^x, c^y, c^z`, local constraint
  `D_i = −i b^x b^y b^z c^x c^y c^z = 1`.
- **The clusters (method).** Periodic `2×2×4` (8 sites), `4×4×4` (32), `8×4×4`
  (64) and `8×8×8` (256) boxes of the network; on the small tori two sites
  can be joined by more than one bond, which the runner keeps as distinct
  bonds.

None is adopted.

## Theorem 1 — the reduction and the projection rule

1. **Three identical copies.** The bond variables `u_ij = i b_i^λ b_j^λ`
   commute with the Hamiltonian and with each other. In a sector `{u}` the
   Hamiltonian is `Σ_α (i/4) c^α·A(u) c^α` with one real antisymmetric
   matrix `A(u)` for all three flavours `α`, entries `2J_λ u_ij` on bonds and
   `2κ u u` on the odd term's paths. Its lowest free energy is
   `−(3/2) Σ ε_k` over the positive levels `ε_k` of `iA(u)`. A gauge
   transformation at one site flips the bond variables around it and leaves
   every loop product unchanged, together with the spectrum.
2. **The projection rule.** Bring `A(u)` to canonical form,
   `Q^T A Q = ⊕ [[0, ε_k], [−ε_k, 0]]` with `Q` orthogonal and `ε_k > 0`. On
   the sector's free ground state the product of all local constraints is
   `Π_i D_i = (−i)^N · s · (−i)^{N_b} · Π_{bonds} u · (det Q · i^{N/2})³`,
   where `N` is the number of sites, `N_b` the number of bonds and `s` the sign
   of the permutation that reorders the site-ordered product of all `6N`
   Majoranas into bond pairs followed by the three flavour groups of `c`.
   The projector onto physical states `Π_i (1 + D_i)/2` keeps a state of the
   sector only if the product is `+1`, and it keeps the free ground state
   when it is. When the product is `−1`, occupying the lowest level in one
   copy flips it, so the sector's lowest physical energy is its free energy
   plus `ε_min`.

The formula follows from reordering the Majoranas and from the fermion
parity of each copy's canonical ground state; the runner checks its overall
sign against exact diagonalization (check 2), with the opposite sign
failing on every sector. ∎

## Diagnostic 1 — exact diagonalization on 8 sites

The full spin model on the `2×2×4` cluster has 16 qubits. For each coupling
set the lowest 120 exact levels are compared with the rule's lowest
physical level of each of the 32 gauge-inequivalent sectors.

| couplings `(J_x, J_y, J_z)` | sectors whose assigned level lies in the window | found in the exact spectrum | ground (rule) | ground (exact) |
|---|---|---|---|---|
| `(1, 1, 2.5)` | 32 | 32 | −35.668888 | −35.668888 |
| `(0.4, 1, 1.6)` | 32 | 32 | −23.613120 | −23.613120 |
| `(1, 1, 0.3)` | 10 | 10 | −24.136132 | −24.136132 |

## Diagnostic 2 — every sector of the 32-site cluster

The `4×4×4` cluster has 32 sites, 48 bonds and 32 ten-site loops; a spanning
tree leaves 17 bonds whose values label all 131072 gauge-inequivalent
sectors, fluxes and windings together.

| couplings, `κ = 0` | lowest locally flux-free (physical) | lowest with any loop at `−1` (physical) | flux gap |
|---|---|---|---|
| isotropic | −77.66563 | −77.23993 | 0.42570 |
| `J_z = 2.5` | −130.62793 | −130.35542 | 0.27251 |

The flux gap is the physical energy of the lowest sector with any loop at
`−1` above the physical ground; both use the projection rule.

## Diagnostic 3 — annealing on 64 and 256 sites

Simulated annealing over all bond configurations (single-bond flips, three
independent starts) and the lowest sector of every winding class. The
fluxed sectors' free energies bound their physical energies from below, so
a positive margin places the physical flux-free energy below every fluxed
sector found.

| cluster | `κ` | flux-free (physical) | lowest fluxed found (free) | margin | single-bond flips |
|---|---|---|---|---|---|
| `8×4×4` | 0 | −152.43808 | −151.88939 | +0.5487 | 0.729–1.303 |
| `8×4×4` | 0.3 | −166.77855 | −166.08563 | +0.6929 | 0.693–1.507 |
| `8×8×8` | 0 | −592.63386 | −592.15465 | +0.4792 | 0.479–0.512 |
| `8×8×8` | 0.3 | −652.73259 | −652.07068 | +0.6619 | 0.662–1.052 |

Annealing is a search, not an enumeration: it does not exclude a lower
fluxed sector that it did not reach.

## Diagnostic 4 — the 32-site cluster with the odd term

All 131072 sectors at each sign of the odd term, isotropic couplings:

| `κ` | lowest locally flux-free (physical) | lowest fluxed (physical) | loops at `−1` | difference |
|---|---|---|---|---|
| `+0.3` | −84.81708 | −85.64104 | 16 of 32 | −0.82396 |
| `−0.3` | −84.81708 | −85.64104 | 16 of 32 | −0.82396 |

Both minima have constraint product `+1`, so the projection leaves them at
their free energies. Every sector's physical energy agrees between the two
signs to rounding, so on this cluster the sign that the network note left
open does not matter for the flux sector. The 32-site torus is four sites
across, and the odd term's paths reach across it; the exception may be a
property of that small torus, and the larger clusters of Diagnostic 3 do
not show it, but this note does not establish why.

## What this does not do

- It proves no flux-selection theorem for the infinite network and imports
  none; the clusters are finite and the larger ones are searched, not
  enumerated.
- It claims no phase, gap in the thermodynamic limit, or physical particle
  identification for the flux excitations or the Majorana modes.
- It adopts no network, bond, odd term, sign convention or representation.

## Prior art (not premises)

Kitaev 2006 (the honeycomb model's exact solution and its projection);
Lieb 1994 (flux-phase theorem, whose hypotheses are not checked here);
Yao and Lee 2011 (the six-Majorana composite construction); Pedrocchi,
Chesi and Loss 2011, and Zschocke and Vojta 2015 (projection onto physical
states on finite clusters); Mandal and Surendran 2009, and O'Brien,
Hermanns and Trebst 2016 (three-dimensional tricoordinated Kitaev models
and their flux sectors). All cited as prior art, not as premises.

## Checks

The runner has five checks: the reduction's gauge invariance and cluster
structure; the projection rule against exact diagonalization; all sectors
of the 32-site cluster at `κ = 0`; annealing on 64 and 256 sites; the
32-site cluster at `κ = ±0.3`.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the explicit supplied network, Hamiltonian and clusters above.
- **N2 — Independence:** self-checked; the exact-diagonalization comparison is internal to this runner.
- **N3 — Imports:** Hilbert kinematics, the network, the Hamiltonian and the representation are supplied, not framework admissions.
- **N4 — Dependencies:** the landed parents' scopes govern.
- **N5 — Resolution:** floating-point spectra and determinants; annealing is a search.
- **N6 — Residuals:** larger clusters, the thermodynamic limit and dynamics of the flux sector remain open.
- **N7 — Counterroutes:** other sign conventions, representations and sectors remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
