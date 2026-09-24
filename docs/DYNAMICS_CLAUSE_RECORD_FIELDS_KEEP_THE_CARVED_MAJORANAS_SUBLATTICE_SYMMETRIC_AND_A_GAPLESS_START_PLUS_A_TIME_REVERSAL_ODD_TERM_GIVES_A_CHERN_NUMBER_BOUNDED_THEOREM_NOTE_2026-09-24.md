---
claim_id: dynamics_clause_record_fields_keep_the_carved_majoranas_sublattice_symmetric_and_a_gapless_start_plus_a_time_reversal_odd_term_gives_a_chern_number_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting: the relaxed carvings of open PR 9054 at the compass point of the fully soldered clause, with records acting as fields, all supplied and none adopted. That note's content rule makes records orthogonal to kept axes, so every record field lies on a dangling axis. (i) Give each c Majorana the parity of its site and each dangling b Majorana the opposite parity. Every bond joins c Majoranas of neighbouring sites, and every dangling-axis field joins b^a_j to c_j, so every coupling joins opposite classes. So S = diag(+-1) anticommutes with the Bloch Hamiltonian (cells of even period) in every gauge sector and for any record contents. Certified to 0 on both networks of open PR 9054, all 24 gauge sectors, with random fields. (ii) Hence the weak Chern numbers of the gapped negative-energy bands vanish: 0 to 5e-16 on the planes k_a = 0 and pi, both networks, with negative-band tops -0.618 (20-site) and -1.437 (16-site) and flat zero bands, 2 and 4 per cell. Zero-energy band touchings, if any, would generically be lines and could carry no Chern charge. (iii) Outside the content rule, a leaf (a site with one kept bond, along axis c) could carry a field along c and stay solvable, since sigma^c_j = -i b^a_j b^b_j on the physical space. That couples two same-class Majoranas and breaks S. On a two-site leaf pair the Majorana spectrum in one parity sector equals the exact spin spectrum to 6e-15. Neither network has leaves. (iv) Kitaev's time-reversal-odd pattern s^a_i s^b_m s^c_k on every bond pair, with Majorana image -i eps_abc u_im u_mk c_i c_k, breaks S. At kappa = 0.05, 0.2, 1 and 4 two exact zero bands per cell stay at zero, the refined gap above them stays open (in the 16-site network it grows from zero, 0.034 at kappa = 0.05, as kappa splits two of its four flat bands), and every weak Chern number stays 0. (v) A gapless start changes this. The 20-site network with its dangling Majoranas decoupled (zero dangling fields) is gapless (6e-13). Kitaev's pattern at kappa = 0.3 gaps it (0.0528) with weak Chern numbers (1, 0, 0) on three planes per axis. Its records cannot all have zero fields, because 7 of them touch unrecorded sites along all three axes. (vi) A SAT search on 4x4x4 finds 16 three-direction networks in which no record touches unrecorded sites along all three axes, so zero dangling fields are realizable there; 8 of them have gapless dispersive Majorana bands. (vii) On those 16 networks, with random zero-field record contents, the covariant time-reversal-odd star terms of weight at most three (open PR 9088), with their factors on recorded sites replaced by the record values, never reduce to a free same-class bilinear. Under the trivial, sign-twist and full actions and possibility covariance, no nonzero covariant term reduces to free Majorana strings at all. Under the axis action a 2-dimensional family does, and all its bilinears join opposite classes. No chiral phase on a realizable carving, no covariant time-reversal-odd term with a same-class image, no Weyl node and no physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_record_fields_keep_carved_majoranas_sublattice_symmetric_2026_09_24.py
---

# Record fields keep the carved Majoranas sublattice-symmetric; a gapless start plus a time-reversal-odd term gives a Chern number

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** a structural theorem with finite certificates on supplied models; unaudited.

## Result

Open PR 9054 carved exactly solvable three-dimensional Kitaev networks out
of the medium. Open PR 9088 found that no covariant time-reversal-odd star
term keeps a carving's Majoranas free. That left the record contents as a
natural source of chirality: record fields break time reversal and keep the
carvings solvable. This note settles what they do, and what chirality in
the carvings needs instead.
- **A sublattice symmetry survives.** Under open PR 9054's content rule,
  record fields sit on dangling axes.
  - Give each `c` Majorana the parity of its site, and each dangling `b`
    Majorana the opposite parity. Then every coupling joins opposite
    classes.
  - So a sublattice operator `S` anticommutes with the Bloch Hamiltonian,
    in every gauge sector and for any record contents.
- **So the gapped bands carry no weak Chern number.** On the planes
  `k_a = 0, π`, `S` together with particle–hole symmetry forces it to zero,
  flat zero bands and all.
- **Breaking `S` is not enough.** Kitaev's own time-reversal-odd pattern
  breaks `S` in both networks. Yet two flat zero bands per cell stay at zero,
  the gap above them stays open, and every weak Chern number stays 0, at
  every `κ` computed up to 4.
- **A gapless start changes this.** Decouple the 20-site network's dangling
  Majoranas (zero dangling fields) and its Majorana bands become gapless.
  Kitaev's pattern then gaps them with a nonzero weak Chern number,
  `(1, 0, 0)`.
  - That network's records cannot all have zero fields.
  - A SAT search finds 16 other three-direction networks whose records can,
    and 8 of them are gapless.
- **Covariance does not supply the missing piece.** On those 16 networks,
  the covariant time-reversal-odd star terms, reduced by the records, never
  give a free same-class bilinear.

So chiral Majorana bands in the carvings need three ingredients together:
- a gapless start: zero dangling fields, realizable on some networks;
- a same-class time-reversal-odd bilinear: Kitaev's pattern supplies one,
  but no covariant star term of weight at most three does, even with record
  reductions;
- a realizable carving where the two combine into a gapped phase.

Only the first is realizable with covariant ingredients here.

## Setting and decision points

- **The carvings of open PR 9054.** These are the compass point of the fully
  soldered clause, with records acting as fields (open PR 9041).
  - Every unrecorded site keeps at most one bond per axis.
  - The content rule makes each record orthogonal to every axis along which
    its unrecorded neighbour keeps a bond. So record fields sit on dangling
    axes only.
- **Kitaev's representation** (prior art: Kitaev 2006).
  - There are four Majoranas `b^x, b^y, b^z` and `c` per site, with
    `σ^a = i b^a c` and the physical constraint `b^x b^y b^z c = 1`.
  - On the physical space `σ^c = −i b^a b^b` for `(a, b, c)` cyclic.
  - Bonds give `−i u_jk c_j c_k`, and a dangling field gives
    `i h b^a_j c_j`.
- **Chern numbers.** The Chern numbers of the negative-energy bands, on
  planes of fixed `k_a`, are computed with the lattice method of Fukui,
  Hatsugai and Suzuki. Exact zero modes are excluded.

The clause, the carvings, the record contents and the time-reversal-odd
pattern are supplied decision points. None is adopted.

## Theorem 1 — record fields keep a sublattice symmetry

Give `c_j` the class `(x + y + z) mod 2` of its site, and each dangling
`b^a_j` the opposite class.
- A bond joins `c_j` and `c_k` at neighbouring sites, so opposite classes.
- A dangling field joins `b^a_j` and `c_j`, which are opposite by
  definition.

So the Majorana coupling graph is bipartite, and `S = diag((−1)^class)`
anticommutes with the Bloch Hamiltonian at every momentum, in every gauge
sector, for any field values. The cells are 4x4x4, an even period, so `S`
does not depend on momentum. On an odd period it would shift momentum by
`π`. The runner checks both networks, all 24 gauge sectors, random record
fields and random momenta: the largest `|S H S + H|` is 0. ∎

## Theorem 2 — so the gapped bands carry no weak Chern number

Both networks carry flat zero bands, 2 and 4 per cell, on both classes.
- `S` maps the negative-energy bands onto the positive ones, so their Chern
  numbers are equal, `C₊ = C₋`.
- On the planes `k_a = 0` and `π`, particle–hole symmetry
  `H(k)* = −H(−k)` maps them onto each other with the opposite sign,
  `C₊ = −C₋`.
- Together, `C₋ = 0`, with no condition on the zero bands.

This is the standard classification (prior art: Schnyder, Ryu, Furusaki
and Ludwig 2008; Kitaev 2009). With `S`, zero-energy band touchings, if
any, would generically be lines, and they could carry no Chern charge.

The runner computes the Chern numbers directly: 0 to 5e-16 on all six
planes for both networks. The negative bands top out at −0.618 (20-site)
and −1.437 (16-site). ∎

## Theorem 3 — leaves, outside the content rule

At a leaf `j`, with its one kept bond along `c`, a record on the far side
along `c` would give a field along the kept axis. The content rule of open
PR 9054 forbids it. But at a leaf that field keeps the model free:
`σ^c_j = −i b^a_j b^b_j` is a bilinear of the two dangling Majoranas, which
enter no bond. The rule's criterion, that a field along a kept axis breaks
solvability, does not hold at leaves. The new coupling joins two Majoranas
of the same class, so it breaks `S`.

The runner checks a two-site leaf pair with random fields along all three
axes. The free-Majorana many-body spectrum in one parity sector equals the
exact spin spectrum to 6e-15, and `|S H S + H|` reaches 12.6. Neither
network of open PR 9054 has leaves: every site keeps two or three bonds. ∎

## Theorem 4 — breaking the symmetry does not by itself give chirality

Add Kitaev's time-reversal-odd pattern `κ s^a_i s^b_m s^c_k` over every site
`m` and every pair of its bonds, with `a` and `c` the bond axes and `b` the
third. Its Majorana image is `−i ε_abc u_im u_mk c_i c_k`, a same-class
hopping, so it breaks `S`.

| Network | `κ` | refined gap above the zero bands | weak Chern numbers |
|---|---|---|---|
| 20-site | 0.05, 0.2, 1, 4 | 0.612, 0.541, 0.569, 0.341 | 0 |
| 16-site | 0.05, 0.2, 1, 4 | 0.034, 0.132, 0.431, 0.210 | 0 |

Two exact zero bands per cell stay at zero throughout. In the 16-site
network the gap grows from zero, because `κ` splits two of its four flat
bands.
- **What follows.** Along any path on which the dispersive gap stays open
  and the flat bands stay at zero, the Chern numbers stay 0.
- **What chirality needs instead.** The gap must vanish somewhere, the flat
  zero bands must split, or leaf fields must enter.
- **Not general.** Terms that split the flat bands need a direct
  computation. An independent check found other time-reversal-odd terms
  that split them and sometimes make the gap vanish at weak coupling. All
  of its gapped cases still had Chern number 0. ∎

## Theorem 5 — a gapless start plus Kitaev's pattern gives a Chern number

Remove the dangling fields of the 20-site network, so its dangling
Majoranas decouple as exact zero modes. Its `c` Majoranas are then gapless:
the refined minimum of `|E|` is 6e-13. Add Kitaev's pattern at `κ = 0.3`
in its lowest gauge sector:
- the spectrum is fully gapped, with a refined gap of 0.0528;
- the weak Chern numbers are `(1, 0, 0)`, on three planes per axis
  (`k_a = 0.4, 1.9, 3.5`).

So a gapless start plus a same-class time-reversal-odd bilinear gives the
carved Majoranas a Chern number, with chiral Majorana surface modes on
surfaces parallel to `x`.

That start is not realizable by records on this network. Seven of its
records touch unrecorded sites along all three axes, so no record content
can avoid them all. ∎

## Theorem 6 — where zero dangling fields are realizable

Search the 4x4x4 carvings in which no record touches unrecorded sites along
all three axes. Then each record can point along an axis that avoids its
unrecorded neighbours, and every dangling field is zero. A SAT search
finds 16 distinct three-direction networks in 3000 solutions. Their
decoupled `c` Majoranas are:
- gapless for the 16- and 18-site networks, 8 of the 16;
- gapped for the 19- and 20-site ones.

In the cases computed so far, Kitaev's pattern leaves the gapless ones
gapless at `κ` between 0.3 and 2, rather than opening a gapped Chern
phase. That computation is exploratory and not certified here. ∎

## Theorem 7 — covariance does not supply a same-class bilinear

Take the covariant time-reversal-odd star terms of weight at most three,
under each landed action and under possibility covariance (open PR 9088).
Place one at every site of the 4x4x4 torus, and replace its factors on
recorded sites by the record values. The records are given random zero-field
contents: each points along a random axis that avoids its unrecorded
neighbours, with a random sign.

The result is a sum of Pauli strings on the carving. Kitaev's
representation decides which strings are free: gauge-invariant bilinears
in the Majoranas, possibly after inserting `b^x b^y b^z c = 1` on their
sites. The runner computes that criterion exactly. It confirms that
Kitaev's pattern is free and same-class, that a bond and a dangling field
are free and opposite-class, and that a kept-axis field is not free.

The free covariant subspace consists of the terms whose every reduced
string is free.

| Covariance | free subspace dimension | same-class bilinears in it |
|---|---|---|
| trivial | 0 | 0 |
| sign twist | 0 | 0 |
| axis | 2 | 0 |
| full | 0 | 0 |
| possibility | 0 | 0 |

These hold on each of the 16 networks. So no covariant star term of this
weight gives the carved Majoranas the same-class coupling that Theorem 5
needs. ∎

## What this means for the lanes

- **Chirality lane.** In the exactly solvable carvings:
  - covariant time-reversal-odd star terms do not keep the Majoranas free
    (open PR 9088);
  - record fields under the content rule keep a sublattice symmetry, so
    they give the gapped bands no weak Chern number;
  - Kitaev's time-reversal-odd pattern alone leaves the gapped networks
    non-chiral;
  - a gapless start with that pattern gives weak Chern number 1.
- **What a chiral carved phase needs.**
  - A realizable gapless carving, which exists (Theorem 6).
  - A same-class time-reversal-odd bilinear that covariance allows. At
    weight at most three there is none, even with record reductions
    (Theorem 7). Longer star terms, other covariances or interacting
    routes remain open.
  - The two meeting in a gapped phase, which is not found yet.
- **Prior art.** Kitaev (2006) gaps his model's gapless phase with the
  three-spin term into a chiral phase. In three dimensions, breaking the
  sublattice symmetry on nodal lines generically leaves Weyl points rather
  than a full gap (Hermanns, O'Brien and Trebst 2015). Both are cited as
  prior art, not as premises.

## Checks

The runner has 7 checks and all pass in about 45 s.

| Check | Result |
|---|---|
| Sublattice symmetry | Both networks, all 24 gauge sectors, random fields and momenta: largest `|S H S + H|` 0. |
| Weak Chern numbers | Six planes, both networks: largest `|C|` 5e-16. Tops −0.618 and −1.437; flat zero bands 2 and 4 per cell. |
| Leaves | Spin spectrum equals one parity sector of the Majorana spectrum to 6e-15. `|S H S + H|` up to 12.6. |
| Kitaev's pattern | The table in Theorem 4: two zero bands per cell kept, gaps open, Chern numbers 0. |
| A gapless start | Gap 6e-13 at `κ = 0`, 0.0528 at `κ = 0.3`; weak Chern numbers `(1, 0, 0)`. Seven records touch three axes. |
| Realizable zero fields | 16 networks; 8 gapless, sizes 16 and 18. |
| Covariant reductions | 16 networks, random zero-field contents: free covariant dimensions 0, 0, 2, 0, 0; same-class bilinears 0. |

## Independent check

A separate checker wrote its own code without reading this runner.
- **Confirmed.**
  - Its construction reproduces open PR 9054's energies and gaps.
  - The sublattice symmetry is exact in all sectors, with fully random
    gauge fields, and on a 2x2x2 supercell.
  - The Chern numbers vanish on 24² and 40² grids in every sector.
  - The leaf identity is exact on the physical space.
  - The Majorana image of the three-spin term is exact for all six axis
    pairs.
  - The refined gaps match, as do the Chern numbers from κ = 0.05 to 4.
- **Flagged, now addressed.**
  - The first version said record fields cannot make the Majoranas chiral.
    It is now scoped to the content rule, with leaves outside it.
  - The flat zero bands were left implicit. They are now stated, and the
    Chern argument uses particle–hole symmetry, so it needs no condition on
    them.
  - Band touchings are now scoped to zero energy.
  - The gap statements now use refined minima and state that the 16-site
    gap grows from zero.
  - "Chirality needs a gapless carving" was too narrow. Theorem 4 now lists
    the three ways, and Theorem 5 shows one.

## What this does not do

- It adopts no clause, carving, record content or time-reversal-odd term.
- It computes Chern numbers for the two networks of open PR 9054 and, with
  zero fields, for the 20-site one. The other networks obey Theorem 1 but
  are not computed.
- It finds no gapped chiral phase on a carving whose records can realize
  zero fields.
- It finds no covariant time-reversal-odd term of weight at most three with a
  same-class image. Longer terms are not treated.
- It claims no chiral phase, Weyl node or physical identification.
