# The Lüders Update is Record-Formation: the Conditional Expectation Forced by Durability

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. Adds no axiom, no fitted input, no audit
verdict.
**Primary runner:**
[`scripts/frontier_luders_from_record_durability_2026_06_06.py`](../scripts/frontier_luders_from_record_durability_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_luders_from_record_durability_2026_06_06.txt`](../logs/runner-cache/frontier_luders_from_record_durability_2026_06_06.txt)

---

## Role

Supplies the premise that
[LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
(audited_conditional) explicitly **assumes**: *"the note assumes the Lüders state
update and the trace/effect probability pairing as supplied."* We derive the
non-selective Lüders update **directly from the Record axiom's durability** — via
the recordable-outcome lens (a record is the realized, durable outcome).

## The derivation (runner SCORECARD 21/21 PASS)

The Record axiom ([MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)):
given a readout context with a finite central-sector decomposition `{P_k}` and a
fixed `K`/CPT conjugation, the realized outcome is recorded **durably** —
*"durable means fixed once registered: the recorded outcome does not change."*

Let the **record algebra** `A_rec` = the `{P_k}`-block-diagonal operators (those
respecting the record-sector decomposition). A **durable record** is a definite
element of `A_rec`: sector-definite, no inter-sector coherence, unchanged once
registered. The map taking a pre-record state to its record content must then:

1. **land in `A_rec`** — durability: the record is sector-definite (no
   inter-sector coherence);
2. **fix `A_rec`** — durability: a record does not change once registered;
3. **preserve the record statistics `Tr(P_k ρ)`** — the outcome probabilities.

The **unique** trace-preserving map satisfying (1)–(3) is the conditional
expectation onto `A_rec` — the **pinching**

```text
   L(ρ) = Σ_k P_k ρ P_k                        (the non-selective Lüders update)
```

— verified to be CPTP, trace-preserving, PSD-output, idempotent (`L²=L`),
`A_rec`-fixing, statistics-preserving, and to satisfy the defining
conditional-expectation trace property `Tr(L(ρ)X) = Tr(ρX)` for `X ∈ A_rec`.
**Uniqueness** is exhibited by teeth: the identity ("no update") fails durability
(output ∉ `A_rec`); a reweighted pinch fails the record statistics; a
basis-rotated pinch records a *different* decomposition (∉ `A_rec`). On the
supplied `{P_k}`, durability fixes the update form uniquely as `L`.

## Two corollaries

- **Idempotence = compositional consistency.** `L² = L` is exactly the
  "recording twice = recording once" axiom (U4) of
  [LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md)
  — now **grounded in durability** rather than posited as a measurement axiom.
- **Selective Lüders.** The selective update `σ|_P = P σ P / Tr(P σ P)` is the
  realized-sector **conditioning** of `L` on the realized outcome `P` (verified a
  valid normalized state).

## Why this is distinct

- **Not the decoherence route.**
  [RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md](RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md)
  derives dephasing by tracing out environment fragments (a decoherence model).
- **Not the measurement-axiom route.** `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY`
  derives Lüders from measurement axioms U1–U4.
- **Here:** the dephasing is forced by the Record axiom's **durability alone**, as
  the conditional expectation onto the record algebra — **model-free**, and it
  *grounds* the U4 the other route assumes.

## Scope and honest residual

- The central-sector decomposition `{P_k}` (which observable is recorded) is the
  **supplied readout context**, not derived — consistent with the Record axiom's
  stated boundary (it "supplies no decomposition"). Given `{P_k}`, durability
  fixes the update **form** uniquely as Lüders.
- This is the **non-selective** update + the selective conditioning; the
  trace/effect *probability pairing* (Born weights) is a separate matter handled
  by the framework's Born/Gleason notes, not re-derived here.
- No new axiom.

## Reprove-and-cite ledger

- **Reproven here** (finite-matrix numerics on the C₃ record sectors): `L` is the
  trace-preserving conditional expectation onto `A_rec` (CPTP, idempotent,
  `A_rec`-fixing, statistics-preserving, trace property); uniqueness via the three
  failed alternatives; idempotence = compositional consistency; the selective
  update as realized-sector conditioning.
- **Cited**: the assumed-Lüders target note
  (`luders_sequential_effect_composition_pep_bridge`); the U1–U4 route
  (`luders_rule_from_composition_consistency`); the decoherence route
  (`record_dephasing_broadcast_interface`); the Record axiom
  (`MINIMAL_AXIOMS_2026-06-05`). The conditional-expectation / pinching
  characterization is standard operator algebra (comparator).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote any note or change any
audited claim scope.

- [LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- [LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md)
- [RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md](RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
