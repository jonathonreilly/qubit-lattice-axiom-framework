---
claim_id: composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: Kitaev-type record carvings (open PRs 9048, 9054, 9112) with one matter Majorana per unrecorded site; composite sites (D-comp), pairing each dynamical site with a neighbour into a dimer whose two qubits play a gauge role tau and a matter role sigma (D-roles); bond terms (tau^l_I tau^l_J)(sigma_I . sigma_J) of weight four between neighbouring dimers; a time-reversal-odd three-dimer term. Finite certificates. (i) One qubit per site: in Kitaev's representation a Majorana bilinear i c_j c_k between two disconnected carving components anticommutes with D_j = b^x b^y b^z c, so the physical projector annihilates it (P (i c_j c_k) P = 0 on the 16-dimensional two-site extended space), a bond bilinear of one component survives with norm 1, and exp(i theta Q) leaks out of the physical space by |sin theta|; so no physical operator rotates two copies of a carving into each other. (ii) The composite bond term sits on the four corners of a plaquette (pairwise distances up to sqrt 2), lies in no closed seven-site star (0 of 216 stars in a block), and its (dimer axis, bond direction) family has orbit 24 under the proper rotations, so the family is covariant and one member is the role pattern. (iii) On a star of four dimers with bond types x, y, z and couplings (1.0, 0.8, 0.6), the 8-qubit spin model has exactly four levels -3e, -e, e, 3e with e = sqrt(2) and degeneracies 32, 96, 96, 32, the three-flavour free-Majorana spectrum of the Yao-Lee reduction (deviation 8e-15); the total matter spin S = sum sigma/2 commutes with H exactly, and the largest S^z per level is 1, 2, 2, 1, so one flavour excitation carries charge one; the multiplet content is (S = 0: 8, 1: 8), (0: 8, 1: 16, 2: 8), the same, (0: 8, 1: 8). (iv) The term kappa (tau^x_1 tau^z_0 tau^y_2)(sigma_1 . sigma_2) is odd under time reversal (T H3 T^-1 = -H3), commutes with S, and the spectrum with it equals the three-flavour free spectrum with next-nearest hopping kappa u u to 2e-14. (v) A honeycomb (brick-wall) layer of dimers with the odd term has, per flavour, Kitaev's Bloch Hamiltonian, gap 2.000 and Chern number of modulus one at J = (1, 1, 1), kappa = 0.2 (+1 in the runner's orientation, -1 at -kappa), so the charged complex fermion f = (c^x + i c^y)/2 has a chiral edge mode of unit S^z charge. The charge is a global U(1) inside an SU(2); no gauge field for it, no three-dimensional composite network realized by records, no net-chiral charged Weyl fermion and no physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/composite_sites_give_the_carved_majoranas_an_exact_charge_2026_09_24.py
---

# Composite sites give the carved Majoranas an exact charge: one qubit per site cannot, two can

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied decision points; unaudited.

## Result

The chiral fermions of open PR 9112 are Majoranas in a Z2 gauge field with no
exact U(1): even its Weyl pair is neutral. This note asks what an exact
charge costs.
- **One qubit per site cannot carry one.** Each unrecorded site of a Kitaev
  carving supplies one matter Majorana. A charge would rotate two Majoranas
  into each other, but a bilinear between two carving components is not a
  physical operator: it is odd under the gauge constraint. Two translated
  copies of a carving therefore have no physical SO(2) between them.
- **Two qubits per matter site can.** Pair each dynamical site with a
  neighbour into a dimer, one qubit carrying the gauge role and one the
  matter role. The weight-four bond term
  `(τ^λ_I τ^λ_J)(σ_I·σ_J)` reduces exactly to Yao–Lee form: a Z2 gauge
  field from the `τ`'s and three Majorana flavours from the `σ`'s, with an
  exact SU(2) whose generator is the total matter spin, a sum of one-qubit
  operators. The complex fermion `(c^x + i c^y)/2` has charge one under it.
- **The chirality survives with the charge.** A time-reversal-odd
  three-dimer term keeps the symmetry and the exact solvability. On a
  honeycomb layer of dimers it gives each flavour a Chern number of modulus
  one, so the charged fermion has a chiral edge mode carrying unit charge.
- **The price.** The bond term lives on a plaquette's four corners, pairwise
  within distance √2, and fits no single seven-site star. So charged matter
  sits on the same rung as SU(N) links (open PR 9081: composite links of 2N
  states): composite sites of two qubits, with plaquette-corner terms.

The charge is a global U(1) inside an SU(2). Gauging it, realizing a
three-dimensional dimer network by records, and a net-chiral charged Weyl
fermion in three dimensions all stay open.

## Setting and decision points

- **Carvings (open PRs 9048, 9054, 9112).** Records carve networks of
  unrecorded sites on which the compass point of the dynamics clause acts as
  Kitaev bonds; each site supplies Majoranas `b^x, b^y, b^z, c` with the
  constraint `D = b^x b^y b^z c = 1`, and `σ^a = i b^a c`.
- **D-comp (supplied).** A pairing of each dynamical site with one nearest
  neighbour into a dimer.
- **D-roles (supplied).** In each dimer one qubit is `τ` (gauge role) and one
  is `σ` (matter role). Which axis the dimers take and which end is which is
  a role pattern, not derived.
- **Bond terms (supplied).** For neighbouring dimers `I, J` whose `τ` qubits
  are adjacent along direction `λ`: `J_λ (τ^λ_I τ^λ_J)(σ_I·σ_J)`.
- **The odd term (supplied).** On a path `1–0–2` with bond types `x, y` at
  the centre: `κ (τ^x_1 τ^z_0 τ^y_2)(σ_1·σ_2)`.

None is adopted.

## Theorem 1 — one qubit per site: no charge between components

Take one site from each of two disconnected components, with Majoranas
`(b^x, b^y, b^z, c)` each, on the 16-dimensional extended space.
- The physical projector `P = (1 + D_1)(1 + D_2)/4` has rank 4, the two-qubit
  space.
- The would-be charge density `Q = i c_1 c_2` anticommutes with `D_1`
  (deviation 0), so `P Q P = 0`.
- A bond bilinear `i c_1 u_12 c_2` of one component, with `u_12 = i b^z_1 b^z_2`,
  survives: `‖P K P‖ = 1`.
- `exp(iθQ)` leaks out of the physical space by `|sin θ|`: 0.2955 at
  `θ = 0.3`, 1 at `θ = π/2`.

So the SO(2) that would rotate two translated copies of a carving into each
other has no physical generator: with one qubit per site the carved Majoranas
are neutral. ∎

## Theorem 2 — the composite bond term's support and covariance

With dimers along `z` and a bond along `x`, the support of
`(τ^x_I τ^x_J)(σ_I·σ_J)` is `(0,0,0), (0,0,1), (1,0,0), (1,0,1)`: the four
corners of an `xz` plaquette, pairwise within distance √2.
- No closed star (a site and its six neighbours) contains it: 0 of the 216
  stars in a block.
- The pair (dimer axis, bond direction) has an orbit of 24 under the 24
  proper rotations, so the family of bond terms is covariant; choosing one
  is the role pattern.

So the term is one rung above the star terms of open PRs 9088 and 9112: a
plaquette-corner term. ∎

## Theorem 3 — the Yao–Lee reduction on a star of four dimers

Take a centre dimer with three leaves of bond types `x, y, z` and couplings
`J = (1.0, 0.8, 0.6)`: eight qubits, 256 states.
- **Spectrum.** Exactly four levels `−3e, −e, e, 3e` with `e = √2 =
  √(J_x² + J_y² + J_z²)`, degeneracies 32, 96, 96, 32. This is the
  three-flavour free-Majorana spectrum: each flavour has one mode of energy
  `e` and one zero mode on the star, and the spin spectrum matches it to
  8e-15 (each free level four times, the gauge multiplicity).
- **The charge.** The total matter spin `S = Σ σ_i/2` commutes with `H`
  exactly. The largest `S^z` in the four levels is 1, 2, 2, 1: one flavour
  excitation raises the charge by one. The multiplet content is `(S = 0: 8,
  1: 8)`, `(0: 8, 1: 16, 2: 8)`, the same, `(0: 8, 1: 8)`; the zero modes
  carry spin, so the ground level is a mixture of singlets and triplets.

The reduction is Yao and Lee's: `τ^λ_i σ^α_i = i b^λ_i c^α_i` with six
Majoranas per dimer, so `(τ^λ_i τ^λ_j)(σ_i·σ_j) = u_ij Σ_α i c^α_j c^α_i` with
`u_ij = i b^λ_i b^λ_j` conserved, and `S` rotates the flavour index. The
complex fermion `f = (c^x + i c^y)/2` carries `S^z = 1`. ∎

## Theorem 4 — a time-reversal-odd term that keeps the charge

`H_3 = κ (τ^x_1 τ^z_0 τ^y_2)(σ_1·σ_2)` on the path `1–0–2` reduces to
`κ u_10 u_02 Σ_α i c^α_1 c^α_2`.
- `T H T⁻¹ = H` and `T H_3 T⁻¹ = −H_3` exactly, with `T` the product of
  `σ^y` times complex conjugation.
- `[H_3, S] = 0` exactly.
- With `κ = 0.35` the spin spectrum equals the three-flavour free spectrum
  with the next-nearest hopping, to 2e-14. The triangle `0–1–2` carries a
  flux, so a sign error in the reduction would have shown.

So chirality and charge coexist on composite sites. ∎

## Theorem 5 — a honeycomb layer of dimers is a charged chiral layer

Embed the honeycomb as a brick wall in an `xy` layer of `Z³`, dimers along
`z`, bond types `x, y` on the `y` bonds and `z` on the `x` bonds (a role
pattern). Every bond term is a plaquette-corner term, and the odd term spans
three dimers. Per flavour the Bloch Hamiltonian is Kitaev's.
- At `J = (1, 1, 1)`, `κ = 0.2`: gap 2.000, Chern number of the lower band
  `+1` in the runner's orientation, `−1` at `−κ` (Fukui–Hatsugai, 36²).

The complex fermion `f` inherits the Chern number and carries `S^z = 1`, so
the layer's chiral edge mode carries unit charge: the spin quantum Hall
structure of Yao and Lee (2011), cited as prior art. ∎

## What this means for the lanes

- **Charged matter.** An exact charge costs two qubits per matter site and
  plaquette-corner terms. One qubit per site gives neutral Majoranas, as in
  open PR 9112.
- **The ladder.** Photon ring: one plaquette-site neighbourhood. Chiral
  Majoranas: one star. Charged chiral fermions: composite sites plus
  plaquette corners. SU(N) links: composite links of 2N states (open PR
  9081).
- **Gauge lane.** The charge here is global. Coupling it to the U(1) link
  field of open PRs 9066–9072 is the natural next block.

## What stays open

- A three-dimensional network of composite sites realizable by records.
  Parallel dimers cannot have bonds along the dimer axis, since the partner
  site would be a network site; a three-direction network needs dimer axes
  that vary by site, a further role pattern not searched here.
- The record pattern that supplies the roles.
- Gauging the U(1); a net-chiral charged Weyl fermion in three dimensions
  (the complex fermion's nodes come in opposite-chirality pairs; the edge
  mode found is two-dimensional).

## Prior art

Kitaev 2006; Yao and Lee 2011 (exactly solvable spin-orbital model with
SU(2) symmetry and a spin quantum Hall effect); Nakai, Ryu and Furusaki 2012;
Seifert et al. 2020; Chulliparambil et al. 2021 (three-dimensional exactly
solvable spin-orbital liquids). All cited as prior art, not as premises.

## Checks

The runner has 5 checks and all pass in about a second.

| Check | Result |
|---|---|
| One qubit per site | `P Q P = 0`; bond bilinear norm 1.000; leakage 0.2955 at `θ = 0.3`, 1 at `π/2`. |
| Support and covariance | Weight 4; distances up to 1.414; 0 of 216 stars contain it; orbit 24. |
| Star of four dimers | Levels `±1.414214, ±4.242641`; degeneracies 32, 96, 96, 32; `[H, S] = 0`; largest `S^z` 1, 2, 2, 1. |
| Odd term | `T H_3 T⁻¹ = −H_3`; `[H_3, S] = 0`; free spectrum matched to 8e-15 and 2e-14. |
| Honeycomb layer | Gap 2.000; Chern `+1.0000` at `κ = 0.2`, `−1.0000` at `−0.2`. |

## Independent check

None yet. The runner was rerun from a clean shell; no independent checker has
reviewed this block.

## What this does not do

- It adopts no composite site, role pattern, bond term or odd term.
- It claims no gauge field for the charge, no three-dimensional record-realized
  composite network, no net-chiral charged Weyl fermion and no physical
  identification.
- The layer result is Kitaev's honeycomb per flavour; the new content is the
  embedding and the charge.
