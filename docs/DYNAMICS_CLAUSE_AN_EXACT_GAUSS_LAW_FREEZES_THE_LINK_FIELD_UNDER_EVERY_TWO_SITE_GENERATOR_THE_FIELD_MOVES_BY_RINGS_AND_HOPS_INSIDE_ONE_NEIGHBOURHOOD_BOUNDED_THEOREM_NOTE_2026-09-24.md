---
claim_id: dynamics_clause_an_exact_gauss_law_freezes_the_link_field_under_every_two_site_generator_the_field_moves_by_rings_and_hops_inside_one_neighbourhood_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting: doubled coordinates (vertex, link, plaquette and cube sites have 0, 1, 2 and 3 odd coordinates). A Gauss law puts each link site's field into the Gauss operators of both of its end vertices. (i) Nearest neighbours differ by one role, so no two link sites are adjacent. Hence every generator that is a sum of nearest-neighbour two-site terms and commutes with every Gauss operator also commutes with every link field; every compression of such a generator onto a Gauss sector does too. This holds for additive (U(1)-type) Gauss laws with static or dynamical vertex charges, and for Z2 Gauss laws. (ii) The smallest Gauss-invariant operators that move the field are vertex-link-vertex hops (only with dynamical vertex charges) and four-link rings around a plaquette. Each lies inside one site's closed neighbourhood; a vertex site's neighbourhood holds no mover. (iii) Under full soldering, the Gauss law sum_l s_l . n(v->l) is covariant, and a covariant vertex charge is a constant. The Gauss-invariant covariant operators on a plaquette site's four links have one real ring coupling. (iv) Take a vertex-star Gauss energy U sum_v (div E)^2 and transverse link fields of equal size h. Through fourth order, the ice space then has ring coupling g = 5 h^4/(32 U^3) and no configuration-dependent diagonal term. At K = -J, D = 0, vertex records and plaquette records along the normal give transverse link fields. Finite certificates: a five-site window, one plaquette and the L = 6 coarse torus. The dynamics clause (open PR 9040), the Gauss law, the soft Gauss energy and the record contents are supplied, not adopted. No photon phase, charge assignment or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_an_exact_gauss_law_freezes_the_link_field_under_two_site_generators_2026_09_24.py
---

# An exact Gauss law freezes the link field under every two-site generator

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** supplied models and finite certificates; unaudited.

## Result

The dynamics clause of open PR 9040 is a sum of nearest-neighbour two-site
terms, and it moves nothing that an exact Gauss law protects:
- Link sites are never adjacent in doubled coordinates.
- Changing a link's field changes the Gauss operators at both of its ends.
- A two-site term can compensate at most one of them.

So any two-site generator that respects the Gauss law leaves every link
field conserved. The field moves only through operators that span a whole
path or loop:
- **Hops,** vertex–link–vertex. These need dynamical charges at the
  vertices.
- **Rings,** the four links around a plaquette.

Each lies inside one site's neighbourhood: a hop inside a link site's, a
ring inside a plaquette site's. Admissibility conditions each site on
exactly this set.

Under full soldering:
- the Gauss law is the outward sum of link Bloch components;
- a vertex charge must be a constant;
- the covariant ring has one real coupling.

With a soft Gauss energy in place of the exact law, record fields on the
links generate that ring at fourth order, with `g = 5h⁴/(32U³)` and no
competing diagonal term.

## Setting and decision points

**Roles.** Doubled coordinates as used in the landed ice notes (for example
`UNIFORM_ICE_BY_FORMATION_TWO_ADJACENT_CUBES_ADMIT_NO_LOCAL_ORDER_EVEN_WITH_BOTH_CUBE_SITES_BOUNDED_THEOREM_NOTE_2026-09-23.md`):
- a site with 0 odd coordinates is a vertex;
- 1 odd coordinate, a link site;
- 2, a plaquette site;
- 3, a cube site.

**Gauss laws.** These are a supplied decision point, called D-gauss here.
- **U(1)-type:** `G_v = Σ_l σ_v(l) E_l − Q_v`.
  - The sum runs over the six links at `v`.
  - `σ = ±1` is the outward orientation.
  - `E_l` is a nondegenerate one-site observable of link site `l`.
  - `Q_v` is a one-site observable of vertex site `v`, or zero for static
    charges.
- **Z2-type:** `G_v = τ^x_v Π_l X_l`.
- Exact form: the generator commutes with every `G_v`, or is compressed
  onto a Gauss sector.
- Soft form: a vertex-star energy `U Σ_v (div E_v)²`.

**Dynamics clause.** Open PR 9040 (D-dyn), with full soldering (D-sold)
where stated. Records act as fields (open PR 9041). The record contents
are a pattern choice (D-pattern). Nothing here is adopted.

## Theorem 1 — the freeze

Let `H = Σ_b h_b` with each `h_b` acting on one nearest-neighbour pair.

**Symmetric form.** If `[H, G_v] = 0` for every vertex `v`, then
`[H, E_l] = 0` for every link `l`.

**Compression form.** For every Gauss sector projector `P`,
`[P H P, E_l] = 0`.

*Proof.* Use a product basis:
- `E_l` is diagonal on link sites;
- `Q_v` is diagonal on vertex sites;
- any basis on the other sites.

A matrix element `⟨c'|H|c⟩` is a sum of `⟨c'|h_b|c⟩`. It can be nonzero
only if `c` and `c'` differ inside a single bond.

Suppose they differ in the value of `E_l`, where `l` runs from `v` to `w`:
- the Gauss values at `v` and `w` both change;
- no two links are adjacent, so the bond's other site is a vertex or a
  plaquette site;
- that other site can compensate at most one of `Q_v`, `Q_w`.

So some Gauss value changes. `[H, G] = 0` forces all such matrix elements
to vanish, and so does compression onto a sector. The Z2 case is the same
with `X_l` eigenvalues. ∎

## Theorem 2 — the smallest movers, and where they live

**Hops.** With dynamical vertex charges, the vertex–link–vertex operators
include Gauss-invariant movers, such as `a_w† U_l a_v`. With static
charges, none move the field.

**Rings.** With static charges, a Gauss-invariant change of the link
fields has zero divergence at every vertex, so its support is a union of
closed loops. The coarse lattice is bipartite and simple, so a nonzero
divergence-free change touches at least four links. Its only four-link
cycles are plaquette boundaries, and on one plaquette the divergence-free
changes are `±(ring)`.

**Where they live.**
- A hop lies in a link site's closed neighbourhood: the link site and its
  two vertices.
- A ring lies in a plaquette site's closed neighbourhood: its four links.
- A vertex site's neighbourhood holds its six links. Each link's far end
  lies outside it, so it holds no mover, only diagonal terms such as the
  Gauss energy.

## Theorem 3 — what soldering allows

Under full soldering the natural link field is `E_l = s_l · ê_l`, and the
Gauss operator becomes `G_v = Σ_l s_l · n(v→l)`, the outward Bloch
components.
- **Covariance.** This `G_v` is invariant under all 24 rotations about
  `v`.
  - With a fixed internal axis and the trivial action, the oriented Gauss
    law is not covariant: 21 of the 24 rotations fail.
- **No dynamical vertex charge.** The rotations about a vertex act on its
  Bloch vector with no fixed axis. The only covariant one-qubit operators
  there are multiples of the identity.
  - So a covariant `Q_v` is a constant.
  - Theorem 2's hops are then unavailable. The movers inside one
    neighbourhood are the rings.
- **One ring coupling.**
  - Eight rotations fix a plaquette site.
  - Operators on its four links that commute with the corner Gauss sums
    form a space of dimension 18. Their movers span `{U_p, U_p†}`.
  - The covariant Hermitian ones form a space of dimension 5, with a
    one-dimensional mover part: one real ring coupling.

## Theorem 4 — a soft Gauss law makes the ring

Replace the exact law with the soft law:
- a vertex-star energy `H_0 = U Σ_v (div E_v)²`, where `E_l = ±1/2`;
- transverse link fields `V = −Σ_l h s_l^⊥` of equal size `h`.

The low space is the ice space: three links in and three out at every
vertex. Through fourth order in `h/U`:

    H_eff = const − g Σ_p (U_p + U_p†),    g = 5 h⁴ / (32 U³),

with no configuration-dependent diagonal term. The ring amplitude is
computed in a frame where each flip amplitude is real.

*Proof.* Flipping one link from an ice state creates charges ±1 at both of
its ends, which costs `2U`.

**Off-diagonal part.** A ring flips its four links in one of 24 orders.
- The first and third intermediate states cost `2U`.
- The second costs `2U` when the first two flips share a corner, where
  their charges cancel. That happens in 16 orders.
- It costs `4U` when they are opposite, in 8 orders.

The sum is `−(h/2)⁴ [16/(2U)³ + 8/(2U·4U·2U)] = −5h⁴/(32U³)`.

**Diagonal part.**
- Pairs of links with no shared vertex cancel against the renormalization
  term.
- Pairs that share a vertex contribute according to whether their flips
  cancel there (`2U`) or add (`6U`). That depends only on whether one link
  is in and the other out.
- Every ice vertex has 9 in–out pairs and 6 same-type pairs, so the
  diagonal energy is the same for every ice configuration. ∎

**Record fields.** At the soldered point `K = −J, D = 0`, the coupling
along a bond `e` is `J(I − e eᵀ)`.
- A vertex record's field on a link has no component along the link.
- A plaquette record along the plaquette normal gives the same.

Theorem 4 still needs equal magnitudes. Record-supplied fields also carry
direction-dependent phases, which enter the ring couplings as a background.
Neither is fixed here.

## What this means for the lanes

- **Photon lane.** It supplies its field dynamics.
  - The ice notes supply ring or Rokhsar–Kivelson Hamiltonians.
  - The hardcore-record gauge-ring note (landed,
    `HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md`)
    supplies three-site hops `a_y† a_x U_e`. It says it does not derive the
    field tensor factors "from one possibility qubit per original site".
  - Theorem 1 shows why the one two-site clause cannot stand in: under an
    exact Gauss law it moves nothing.
  - What moves the field is a term of Admissibility shape:
    - a ring clause at plaquette sites (Theorem 3: one real coupling);
    - or a soft Gauss energy at vertex sites (Theorem 4: the ring at fourth
      order from record fields).
- **Charged matter.** Under full soldering there is no dynamical charge on
  a vertex qubit, and so no hop. Charges then appear only as defects of a
  soft Gauss law.
- **Kitaev gauge field.** The exact Z2 field of open PRs 9048 and 9054
  evades Theorem 1. Its bond variables `u_jk = i b_j b_k` are shared by two
  sites and are not the field of a separate link site.

## Checks

The runner has 11 checks and all pass in about 4 s.

| Check | Result |
|---|---|
| Roles | Neighbours differ by one role. There are no link–link bonds. Neighbour counts: vertex 6 links; link 2 vertices + 4 plaquettes; plaquette 4 links + 2 cubes; cube 6 plaquettes. |
| Freeze, U(1) | Gauss-invariant two-site spans of dimension 38 (static charges) and 30 (dynamical). `max |[H, E_l]|` ≤ 2e-14. |
| Freeze, Z2 | Span of dimension 30; `max |[H, X_l]|` 2e-14. The three-site `τ^z Z τ^z` moves the field. |
| Freeze, compression | 7 Gauss sectors; `|[PHP, E_l]| = 0`, against `|[H, E_l]| = 53`. |
| Hops | Movers exist with dynamical charges (norm 5.66) and not with static charges (3e-15). |
| Rings | The L = 6 coarse torus is bipartite and simple. It has 648 four-cycles, all plaquettes, and the divergence-free changes are `±(1, 1, −1, −1)`. |
| Soldered vertex | Invariant to 1e-14. The invariant one-qubit space has dimension 1. The trivial action fails for 21 of 24 rotations. |
| Soldered plaquette | Stabilizer of order 8. Gauss-commuting space of dimension 18 with 2 movers; covariant Hermitian space of dimension 5 with 1 mover. |
| Soft Gauss ring (ED) | Half-splitting / `5h⁴/(32U³)` = 0.99944 at h/U = 0.04 and 0.99986 at 0.02. |
| Soft Gauss diagonal | The fourth-order diagonal energy is equal to machine precision on 5 ice configurations; the four sampled ones differ from the reference on at least 308 of 648 links. The ring element is exactly `−5/32`. |
| Transverse fields | Largest longitudinal component 0. |

## What this does not do

- It adopts no Gauss law, soft Gauss energy, soldering or record pattern.
- It derives no photon phase. The phase of the pure-ring cubic model, at
  zero Rokhsar–Kivelson potential, is not determined here.
- It does not treat record-supplied field phases or unequal magnitudes.
- It does not treat vertex qubits that stay unrecorded under the soft law.
- It makes no claim about non-Abelian Gauss laws or larger link spaces.
