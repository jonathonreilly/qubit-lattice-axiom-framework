# `CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Claim type:** meta
**Parent under repair:** [`CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md`](CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md)
**Wave:** downstream surgical-fix wave (direct dependent of `anomaly_forces_time_theorem`).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only. This note does not set or predict the parent's audit outcome.

## 1. Source character

`CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md`
is a `positive_theorem` that proves an **operational no-past-signaling**
statement: on the single-clock Hilbert/local-data surface, an operation
chosen at clock time `t_1` cannot alter the operational probability law
of a record or boundary datum at an earlier clock time `t_0 < t_1`. The
proof is a three-line trace-preservation argument:

```
Tr[ E_x(σ_a) ] = Tr[ σ_a ] = Tr[ U_10(M_a(ρ_0)) ] = Tr[ M_a(ρ_0) ].
```

The proof's own trace-preservation step is unaffected by the surgical
fixes here. What was patched is (i) the **tier qualifier** on the
single-clock surface ("retained" vs the actual `unaudited` ledger tier),
and (ii) **disclosure of admission-inheritance** from the upstream
parent.

## 2. Findings

### F-A — Tier over-claim "retained" for the single-clock surface

**Symptom:** five sites in the source note described the single-clock
surface as "retained":

| Location | Original wording |
|---|---|
| Scope header | "single-clock Hilbert/local-data surface" (claim-section: see Claim block) |
| Claim block (line ~13) | "On the retained single-clock framework surface, …" |
| Existing imports block (line ~31) | "the retained single-clock/codimension-1 surface" |
| Claim boundary (line ~252) | "exact no-past-signaling on the retained single-clock Hilbert/local-data surface" |
| Trailing "no derivation" bullet (line ~267) | "no derivation of the retained single-clock surface itself" |

**Reality (per 2026-05-17 ledger snapshot):** the single-clock companion
theorem `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
sits at:

| `audit_status` | `effective_status` | `claim_type` |
|---|---|---|
| `unaudited` | `unaudited` | `positive_theorem` |

Calling it "retained" is therefore an over-statement of the upstream
tier.

**Fix:** all five sites now use "cited single-clock surface" wording
with explicit acknowledgment that the tier is inherited from the
single-clock companion (currently `unaudited`). A new
"Upstream-tier and admission inheritance (2026-05-17)" subsection
records the actual ledger tiers of all cited dependencies.

### F-B — Missing admission-inheritance disclosure

**Symptom:** the note imported the single-clock structure as its
load-bearing dependency without disclosing:

- the upstream parent's named admission (iv) (single-clock codimension-1
  evolution excludes `d_t > 1`);
- the parent's recent `F-B` framing-fix
  ([`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md)),
  which identifies admission (iv) as the routing target for the
  parent's inherited `d_t > 1`-exclusion;
- the fact that the **same single-clock companion** is both this
  chronology proof's load-bearing input and the parent's admission (iv)
  routing target — so any revision to admission (iv) propagates into
  this chronology proof.

The chronology proof does **not** import `d_t = 1`, the `(3, 1)`
signature, or any other parent conclusion; it only imports the
single-clock evolution structure. But the single-clock companion is the
**same theorem** that the parent routes admission (iv) to.

**Fix:** the new "Upstream-tier and admission inheritance" subsection
makes the inheritance explicit, links to the upstream `F-B` framing-fix,
and states that future revisions to admission (iv) propagate into the
load-bearing input here. The trace-preservation argument itself is
unaffected.

## 3. What this fix does NOT do

- Change the three-line trace-preservation argument.
- Change the formal model (`ρ_0`, `M_a`, `U_10`, `E_x`, …).
- Change the boundary-data version or the Heisenberg-dual statement.
- Change the Loschmidt-echo wording or the "Why CPT and T do not create
  a channel to the past" framing.
- Change the reviewer-pressure checks (delayed choice, future erasure,
  postselection, advanced fields, CTCs).
- Change the claim-boundary list of what is / is not proved.
- Promote any upstream companion theorem.
- Modify pipeline code or any other source theorem note.
- Set or predict an audit outcome.

## 4. Suggested auditor verdict

`audited_conditional` (positive_theorem retained; effective tier
inherits from the single-clock companion, currently `unaudited`).

The corrected note brings the in-note tier description into line with
the ledger and discloses the admission-inheritance from the upstream
parent. The proof's own trace-preservation argument is unaffected.

Once the single-clock companion audits through, the chronology proof's
effective tier rises automatically without further surgical edits.

## 5. Verification

Paired runner:
`scripts/frontier_chronology_protection_downstream_fix.py`

Programmatically verifies:

- **F-A:** all five "retained single-clock …" wordings have been
  retired; replacement "cited single-clock …" / "currently `unaudited`"
  wording is present; the "Upstream-tier and admission inheritance"
  subsection lists the single-clock companion at `unaudited`.
- **F-B:** the new subsection enumerates the cited dependencies with
  their actual ledger tiers; links to the upstream `F-B` framing-fix;
  records that revisions to admission (iv) propagate into the
  chronology proof.
- **Structural invariants:** trace-preservation argument
  (`Tr[ E_x(σ_a) ] = Tr[ σ_a ] = Tr[ U_10(M_a(ρ_0)) ] = Tr[ M_a(ρ_0) ]`)
  preserved; formal-model definitions preserved; reviewer-pressure
  checks (delayed choice, future erasure, postselection, advanced
  fields, CTCs) preserved; claim-boundary list preserved.

Cached output: `logs/runner-cache/frontier_chronology_protection_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md`](CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — upstream parent (single-clock import route)
- [`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md) — upstream `F-B` fix
- [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) — single-clock companion (the load-bearing input; currently `unaudited`)
- [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507) — sibling downstream fix (`s3_anomaly_spacetime_lift_note`)
- [PR #1509](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1509) — sibling downstream fix (`dt1_time_dimension_proof_walk`)
- [PR #1510](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1510) — sibling downstream fix (`s3_time_spacetime_tensor_primitive`)
- [PR #1511](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1511) — sibling downstream fix (`axiom_first_sm_anomaly_cancellation_complete`)
