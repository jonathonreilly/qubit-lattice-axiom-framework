# Koide: the two records aspects are the two C3 channels — pointer (block/ratio) and relaxation (trace/asymmetry)

**Date:** 2026-05-31
**Claim type:** bounded structural grounding (positive) + ledger wall-corrections
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
**Primary runner:**
`scripts/frontier_koide_records_pointer_grounds_block_channel_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_records_pointer_grounds_block_channel_2026_05_31.txt`.

## Result (one sentence)

The native records dynamics supplies **both** `C_3` measures, one per channel: the
records **pointer** (einselection) is the 2-block grading (per-block `-> ` the **ratio**
channel, `Q=2/3`), while the records **relaxation** (dephasing `-> ` maximally-mixed) is
the full-algebra trace (per-dimension `-> ` the **asymmetry** channel, `2/9`) — so the
"per-block-vs-per-dimension ambiguity" is the records carrying a pointer and a relaxation,
which read the doublet's two complementary observables.

## The pointer is the 2-block grading (per-block counting is native)

A real, charge-conjugation-invariant environment monitors the real `C_3`-equivariant
observable `S = C + C^2`, whose spectrum is `{+2, -1, -1}` — exactly **two** eigenspaces
(singlet `+2`, doublet `-1`) (F1). The complex character lines `omega, omega^2` are
complex **conjugates**, hence carry the **same** pointer eigenvalue and are
**record-indistinguishable** by any real correlator, so they einselect together as **one**
doublet sector. The pointer therefore resolves the 2 Wedderburn **blocks**, not the 3
character dimensions — **per-block counting is native**, not an arbitrary choice.

This **sidesteps** the chiral no-go (F2): the block grading `S` **commutes** with
`Gamma_chi = 2 P_singlet - I` (co-diagonalizing the 2 blocks), never anticommutes, so
`koide_z3_equivariant_anticommuting_no_go` (which forbids *chiral/anticommuting* block
operators) does not touch it. Likewise the doublet complex structure `J = (C-C^2)/sqrt3`
commutes with `C` and is a single **fixed tensor** (not a continuous `U(1)_b`), so `C^3=I`
does not obstruct the per-block measure-`J`.

## Relaxation is the trace (the other channel)

The records **dephasing** fixed point is the maximally-mixed state `I/3` — the
full-algebra **trace** — which weights the doublet by its **dimension** `2` (F3) `-> `
per-dimension `-> ` the spectral-**asymmetry** channel. So the two native records aspects
map cleanly:

| records aspect | object | measure | channel |
|---|---|---|---|
| **pointer** (einselection) | `S = C+C^2`, 2 blocks | per-block `(1,1)` | **ratio** `Q=2/3` |
| **relaxation** (dephasing) | max-mixed `I/3`, trace | per-dimension `(1,2)` | **asymmetry** `2/9` |

## The functional fork

With block energies `(E_+, E_perp) = (3a^2, 6|b|^2)` (F4): every equal-weight functional
(geometric mean, log-sum, product) extremizes at `E_+ = E_perp -> r=1/2 -> Q=2/3` (the
per-block / ratio reading); every dimension-weighted functional extremizes at
`E_perp = 2 E_+ -> r=1 -> Q=1`; the **linear trace** is **flat** on the fixed-norm
constraint (ranks neither, matching the retained `no_go` trace-degeneracy). So the bit is
*which functional*, and the pointer-vs-relaxation split is what supplies each side.

## Wall corrections (ledger-verified)

Several walls cited against *forcing* `r=1/2` are unaudited and/or mis-targeted:
- `koide_berry_bundle_obstruction_theorem` is **unaudited** (cannot load-bear) **and**
  self-defeating as a wall against `r=1/2`: it constructs its base manifold **as** the
  `sigma=1/2` locus (`K_norm = {s in S^2 : (s.e_+)^2 = 1/2}`), i.e. takes `r=1/2` as
  *input*, then proves `c_1=0` on that locus — so it bears only on forcing the **phase**
  `delta=2/9`, not the modulus.
- `koide_a1_fractional_topology_no_go` is **unaudited** and targets the `2/9` **radian
  phase**, not `r`.
- `bae_max_entropy_..._obstruction` is **unaudited** (not retained_bounded as sometimes
  cited).
- `C^3=I` blocks only a continuous `U(1)_b` *symmetry*, not the **fixed** complex
  structure `J` the per-block measure uses (verified `[J,C]=0`).

## Boundary

This is a native **grounding** of the channel map (the records dynamics supplies both
measures), **not** a forced selection of `r=1/2`. What remains open is only whether the
pointer's equal-**energy** extremum (`r=1/2`, not just per-block *counting*) is **forced**
by a max-redundancy / quantum-Darwinism **objectivity** principle: does the binary
singlet-vs-doublet record weight the 2 sectors by **count** (`-> r=1/2`) or by Hilbert
**dimension** (`-> r=1`)? That is the single sharpest next target, and it is the
convergence point of all the panel's lenses.

## Anchors (live-ledger tiers)

retained / retained_bounded / retained_no_go: `koide_z3_equivariant_anticommuting_no_go`
(retained_bounded, scope-limited to chiral/anticommuting), `cl3_complexification_split`,
`koide_kappa_block_total_frobenius_algebraic` (retained, the `E_+=E_perp <=> Q=2/3`
extremum identity), `koide_circulant_q_two_thirds_algebraic`. Unaudited (corrected):
`koide_berry_bundle_obstruction_theorem`, `koide_a1_fractional_topology_no_go`,
`bae_max_entropy`. Complements `KOIDE_READOUT_CHANNEL_MAP_NOTE` and
`KOIDE_THREE_MEASURES_THREE_OBSERVABLES_NOTE`.
