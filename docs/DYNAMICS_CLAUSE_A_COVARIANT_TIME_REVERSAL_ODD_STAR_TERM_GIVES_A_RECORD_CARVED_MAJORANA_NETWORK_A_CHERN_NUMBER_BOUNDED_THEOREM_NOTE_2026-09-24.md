---
claim_id: dynamics_clause_a_covariant_time_reversal_odd_star_term_gives_a_record_carved_majorana_network_a_chern_number_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: the compass point of the fully soldered dynamics clause (open PR 9040), records acting as fields (open PR 9041), a record pattern with record contents, and a covariant time-reversal-odd star term. The clause and the star term are covariant under full soldering. The record pattern and its contents are supplied, non-covariant choices. (i) A 19-site relaxed three-direction network on the 4x4x4 cell (from open PR 9097's zero-field search) has no record touching unrecorded sites along all three axes. Each record points along the last axis that avoids its unrecorded neighbours, with sign (-1)^(x+y+z), so every field on an unrecorded site vanishes. (ii) Covariant odd star terms under full soldering, built as signed orbits of the 24 proper rotations, give 37 lattice terms at weights 1 and 3 (open PR 9088's count) and 325 at weights 1, 3, 5 and 7. (iii) Pauli strings on the carving, with records replaced by their values, are mapped exactly to Kitaev's Majoranas. The map reproduces the bond matrix, and matches exact spin spectra on three-site clusters and on 30 random tree clusters with multi-site strings to 1e-14. (iv) The covariant terms whose reduced strings are all free Majorana bilinears form a 41-dimensional subspace here; 5 of its directions act on the Majoranas. The projection onto it of the weight-5 orbit s^x_{+x} s^y_{-x} s^y_{+y} s^z_{-y} s^z_{+z} is a covariant term of weights 5 and 7. Its non-free strings cancel exactly, and its free image is 27 Kitaev patterns at corners plus the dangling-axis field s^x at (2,2,2), with the largest coefficient. (v) The compass bonds plus lambda times that term, in the 16 translation-invariant flux sectors of the cell: at lambda = 1, 2 and 4 the lowest (8 degenerate) have 12 exact zero modes per cell, a gap above them (0.019, 0.035, 0.017), and weak Chern numbers (-1, 0, 0). The phase is a window: the gap vanishes at lambda = 0.5 and 10 and is open at 0.9 and 8. (vi) A slab 12 cells thick, open along z, carries one chiral Majorana mode on each surface, of opposite chirality. (vii) The field term is essential: without it the gap vanishes. Time reversal (lambda -> -lambda) and uniform instead of staggered record signs both give (+1, 0, 0). (viii) Dangling fields decide the net chirality. With fields on all 13 dangling axes, of sizes 0.5 to 1.5 times 0.1 (three draws) or 0.2, 2 exact zero modes per cell remain, the chiral bands stay separated from the 12 bands grown from the zero modes and keep Chern number -1 on the k_x planes, and the negative zero-mode bands take +1, so the total vanishes. With fields of 0.1 on only the z axis at (2,1,2) and the x axis at (2,2,1), 10 exact zero modes remain, the other bands stay gapped at zero energy and the total C_x stays -1; on the y axis at (0,0,1) and the x axis at (0,1,0) the total is 0. With generic record contents no covariant term stays free. (ix) Another free term, with coefficients (-1.928, -1.492, 4.792, -0.488, -0.316) on the sign-fixed principal directions of the free subspace's action on the Majoranas, at lambda = 1 in a lowest flux sector: the 20 coupled Majoranas have exactly two band touchings (24 seeds), a particle-hole pair at k* and -k*, at energies -0.0071 and +0.0071, with Berry monopole charges -1 and +1 and linear splitting; C_x jumps by the charges at the nodes. At low energy this pair is one neutral two-component Weyl fermion. No chiral phase of the full lattice, no charged fermion and no physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_covariant_star_term_gives_carved_majoranas_a_chern_number_2026_09_24.py
---

# A covariant time-reversal-odd star term gives a record-carved Majorana network a Chern number

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied decision points; unaudited.

## Result

The chirality lane of this campaign had reached a precise gap.
- Open PR 9088 found no covariant time-reversal-odd star term of weight at
  most three that keeps a carving's Majoranas free.
- Open PR 9097 found that record fields keep the carved Majoranas
  sublattice-symmetric, so they give no Chern number.
- No covariant weight-three term, reduced by records, gives a same-class
  Majorana coupling.

This note goes to higher weight, on a supplied record pattern.
- **A free covariant term exists.** On a realizable carving whose records
  give zero fields, covariant odd star terms of weight 5 and 7 reduce to free
  Majorana bilinears. One of them has 27 copies of Kitaev's pattern at
  corners plus one dangling-axis field.
  - The record contents decide which strings survive and fix the pattern's
    signs.
  - Uniform signs flip the Chern number, as does time reversal.
  - Random contents give no free image in the cases tried.
- **It makes the Majoranas chiral.** Added to the compass-point bonds, it
  turns four flat zero modes per cell into dispersive bands. In a window of
  couplings those bands are gapped, with weak Chern numbers `(−1, 0, 0)`
  in every lowest translation-invariant flux sector.
- **The surfaces show it.** A slab carries one chiral Majorana mode on each
  surface, with opposite chirality.
- **Another direction gives a Weyl pair.** A second free covariant term on
  the same carving leaves the bands gapless at exactly one particle–hole
  pair of Weyl nodes, of charges −1 and +1. At low energy that is one
  neutral Weyl fermion.

So the clause and a covariant star term, one Admissibility neighbourhood
wide, give chiral Majorana bands on a supplied record pattern. This is the
first chiral content the campaign has found from covariant operators. The
carving and its contents are fine-tuned.
- **Dangling fields.** Fields on every dangling axis leave the chiral bands
  in place, still with Chern number −1. But they turn the 12 zero modes
  into bands that carry the opposite Chern number, +1, so the total
  cancels. Fields on some pairs of axes keep the total at −1.

## Setting and decision points

- **The clause.** The compass point of the fully soldered clause (open PR
  9040; D-dyn, D-sold), with records acting as fields (open PR 9041).
- **The carving (D-pattern, supplied, not covariant).** A 19-site relaxed
  network on the 4x4x4 cell, spanning all three directions, from open PR
  9097's zero-field search:

      (0,0,0) (0,0,1) (0,1,0) (0,1,3) (0,2,3) (1,0,1) (1,0,2) (1,1,2)
      (1,1,3) (1,3,1) (2,1,2) (2,2,1) (2,2,2) (2,3,0) (2,3,1) (3,0,0)
      (3,2,3) (3,3,0) (3,3,3)

  It has 22 bonds, one local loop per cell and three windings, with 13
  dangling axes.
- **The record contents (D-pattern, supplied, not covariant).**
  - Each record points along the last axis that avoids its unrecorded
    neighbours. That is possible because none touches them along all three
    axes.
  - Its sign is `(−1)^(x+y+z)`, staggered.
  - Every field on an unrecorded site vanishes.
- **The star term (D-chir, extended to weight at most seven).**
  - It is a covariant odd star term under full soldering: a sum over lattice
    sites of Pauli strings on the site and its six neighbours, invariant
    under the 24 proper rotations acting on positions and spins together.
  - The particular term is chosen for being free on the supplied carving.
- **Kitaev's representation** (prior art: Kitaev 2006).
  - `σ^a = i b^a c`, with the physical constraint `b^x b^y b^z c = 1`.
  - So `σ^a = −i b^{a+1} b^{a+2}` on the physical space.
  - Bonds pair into gauge fields, `b_j b_k = −i u_jk`.

None is adopted.

## Theorem 1 — the carving and its zero-field records

The network is connected with winding rank 3, and keeps at most one bond per
axis at each site. Every record touches unrecorded sites along at most two
axes. With the stated contents, the field of every record on every
unrecorded neighbour is exactly 0. ∎

## Theorem 2 — covariant odd star terms as signed orbits

Under full soldering, a proper rotation maps a Pauli string on the star to
plus or minus another. So the covariant terms are the orbit sums with
consistent signs, and an orbit whose stabilizer reverses a sign vanishes.
The runner counts lattice terms, placing weight-one fields at the centre:
- weights 1 and 3 give 37, open PR 9088's full-soldering count;
- weights 1, 3, 5 and 7 give 325.

At the level of the star alone there is one more orbit each, 38 and 326.
It is the radial field `Σ_a (σ^a_{+a} − σ^a_{−a})` on the six neighbours,
which sums to zero over the lattice. ∎

## Theorem 3 — exact Majorana images

For each Pauli string on the carving, the runner inserts the physical
constraint on a subset of its sites and pairs every `b` on a kept bond with
its partner. What remains is a free term if at most two Majoranas are left,
`c`'s or dangling `b`'s. The runner tracks every sign.
- **Bonds.** The map reproduces the network's bond matrix exactly.
- **Three-site clusters.** On 12 random three-site clusters, the spin
  spectrum equals one parity sector of the Majorana spectrum to 5e-15.
  Each cluster has bonds, Kitaev's pattern with a random coefficient, and
  random dangling fields.
- **Multi-site strings.** The same holds, to 1e-14, on 30 random tree
  clusters of up to six sites. Their terms include products of two or three
  bonds and fields.
- **Free and not free.** Kitaev's pattern is a free same-class bilinear, and
  a kept-axis field is not free. ∎

## Theorem 4 — a covariant term with a same-class image

Place every covariant term at every lattice site, and replace its factors on
recorded sites by the record values.
- **The free subspace.** The terms whose reduced strings are all free form a
  41-dimensional subspace of the 325. Only 5 of its directions act on the
  Majoranas of this carving; the rest reduce to nothing or to constants.
- **The term.** Project onto it the orbit of the weight-5 string
  `σ^x_{+x} σ^y_{−x} σ^y_{+y} σ^z_{−y} σ^z_{+z}`, on five neighbours of a
  centre. The projection is a covariant term built from 23 orbits of
  weights 5 and 7.
  - Its non-free reduced strings cancel exactly, to 1e-15.
  - Its free image is 27 Kitaev patterns at corners of the carving, which
    are same-class couplings, plus the field `σ^x` at `(2,2,2)` on a
    dangling axis. The field has the largest coefficient, −1.18.
- **Every free term acts through the same 28 strings.** No free covariant
  term couples the other 12 dangling `b` Majoranas. So on this carving the
  12 zero modes per cell of Theorem 5 cannot be removed by any free
  covariant star term of weight at most seven. ∎

## Theorem 5 — the chiral phase

Add `λ` times that term to the compass-point bonds. In each of the 16
translation-invariant flux sectors of the 4x4x4 cell the model is free
Majoranas.

| `λ` | lowest sectors | next sector (6³ grid) | zero modes per cell | gap above them | weak Chern numbers |
|---|---|---|---|---|---|
| 1 | 8 of 16 | +0.012 | 12 | 0.0190 | (−1, 0, 0) |
| 2 | 8 of 16 | +0.024 | 12 | 0.0351 | (−1, 0, 0) |
| 4 | 8 of 16 | +0.039 | 12 | 0.0174 | (−1, 0, 0) |

- **The Chern numbers.** The one on planes normal to `x` is −1 in every
  lowest sector. In the first it is −1 on four `k_x` planes, and 0 on four
  `k_y` and four `k_z` planes. The gaps are refined minima over the
  Brillouin zone of the bands above the exact zero modes.
- **Where the chirality forms.** At `λ = 0` the network is gapped (0.78)
  above 16 flat zero modes per cell: 3 from an imbalance of `c`'s between
  the classes, and 13 dangling `b`'s. The term couples the three `c` zero
  modes and the field's dangling `b` into dispersive bands. The chiral band
  is the negative band nearest zero, and 12 dangling `b`'s stay decoupled.
- **A window.** The gap vanishes at `λ = 0.5` and at `λ = 10`, and is open at
  0.9 (0.0105) and 8 (0.0017). An independent check places the window at
  about `0.80 < λ < 8.5`. ∎

## Theorem 6 — chiral surface modes

Cut the lattice into a slab 12 cells thick, open along `z`, at `λ = 2` in
the first lowest sector. Keep `k_x = 1` and `k_y` as good momenta, and scan
`k_y` over 121 values.
- **Localization.** The in-gap states, between the zero modes and 0.8 of
  the bulk gap, sit on the two surfaces: 64 top-surface and 31
  bottom-surface states, against 4 others.
- **Chirality.** As `k_y` winds once, the top-surface states cross the
  energies −0.01 and 0.01 once each, upward. The bottom-surface states cross
  them once each, downward.

So each surface carries one chiral Majorana mode, with opposite chirality
on the two, as a Chern number of magnitude 1 on the `k_x` planes requires.
These modes sit alongside the 12 decoupled bulk zero modes per cell. ∎

## Theorem 7 — dangling fields decide the net chirality

The 12 zero modes per cell sit entirely on dangling `b` Majoranas, which the
zero-field records leave decoupled. Fields on dangling axes couple them in.
- **Fields on every dangling axis.** Give every dangling axis a field
  through the clause, with random signs and sizes between 0.5 and 1.5 times
  `ε`. Keep the star term as reduced by the zero-field contents, at
  `λ = 2`. Take `ε = 0.1` with three random draws, and `ε = 0.2`. A dangling
  `b` enters only its own field, so on 12 of the 13 axes a field's sign is
  the relabelling `b → −b`; only the sign at `(2,2,2)`, where the star
  term also acts, matters.
  - That couples the `b`'s in, leaving 2 exact zero modes per cell.
  - **The chiral bands survive.** The 12 bands grown from the zero modes
    stay below the chiral bands. Refined over the zone, they reach 0.122,
    0.079, 0.105 and 0.265, and the chiral bands start at 0.155, 0.113,
    0.138 and 0.286. The ten negative chiral bands keep Chern number −1 on
    the `k_x` planes.
  - **The zero modes compensate.** The negative bands grown from the zero
    modes carry Chern number +1 on the same planes. So all the negative
    bands together have Chern number 0. That total sits above 2 flat bands
    at exactly zero energy, across a gap of order `ε²`.
- **Fields on two axes.** Put fields of 0.1 on only two dangling axes.
  - On the z axis at `(2,1,2)` and the x axis at `(2,2,1)`, 10 exact zero
    modes remain, the other bands stay gapped at zero energy (4.7e-3 on the
    grid), and the total `C_x` stays −1.
  - On the y axis at `(0,0,1)` and the x axis at `(0,1,0)`, the total is 0.
- **Generic contents.** Open PR 9054's generic contents, a fixed direction
  projected orthogonal to kept axes, leave fields on the dangling axes.
  With them, no covariant odd star term of weight at most seven stays free
  on this carving.

So which dangling axes carry fields decides the net chirality. Fields on
all of them make the zero modes cancel it; the zero-field contents keep it,
with 12 zero modes; fields on some pairs of axes keep it too. ∎

## Theorem 8 — what fixes the handedness

- **The field is essential.** Keep only the 27 Kitaev patterns and drop the
  dangling-axis field. The gap then vanishes at `λ = 2`.
- **Time reversal.** The reduced term has only odd-weight strings, so
  `λ → −λ` is time reversal. At `λ = −2` the weak Chern numbers are
  `(+1, 0, 0)`.
- **Record signs.** With uniform instead of staggered record signs, the
  projected term gives the same gap, 0.0351 at `λ = 2`, and weak Chern
  numbers `(+1, 0, 0)`.

So the record contents set the handedness. ∎

## Theorem 9 — another free direction gives one Weyl pair

The five active free directions give other phases too.
- **The term.** Take the principal directions of the free subspace's
  action on the Majoranas: the right singular vectors of its Majorana rows,
  each signed so that its largest orbit entry is positive. Take the term
  with coefficients `(−1.928, −1.492, 4.792, −0.488, −0.316)` on them,
  found by a random search. Its largest string coefficient is 4. Add it at
  `λ = 1` to the compass bonds, in a lowest translation-invariant flux
  sector.
- **Two nodes.** The 12 zero modes stay decoupled; drop them, leaving 20
  coupled Majoranas. A search from 24 seeds finds the middle two bands
  touching at exactly two momenta, `k* ≈ (5.172, 6.197, 6.074)` and `−k*`
  (mod `2π`).
- **Weyl charges.** The lower bands carry Berry flux −1 through a small
  sphere around `k*`, and +1 around `−k*`. The touchings sit at energies
  −0.0071 and +0.0071, so each node sits in a small pocket.
- **Linear splitting.** Away from the node the splitting grows linearly,
  with slopes 0.31 to 1.39 along six directions. The slopes agree at
  `|q| = 10⁻³` and `10⁻²`.
- **Planes.** Over 13 planes, `C_x` jumps by the node charges at the nodes'
  `k_x` and is otherwise constant.

The two nodes are a particle–hole pair. The modes near `−k*` are the
conjugates of those near `k*`, so at low energy the pair is one
two-component Weyl fermion (prior art: Hermanns, O'Brien and Trebst 2015).
It is neutral. No exact U(1) counts it: the number of excitations near `k*`
is conserved only at low energy. The 12 decoupled zero modes remain beside
it. Like the rest of this note it uses the zero-field contents. What
dangling fields do to it is not computed here: the bands grown from the zero
modes then crowd the node's energy. ∎

## Exploratory results, not certified here

- **Between the phases.** At `λ = 0.5` the dispersive gap vanishes on every
  `k_x` slice from 0.39 to 2.36. So the zero-energy set spreads over a
  range of `k_x`, as a Majorana Fermi surface would, rather than at
  isolated Weyl points.
- **Doubled cells.** An independent check searched cells doubled along `x`,
  `y` and `z`, 128 sectors each.
  - At `λ = 1` the translation-invariant sector stays lowest.
  - At `λ = 2` and 4, doubling along `x` or `y` finds lower sectors, by
    9e-4 and 6e-4 per cell. They are gapped (0.040 and 0.020) with the same
    weak Chern numbers.
- **Other axis rules and carvings.**
  - The independent check found that choosing the first instead of the last
    free axis gives `(0, 0, +1)`, consistent with the carving's C2
    symmetry.
  - A coarse survey of the 16 realizable networks of open PR 9097 found
    candidates on 5. Refined checks of several showed gaps that vanish
    somewhere, with Chern numbers differing between planes.
- **Other free directions.** A random search over the five active free
  directions, with the largest string coefficient 1, 2 or 4, found coarse
  (6³-grid) gaps up to twice this term's.
  - Refined, the best gapped case has gap 0.044 and weak Chern numbers
    `(+1, 0, 0)`. Its dangling-field test also gives compensation, with
    the signs reversed.
  - Several coarse candidates were gapless when refined, with Chern numbers
    differing between `k_x` planes. One of them is Theorem 9's Weyl pair.

## What this means for the lanes

- **Chirality lane.** The clause and a covariant star term of weights five
  and seven give chiral Majorana bands on a supplied record pattern. Every
  operator in them is covariant; the carving and its zero-field contents
  are supplied and fine-tuned.
- **The ladder of the synthesis.** On this carving no covariant term of
  weight three or less is free, and weights five and seven suffice. That is
  still one Admissibility neighbourhood, like the photon's ring.
- **What stays open.**
  - The chiral fermions are neutral Majoranas in a Z2 gauge field. The
    Weyl pair of Theorem 9 is one neutral Weyl fermion, with no exact U(1)
    charge. Charged Weyl fermions remain open.
  - The spin model's ground state is extensively degenerate, from the 12
    decoupled zero modes per cell.
  - The gap is small, 0.02 to 0.035 of `|K|`.
  - Fields on every dangling axis cancel the net chirality through the
    zero modes. Which partial field patterns keep it is mapped only for
    pairs of axes.
- **Prior art.**
  - Kitaev (2006): a time-reversal-odd three-spin term gaps his model into
    a chiral phase.
  - Hermanns, O'Brien and Trebst (2015): three-dimensional Kitaev models
    with Majorana Fermi surfaces, Weyl nodes and chiral surface modes.

  Both are cited as prior art, not as premises.

## Checks

The runner has 9 checks and all pass in about two minutes.

| Check | Result |
|---|---|
| The carving | Connected, winding rank 3, 22 bonds; records touch at most 2 axes; largest field on an unrecorded site 0. |
| Covariant terms | 37 lattice terms at weights 1 and 3, 325 at weights 1 to 7. |
| Majorana images | Bond matrix exact; three-site clusters to 5e-15; 30 random tree clusters to 1e-14; the free and not-free cases. |
| The term | Free subspace 41, of which 5 act, all through the same 28 strings; 23 orbits of weights 5 and 7; non-free strings cancel to 1e-15; image of 27 Kitaev patterns plus the field at `(2,2,2)`. |
| The chiral phase | The table above. |
| Surface modes | 64 top and 31 bottom in-gap surface states, 4 others; signed crossings of ±0.01, top +1 and bottom −1. |
| Dangling fields | Zero modes all on dangling `b`'s. Fields on all 13 axes (0.1, three draws; 0.2): 2 zero modes remain, the chiral bands stay separated and keep −1, the zero-mode bands take +1, total 0. Fields of 0.1 on z`(2,1,2)` and x`(2,2,1)` only: total −1, gap 4.7e-3; on y`(0,0,1)` and x`(0,1,0)`: total 0. Generic contents leave no free term. |
| Window and handedness | Gap 3e-14, 0.0105, 0.0017 and 6e-17 at `λ = 0.5, 0.9, 8, 10`; without the field, gap 5e-18; `λ = −2` and uniform signs give `(+1, 0, 0)`. |
| Weyl pair | Coefficients `(−1.928, −1.492, 4.792, −0.488, −0.316)`: 20 coupled Majoranas; 2 touchings at `±k*`, energies ∓0.0071, charges ∓1; slopes 0.31–1.39, the same at 1e-3 and 1e-2; `C_x` jumps at the nodes. |

## Independent check

A separate checker wrote its own code without reading this runner.
- **Confirmed.**
  - It reproduced every number in the table, on grids up to 72².
  - It diagonalized the full 19-qubit spin model on the one-cell torus. The
    ground energy equals the Majorana minimum over the 16 sectors, to 9e-13
    at `λ = 1` and 4e-12 at `λ = 4`, and the second level matches too.
  - Under random perturbations within the active free directions, 56 of 60
    trials at relative size up to 0.07 stayed gapped with `(−1, 0, 0)`.
    Every gapped case had that vector.
- **Flagged, now addressed.**
  - The first version called every ingredient covariant. The carving and
    its contents are supplied, non-covariant choices.
  - It motivated the result by open PR 9097's gapless-start recipe. The
    chirality actually forms among flat zero modes of a gapped start.
  - It left out the dangling-axis field, which the gap needs.
  - It described the phase as a gap opening at small coupling. It is a
    window in `λ`.
  - The doubled-cell sectors and the content dependence are now reported.
  - The statement about pure-gauge parts was vacuous and is removed.

## Second independent check (dangling fields)

A second checker wrote its own band search and three Chern computations
(Fukui–Hatsugai, Wilson loops, and a Kubo sum). It reused only the model's
Hamiltonian.
- **Confirmed.** The four all-axis cases reproduce to four decimals, with
  zero-mode bands +1, chiral bands −1 and total 0. The same holds for six
  more draws, for `ε` from 0.02 to 5, and at `λ = 1` and 4.
- **Caveats, now stated.**
  - At `ε = 0.2` some other draws let the two band groups overlap in
    energy. Their Chern numbers stay +1 and −1.
  - The zero total is protected only by a gap of order `ε²` above 2 flat
    zero-energy bands.
  - For 12 of the 13 axes a field's sign is a relabelling.
- **Refuted and corrected.** The first version said the net chirality needs
  exactly zero dangling fields. Fields on 5 of the 66 pairs of axes keep
  the total at −1 over a range of sizes, and an odd number of fields (one or
  three) lets the bands reach zero energy. Theorem 7 now states the
  all-axis result and the pair cases.

## What this does not do

- It adopts no clause, carving, record content or star term.
- It treats one carving, one content assignment and one covariant term in
  full. Doubled cells and other contents appear only in the exploratory
  results.
- It claims no chiral phase of the full lattice, no charged fermion and no
  physical identification. The Weyl fermion of Theorem 9 is neutral and
  emergent at low energy.
