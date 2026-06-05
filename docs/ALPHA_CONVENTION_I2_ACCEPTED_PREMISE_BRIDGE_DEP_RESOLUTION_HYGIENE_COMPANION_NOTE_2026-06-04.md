# α Convention I2 Accepted-Premise Bridge: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
parent
[`ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
does not load-bear on the specific *audit grade* of its dep
[`G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md)
— only on that dep's *algebraic conditional content* (the positive
bare-coupling readout `g_bare = 1`), which the parent's own runner
[`scripts/alpha_convention_i2_accepted_premise_runner.py`](../scripts/alpha_convention_i2_accepted_premise_runner.py)
already consumes via pure symbolic substitution
`(g_bare**2/(4*pi)).subs(g_bare, 1)` with no read of the dep's
audit-status field. This is not a new theorem claim, not a status
promotion, and not an attempt to perform re-audit work. If the audit
pipeline seeds this file, it is a meta companion row. This companion
writes no audit verdict and does not supply a direct effective-status
change.
**Companion target:** `alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27`
(parent note
[`docs/ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)).
**Primary runner:**
[`scripts/audit_companion_alpha_convention_i2_accepted_premise_bridge_dep_resolution_2026_06_04.py`](../scripts/audit_companion_alpha_convention_i2_accepted_premise_bridge_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_alpha_convention_i2_accepted_premise_bridge_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_alpha_convention_i2_accepted_premise_bridge_dep_resolution_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
exact-symbolic substitution chain (B1)-(B4) is independently re-verified
by the parent's own runner on the *same* sympy primitives, with no
citation to any external audit grade. The companion records that
substance-vs-grade separation as machine-checkable evidence for later
independent audit handling; it does not re-audit the parent and does
not promote status.

---

## 0. Why this companion exists

The parent's prior audit snapshot (archived 2026-06-04 with audit_date
2026-05-28) treated the row as `audited_clean` with effective_status
`audited_clean`, recording verdict scope: bounded accepted-premise
bridge passing (B1)-(B4) by exact symbolic substitution arithmetic.

That snapshot was invalidated with reason

```text
dep_weakened:g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26:retained_bounded->retained_pending_chain
```

The dep
[`G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md)
later moved from the `retained_bounded` effective view back to an
`unaudited` state in subsequent audit-lane activity. At the time of this
companion, the dep is `unaudited` on `origin/main`.

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the dep's *audit
> grade* (which was weakened) — or only on a *symbolic algebraic
> conditional* (`g_bare = 1` substituted into (P1)) that the parent's
> own runner exercises in pure sympy, independently of the dep's grade?

This companion records that the second reading is the one supported by
the parent's runner and note text. The parent's runner performs
`alpha_from_P1.subs(g_bare, 1)` as a pure symbolic rational-arithmetic
substitution on `Q[g_bare, alpha_bare, alpha_LM, alpha_s, u_0]`; it
does not query, cite, or consume any audit-status field of the dep.
The parent note explicitly phrases step (B1) as *conditional* via the
dep — "At `g_bare = 1` (conditional via the g_bare two-Ward sibling
accepted-premise bridge)" — which is a conditional algebraic
substitution, not a grade-source statement.

This companion is therefore audit-friendly evidence that the prior
runner evidence for the parent's substantive content is unchanged
across the dep audit-grade change. It is not a re-audit and does not
promote status; it documents the load-bearing-step dependency surface
in machine-checkable form for later independent audit handling.

---

## 1. Parent recap and prior audit grade

The parent
[`ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
addresses the following question:

> Given the supplied accepted-premise packet (P1) — the standard QFT
> dimensionless-coupling convention `α := g_bare² / (4π)` — together
> with the `g_bare = 1` conditional bridge and the `α_LM`
> geometric-mean identity, derive the canonical bridge-readout
> `α = 1/(4π)` at `g_bare = 1` as an exact rational-arithmetic
> identity.

The parent reaches the bounded conclusion that (B1)-(B4) follow from
the accepted-premise packet (P1) + g_bare bridge + α_LM
geometric-mean identity by exact symbolic substitution arithmetic via
the following runner blocks:

1. **Source firewall** (Section 0): note file exists, contains required
   accepted-premise and status-boundary phrases, excludes
   forbidden status/import phrases (`audited_conditional`,
   `effective_status =`, `retained_bounded`, `No new admissions`,
   `PDG load-bearing value`);
2. **Exact symbolic substitution chain (B1)-(B4)** (Section A):
   - (B1) `alpha_from_P1.subs(g_bare, 1) = 1/(4π)` via sympy-exact
     simplification;
   - (B2) functional-uniqueness: a rescaled `α' = k · g_bare²/(4π)`
     with `k ≠ 1` violates (P1);
   - (B3) composition with the `α_LM² = α_bare · α_s(v)` identity by
     exact polynomial-ring substitution;
   - (B4) canonical Wilson-surface consequence: `α = 1/(4π)` at
     `g_bare = 1`;
3. **Functional form audit on (P1)** (Section B): (P1) is exactly
   `1/(4π) · g_bare²`, with monomial coefficient sequence `[1, 0, 0]`,
   no constant term, no linear term, second derivative `1/(2π)` at zero;
4. **Numerical α at g_bare = 1** (Section C): `1/(4π) = 0.0795774…`
   matches the parent alpha_bare bridge's `(D2)` value;
5. **α_LM composition numerical cross-check** (Section D): four
   `(α_bare, u_0)` symbolic test pairs and four numerical `u_0` values
   confirm the geometric-mean identity holds;
6. **Isolation from I1 and I3** (Section E): the bridge addresses only
   I2; I1 and I3 are explicitly consumed-only;
7. **No-import audit** (Section F): no continuum 4D-Fourier import, no
   Wick rotation, no PDG / fitted / Monte Carlo / running-scheme
   input; load-bearing inputs are exactly four — (P1), the `α_LM`
   identity, the `g_bare = 1` conditional, and rational arithmetic;
8. **Vocabulary audit + no-go compatibility** (Section G): no new repo
   vocabulary, no multiplicative cross-row combination, regulator
   no-go respected, no new repo-wide axiom.

The prior clean snapshot recorded the parent's two deps and their
snapshot effective statuses:

- `alpha_lm_geometric_mean_identity_theorem_note_2026-04-24`:
  `retained` (still `retained` on current `origin/main` — unchanged);
- `g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26`:
  `retained_bounded` (now `unaudited` on current `origin/main` — the
  invalidation trigger).

The parent's runner reads neither dep's ledger row. It re-derives the
substantive content on pure sympy primitives.

---

## 2. Invalidation cause

The audit ledger records the archived invalidation reason

```text
dep_weakened:g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26:retained_bounded->retained_pending_chain
```

This invalidation moves the parent from `audited_clean` back to
`unaudited` not because of any change in the parent's runner, note
text, prose, or computed outputs, and not because of any change in the
underlying mathematical content of the dep (the dep's
`(B3)-(B4)` chain still yields `g_bare² = 1` and positive-branch
`g_bare = 1` as exact rational arithmetic on the same retained Rep-B
input `F_Htt = 1/√6`). It is a grade-propagation event in the audit
graph: the dep's `effective_status` was downgraded, and the
dep-weakening rule re-opens the parent for fresh re-audit work.

At the time of this companion, the dep had *not* been restored to the
`retained_bounded` effective view on `origin/main`. The dep is
currently `unaudited`. This companion therefore does *not* use the
"dep restored" angle; it uses the "parent does not load-bear on the
weakened content" angle.

---

## 3. Substance-vs-grade separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content does not load-bear
on the *audit grade* of `g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26`.**
The parent's runner
[`scripts/alpha_convention_i2_accepted_premise_runner.py`](../scripts/alpha_convention_i2_accepted_premise_runner.py)
performs the (B1) substitution
`alpha_from_P1.subs(g_bare, 1) = 1/(4π)` as a pure sympy symbolic
operation on the polynomial ring `Q[g_bare, alpha_bare, alpha_LM,
alpha_s, u_0]`. The only role the dep plays is to *supply* the
conditional value `g_bare = 1`, which the parent's runner consumes as a
symbolic substitution argument — not as a status-graded import. The
parent's runner does not import the dep's runner, does not import the
dep's note, and does not read the audit ledger.

The remaining substitution steps (B2)-(B4), the `α_LM`
geometric-mean composition, the functional-form audit, the numerical
cross-check, the I1/I3 isolation, the no-import audit, and the
vocabulary audit are all pure sympy or finite-dimensional numerics
internal to the parent's runner — none consult the dep's grade.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head and
   confirming all blocks pass with the unchanged
   `VERDICT: bounded accepted-premise bridge passes` final tag
   (Block 1 of this companion's runner);
2. Re-verifying the load-bearing exact substitution
   `(g_bare²/(4π)).subs(g_bare, 1) = 1/(4π)` directly from sympy
   primitives — *as a pure symbolic rational substitution*, independent
   of the dep runner (Block 2);
3. Confirming via static source-scan that
   [`scripts/alpha_convention_i2_accepted_premise_runner.py`](../scripts/alpha_convention_i2_accepted_premise_runner.py)
   contains no executable references to the dep's audit-status fields
   (the existing mentions of `effective_status =` and `retained_bounded`
   are in the Section 0 *forbidden-phrase exclusion list*, asserting
   that the parent NOTE does NOT contain those phrases — i.e., they
   are status-citation-avoidance assertions, not status reads)
   (Block 3);
4. Confirming via static source-scan that the parent note
   [`ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
   contains no claim that the substantive bridge conclusion depends on
   the dep's audit grade; the parent's load-bearing phrase is
   explicitly *conditional* — "At `g_bare = 1` (conditional via the
   g_bare two-Ward sibling accepted-premise bridge)" — which is an
   algebraic conditional, not a grade-source statement (Block 4);
5. Counterfactual confirmation: re-executing the parent's runner with
   the dep at `unaudited` (the current `origin/main` state) yields
   identical pass count and identical `VERDICT` line (Block 5);
6. Functional-form algebraic self-check: independent sympy re-derivation
   that `(P1)` is exactly the monomial `1/(4π) · g_bare²` with degree
   2, zero constant term, zero linear term, second derivative `1/(2π)`
   at zero, and that `α(g_bare=1) = 1/(4π)` regardless of the dep
   (Block 6);
7. `α_LM` composition algebraic self-check: independent sympy
   re-derivation that `α_LM² / α_s = α_bare` holds as a polynomial-ring
   identity, and that substituting `α_bare = g_bare²/(4π)` is an exact
   rational substitution that does not consult the dep's grade
   (Block 7);
8. Status-boundary preservation: the parent note's independent
   audit-lane boundary is preserved; the companion declares
   `Type: meta` and disclaims status promotion (Block 8).

These are static and dynamic facts about the parent's runner and note;
they do not depend on the dep's audit-lane decisions.

---

## 4. Substance-unchanged assertion

The parent's runner final `VERDICT` line on the current `origin/main`
head is

```text
VERDICT: bounded accepted-premise bridge passes; (B1)-(B4) follow from the
  accepted-premise packet (P1) + g_bare bridge + alpha_LM
  geometric-mean identity by exact symbolic substitution arithmetic.
```

with `TOTAL: PASS = 61, FAIL = 0` (`EXACT: PASS = 56, BOUNDED:
PASS = 5`). This matches the previous-snapshot exec-trace verdict.

The parent's note text, runner code, and runner outputs are unchanged
relative to the snapshot under which it was `audited_clean`. The dep's
underlying mathematical content (the `g_bare² = 1` and positive-branch
`g_bare = 1` derivation from `(P1)` + Rep-B `F_Htt = 1/√6`) is also
unchanged on `origin/main`; only the dep's audit-lane grade has moved.

The substantive bounded claim of the parent is therefore unchanged,
and the parent's runner continues to mechanically demonstrate it. The
audit lane may still treat the prior clean snapshot, the dep
weakening, and any parent re-audit need independently. The present
companion only provides the machine-checkable evidence above.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner, or the dep's note
  or runner;
- claim that the dep
  [`G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md)
  has been restored to any prior grade (it has not);
- assert that the parent's bounded scope is the only correct reading;
- close the parent's open conditional gates (the `(P1)` accepted
  premise and the `g_bare = 1` conditional remain admitted exactly as
  the parent and dep notes state them);
- derive `(P1)` itself from the one-qubit operator algebra on the `Z³`
  lattice/operator-algebra setting (the canonical QFT dimensionless-coupling
  convention remains an admitted convention);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict, or set any audit
  status.

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Audit-lane handoff

Independent audit handling can decide whether and how to re-audit the
parent under the dep's current `unaudited` grade. The present companion
supplies:

- block-level static and dynamic evidence that the parent's substantive
  conclusion is mechanically demonstrated by the parent's own runner
  with no audit-status dependency on the dep;
- a verification that the parent's runner continues to pass at the
  current `origin/main` head with the dep at `unaudited`;
- a static source scan that confirms zero executable audit-status
  references in the parent's runner (existing `effective_status =`
  and `retained_bounded` mentions are confined to the Section 0
  forbidden-phrase exclusion check on the parent note text);
- a static source scan that confirms the parent note does not load-bear
  on the dep's audit-status grade — the only dep reference is the
  conditional-substitution phrase "At `g_bare = 1` (conditional via
  the g_bare two-Ward sibling accepted-premise bridge)";
- a small set of self-checks (functional-form audit, `α_LM`
  composition, status-boundary preservation) that exercise the
  remaining substantive content of the parent independently of the
  dep's grade.

If later independent audit handling treats the prior clean analysis of
the parent as reusable under the present dep grade, this companion
records the evidence surface for that treatment. If later handling
re-audits from scratch or escalates the dep re-audit, this companion
does not block that path; it only documents the parent's
substance-vs-grade dependency surface.

This companion's type is meta, with audit-companion scope. It is not a
status change.

---

## 7. Existing No-Go Compatibility

- The **multiplicative bridge no-go** (Cheeger-Simons R/Z foreclosure)
  is respected: this companion does not multiplicatively combine the
  `(4π)` convention factor with any other framework constant; it only
  observes that the parent's exact rational substitution
  `α(g_bare=1) = 1/(4π)` is sympy-internal.
- The **regulator-dependence no-go** for the hierarchy exponent `16`
  is respected: this companion addresses only the parent's prefactor
  convention chain `(B1)-(B4)`, not the exponent `16` in `α_LM^16`
  or any downstream hierarchy primitive.
- The **no-imports** rule is respected: no new convention, no new
  axiom, no new framework primitive is introduced. The companion
  consumes only the parent's existing runner, the dep's existing note
  metadata (for reading the invalidation reason from the audit
  ledger), sympy, and standard finite-dimensional numerics.

---

## 8. Pattern reference

This companion follows the dep-resolution hygiene companion template
already used by landed dep-resolution hygiene companions. This section
is a style note, not a dependency edge. The present companion uses the
same "parent does not load-bear on the weakened content of the dep"
angle for the `alpha_convention_i2_accepted_premise_bridge` parent
under the `g_bare_two_ward_h_unit_residue_accepted_premise_bridge`
dep-weakening invalidation.
