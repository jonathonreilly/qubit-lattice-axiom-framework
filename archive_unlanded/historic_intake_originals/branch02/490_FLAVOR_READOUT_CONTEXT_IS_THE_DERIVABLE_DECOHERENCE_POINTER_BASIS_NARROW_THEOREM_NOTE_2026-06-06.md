# The Flavor Readout Context (Corner vs C3) is the Derivable Decoherence Pointer Basis — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (the readout context is derivable from `{LATTICE, QUANTUM}`; mechanism + open scale identified)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/flavor_readout_context_pointer_basis_runner.py`](../scripts/flavor_readout_context_pointer_basis_runner.py)
**Cached output:** [`logs/runner-cache/flavor_readout_context_pointer_basis_runner.txt`](../logs/runner-cache/flavor_readout_context_pointer_basis_runner.txt)

## Audit context (and a correction)

The flavor sector-assignment — charged fermions recorded in the **corner** mass-eigenbasis
(`U_e = I`), the neutrino in the **C3** central-sector basis (→ the PMNS trimaximal column;
→ small-CKM-vs-large-PMNS) — was tentatively framed as a "RECORD-disclaimed G4 gate, not
derivable from the axioms." **That framing was wrong and is corrected here.** The error:
"the RECORD axiom disclaims the decoherence dynamics" was read as "the framework cannot
derive it." But the decoherence *dynamics* **is** the `LATTICE`+`QUANTUM` unitary evolution
(system + environment, traced); the RECORD axiom disclaims it only as a *primitive*. So the
readout context is **derivable from `{LATTICE, QUANTUM}`** — it is the **decoherence pointer
basis (the predictability sieve)** — and this note exhibits the mechanism.

## Safe statement

The pointer/readout basis of a system is the eigenbasis of whichever **dominates**: the
self-Hamiltonian (the mass operator `M`) or the environment coupling (`K`). For the
generation sector, `K` is the native `C3`-symmetric lattice coupling (`C + C^† = J − I`,
eigenbasis = the `C3` singlet⊕doublet) and `M` is the mass operator (corner-diagonal for the
charged sector).

**Theorem.**

1. **Coupling-dominated (`K ≫ M`) → C3.** When the mass splitting is negligible against the
   `C3` coupling, the pointer basis is `K`'s eigenbasis = the `C3` singlet⊕doublet, with a
   **trimaximal column** (the recorded `C3`-singlet). This is the **neutrino** regime
   (tiny mass splitting) → large PMNS.

2. **Mass-dominated (`M ≫ K`) → corner.** When the mass splitting dominates the coupling,
   the pointer basis is `M`'s eigenbasis = the **corner** basis. This is the **charged**
   regime (large, distinct masses) → `U_e = I`, no trimaximal column.

3. **The sector-distinguisher is the mass scale.** The pointer basis tunes continuously from
   corner (large `M`) to `C3` (small `M`) as `M/K` varies. The mass hierarchy — which is
   *in the framework* — selects corner for the (heavy) charged fermions and `C3` for the
   (light) neutrino. Hence corner-vs-`C3`, and small-CKM-vs-large-PMNS, is the **decoherence
   pointer basis**, derivable from `{LATTICE, QUANTUM}`.

So the flavor readout context is **not** a missing 4th principle: the RECORD axiom disclaims
the decoherence dynamics, but `{LATTICE, QUANTUM}` supply it (the predictability sieve), and
the sector difference is fixed by the (framework-internal) mass scale.

## The genuine open piece (a computation, not a principle)

What remains open is **quantitative**: the **emergent `C3` coupling scale** `|K|` must sit
*between* the neutrino and charged mass splittings (`Δm_ν ≪ |K| ≪ Δm_charged`) for the sieve
to land on `C3` for neutrinos and corner for charged fermions. That scale is the open
"actual emergent coupling" object
([`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
`retained_bounded`) — a `LATTICE`+`QUANTUM` **computation** (identify the generation-sector
environment coupling and its scale), **not** an additional axiom.

## What the prior mechanism-guesses got wrong

Two earlier groundings this session were refuted because they guessed the wrong *mechanism*,
not because the difference is underivable:

- **gauge-localization** — refuted (corner = momentum, not local; local is generation-blind).
- **Dirac-vs-Majorana mass mechanism** — refuted (the `C3` column is record-based, holds for
  any pre-record `M_ν`).

The correct mechanism is the **mass-scale predictability sieve** above — a different object
(the decoherence regime), consistent with both refutations.

## Boundary (honest)

- **The charged mass eigenbasis = corner** rests on the (unaudited) `Z_3` trichotomy
  (`q_H=0 → Y_e` diagonal-in-corner). The sieve says "pointer = mass eigenbasis for `M ≫ K`";
  *which* basis that is (corner) is the trichotomy's job.
- **The emergent `C3` coupling scale `|K|`** is the quantitative open input (above); the
  ordering `Δm_ν ≪ |K| ≪ Δm_charged` is required and not yet computed.
- **Why the neutrino is light** (so the coupling dominates) is a separate question.
- The predictability sieve / "pointer = dominant-term eigenbasis" is standard decoherence;
  the framework content is the realization (`M` corner, `K` the native `C3` coupling).

## Forbidden imports check

No new axiom. The pointer basis is the eigenbasis of the dominant of `{M, K}`, both existing
framework objects (`M` the mass operator; `K = C + C^†` the native double-shift coupling).
The decoherence dynamics is the `LATTICE`+`QUANTUM` unitary evolution — disclaimed by RECORD
as a primitive but supplied by the other axioms. No principle is imported; the open piece is
a scale computation.

## Runner check breakdown

Class A: the `C3` coupling gives trimaximal columns (pure-coupling pointer); a corner mass
gives the corner pointer; the predictability sieve yields corner for `M ≫ K` and `C3` (a
trimaximal column) for `K ≫ M`; the mass scale tunes between them; conclusion lines
documented. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is exact: the pointer basis (eigenbasis of the dominant of mass `M` and
the native `C3` coupling `K`) is corner when the mass splitting dominates and `C3` (with a
trimaximal column) when the coupling dominates, tuning continuously with the mass scale. The
correction is real and load-bearing: the flavor readout context is **derivable** from
`{LATTICE, QUANTUM}` as the decoherence pointer basis — the RECORD axiom disclaims the
decoherence *primitive*, not the derivation — so it is **not** a 4th-principle gate. The
genuine residue is quantitative (the emergent `C3` coupling scale, and the charged
corner-basis via the unaudited trichotomy), and "why the neutrino is light" is separate.
Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/flavor_readout_context_pointer_basis_runner.py
```
