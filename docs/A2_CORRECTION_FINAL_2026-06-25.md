# A2 (Quantum) — Final Minimal Correction (PROPOSAL)

- **Type:** PROPOSAL (axiom transparency correction).
- **Status:** `hypothetical_axiom_status` (`proposal_allowed=false`). Sets **NO** audit status; owner + audit lane hold sole authority over disposition, tier, and any landing.
- **Date:** 2026-06-25
- **Touches NO canonical / audit / publication file.** Does not edit `docs/MINIMAL_AXIOMS_*.md`, `docs/audit/data/**`, `AUDIT_LEDGER.md`, `AUDIT_QUEUE.md`, `MISSING_DERIVATION_PROMPTS.md`, any `*_EFFECTIVE_STATUS.md`. Supersedes the four-clause draft `A2_MINIMAL_CORRECTION_PROPOSAL_2026-06-24.md` (withdrawn — see Provenance).

---

## THE CHANGE

**Current canonical A2** (`MINIMAL_AXIOMS_2026-06-05.md`):
> [A2] QUANTUM. At each site the primitive local degree of freedom is one qubit; the one-site operator algebra is **`M₂(C)`, equivalently `Cl(3,0)` in its real-algebra reading**. (Posited to supply ONLY the one-site algebraic carrier — explicitly NOT a dynamics, composition beyond lattice placement, measurement instrument, Born rule, species identification, gauge group, particle content, or observable bridge.)

**Proposed A2 (final):**
> [A2] QUANTUM. At each site the primitive local degree of freedom is one qubit; the one-site operator algebra is the **complex `*`-algebra `M₂(C)` with its standard Hermitian (conjugate-transpose) involution**. (Posited to supply ONLY the one-site algebraic carrier — explicitly NOT a dynamics, composition beyond lattice placement, measurement instrument, Born rule, species identification, gauge group, particle content, or observable bridge.) *(Its real Clifford form `Cl(3,0) ≅ M₂(C)` as real `*`-algebras is a cited theorem, available downstream, not posited here.)*

**Net delta (exactly two axiom-text edits + one appended non-primitive pointer):**
1. `M₂(C), equivalently Cl(3,0) in its real-algebra reading` → `the complex *-algebra M₂(C) with its standard Hermitian (conjugate-transpose) involution`.
2. Appended cited pointer: the `Cl(3,0) ≅ M₂(C)` real-algebra isomorphism is a downstream theorem, not posited.

Bare qubit/`M₂(C)` content, tier (axiom), and the disclaimer parenthetical are **unchanged**. No companion supplied-vs-derived note is added (the discipline is not being violated downstream — see Impact).

## WHY

A blind panel raised four concerns about the current text, **all flowing from the one clause `, equivalently Cl(3,0) in its real-algebra reading`:** (C1) the `Cl(3,0)` real form pre-stages a reality/conjugation (`K`/CPT) structure the Record axiom A3 should own; (C2) it foregrounds latent `Spin(3)=SU(2)` (Cl(3,0)'s even subalgebra) in tension with "NOT a gauge group"; (C3) it invites reading the complex unit `i` as the Clifford pseudoscalar `ω`; (C4) its grade-3 vector subspace is silently the same 3 as the spatial `Z³` (an A1↔A2 coupling).

**Dropping that one clause neutralizes all four at the axiom level** — `M₂(C)` as a bare complex `*`-algebra foregrounds no real form, no grading, no pseudoscalar, and no intrinsic "3" — while each fact survives as a true **theorem about** `M₂(C)` (the supplied-vs-derived posture). C4's removal is a genuine *soundness* gain: it deletes a hidden axiom-to-axiom dimension coupling. This removes **no algebra** — `M₂(C)` *is* `Cl(3,0)` up to isomorphism; it removes the *license to read the Clifford grade/real-form/pseudoscalar off the axiom as primitive*.

## THE TWO ADDED FACTS (both verified)

1. **Pinning the standard Hermitian (conjugate-transpose) involution is mandatory, not over-specification.** A bare `*`-algebra leaves *which* involution unspecified, and the choice is load-bearing for reality/CPT. `M₂(C)` admits inequivalent involutions; the transpose-type involution **fails the C\*-axiom** — e.g. `a = [[1,i],[i,−1]] ≠ 0` has `aᵀa = 0` (verified), so it is not positive — whereas the conjugate-transpose is the C\*-adjoint (`a†a ⪰ 0`, eigs `{0,4}`; verified). The Hermitian adjoint is the qubit's physical, forced involution; naming it removes the ambiguity.
2. **`Cl(3,0) ≅ M₂(C)` as real `*`-algebras.** Verified: `dim_R = 2³ = 8 = ` (4-over-C of `M₂(C)`); Pauli rep `e_i = σ_i` (`e_i² = +I`, anticommuting); pseudoscalar `ω = e₁e₂e₃ = iI` is central with `ω² = −I` and `ω† = −ω`; signature-correct (vs `Cl(0,3) = H⊕H`). The **"real `*`-algebras"** qualifier is mandatory (dimensions match over R, not C) and is what keeps the `i ↔ ω` story strictly on the theorem side (blocks C3 from re-leaking).

## WHY THE PINNED INVOLUTION DOES NOT RE-OPEN C1 (corrected rationale)

The C\*-adjoint **underdetermines** A3's antilinear conjugation `K`: multiple inequivalent conjugations (e.g. `J₁(X)=X̄` fixing `M₂(R)`; `J₂(X)=σ_y X̄ σ_y` fixing a different real form) are compatible with the **same** conjugate-transpose adjoint (verified). So the adjoint selects no real form, no `K`, no `K²=±1` — all free for A3.

The clean separator is **structural, not "linear vs antilinear"** (a correction to an earlier draft's rationale — the adjoint is itself conjugate-linear, `(λA)† = λ̄A†`, verified):
- The adjoint `†` is a conjugate-linear **anti-automorphism** (`(AB)† = B†A†`); its fixed set (Hermitian matrices) is a real **Jordan** space that is **not a subalgebra**, so `†` defines **no real form** of the algebra. It supplies a **positivity / inner-product** datum.
- A3's `K`/CPT is a conjugate-linear **automorphism** (`K(AB)=K(A)K(B)`); its fixed set (e.g. `M₂(R)`) **is** a real subalgebra — a genuine reality structure.
- Structurally `† = transpose ∘ K̄`; recovering `K` from `†` requires independently choosing the transpose (a real basis / symmetric form), which A3 supplies. Equivalently: `†` acts on the **operator algebra**; `K` acts on the **state space `C²`** — different objects on different carriers.

**A3 must therefore define `K` as an antilinear automorphism distinct from `†`.**

## HONEST RESIDUE (framing, not a content change)

Committing to a C\*-algebra at all canonically fixes complex conjugation on the center `C·I` and the real Jordan space of self-adjoint observables — i.e. **A2 fixes the reality of *observables* (Jordan/positivity)**, while the **reality of *states* (`K`/CPT/charge conjugation) remains A3's to own.** This thin residue is unavoidable for any honest qubit carrier and is **already implicit in writing `M₂(C)` in the current text too**, so it is not new. The proposal does **not** claim the pin "imports nothing reality-related"; it claims it imports no *state* reality structure / `K`. Likewise, the adjoint supplies an inner-product / positive cone (and lets "observable = self-adjoint" be stated later) but **not** a Born rule or measurement instrument — the carrier-level disclaimer stays honest. (Wording note: the adjoint is the *canonical* C\*-involution — unique up to `*`-isomorphism once the qubit inner product is fixed — not literally "the unique involution.")

## IMPACT (downstream)

The supplied-vs-derived discipline is **not being violated downstream**, so no companion note is needed. Triage + an independent grep found **0 logical reframes**: every consumer either derives the spinor/SU(2)/`K`/grade-3 structure or cites the retained `Cl(3,0)` theorems (`CL3_COMPLEXIFICATION_SPLIT`, `CL3_PAULI_IRREP_UNIQUENESS`, `AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS`), not a free pass off A2.

Caveats (cosmetic, not logical): (a) rows phrased "the Quantum axiom's `M₂(C)≅Cl(3,0)`" should, at point of use, cite the iso theorem rather than the axiom — the appended pointer keeps such references valid; (b) the downstream theorem should name **reversion ↔ conjugate-transpose** as the matching Clifford anti-involution, so a later involution mismatch cannot reintroduce a reality choice at the point of use; (c) a pre-existing labeling drift exists (≈10 rows use a *legacy* numbering `A1 = Cl(3)` / `A2 = Z³`, the reverse of the current `A1 = Lattice` / `A2 = Quantum`) — flagged, out of scope for this edit.

## PROVENANCE (validation)

- **Panel 1** (`A2_CORRECTION_BEFORE_AFTER_PANEL_VERDICT_2026-06-24.md`, Opus 4.8): the original four-clause draft = improvement but `revise_substantially` — scoping belongs out of the axiom; `i=ω` over-reach; "INTENDED" teleology. Four-clause draft **withdrawn**.
- **Codex `gpt-5.5`** (`A2_CORRECTION_CODEX_GPT55_CROSSCHECK_2026-06-24.md`): independent, same direction (repackage; soften `i=ω`; SU(2) algebraic-only).
- **Panel 2** (`A2_MINIMAL_EDIT_PANEL_VERDICT_2026-06-25.md`, Opus 4.8): minimal drop-`Cl(3,0)` edit = 10/10 improvement, 0/10 keep-primitive; `tweak_then_ship`, lone mandatory tweak = pin the involution.
- **Panel 3** (`A2_FINAL_BEFORE_AFTER_PANEL_VERDICT_2026-06-25.md`, Opus 4.8, **max effort**): this final form = 10/10 improvement, 4 `yes_correct` / 6 `minor_tweak` / 0 `no`; C1–C4 all stay neutralized; both math facts correct; **axiom text judged final**; only the justifying prose needed the anti-automorphism/positivity rewording applied here.
- Numerical checks (this proposal): `σ₁σ₂σ₃ = iI`, `ω²=−I`; `(λA)†=λ̄A†`, `(AB)†=B†A†`, `†=transpose∘K̄`; transpose-involution `aᵀa=0` (fails C\*) vs `a†a⪰0`.

## WHAT THE OWNER + AUDIT MUST CHECK

1. Tier unchanged (axiom); bare posit byte-equivalent (qubit = `M₂(C)`); disclaimer verbatim.
2. The two added facts (C\*-adjoint involution; `Cl(3,0)≅M₂(C)` as real `*`-algebras) — re-verify if desired.
3. C1 firewall rests on the corrected rationale (adjoint = anti-automorphism/positivity, underdetermines `K`), and A3 defines `K` as an antilinear automorphism distinct from `†`.
4. One-time confirmation no downstream axiom/canonical row depends on the *named* `Cl(3,0)` form as primitive (consistent with the 0-reframe triage, not re-adjudicated here).
5. The cited `Cl(3,0)` theorem, where used, names reversion ↔ conjugate-transpose.

**Independent audit required. Sets no audit status; owner + audit lane sole authority.**
