# Born Retention Completion Bundle: Path to Promote Born from Bounded Support to Retained Closure

**Date:** 2026-05-20
**Type:** meta (tracking + chain bundle)
**Status:** path-only tracking note; independent audit lane owns all verdicts
**Closes (proposed):** none directly — this is a bundle/tracking note
that **identifies the chain** by which
[`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md)
(`bounded_theorem`, currently bounded support) can be re-audited as
retained closure once two in-flight prerequisite PRs land.

## Purpose

This is a tracking surface, not a derivation and not an authority surface.

The Born derivation route landed in `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20`
imports five named inputs:

1. Gleason 1957 — standard math (textbook)
2. Busch 2003 / Caves-Fuchs-Manne-Renes 2004 POVM extension to dim-2 — standard math (textbook)
3. Lüders 1951 / Cassinelli-Lahti 1995 — measurement update rule
4. No-extra-structure pre-record identification — pre-record reference state
5. Persistent-record → Kraus operator identification

Inputs (1) and (2) are textbook math imports that the framework cites
as named non-derivation imports — they will remain admitted forever
(no framework-internal derivation can replace Gleason's theorem; it's
a foundational result of operator-algebraic probability theory).

Inputs (3)–(5) are framework-internal admissions that can be closed:

- (3) **Lüders** → closed by in-flight PR #1606 (`LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20`)
- (4) **No-extra-structure** → bounded support already landed via `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20`
- (5) **Record-as-Kraus** → closed by in-flight PR #1608 (`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20`)

This note identifies the chain assembly: once #1606 and #1608 land
and the audit lane retains them, the Born derivation note has 2
remaining standard-math imports (Gleason + Busch). The Born note can
then be re-audited and lifted from `bounded_theorem` support to
`retained_bounded` (with the standard-math imports as named bounded
admissions) — the framework's strongest possible Born retention given
that Gleason/Busch are textbook imports, not internal derivations.

## Chain assembly

```
                  MINIMAL_AXIOMS_2026-05-20 (retained)
                   |
                   v
        PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20
        (landed via PR #1604, bounded support)
                   |
                   v
        BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20
        (landed via PR #1604, bounded support / repair route)
                   ^
                   |  +-- LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY (PR #1606, in flight)
                   |
                   +---- PERSISTENT_RECORD_AS_KRAUS_OPERATOR (PR #1608, in flight)
                   |
                   +---- (standard math imports: Gleason 1957, Busch 2003)
```

## Promotion path

When PRs #1606 and #1608 land and reach `retained` / `retained_bounded`:

1. Each removes one named admitted input from the Born derivation chain
2. The Born note's `admitted_context_inputs` list reduces from 5 to 2
3. The remaining 2 admissions (Gleason 1957, Busch 2003) are standard
   math imports — they are inherently external textbook content, not
   framework-derivable
4. The Born note becomes eligible for re-audit at `bounded_theorem` →
   `retained_bounded` (with Gleason + Busch as named bounded
   admissions)
5. **The framework's Born-rule derivation lane retains** — closing
   the long-standing `BORN_RULE_ANALYSIS_2026-04-11.md` `audited_failed`
   problem via a structurally different repair route

## Retention ceiling

The honest ceiling for Born retention on this chain is
**`retained_bounded`**, not full `retained` (`positive_theorem`)
closure. Reason: Gleason 1957 and Busch 2003 are mainstream
foundational mathematics that the framework imports rather than
re-derives. Like Bertrand 1873 / Ehrenfest 1917 / Tangherlini 1963
in the D=3 chain, these remain named non-derivation imports
permanently.

To exceed `retained_bounded` and reach full `retained` would require
a framework-internal derivation of Gleason's theorem itself, which
is not in the scope of any current work.

## Status after expected landings

| Prerequisite | PR | Expected status after landing |
|---|---|---|
| `MINIMAL_AXIOMS_2026-05-20` | #1604 (landed) | canonical axiom doc |
| `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20` | #1604 (landed) | bounded support → re-audit may lift to `retained_bounded` once no-extra-structure premise is independently audited |
| `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20` | #1606 (in flight) | `bounded_theorem` candidate; expected `retained_bounded` after audit |
| `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20` | #1608 (in flight) | `bounded_theorem` candidate; expected `retained_bounded` after audit |
| `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20` | #1604 (landed) | currently bounded support; **after #1606 + #1608 retain**, eligible for re-audit lift to `retained_bounded` |
| `BORN_RULE_ANALYSIS_2026-04-11` | (existing) | currently `audited_failed` (gravitational Hartree route); replaced by the Gleason–Busch route via the chain above |

## Action items (not in scope of this PR)

1. **Wait for #1606 and #1608 to land** and retain (independent audit lane).
2. **Re-audit `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20`** with the closed prerequisites — expected verdict: `retained_bounded` with Gleason 1957 + Busch 2003 as named bounded admissions.
3. **Update `BORN_RULE_ANALYSIS_2026-04-11`'s status surface** to note that the gravitational Hartree route remains failed but a structurally different Gleason–Busch route on the qubit reframe has reached `retained_bounded` (the explicit repair target on `NONLINEAR_BORN_GRAVITY_NOTE.md`'s audit verdict).

Steps (1)–(3) are not part of this PR's content. This PR is solely a tracking note that identifies the chain assembly and the promotion path.

## What this note is

- A meta tracking note recording the chain assembly for Born retention
- A path identification, not a derivation
- A reference for the independent audit lane to know the chain it would re-audit once prerequisites land

## What this note is not

- Not a Born derivation (that's `BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20`)
- Not a Lüders rule derivation (that's PR #1606)
- Not a Record-as-Kraus derivation (that's PR #1608)
- Not a retained promotion (verdicts are set only by the independent audit lane)
- Not a closure of any audited row (it's a chain identification, not a closure)
- Not a numerical-prediction change

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links so the citation graph records them as chain nodes):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — canonical axiom doc supplying A1+A2 qubit-form on which the Born route is built
- [`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md) — the Born route this bundle identifies the promotion path for
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) — landed companion supplying the pre-record reference

**Plain-text pointer references** (NOT load-bearing deps; in-flight prerequisites or external repair-target references):

- `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md` (in flight PR #1606; will become load-bearing dep once landed)
- `PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md` (in flight PR #1608; will become load-bearing dep once landed)
- `BORN_RULE_ANALYSIS_2026-04-11.md` (`audited_failed`; repair target reference, not load-bearing)
- `NONLINEAR_BORN_GRAVITY_NOTE.md` (retained_bounded; repair-target text reference, not load-bearing)
- Gleason 1957 / Busch 2003 / CFMR 2004 — standard math imports, not framework rows
