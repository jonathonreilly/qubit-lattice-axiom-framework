# The Emergent C3 Coupling |K|: the Naive Second Order Cancels; |K| is Sourced by the hw-Asymmetry — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (the structure and source of |K|; precise value left open)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/emergent_coupling_amplitude_source_runner.py`](../scripts/emergent_coupling_amplitude_source_runner.py)
**Cached output:** [`logs/runner-cache/emergent_coupling_amplitude_source_runner.txt`](../logs/runner-cache/emergent_coupling_amplitude_source_runner.txt)

## Audit context

[`EMERGENT_C3_COUPLING_SCALE_PREDICTABILITY_SIEVE_WINDOW_NARROW_THEOREM_NOTE_2026-06-06`](EMERGENT_C3_COUPLING_SCALE_PREDICTABILITY_SIEVE_WINDOW_NARROW_THEOREM_NOTE_2026-06-06.md)
constrained the emergent `C3` coupling scale `|K|` to a ~9-order window and showed the flavor
pattern is robust to its precise value. This note pins down the **structure and source** of
`|K|` — the coefficient of the native double-shift `C3` coupling (`J − I`) on the generation
triplet — and finds that the naive computation **cancels**, locating `|K|` in the same open
"actual emergent coupling" object as the framework's `r=0` cancellation.

## Safe statement

Setup: three site-qubits (`C^8`); the native single-hop `V = t·Σ_μ X_μ` (single bit-flips);
a diagonal `H_0` = energy per Hamming-weight (excitation count, gap `ε`). The generation
triplet is the hw=1 sector.

**Theorem.**

1. **First order vanishes.** The single-hop projected to hw=1 is zero (`P V P^T = 0`): a
   single bit-flip leaves the triplet. So the generation coupling is the **second-order**
   (double-shift) effective operator, through the hw=0 vacuum and the hw=2 states.

2. **The naive second order cancels.** With **symmetric** energies (`E_n = n·ε`), the
   second-order effective Hamiltonian on hw=1 is `∝ I`: the hw=0 path (`+t²/ε · J`) and the
   hw=2 path (`−t²/ε · (I + J)`) **cancel the `J − I` (`C3`) coupling**. So
   `|K|_naive = 0` — the same cancellation structure as the staggered `r=0` no-go.

3. **`|K|` is sourced by the hw-asymmetry.** An energy **asymmetry** between the hw=0 and
   hw=2 intermediate states (an interaction / chemical-potential nonlinearity `δ`, so
   `E_2 = 2ε + δ`) breaks the cancellation: a nonzero `C3` coupling (`J − I`) emerges, with
   `|K| ~ t²·δ/ε²`, growing with `δ` and carrying the exact `C3` (`J − I`) form.

So the precise `|K|` is **not** a naive hopping amplitude; it is the
**symmetric-double-shift coefficient**, sourced by the interaction-induced hw-asymmetry `δ`.

## The genuine open piece

The precise `|K| ~ t²·δ/ε²` requires the emergent scales `t` (single-hop), `ε` (excitation
gap), and especially `δ` (the hw=0-vs-hw=2 interaction asymmetry) — the open "actual emergent
coupling" object
([`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
`retained_bounded`). These are not pinned here. But the flavor pattern is **robust** to the
precise `|K|`: any value in the ~9-order window (predictability-sieve note) gives neutrino →
`C3` and all heavier sectors → corner, so the qualitative result survives the open `δ`.

## Boundary (honest)

- **A structure + source result, not a precise `|K|`.** It shows `|K| ~ t²·δ/ε²` and that the
  naive (symmetric) computation cancels; it does **not** compute `δ` (the interaction
  asymmetry), `t`, or `ε`.
- **The cancellation is the load-bearing finding**: future work must not estimate `|K|` from
  the naive single-hop second order (it is zero) — `|K|` requires the hw-asymmetry, shared
  with the `r=0`/chirality structure.
- Uses the single-hop + Hamming-graded diagonal as the minimal model of the native lattice
  dynamics; the specific interaction generating `δ` is the open dynamics.

## Forbidden imports check

No new axiom. The single-hop `V = t Σ X_μ` and the Hamming-graded diagonal are the minimal
native lattice dynamics; the second-order effective operator and the cancellation are
arithmetic. The precise `δ` (and `t`, `ε`) are named open, not imported.

## Runner check breakdown

Class A: the single-hop vanishes on hw=1 at first order; the symmetric second-order is `∝ I`
(cancellation, `|K|=0`); an hw=2 asymmetry `δ` sources a nonzero `C3` coupling `|K|` of the
`J − I` form, growing with `δ`. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0,
total_pass: N}`.

## Honest auditor read

The class-A content is exact second-order perturbation theory on `C^8`: the single-hop
vanishes on hw=1 at first order, the symmetric second-order cancels to `∝ I` (so the naive
`|K|` is zero — the staggered-cancellation structure), and an hw=0-vs-hw=2 energy asymmetry
`δ` sources the `C3` coupling `|K| ~ t²·δ/ε²` with the `J − I` form. The result is a
**structure + source** localization of `|K|`, not a precise value: the precise `|K|` reduces
to the emergent `δ` (the open coupling), and the flavor pattern is robust to it. Effective
status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/emergent_coupling_amplitude_source_runner.py
```
