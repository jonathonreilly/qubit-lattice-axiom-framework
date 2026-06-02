# Koide Circulant Readout Bookkeeping Map

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** finite circulant decomposition and readout bookkeeping. This note does
not identify the interaction that reads each channel.
**Primary runner:**
`scripts/frontier_koide_readout_channel_map_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_readout_channel_map_2026_05_31.txt`.

## Result

For one finite circulant generation operator
`H=aI+bC+conj(b)C^2`, the runner checks:

- `a=Tr(H)/3` is the `C_3`-fixed singlet amplitude;
- `b=(1/3)Tr(C^{-1}H)` is the doublet amplitude;
- the pure singlet limit `b=0` gives degenerate eigenvalues and `Q=1/3`;
- the equal-block value `r=|b|^2/a^2=1/2` gives the Koide ratio `Q=2/3`;
- the finite spectral-asymmetry readout gives `L_3(1,2)=2/9`;
- changing the phase of `b` at fixed `|b|` leaves `Q` unchanged.

This is a bookkeeping map of finite readouts of the same circulant operator: singlet
scale, doublet magnitude, spectral-asymmetry weight, and phase. It is not an
identification of charged-lepton interactions or a derivation of the sector
that reads each quantity.

## Boundary

The open source question is which interaction or record mechanism reads each
finite readout in the charged-lepton lane. Until that is derived or explicitly admitted,
the channel names are bookkeeping labels, not closure.

## Load-Bearing Authorities

[AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
[KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
