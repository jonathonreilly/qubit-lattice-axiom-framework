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
been using implicitly: **physical observables are *registered* outcomes — central
sectors of the readout context — so an observable is established by showing what the
record registers, not by forcing a pre-record operator into a specific form.** The
first fully worked instances are the PMNS trimaximal column
([`PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md`](PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md))
and the charged-lepton Koide weight `r = 1/2`.

## Ontology (register, not read)

Reality is the record stack. The RECORD axiom: "the realized outcome is the `K`/CPT
orbit of the realized central sector." The record **registers which central sector is
realized**; it does not observe a pre-existing value. Three consequences, which the
rest of the note depends on:

- **Observables are constituted, not observed.** An observable is the *pattern of
  registrations* in the record stack — it lives *in* the stack, not behind it. There
  is no separate pre-record value sitting underneath, waiting to be measured.
- **Nothing is forced, derived, or read.** The axiom "supplies no ... weighting,
  normalization, probability ... within-sector data": so the record imposes no prior
  (nothing forced) and reflects no pre-existing magnitude (nothing read). What is
  realized is registered, faithfully.
- **Pre-record operators and states are reconstructions.** A "pre-record mass
  operator" or a "reference state `I/d`" is a calculational device used to *compute*
  what would be registered — not the reality. Treating a reconstruction (e.g. a
  reference state's value) as the registration is the realist slip this note exists to
  prevent.

## The principle

Let a readout context provide a finite central-sector decomposition: orthogonal
projectors `{P_k}` with `sum_k P_k = I`. Define the **registration map** on operators

```text
D(M) = sum_k P_k M P_k.
```

`D` is the outcome structure of registration: only the central-sector content is
registered, so

1. **Observables are central-sector structure.** What is registered is which central
   sector is realized and the central-sector overlaps of reference (e.g. flavor)
   states `tr(P_k rho)`. These are fixed by `{P_k}` (the partition), and the realized
   *weights* between sectors are the registered pattern (below).

2. **Pre-record inter-sector coherence is never registered.** Two pre-record operators
   differing only by inter-sector (`P_j · P_k`, `j != k`) coherence have the identical
   registration `D(M)`. A pre-record operator need not be block-diagonal: that part of
   it is simply not part of any record.

3. **Within-sector data is not registered at the partition level.** `D` preserves each
   block `P_k M P_k`; whatever observable that within-sector content carries is the
   registered pattern *of that sector*, matched to experiment — not handed down by the
   partition.

## The recipe (how to use it in a lane)

1. **Fix the algebra and its symmetry** (retained/derived, not assumed).
2. **Identify the central-sector decomposition `{P_k}`** (the einselected partition),
<<<<<<< HEAD
   *and name the predicate it is modulo* (typically `K`-reality, which fixes the
   coarseness — see the named-predicate guardrail).
3. **Read the observable off the record:** the central-sector overlaps `tr(P_k rho)`
   are the prediction. Pre-record coherence is washed out (step 2 of the principle);
   do not force the pre-record operator.
4. **Declare within-sector observables free/matched** (step 3 of the principle), not
   derived — unless a separate pre-record argument supplies them.
=======
   *and name the predicate that fixes its coarseness* (typically `K`-reality).
3. **Establish the partition-level observable** as the registered central-sector
   structure (overlaps `tr(P_k rho)`). Do not force the pre-record operator; its
   inter-sector coherence is not registered (principle step 2).
4. **Treat per-sector weights/magnitudes as the registered pattern**, matched to
   experiment, not derived from the partition (principle step 3, and G3 below).
>>>>>>> 6121b82e6 (science(meta): sharpen to register-not-read ontology; r=1/2 as the worked weight case)

## What the principle does NOT license (guardrails)

This is the load-bearing scope. The principle is an *outcome-structure* statement, not
a license to skip work or to slip back into realism:

- **Decomposition-input guardrail.** `{P_k}` is not invented by the recipe; a
  different valid decomposition gives different overlaps. It must come from the
  retained algebra + symmetry plus the partition predicate. Asserting a convenient
  `{P_k}` to get a desired answer is circular and forbidden.
<<<<<<< HEAD
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
=======
- **G2 — coarseness needs a named predicate.** A coarser and a finer partition are
  both complete/orthogonal; which is the readout context is fixed by a predicate (for
  the `C_3` flavor algebra, `K`-reality, selecting the 2-block singlet⊕doublet over
  the 3-mode split). That predicate must be named and tracked; on `origin/main`
  `K`-reality is an **admitted** residual (the standing `delta=0`/chirality pin).
- **G3 — per-sector weights are registered, not delivered.** The partition is
  delivered by the record; the *weight between sectors* (e.g. the Koide block-weight
  `r`) is **not**. A weight is the registered pattern of a sector — a value *in the
  record stack* like the masses, neither imposed by a prior (the axiom disclaims
  weighting) nor read from a pre-record magnitude (there is none). **Worked case:**
  `r = 1/2` is the charged-lepton registered pattern; quarks and neutrinos register
  other `r` (the dial is read off the stack, not selected). The standing error to
  avoid: computing a *reference state's* weight (the max-entropy `rho = I/3` gives
  dimension weight `(1,2) -> r = 1`) and mistaking that reconstruction for the
  registration — `I/3` is not the charged-lepton record. There is nothing to derive
  here, only to match; the framework's obligation is consistency (that `r = 1/2` is a
  registerable, stable pattern — it is the balanced/max-sector-entropy stationary
  point of the `r`-family).
- **G4 — outcome structure, not dynamics.** The axiom supplies that the outcome *is* a
  central sector; it disclaims the decoherence *process* that produces records. A
  dynamical (quantum-Darwinism-style) derivation of record formation is a separate,
  currently `unaudited` task, not invoked by this principle.
>>>>>>> 6121b82e6 (science(meta): sharpen to register-not-read ontology; r=1/2 as the worked weight case)

## Derivability (is the principle repo-native?)

| element | status |
|---|---|
<<<<<<< HEAD
| "observable = recorded central sector; inter-/within-sector coherence not recorded" | **RECORD axiom, verbatim** (outcome structure) |
| the record map `D(M) = sum P_k M P_k` realizing it on operators | elementary; class-A verified |
| a specific decomposition `{P_k}` for a lane | must be **retained/derived** per lane (decomposition-input guardrail) |
| which coarseness (the partition predicate) | **modulo a named predicate** (e.g. `K`-reality, admitted) (named-predicate guardrail) |
| a dynamical derivation of record formation | **open / unaudited** (no-dynamics guardrail); not used here |
=======
| "observable = registered central sector; inter-/within-sector coherence not registered" | **RECORD axiom, verbatim** (outcome structure) |
| the registration map `D(M) = sum P_k M P_k` realizing it on operators | elementary; class-A verified |
| a specific decomposition `{P_k}` for a lane | must be **retained/derived** per lane (G1) |
| which coarseness (the partition predicate) | **modulo a named predicate** (e.g. `K`-reality, admitted) (G2) |
| per-sector weights (e.g. `r`) | **registered/matched**, not delivered (G3) |
| a dynamical derivation of record formation | **open / unaudited** (G4); not used here |
>>>>>>> 6121b82e6 (science(meta): sharpen to register-not-read ontology; r=1/2 as the worked weight case)

**The principle itself adds no axiom.** It is the outcome-structure reading of the
existing RECORD axiom. Each *application* must still (i) supply a retained algebra,
(ii) supply and name the partition predicate, (iii) keep partition-level observables
(delivered) separate from per-sector weights (registered/matched). With those, a
partition-level observable is repo-native modulo the named predicate; without them, the
principle is not a shortcut.

## Worked instances

<<<<<<< HEAD
`PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NOTE_2026-06-05`: algebra =
`M_3(C)` with retained `C_3` (decomposition-input guardrail satisfied); predicate =
`K`-reality selecting the singlet⊕doublet partition (named-predicate guardrail);
observable = the singlet sector's corner overlap
`|<corner|W>|^2 = 1/3` = the **trimaximal PMNS column**; the pre-record DM-neutrino
operator that breaks `W` records to the same column (principle step 2); `theta_13` is
within-sector and stays free (within-sector-free guardrail). The Koide block-weight
`r` is explicitly *not* delivered (within-sector-free guardrail), and no
decoherence-dynamics derivation is claimed (no-dynamics guardrail).
=======
- **Trimaximal PMNS column (partition delivered):**
  `PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NOTE_2026-06-05`. Algebra =
  `M_3(C)` with retained `C_3` (G1); predicate = `K`-reality selecting singlet⊕doublet
  (G2); observable = the singlet sector's corner overlap `|<corner|W>|^2 = 1/3` = the
  trimaximal column, **delivered** by the partition; the `W`-breaking pre-record
  operator is a reconstruction whose inter-sector coherence is not registered
  (principle step 2). `theta_13` and the Koide `r` are *not* delivered (G3).
- **Charged-lepton Koide `r = 1/2` (weight registered):** the singlet⊕doublet
  partition is the same; `r` is the registered pattern of the charged-lepton sector
  (`r = 1/2`), not a value the partition hands down. It is matched, like the masses;
  the framework's job is to confirm `r = 1/2` is a stable registerable pattern, not to
  force it (G3). Different sectors register different `r`.
>>>>>>> 6121b82e6 (science(meta): sharpen to register-not-read ontology; r=1/2 as the worked weight case)

## Runner check breakdown

Class A finite-dimensional algebra: `D` is an idempotent trace-preserving registration
channel; it drops inter-sector coherence and preserves within-sector blocks; two
operators differing only in inter-sector coherence register identically; central-sector
overlaps are `{P_k}`-fixed and `M`-independent; within-sector variation leaves them
<<<<<<< HEAD
unchanged; the `C_3` instance gives `1/3`; and the two guardrails (different
decomposition -> different overlaps; coarser/finer both valid -> predicate needed) are
exhibited. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.
=======
unchanged; a per-sector weight (`r`) depends on the realized state, not on the
partition (the G3 separation); the `C_3` instance gives `1/3`; and the two guardrails
(G1 different decomposition → different overlaps; G2 coarser/finer both valid →
predicate needed) are exhibited. Expected `runner_check_breakdown = {A: N, B: 0, C: 0,
D: 0, total_pass: N}`.
>>>>>>> 6121b82e6 (science(meta): sharpen to register-not-read ontology; r=1/2 as the worked weight case)

## Honest auditor read

The runner is abstract class-A algebra confirming the outcome-structure claims, the
partition/weight separation, and the guardrails. The note asserts only the
register-not-read reading of the RECORD axiom plus a usage discipline; it deliberately
under-claims, routing every substantive ingredient (the decomposition, the partition
predicate, per-sector weights, the dynamical process) to per-lane derivation, named
admissions, or matched registration via the guardrails. It introduces no axiom and no
import. Whether to adopt this as the canonical methodology statement — and whether the
guardrails are tight enough — is for the independent audit lane to decide; effective
status remains `unaudited` until then.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/record_outcome_observable_principle_runner.py
```
