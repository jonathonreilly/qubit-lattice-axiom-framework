# Qubit Axiom Hardening: Local-Algebra Equivalence, Per-Site k = 1, and Projective Measurement Selection

**Date:** 2026-05-20
**Status:** current framework hardening note
**Type:** meta (companion to `MINIMAL_AXIOMS_2026-05-20.md` A1)
**Defends:** `MINIMAL_AXIOMS_2026-05-20.md` A1 statement against the
"vocabulary substitution" framing raised on PR #1604.
**Records:** per-site k = 1 selection and LSP-projective instrument
selection ratifications.

## Purpose

PR #1604 first-pass review raised the objection that A1's bare
"a qubit at every site" form *"reduces axiomatic content to
vocabulary substitution unless the canonical statement preserves
the physical Cl(3) commitment explicitly."*

This note rejects that framing for the local-algebra commitment. The
bare-qubit Axiom 1 commits to the same retained local operator algebra
as the "physical-Cl(3,0)" phrasing: both name the same
algebra-isomorphism class. The bare form is preferred for readability
and Maxwell-tight minimality, **not** because it weakens the algebraic
commitment. The 2026-05-22 ratifications below also make explicit that
"qubit at every lattice site" means one qubit per site, not a
multi-copy module carrying the same algebra, and that ideal unrefined
sharp projective measurements use the Lüders instrument.

## The local-algebra commitment of Axiom 1 under either phrasing

The per-site operator algebra committed by Axiom 1 is one specific
real-algebra-isomorphism class. That class has many co-equal
names; here are the five most relevant:

| Name | Form |
|---|---|
| Operator-algebraic | `M_2(ℂ)` (bounded operators on `ℂ²`) |
| Geometric (real Clifford) | `Cl(3,0)` (real algebra over `ℝ³`) |
| Generator-relation | algebra of three anticommuting self-adjoint `σ_a` with `σ_a² = I` |
| Quantum-information | one qubit |
| Pauli-group span | complex-linear span of `{±I, ±iI, ±σ_a, ±iσ_a}` |

These are **the same object** under five co-equal labels. The
equivalences are audit-ratified:

- `cl3_complexification_split_narrow_theorem_note_2026-05-10`
  (`retained`, positive_theorem): `Cl(3,0) ⊗_ℝ ℂ ≅ M_2(ℂ) ⊕ M_2(ℂ)`
- `cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10`
  (`retained`, positive_theorem): faithful complex irrep is 2-dim
- `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10`
  (`retained_bounded`, bounded_theorem): Pauli-irrep uniqueness

## Rejecting the "vocabulary substitution" framing

The objection implicitly assumes that "qubit" is a less precise
term than "physical Cl(3,0)" — that the bare form loses
commitment-strength or mathematical content.

**That assumption is wrong on three counts.**

### Count 1 — "qubit" has a precise, standard, retained-grade meaning

"Qubit" is not a casual term. In contemporary physics and quantum
information theory it has an exact mathematical definition: the
operator algebra `M_2(ℂ)` acting on a 2-dim complex Hilbert space
`ℂ²` (Nielsen-Chuang Ch.1; Wilde Ch.2; Watrous Ch.1). This is
textbook content — no ambiguity, no informality.

In the framework, "qubit" is bound to that exact mathematical
object via the retained narrow theorems above. The bare-qubit
form is not a casual rename of `Cl(3,0)` — it names the same
algebra via its standard quantum-information-theoretic label.

### Count 2 — every existing `Cl(3)`-language retained row reads cleanly under the qubit identification

The framework's existing retained / retained_bounded / retained_no_go
surface uses `Cl(3)` language pervasively. Examples:
`cl3_color_automorphism_theorem` (`retained_bounded`),
`cl3_complexification_split_narrow_theorem_note_2026-05-10`
(`retained`),
`cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10`
(`retained`),
`cl3_gamma_involution_determinant_narrow_theorem_note_2026-05-10`
(`retained`), and the audited_conditional
`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md` at
the narrowed U1-U3 scope.

Every one of these rows, when stated under the qubit identification,
reduces to a statement about `M_2(ℂ)` and its complex
representations. Nothing in the existing retained surface is lost
under the qubit reading; the equivalence is what makes the bare-qubit
form valid.

### Count 3 — local-algebra commitment of "reality is a qubit at every lattice site"

The bare Axiom 1 says: at every site `x ∈ Z^3`, there is a qubit. By
the standard algebraic meaning of "qubit" in this framework, its
local-algebra commitment is:

- per-site operator algebra `A_x = M_2(ℂ)`
- equivalently as a real algebra, `A_x ≅ Cl(3,0)`
- Pauli generators `σ_a^x` for `a ∈ {1, 2, 3}` per site
- the central pseudoscalar maps to `i · 𝟙_{M_2(ℂ)}` under the
  `Cl(3,0) ≅ M_2(ℂ)` identification

That local-algebra commitment is exactly equal to the commitment of
"the physical local algebra is `Cl(3,0)` at every site." The
operator-algebra content is point-for-point the same. The separate
representation-multiplicity question is the 2026-05-22 ratification
handled below.

All non-axiom structures enter only through their named derivation
lanes.

## What the objection would require to be sound

The objection that the bare form is vocabulary substitution would
require at least one of:

1. **"Qubit" has ambiguous meaning.** False. Standard QI textbook
   definition.
2. **The qubit / `M_2(ℂ)` identification is not retained.** False.
   Two retained positive_theorem narrow theorems certify it.
3. **The bare form fails to commit to the same algebra as
   `Cl(3,0)` framing.** False. Both name the same retained
   isomorphism class.
4. **Existing `Cl(3)`-language retained content silently breaks
   under the qubit reading.** False. The equivalence is the
   identity; no derivation pathway changes.

None of these hold. The bare form is sound.

## The disagreement reduces to a presentational choice

For the local-algebra content, the disagreement reduces to:

- **Form A (reviewer-preferred):** *"physical local algebra is
  `Cl(3,0)`, equivalently `M_2(ℂ)` (the single-qubit operator
  algebra)"* — 14 words, names the real-algebra side first
- **Form B (canonical-as-adopted):** *"Reality is a qubit at every
  lattice site"* — names the qubit/operator-algebra side first

Both name the same retained mathematical object. Both have identical
local-algebra commitment-strength. Neither is *more solid* than the
other as a local-algebra statement.

Form B is preferred for:
1. **Readability** — direct physical wording
2. **Maxwell-tight minimality** — matches the style of Newton I,
   Galilean relativity, Maxwell's equations
3. **Direct physical content** — "reality is a qubit at every
   lattice site" is the actual physical claim; `Cl(3,0)` is the
   real-algebra label for the operator algebra of that qubit
4. **Derivation-lane clarity** — downstream structures keep their
   named lanes rather than moving into the axiom

Form A is preferred for:
1. **Continuity** with existing repo `Cl(3)`-language notes —
   but the equivalence resolves this automatically; no content
   conflict exists
2. **Explicit naming of the real-algebra structure** — but the
   commentary block in `MINIMAL_AXIOMS_2026-05-20.md` already
   provides this; the equivalence does not need to be in the
   axiom statement itself

The framework's choice: Form B in the axiom statement, full
local-algebra content in the commentary block. Mathematically
identical to Form A at the local-algebra level; preferred for
minimality and readability.

## Hardening: what the canonical statement of A1 commits to

For maximum clarity, the bare A1 statement *"Reality is a qubit at
every lattice site"* commits the framework to the following local
algebraic content:

1. Per-site operator algebra `A_x = M_2(ℂ)` (4-dim over `ℂ`,
   8-dim over `ℝ`)
2. Equivalently, per-site real Clifford algebra `A_x ≅ Cl(3,0)`
3. Per-site Pauli-generator presentation `σ_1, σ_2, σ_3` with
   `σ_a² = I, σ_a σ_b = -σ_b σ_a` for `a ≠ b`
4. Per-site pseudoscalar `ω = σ_1 σ_2 σ_3` (the `Cl(3,0)` volume
   element, distinct from the identity `𝟙`), satisfying `ω² = -𝟙`
   and central in `Cl(3,0)`. Under the `Cl(3,0) ≅ M_2(ℂ)`
   identification, `ω` maps to `i · 𝟙_{M_2(ℂ)}`, recovering the "i"
   of quantum mechanics geometrically.
5. The retained algebraic support carried by
   `cl3_complexification_split_narrow_theorem_note_2026-05-10`,
   `cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10`,
   `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10`,
   and the bounded-retained `cl3_color_automorphism_theorem`

That is the primitive local-algebra commitment of Axiom 1 in the
bare-qubit form. It is identical to the local-algebra commitment of
the "physical `Cl(3,0)`" form. The representation-multiplicity
ratification below records the intended one-qubit-per-site reading
inside Axiom 1; all other non-axiom structures enter only through
their named derivation lanes.

## Conclusion

The bare-qubit Axiom 1 is sound as a local-algebra statement. The
"vocabulary substitution" objection is not a solidity concern but a
presentational preference for continuity with existing
`Cl(3)`-language. Solidity of the local-algebra identification is
established by:

- Retained narrow theorems certifying the `M_2(ℂ) ≅ Cl(3,0)`
  equivalence
- Identical local-algebra commitment-strength to the alternative phrasing
- Preserved downstream `Cl(3)`-language content under either local-algebra
  reading
- Explicit routing of non-axiom structures to named derivation lanes

The canonical A1 statement stays:

> **A1.** Reality is a qubit at every lattice site.

Bundled with the binding commentary block in
`MINIMAL_AXIOMS_2026-05-20.md`, this is the framework's
foundational commitment. Mathematically identical to the
`Cl(3,0)`-framing at the local-algebra level; preferred for minimality
and readability.

## Hardening II: k = 1 per-site selection (load-bearing ratification, 2026-05-22)

### Background — the auditor's flag on U4 closure

The audit verdict on
`U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20`
recorded `audited_renaming` with the following rationale:

> *"U4 and A1's 'qubit at every lattice site' are identified by
> axiom-content unpacking, not by a derivation chain bridging two
> separately specified objects... If the qubit reframe of A1 is later
> treated by audit policy as a definitional equivalence rather than a
> load-bearing axiom (e.g. via QUBIT_AXIOM_HARDENING_NOTE_2026-05-20
> ratification), this row could be reconsidered as audited_decoration
> under the cl3_complexification_split parent."*

In plain language, the audit lane is currently treating A1's
"qubit" reading and the prior "Cl(3) per site" reading as **two
labels for the same M_2(ℂ) object** — a definitional equivalence,
not a strengthening. Under that conservative reading, the
**multiplicity-k selection** is left open as it was under the
pre-reframe framing.

This section ratifies the framework-rule reading: Axiom 1's "qubit"
form selects `k = 1` as part of its intended axiom content.

### The k-selection question

The abstract real-Clifford algebra `Cl(3,0)` admits faithful
finite-dimensional complex representations of complex dimension
`dim_ℂ V = 2k` for any multiplicity `k ≥ 1`, decomposing as direct
sums of 2-dimensional irreducible chirality modules. Under the
pre-2026-05-20 "physical Cl(3) per site" framing:

- Axiom 1 fixed the per-site **algebra** as `Cl(3,0)`
- Axiom 1 did **not** fix the **multiplicity** k of the per-site module
- Selecting `k = 1` was an open task carried by substep 1 of
  `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03` (the U4
  bridge: "the per-site Hilbert IS the Cl(3) faithful complex
  irrep on per-site `V`")

Both `k = 1` (single qubit per site) and `k ≥ 2` (multi-copy
modules per site) are admissible Cl(3) representations on the
abstract algebraic surface; selecting `k = 1` required additional
physical input.

### Ratification clause

The 2026-05-20 reframe, read with this ratification, replaces this
two-step structure with a single load-bearing Axiom 1 commitment:

> **(R1) Per-site k = 1 selection.** Axiom 1's reading of "qubit at every
> lattice site" carries the `k = 1` selection as load-bearing axiom
> content. The per-site Hilbert space `H_x` is **exactly** `ℂ²` —
> the unique faithful complex irreducible module of `M_2(ℂ)`, with
> multiplicity `k(x) = 1`, not a multi-copy direct sum.

For a standalone one-qubit site, the standard quantum-information
meaning is `ℂ²` with `M_2(ℂ)` acting irreducibly. The k = 1
selection is the intended reading of the framework phrase "a qubit at
every lattice site." Under the qubit reframe, Axiom 1's commitment is
**not** "any Cl(3) module per site (with k open)" but rather "one
qubit per site (k = 1 fixed)".

Relative to the weaker algebra-only reading, this is a strengthening
of Axiom 1's usable content, not a separate axiom. (R1) was implicit
in the framework's one-qubit-per-site intent — every site is a qubit,
not some multi-copy alternative — and is now ratified in explicit
framework-rule text so the audit lane can read it as load-bearing.

### Load-bearing status

(R1) is recorded as an **explicit framework rule**, on the same
authority surface as Axiom 1 itself. It is:

- **Load-bearing**, not definitional: it constrains the per-site
  multiplicity index k(x) beyond what "per-site algebra = M_2(ℂ)"
  alone constrains
- **Not derivable from operator-algebra structure alone**: both
  k = 1 and k ≥ 2 are admissible Cl(3) modules on the abstract
  surface, so the selection is a framework-level commitment, not a
  theorem
- **Explicitly ratified by the framework author / repo owner** as
  Axiom 1 content consistent with the one-qubit-per-site reading
  recorded in this hardening note

### Re-audit candidates (no automatic promotion)

Under (R1) as load-bearing Axiom 1 content, the following rows should
be eligible for independent re-audit or follow-up audit classification.
This section only identifies the admission that (R1) may remove if
the audit lane accepts the ratification as load-bearing authority:

- `staggered_dirac_substep1_u4_conditional_single_module_narrow_bounded_note_2026-05-17`
  — Conditional sub-claim (C1) "if k = 1, dim H_x = 2" becomes a
  re-audit candidate with the `k = 1` premise supplied by (R1).
- `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16`
  — U4 admission ("per-site Hilbert IS Cl(3) faithful complex irrep
  on Z^3 substrate") is a candidate for removal if audit accepts (R1)
  as the relevant Axiom 1 content.
- `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17`
  — Same U4 admission is a candidate for removal under the same
  re-audit condition.
- `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` — dim 2
  should be re-audited with (R1) as the proposed Axiom 1 authority for
  the per-site `H_x = ℂ²` premise.
- `no_per_site_bosonic_ccr_theorem_note_2026-05-02`,
  `no_per_site_chirality_theorem_note_2026-05-02`,
  `pauli_group_order_theorem_note_2026-05-02`,
  `q_integer_spectrum_theorem_note_2026-05-02`,
  `per_site_su2_spin_half_theorem_note_2026-05-02` — all consume the
  per-site-dim = 2 result; if the parent dim-2 row audits clean under
  (R1), these become dependency-chain re-audit candidates.
- `multisite_pauli_group_theorem_note_2026-05-02` is not listed as
  closed by (R1) alone because its audit history includes a separate
  minimal-generator issue. It should be handled only if a later audit
  packet addresses that independent obstruction.
- `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20`
  — the auditor's follow-up note suggested this row could be
  reconsidered as `audited_decoration` under
  `cl3_complexification_split` if the ratification path is accepted.

This list does **not** retag any of those rows by itself. Each
re-audit is an independent audit-lane decision. (R1) supplies the
strengthened axiom reading; the audit lane applies it.

### What (R1) does not commit to

(R1) does **not** commit to:

- A specific Hamiltonian, dynamics, or evolution rule
- A specific measurement instrument selection by itself; the separate
  LSP-projective ratification below addresses only ideal unrefined
  sharp projective measurements
- A specific record-formation map or persistent-record kernel
- The staggered-Dirac realization gate's substeps 2-4 (Kawamoto-Smit
  taste structure, substrate-fundamentality, physical-species bridge)
- Any matter content beyond the per-site qubit algebra

These remain in their own derivation lanes. (R1) closes only the
multiplicity-selection question at the per-site axiom level.

### What this hardens

This section converts the auditor's "if the qubit reframe is
treated as a load-bearing axiom" conditional into a **standing
framework rule**. The audit lane is now able to read Axiom 1 as
carrying the k = 1 selection by axiom-rule status, on the same
authority surface as the per-site M_2(ℂ) commitment itself.

(R1) is the framework's explicit response to the audit verdict on
U4 closure. The reviewer of this PR is asked to confirm that, on
land, Axiom 1 will be read as carrying (R1) as load-bearing — not as
a relabeling.

## Hardening III: LSP-projective instrument selection (load-bearing ratification, 2026-05-22)

### Background — the Lüders bridge flag

The audit verdict on
`luders_rule_from_composition_consistency_note_2026-05-20` recorded a
conditional status because the source note used the sequential product

```text
M_{P,E} = P E P
```

without a retained framework authority selecting the corresponding
measurement instrument. A later conditional bridge,
`luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22`,
showed the algebraic implication with a runner: **if** the projective
measurement Kraus operator is `K_P = P`, then the sequential effect is
`K_P† E K_P = P E P`. The same runner also exhibited twisted
alternatives, confirming that the selection is load-bearing rather
than forced by Axiom 1 and Axiom 2 alone.

The framework now ratifies the narrow, standard projective-measurement
selection needed by that bridge.

### Ratification clause

For an **ideal unrefined sharp projective measurement** of an
orthogonal projection `P ∈ A_Λ` on a finite qubit-lattice region, the
framework's projective-measurement instrument is the Lüders operator

```text
K_P := P
```

and therefore the sequential composition of outcome `P` followed by
effect `E` is

```text
M_{P,E} := K_P† E K_P = P E P.
```

Equivalently, on states this is the unnormalized operation
`ρ -> P ρ P`, with the usual normalization by `tr(Pρ)` when a
conditioned post-measurement state is required and `tr(Pρ) != 0`.

### Scope boundary

LSP-projective is a **projective-only framework rule**, not a universal
instrument-selection theorem. Its scope is exactly:

- ideal, sharp projective measurement of a projection `P`
- unrefined Lüders measurement, not a fine-grained von Neumann
  refinement later coarse-grained to `P`
- no additional outcome-dependent unitary inside the `P` subspace
- no extra decoherence channel or apparatus back-action folded into the
  ideal projective measurement act

Outside that scope, the framework remains open:

- non-projective POVMs, including weak measurements, ancilla-coupled
  measurements, and smeared lattice observables, still require their
  own instrument-selection rule
- real apparatus disturbances may be modeled by richer instruments or
  by dynamics around the ideal measurement
- the existing Stinespring/Kraus construction may still take arbitrary
  Kraus families as input for non-projective or apparatus-specific
  contexts

### Why this is a framework rule, not a theorem

The literature on sequential products shows that effect-algebra
sequential products are not unique. The qubit algebra plus the `Z^3`
spatial substrate alone do not force `K_P = P`; alternative projective
instruments with the same effect can include refinements,
outcome-dependent unitaries, or other instrument structure. The
framework therefore records LSP-projective as a **selection**: for the
ideal unrefined projective case, use the standard Lüders instrument and
do not add hidden measurement rotations or refinements.

This is the conventional physics reading of an ideal sharp projective
measurement on a qubit system. The selection is obvious in that
standard setting, but it remains load-bearing for the audit graph
because it chooses one instrument among mathematically allowed
alternatives.

### Load-bearing status

LSP-projective is recorded as an **explicit framework rule** on the
same authority surface as the qubit axiom hardening text. It is:

- **Load-bearing**, not merely definitional: it selects the projective
  measurement instrument needed to read `M_{P,E} = P E P`
- **Narrowly scoped**: ideal unrefined sharp projective measurements
  only
- **Not derivable from Axiom 1 and Axiom 2 alone**: the rule supplies a
  standard measurement selection, not a new theorem
- **Explicitly ratified by the framework author / repo owner** as
  framework-rule content consistent with the one-qubit-per-site
  reading recorded in this hardening note

### Re-audit candidates (no automatic promotion)

Under LSP-projective as load-bearing framework-rule content, the
following rows should be eligible for independent re-audit or follow-up
audit classification. This section only identifies the admission that
LSP-projective may remove if the audit lane accepts the ratification as
load-bearing authority:

- `luders_rule_from_composition_consistency_note_2026-05-20` — the
  audited conditional Lüders parent whose current blocker is the
  missing bridge authority for `M_{P,E} = P E P`.
- `luders_sequential_product_conditional_bridge_narrow_theorem_note_2026-05-22`
  — the conditional bridge showing that `K_P = P` implies `P E P` and
  exhibiting non-Lüders alternatives.
- `born_rule_from_gleason_busch_derivation_note_2026-05-20` — only as
  a downstream re-evaluation candidate after the Lüders/projective
  bridge is independently re-audited; the Born chain may still have
  other blockers.

This list does **not** retag any row by itself. Each re-audit is an
independent audit-lane decision. LSP-projective supplies the approved
framework-rule selection; the audit lane applies it.

### What LSP-projective does not commit to

LSP-projective does **not** commit to:

- a specific Hamiltonian, dynamics, or measurement schedule
- a universal instrument-selection rule for POVMs
- a persistent-record map or record-formation kernel
- an ontic interpretation of collapse beyond the operational Lüders
  update for the ideal projective case
- any Born-rule promotion by itself

These remain in their own derivation lanes. LSP-projective closes only
the ideal projective instrument-selection question.

## What this file is not

- Not a derivation. The retained narrow theorems are cited from
  existing audit-ratified content.
- Not a numerical-prediction change.
- Not an additional axiom. The algebraic `M_2(ℂ) ≅ Cl(3,0)` content
  is unchanged from `MINIMAL_AXIOMS_2026-05-03.md`; this note records
  the explicit (R1) k = 1 selection ratification inside Axiom 1's
  qubit reading and the LSP-projective ideal projective measurement
  selection as framework-rule content.
- Not a rejection of the `Cl(3)`-framing literature in the repo.
  That literature reads cleanly under the qubit identification by
  the retained equivalence.
- Not an automatic promotion of any audited_conditional row.
  (R1) and LSP-projective supply strengthened framework readings;
  downstream re-audits are independently owned by the audit lane.

## Citation-graph note

Upstream (all retained):
- `cl3_complexification_split_narrow_theorem_note_2026-05-10`
- `cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10`
- `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10`
- `cl3_color_automorphism_theorem` (retained_bounded)

Plain-text pointer references (NOT load-bearing deps; recorded
for navigation, not for citation-graph dep tracking):

- `MINIMAL_AXIOMS_2026-05-20.md` — canonical axiom doc; (R1)
  applies to Axiom 1 of this doc
- `U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md`
  — the audited_renaming row whose audit-lane follow-up note
  ("ratification via QUBIT_AXIOM_HARDENING") motivated (R1)
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — open-gate
  parent whose substep-1 U4 bridge is the target of the re-audit path
  enabled by (R1)
- `LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md`
  — conditional LSP-projective bridge with runner-backed algebra and a
  non-Lüders counterexample
- `LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md` —
  audited_conditional Lüders parent targeted by the LSP-projective
  re-audit path
- The rows listed under "Re-audit candidates"

This note does not modify any retained row. It records the
defense of the canonical A1 statement against the "vocabulary
substitution" framing using existing retained-grade content, and
ratifies (R1) as the load-bearing k = 1 selection plus
LSP-projective as the ideal projective measurement selection for
re-audit consumption by the audit lane.
