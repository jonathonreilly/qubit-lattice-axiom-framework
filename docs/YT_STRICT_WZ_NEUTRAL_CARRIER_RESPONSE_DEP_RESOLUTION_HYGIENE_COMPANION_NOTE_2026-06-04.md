---
claim_id: yt_strict_wz_neutral_carrier_response_dep_resolution_hygiene_companion_note_2026-06-04
claim_type_author_hint: meta
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Strict W/Z Neutral-Carrier Response: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the parent
[`YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md`](YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md)
does not load-bear on the specific *audit grade* of its dep
[`YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`](YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md)
— only on that dep's *structural neutral-ray finite-Pauli/projector
algebra*, which the parent's own runner
[`scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py`](../scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py)
already re-verifies block-for-block. This is not a new theorem claim,
not a status promotion, and not an attempt to perform re-audit work.
If the audit pipeline seeds this file, it is a meta companion row; the
audit lane still sets `audit_status`, and the pipeline-derived
`effective_status` remains downstream of that authority.

**Companion target:** `yt_strict_wz_neutral_carrier_response_packet_note_2026-05-25`
(parent note
[`docs/YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md`](YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md)).
**Primary runner:**
[`scripts/audit_companion_yt_strict_wz_neutral_carrier_response_dep_resolution_2026_06_04.py`](../scripts/audit_companion_yt_strict_wz_neutral_carrier_response_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_yt_strict_wz_neutral_carrier_response_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_yt_strict_wz_neutral_carrier_response_dep_resolution_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
substantive content (the strict W/Z denominator response rows on the
retained one-Higgs EW surface, source-coordinate invariance, and
radial Jacobian recovery) is independently re-verified by the parent's
own runner from `sympy` primitives on the *same* neutral carrier ray,
with no citation to the dep's audit grade. The companion records that
substance-vs-grade separation as machine-checkable evidence for the
audit lane; it does not re-audit the parent and does not promote
status.

---

## 0. Why this companion exists

The parent's prior audit snapshot (archived 2026-06-04) treated the
row as a clean bounded theorem with claim scope

> Exact bounded W/Z denominator support on the audited neutral carrier
> ray: differentiating retained one-Higgs EW mass rows
> `M_W = g_2 v / 2` and `M_Z = sqrt(g_2^2 + g_Y^2) v / 2` with respect
> to a common local radial source coordinate gives the W/Z response
> rows, source-reparameterization invariance, and radial Jacobian
> recovery conditional on known `g_2`.

That snapshot was invalidated with reason

```text
dep_weakened:yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25:retained_bounded->unaudited
```

The dep
[`YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`](YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md)
moved from the retained-bounded effective view back to an unaudited
state in subsequent audit-lane activity.

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the dep's *audit
> grade* (which was weakened) — or only on a *structural fact* (the
> finite-Pauli/projector identification of `P_- H_0 = H_0` and the
> consequent `H(s) = (0, v(s)/sqrt(2))^T` neutral ray) that the
> parent's own runner re-verifies block-for-block, independently of
> the dep's grade?

This companion records that the second reading is the one supported by
the parent's runner and note text. The parent's runner directly
re-derives the neutral-ray relations on its own (see §3 below), and
its load-bearing step is elementary differentiation of two retained EW
mass formulas with respect to a single local scalar source coordinate.

This companion is therefore audit-friendly evidence that the prior
reading of the parent's substantive content survives the dep's audit
grade change. It is not a re-audit and does not promote status; it
documents the load-bearing-step dependency surface in machine-checkable
form so the audit lane can decide how to treat the parent in light of
the dep weakening.

---

## 1. Parent recap and prior audit grade

The parent
[`YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md`](YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md)
gives strict tree-level W/Z response rows on the retained one-Higgs EW
surface, on a neutral carrier ray, with respect to an arbitrary local
radial scalar source coordinate. The result is denominator-side only:
no top numerator response row, no retained physical-scale `g_2(v)`, no
positive `y_t` closure.

The parent's runner emits

```text
SUMMARY: PASS=47 FAIL=0
```

via six parts:

1. **Anchors / authority scope** — file-existence checks for the note
   and authority sources, plus ledger-grade reads for the
   retained-or-non-retained witness rows (`ew_higgs_gauge_mass`,
   `yt_source_action_support_packet`, `sm_one_higgs_yukawa_gauge_selection`,
   `standard_model_hypercharge_uniqueness`, `ew_coupling_derivation_note`).
   The parent runner does **not** read the audit grade of the dep
   `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`.
2. **Neutral ray tangent** — `H(s) = (0, v(s)/sqrt(2))^T`, `P_- H = H`,
   `P_- dH/ds = dH/ds`, `Q dH/ds = 0`. Pure `sympy` algebra; no dep grade
   consulted.
3. **Strict W/Z response rows** — differentiate `M_W = g_2 v / 2` and
   `M_Z = sqrt(g_2^2 + g_Y^2) v / 2`; verify rows, ratio, and Jacobian
   recovery. Pure `sympy` algebra.
4. **Reparameterization** — `s = f(r)` invariance of the W/Z ratio.
   Pure `sympy` algebra.
5. **Current Y_T closure boundary** — record which retained authorities
   the parent does and does not have; the dep is **not** named here.
6. **Firewalls / forbidden-overclaim absences** — text-presence /
   absence checks on the note.

The prior clean snapshot (codex-audit-loop, high confidence) recorded
chain_closure_explanation

> The retained EW theorem supplies the W/Z mass formulas, the audited
> neutral-carrier bridge supplies the `P_-` radial carrier, and the
> source-coordinate gate supplies the common-coordinate /
> reparameterization cancellation; the derivative identities then
> close by elementary algebra.

That explanation cites the dep's *prior* audited bookkeeping but does
not assert that the parent's *substantive conclusion* depends on the
dep's audit grade. The present companion's narrow observation is that
the parent's *runner* — which is what mechanically demonstrates the
substantive claim — does not depend on the dep's grade at all (see
§3), and the parent's runner re-derives the neutral-ray algebra
inline (Part 2) without ever consulting the dep's ledger row.

---

## 2. Invalidation cause

The audit ledger records the archived invalidation reason

```text
dep_weakened:yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25:retained_bounded->unaudited
```

This invalidation moves the parent from `audited_clean` back to
`unaudited` not because of any change in the parent's runner, note
text, prose, or computed outputs, and not because of any change in the
underlying mathematical content of the dep. It is a grade-propagation
event in the audit graph: the dep's `effective_status` was downgraded,
and the dep-weakening rule re-opens the parent for fresh re-audit work.

At the time of this companion, the dep had *not* been restored to the
retained-bounded effective view on `origin/main`. This companion
therefore does *not* use the "dep restored" angle; it uses the
"parent does not load-bear on the weakened content" angle.

---

## 3. Substance-vs-grade separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content does not
load-bear on the *audit grade* of
`yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`.** The
parent's runner
[`scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py`](../scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py)
re-derives the neutral-ray facts directly (`P_- H = H`,
`P_- dH/ds = dH/ds`, `Q dH/ds = 0`) on the same `(0, v(s)/sqrt(2))^T`
ray as Part 2, and it does not query, cite, or consume any
audit-status field of the dep. The remaining content of the parent
(strict W/Z response rows, source-coordinate reparameterization
invariance, radial Jacobian recovery, current-closure-boundary
recording, and firewall text-checks) is elementary `sympy`
differentiation plus text-presence assertions, computed entirely
inside the parent's runner from `sympy` primitives.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head
   and confirming it passes with identical `SUMMARY: PASS=47 FAIL=0`
   (Block 1 of this companion's runner);
2. Re-verifying the neutral-ray finite-Pauli/projector algebra
   (`P_- H_0 = H_0`, `Q H_0 = 0`, `sigma_z = I - 2 P_-`, P_+/P_-
   projector / orthogonality / completeness) directly from `sympy`
   primitives, independent of the dep runner and dep grade (Block 2);
3. Confirming via static source-scan that
   [`scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py`](../scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py)
   does not read the dep's audit-status fields (no
   `ledger_row("yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25")`
   call) (Block 3);
4. Confirming via static source-scan that the parent note contains no
   claim that the substantive transport conclusion depends on the
   dep's audit grade (Block 4);
5. Counterfactual confirmation: re-executing the parent's runner
   without consulting the dep's audit grade yields identical pass
   count and identical summary (Block 5);
6. Strict W/Z response self-check at the algebraic level (the parent's
   load-bearing differentiation) independent of any dep grade
   (Block 6);
7. Source-coordinate reparameterization invariance self-check
   (`s = f(r)` invariance of the W/Z ratio) independent of any dep
   grade (Block 7);
8. No-claim / forbidden-overclaim gate preservation: the parent note
   still contains the explicit "Status:** retained" absence and
   "positive Y_T closure has been obtained" absence (Block 8).

These are static and dynamic facts about the parent's runner and note;
they do not depend on the dep's audit-lane decisions.

---

## 4. Substance-unchanged assertion

The parent's runner on the current `origin/main` head emits

```text
SUMMARY: PASS=47 FAIL=0
```

This matches the pass-count recorded in the parent note and the prior
clean snapshot's check breakdown.

The parent's note text, runner code, and runner outputs are unchanged
relative to the snapshot under which it was `audited_clean`. The dep's
underlying mathematical content (the `P_-` neutral-carrier ray
identification on the retained one-Higgs EW doublet) is also
unchanged on `origin/main`; only the dep's audit-lane grade has moved.

The substantive bounded claim of the parent is therefore unchanged,
and the parent's runner continues to mechanically demonstrate it. The
audit lane retains exclusive authority to decide how the prior clean
treatment should be handled under the dep's current grade; the present
companion only provides the machine-checkable evidence above to
support that decision.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner, or the dep's note
  or runner;
- claim that the dep
  [`YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`](YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md)
  has been restored to any prior grade (it has not);
- assert that the parent's bounded scope is the only correct reading;
- close the parent's open numerator/coefficient gates (those remain
  open exactly as the parent states them: top coefficient value,
  retained one-Higgs top carrier authority, retained hypercharge
  uniqueness authority, retained physical-scale `g_2(v)` authority,
  matching to physical scale, `m_t` / `y_t` / `v = 246 GeV`);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict; the audit lane sets
  `audit_status` independently.

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Audit-lane handoff

The audit lane decides whether and how to re-audit the parent under
the dep's current `unaudited` grade. The present companion supplies:

- block-level static and dynamic evidence that the parent's substantive
  conclusion is mechanically demonstrated by the parent's own runner
  with no audit-status dependency on the dep;
- a verification that the parent's runner continues to pass at the
  current `origin/main` head with the dep at `unaudited`;
- a static source scan that confirms zero dep-ledger reads in the
  parent's runner;
- a static source scan that confirms the parent note does not
  load-bear on the dep's audit-status grade;
- a small set of self-checks (neutral-ray finite-Pauli/projector
  algebra, strict W/Z response, source-coordinate reparameterization
  invariance, no-claim/forbidden-overclaim text-presence) that
  exercise the substantive content of the parent independent of the
  dep's audit grade.

If the audit lane chooses to treat the prior clean analysis of the
parent as reusable under the present dep grade, this companion records
the basis on which that decision can be made. If the audit lane chooses
to re-audit from scratch or to escalate the dep re-audit, this
companion does not block that path; it only documents the parent's
substance-vs-grade dependency surface.

This companion's type is meta, with audit-companion scope. It is not a
status change.
