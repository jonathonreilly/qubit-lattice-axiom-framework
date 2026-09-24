---
claim_id: dynamics_clause_time_reversal_odd_star_terms_covariance_allows_them_and_on_the_cube_carving_none_keeps_the_majoranas_free_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Time reversal flips every Pauli, so a term is odd under it exactly when its Pauli strings have odd weight; the smallest are one-site fields and three-spin terms. Within one Admissibility neighbourhood (a star: a site m and its six neighbours), at weight at most three: (i) possibility covariance allows exactly one time-reversal-odd star term, the orientation-weighted scalar chirality of each octant's three neighbours, sum det[d1 d2 d3] s_d1 . (s_d2 x s_d3). It avoids the centre: every term through the centre, and every term on a collinear pair plus a third neighbour, vanishes because a proper rotation reverses the order of two of its sites while the chirality changes sign. (ii) Under the four landed actions (trivial, sign twist, axis, full) the covariant odd star terms span 68, 50, 49 and 37 dimensions: fields 3/1/0/0; through the centre with perpendicular neighbours 18/12/12/12, with collinear neighbours 18/8/8/2; octant triples 11/11/11/11; a collinear pair plus a third neighbour 18/18/18/12. (iii) None contains Kitaev's pattern s^a_i s^c_m s^b_k (a, b the bond axes to i and k, c the third axis). (iv) On the 8-site cube carving the Pauli strings that commute with the six loop operators are exactly the 2048 products of bond operators, and in Kitaev's representation each has Majorana degree 0, 2 or 4. Under every one of the five covariances, no nonzero covariant odd star term inside the cube both keeps the six loops and is bilinear in the Majoranas. Under the axis and full actions exactly one keeps the loops: the tripod, sum over octants of sign(d_x d_y d_z) s^x_{m+d_x} s^y_{m+d_y} s^z_{m+d_z}, which is quartic. A star meets the cube in four sites, so (iv) covers every odd star term inside the cube. Terms that reach recorded sites, longer terms on the full star, other carvings, and any chiral phase or physical identification are not treated."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_time_reversal_odd_star_terms_and_free_majoranas_on_the_cube_2026_09_24.py
---

# Time-reversal-odd star terms: covariance allows them, and on the cube carving none keeps the Majoranas free

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied covariance; unaudited.

## Result

Chiral matter needs time reversal or parity to be broken somewhere. The
Moriya coupling of open PR 9050 already gives the clause parity-odd
content. This note asks two things. What time-reversal-odd content can one
Admissibility neighbourhood carry covariantly? And does any of it keep the
exactly solvable carvings of open PRs 9048 and 9054 free, the way Kitaev's
three-spin term keeps his model free?
- **Possibility covariance allows one term.** It is the
  orientation-weighted chirality of the three neighbours in each octant,
  `Σ det[d₁ d₂ d₃] s_{d₁}·(s_{d₂} × s_{d₃})`. It avoids the centre.
- **The landed actions allow many.** At weight at most three they span 68,
  50, 49 and 37 dimensions (trivial, sign twist, axis, full).
- **None keeps the cube's Majoranas free.**
  - Kitaev's pattern is never covariant.
  - On the cube, no covariant odd star term both keeps the six loop
    operators and is bilinear in the Majoranas.
  - Under the axis and full actions exactly one term keeps the loops: the
    tripod `Σ sign(d_x d_y d_z) s^x_{m+d_x} s^y_{m+d_y} s^z_{m+d_z}`. It is
    quartic. It keeps the Z2 fluxes static but makes the Majoranas
    interact.

So a free chiral Majorana medium on the cube needs time-reversal-odd content
from outside this class. The candidates are the record contents (fields on
dangling axes, which the scan of open PR 9054 found gapped), terms that
reach recorded sites, and other carvings.

## Setting and decision points

- **Time reversal.** `Θ = Π_j iσ^y_j K` flips every Pauli. A Pauli string is
  odd under it exactly when its weight is odd.
- **The star.** A site `m` and its six neighbours. A field on a neighbour
  is the same lattice-wide term as a field on the centre, so fields are
  counted once. Three-spin terms sit on 35 triples in four classes:
  - through the centre, with perpendicular neighbours (12 triples);
  - through the centre, with collinear neighbours (3);
  - the three neighbours of one octant, one per axis (8);
  - a collinear pair of neighbours plus a third (12).
- **The covariances.**
  - The four landed actions of the soldering menu: trivial, sign twist,
    axis and full.
  - Possibility covariance: lattice rotations move positions only, and the
    term is also invariant under every internal rotation.
- **The carving.** The cube of open PR 9048. It has one loop operator per
  face: the product of the Paulis along the face's normal axis.
- **Free.** Bilinear in Kitaev's Majoranas. In his representation (prior
  art) a bond operator `s^a_j s^a_k` on an `a`-bond is `i u_jk c_j c_k`.
  So a product of bond operators over an edge set carries the `c`'s of the
  sites of odd degree.

The dynamics clause, every star term and every covariance are supplied
decision points. None is adopted.

## Theorem 1 — possibility covariance allows one odd star term

An internally invariant three-index tensor is proportional to `ε_{αβγ}`. So
an odd three-spin term is a sum of scalar chiralities
`χ(a, b, c) = s_a·(s_b × s_c)`, which change sign when two sites are
swapped. Its coefficient on ordered triples must be invariant under the 24
proper rotations and antisymmetric under reordering.
- **Through the centre.** A proper rotation fixes `m` and swaps the two
  neighbours. For a perpendicular pair it is the half-turn about their
  bisector. For a collinear pair it is any half-turn about a perpendicular
  axis. So the coefficient equals its own negative and vanishes.
- **A collinear pair plus a third.** The half-turn about the third
  neighbour's axis swaps the pair and fixes the third. The coefficient
  vanishes.
- **Octants.** No proper rotation reverses the orientation of an octant's
  triple, and `det[d₁ d₂ d₃]` is invariant and antisymmetric. So exactly one
  term survives, `Σ_octants det[d₁ d₂ d₃] χ(d₁, d₂, d₃)`.
- **Fields.** A field is a vector, so no invariant field exists.

The runner computes the invariant space directly: dimension 1, equal to the
octant chirality to 6e-16. ∎

## Theorem 2 — the landed actions allow many, none of Kitaev's form

Group-averaging over the 24 rotations gives the covariant odd star terms.

| Class | trivial | sign twist | axis | full |
|---|---|---|---|---|
| Fields | 3 | 1 | 0 | 0 |
| Through the centre, perpendicular | 18 | 12 | 12 | 12 |
| Through the centre, collinear | 18 | 8 | 8 | 2 |
| Octant triples | 11 | 11 | 11 | 11 |
| Collinear pair plus a third | 18 | 18 | 18 | 12 |
| **Total** | **68** | **50** | **49** | **37** |

Kitaev's pattern is `s^a_i s^c_m s^b_k`, where `a` and `b` are the bond axes
to `i` and `k` and `c` is the third axis. On a carving it is bilinear in the
Majoranas. The span of its 12 terms meets every covariant space, and the
possibility-covariant one, only in zero. ∎

## Theorem 3 — on the cube, loop-keeping strings are bond products

- **The commutant.** The six loops generate a group of rank 5, since their
  product is the identity up to phase. Their commutant among Pauli strings
  on 8 qubits therefore has `2^(16−5) = 2048` elements, up to phase.
- **Bond products.** The 4096 edge sets of the cube give exactly these 2048
  strings. Only the empty set and the full set give the identity.
- **Majorana degree.** A product over an edge set is gauge fields times the
  `c`'s of its odd-degree sites. On the physical space the product of all
  eight `c`'s is a gauge constant, so the degree counts up to complement.
  It is 0, 2 or 4.
- **Examples.** Kitaev's pattern has degree 2. The tripod at `m` equals
  `−i (s^x_m s^x_{m+x})(s^y_m s^y_{m+y})(s^z_m s^z_{m+z})`, with degree 4. ∎

## Theorem 4 — on the cube no covariant odd star term keeps the Majoranas free

Evaluate each covariant term on the cube, keeping the star terms whose
support lies inside it: fields, perpendicular triples through the centre,
and octant triples. A star meets the cube in four sites, so these are all
the odd star terms inside the cube.

| Covariance | Nonzero on the cube | Keeps the six loops | Keeps them and is bilinear |
|---|---|---|---|
| trivial | 32 | 0 | 0 |
| sign twist | 24 | 0 | 0 |
| axis | 23 | 1 | 0 |
| full | 23 | 1 | 0 |
| possibility | 1 | 0 | 0 |

The loop-keeper under the axis and full actions is the tripod
`Σ_octants sign(d_x d_y d_z) s^x_{m+d_x} s^y_{m+d_y} s^z_{m+d_z}`. Every
string in it has Majorana degree 4. ∎

## What this means for the lanes

- **Chirality lane.**
  - Covariance allows time-reversal-odd content, even without soldering:
    the octant chirality is possibility-covariant.
  - No covariant odd star term keeps the cube's Majoranas free.
  - Under soldering the tripod is the one covariant odd term that keeps the
    Z2 fluxes static. It adds a Majorana interaction on each flux sector.
- **Where free chirality could come from.** Odd content from outside this
  class:
  - the record contents, meaning the fields on dangling axes, which open
    PR 9054's scan found gapped;
  - terms that reach recorded sites;
  - other carvings.
- **The ladder of the synthesis.** At this order, chirality sits beyond the
  free sector of the carvings.

## Checks

The runner has 5 checks and all pass in about 10 s.

| Check | Result |
|---|---|
| Possibility covariance | Dimension 1, only in the octant class; it equals the orientation-weighted chirality to 6e-16. |
| Landed actions | Totals 68, 50, 49, 37, with the class table above. |
| Kitaev's pattern | 12 pattern terms; intersection 0 with all five covariant spaces. |
| Cube commutant | 2048 loop-commuting strings equal the 2048 bond products; degrees 0, 2 and 4. Kitaev's pattern has degree 2. The tripod equals `−i K_x K_y K_z` exactly, has degree 4 and is odd under `Θ`. |
| Cube, covariant terms | The table above: no covariant term keeps the loops and is bilinear; the one loop-keeper (axis, full) is the tripod. |

## What this does not do

- It adopts no star term and no covariance.
- On the full star it covers weight at most three. On the cube the result
  covers every odd star term inside the carving.
- Terms that reach recorded sites act through record contents and are not
  treated. Neither are the face-diagonal strips of open PR 9048 or the
  networks of open PR 9054.
- It does not study the tripod's interacting dynamics. It claims no chiral
  phase, Chern number, Weyl node or physical identification.
