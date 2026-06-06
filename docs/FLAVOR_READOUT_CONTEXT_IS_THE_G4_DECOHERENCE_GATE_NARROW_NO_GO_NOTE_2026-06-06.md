# The Flavor Readout-Context Difference (Corner vs C3) is the RECORD-Disclaimed G4 Gate — Narrow No-Go

**Date:** 2026-06-06
**Claim type:** no_go (bounded; locates the flavor sector-assignment in the axiom's disclaimed slot)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/flavor_readout_context_is_g4_gate_runner.py`](../scripts/flavor_readout_context_is_g4_gate_runner.py)
**Cached output:** [`logs/runner-cache/flavor_readout_context_is_g4_gate_runner.txt`](../logs/runner-cache/flavor_readout_context_is_g4_gate_runner.txt)

## Audit context

This session established (record-ontology lepton/quark results): charged fermions are
recorded in the **corner** mass-eigenbasis (`U_e = I`), the neutrino in the **C3**
central-sector basis (its recorded `C3`-singlet `W` is the PMNS trimaximal column); and
small-CKM-vs-large-PMNS is this readout-context misalignment. The open question is *why*
the assignment is corner-for-charged, `C3`-for-neutrino. Two natural groundings were
attacked this session and **both refuted**:

- **gauge-localization** — refuted: the corner basis is the **momentum (BZ)** basis, and a
  position-local observable is **generation-blind**
  ([`FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31`](FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md));
- **Dirac-vs-Majorana mass mechanism** — refuted: the `C3` trimaximal column is
  **record-based**, holding for any pre-record `M_ν` (even a `W`-breaking one)
  ([`PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05`](PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md)),
  not from a circulant Majorana mass.

This note locates the question precisely: it is the RECORD axiom's **explicitly disclaimed**
decoherence/sector-generation slot, and no native *sector-blind* coupling can supply it.

## Safe statement

The pointer/readout basis is the eigenbasis of the system–environment (monitoring) coupling.

**Theorem (no-go).**

1. **The readout context is axiom-disclaimed.** The RECORD axiom
   (`MINIMAL_AXIOMS_2026-06-05`) states a record "supplies **no readout context,
   decomposition, `K`/CPT structure, sector-generation rule, weighting, ...
   measurement/decoherence dynamics, ... within-sector data**." So *which* readout
   context (corner vs `C3`) applies to a sector is an **input**, not derived by the axiom.

2. **Native sector-blind couplings cannot produce the difference.**
   - A native `C3`-symmetric monitored coupling (`C + C^† = J − I`, spectrum `{2,−1,−1}`)
     einselects the **singlet⊕doublet (`C3`) partition** — ranks `(1,2)` — the **same for
     every sector**. It never yields the corner partition (`(1,1,1)`).
   - A generation-blind (gauge) coupling (`∝ I` on the generation index) einselects
     **nothing** on generations (one rank-3 block).
   So neither the `C3`-symmetric lattice coupling nor the generation-blind gauge coupling
   can give corner-for-charged and `C3`-for-neutrino: producing both requires a coupling
   that **differs by sector** (a corner-diagonal coupling for one, `C3`-symmetric for the
   other).

3. **The required sector-distinguishing input is not in the framework.** It is exactly the
   disclaimed slot of (1), and the two natural candidates that could supply it
   (gauge-localization, Dirac-vs-Majorana) are refuted (Audit context). Hence the flavor
   sector-to-readout-basis assignment — and with it the corner-vs-`C3` / small-CKM-vs-large-
   PMNS structure — is a genuine **4th-principle gate**: a sector-distinguishing decoherence
   rule, **not derivable from `{LATTICE, QUANTUM, RECORD}`**.

## Boundary (scope of the no-go)

- **Scoped to derivability from the current axioms + native sector-blind couplings.** It is
  **not** a claim that no sector-distinguishing principle can exist — only that the three
  axioms plus the `C3`-symmetric lattice and generation-blind gauge couplings do not supply
  one, and the two obvious candidates are refuted.
- **Does not foreclose a future 4th principle.** A genuine sector-distinguishing decoherence
  rule (the open "actual emergent coupling" object,
  [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
  `retained_bounded`) remains a positive route — this note marks where it must enter.
- The neutrino's unique gauge-singlet status (`ν_R = (1,1)_0`, `retained_bounded`) is surely
  *relevant* but no retained mechanism connects it to the readout basis (the two that try
  are refuted).

## No-Go Discipline Gate

**Status:** PASS for the scoped no-go (the corner-vs-`C3` assignment is not derivable from
the three axioms + native sector-blind couplings, with the two natural candidates refuted).

### N1 — Alternative route enumeration

| route | attempt | status |
|---|---|---|
| `C3`-symmetric lattice coupling | einselect the generation readout | gives `C3` for ALL sectors (ranks (1,2)); cannot give corner |
| generation-blind gauge coupling | distinguish sectors by gauge charge | generation-blind (rank-3); einselects nothing |
| gauge-localization | charged → local/corner | REFUTED (corner=momentum; local=generation-blind) |
| Dirac-vs-Majorana | neutrino → circulant `C3` | REFUTED (`C3` is record-based; holds despite `W`-breaking operator) |
| a sector-distinguishing decoherence rule | supply the readout context per sector | OPEN — the disclaimed slot; the positive route, not foreclosed |

### N2 — Wall-independence audit

The single wall is the axiom disclaimer (the readout context is an input). The
sector-blindness of the native couplings is an independent algebraic fact (ranks (1,2)
for `C3`-symmetric, (3) for gauge), not a restatement of the disclaimer.

### N3 — Hidden-wall scan

Load-bearing inputs are explicit: the RECORD-axiom disclaimer (quoted), the einselected-
partition = degenerate-eigenspace fact, and the two cited refutations. "Native", "gauge",
"decoherence" are not used as hidden retained inputs.

### N4 — Residual matching

| witness | residual | here | match? |
|---|---|---|---|
| `MINIMAL_AXIOMS_2026-06-05` | record supplies no readout context / decoherence dynamics | the disclaimed slot | yes |
| `FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED` | local is generation-blind; corner=momentum | refutes gauge-localization | yes |
| `PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR` | `C3` column is record-based, any `M_ν` | refutes Dirac-Majorana | yes |

### N5 — Rhetoric audit

"Not derivable" is scoped to `{LATTICE, QUANTUM, RECORD}` + native sector-blind couplings.
No "only/last/closes/exhausted/impossible" framing; the 4th-principle route is named open.

### N6 — Partial-closure path scan

The open positive path (a sector-distinguishing decoherence rule / the "actual emergent
coupling") is named and explicitly *not* called a new axiom — it may itself be derivable
from `{LATTICE, QUANTUM}` dynamics once the generation-sector environment coupling is
identified. This note does not foreclose it.

### N7 — Steelman

Strongest objection: the lattice dynamics (`LATTICE`+`QUANTUM`) might *derive* the
sector-distinguishing coupling (e.g. the Higgs-Yukawa breaks `C3` for charged fermions),
so the assignment could be native after all. Response: this is the open route (N6) — but
the specific Higgs/Dirac-Majorana realization is refuted (the `C3` is record-based, not
from the operator), so the welding is unbuilt; the steelman keeps the route open, it does
not supply the mechanism.

### N8 — Cross-cycle echo

Prior overclaims grounded the flavor difference in one mechanism and declared it solved
(localization; Dirac-Majorana). This note avoids that echo by recording both refutations
and keeping the 4th-principle route open rather than asserting a mechanism.

## Forbidden imports check

No new axiom. Uses the RECORD-axiom disclaimer (quoted), the einselected-partition algebra,
and two cited refutations. It *records* that a sector-distinguishing input is required and
absent — it does not import one.

## Honest auditor read

The class-A content is exact: a `C3`-symmetric coupling einselects the `(1,2)` partition
for any sector, a generation-blind coupling einselects nothing, so producing corner-for-
charged and `C3`-for-neutrino requires a sector-differing coupling — which is precisely the
RECORD-axiom-disclaimed slot, with the two natural candidates refuted this session. The
note's content is a precise **localization** of the flavor sector-assignment in the axiom's
open slot, not a solution; it keeps the 4th-principle (sector-distinguishing decoherence)
route explicitly open. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/flavor_readout_context_is_g4_gate_runner.py
```
