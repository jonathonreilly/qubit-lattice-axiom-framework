# EW Current Traceless-Generator Selector: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
parent
[`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md)
does not load-bear on the specific *audit grade* of its dep
[`AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md)
— only on that dep's *current-form context* (the point-split bilinear
shape `J^{mu,A}_x ~ bar(psi)_x Q_EW^A U_mu(x) psi_{x+mu}`) which the
parent note already labels "bounded current-form context...this branch
does not promote it to repo-wide axiom status" (parent cited-context
section). The parent's load-bearing step is an exact rational
counterexample (`T_3` vs `M = I_color`) computed inside the parent
runner from `fractions.Fraction` primitives with no reference to the
dep's audit grade. This is not a new theorem claim, not a status
promotion, and not an attempt to perform re-audit work. If the audit
pipeline seeds this file, it is a meta companion row. This companion
writes no audit verdict and does not supply a direct effective-status
change.
**Companion target:** `ew_current_traceless_generator_selector_no_go_note_2026-05-03`
(parent note
[`docs/EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md)).
**Primary runner:**
[`scripts/audit_companion_ew_current_traceless_generator_selector_dep_resolution_2026_06_04.py`](../scripts/audit_companion_ew_current_traceless_generator_selector_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_ew_current_traceless_generator_selector_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_ew_current_traceless_generator_selector_dep_resolution_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
counterexample (`Tr_internal(T_3) = 0` together with
`Tr_internal(T_3^2) = 1/2` and `M = I_color` purely color-Fierz singlet)
is independently re-verified by the parent's own runner over rational
arithmetic, with no citation to any external audit grade. The
companion records that substance-vs-grade separation as
machine-checkable evidence for later independent audit handling; it
does not re-audit the parent and does not promote status.

---

## 0. Why this companion exists

The parent's prior audit snapshot (archived 2026-06-04) was
`audited_clean` at `claim_type=no_go`, with `auditor_confidence=high`
and verdict scope

> "Narrow no-go that EW-generator tracelessness alone cannot derive the
> connected-trace selector kappa_EW = 0 for the EW current matching gate."

That snapshot was invalidated with reason

```text
dep_weakened:axiom_first_lattice_noether_theorem_note_2026-04-29:retained_bounded->unaudited
```

The dep
[`AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md)
was downgraded from a retained-bounded generated ledger view to
`unaudited` in subsequent audit activity and remains `unaudited` on
`origin/main` as of the current head.

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the dep's *audit
> grade* (which was weakened) — or only on a *structural / shape* fact
> (the point-split bilinear form of an EW Noether current) that the
> parent's own runner does not consume at all, since the load-bearing
> step is an exact rational counterexample computed inside the parent
> runner from `fractions.Fraction` arithmetic?

This companion records that the second reading is the one supported by
the parent's runner and note text. The parent's runner computes
`Tr(T_3) = 0`, `Tr(T_3^2) = 1/2`, the Fierz singlet
`S(I_color) = N_c = 3`, and the connected channel weight
`Tr(T_3^2) * S(I_color) = 3/2` directly, plus the `K_EW(0) = 9/8` vs
`K_EW(1) = 1` separation, all over rational arithmetic. None of these
algebraic facts depend on the audit grade of the dep.

This companion is therefore audit-friendly evidence that the prior
runner evidence for the parent's substantive content is unchanged
across the dep audit-grade change. It is not a re-audit and does not
promote status; it documents the load-bearing-step dependency surface
in machine-checkable form for later independent audit handling.

---

## 1. Parent recap and prior audit grade

The parent
[`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md)
addresses the following question:

> Does the internal-trace identity `Tr_internal(Q_EW) = 0` imply the
> connected-trace EW readout `kappa_EW = 0` in the EW current matching
> gate?

The parent reaches the bounded no-go conclusion that it does not. The
load-bearing step is the exact rational counterexample at `N_c = 3`,
`Q_EW = T_3 = diag(1/2, -1/2)`:

```text
Tr_internal(T_3)   = 0     (kills Wick-disconnected one-current loops)
Tr_internal(T_3^2) = 1/2   (non-zero quadratic trace)
S(I_color)         = N_c = 3   (color Fierz singlet of M = I_color)
Tr_internal(T_3^2) * S(I_color) = 3/2 != 0
```

so `Tr_internal(T_3) = 0` coexists with a non-zero color-singlet
channel weight, and the proposed implication fails.

The parent runner additionally records the explicit selector
separation:

```text
K_EW(0) = 9/8,   K_EW(1) = 1,   K_EW(0) != K_EW(1)
```

confirming that the traceless-generator route cannot fix `kappa_EW`.

The prior `audited_clean` snapshot
(`codex-cli-gpt-5.5-per-site-k1-...`,
`auditor_confidence=high`) recorded `load_bearing_step_class=A`,
`runner_check_breakdown={A: 14, B: 15, C: 0, D: 0, total_pass: 29}`,
with `chain_closure_explanation`

stating that the cited gate and Fierz input define `kappa_EW` as the
color-singlet-channel coefficient, while the `T_3 / M = I_color`
witness gives `Tr(T_3) = 0` but `Tr(T_3^2) S = 3/2`. That is enough to
refute the proposed implication without a broader positive EW-current
theorem.

That explanation already pins the load-bearing surface on the
`T_3 / I_color` algebraic witness and on the gate's `kappa_EW`
definition (which lives in the gate note, not in the Noether dep).
The Noether note appears in the chain only as
"bounded current-form context for the point-split bilinear" — and the
parent note states this explicitly in its own cited-context section
(parent §lines 167-169).

The dep's *grade* is therefore not on the load-bearing path. The
parent's substantive no-go is an algebraic identity over `Fraction`
arithmetic that the parent runner re-derives every run.

---

## 2. Invalidation cause

The audit ledger records

```text
previous_audits[0].invalidation_reason =
    dep_weakened:axiom_first_lattice_noether_theorem_note_2026-04-29:retained_bounded->unaudited
```

This invalidation moves the parent from `audited_clean` back to
`unaudited` not because of any change in the parent's runner, note
text, prose, or computed outputs, and not because of any change in the
underlying mathematical content of the dep. It is a grade-propagation
event in the audit graph: the dep's `effective_status` was downgraded,
and the dep-weakening rule re-opens the parent for fresh re-audit
work.

The dep has *not* been restored to a retained-bounded generated ledger
view on `origin/main`.
This companion therefore does *not* use the "dep restored" angle; it
uses the "parent does not load-bear on the weakened content" angle.

---

## 3. Substance-vs-grade separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content does not load-bear
on the *audit grade* of `axiom_first_lattice_noether_theorem_note_2026-04-29`.**
The parent's runner
[`scripts/frontier_ew_current_traceless_generator_selector_no_go.py`](../scripts/frontier_ew_current_traceless_generator_selector_no_go.py)
computes the load-bearing counterexample directly over
`fractions.Fraction` primitives. The runner's interaction with the
Noether dep is limited to a single existence/shape check:

```python
check("Noether note provides bounded current-form context",
      "J^{μ,A}_x" in noether)
```

i.e. that the dep note's text contains the point-split bilinear
symbol `J^{mu,A}_x` (the shape `bar(psi)_x Q_EW^A U_mu(x) psi_{x+mu}`).
This is a static string presence check; it does not query, cite, or
consume any audit-status field of the dep. Even if this check were
removed, the load-bearing algebraic counterexample
(`Tr(T_3) = 0`, `Tr(T_3^2) = 1/2`, `S(I_color) = 3`, `K_EW(0) = 9/8`
vs `K_EW(1) = 1`) is computed in the runner without any reference to
the dep note at all.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head
   and confirming all 29 checks pass with the canonical RESULT line
   (Block 1 of this companion's runner);
2. Re-verifying the load-bearing algebraic counterexample inputs
   (`Tr(T_3)`, `Tr(T_3^2)`, `S(I_color)`, `C(I_color)`,
   `Tr(T_3^2) * S(I_color)`) directly over `Fraction` arithmetic,
   independent of the parent runner (Block 2);
3. Confirming via static source-scan that
   [`scripts/frontier_ew_current_traceless_generator_selector_no_go.py`](../scripts/frontier_ew_current_traceless_generator_selector_no_go.py)
   contains zero references to audit-status fields (`audit_status`,
   `effective_status`, `intrinsic_status`, `retained_bounded`,
   `audited_clean`, `audited_conditional`, `unaudited`, etc.)
   (Block 3);
4. Confirming via static source-scan that the parent note
   [`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md)
   contains no claim that the substantive no-go depends on the dep's
   audit grade; the parent note in fact explicitly demotes the Noether
   dep to "bounded current-form context...this branch does not promote
   it to repo-wide axiom status" (Block 4);
5. Counterfactual confirmation: re-executing the parent's runner with
   the dep's grade conceptually treated as `unaudited` (i.e., on the
   current `origin/main` head, which is exactly that state) yields
   identical pass count and identical RESULT line (Block 5);
6. The `K_EW(0) = 9/8` vs `K_EW(1) = 1` separation at the algebraic
   level (independent of any dep grade) (Block 6);
7. The `(Tr T_3)^2 = 0` vs `Tr(T_3^2) = 1/2` distinction at the
   algebraic level (the substance of the no-go) (Block 7);
8. No-claim gate preservation; companion declares `claim_type=meta`
   and disclaims status promotion (Block 8).

These are static and dynamic facts about the parent's runner and
note; they do not depend on the dep's audit-lane decisions.

---

## 4. Substance-unchanged assertion

The parent's runner RESULT on the current `origin/main` head is

```text
RESULT: PASS=29 FAIL=0
```

This matches the breakdown recorded in the parent note's prior
`audited_clean` snapshot (`runner_check_breakdown.total_pass = 29`).

The parent's note text, runner code, and runner outputs are unchanged
relative to the snapshot under which it was `audited_clean`. The
dep's underlying mathematical content (the point-split bilinear form
of the staggered current) is also unchanged on `origin/main`; only
the dep's audit-lane grade has moved.

The substantive no-go claim of the parent is therefore unchanged, and
the parent's runner continues to mechanically demonstrate it. The
present companion does not decide whether the prior clean snapshot can
be reused under the dep's current generated ledger view or whether
fresh re-audit is needed; it only provides the machine-checkable
evidence above.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner, or the dep's note
  or runner;
- claim that the dep
  [`AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md)
  has been restored to any prior grade (it has not);
- assert that the parent's narrow no-go scope is the only correct
  reading;
- close the EW current matching gate positively (that gate remains open
  exactly as its note states);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict, or set any audit
  status.

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Audit Handoff

Independent audit handling can decide whether and how to re-audit the
parent under the dep's current `unaudited` grade. The present companion
supplies:

- block-level static and dynamic evidence that the parent's
  substantive no-go is mechanically demonstrated by the parent's own
  runner with no audit-status dependency on the dep;
- a verification that the parent's runner continues to pass at the
  current `origin/main` head with the dep at `unaudited`
  (`RESULT: PASS=29 FAIL=0`);
- a static source scan that confirms zero audit-status references in
  the parent's runner;
- a static source scan that confirms the parent note does not
  load-bear on the dep's audit-status grade, and in fact explicitly
  demotes the Noether dep to "bounded current-form context";
- a small set of self-checks (algebraic counterexample inputs,
  selector separation, distinct linear vs quadratic trace) that
  exercise the parent's load-bearing content independent of the dep.

If later independent audit handling treats the prior clean analysis of
the parent as reusable under the present dep grade, this companion
records the evidence surface for that treatment. If later handling
re-audits from scratch or escalates the dep re-audit, this companion
does not block that path; it only documents the parent's
substance-vs-grade dependency surface.

This companion is `meta`, scope `audit_companion`. It is not a status
change.
