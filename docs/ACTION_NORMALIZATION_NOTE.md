# Action Normalization Convention-Free Selection No-Go

**Date:** 2026-04-12; no-go repair 2026-05-26; runner certificate repair
2026-06-15
**Runner:** `scripts/frontier_action_normalization.py`
**Claim type:** no_go
**Status:** exact/bounded negative boundary for convention-free selection of
the coefficient `c` in `S = L(1 - c*f)`.

## Purpose

Earlier versions tried to explain a preferred coefficient by admitting a
lattice-field-to-Newtonian-potential map, a weak-field metric readout, and a
Poisson source normalization. Audit correctly found that those bridges were
not derived in the packet.

This repair keeps the real science already present in the runner:

The current propagator-Poisson packet does not select `c` convention-free.
It exposes a one-parameter convention family. A specific value of `c` appears
only after choosing how the lattice scalar `f`, physical potential `Phi`, and
source normalization are identified.

## No-Go Claim

Within the runner's finite propagator-Poisson model, the following routes do
not select a unique `c`:

1. **Self-consistency convergence.** The loop converges for all tested positive
   values `c in {0.1, 0.2, 0.5, 1, 2, 5, 10}`.
2. **Rescaling degeneracy.** The transformation
   `(c, G) -> (c/a, a*G)` keeps `c*G` fixed and leaves the effective product
   `c*f` approximately invariant in the cached scan.
3. **PPN gamma readout.** If one identifies `Phi = c*f/2`, then
   `g_tt = -(1 - c*f)` reads as `g_tt = -(1 - 2*Phi)` and
   `g_rr = 1 + c*f` reads as `g_rr = 1 + 2*Phi`, so `gamma = 1` for every
   positive `c` under that identification.
4. **Massive-probe deflection sanity check.** The cached massive-probe
   deflection magnitude changes with `c`; it is not a null-ray or light-bending
   channel that can select `c`.
5. **Source-normalization convention.** The apparent `c=1` and `c=2`
   representatives correspond to different choices of the `f/Phi` and Poisson
   source normalization conventions, not to a convention-free observable.

Therefore the current packet cannot prove a convention-free action
normalization theorem. It proves the negative boundary: `c` is convention-
locked unless a separate retained bridge fixes the scalar-potential and source
normalization conventions.

## Preserved Finite Facts

The committed cache `logs/runner-cache/frontier_action_normalization.txt`
now reports a real PASS/FAIL certificate:

- 21 checks for the one-dimensional positive-`c` scan: controlled loop,
  finite nonzero field, and finite radial beta diagnostic for each tested `c`;
- 2 aggregate checks that all tested positive `c` values remain controlled and
  that fixed-`G` effective coupling changes across `c`;
- 6 checks for reciprocal `(c, G)` rescaling with fixed `c*G`, including
  stability of `c*phi_max`;
- 4 analytical PPN checks showing `gamma = 1` for multiple `c` values after
  the convention `Phi = c*f/2`;
- 6 controlled scan checks along the `c = 1` line in the `(c, G)` basin;
- 3 finite-positive massive-probe deflection sanity checks.

The runner exits nonzero if any certificate check fails or if the certificate
count no longer matches the expected 42 PASS checks.

## Boundary

This row does not claim:

- derivation of the lattice `f/Phi` identification;
- derivation of the weak-field metric readout;
- derivation of Poisson source normalization;
- a convention-free preferred value of `c`;
- a null-ray or light-bending runner channel;
- any new axiom or audit verdict.

A later bridge theorem could still choose a convention and then determine a
representative `c`. That would be a separate positive result. This row only
records that the current finite runner packet does not make that choice
without an added bridge.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_action_normalization.py
```

Expected summary:

```text
TOTAL: PASS=42 FAIL=0
```
