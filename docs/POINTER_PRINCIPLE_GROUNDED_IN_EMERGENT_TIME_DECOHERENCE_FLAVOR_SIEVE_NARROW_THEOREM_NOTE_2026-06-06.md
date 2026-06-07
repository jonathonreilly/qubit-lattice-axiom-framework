# The Predictability Sieve's Energy-Monitored Pointer Principle is Grounded in the Emergent-Time Decoherence Dynamics (not admitted) — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (grounds the admitted pointer principle in the decoherence dynamics; conditional grounding)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/pointer_principle_grounded_in_emergent_time_decoherence_runner.py`](../scripts/pointer_principle_grounded_in_emergent_time_decoherence_runner.py)
**Cached output:** [`logs/runner-cache/pointer_principle_grounded_in_emergent_time_decoherence_runner.txt`](../logs/runner-cache/pointer_principle_grounded_in_emergent_time_decoherence_runner.txt)

## Audit context

The active-sector predictability sieve
[`ACTIVE_SECTOR_GROUNDED_BY_MASS_VS_K_DOMINANT_OPERATOR_SIEVE`](ACTIVE_SECTOR_GROUNDED_BY_MASS_VS_K_DOMINANT_OPERATOR_SIEVE_NARROW_THEOREM_NOTE_2026-06-06.md)
(`unaudited`) derives **large PMNS / small CKM** *given* the pointer principle — *"the
pointer/active basis is the eigenbasis of the **dominant** of {M, K}"* — but explicitly leaves
that principle as **an admitted open slot** (*"the energy-monitoring / dominant-operator pointer
principle … an open slot"*). This note **grounds** that principle in the **emergent-time
decoherence dynamics** — connecting the session's foundation (the derived time axis = the
record-count `I`-axis = the thermodynamic arrow) to the flavor-mixing prize.

## Safe statement

The `hw=1` generation triplet
([`THREE_GENERATION_OBSERVABLE_THEOREM`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md), `retained`)
carries the system energy `H_S = M + |K|(J−I)`: the **mass** `M` (corner/BZ-basis-diagonal, three
distinct eigenvalues) and the emergent `C₃` coupling `K = |K|(J−I)` (`C₃`/DFT-basis-diagonal,
carrying the singlet `W=(1,1,1)/√3`).

**Theorem (the pointer principle is grounded, not admitted).**

1. **(a) Energy-monitoring is grounded in the emergent-time structure.** `H_S` is the **generator
   of emergent-time** (the record-count `I`-axis) translation. Records accumulate along the
   `I`-axis (records = decoherence = the thermodynamic arrow), so the **durable (pointer) records
   are the `H_S` eigenstates** — the only states stationary under the record-accumulation flow. The
   environment monitors **energy** because energy generates that flow.
2. **(b) The energy-monitoring decoherence einselects the `H_S` eigenbasis.** With the environment
   coupling to the system energy (`H_int ∝ H_S ⊗ B`), the coherences between distinct `H_S`
   eigenvalues dephase (verified: max off-diagonal coherence `→ 0` in the `H_S` eigenbasis after
   evolution), leaving the `H_S` eigenbasis as the pointer/record basis.
3. **(c) The `H_S` eigenbasis IS the dominant of {M, K}.** For `|K| ≪` the mass-split it is the
   **corner** (mass) basis (three distinct eigenvalues); for `|K| ≫` the split it is the **`C₃`/DFT**
   basis (one eigenvector is the singlet `W`, max overlap `1.000` — the **trimaximal column**). This
   is precisely the sieve's principle — now **derived** from the dynamics of (a)+(b).
4. **(d) Flavor consequence (the sieve's payload).** Charged leptons (heavy → corner, `U_e=I`) and
   the neutrino (light → `C₃`, recording `W`) give `PMNS = U_e†U_ν` with a **trimaximal column** and
   `O(1)` mixing; both quark sectors (heavy → corner) give `V_CKM = U_up†U_dn = I` (**small /
   near-diagonal, no trimaximal column**). Verified.

So the predictability sieve's energy-monitored pointer principle — admitted in the sieve note — is
**grounded in the emergent-time decoherence dynamics**: energy is the `I`-axis generator, records are
its decoherence-stable eigenstates, and that eigenbasis is the dominant of `{M, K}`.

## What this advances

- The sieve moves from *"conditional on the energy-monitored pointer principle"* toward *"grounded in
  the records = decoherence = emergent-time-arrow dynamics."* The session's foundation results — the
  derived time axis (the record-count `I`-gradient) and records = decoherence (the thermodynamic
  arrow) — are exactly what supplies the grounding; the large-PMNS / small-CKM contrast inherits it.
- It replaces the **refuted** position-detection grounding (the corner basis is the *momentum* basis,
  generation-blind) with the generation-*dependent* energy sieve, now dynamically grounded.

## Boundary (honest)

- **A grounding of the pointer principle, not a derivation of the spectra.** The masses and `|K|` are
  the registered patterns (matched, not derived here); this note grounds *which basis records form
  in*, given those scales.
- **Standard decoherence model.** The einselection uses a generic energy-monitoring system-environment
  coupling (`H_int ∝ H_S ⊗ B`); the *energy*-monitoring (vs an arbitrary observable) is what (a)
  grounds in the emergent-time structure. It is a conditional grounding, not a derivation of the
  microscopic environment.
- It does **not** close the flavor sector: the `r=1/2` count-selector (the firewalled lepton pin) and
  the staggered-Dirac carrier admission are upstream and untouched.

## Forbidden imports check

No new axiom. A_min (the `hw=1` triplet; `H_S = M + K`; RECORD = the `I`-axis the energy generates) +
standard decoherence (reproduced in the runner). The emergent-time identification (energy = the
`I`-axis generator; records = decoherence) is the session's foundation, not a new import. Exact
finite-dimensional.

## Runner check breakdown

Class A: (1) `H_S` eigenbasis = corner for `M`-dominant, `C₃` (singlet `W`) for `K`-dominant; (2)
energy-monitoring decoherence einselects the `H_S` eigenbasis (coherences decay); (3) energy = the
emergent-time generator (its eigenstates are the durable records); (4) flavor payload — leptons →
PMNS trimaximal column, quarks → CKM small. Expected `runner_check_breakdown = {A: 5, B: 0, C: 0,
D: 0, total_pass: 5}`.

## Honest auditor read

The system energy `H_S=M+|K|(J−I)` generates the emergent-time (record-`I`-axis) evolution; its
eigenstates are the only states stationary under that flow, hence the durable records, and an
energy-monitoring environment dephases all other coherences (verified). That `H_S` eigenbasis is the
corner (mass) basis when `M` dominates and the `C₃`/DFT basis (carrying the singlet `W`) when `|K|`
dominates — exactly the predictability sieve's dominant-operator pointer principle, here derived from
the decoherence dynamics rather than admitted, and reproducing large-PMNS / small-CKM. The note is
honest that it grounds the pointer *principle* (not the spectra) and uses a standard energy-monitoring
decoherence model whose energy-selectivity is what the emergent-time structure supplies. Effective
status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/pointer_principle_grounded_in_emergent_time_decoherence_runner.py
```
