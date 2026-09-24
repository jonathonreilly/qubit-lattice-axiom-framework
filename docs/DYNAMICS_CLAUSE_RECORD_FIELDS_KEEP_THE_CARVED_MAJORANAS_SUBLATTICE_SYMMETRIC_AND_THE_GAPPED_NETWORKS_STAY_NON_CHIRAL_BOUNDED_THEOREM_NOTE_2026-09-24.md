---
claim_id: dynamics_clause_record_fields_keep_the_carved_majoranas_sublattice_symmetric_and_the_gapped_networks_stay_non_chiral_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting: the relaxed carvings of open PR 9054 at the compass point of the fully soldered clause, with records acting as fields, all supplied and none adopted. There, every record field lies on a dangling axis. (i) Give each c Majorana the parity of its site, and each dangling b Majorana the opposite parity. Every bond joins c Majoranas of neighbouring sites, and every dangling-axis field joins b^a_j to c_j. So every coupling joins opposite classes, and S = diag(+-1) anticommutes with the Bloch Hamiltonian at every momentum, in every gauge sector and for any record contents. This is certified on both networks of open PR 9054, all 24 gauge sectors, with random fields, to 0. (ii) Hence every weak Chern number of the gapped negative-energy bands vanishes (0 to 5e-16 on the planes k_a = 0 and pi, both networks, top of the negative bands -0.618). With the sublattice symmetry, generic band touchings would be lines rather than Weyl points. (iii) A leaf, meaning a site with a single kept bond along axis c, may carry a field along c while staying solvable, since sigma^c_j = -i b^a_j b^b_j on the physical space. That couples two same-class dangling Majoranas and breaks S. On a two-site leaf pair, the Majorana spectrum in one parity sector equals the exact spin spectrum to 6e-15. (iv) Adding Kitaev's time-reversal-odd pattern s^a_i s^b_m s^c_k on every bond pair of the networks breaks S, but the gap stays open up to kappa = 4 (smallest 0.13) and every weak Chern number stays 0. A Chern number changes only through a gap closing, so chiral Majorana bands in these carvings need a gapless carving, a gap-closing term or leaves. No chiral phase, Weyl node, Chern number or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_record_fields_keep_carved_majoranas_sublattice_symmetric_2026_09_24.py
---

# Record fields keep the carved Majoranas sublattice-symmetric, and the gapped networks stay non-chiral

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** a structural theorem with finite certificates on supplied models; unaudited.

## Result

Open PR 9054 carved exactly solvable three-dimensional Kitaev networks out
of the medium. Open PR 9088 found that no covariant time-reversal-odd star
term keeps a carving's Majoranas free. That left the record contents as
the natural source of chirality: record fields break time reversal and
keep the carvings solvable. This note shows they cannot make the carved
Majoranas chiral.
- **A sublattice symmetry survives.** Record fields sit on dangling axes.
  Give each `c` Majorana the parity of its site, and each dangling `b`
  Majorana the opposite parity. Then every coupling joins opposite
  classes. So a sublattice operator `S` anticommutes with the Bloch
  Hamiltonian, in every gauge sector and for any record contents.
- **So there are no Chern numbers.** With `S`, every weak Chern number of
  the gapped bands vanishes. Band touchings, if any, would be lines, not
  Weyl points. This fits open PR 9054's scan, which found every network it
  computed gapped.
- **Leaves are the one exception.** A site with a single kept bond may
  carry a field along that bond and stay solvable. That field couples two
  dangling Majoranas of the same class, so it breaks `S`.
- **Breaking `S` is not enough.** Kitaev's own time-reversal-odd pattern
  breaks `S` in both networks. Yet their gaps stay open, and every weak
  Chern number stays 0 up to `κ = 4`. A Chern number changes only when a gap
  closes, so chirality needs a gapless carving to start from.

## Setting and decision points

- **The carvings of open PR 9054.** These are the compass point of the fully
  soldered clause, with records acting as fields (open PR 9041).
  - Every unrecorded site keeps at most one bond per axis.
  - Each record is orthogonal to every axis along which its unrecorded
    neighbour keeps a bond. So record fields sit on dangling axes only.
- **Kitaev's representation.** Four Majoranas `b^x, b^y, b^z` and `c` per
  site, with `σ^a = i b^a c` and the physical constraint `b^x b^y b^z c = 1`.
  On the physical space `σ^c = −i b^a b^b` for `(a, b, c)` cyclic. Bonds give
  `−i u_jk c_j c_k`, and a dangling field gives `i h b^a_j c_j`. This is
  prior art (Kitaev 2006).
- **Chern numbers.** Chern numbers of the negative-energy bands on the
  planes `k_a = 0` and `π` of each axis, computed with the lattice method of
  Fukui, Hatsugai and Suzuki.

The clause, the carvings and the record contents are supplied decision
points. None is adopted.

## Theorem 1 — record fields keep a sublattice symmetry

Give `c_j` the class `(x + y + z) mod 2` of its site, and each dangling
`b^a_j` the opposite class.
- A bond joins `c_j` and `c_k` at neighbouring sites, so opposite classes.
- A dangling field joins `b^a_j` and `c_j`, which are opposite by
  definition.

So the Majorana coupling graph is bipartite, and `S = diag((−1)^class)`
anticommutes with the Bloch Hamiltonian at every momentum, in every gauge
sector, for any field values. The runner checks both networks of open PR
9054, all 24 gauge sectors, random record fields and random momenta: the
largest `|S H S + H|` is 0. ∎

## Theorem 2 — so the gapped bands carry no Chern number

A two-dimensional Hamiltonian with a sublattice symmetry has no Chern
invariant: `S` maps the negative-energy bundle to the positive one, which
forces its Chern number to vanish when the zero-energy bands are trivial.
This is the standard classification (prior art: Schnyder, Ryu, Furusaki
and Ludwig 2008; Kitaev 2009). In three dimensions the same symmetry makes
generic band touchings lines rather than Weyl points.

The runner computes the Chern numbers of the lowest sector's
negative-energy bands directly. On all six planes, for both networks, they
are 0 to 5e-16. The top of the negative bands is −0.618. ∎

## Theorem 3 — leaves are the exception

At a leaf `j`, with its one kept bond along `c`, a record on the far side
along `c` gives a field along the kept axis. There
`σ^c_j = −i b^a_j b^b_j`, a bilinear of the two dangling Majoranas, which
do not enter any bond. So the model stays free, but the new coupling joins
two Majoranas of the same class and breaks `S`.

The runner checks this on a two-site leaf pair with random fields along all
three axes. The free-Majorana many-body spectrum in one parity sector
equals the exact spin spectrum to 6e-15, and `|S H S + H|` reaches 12.6. The
networks of open PR 9054 have no leaves. Every site there keeps two or
three bonds. ∎

## Theorem 4 — breaking the symmetry does not by itself give chirality

Add Kitaev's time-reversal-odd pattern `κ s^a_i s^b_m s^c_k` over every site
`m` and every pair of its bonds, with `a` and `c` the bond axes and `b` the
third. Its Majorana image is a same-class hopping `u_im u_mk c_i c_k`, which
breaks `S`.

| Network | `κ` | `|S H S + H|` | smallest nonzero `|E|` | weak Chern numbers |
|---|---|---|---|---|
| 20-site | 0.2, 1, 4 | 6.8, 33.9, 135.8 | 0.541, 0.570, 0.342 | 0 |
| 16-site | 0.2, 1, 4 | 5.5, 27.7, 110.9 | 0.132, 0.432, 0.212 | 0 |

The gaps never close. A Chern number can change only when a gap closes, so
these gapped networks stay non-chiral under any time-reversal-odd
bilinear too small to close their gap. ∎

## What this means for the lanes

- **Chirality lane.** In the exactly solvable carvings:
  - covariant time-reversal-odd star terms do not keep the Majoranas free
    (open PR 9088);
  - record fields keep a sublattice symmetry, so they give no Chern number;
  - even explicit time-reversal-odd Kitaev terms leave the gapped networks
    non-chiral.
- **What chiral Majorana bands would need.**
  - A gapless carving: nodal lines, which the sublattice symmetry allows,
    then gapped by a sublattice-breaking term. That is Kitaev's own route in
    his gapless phase.
  - Or leaves with kept-axis fields, which break `S`. Their effect on Chern
    numbers is not computed here.
  - Or a term strong enough to close the gap.

  Open PR 9054's scan found no gapless network.
- **Prior art.** Kitaev (2006) gaps his model's gapless phase with the
  three-spin term into a chiral phase. Hermanns, O'Brien and Trebst (2015)
  find Majorana nodal lines and Weyl nodes in three-dimensional Kitaev
  models. Both are cited as prior art, not as premises.

## Checks

The runner has 4 checks and all pass in about 3 s.

| Check | Result |
|---|---|
| Sublattice symmetry | Both networks, all 24 gauge sectors, random fields and momenta: largest `|S H S + H|` 0. |
| Weak Chern numbers | Six planes, both networks: largest `|C|` 5e-16. Top of the negative bands −0.618. |
| The leaf exception | Spin spectrum equals one parity sector of the Majorana spectrum to 6e-15. `|S H S + H|` up to 12.6. |
| Kitaev's pattern | Symmetry broken, gaps open (smallest 0.132), Chern numbers 0 at `κ = 0.2, 1, 4`. |

## What this does not do

- It adopts no clause, carving or record content.
- It computes Chern numbers for the two networks of open PR 9054. The other
  networks of its search obey Theorem 1 but are not computed here.
- It does not search for gapless carvings or carvings with leaves, and it
  does not compute Chern numbers with leaf fields.
- It treats bilinear terms only. It claims no chiral phase, Weyl node, Chern
  number or physical identification.
