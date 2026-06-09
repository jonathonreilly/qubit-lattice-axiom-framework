# Claim Status Certificate

## Claim

The leading canonical staggered + Wilson action-density surface has bounded action support and a conservative gauge-background-independent local J budget. After the 2026-06-09 repair, the Wilson plaquette budget is computed on the canonical Wilson surface

```text
S_W = (beta / N_c) sum_P (N_c - Re Tr U_P)
    = beta sum_P (1 - Re Tr U_P / N_c).
```

Therefore each plaquette orientation contributes at most `2 beta`, and for `d=4`, `beta=6`, `q_face=6`,

```text
J_max <= |m| + d/2 + r_W d + 2 beta q_face = |m| + 78.
```

## Status

Repair-ready for review. This is not an audit verdict and does not retag the ledger.

## Dependencies

- A1/A2 minimal lattice algebra and graph support.
- Parent RP note action carriers.
- Symmetric-canonical Wilson diagonal form.
- Bounded Wilson-surface source packet for the plaquette normalization.
- Hastings-Koma / Nachtergaele-Sims estimate, used conditionally after an exact finite-range/quasilocal Hamiltonian bridge is available.

## Remaining Frontier

The exact reconstructed Hamiltonian locality step for `H = -log(T)/a_tau` remains outside this repair. If audit requires a retained Wilson-surface bridge, that source packet is the next row to promote independently.

