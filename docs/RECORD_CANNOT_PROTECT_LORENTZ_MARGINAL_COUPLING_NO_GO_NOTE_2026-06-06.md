# Record Cannot Be the Lorentz-Naturalness Custodial Mechanism: a Category Argument (No-Go)

**Date:** 2026-06-06
**Claim type:** no_go (structural)
**Type:** no_go
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_record_cannot_protect_lorentz_marginal_coupling_2026_06_06.py`](../scripts/frontier_record_cannot_protect_lorentz_marginal_coupling_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_record_cannot_protect_lorentz_marginal_coupling_2026_06_06.txt`](../logs/runner-cache/frontier_record_cannot_protect_lorentz_marginal_coupling_2026_06_06.txt)

---

## Role

This note answers a specific question: does the **Record axiom** supply the
custodial mechanism the Lorentz-naturalness gap requires (the open residual D of
`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06`, #3123)? Concretely,
can the metric be "recordized" so that Record's structure protects the marginal
velocity coupling (the SME `c`-coefficient, `c_t/c_s`) against the Collins
radiative regeneration — a typicality decoupling stronger than generic
coarse-graining?

**Answer: no — and the route does not even *reach* Collins.** The obstruction is a
**category mismatch**, made concrete here (runner **13 PASS / 0 FAIL**). This is a
scoped structural no-go; it adds **no axiom**.

It is also constructive in two ways: it shows precisely **where Record does the
work** (and it does, upstream), and it **unifies** the Lorentz-naturalness residual
with the framework's standing action-form no-go.

## The category argument

Collins–Perez–Sudarsky–Urrutia–Vucetich regeneration **shifts the MEAN of a
marginal coupling**: a power-divergent loop migrates UV Lorentz violation into the
IR kinetic coefficient `c_s`. Every lever the Record axiom supplies acts on a
**different category**:

| Record lever | What it acts on | Blind to `c_s`? (runner) |
|---|---|---|
| record **formation** / redundancy (quantum Darwinism) | the *rate* of broadcast | **yes** — `U = e^{-i c_s K t}` depends only on `c_s·t`; the formed record is identical for any `c_s` at rescaled time (A1–A2; matches `RECORD_FORMATION`: any `g>0` works at `t=π/4g`) |
| **einselection** / pointer-non-demolition | the pointer **basis** | **yes** — fixed by `[H_int,Π]=0`, a condition independent of the kinetic coefficient (C1–C2) |
| **additivity** over disjoint records | disjoint **supports** | **yes** — `I(R₁∪R₂)=I(R₁)+I(R₂)` holds for every `c_s` (D1) |
| **typicality** / entropy | **fluctuations** (variance) | **yes** — two joint laws with the same single-record marginal differ in variance (E1–E2; the Cauchy-classifier of `RECORD_IID_TYPICALITY_FIREWALL`: additivity yields no sequence law, is scale-blind in the velocity ratio) |

So Record acts on **basis**, **support**, and **fluctuations**. **A
fluctuation-suppressor cannot cancel a mean-shift**, and none of these levers
touches the coefficient of a marginal operator in `H`. The marginal `c_s` is
invisible to all of them — the runner exhibits a `c_s` mean-shift surviving each
lever. Record does not reach the operator Collins moves.

This also disposes of the two species-level steelmen (runner B, C): two species
with different `c_s` form **equally good objective records** (objectivity does not
forbid a speed difference), and the difference lives *inside* the additive envelope
and stays independently recordable (so it is a genuine observable, not protected).

## Where Record *does* do the work (it is not absent — it is upstream)

The no-go is specific to the *residual*. Record is genuinely load-bearing for the
parts of the Lorentz story that succeeded:

1. **"Durable, timeless, no time metric" → continuous time → `c_t` fixed.** This is
   why the marginal gate dissolves at tree level (#3020) and why Collins' two-parameter
   gate reduces to one number `c_s` (#3121).
2. **Record-preservation → the gauge-invariant-local (Wilson) FORM class**
   (`DYNAMICS_FORM_FROM_RECORD_PRESERVATION`), and record-formation → a conserved
   pointer + locality (`RECORD_FORMATION`). Record forces the dynamics *form*.
3. **The K/CPT readout → CPT-exactness → the CPT-*odd* LV sector is forbidden**
   (the retained emergent-Lorentz note's dim-3/dim-5 protection).

What Record cannot do is protect the **CPT-even** marginal coupling, because (a) its
K/CPT power is exhausted on the odd sector, and (b) the coupling lives in the
**un-forced dynamics residual**, not in the readout.

## The unification (constructive)

The residual `c_s` is a **coupling** in the forced gauge-invariant-local class: a
`c_s` mean-shift `δc` keeps `H` gauge-covariant + local + Hermitian — a valid class
member (runner F1). So `δc` is *un-forced* exactly as `β`/`g_bare` are
(`DYNAMICS_FORM` item 5; `BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO`). Therefore:

> The **Lorentz-naturalness residual is the same residual as the action-form
> no-go** — "couplings are not forced" — seen at a second operator dimension.

Record forces the *form*; it cannot fix *this coupling*, just as it cannot fix `β`
or `g_bare`. The framework does not have many separate naturalness problems here; it
has **one** residual (within-class coupling selection not forced) showing up in the
velocity sector.

## Verdict and the only closures

Route (b) (recordize the metric / typicality) **does not close, and does not reach,
Collins.** The only closures remain:
- **(i)** a hidden symmetry of the `Z³ + continuous-time + Cl(3,0)` structure that
  forbids the marginal operator (open; the genuinely framework-native target — and,
  per this note, it must come from `Quantum`/`Lattice`, **not** Record);
- **(ii)** an admitted custodial / `c_t=c_s` axiom — and `c_t=c_s` is a fourth
  signed-permutation (4D-hypercubic) direction the `Z³` Lattice axiom explicitly
  denies, so it is **strictly a new axiom**, not weaker than one.

## What this note does NOT claim

- It does **not** claim the framework is inconsistent — only that Record is the
  wrong axiom for this residual.
- It does **not** contradict #3123 (it answers its residual-D sub-question), #3121,
  or the tree-level dissolution; and it is consistent with the framework's own
  `RECORD_IID_TYPICALITY_FIREWALL` and `DYNAMICS_FORM`/`RECORD_FORMATION` results.
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG/fitted/`β=6`/
  `g_bare` input. It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): record formation depends only on `c_s·t` (so the
  record does not pin `c_s`); two species with different `c_s` form identical
  objective records; `[H_int,Π]=0` (einselection) is `c_s`-independent; the additive
  readout holds for every `c_s`; the Cauchy-classifier (same marginal, different
  variance → no typicality functional); a `c_s` mean-shift stays in the
  gauge-invariant-local class.
- **Cited** (comparator/scope only): `RECORD_FORMATION_POINTER_NON_DEMOLITION_...`,
  `DYNAMICS_FORM_FROM_RECORD_PRESERVATION_...` (couplings un-forced),
  `RECORD_IID_TYPICALITY_FIREWALL_2026-06-06` (no typicality functional),
  `BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06` (the unification);
  Collins et al *PRL* 93 (2004) 191301.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It
does not promote this note or change any audited claim scope.

- [DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- [RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- [RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md](RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md)
- [BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md) (the parent residual D, #3123 — this note answers its "does Record protect the marginal coupling?" sub-question)

### Source-note boundary

**Hypothesis set:** (1) the three axioms (Lattice `Z³`, Quantum `Cl(3,0)`, Record =
durable K/CPT-orbit registration, finitely-additive scalar); (2) the framework's own
record-dynamics results (record-preservation → gauge-invariant-local form;
record-formation → conserved pointer + locality; the IID/typicality firewall); (3)
the Collins regeneration as a mean-shift of the marginal coupling. The result is
structural (finite toy models + the category argument).

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (einselection, pointer basis, quantum Darwinism, additive
readout, marginal operator, mean-shift). No fitted/PDG/`β=6`/`g_bare` value consumed.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of #3123, the Record-dynamics notes, the action-form no-go, or any upstream
row. The audit lane is the only status authority.
