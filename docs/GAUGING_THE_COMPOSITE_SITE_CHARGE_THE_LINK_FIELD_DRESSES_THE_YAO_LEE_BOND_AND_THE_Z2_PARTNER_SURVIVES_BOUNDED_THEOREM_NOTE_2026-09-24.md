---
claim_id: gauging_the_composite_site_charge_the_link_field_dresses_the_yao_lee_bond_and_the_z2_partner_survives_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: doubled coordinates with one role per site class (D-roles: vertex = matter qubit sigma, link = U(1) link qubit with E_l = s^z_l/2 along the link's orientation as in open PR 9066, cube = the Z2 gauge partner tau of the vertex at -(1,1,1), plaquette free; D-comp); the Yao-Lee bond of open PR 9144 between composite sites two steps apart with its charged part dressed by the link raising operator, J (tau^l tau^l)[sigma^z sigma^z + 2(sigma^+ s^+_l sigma^- + h.c.)]; the Gauss law G_v = sum_out E_l - n_v + rho_v with n_v = (1 + sigma^z_v)/2 and the staggered background rho_v = 1 on odd vertices (D-background); the covariant ring -g (U + U^dag) of open PR 9072. Finite certificates on one plaquette of four composite sites with four links (12 qubits). (i) The dressed bond's five-site support (two vertices, one link, two cubes) fits a 4 x 2 x 2 block and no closed seven-site star; cube sites have six cube neighbours at distance two; the four site classes take four roles. (ii) Every Gauss operator commutes exactly with the dressed bonds and with the ring; the undressed Yao-Lee bonds violate it with commutator norm 2.0; the total matter charge commutes with H, while the matter S^x commutes with the undressed bonds (norm 0) and not with the dressed ones (norm 1.0): the SU(2) of open PR 9144 breaks to the gauged U(1). (iii) The product of the four partner qubits' sigma^z commutes exactly with the dressed Hamiltonian and the ring, and equals minus the product of the four bond factors: the Z2 flux sector survives the gauging. (iv) The gauge sector has dimension 112 of 4096; every state has total charge 2, the number of odd vertices; the matter record at each vertex equals the outward link flux plus the background, so the six matter patterns are functions of the link records (with 1, 1, 1, 1, 1, 2 link patterns each); H leaves the sector invariant (leakage 0); the lowest levels are -7.7274 (twice), -6.8990 (twice) at g = 0 and -7.8175 (twice), -6.8217 (twice) at g = 1/2, the latter with the ground pair in the Z2 flux sector W = +1 and the W = -1 sector starting at -6.8217. No gauged phase, no continuum, no three-dimensional record realization and no physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/gauging_the_composite_site_charge_with_the_link_field_2026_09_24.py
---

# Gauging the composite-site charge: the link field dresses the Yao–Lee bond and the Z2 partner survives

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied decision points; unaudited.

## Result

Open PR 9144 gave the carved Majoranas an exact charge by pairing each site
with a partner qubit: the Yao–Lee bond `(τ^λ τ^λ)(σ·σ)` has an SU(2) generated
by the matter spin, and its complex fermion carries charge one. That charge
was global. Open PRs 9066–9072 supply a U(1) link field with an exact Gauss
law and a covariant ring. This note couples the two.
- **The two structures fit the doubled lattice with one role per site
  class.** Vertex sites carry the matter qubit, link sites the U(1) field,
  cube sites the Z2 partner (cube sites are mutually adjacent at distance two
  along every axis, as vertices are), and plaquette sites stay free.
- **Minimal coupling is one link operator inside the bond.** Dressing the
  charged part of the Yao–Lee bond with the link raising operator,
  `σ^+_v s^+_l σ^-_{v'}`, makes every Gauss operator commute with the
  Hamiltonian exactly; without it the commutator has norm 2. The matter SU(2)
  breaks to the gauged U(1).
- **The Z2 structure survives.** The partner qubits' plaquette product still
  commutes with everything, so the model keeps a static Z2 flux sector as the
  undressed Yao–Lee model does. Per Z2 sector the model is a U(1) quantum
  link theory of the charged fermion plus a neutral Majorana flavour.
- **The background is the staggered sea.** On a closed lattice the outward
  fluxes sum to zero, so a one-sign charge has no gauge-invariant state; a
  staggered background charge gives a half-filled sector. Here the sector has
  112 of 4096 states, total charge 2 in every one, and the matter records are
  functions of the link records: the Gauss law as a support condition among
  records, as in the landed
  `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md`.

So the framework's three supplied structures, the Z2 gauge field of the
carvings, the U(1) link field, and charged matter on composite sites, coexist
on one lattice with exact gauge invariance. The price of the gauging is one
more site class in the role pattern, a `4 × 2 × 2` block for the bond, the
staggered background, and the loss of exact solvability in the charged
sector.

## Setting and decision points

- **D-roles (open PRs 9066, 9077).** Doubled coordinates: vertex, link,
  plaquette and cube sites have 0, 1, 2 and 3 odd coordinates.
- **D-comp (supplied).** The composite site of vertex `v` is `(v, v + (1,1,1))`:
  its matter qubit `σ` at `v` and its partner `τ` at the cube site. Bond
  types follow the axis of the bond, `λ(e) = e`.
- **The link field (open PR 9066).** `E_l = s^z_l/2` along the link's
  orientation; `s^±_l` raise and lower it.
- **The dressed bond (supplied).**
  `J (τ^λ_c τ^λ_{c'}) [σ^z_v σ^z_{v'} + 2(σ^+_v s^+_l σ^-_{v'} + σ^-_v s^-_l σ^+_{v'})]`
  for composite sites two steps apart along `e`, with `l` the link between
  the vertices, oriented from `v` to `v'`. `J = 1`.
- **The Gauss law and background (D-background, supplied).**
  `G_v = Σ_out E_l − n_v + ρ_v`, `n_v = (1 + σ^z_v)/2`, `ρ_v = 1` on odd
  vertices and 0 on even ones.
- **The ring (open PR 9072).** `−g (U + U†)` with `U` the oriented product
  of `s^±` around the plaquette.

None is adopted.

## Theorem 1 — geometry

For a bond along `x` from `v = (0,0,0)`: support `(0,0,0), (2,0,0)` (vertices),
`(1,0,0)` (link), `(1,1,1), (3,1,1)` (cubes). Its bounding box is `4 × 2 × 2`;
no closed star of seven sites contains it (0 of 343 stars in a block). A cube
site's six neighbours at distance two are cube sites. So the composite bond
of open PR 9144 (a plaquette-corner term) becomes, once gauged, a
double-plaquette block term, and every site class of the doubled lattice
carries one role. ∎

## Theorem 2 — gauge invariance and the broken SU(2)

On the plaquette of four composite sites with bond types `x, y, x, y`:
- `[G_v, H_dressed] = 0` and `[G_v, ring] = 0` exactly for all four
  vertices; `‖[G_v, H_bare]‖ = 2.0` for the undressed bonds.
- `[S^z, H] = 0` (the total matter charge is conserved), `‖[S^x, H_dressed]‖
  = 1.0` while `[S^x, H_bare] = 0`.

The dressing is minimal coupling: the hop of the charged fermion carries one
unit of link flux, and nothing else changes. ∎

## Theorem 3 — the Z2 partner survives

`W = τ^z_1 τ^z_2 τ^z_3 τ^z_4` commutes exactly with the dressed Hamiltonian
and with the ring, and equals minus the product of the four bond factors
`τ^λ_I τ^λ_J`. In Yao–Lee form the partner Majoranas enter only through the
link variables `u = i b^λ b^λ`, which the dressing does not touch; so the
Z2 gauge field stays static, and each Z2 sector is a U(1) quantum link model
of the charged fermion `f = (c^x + i c^y)/2` plus the neutral flavour `c^z`.
The charged sector is no longer free. ∎

## Theorem 4 — the gauge sector and the support condition

- Dimension 112 of 4096; total charge `N_f = 2` in every state, the number
  of odd vertices, since the outward fluxes of a closed graph sum to zero.
- In every gauge-invariant basis state `n_v = Σ_out E_l + ρ_v`: the matter
  record is a function of the surrounding link records. Six matter patterns
  occur, with 1, 1, 1, 1, 1, 2 link patterns each.
- `H` leaves the sector invariant (leakage 0), and `W` is diagonal on it.
- Lowest levels: `g = 0`: −7.7274 (twice), −6.8990 (twice); `g = 1/2`:
  −7.8175 (twice), −6.8217 (twice). At `g = 1/2` the ground pair lies in
  `W = +1` and the `W = −1` sector starts at −6.8217. ∎

## What this means for the lanes

- **Gauge and matter lanes.** The ladder now has: Z2 gauge field and neutral
  Majoranas at one qubit per site (open PRs 9048, 9054, 9112); a global
  charge at two qubits per site (open PR 9144); a gauged charge at three site
  classes, vertex, cube and link, with the plaquette class free for the ring
  clause's own qubits.
- **Records.** The Gauss law is again a support condition among records:
  given the link records around a vertex, the matter record is fixed. The
  staggered background is the half-filled sea of the landed staggered notes.
- **What the framework supplied.** Roles, the composite pairing, the link
  identification, the dressing, the background and the ring are all
  decision points; the only theorem-level content is that they are mutually
  consistent with exact gauge invariance and a surviving Z2 sector.

## What stays open

- A three-dimensional network of composite sites realized by records (the
  vertex–cube pairing is a role pattern here).
- The phase of the gauged model, the fate of the neutral flavour, and
  whether the ring clause and the dressed bonds can be generated rather than
  supplied.
- Chirality with the gauged charge: the odd term of open PR 9144 was not
  dressed here.

## Prior art

Kitaev 2006; Yao and Lee 2011; Chandrasekharan and Wiese 1997 (quantum link
models); Banerjee, Dalmonte, Müller, Rico, Stebler, Wiese and Zoller 2012
(U(1) quantum link models with staggered fermionic matter). All cited as
prior art, not as premises.

## Checks

The runner has 4 checks and all pass in about a second.

| Check | Result |
|---|---|
| Geometry | Roles vertex, vertex, link, cube, cube; box `4 × 2 × 2`; 0 stars; six cube neighbours at distance two. |
| Gauge invariance | Commutators 0 (dressed, ring), 2.0 (bare); `[S^z, H] = 0`; `‖[S^x, H_dressed]‖ = 1.0`, `[S^x, H_bare] = 0`. |
| Z2 partner | `[W, H] = [W, ring] = 0`; bond-factor product `= −W`. |
| Gauge sector | 112 states; `N_f = 2`; leakage 0; levels as above. |

## Independent check

None yet. The runner was rerun from a clean shell; no independent checker has
reviewed this block.

## What this does not do

- It adopts no role pattern, pairing, dressing, background or ring.
- It treats one plaquette of four composite sites; no phase, continuum or
  three-dimensional record realization is claimed.
- It does not dress the time-reversal-odd term of open PR 9144.
