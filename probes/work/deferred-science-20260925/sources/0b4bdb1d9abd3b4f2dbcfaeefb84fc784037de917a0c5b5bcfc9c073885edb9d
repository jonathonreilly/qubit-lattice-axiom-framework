---
claim_id: the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: composite sites of open PR 9144 (one gauge-role qubit tau and one matter-role qubit sigma) placed as in open PR 9149 at a vertex and its cube partner of the doubled lattice (D-comp, D-roles); Yao-Lee bonds J (tau^l tau^l)(sigma . sigma) between unrecorded composite sites two steps apart whose intermediate link site carries a record along axis l (D-flavour: flavour = record axis); recorded composite sites carry no bond term (D-frozen); the covariant odd term kappa (tau^l tau^n tau^m)(sigma . sigma) summed over cyclic (l, m, n) at every site; the flux-free sector u = +1. Finite certificates. (i) The hyperhoneycomb (10,3)-b graph embeds in Z^3, hence in the vertex sublattice of the doubled lattice, with every bond on a lattice axis and exactly three of the six neighbours used: straight chains of alternating x, y flavours run along x in layers z = 0, 2 mod 4 and along y in layers 1, 3 mod 4, joined by z-flavour bonds; the induced subgraph is trivalent, bipartite, connected, of girth 10 with 10 ten-cycles through a site, 8 sites per 2 x 2 x 4 cell and 4 per primitive cell, and it keeps an inversion about a chain-bond midpoint. (ii) Per 4 x 4 x 8 doubled cell the record pattern has 8 unrecorded and 8 recorded composite sites and 12 flavour records among 48 link sites; the site set has a stabiliser of order 8 in the 24 proper rotations (orbit 3) and the pattern with flavours a stabiliser of order 2 (orbit 12); the rule flavour = record axis is equivariant, the pattern is supplied. (iii) On an 8-qubit star with the odd term (J = 1.0, 0.8, 0.6; kappa = 0.35) the total matter spin commutes with H exactly and the 256 levels equal the three-flavour free-Majorana spectrum to 2e-14 for either sign of the odd hopping, which is a convention since the spectrum is even in kappa; all 10 loop operators through a site commute with all 1176 bond and odd terms near it; the bond fits a 4 x 2 x 2 block and the odd term a 6 x 2 x 2 or 4 x 2 x 4 block. (iv) At kappa = 0, isotropic J, the flux-free Majorana spectrum has a nodal line (gap below 1e-7, dimension estimate 0.85 from 576 and 1460 near-zero grid points at N = 16, 48); at J = (1, 1, 2.5) it is gapped with gap 1.0000. (v) At kappa = 0.3 the spectrum is symmetric under E -> -E at every k and the line breaks into 2 Weyl points at k/2pi = (0.355, 0.645, 0) and (0.645, 0.355, 0) of the supercell zone with Berry flux -1 and +1 (dimension estimate 0.06); the charged complex fermion inherits them as an opposite-chirality pair. (vi) Six-valent route: the operators i b^l c^a and i c^a c^b of a site with six gauge and three matter Majoranas generate an algebra of dimension 256 on 16 states, so a six-valent Yao-Lee site with SU(2) needs 4 qubits (3 for U(1), 2 for the trivalent site); on the cubic lattice the zero-flux c-Majorana bands have a zero-energy surface (dimension estimate 2.12), the pi-flux bands one eightfold node per 2 x 2 x 2 zone with zero Berry flux and lower energy per site (-1.1938 against -1.0026). No ground-state flux sector of the spin model, no gauging of the charge, no net-chiral charged Weyl fermion, no phase and no physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_dimensional_composite_site_network_with_an_exact_charge_2026_09_24.py
---

# The hyperhoneycomb embeds in the doubled cubic lattice: a three-dimensional composite-site network with an exact charge

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied decision points; unaudited.

## Result

Open PR 9144 gave the carved Majoranas an exact SU(2) charge with composite
sites and Yao–Lee bonds, but its network was a two-dimensional layer; open PR
9149 gauged the charge on one plaquette. The Yao–Lee construction is exactly
solvable when the three gauge Majoranas of a site pair with three distinct
bond flavours, so it needs a trivalent network, and the cubic lattice is
six-valent. This note asks whether a three-dimensional trivalent network of
composite sites sits on the doubled cubic lattice under nearest-neighbour
bonds.

- **It does: the hyperhoneycomb.** Straightening the zigzag chains of the
  hyperhoneycomb (10,3)-b lattice into axis chains embeds its graph in `Z^3`
  with every bond along a lattice axis and exactly three of the six
  neighbours used. Chains of alternating `x, y` flavours run along `x` in two
  layers out of four and along `y` in the other two; `z`-flavour bonds join
  the layers. The network is the induced subgraph of its site set, so the
  three-of-six selection is done entirely by which composite sites are
  unrecorded: no bond needs to be cut by a record.
- **What records supply.** Half the composite sites are recorded; the link
  site in the middle of each bond carries a record along the bond's flavour
  axis. The rule "flavour = record axis" is equivariant under the proper
  rotations; the pattern is a role pattern with orbit 12 (orbit 3 for the
  site set alone, whose stabiliser has order 8: the straightened chains give
  the embedding a tetragonal symmetry).
- **The charge and the solvability are exact.** The total matter spin, a sum
  of one-qubit operators, commutes with every bond and with the covariant odd
  term; the 10-loop operators commute with every term; on an 8-qubit star the
  spin spectrum is the three-flavour free-Majorana spectrum.
- **Bands: a nodal line, then a Weyl pair.** In the flux-free sector at
  isotropic coupling the Majorana bands are gapless on a line; the odd term
  breaks the line into two Weyl points of opposite chirality, pinned at zero
  energy by inversion together with particle-hole symmetry. The charged
  complex fermion `(c^x + i c^y)/2` inherits them: a charged Weyl pair of
  net chirality zero.
- **The six-valent route costs more.** A six-valent Yao–Lee site with SU(2)
  needs four qubits (three for U(1)); on the cubic lattice its flux-free
  bands have a zero-energy surface and its π-flux bands an eightfold node
  with zero Berry flux, so it gives neither a nodal line nor Weyl points
  without further terms.

Supplied model, finite diagnostic, no physical reading.

## Setting and decision points

- **D-roles, D-comp (open PRs 9066, 9144, 9149).** Doubled coordinates:
  vertex, link, plaquette and cube sites have 0, 1, 2, 3 odd coordinates. A
  composite site is a vertex `2p` (matter qubit `σ`) with its cube partner
  `2p + (1,1,1)` (gauge qubit `τ`).
- **D-net (supplied).** The unrecorded composite sites are those with
  network coordinate `p = (i, j, z)` satisfying: `j` even for `z ≡ 0`, `i`
  odd for `z ≡ 1`, `j` odd for `z ≡ 2`, `i` even for `z ≡ 3` (mod 4). All
  other composite sites are recorded.
- **D-flavour (supplied).** For two unrecorded composite sites two steps
  apart, the link site between them carries a record along an axis `λ`, and
  the supplied bond is `J_λ (τ^λ_I τ^λ_J)(σ_I·σ_J)`. The pattern used: chain
  bonds alternate `x, y` along the chain (shifted by one bond in layers 2 and
  3 so that the pattern keeps the `(1,1,2)` translation and the inversion),
  interlayer bonds carry `z`.
- **D-frozen (supplied).** Recorded composite sites carry no bond term.
- **The odd term (supplied, open PR 9144).** At every site `0` with
  neighbours `n_λ` along its flavour-`λ` bond,
  `κ Σ_{(λ,μ,ν) cyclic} (τ^λ_{n_λ} τ^ν_0 τ^μ_{n_μ})(σ_{n_λ}·σ_{n_μ})`.
- **The sector.** The flux-free sector `u = +1` on every bond in Kitaev's
  orientation; Lieb's rule for loops of length `2 mod 4` and the numerics of
  Mandal and Surendran select it (prior art), not this note.

None is adopted.

## Theorem 1 — the hyperhoneycomb embeds with axis bonds

The site set of D-net, with nearest-neighbour bonds, is a trivalent induced
subgraph of `Z^3`: every site has exactly three neighbours in the set, and
every adjacent pair of sites is a bond. It is bipartite, connected on the
`4 × 4 × 8` torus, has girth 10 with 10 ten-cycles through each site and
coordination sequence `3, 6, 12, 24, 38`. The `2 × 2 × 4` cell holds 8
sites; the translation `(1, 1, 2)` preserves sites and flavours, so the
primitive cell holds 4. The inversion `(i, j, z) ↦ (1 − i, −j, −z)` about
a chain-bond midpoint preserves sites and flavours. Every site's three bonds
carry the three flavours `x, y, z`.

The graph is the hyperhoneycomb: chains in alternating perpendicular
directions in successive layers, each chain site joined to the adjacent
layer by its third bond, alternately up and down along the chain, with
4 sites per cell and girth 10 (Mandal and Surendran 2009). Straightening the
zigzag chains changes the geometry, not the graph. ∎

## Theorem 2 — the record pattern and its covariance

Per `4 × 4 × 8` doubled cell: 16 vertices, 8 unrecorded (network) and 8
recorded; 48 link sites, of which 12 carry flavour records (the bonds), 24
join a network site to a recorded site and 12 join two recorded sites.
Under the 24 proper rotations, combined with translations, the site set has
a stabiliser of order 8 (orbit 3) and the pattern with flavours a stabiliser
of order 2 (orbit 12). The rule "flavour = record axis" is equivariant:
rotating the record rotates the flavour with it. So the rule is covariant and
the pattern is supplied, as in open PR 9144's honeycomb layer: one member of
a covariant family. ∎

## Theorem 3 — exact charge, exact solvability

- **Star.** Four composite sites (8 qubits, 256 states), bonds `x, y, z`
  from the centre with `J = (1.0, 0.8, 0.6)`, and the three odd terms at the
  centre with `κ = 0.35`. The total matter spin `S = Σ σ/2` commutes with `H`
  exactly (deviation 0), and the 256 levels (16 distinct, lowest −6.035520)
  equal the three-flavour free-Majorana spectrum with second-neighbour
  hopping `±κ` to 2e-14 for either sign. The spectrum is even in `κ`: the
  two signs are spin-flip time-reversal images of each other, so the sign
  of the reduction is a convention that no spectrum fixes.
- **Loops.** The 10 loop operators through a site, products over the loop of
  the `τ` Pauli of the flavour the loop does not use, commute with all 1176
  bond and odd terms in a window around the site (Pauli-string algebra);
  changing one Pauli breaks the commutation.
- **Supports.** The bond (two vertices, one link record, two cubes) fits a
  `4 × 2 × 2` block; the odd term fits a `6 × 2 × 2` block on a chain and a
  `4 × 2 × 4` block at a corner.

The reduction is Yao and Lee's: `τ^λ σ^α = i b^λ c^α`, the bond is
`u_IJ Σ_α i c^α_I c^α_J` with `u_IJ = i b^λ_I b^λ_J` conserved, and the odd
term is `−u u Σ_α i c^α c^α` between second neighbours. `S` rotates the
flavour index; `(c^x + i c^y)/2` carries `S^z = 1`. ∎

## Theorem 4 — the flux-free bands have a nodal line

With `J = (1, 1, 1)`, `κ = 0`, in the `2 × 2 × 4` supercell (8 bands per
flavour): the gap vanishes (below 1e-7 after refinement, at
`k/2π = (0.0833, 0.5833, 0)` for one point); the number of grid points with
gap below `1.5 · 2π/N` is 576 at `N = 16` and 1460 at `N = 48`, a dimension
estimate 0.85: a line. Bandwidth 6.000. At `J = (1, 1, 2.5)` the gap is
1.0000. ∎

## Theorem 5 — the odd term gives a charged Weyl pair

With `κ = 0.3`: the spectrum is symmetric under `E → −E` at every `k`
(inversion of Theorem 1 composed with particle-hole symmetry), so
zero-energy touchings are two-band crossings. Exactly 2 nodes are found, at
`k/2π = (0.355, 0.645, 0)` and `(0.645, 0.355, 0)` of the supercell zone,
each a touching of one pair of bands, with Berry flux through a surrounding
cube `−1` and `+1` (residual 0.000); the near-zero count is 200 and 214 at
`N = 16, 48`, a dimension estimate 0.06: points. The complex fermion of
Theorem 3 has the same Bloch matrix, so it carries the pair with unit
charge: a charged Weyl pair of total chirality zero, as Nielsen and
Ninomiya require on a lattice. ∎

## Theorem 6 — the six-valent route

- **Site content.** A six-valent Yao–Lee site needs six gauge Majoranas
  `b^1..b^6` and three matter Majoranas. The operators `i b^λ c^α` and
  `i c^α c^β` generate an algebra of dimension 256 on the 16-dimensional
  eigenspace of the central product: `M_16`, four qubits per composite site,
  half of a `2 × 2 × 2` doubled cell. With two matter Majoranas (U(1) only)
  the dimension is 64 on 8 states, three qubits; the trivalent Yao–Lee site
  gives 16 on 4, the two qubits of open PR 9144.
- **Bands.** On the cubic lattice with all six bonds, the zero-flux c-Majorana
  bands have a zero-energy surface (counts 1084 and 11164, dimension
  estimate 2.12); the π-flux bands have one node per `2 × 2 × 2` zone
  (counts 1 and 1), eightfold degenerate, with zero Berry flux of the lower
  bands, and the lower energy per site (−1.1938 against −1.0026), the
  ordering Lieb's theorem gives. Neither is a nodal line or a Weyl point. ∎

## Diagnostic (spectra table)

| Network, sector, term | Gapless manifold | Dimension estimate | Nodes, chirality |
|---|---|---|---|
| Hyperhoneycomb, flux-free, `J = (1,1,1)`, `κ = 0` | line | 0.85 (576 → 1460) | — |
| Hyperhoneycomb, flux-free, `J = (1,1,2.5)`, `κ = 0` | none, gap 1.0000 | — | — |
| Hyperhoneycomb, flux-free, `J = (1,1,1)`, `κ = 0.3` | points | 0.06 (200 → 214) | 2 nodes, `−1, +1` |
| Cubic six-valent, zero flux | surface | 2.12 (1084 → 11164) | — |
| Cubic six-valent, π flux | point, eightfold | 0.00 (1 → 1) | Berry flux 0 |

Supplied model, finite diagnostic, no physical reading.

## What this means for the lanes

- **Matter lane.** Three-dimensional charged matter on composite sites fits
  the doubled lattice with nearest-neighbour bonds. The price: half the
  composite sites recorded, a flavour record on each bond link, a
  `4 × 2 × 2` bond block, and one member of a 12-element family of patterns.
- **The ladder (open PR 9144).** Photon ring: one plaquette neighbourhood.
  Chiral neutral Majoranas: one star (open PR 9112). Charged chiral
  fermions: composite sites on a layer. Charged Weyl pair in three
  dimensions: composite sites on the hyperhoneycomb carving.
- **Gauge lane.** The link sites carry the flavour records here; in open PR
  9149 they carry the U(1) field. The two uses of the link class compete,
  which is a decision point for the gauged version.
- **Six-valent networks** sit one rung higher: four qubits per site, and the
  cubic flux-free bands are a surface rather than a line.

## What stays open

- The ground-state flux sector of the spin model on this network (only the
  flux-free sector is computed; Lieb's rule and prior numerics select it as
  prior art).
- Gauging the charge on the three-dimensional network (the link class is
  taken by flavour records).
- The recorded composite sites are frozen by decision; under the
  "records act as fields" reading of open PR 9041 their contents would have
  to be orthogonal to the flavours reaching them, not checked here.
- Whether the hyperoctagon (10,3)-a admits an axis-bond embedding; whether a
  full-density trivalent subgraph of `Z^3` gives a three-dimensional network.
- Second-neighbour terms on the six-valent cubic network and their nodes.

## Prior art

Kitaev 2006; Yao and Lee 2011; Mandal and Surendran 2009 (Kitaev model on the
hyperhoneycomb, gapless line); Hermanns and Trebst 2014 (hyperoctagon,
Majorana Fermi surface); Hermanns, O'Brien and Trebst 2015 (Weyl points from
the nodal line under time-reversal breaking, pinned at zero energy);
O'Brien, Hermanns and Trebst 2016 (classification of three-dimensional
Kitaev models); Lieb 1994 (flux phase); Nielsen and Ninomiya 1981; Wells
1977 and O'Keeffe et al. 2008 (the (10,3)-b or ThSi2 net). All cited as
prior art, not as premises.

## Checks

The runner has 8 checks and all pass in about 20 seconds, single-threaded,
under 100 MB.

| Check | Result |
|---|---|
| Embedding | 8 sites per `2 × 2 × 4` cell, degrees 3, induced, bipartite, `(1,1,2)` translation, inversion, girth 10, 10 ten-cycles, coordination `3, 6, 12, 24, 38`, connected. |
| Record pattern | 8 unrecorded, 8 recorded; 12 flavour records of 48 links; stabilisers 8 (orbit 3) and 2 (orbit 12). |
| Star | `[H, S] = 0` exactly; spectrum deviation 1.6e-14 and 1.5e-14 for `±κ`; lowest −6.035520. |
| Loops and supports | 10 loops commute with 1176 terms; control breaks; boxes `4 × 2 × 2`, `6 × 2 × 2`, `4 × 2 × 4`. |
| Nodal line | gap below 1e-7; dimension 0.85; bandwidth 6.000; anisotropic gap 1.0000. |
| Weyl pair | 2 nodes, chiralities `−1, +1`, residual 0.000, `E → −E` symmetry exact; dimension 0.06. |
| Six-valent content | 256 on 16, 64 on 8, 16 on 4. |
| Cubic bands | dimensions 2.12 and 0.00; eightfold node, Berry flux 0; energies −1.0026, −1.1938. |

## Independent check

None. The runner was rerun from a clean shell; no independent checker has
reviewed this block.

## What this does not do

- It adopts no composite site, role pattern, flavour rule, freezing rule or
  odd term.
- It does not determine the spin model's ground-state flux sector, does not
  gauge the charge, and does not claim a net-chiral charged Weyl fermion.
- The nodal line and the Weyl pair are the hyperhoneycomb Kitaev results per
  flavour (prior art); the new content is the axis-bond embedding on the
  doubled lattice, the record pattern and its covariance, the charge, and
  the six-valent counting.
- No phase, no continuum limit and no physical identification is claimed.
