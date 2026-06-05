# Static-Source Readout I1 Accepted-Premise Bridge: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
parent
[`STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
does not load-bear on the specific *audit grade* of its dep
[`ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
— only on that dep's *structural definitional identity*
`alpha := g_bare^2 / (4*pi)` consumed at steps (B2)-(B4) of the parent's
proof-walk, which the parent's own runner
[`scripts/static_source_readout_i1_accepted_premise_runner.py`](../scripts/static_source_readout_i1_accepted_premise_runner.py)
already re-verifies symbolically by direct sympy substitution.
This is not a new theorem claim, not a status promotion, and not an
attempt to perform re-audit work. If the audit pipeline seeds this
file, it is a meta companion row; the audit lane still sets
`audit_status`, and the pipeline-derived `effective_status` remains
downstream of that authority.
**Companion target:** `static_source_readout_i1_accepted_premise_bridge_bounded_note_2026-05-27`
(parent note
[`docs/STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)).
**Primary runner:**
[`scripts/audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.py`](../scripts/audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
substitution-arithmetic substance — exact rational-arithmetic identities
over `Q[g_bare, alpha, C, 1/r]` for (B1)-(B4) — is independently
re-verified by the parent's own runner using only sympy primitives,
with no citation to any external audit grade. The companion records
that substance-vs-grade separation as machine-checkable evidence for
the audit lane; it does not re-audit the parent and does not promote
status.

---

## 0. Why this companion exists

The parent's prior audit snapshot (archived 2026-06-04) treated the row
as `audited_clean` with verdict scope:

> Conditional/local accepted-premise bridge: given local P1
> static-source readout `V(r) = -C*g_bare^2*G(r)`, the Maradudin
> asymptotic supplied through its retained decoration parent, the
> retained I2 convention `alpha := g_bare^2/(4*pi)`, and the retained
> `g_bare=1` conditional, exact substitution gives
> `V(r) -> -C*g_bare^2/(4*pi*|r|) = -C*alpha/|r|` and
> `alpha = 1/(4*pi)` at `g_bare=1`. This does not derive or promote P1
> to Tier-A, does not promote the parent alpha_bare bridge, and does
> not close Newton-law/gravity, 4D loop/Wick, hierarchy,
> physical-continuum, Wilson plaquette matching, generator
> normalization, or `C=C_F` derivation claims.

That snapshot was invalidated with reason

```text
dep_weakened:alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27:retained_bounded->unaudited
```

The dep
[`ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
moved from the retained-bounded effective view back to an unaudited
state in subsequent audit-lane activity.

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the dep's *audit
> grade* (which was weakened) — or only on a *structural fact* (the
> definitional identity `alpha := g_bare^2 / (4*pi)`) that the parent's
> own runner re-verifies symbolically, independently of the dep's
> grade?

This companion records that the second reading is the one supported by
the parent's runner and note text. The parent's runner re-derives the
substitution chain by direct sympy primitives (Section A: exact
substitution; Section C: numerical cross-check); the parent's
load-bearing step is exact rational-arithmetic algebra over a fixed
polynomial ring once the named premise (P1) and the named definitional
identity (D) := `alpha := g_bare^2 / (4*pi)` are consumed.

This companion is therefore audit-friendly evidence that the prior
reading of the parent's substantive content survives the dep's audit
grade change. It is not a re-audit and does not promote status; it
documents the load-bearing-step dependency surface in machine-checkable
form so the audit lane can decide how to treat the parent in light of
the dep weakening.

---

## 1. Parent recap and prior audit grade

The parent
[`STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
addresses the following question:

> Formalize, in audit-readable accepted-premise form, the parent
> alpha_bare bridge's I1 supplied identification — the
> lattice-gauge-theory static-source linear-response readout convention
> `V(r) = -C g_bare^2 G(r)` — then derive by exact substitution that,
> under the sibling Maradudin asymptotic `G(r) -> 1/(4 pi |r|)` and the
> sibling I2 dimensionless-coupling identity `alpha := g_bare^2/(4 pi)`,
> the large-`|r|` limit of `V(r)` is `-C alpha/|r|`, specializing at
> `g_bare = 1` to `V(r) -> -C/(4 pi |r|)` with `alpha = 1/(4 pi)`.

The parent reaches the bounded conclusion

```text
TOTAL   : PASS = 52, FAIL = 0
VERDICT: bounded accepted-premise bridge passes; (B1)-(B4) follow from
  accepted-premise packet (P1) + Maradudin bridge + sibling I2/g_bare
  bridges by exact symbolic substitution arithmetic.
```

via the four substitution-arithmetic steps (B1)-(B4) in the parent's
§"Proof-walk":

1. **(B1) Maradudin substitution** into the static-source linear-response
   readout: substitute `G(r) -> 1/(4*pi*|r|)` into
   `V(r) = -C*g_bare^2*G(r)` to obtain the large-|r| asymptotic
   `V(r) -> -C*g_bare^2/(4*pi*|r|)`;
2. **(B2) Canonical dimensionless-coupling identity** consumed from the
   sibling I2 bridge: `alpha := g_bare^2/(4*pi)`;
3. **(B3) Substitution composition**: `V(r) -> -C*alpha/|r|` as
   `|r| -> infinity`, by exact rational-arithmetic over the polynomial
   ring `Q[g_bare, alpha, C, 1/r]`;
4. **(B4) `g_bare = 1` specialization**: under the sibling `g_bare`
   bridge, `alpha = 1/(4*pi)`, which is the I1 readout identification.

The prior clean snapshot (codex-gpt-5.5-xhigh, high confidence)
recorded a class-B load-bearing step and a 52-pass runner breakdown
(EXACT=41, BOUNDED=11), with chain-closure explanation

> The chain closes at the conditional bounded scope: P1 remains a local
> admitted readout convention, M1 is consumed through the retained
> Maradudin parent behind the decoration wrapper, I2 and `g_bare=1` are
> retained_bounded dependencies, and the B1-B4 algebra is exact. It
> does not close the admitted P1 derivation or any downstream
> physical/gravity/continuum claim.

That explanation phrases the chain *as if* the dep's audit grade is
load-bearing. The present companion's narrow observation is that the
parent's *runner* — which is what mechanically demonstrates the
substantive claim — does not depend on the dep's grade at all (see §3).

---

## 2. Invalidation cause

The audit ledger records the archived invalidation reason

```text
dep_weakened:alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27:retained_bounded->unaudited
```

This invalidation moves the parent from `audited_clean` back to
`unaudited` not because of any change in the parent's runner, note
text, prose, or computed outputs, and not because of any change in the
*underlying mathematical content* of the dep. It is a grade-propagation
event in the audit graph: the dep's `effective_status` was downgraded,
and the dep-weakening rule re-opens the parent for fresh re-audit work.

At the time of this companion, the dep had *not* been restored to the
retained-bounded effective view on `origin/main`. This companion
therefore does *not* use the "dep restored" angle; it uses the
"parent does not load-bear on the weakened content" angle.

---

## 3. Substance-vs-grade separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content does not load-bear
on the *audit grade* of
`alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27`.**
The parent's runner
[`scripts/static_source_readout_i1_accepted_premise_runner.py`](../scripts/static_source_readout_i1_accepted_premise_runner.py)
re-verifies the substitution arithmetic directly by introducing the
symbolic identity `alpha_def := g_bare^2/(4*pi)` as a sympy expression
on its own line (Section A), then computing (B1)-(B4) by direct
substitution; it does not query, cite, or consume any audit-status
field of the dep. The remaining steps (Casimir convention `C = C_F`,
numerical cross-check, Z^3 Green's function bounded check) are
algebraic-structural statements about a fixed polynomial ring and a
standard subtracted-Fourier-integral, computed entirely inside the
parent's runner from sympy/numpy primitives.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head and
   confirming all 52 checks pass with `EXACT=41 BOUNDED=11`
   (Block 1 of this companion's runner);
2. Re-verifying the canonical I2 dimensionless-coupling identity
   `alpha := g_bare^2/(4*pi)` symbolically via independent sympy
   primitives, without importing or executing any code from the dep
   (Block 2);
3. Confirming via static source-scan that
   [`scripts/static_source_readout_i1_accepted_premise_runner.py`](../scripts/static_source_readout_i1_accepted_premise_runner.py)
   contains zero references to audit-status fields (`audit_status`,
   `effective_status`, `intrinsic_status`, `retained_bounded`,
   `audited_clean`, etc.) (Block 3);
4. Confirming via static source-scan that the parent note
   [`STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
   contains no claim that the substantive substitution conclusion
   depends on the dep's audit grade (Block 4);
5. Counterfactual confirmation: re-executing the parent's runner
   without consulting the dep's audit grade yields identical pass count
   and identical `VERDICT` (Block 5);
6. Direct symbolic re-derivation of the (B1)-(B4) substitution chain
   at the algebraic level (sympy `simplify` residuals zero) independent
   of any dep grade (Block 6);
7. Numerical cross-check of `alpha = 1/(4*pi)` at `g_bare = 1` and the
   Casimir convention `C_F = 4/3` at `N_c = 3` independent of any dep
   grade (Block 7);
8. No-claim gate preservation: the runner's no-new-axiom / no-new-vocab
   / multiplicative-bridge / regulator-dependence gates remain green
   across runs (Block 8).

These are static and dynamic facts about the parent's runner and note;
they do not depend on the dep's audit-lane decisions.

---

## 4. Substance-unchanged assertion

The parent's runner output on the current `origin/main` head is

```text
TOTAL   : PASS = 52, FAIL = 0
VERDICT: bounded accepted-premise bridge passes; (B1)-(B4) follow from
  accepted-premise packet (P1) + Maradudin bridge + sibling I2/g_bare
  bridges by exact symbolic substitution arithmetic.
```

with breakdown `EXACT: PASS=41 FAIL=0` and `BOUNDED: PASS=11 FAIL=0`.
This matches the runner totals recorded in the prior `audited_clean`
snapshot (52 total = 41 EXACT + 11 BOUNDED). The parent's verification
prose currently states `TOTAL: PASS=35 FAIL=0`, which the prior auditor
already flagged as non-load-bearing transcript drift; the current
checks have grown to 52 and all pass, but the substantive verdict is
unchanged.

The parent's note text, runner code, and runner outputs are unchanged
relative to the snapshot under which it was `audited_clean`. The dep's
underlying mathematical content (the canonical dimensionless-coupling
identity `alpha := g_bare^2/(4*pi)`) is also unchanged on `origin/main`;
only the dep's audit-lane grade has moved.

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
  [`ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
  has been restored to any prior grade (it has not);
- assert that the parent's bounded scope is the only correct reading;
- close the parent's open gates (derivation of (P1) from the one-qubit
  operator algebra on `Z^3`, derivation of `C = C_F`, promotion of the
  planned parent `alpha_bare` bridge, Newton-law/gravity, 4D
  loop/Wick, hierarchy primitives, physical continuum, Wilson plaquette
  matching, generator normalization — all remain open exactly as the
  parent note states them);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict; the audit lane sets
  `audit_status` independently;
- assert anything about the sibling Maradudin or `g_bare` bridges
  beyond what the parent note already states.

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
- a static source scan that confirms zero audit-status references in
  the parent's runner;
- a static source scan that confirms the parent note does not load-bear
  on the dep's audit-status grade;
- a small set of self-checks (symbolic substitution re-derivation,
  numerical alpha and `C_F` cross-checks, no-claim gate) that exercise
  the remaining substantive content of the parent independent of the
  dep grade.

If the audit lane chooses to treat the prior clean analysis of the
parent as reusable under the present dep grade, this companion records
the basis on which that decision can be made. If the audit lane chooses
to re-audit from scratch or to escalate the dep re-audit, this
companion does not block that path; it only documents the parent's
substance-vs-grade dependency surface.

This companion's type is meta, with audit-companion scope. It is not a
status change.

---

## 7. Boundaries

This companion does not close:

- derivation of (P1) (the named lattice-gauge-theory static-source
  linear-response readout convention) from the framework's one-qubit
  operator algebra on the `Z^3` spatial substrate;
- derivation of the sibling I2 identity `alpha := g_bare^2/(4*pi)` —
  the dep
  [`ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md)
  remains the canonical source-of-truth for this identity, and its
  audit-grade fate is decided by the audit lane;
- derivation of the sibling Maradudin asymptotic
  `G(r) -> 1/(4*pi*|r|)` — registered by
  [`LATTICE_GREENS_MARADUDIN_ASYMPTOTIC_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`](LATTICE_GREENS_MARADUDIN_ASYMPTOTIC_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md);
- derivation of the sibling `g_bare = 1` conditional — registered by
  [`G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md);
- promotion of the planned parent
  `ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE_2026-05-26.md`
  status — the audit lane decides whether that parent's status improves
  once this bridge family is re-reviewed;
- the 4D loop integral `d^4 k / (2 pi)^4` and the Wick rotation
  `Z^3 -> Z^4` (foreclosed by the species-count regulator-dependence
  no-go);
- the hierarchy primitives P1, P2, P4 of
  `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`;
- any downstream Newton-law, gravity, physical-continuum, or
  phenomenology claim.

The companion records load-bearing-step dependency-surface evidence
only. It does not eliminate the parent's admitted (P1); it does not
substitute for sibling-bridge derivations; and it does not change the
parent's or dep's audit grade. The audit lane retains exclusive
authority over status fields.
