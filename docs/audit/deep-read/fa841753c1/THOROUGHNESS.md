# Thoroughness check

Date: 2026-11-09

Pin: `fa841753c1a6296e5ad45518375660b0f1004769`

The preserved cards are notes 1551–1737, 187 notes. A seeded draw, `Random(20261109).sample`, took 8 of them: 1563, 1586, 1598, 1625, 1646, 1659, 1676, and 1709. Each note was read again from the pin. The old card text was the comparison, not the input.

## Result

None of the eight is a repair. That matches the old cards. The open physics in those cards is still open.

Recomputed here:

- Note 1563: `exp(-1/2)` equals the printed `0.6065306597126334`. `68 exp(1/2) A_corr` equals the printed `0.014968953879175233`. `K_sum` is `K_G + K_I + K_S` and equals the printed `0.10165965950324864`. `D = n exp[-(c-K_sum)n]` is largest at the integer `n=10` and equals the printed `3.740359343746328`.
- Note 1625: under the supplied energy law, `n_d = 2` gives `r = 1` and `n_d = 1` gives `r = 1/2`. The note already withdraws the partition-ratio route.
- Note 1659: an SU(3)-equivariant projector on the adjoint is `0` or `I`, so rank 1 and rank 7 are unavailable. The note does not derive `21/4`. The runner was not executed. The old card did not execute it either.
- Note 1709: `b v_F + a v_B` is invariant, the determinant is 0, the nonzero eigenvalue is `-(a+b)`, and `d eta/dl = -(eta-1)(a + b eta)`. The coefficients `a` and `b` stay underived.

Notes 1586, 1598, 1646, and 1676 already state their own limits: `r = 1/2` is not the symmetry point, the d=3 bar memo reports no measurement, the broad sign no-go is withdrawn, and the curvature no-go is not an absolute GR no-go.

## What this does not match

The old cards also recorded ledger, manifest, and status-label bookkeeping. That bookkeeping produced no repair in this draw. The new read does not copy it.

This draw did not include notes 1716 and 1737, which are the two repairs already on `FIXES.md`.
