# Real Record Readout (No Intrinsic i) Unifies Gauge Invariance, Phase-Blindness (P2), and the Flavor 2-Sector — PROPOSAL + Narrow Theorem Note

**Date:** 2026-06-04 (banked 2026-07-06)
**Type:** meta
**Claim type:** meta (historical axiom-proposal provenance note; non-claim source)
**Scope boundary:** Historical/provenance banking only. This file records a
pre-reset proposal draft recovered from an uncommitted 2026-06-08-era stash;
it does not add, approve, or revise any framework axiom, primitive, theorem,
dependency edge, or publication surface.
**Audit boundary:** Independent audit lane only. This note proposes no audit
verdict and sets no `effective_status`.
**Status:** **SUBSUMED PROPOSAL.** The proposed clarification was never
applied and never entered the ledger; the 2026-06-29 foundation reset
independently absorbed its intent (see Subsumption Posture below). Sets
**NO** audit status, claims no theorem, grants no promotion. Owner + audit
lane hold sole authority over disposition.
**Touches NO canonical / audit / publication file.** Does not edit
`docs/MINIMAL_AXIOMS_*.md`, `docs/audit/**`, `MISSING_DERIVATION_PROMPTS.md`,
any `*_EFFECTIVE_STATUS.md`, and runs no tracked-output rewriter.
**Primary runner:**
[`scripts/audit_companion_real_record_no_i_unification_2026_06_04.py`](../scripts/audit_companion_real_record_no_i_unification_2026_06_04.py)
(13 PASS / 0 FAIL; cache
[`logs/runner-cache/audit_companion_real_record_no_i_unification_2026_06_04.txt`](../logs/runner-cache/audit_companion_real_record_no_i_unification_2026_06_04.txt),
regenerated 2026-07-06).

## Subsumption Posture (2026-07-06)

This note was drafted 2026-06-04 against the then-current axiom memo
(`MINIMAL_AXIOMS_2026-06-04.md`), whose Record axiom called the readout a
"real scalar" functional. The proposal targeted the ambiguity in that word
"real" (real-valued vs. real-as-operator) and asked for the real-as-operator
reading: no intrinsic complex unit in the record, with the imaginary unit
assigned to the per-site algebra axiom. The draft was stashed uncommitted on
2026-06-08 and recovered 2026-07-06; it never entered the audit ledger.

The 2026-06-29 foundation reset (`MINIMAL_AXIOMS_2026-06-29.md`) absorbed the
proposal's intent without adopting its sentence:

- The sentence the proposal wanted to sharpen no longer exists. The Record
  axiom no longer describes a real scalar functional of observables; a record
  locks exactly one admissible local possibility, and "a readout value is
  determined by record content alone."
- The division of labor landed in stronger form on the Qubit side: "A
  `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
  adds no further primitive structure," with "No possibility is privileged.
  Possibilities are distinguished by the supplied algebraic structure alone."
  Under this text the complex unit is presentational, not primitive — beyond
  the proposal, which still assigned `i` to an axiom.
- The proposal's operational clause (a record cannot resolve a pair related
  only by complex conjugation) is derivable from the current text: complex
  conjugation is implemented by a real-algebra automorphism preserving all
  supplied structure, so no axiom-supplied datum distinguishes a conjugate
  pair, and readout reads record content alone.
- The three payoffs arrived by other routes. (A) gauge invariance remains the
  standing Record corollary. (B) phase-blindness landed as the additive-even
  phase-free readout theorem (retained grade; part of the theta Tier-A
  retirement discharge basis, 2026-07-05), with the axiom memo explicitly
  keeping P2/phase-blindness outside axiom content. (C) the flavor 2-sector
  is carried by the K/CPT-orbit and supplied-context bridge notes, with the
  `AC_phi_lambda` decomposition chain rebased onto the four-axiom surface
  (2026-07-05) and `r = 1/2` filed as a recorded branch; the Layer-2
  equipartition residual named in section 4 below remains the open
  derivation target it declared.

No axiom action is open from this note. One observation is recorded without
weight: no current main text pins the Record axiom's "scalar readout" as
real-valued; the operative content lives in the landed phase-free theorems.

The body below is preserved verbatim from the 2026-06-04 draft. Its internal
links and axiom references are to 2026-06-04-era surfaces (in particular
`MINIMAL_AXIOMS_2026-06-04.md`, since superseded) and are retained as written
for provenance.

---

## 0. One-paragraph summary

The Record axiom currently states the record readout is a **real scalar**
functional. That word "real" is ambiguous between *real-valued* (the number is
real; the observable may be complex/Hermitian, carrying the imaginary unit `i`)
and *real-operator* (the readout carries **no intrinsic `i`** — it is
conjugation-symmetric). This note proposes sharpening it to the **real-operator**
reading, with the division of labor that **`i` belongs to the Quantum axiom**
(the per-site `M_2(C)`) and **the Record is the real readout of that complex
structure.** The proposal's load-bearing payoff: a *single* clarification forces,
as one principle, (A) gauge invariance, (B) phase-blindness/P2, and (C) the
flavor 2-sector (Koide `Q=2/3` structure). Frame, phase, and chirality are the
same object — the imaginary part the real record drops. The exact Koide value
`r=1/2` is **not** forced by the clarification; it reduces to the explicit
residual that the 2-sector record-bit is *full* (equipartition), to be derived,
not axiomatized.

## 1. The proposed Record-axiom clarification (for review; NOT applied)

> **Proposed clause (real-operator readout).** The record readout is real *as an
> operator*: the record functional and its underlying recorded observables carry
> no intrinsic complex unit `i`; equivalently they are invariant under the
> conjugation (reality) operation, so the record cannot resolve a pair related
> only by complex conjugation. The imaginary unit `i` is supplied solely by the
> **Quantum** axiom (the per-site `M_2(C) ~= Cl(3,0)`); the **Record** axiom is
> the real readout of that complex structure.

This is a **sharpening along the existing intent** ("a real scalar record" = a
real classical fact), not a new flavor-specific axiom: it is a general statement
about records, and its consequences (§3) span gauge, observable-principle, and
flavor. Owner approval is required before any application; this note does not
apply it.

## 2. Setup (primitives)

The C₃ generation structure: the three generations carry the cyclic group C₃
(generator `U`, `U^3=I`). Over `C`, `U` has the three distinct eigenvalues
`{1, ω, ω̄}`; the `ω`/`ω̄` pair is the **chirality** (the orientation of the
doublet rotation). Over `R`, C₃ has exactly two irreducible representations: the
**trivial** (1-d, the singlet) and the **standard** (2-d, the doublet — a 120°
rotation, irreducible over `R`). A "record" is a coarse-graining (a set of
orthogonal projectors) of this space; "stable" means it commutes with the
C₃-symmetric interaction (a circulant `aI + bU + b̄U²`).

## 3. The theorem (conditional on §1): one principle, three consequences

> **Theorem (real record strips the imaginary part — frame, phase, chirality).**
> Under the proposed real-operator Record clarification (§1):
>
> - **(A) Gauge invariance.** The real/relational record cannot encode the
>   unfixed local **frame** (the relative orientation between sites). This is the
>   existing Record corollary (gauge invariance of observables = commutant of the
>   per-vertex Gauss-law generators); the clarification names its mechanism (the
>   record drops the frame's `i`-valued relative phase).
> - **(B) Phase-blindness / P2.** For the amplitude `Z = det(D+J) ∈ C*`, a real
>   readout keeps only the real part `log|Z|`, not `i·arg Z`: a continuous
>   single-valued real additive functional kills the compact phase `U(1)`
>   (`c·θ = c·(θ+2π) ⇒ c=0`). So the readout depends on `|Z|` alone — this **is**
>   the P2 phase-blindness premise of the observable-principle parent, now a
>   consequence of the real readout rather than a separate admission.
> - **(C) Flavor 2-sector (Koide structure).** The real C₃-invariant operator
>   algebra is 2-dimensional `{I, U+Uᵀ}`; its common eigenspaces are the singlet
>   (1-d) and the doublet (2-d, a **degenerate** eigenspace), so a real record
>   resolves **only** singlet | doublet — the unique nontrivial real
>   C₃-invariant partition. Resolving the three generations individually requires
>   the generator `i(U−Uᵀ)`, which is Hermitian but **purely imaginary** (`i` ×
>   real-antisymmetric) — excluded from a real record. Hence the flavor record is
>   the 2-sector bit, giving the Koide `Q = 1/3 + (2/3)r` structure.

**Unification.** (A)/(B)/(C) are the *same* statement: the imaginary part the
real record drops is, respectively, the **frame** (gauge), the **phase** (P2),
and the **chirality** (flavor). The `i` is the Quantum axiom's; the Record is its
real shadow. The runner verifies the load-bearing algebra of (B) and (C) and the
consistency of the division of labor (Part-by-part, 13/0).

## 4. What is NOT forced — the honest residual (Layer 2)

The clarification forces the 2-sector **basis** (Layer 1), **not** the exact
Koide value `r = 1/2`. `r = |b|²/a²` is the doublet/singlet **power ratio** of
the state, which the real record reads but does not fix. `r = 1/2` is the
**equipartition** point — the 2-sector record-bit at *full* entropy
(`p_singlet = p_doublet = 1/2`; the runner confirms the 2-sector entropy peaks at
`r ≈ 0.5002`). Whether the record-bit is full (equipartitioned) is the **explicit
remaining residual**, to be **derived** (a max-entropy / record-objectivity
argument), **not** axiomatized. This note does not close it.

Relatedly, the chirality `δ = arg b` (and the absolute masses) live on the
**Quantum (complex)** side: `Q` is `δ`-independent, so the real-record value
`r` survives in the actual `δ ≠ 0` (chiral, non-degenerate) mass spectrum — the
record forgets the chirality the masses keep.

## 5. What this does NOT claim / scope

- It does **not** apply the axiom clarification (PROPOSAL only; owner approval
  required).
- It does **not** force `r = 1/2` (Layer 2 residual, §4).
- It does **not** touch `β = 6`, the gauge coupling, or the absolute mass scale
  (the *dynamical* sector — a separate wall no readout principle addresses).
- It does **not** consume PDG / fitted / lattice-MC / `β = 6` inputs; `δ = 2/9`
  appears only as a comparator.
- It does **not** promote, demote, or set the audit status of any row
  (`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, the gauge-invariance corollary, the
  flavor/Koide rows, the staggered-Dirac gate, or any other). Audit lane is the
  only status authority.

## 6. Dependencies and citations

**Load-bearing (markdown-link) authorities:**

- The Record axiom being clarified:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md).
- The owner-approval policy for axiom content:
  [`audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md).
- The observable-principle parent whose P2 this would discharge:
  [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  (live `unaudited`).
- The prior P2 sector-resolution (this note gives the deeper real-readout reason):
  [`OBSERVABLE_PRINCIPLE_P2_PHASE_BLINDNESS_SECTOR_RESOLVED_NARROW_THEOREM_NOTE_2026-06-04.md`](OBSERVABLE_PRINCIPLE_P2_PHASE_BLINDNESS_SECTOR_RESOLVED_NARROW_THEOREM_NOTE_2026-06-04.md).
- The Frobenius isotype-split no-go (the singlet:doublet weight is free — Layer 2):
  [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  (live `retained_no_go`).

**External / standard facts (cited as comparator, reproven in the runner):**

- Real irreducible representations of `C₃`: trivial (1-d) ⊕ standard (2-d); the
  standard rep is `R`-irreducible (a 120° rotation has no real eigenvector).
- A continuous homomorphism from the compact `U(1)` to `(R,+)` is trivial
  (Pontryagin/character theory: `\hat{T} = Z`).

**See-also (non-load-bearing, backticked):**
`GAUGE_INVARIANCE_OF_OBSERVABLES_COROLLARY` family (gauge-from-Record, #2667),
`KOIDE_DELTA_RADIAN_PERIOD_PHYSICAL_NOT_VACUOUS_NARROW_THEOREM_NOTE_2026-06-04.md`.

### Source-note boundary

**Hypothesis set used:** (1) the proposed real-operator Record clarification (§1,
under review, not applied); (2) the C₃ generation structure (framework); (3) real
representation theory of C₃ (external); (4) `Hom_cont(U(1),(R,+)) = {0}`
(external). No fitted/PDG/`β=6` inputs.

**Forbidden-imports check:** introduces **no** new framework axiom (it *proposes*
a clarification of the existing Record axiom, for review, not applied) and **no**
new repo vocabulary or class tags. Uses standard terms ("real irrep," "circulant,"
"chirality," "Pontryagin") and repo-canonical "P2," "phase-blindness," "2-sector,"
"singlet/doublet."

**No-promotion statement:** this note sets no audit status and applies no axiom
change. The audit lane and the owner (for axiom content) are the only
authorities.
