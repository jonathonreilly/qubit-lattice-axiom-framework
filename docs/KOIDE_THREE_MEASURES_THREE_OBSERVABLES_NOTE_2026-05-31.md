# Koide Count Readouts and Spectral-Asymmetry Bookkeeping

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** finite `C_3` count/readout bookkeeping. This note does not derive the
charged-lepton Koide value from the framework and does not prove that no selector
question remains.
**Primary runner:**
`scripts/frontier_koide_three_measures_three_observables_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_three_measures_three_observables_2026_05_31.txt`.

## Result

For the finite `C_3` circulant parameter `r=|b|^2/a^2`, the runner checks the algebraic
readout table

| weight `(mu,nu)` | extremum `r*=nu/(2mu)` | `Q=(1+2r*)/3` |
|---|---:|---:|
| democratic `(1,0)` | `0` | `1/3` |
| equal-block `(1,1)` | `1/2` | `2/3` |
| dimension `(1,2)` | `1` | `1` |

It also independently evaluates the finite spectral-asymmetry/Lefschetz weight
`L_3(1,2)=2/9` and records the bookkeeping identity
`2/9=(3-1)/3^2`.

The useful reframe is narrow: the block count and the dimension count are distinct
finite readouts, and the dimension count has a spectral-asymmetry interpretation. This
does not by itself select the charged-lepton mass-ratio readout or retire the
separate source problem for `r=1/2`.

## Boundary

This note should not be cited as a derivation of the empirical
charged-lepton sector. It only prevents one bookkeeping confusion: `Q=1` from the
dimension weight and `L_3(1,2)=2/9` are different readouts, not a competing proof that
the mass-ratio readout should be `Q=1`.

## Load-Bearing Authorities

[AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
[KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
