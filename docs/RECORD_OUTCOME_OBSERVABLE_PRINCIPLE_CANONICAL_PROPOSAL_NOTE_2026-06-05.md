# The Record-Outcome Observable Principle — Canonical Methodology (Proposal)

**Date:** 2026-06-05
**Claim type:** meta (methodology principle, proposed for audit adoption)
**Status:** unaudited candidate. This note *proposes* a canonical reading of the
RECORD axiom for use across lanes; per the convention-adoption precedent
(`CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08`,
`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10`), adoption is decided
by the independent audit lane, not self-declared here.
**Primary runner:** [`scripts/record_outcome_observable_principle_runner.py`](../scripts/record_outcome_observable_principle_runner.py)
**Cached output:** [`logs/runner-cache/record_outcome_observable_principle_runner.txt`](../logs/runner-cache/record_outcome_observable_principle_runner.txt)

## Purpose

To state, once and citably, the reading of the RECORD axiom that several lanes have
been using implicitly: **physical observables are recorded outcomes, i.e. central
sectors of the readout context — so an observable is derived by showing what gets
recorded, not by forcing the pre-record operator into a specific form.** The first
fully worked instance is the PMNS trimaximal column
([`PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md`](PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md)).

## The axiom this rests on

`MINIMAL_AXIOMS_2026-06-05` (RECORD), verbatim:

> "Given a readout context with a finite central-sector decomposition and a fixed
> `K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized
> central sector. ... A record supplies no readout context, decomposition, `K`/CPT
> structure, sector-generation rule, weighting, normalization, probability,
> measurement/decoherence dynamics, ... within-sector data, or occupancy rule."

The principle below is the **outcome-structure** content of this axiom — what an
outcome *is* — and nothing more. It does **not** invoke the disclaimed pieces
(decoherence dynamics, weighting, within-sector data, sector-generation rule).

## The principle

Let a readout context provide a finite central-sector decomposition: orthogonal
projectors `{P_k}` with `sum_k P_k = I`. Define the **record map** on operators

```text
D(M) = sum_k P_k M P_k.
```

Then, as a reading of the RECORD axiom's outcome structure:

1. **Observables are central-sector structure.** What is recorded — and hence
   physical — is which central sector is realized and the central-sector overlaps of
   reference (e.g. flavor) states `tr(P_k rho)`. These are fixed by `{P_k}` alone.

2. **Pre-record inter-sector coherence is not recorded.** Two pre-record operators
   that differ only by inter-sector (`P_j · P_k`, `j != k`) coherence have the
   identical record `D(M)`. So that coherence is not an observable, and a pre-record
   operator need not be forced to be block-diagonal: `D` makes it so.

3. **Within-sector data is not recorded.** `D` preserves each block `P_k M P_k`
   verbatim; the within-sector content (and any observable it sets) is left free by
   the record, to be matched to experiment rather than derived from the partition.

## The recipe (how to use it in a lane)

To derive a partition-level observable in any lane:

1. **Fix the algebra and its symmetry** (e.g. `M_3(C)` with the `C_3` generation
   structure). This must be retained/derived, not assumed.
2. **Identify the central-sector decomposition `{P_k}`** (the einselected partition),
   *and name the predicate it is modulo* (typically `K`-reality, which fixes the
   coarseness — see the named-predicate guardrail).
3. **Read the observable off the record:** the central-sector overlaps `tr(P_k rho)`
   are the prediction. Pre-record coherence is washed out (step 2 of the principle);
   do not force the pre-record operator.
4. **Declare within-sector observables free/matched** (step 3 of the principle), not
   derived — unless a separate pre-record argument supplies them.

## What the principle does NOT license (guardrails)

This is the load-bearing scope. The principle is an *outcome-structure* statement, not
a license to skip work:

- **Decomposition-input guardrail.** `{P_k}` is not invented by the recipe; a
  different valid decomposition gives different overlaps. It must come from the
  algebra + symmetry (retained) plus the partition predicate. Asserting a convenient
  `{P_k}` to get a desired answer is circular and forbidden.
- **Named-predicate guardrail.** A coarser and a finer partition are
  both complete/orthogonal; which one is the readout context is fixed by a predicate
  (for the `C_3` flavor algebra this is `K`-reality, which selects the 2-block
  singlet⊕doublet over the 3-mode split). That predicate must be named and tracked;
  on `origin/main` `K`-reality is an **admitted** residual (the standing
  `delta=0`/chirality pin), not derived.
- **Within-sector-free guardrail.** Weights/measures inside a
  sector (e.g. the Koide block-weight `r`, the solar/`theta_13` angles) are *not* the
  record's content. The principle gives the partition-level structure only; conflating
  it with within-sector data is an overreach.
- **No-dynamics guardrail.** The axiom supplies that the outcome *is* a
  central sector; it disclaims the decoherence *process* that produces it. A dynamical
  derivation (quantum-Darwinism-style) that the record *must* form on a given partition
  is a separate, currently `unaudited` task, and is not invoked by this principle.

## Derivability (is the principle repo-native?)

| element | status |
|---|---|
| "observable = recorded central sector; inter-/within-sector coherence not recorded" | **RECORD axiom, verbatim** (outcome structure) |
| the record map `D(M) = sum P_k M P_k` realizing it on operators | elementary; class-A verified |
| a specific decomposition `{P_k}` for a lane | must be **retained/derived** per lane (decomposition-input guardrail) |
| which coarseness (the partition predicate) | **modulo a named predicate** (e.g. `K`-reality, admitted) (named-predicate guardrail) |
| a dynamical derivation of record formation | **open / unaudited** (no-dynamics guardrail); not used here |

**The principle itself adds no axiom.** It is the outcome-structure reading of the
existing RECORD axiom. Each *application* must still (i) supply a retained algebra,
(ii) supply and name the partition predicate, and (iii) restrict its claim to
partition-level observables. With those, a partition-level observable is repo-native
modulo the named predicate; without them, the principle is not a shortcut.

## Worked instance

`PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NOTE_2026-06-05`: algebra =
`M_3(C)` with retained `C_3` (decomposition-input guardrail satisfied); predicate =
`K`-reality selecting the singlet⊕doublet partition (named-predicate guardrail);
observable = the singlet sector's corner overlap
`|<corner|W>|^2 = 1/3` = the **trimaximal PMNS column**; the pre-record DM-neutrino
operator that breaks `W` records to the same column (principle step 2); `theta_13` is
within-sector and stays free (within-sector-free guardrail). The Koide block-weight
`r` is explicitly *not* delivered (within-sector-free guardrail), and no
decoherence-dynamics derivation is claimed (no-dynamics guardrail).

## Runner check breakdown

Class A finite-dimensional algebra: `D` is an idempotent trace-preserving dephasing
channel; it drops inter-sector coherence and preserves within-sector blocks; two
operators differing only in inter-sector coherence record identically; central-sector
overlaps are `{P_k}`-fixed and `M`-independent; within-sector variation leaves them
unchanged; the `C_3` instance gives `1/3`; and the two guardrails (different
decomposition -> different overlaps; coarser/finer both valid -> predicate needed) are
exhibited. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The runner is abstract class-A algebra confirming the outcome-structure claims and the
guardrails. The note's only assertion is the outcome-structure reading of the RECORD
axiom plus a usage discipline; it deliberately under-claims, routing every substantive
ingredient (the decomposition, the partition predicate, within-sector data, the
dynamical process) to per-lane derivation or named admissions via the guardrails. It
introduces no axiom and no import. Whether to adopt this as the canonical methodology
statement — and whether the guardrails are tight enough — is for the independent audit
lane to decide; effective status remains `unaudited` until then.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/record_outcome_observable_principle_runner.py
```
