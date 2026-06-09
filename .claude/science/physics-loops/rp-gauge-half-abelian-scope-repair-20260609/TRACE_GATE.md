# Trace Gate

Target:
`rp_gauge_half_wilson_temporal_bridge_narrow_theorem_note_2026-06-06`

Blocker:
`scope_too_broad: restrict the retained claim to the abelian Z_N/U(1) surfaces, or replace W2/W3 with the correct nonabelian matrix-coefficient Peter-Weyl or explicitly projected character-kernel derivation and add a reconstruction/Gram check for that normalization.`

Repair:
This PR takes the first audit-offered path. The source theorem is now exact
only for the abelian `Z_N` and `U(1)` surfaces. SU(2)/SU(3) coefficient probes
remain visible as diagnostics, but are explicitly non-load-bearing for W2/W3.

Guard:
The runner now includes the SU(2) first-order mismatch at `g=h=i sigma_x`:
the true beta-linear coefficient of `exp((beta/2) Re Tr(g h^dag))` is 1, while
the old product-character substitution gives 0 because both fundamental
characters vanish. This prevents the old nonabelian product-character
reconstruction from silently returning.
