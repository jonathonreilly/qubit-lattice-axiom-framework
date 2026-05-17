# Observable-Principle P1 Bridge — Route D Sharpened No-Go Note

**Date:** 2026-05-17
**Claim type:** no_go
**Scope:** Sharpened structural no-go consolidating the convergent finding
of four prior route attempts (Routes A, B, C, E) on the P1 admitted premise
(scalar additivity on independent subsystems) of
[`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md).
This note **does not claim P1 is false**. It claims, in the sharpened
structural form documented below, that P1 is **not derivable** from the
framework's current retained authority chain combined with the four
families of standard mathematical scaffolds enumerated in §2
(operator-algebraic, information-theoretic, framework-internal,
cross-disciplinary categorical/topological/tropical). The
counterexample family `F_p[J] = r(J)^p` for `p in R \ {0}` is the
universal obstruction across all four routes.
**Status authority:** source-note proposal only; independent audit lane
sets any audit result and pipeline-derived effective status.
**Runner:**
[`scripts/frontier_observable_principle_p1_bridge_route_d_sharpened_no_go_narrow.py`](../scripts/frontier_observable_principle_p1_bridge_route_d_sharpened_no_go_narrow.py)

## 0. Honest framing up front

This note records the **structural consolidation** of four independent
prior closure attempts on P1, each of which converged on the same
obstruction from a different direction:

- [Route A (PR #1373)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1373):
  operator-algebraic external scaffold (Hilbert tensor product
  factorization, Grassmann determinant block factorization, trace-state
  factorization on type II_1 factors, Reeh-Schlieder cyclicity, cluster
  decomposition).
- [Route B (PR #1368)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1368):
  information-theoretic external scaffold
  (Shannon 1948, Khinchin 1957, Aczel-Daroczy 1975, Cauchy's logarithm
  functional equation).
- [Route C (PR #1402)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1402):
  framework-internal retained-primitive audit (each catalog retained
  framework theorem tested against the explicit Route-C exclusion
  question).
- [Route E (PR #1406)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1406):
  Tao-style cross-disciplinary stretch search (Atiyah-Singer index,
  K-theory / Euler characteristic, Cramer rate function, tropical
  max-plus, anabelian homology, geometric quantization, Legendre / free
  energy, synthetic differential geometry, Tarski first-order logic,
  Tao blog functional equations).

All four routes landed as `bounded_theorem` with explicit admission that
the route did NOT close P1. Routes A/C/E used the explicit
counterexample family `F_p[J] = r(J)^p` (for real `p`) to demonstrate
the structural obstruction; Route B identified that every classification
theorem in the Shannon-Khinchin-Aczel-Daroczy class takes additivity as
a hypothesis input.

This Route D no_go consolidates those four findings into a single
sharpened structural statement: P1 is **not derivable** from the
current retained authority chain combined with standard mathematical
scaffolds. The consolidated statement is sharper than any of the
four sub-routes because it is the combined enumeration of all four
independent obstructions, and weaker than a global claim of
falsity because it is scope-bounded to the explicitly enumerated
authority chain + four scaffold families.

This note explicitly DOES NOT claim P1 is false. It does NOT
promote or alter the status of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, `CPT_EXACT_NOTE.md`, or any
upstream row. The audit row of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` stays `audited_conditional`
with P1 admitted; this no_go rigorously documents that closure via the
four attempted scaffold families is structurally foreclosed, leaving
the legitimate forward paths in §5.

## 1. Statement

### 1.1 The sharpened no-go theorem

> **Theorem (Route D, sharpened structural no-go on P1).**
> Let `Z[J] := det(D + J)` denote the staggered Grassmann partition
> function on an exact minimal hierarchy block, and let
> `r(J) := |Z[J]| > 0` (real positive). Let
> `A_RETAINED` denote the current retained framework authority chain
> (i.e., the set of authority rows whose live effective_status on
> `docs/audit/data/audit_ledger.json` is `retained`, `retained_bounded`,
> `retained_no_go`, or `retained_pending_chain`). Let `S_STD` denote the
> four families of standard mathematical scaffolds:
>
> - `S_OA`: operator-algebraic scaffolds (Hilbert tensor product
>   factorization, type II_1 trace-state factorization, Reeh-Schlieder
>   cyclicity, cluster decomposition);
> - `S_IT`: information-theoretic uniqueness theorems
>   (Shannon-Khinchin-Aczel-Daroczy classification, Cauchy logarithm
>   functional equation);
> - `S_FI`: framework-internal retained primitives (reflection
>   positivity, anomaly-forces-time, CL3 color automorphism, gauge
>   closure, generation algebra, scale-invariance, max-entropy
>   obstruction);
> - `S_CD`: cross-disciplinary categorical/topological/tropical
>   scaffolds (Atiyah-Singer index, K-theory / Euler characteristic,
>   homology direct sum, Cramer rate function, tropical max-plus,
>   geometric quantization, Legendre / free energy, synthetic
>   differential geometry, Tarski first-order, Tao functional-equation
>   classifier).
>
> Then P1 (scalar additivity on independent subsystems for physical
> scalar bosonic observable generators) is **not derivable** from
> `A_RETAINED ∪ S_STD`. The counterexample family
>
> ```text
> F_p[J] := r(J)^p,        p in R \ {0}                                (1)
> ```
>
> is compatible with every primitive in `A_RETAINED ∪ S_STD`: continuous,
> CPT-even (depends only on `|Z|`), multiplicatively factorizing on
> independent subsystems, Hilbert-tensor-product-compatible,
> trace-state-compatible, reflection-positivity-compatible, anomaly-
> compatible, gauge-compatible, max-entropy-class compatible; but
> fails block-additivity for every `p ≠ 0`. Only the `p -> 0` limit
> (`log r`, equivalently `log|Z|`) is additive, and selecting it from
> the family requires the Cauchy classifier (`f(xy) = f(x) + f(y) → c log`),
> which IS P1 in different vocabulary.

### 1.2 What this no-go does NOT claim

This no-go **does not** claim:

- That P1 is false. The counterexample family `F_p` shows that
  multiplicative factorization permits non-additive members; it does
  not show that physical scalar bosonic observables must be one of the
  non-additive members.
- That the additive choice `log|Z|` is wrong. The parent note proves
  `W = log|det(D+J)|` is the unique additive CPT-even continuous
  scalar generator on independent subsystems given P1. This no_go
  agrees with that conditional statement; it documents that the
  selection of "additive" over "multiplicative" (or `r^p`) is the
  admitted classification choice P1.
- That `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` should be demoted.
  Its audit verdict `audited_conditional` already admits P1 as a
  bridge premise; this no_go provides rigorous structural backing
  for the verdict rather than overturning it.
- That no future closure of P1 is possible. The forward paths in §5
  remain legitimate; this no_go forecloses the four scaffold families
  already attempted, not the entire space of derivations.

### 1.3 Scope boundary

This no_go is scope-bounded to:

- The current retained authority chain (live ledger snapshot
  2026-05-17).
- The four scaffold families enumerated in §1.1.
- The Grassmann partition function `Z[J] = det(D+J)` on exact minimal
  hierarchy blocks.
- The scalar functional admissibility class on `r = |Z| > 0`.

Out of scope:

- Promotion or demotion of any cited authority row.
- New axioms or new repo vocabulary (per
  [`feedback_no_new_axioms.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/main/.claude/memory/feedback_no_new_axioms.md) and
  [`feedback_no_new_repo_vocabulary.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/main/.claude/memory/feedback_no_new_repo_vocabulary.md)).
- The `v = 246.28 GeV` numerical readout of the parent note.
- The hierarchy baseline `M_Pl * alpha_LM^16`.
- The measurement comparator `v_meas`.

## 2. The five independent obstructions D1-D5

Each obstruction is individually sufficient to block derivation of P1 from
the corresponding scaffold family. The aggregate is the consolidated
no-go.

### 2.1 D1 — operator-algebraic compatibility (Route A)

**Obstruction.** `F_p[J] = r(J)^p` is consistent with tensor product
Hilbert factorization for all `p in R \ {0}`.

Hilbert tensor product factorization `H = H_A ⊗ H_B` for independent
subsystems gives `Z[J_A ⊕ J_B] = Z_A[J_A] · Z_B[J_B]` (multiplicative).
For any real `p`:

```text
F_p[J_A ⊕ J_B] = r(J_A ⊕ J_B)^p
              = (r(J_A) · r(J_B))^p
              = r(J_A)^p · r(J_B)^p
              = F_p[J_A] · F_p[J_B].                                    (2)
```

So `F_p` is multiplicatively factorizing for every `p`. It is also
continuous (composition of continuous functions), CPT-even (depends only
on `|Z|`), and positive (since `r > 0`). It is therefore
operator-algebraically admissible for every `p`. Block-additivity
`F_p[J_A ⊕ J_B] = F_p[J_A] + F_p[J_B]` holds only when

```text
(r_A r_B)^p = r_A^p + r_B^p.                                            (3)
```

This is a non-trivial constraint on `(r_A, r_B)` and `p`; in particular
it fails for generic `(r_A, r_B)` with `r_A, r_B > 0` unless `p = 0`
(i.e., the `log` representative). The `F_p` family is therefore the
explicit witness that operator-algebraic factorization is compatible
with non-additive scalar functionals. See
[Route A PR #1373](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1373)
for the full operator-algebraic enumeration (Hilbert factorization,
Grassmann determinant block factorization on real-D blocks, type II_1
trace-state factorization, Reeh-Schlieder cyclicity, cluster
decomposition).

### 2.2 D2 — information-theoretic uniqueness theorems require additivity input (Route B)

**Obstruction.** Every published Shannon-Khinchin-Aczel-Daroczy
uniqueness theorem takes additivity (or the equivalent chain rule) as a
hypothesis input and classifies the unique additive functional
satisfying further regularity conditions as `H(p) = -k sum p_i log p_i`.
They do not derive additivity; they classify the additive class.

- Cauchy 1821: `f(xy) = f(x) + f(y) + continuity → c log` — additivity
  hypothesis input.
- Shannon 1948 (Bell Syst. Tech. J. 27): independence-additivity as
  design requirement input.
- Khinchin 1957 Thm 1: hypothesis (K3) is the chain-rule additivity
  hypothesis input.
- Aczel-Daroczy 1975: weakens (K2) but keeps the additivity hypothesis
  input.

Applying any of these theorems to `|Z[J]|` on independent Grassmann
blocks therefore requires assuming additivity as input, then classifying
the unique functional as `c log` as output. This is exactly the parent
note's existing conditional structure: assume P1, conclude
`W = log|det|`. The Shannon route therefore **relabels P1 in
information-theoretic vocabulary; it does not derive P1**. See
[Route B PR #1368](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1368)
for the full enumeration.

### 2.3 D3 — framework retained primitives don't exclude `F_p` (Route C)

**Obstruction.** None of the currently retained framework primitives in
the load-bearing catalog independently excludes the non-additive
counterexample family `F_p` for `p ≠ 1`.

Each retained candidate constrains an aspect of the lattice theory
**orthogonal** to scalar-functional admissibility on the Dirac block:

| Candidate | Live status | Constraint | Excludes `F_p`? |
|---|---|---|---|
| `observable_principle_real_d_block_uniqueness_narrow_theorem_note_2026-05-10` | audited_failed | written X2 embeds P1 (criterion A); audit also rejected the universal uniqueness conclusion | not retained authority; cannot close Route C |
| `axiom_first_reflection_positivity_theorem_note_2026-04-29` | unaudited | measure positivity | no — `F_p > 0` for all `p` on real-D blocks |
| `anomaly_forces_time_theorem` | unaudited | gauge content + spacetime signature | no — orthogonal to scalar functional |
| `cl3_color_automorphism_theorem` | retained_bounded | rep theory | no — orthogonal |
| `graph_first_su3_integration_note` | retained_bounded | gauge axis selection | no — orthogonal |
| `native_gauge_closure_note` | retained_bounded | gauge closure | no — orthogonal |
| `staggered_dirac_realization_gate_note_2026-05-03` | open_gate | gate explicitly open | n/a — gate open |
| `observable_generator_additivity_from_cluster_decomposition_theorem_note_2026-05-10` | unaudited | explicitly admits same selection step | reproduces (A) admission |
| `observable_principle_scale_invariant_source_response_narrow_theorem_note_2026-05-16` | unaudited | imports (X2) wholesale | inherits (A) |
| `bae_max_entropy_retained_bounded_obstruction_note_2026-05-10_baemaxent` | bounded obstruction | max-entropy approaches fail to canonically select | n/a — explicit obstruction |
| `cpt_exact_note` | audited_conditional | CPT-even (P2) on phase blindness | no — `F_p` is CPT-even for all `p` |

The only catalog candidate with explicit scalar-functional content
(`OBSERVABLE_PRINCIPLE_REAL_D_BLOCK_UNIQUENESS`) is now audited_failed;
in any case, its written admissibility class embeds P1 as criterion
`(A)`, so using it to exclude `F_p` begs the question. Combinations of
retained candidates likewise fail: in every combination the embedded
`(A) = P1` would be the load-bearing step.
See [Route C PR #1402](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1402)
for the full audit.

### 2.4 D4 — cross-disciplinary functor-additivity inapplicable (Route E)

**Obstruction.** Standard cross-disciplinary scaffolds that supply
"additivity-on-direct-sums" theorems are inapplicable to `Z[J] in R`
because their additivity is on integer-valued or vector-space-valued
invariants (Pattern D), not on scalar real-valued functionals.

- Atiyah-Singer index `ind(D_1 ⊔ D_2) = ind(D_1) + ind(D_2)`:
  presupposes additivity via the `dim` functor on direct sums of vector
  spaces. `Z[J] = det(D+J) in R` is a single real number; it has no
  direct-sum structure.
- K-theory / Euler characteristic
  `chi(X ⊔ Y) = chi(X) + chi(Y)`: presupposes additivity via the
  Grothendieck ring `K_0`. `Z[J]` is not a `K_0` class.
- Homology direct sum
  `H_*(X ⊔ Y) = H_*(X) ⊕ H_*(Y)`: presupposes additivity via direct
  sums of vector spaces. `Z[J]` is a scalar.
- Synthetic differential geometry / tangent functor
  `T(M × N) = TM ⊕ TN`: presupposes additivity via tangent functor on
  manifolds. `Z[J]` is a scalar, not a manifold.

These four Pattern-D scaffolds therefore have **no native applicability**
to the scalar real-valued partition function. The remaining
cross-disciplinary candidates (Cramer rate, tropical, geometric
quantization, Legendre / free energy, Tao Cauchy functional equation)
are Pattern-L: they invoke `log` explicitly. See §2.5 (D5) below.
See [Route E PR #1406](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1406)
for the full ten-candidate enumeration.

### 2.5 D5 — Pattern L circularity (Routes A, B, C, E)

**Obstruction.** Every cross-disciplinary candidate that attempts to
"select the log representative" of the multiplicative class invokes
`log` explicitly, which IS the Cauchy classifier among continuous group
homomorphisms `(R_+, *) -> (R, +)`, which IS P1 in different
vocabulary.

Pattern-L candidates:

- Cramer rate function `Lambda(X) = log E[e^{lambda X}]`: invokes `log`.
- Tropical dequantization `(*, +) → (max, +)` via `log_b`: invokes `log`.
- Geometric quantization semiclassical action `S_cl = -hbar log Z`:
  invokes `log`.
- Free energy `F = -k_B T log Z`: invokes `log`.
- Tao blog Cauchy classifier `f(xy) = f(x) + f(y) + continuity → c log`:
  invokes `log` as the Cauchy classifier.
- Shannon-Khinchin-Aczel-Daroczy entropy
  `H(p) = -k sum p_i log p_i` (Route B): invokes `log` and presupposes
  additivity.

In each case, the choice of `log` over `(.)^p` (`p ≠ 0`) is the choice
of an **additive** target over a **multiplicative**-only target. That
choice IS P1. The selection step is therefore circular: it presupposes
the additive class as the physical scalar bosonic observable generator
class, which is the admission P1 itself. See
[Route A PR #1373](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1373)
and [Route E PR #1406](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1406)
for the full Pattern-L enumeration.

## 3. Convergence across the four routes

The four prior routes attacked P1 from four structurally distinct
directions and converged on the same admission. The convergence is the
load-bearing evidence for the sharpened no-go:

| Route | PR | Direction | Outcome | Obstruction |
|---|---|---|---|---|
| A | [#1373](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1373) | Operator-algebraic external | `bounded_theorem` | D1 |
| B | [#1368](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1368) | Information-theoretic external | `bounded_theorem` (landed) | D2 |
| C | [#1402](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1402) | Framework-internal | `bounded_theorem` | D3 |
| E | [#1406](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1406) | Tao cross-disciplinary | `bounded_theorem` | D4 (Pattern D) + D5 (Pattern L) |

All four routes record the same explicit counterexample family
`F_p[J] = r(J)^p` (Routes A, C, E directly; Route B implicitly via
the "every uniqueness theorem takes additivity as hypothesis" finding).
All four routes record explicit admission that P1 is NOT closed.

## 4. Verifying the `F_p` counterexample family

The runner verifies the `F_p` counterexample family explicitly at
exact SymPy / Fraction precision, plus the four routes' independent
confirmations, plus the structural enumeration of Patterns L and D, plus
the explicit no-promotion language.

- **T1**: states the no_go theorem precisely (parses note content for
  required statement strings).
- **T2**: enumerates the five obstructions D1-D5.
- **T3**: verifies `F_p` counterexample explicitly:
  - `F_p` is continuous (symbolic SymPy);
  - `F_p` is CPT-even (depends only on `|Z|`, symbolic);
  - `F_p` is multiplicatively factorizing on independent subsystems
    (symbolic);
  - `F_p` is NOT additive for `p ≠ 0` (rational grid for
    `p ∈ {-2, -1, 1/2, 1, 2, 3}`).
- **T4**: enumerates the four routes' independent confirmations
  (parses note for Routes A/B/C/E PR references and admission strings).
- **T5**: structural enumeration: Pattern L (log-reducing) vs
  Pattern D (functor-additivity inapplicable).
- **T6**: identifies what WOULD close the gap (a retained primitive
  excluding `F_p` — none identified at runner time).
- **T7**: forward paths: (a) new retained-grade primitive; (b) permanent
  P1 admission (parses note for both paths present).
- **T8**: no_go scope boundary: does NOT claim P1 is FALSE (parses for
  required scope-bounding language).
- **T9**: explicit list of out-of-scope: doesn't promote/demote any
  upstream (parses for no-promotion strings).
- **T10**: source-note boundary check (Claim type: no_go; Status
  authority: source-note proposal only; no forbidden overclaim strings).

## 5. Forward paths (out of scope of this no_go)

This no_go forecloses the four scaffold families A/B/C/E for closing
P1; it does NOT foreclose every conceivable closure path. Two
legitimate forward paths remain:

### 5.1 Path (a) — discover/derive a new retained-grade primitive

A retained-grade theorem identifying "physical scalar bosonic observable
generator" with the additive subclass on independent subsystems would
exclude `F_p` for `p ≠ 0` and retire P1. No such primitive is currently
identified in the framework's load-bearing chain (per Route C audit).
A new such primitive would need to:

- Be derivable from existing retained primitives (no new axiom per
  [`feedback_no_new_axioms.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/main/.claude/memory/feedback_no_new_axioms.md));
- Provide an independent classification mechanism for scalar functionals
  on `r = |Z| > 0` that excludes `F_p` for `p ≠ 0` without invoking `log`
  (otherwise it reproduces Pattern L circularity D5);
- Survive independent audit ratification.

This is research-grade open work; this no_go does not undertake it and
does not pre-judge its existence or non-existence.

### 5.2 Path (b) — accept P1 as a permanent classification premise

The parent note `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` already
operates in this mode: P1 is admitted as a physical-principle premise
and the conditional load-bearing statement says "given P1, the
exact-algebra closure holds verbatim". The audit row
`audited_conditional` reflects this admission. Path (b) is therefore
the **current state** of the parent note; this no_go provides
rigorous structural backing for keeping the audit row at
`audited_conditional` rather than treating it as a transient gap.

If path (a) is not closed in finite time, path (b) is the legitimate
permanent stance: `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` ships its
conditional exact-algebra closure with P1 admitted indefinitely, and
downstream rows that cite it inherit the conditional shape.

## 6. What this no_go closes (positive content)

The no_go has positive content despite the negative outcome:

- **Documents 4 independent failed closure paths with rigor.** Future
  agents do not need to re-attack Routes A/B/C/E; this no_go records
  why each route structurally cannot close P1.
- **Identifies the exact structural primitive that would be needed.**
  A retained-grade theorem identifying "physical scalar bosonic
  observable generator" with the additive subclass on independent
  subsystems, derivable from existing retained primitives without
  invoking `log` (= Pattern L circularity).
- **Names the specific counterexample family as the universal
  obstruction.** `F_p[J] = r(J)^p` is the witness that surfaces in
  every direction; it is not an artifact of one scaffold.
- **Identifies the legitimate forward paths.** (a) new retained-grade
  primitive (research-grade open); (b) accept P1 as a permanent
  classification premise (current state of parent note).
- **Provides audit-lane evidence** that
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` correctly stays
  `audited_conditional` with P1 admitted, rather than being mistaken
  for a transient gap pending closure.

## 7. Mandatory four exercises (documented, not re-attempted)

Routes A/B/C/E each ran the mandatory four exercises (assumptions,
Elon first-principles, lit search, math search). This consolidated
no_go does not re-run them; it documents the cross-route synthesis.

### 7.1 Assumptions audit (cross-route synthesis)

- **Explicit assumptions** covered across the four routes:
  - Hilbert tensor product on `H = H_A ⊗ H_B` (Route A, substrate
    primitive).
  - Grassmann determinant block factorization on real-D blocks
    (Routes A/C, retained via
    [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)).
  - Cauchy log functional equation (Route B, classical).
  - Shannon-Khinchin-Aczel-Daroczy classification axioms (Route B).
  - Atiyah-Singer index additivity (Route E, Pattern D).
  - K-theory / Euler characteristic / homology direct sum (Route E,
    Pattern D).
  - Cramer rate function (Route E, Pattern L).
  - Tropical max-plus dequantization (Route E, Pattern L).
- **Implicit assumption** in every route: "physical scalar bosonic
  observable generator = continuous additive scalar functional of
  `|Z|`". This implicit classification choice IS P1; it is the source
  of the circularity in every route.

### 7.2 Elon first-principles (cross-route synthesis)

From canonical primitives across the four routes:

- Multiplicative factorization is forced by Hilbert tensor product
  + finite Grassmann (Routes A/C).
- Going from multiplicative `r_A · r_B` to additive `log r_A + log r_B`
  is the Cauchy classifier (Routes A/B/E).
- The Cauchy classifier selects `log` as the unique continuous group iso
  `(R_+, *) → (R, +)` UP TO BASE; the choice of additive target IS the
  selection step P1 (Routes A/B/E).
- Pattern-D candidates (Atiyah-Singer, K-theory, homology, tangent
  functor) all rely on the `dim` functor or alternating sums on direct
  sums of vector spaces; `Z[J] in R` is a scalar, not a vector space
  (Route E).
- No published theorem in any of the four scaffold families derives
  additivity-from-independence on real-valued scalar functionals of a
  multiplicatively factorizing partition function without one of these
  moves (Pattern L circularity or Pattern D inapplicability).

### 7.3 Literature search (cross-route synthesis)

External authorities surveyed across the four routes:

- **Operator-algebraic**: Reeh-Schlieder 1961, Connes 1976, Connes-Stormer
  1978, Lieb-Robinson 1972, Hastings-Koma 2006, Streater-Wightman 1964,
  Haag 1992, Weinberg 1995, Takesaki 2003.
- **Information-theoretic**: Cauchy 1821, Aczel 1966, Shannon 1948,
  Khinchin 1957, Aczel-Daroczy 1975, Csiszar 2008.
- **Cross-disciplinary**: Atiyah-Singer 1968, Atiyah 1967, Cramer
  1938, Sanov 1957, Viro 2000, Maclagan-Sturmfels 2015, Hatcher 2002,
  Woodhouse 1992, Feynman-Hibbs 1965, Landau-Lifshitz 1980, Kock 2006,
  Tarski 1959, Tao blog, Ayala-Francis 2012, Lieb-Yngvason 1998.

No published derivation of additivity-from-independence on real-valued
scalar functionals of a partition function without one of the
identified moves (Pattern L invocation of `log` or Pattern D direct-sum
of vector-space-valued invariants).

### 7.4 Math search (Tao-style, cross-route synthesis)

Cross-disciplinary candidate enumeration from Route E:

| Code | Discipline | Pattern | Outcome |
|---|---|---|---|
| A | Atiyah-Singer index | D | inapplicable to scalar `Z` |
| B | Euler char / K-theory | D | inapplicable to scalar `Z` |
| C | Cramer rate function | L | invokes `log` (= P1) |
| D | Tropical max-plus | L | invokes `log` (= P1) |
| E | Anabelian / homological | D | inapplicable to scalar `Z` |
| F | Geometric quantization | L | invokes `log` (= P1) |
| G | Legendre / free energy | L | invokes `log` (= P1) |
| H | Synthetic diff geom / tangent | D | inapplicable to scalar `Z` |
| I | Tarski first-order logic | — | no native theorem |
| J | Tao functional equation | L | invokes `log` (= P1) |

All ten cross-disciplinary candidates reduce to Pattern L (Cauchy = P1)
or Pattern D (not applicable to scalar `Z[J] ∈ R`).

## 8. Repo vocabulary discipline

This note uses only repo-canonical vocabulary (per
[`feedback_no_new_repo_vocabulary.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/main/.claude/memory/feedback_no_new_repo_vocabulary.md)):

- "independent subsystems" (Grassmann block direct sum) — canonical.
- "scalar functional" — canonical.
- "additivity" / "multiplicative factorization" — canonical.
- "functor-additivity" — used in the Route E PR body and runner as
  description of Pattern-D objects (`dim`, `chi`, K-theory rank); not
  a new repo tag.
- "Pattern L circularity" / "Pattern D inapplicability" — Route E
  vocabulary, used here as descriptive labels for the two structural
  patterns; not a new repo tag, not framework axiom language.
- "counterexample family `F_p`" — Route A/C/E vocabulary, used here
  as the explicit non-additive multiplicative scalar functional.

No new repo-wide tags, no new framework classifications, no
status-promotion language.

## 9. Status authority and source-note boundary

This is a source-note proposal only. The independent audit lane sets
audit results and pipeline-derived effective status. This note does
not predict or claim an audit verdict.

- **Claim type:** no_go.
- **Status authority:** source-note proposal only; independent audit
  lane sets any audit result and pipeline-derived effective status.
- **Effective status on creation:** `unaudited` (set by audit lane,
  not authored).

This note does not promote, alter, or set the audit status of:

- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` (stays
  `audited_conditional`);
- `OBSERVABLE_PRINCIPLE_REAL_D_BLOCK_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
  (stays `retained_bounded`);
- `CPT_EXACT_NOTE.md` (stays `audited_conditional`);
- `STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`
  (stays `retained_bounded`);
- Any of the cited Route A/B/C/E sibling bounded notes.

## 10. External authorities cited inline (cross-route consolidation)

- Reeh-Schlieder, Nuovo Cimento 22 (1961), 1051-1068
- A. Connes, *Classification of injective factors*, Ann. of Math. 104 (1976), 73-115
- A. Connes & E. Størmer, J. Funct. Anal. 28 (1978), 187-196
- E. H. Lieb & D. W. Robinson, Comm. Math. Phys. 28 (1972), 251-257
- M. B. Hastings & T. Koma, Comm. Math. Phys. 265 (2006), 781-804
- R. F. Streater & A. S. Wightman, *PCT, Spin and Statistics, and All That*, Princeton (1964)
- R. Haag, *Local Quantum Physics*, Springer (1992)
- S. Weinberg, *The Quantum Theory of Fields, Vol. I*, Cambridge (1995), §4.4
- M. Takesaki, *Theory of Operator Algebras I-III*, Springer (2003)
- A.-L. Cauchy, *Cours d'Analyse* (1821), §V
- J. Aczel, *Lectures on Functional Equations and Their Applications* (1966), §2.1 Thm 1
- C. E. Shannon, *A Mathematical Theory of Communication*, Bell Syst. Tech. J. 27 (1948), 379-423, 623-656
- A. I. Khinchin, *Mathematical Foundations of Information Theory*, Dover (1957), Thm 1
- J. Aczel & Z. Daroczy, *On Measures of Information and Their Characterizations*, Academic Press (1975)
- I. Csiszar, *Axiomatic Characterizations of Information Measures*, Entropy 10 (2008), 261-273
- M. F. Atiyah, I. M. Singer, Ann. of Math. 87 (1968), 484-530
- M. F. Atiyah, *K-Theory*, Benjamin (1967)
- H. Cramer, Actualités Sci. Indust. 736 (1938)
- I. N. Sanov, Mat. Sbornik 42 (1957)
- O. Viro, "Dequantization of real algebraic geometry on logarithmic paper" (2000)
- D. Maclagan, B. Sturmfels, *Introduction to Tropical Geometry*, AMS (2015)
- A. Hatcher, *Algebraic Topology*, Cambridge (2002)
- N. M. J. Woodhouse, *Geometric Quantization*, Oxford (1992)
- R. P. Feynman, A. R. Hibbs, *Quantum Mechanics and Path Integrals* (1965)
- L. D. Landau, E. M. Lifshitz, *Statistical Physics* (1980)
- A. Kock, *Synthetic Differential Geometry*, Cambridge (2006)
- A. Tarski, *What is Elementary Geometry?* (1959)
- T. Tao, *What's new* blog (terrytao.wordpress.com)
- D. Ayala, J. Francis, arXiv:1206.5522
- E. H. Lieb, J. Yngvason, arXiv:math-ph/9805005

## 11. Cross-references

- Parent: [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
- Audit packet: [`OBSERVABLE_PRINCIPLE_AUDIT_NOTE_2026-05-02.md`](OBSERVABLE_PRINCIPLE_AUDIT_NOTE_2026-05-02.md)
- Route A (operator-algebraic): [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_OPERATOR_ALGEBRAIC_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_OPERATOR_ALGEBRAIC_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)
  — PR #1373
- Route B (information-theoretic): [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)
  — PR #1368
- Route C (framework-internal): [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_FRAMEWORK_INTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_FRAMEWORK_INTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)
  — PR #1402
- Route E (Tao-style cross-disciplinary): [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_E_TAO_CROSS_DISCIPLINARY_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_E_TAO_CROSS_DISCIPLINARY_NARROW_BOUNDED_NOTE_2026-05-17.md)
  — PR #1406
- Failed real-D candidate (context-only): `OBSERVABLE_PRINCIPLE_REAL_D_BLOCK_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
- CPT upstream: [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)
- Grassmann factorization: [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
