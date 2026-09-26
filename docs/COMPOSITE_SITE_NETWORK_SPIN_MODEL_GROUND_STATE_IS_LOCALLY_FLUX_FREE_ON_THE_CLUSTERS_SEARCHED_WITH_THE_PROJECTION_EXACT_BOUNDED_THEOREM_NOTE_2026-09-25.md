---
claim_id: composite_site_network_spin_model_ground_state_is_locally_flux_free_on_the_clusters_searched_with_the_projection_exact_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Supplied connected finite colored graph and real antisymmetric three-flavour Majorana comparator, with
  local Clifford constraints. The global-parity criterion gives the projected sector minimum, with zero-mode qualification.
  Numerical enumeration on32sites and searches on64/256sites compare sectors; a restricted8site spin-spectrum window
  is a consistency check, not an operator equivalence or exhaustive spectrum proof. No thermodynamic flux theorem
  or universal spin-map sign is established.
upstream_dependencies:
- minimal_axioms
- the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
- composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
runner: scripts/composite_site_network_ground_flux_sector_with_exact_projection_2026_09_25.py
---

# Projection of a supplied Majorana comparator and finite flux searches

**Type:** bounded_theorem
**Status:** conditional Clifford algebra and finite numerical diagnostics; unaudited.

## Supplied model and sign boundary

Use the current parents' explicit periodic colored graph, three distinct colors at each vertex and tensor-product Clifford kinematics. Each site has b_x,b_y,b_z,c_x,c_y,c_z with D_i=-i b_x b_y b_z c_x c_y c_z=1. Supply u_ij=i b_i^lambda b_j^lambda and the runner's real antisymmetric A(u), with A_ij=2J_lambda u_ij and its explicitly oriented odd paths. The comparator is H=sum_alpha (i/4)c^alpha A c^alpha. No physical pattern, parton interpretation or selected gauge sector is derived.

An operator map to the positive-J spin Hamiltonian is not established by spectrum matching. With the usual onsite bilinear Pauli convention and u=i b_i b_j, the positive-J spin bond corresponds to the opposite hopping sign. An independent two-vertex three-colour Clifford control finds a full-spectrum discrepancy for the uncorrected plus sign; the opposite hopping sign matches. The odd-path sign also remains supplied. Below, 'physical' in historical tables means projection of this specified comparator. The eight-site spin comparison is reported only in its computed spectral window.

## Conditional projection theorem

For a connected finite trivalent colored multigraph, u variables commute with each other and the supplied quadratic comparator. A local D_i flips incident bond signs and corresponding matter Majoranas; this preserves the comparator and all loop products. Local ten-loop products alone need not specify global winding.

At nonsingular A, choose real orthogonal Q with Q^T A Q equal to positive blocks [[0,epsilon],[-epsilon,0]]. The free energy is -(3/2)sum epsilon. Reordering site-ordered Majoranas into oriented bond pairs and three matter groups yields

`Ptot=(-i)^N s (-i)^Nb product(u) [det(Q) i^(N/2)]^3`,

where s is the explicit permutation sign. This is the product of local constraints on the free ground state. The formula requires complete canonical pairs and a nonzero spectral gap for that ground parity to be well-defined.

Sufficiency follows from the gauge group: on a connected graph only the identity and product of all D_i stabilize every bond sign. All other group elements send a state to an orthogonal bond sector. Hence the full local projector has squared norm 2^(1-N) on a unit vector with Ptot=+1 and zero for Ptot=-1. A single matter occupation reverses Ptot, so the minimum projected energy is Efree for +1 and Efree+epsilon_min for -1. If exact zero modes exist, their occupation reverses parity at zero cost; the minimum remains Efree but an individual free-ground parity is not unique. The runner treats levels below its numerical tolerance as zero, a numerical classification rather than a proof of exact singularity.

The matrix entries, constraint algebra and this projection statement are conditional supplied mathematics. They do not by themselves prove the positive-J spin/odd-term operator equivalence.

## Numerical scope

All-sector enumeration refers to gauge fixing a spanning tree in the connected32site graph: E-V+1=17 remaining signs, hence131072 representatives. Energies use floating point, not certified intervals. The64/256site search retains annealing minima and about48 sampled bond flips; it does not test every single flip or all sectors. A positive sampled margin is not a global flux-selection theorem. The32site odd-term exception is retained.

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

Simulated annealing over all bond configurations (single-bond flips, three starts on64sites and two on256sites) and the lowest sector of every winding class. The
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
their free energies. Every enumerated sector's projected energy agrees between the two
signs to rounding, so on this cluster the sign that the network note left
open does not matter for the flux sector. The 32-site torus is four sites
across, and the odd term's paths reach across it; the exception may be a
property of that small torus, and the larger clusters of Diagnostic 3 do
not show it, but this note does not establish why.


## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite graph, Clifford representation, comparator and named sectors.
- **N2:** no imported flux-selection or phase theorem.
- **N3:** source Hamiltonian, odd sign and representation are supplied.
- **N4:** current parent scope and spin-map sign limitation remain explicit.
- **N5:** numerical spectra and searches are not certified global enclosures.
- **N6:** operator mapping, exhaustive larger flux classes and limiting inference remain open.
- **N7:** unvisited sectors, zero modes and alternate sign conventions remain counterroutes.
- **N8:** no physical particle claim, new premise or audit verdict.

## Actual inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24](COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md)
