# Three-Axiom Clean Base with Record (Promotion Proposal)

**Date:** 2026-06-04
**Type:** meta
**Status:** **proposal** for governance / review-loop ratification. This note
does **not** unilaterally re-axiomatize; it proposes promoting the
already-shipped, established-irreducible observable-principle atom (P1) to a
third axiom (Record), and documents the resulting clean three-axiom base
together with a per-axiom anti-smuggling audit. Adoption is a governance
decision (the registry move below), to be taken through the review loop.
**Runner:** [`scripts/audit_companion_three_axiom_clean_base_exact.py`](./../scripts/audit_companion_three_axiom_clean_base_exact.py)
**Authority role:** architecture proposal. The math it relies on is shipped
and cited (P1 irreducibility, the qubit algebra); the runner grounds only the
facts that keep each axiom statement honest.

## Summary

The framework currently has two axioms (qubit, lattice) plus the observable
principle P1 carried as a Tier-A admitted input. P1 is established
**irreducible** (no internal theorem derives the additive-log readout;
[OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md](OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md)
and the selector dichotomy `OBSERVABLE_PRINCIPLE_P1_EXPONENT_SELECTOR_DICHOTOMY_NARROW_NOTE_2026-06-02`).
An irreducible primitive belongs in the axiom column, not as a hidden
admission. This note proposes promoting P1 to **Axiom III (Record)**, yielding
the clean three-axiom base, and audits each axiom for smuggling.

## The three axioms (proposed)

> **I. Quantum.** Reality is a qubit at every site (a two-state complex
> system; operator algebra `M_2(C)`).
>
> **II. Locality.** The sites form the 3-D cubic lattice `Z^3` (finite-range
> near-neighbour adjacency; separated regions independent).
>
> **III. Record.** The physical observable is the information — the additive
> logarithm — of the record.

All three are **timeless statements of what-is**: reality *is* qubits; the
sites *form* `Z^3`; the observable *is* the information of the record. No
dynamics, time, or probability-flow appears in any axiom; those are derived.

## Why promote P1 (rather than keep it as a Tier-A admission)

- **It is irreducible.** P1 — the readout additive over independent records,
  hence the logarithm — has no internal derivation
  ([P1 exponent-fixing irreducibility](OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md);
  parent [OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)).
  A primitive that cannot be reduced is honestly an axiom, not a derivation
  target held open forever.
- **It removes bounded-lane churn.** As a Tier-A admitted input, P1 caps every
  dependent lane at `retained_bounded`. The registry
  ([ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md))
  states that removing a target lets `compute_effective_status` cascade
  dependents toward unbounded `retained`. Promotion un-caps exactly the lanes
  bounded **solely** by the P1 dependency.
- **It is the only clean promotion.** Of the four Tier-A admissions
  {P1, AC_φλ, S, θ}: **S** (the scale) and **θ** are value-fixing
  *conventions*, not structural axioms; **AC_φλ** is an open derivation target
  (not proven irreducible); the open gates (staggered-Dirac, `g_bare = 1`) are
  derivation targets; **composition** is a derived consequence (local
  tomography from the complex structure, `TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_...`
  / `LOCAL_TOMOGRAPHY_FROM_QUBIT_COMPLEX_STRUCTURE_...`); the **modulus (P2)**
  is a separate admission. Only P1 is an established-irreducible primitive.
  After promotion the genuine-admission set is **{AC_φλ, S, θ}**.

## Per-axiom anti-smuggling audit

### Axiom I — Quantum

- **Commits to:** a two-state **complex** system, **per site**. (The complex
  unit is the real content — it is what makes the algebra `M_2(C)`, the qubit,
  rather than the real `M_2(R)`, the rebit; openly stated, not hidden.)
- **Does NOT smuggle the spatial dimension.** The "3" of the equivalent name
  `Cl(3,0)` is the algebra's count of mutually-anticommuting Hermitian
  generators (the three Paulis), an intrinsic fact about `M_2(C)` — **not** the
  spatial dimension. The two are independent: a qubit Ising-couples in any
  number of lattice directions (runner Q2), so Axiom I's algebra-3 does not fix
  and is not fixed by Axiom II's spatial-3. *Discipline:* never claim one
  derives the other.
- **Does NOT smuggle measurement.** State "operator algebra", not "observable
  algebra" — "observable" forward-references Record.
- **Does NOT smuggle composition.** Stated per-site; the multi-site tensor rule
  is a derived consequence (local tomography from the complex structure), not a
  premise.

### Axiom II — Locality

- **Commits to:** discreteness **+** `d_s = 3` **+** cubic adjacency **+**
  translation-invariance **+** finite-range locality / independence — a rich
  spatial-structure primitive.
- **Honest residual, not a smuggle:** `d_s = 3`, the cubic structure, and
  discreteness are **primitives here** — the qubit does not force them (a qubit
  lives on any `Z^d`). They are visible in "`Z^3`", not hidden; the discipline
  is to present Axiom II honestly as the *geometry* axiom, not as bare
  "locality".
- **Physical/fundamental status is INHERITED**, not separately asserted.
  Because Axiom I says reality **is** the qubits (and they sit at discrete
  sites), the lattice is the fundamental structure: there is no continuum to
  take a limit of; the continuum is an emergent large-scale approximation; the
  lattice spacing is physical (and is the scale `S`); Lorentz invariance is
  emergent, not exact. No second "reality is a lattice" claim is needed or made.

### Axiom III — Record

- **Commits to:** the additive-logarithm readout (P1), as a **timeless form**.
  "Record" is a **noun** (a definite configuration — the read-out, classical
  side, as opposed to the qubit amplitudes), not a verb.
- **Does NOT smuggle the transition.** It does not assert that amplitudes
  *become* a record; the measurement/decoherence transition (Born via
  Gleason/Busch) is derived.
- **Does NOT smuggle time.** No "at creation" / "when" — emergent time is
  derived.
- **Does NOT smuggle the probabilities.** Born weights are derived, not posited.
- **Does NOT smuggle the modulus.** The `|·|` (P2) is a separate admission;
  Axiom III is the logarithm, not the modulus.
- **Does NOT smuggle the arrow.** A timeless "is" statement carries no
  irreversibility; durability / the low-entropy past stays a separate admission.

## Grammar check (the cleanliness tell)

I, II, III are parallel "what-is" statements (`is` / `form` / `is`). None
describes a happening. That parallel grammar is the check that Axiom III is as
clean as I and II — it states a *form*, not an *event*.

## Honest residuals after adoption

- **Genuine admissions:** {AC_φλ (generations/Koide), S (scale = the physical
  lattice spacing), θ (strong-CP)}, plus the **modulus (P2)** and the **arrow**
  (kept out of Axiom III).
- **Open gates (derivation targets):** staggered-Dirac realization; `g_bare = 1`.
- **Derived (not admissions):** composition / local tomography.

## Governance (how adoption actually happens)

The promotion is an **audit-config** change: move P1's canonical id
`observable_principle_from_axiom_note` from `tier_a_admissions.json` to
`axiom_premise_nodes.json`, which triggers the effective-status cascade.
Framework PRs do not land audit data; **this note is only the science-side
proposal and justification.** Adoption, and the registry edit, are for the
review loop / governance.

## Validation

[`scripts/audit_companion_three_axiom_clean_base_exact.py`](./../scripts/audit_companion_three_axiom_clean_base_exact.py)
(4 checks, all PASS) grounds the facts the audit relies on: (Q1) `M_2(C)` has
exactly three anticommuting Hermitian generators; (Q2) that algebra-3 is
**independent** of the lattice dimension (a qubit sits on any `Z^d`), refuting
the only cross-axiom smuggle; (Q3) the qubit's complex structure
`omega = sigma_1 sigma_2 sigma_3 = i`; (Q4) Axiom III's additive-log form. P1's
*irreducibility* is the separately shipped result, cited not re-proven.

## Cross-references

- [MINIMAL_AXIOMS_2026-05-20.md](MINIMAL_AXIOMS_2026-05-20.md) — the current
  two-axiom base this proposes to extend to three.
- [OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md](OBSERVABLE_PRINCIPLE_P1_EXPONENT_FIXING_IRREDUCIBILITY_NARROW_NOTE_2026-05-31.md)
  and [OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  — the P1 irreducibility that justifies the promotion.
- [ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  — the Tier-A registry and the auto-cascade mechanism.
- `TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md`
  and `LOCAL_TOMOGRAPHY_FROM_QUBIT_COMPLEX_STRUCTURE_NARROW_THEOREM_NOTE_2026-06-03.md`
  (in review) — composition as a *derived* consequence of Axiom I, not an axiom.
