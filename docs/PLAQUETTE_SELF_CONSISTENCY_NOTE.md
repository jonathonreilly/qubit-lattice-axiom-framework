# Plaquette Self-Consistency Finite MC Diagnostic

**Date:** 2026-04-15; finite-diagnostic repair 2026-05-25
**Status:** bounded-support finite Wilson-plaquette diagnostic. The canonical infinite-volume value `0.5934` is an admitted comparison/reuse number here, not a value derived by this note.
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_plaquette_self_consistency_finite_mc_repair.py`

## Actual claim

For a finite periodic `L^4` lattice with `SU(3)` link variables and Wilson single-plaquette action

```text
S_W[U; beta] = (beta / 3) sum_P (3 - Re Tr U_P),
```

the average plaquette

```text
P_bar(U) = (1 / N_P) sum_P Re Tr U_P / 3
```

is a well-defined bounded observable of the finite compact configuration space. A Monte Carlo runner can evaluate finite-volume diagnostics of this observable at `beta = 6`, and those diagnostics are not fit parameters.

That is the entire repaired claim.

## What changed

The earlier row mixed a true finite same-surface statement with a stronger unresolved physical readout:

- true finite statement: `P_bar` is a unique observable of the finite Wilson partition function once `beta`, lattice size, action, and measure are selected;
- unresolved physical readout: the canonical `0.5934` value at the physical `beta=6` surface is not derived analytically here and is not certified here by a completed same-surface MC campaign.

This repair keeps the finite observable/diagnostic theorem and withdraws the stronger value-closure language. The canonical value `0.5934` may still be used by downstream notes only as an admitted comparison/reuse number unless a separate retained MC certificate or analytic beta=6 closure is supplied.

## Finite theorem

Fix:

- finite periodic lattice size `L`;
- gauge group `SU(3)` on each oriented link;
- Wilson single-plaquette action at a specified `beta`;
- compact Haar product measure over all links.

Then:

1. the finite configuration space is compact;
2. `S_W[U; beta]` is real and finite for every configuration;
3. the finite partition function `Z_L(beta)` is finite and positive;
4. `P_bar(U)` is bounded configuration-wise;
5. the finite expectation

```text
<P>_L(beta) = Z_L(beta)^(-1) integral P_bar(U) exp(-S_W[U; beta]) dU
```

is a unique mathematical number for the selected finite surface.

Monte Carlo is an evaluation method for this finite expectation. It does not introduce a fit parameter, but a short finite diagnostic run is not the same as an infinite-volume physical certificate.

## Runner-backed diagnostic

The paired runner verifies:

- `SU(3)` proposal construction preserves unitarity and determinant one to numerical tolerance;
- finite-lattice link and plaquette counts for `L^4`;
- Wilson action and average plaquette are finite and real on sampled `SU(3)` configurations;
- a one-plaquette Metropolis diagnostic changes the average plaquette between `beta=0` and `beta=6` in the expected direction;
- the source note explicitly withholds a derivation of the canonical `0.5934` readout;
- after audit-pipeline regeneration, the row is dependency-free and requeued for independent audit.

## Boundaries

This row does not claim:

- a completed same-surface MC certificate for `0.5934`;
- an analytic tensor-transfer/Perron solution for the physical `beta=6` boundary character;
- that the finite diagnostic runner is an infinite-volume extrapolation;
- that downstream uses of `0.5934` are proven by this note;
- any audit verdict or status promotion.

The remaining science target is still the real one: either ship a completed same-surface MC certificate for the physical value or derive the beta=6 boundary-character/tensor-transfer closure analytically.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_plaquette_self_consistency_finite_mc_repair.py
```
