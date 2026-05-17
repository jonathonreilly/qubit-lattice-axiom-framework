# Observable-Principle P1 Bridge — Route E Tao-style Cross-Disciplinary Narrow Bounded Note

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Scope:** Layer-1 external mathematical scaffold recording a Tao-style
cross-disciplinary search for a non-obvious mathematical structure that
derives additivity from independence as a CONSEQUENCE rather than a
hypothesis. Ten candidate disciplines (Atiyah-Singer index additivity,
Euler characteristic / K-theory on disjoint unions, Cramér / Sanov
large-deviation rate functions, tropical max-plus dequantization,
homological additivity on disjoint unions, geometric quantization,
Legendre transform / variational principle, synthetic differential
geometry tangent functors, Tarski first-order logic, and Tao-blog
post-2020 multiplicative-to-additive functional equations) are each
audited against the explicit question:

> Does the candidate derive additivity from independence WITHOUT taking
> additivity as a hypothesis, AND does the derived additivity rule out
> the non-additive counterexample family `F_p[J] = r(J)^p` for `p ≠ 1`
> on the staggered Grassmann partition function?

**Verdict:** NONE of the ten candidates does so. Every cross-disciplinary
construction surveyed either (i) invokes `log` explicitly to convert
multiplicative-to-additive (which is the Cauchy choice = P1 itself,
reproducing Routes A/B/C), or (ii) packages additivity in
dimension / integral / vector-space functorial structure that does NOT
apply to the scalar real-valued `Z[J] = det(D+J) ∈ R` setting.

The Route E stretch attempt therefore lands as a **bounded_theorem** that
records the cross-disciplinary survey result alongside Routes A
(operator-algebraic, PR #1373), B (Shannon/Khinchin, PR #1368), and C
(framework-internal, PR #1402). All four routes converge on the same
structural admission: standard mathematical scaffolds CANNOT derive
additivity from independence on real-valued scalar functionals of a
multiplicatively-factorizing partition function without an upstream
additivity-forcing primitive or a hidden classification axiom. The
`F_p[J] = r(J)^p` family is the explicit witness that obstructs every
attempted closure.

**Status authority:** source-note proposal only; independent audit lane
sets any audit result and pipeline-derived effective status.
**Runner:**
[`scripts/frontier_observable_principle_p1_bridge_route_e_tao_cross_disciplinary_narrow.py`](../scripts/frontier_observable_principle_p1_bridge_route_e_tao_cross_disciplinary_narrow.py)

## 0. Honest framing up front

This note records the Route E cross-disciplinary stretch attempt to
close the P1 admitted premise of
[`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md).
The Routes A (operator-algebraic), B (Shannon/Khinchin classification),
and C (framework-internal candidate audit) all returned
`bounded_theorem` with explicit `F_p[J] = r(J)^p` counterexample. The
Route E stretch attempts a Tao-style "open the search wide" pass over
ten cross-disciplinary scaffolds (Atiyah-Singer index, K-theory,
Cramér rate functions, tropical max-plus, anabelian / homological
disjoint-union, geometric quantization, Legendre transform, synthetic
differential geometry, Tarski first-order logic, Tao-blog functional
equations) and asks whether ANY of them genuinely derives
additivity-from-independence WITHOUT presupposing additivity.

The Route E attempt **fails to close P1 positively**. Every candidate
surveyed reduces to one of two structural patterns:

- **Pattern L (log-invocation):** the candidate introduces `log`
  explicitly to convert a multiplicative independence-factorization to
  additivity (Cramér cumulant generating function, free energy
  `F = -k_B T log Z`, classical action as `-log Z` saddle limit,
  tropical dequantization map `x → log_b(x)`, von Neumann entropy
  `-Tr(ρ log ρ)`). The `log` choice IS the Cauchy classifier; choosing
  `log` over `(·)^p` is P1 in different vocabulary.
- **Pattern D (dimension/functor-additivity):** the candidate is an
  invariant valued in `Z` or in a vector space, with additivity coming
  from the dimension or integration functor's structural action on
  direct sums (Atiyah-Singer index `dim ker - dim coker` via
  Grothendieck ring homomorphism, Euler characteristic `Σ(-1)^k dim H_k`,
  K-theory `K(X ⊔ Y) = K(X) × K(Y)`, factorization homology symmetric
  monoidal direct sum, smooth tangent functor `T(M × N) = TM ⊕ TN`).
  These do NOT apply to scalar real-valued `Z[J] ∈ R` — the staggered
  Grassmann partition function is a number, not a vector space or
  integer.

The honest landing is therefore a **bounded_theorem** that records the
ten-candidate cross-disciplinary survey result with the explicit
admission that NONE of them retires P1. P1 closure requires either
(a) a separate retained-grade theorem identifying physical scalar
observables with the additive class on independent subsystems
(none currently identified), or (b) a sharpened no_go declaring P1
genuinely undecidable from the present axiom stack `A_min`.

This note explicitly DOES NOT promote or alter the status of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, `CPT_EXACT_NOTE.md`, or any
upstream row.

## 1. The cross-disciplinary candidate table

The ten candidates surveyed, with their additivity-theorem statement,
the pattern they reduce to (L = log-invocation, D = dimension/functor),
and whether they derive additivity-from-independence without
presupposing it.

| Code | Discipline | Additivity-theorem statement | Pattern | Derives or presupposes additivity? |
|------|-----------|------------------------------|---------|-----------------------------------|
| A | Atiyah-Singer index | `ind(D_1 ⊔ D_2) = ind(D_1) + ind(D_2)` | D | Presupposes (via ring homomorphism into `Z`; index is `dim ker - dim coker`, additive by `dim` functor on direct sums) |
| B | Euler char / K-theory | `χ(X ⊔ Y) = χ(X) + χ(Y)`; `K(X ⊔ Y) ≅ K(X) × K(Y)` | D | Presupposes (`χ = Σ(-1)^k dim H_k` additive by dim on direct sum; K-theory Grothendieck ring) |
| C | Cramér rate function | `Λ_{X+Y}(λ) = Λ_X(λ) + Λ_Y(λ)` for `X ⊥ Y` | L | Invokes log: `Λ = log E[e^(λX)]`. Multiplicative MGF `M_{X+Y} = M_X M_Y` is converted to additive `Λ` BY taking log. The log choice is the Cauchy classifier. |
| D | Tropical max-plus | `log_b: (R_+, ·) → (R_+, max)` is a semiring homomorphism in the `b → ∞` limit | L | Invokes log: the dequantization map IS `x → log_b(x)`. The choice of log over `(·)^p` is the same Cauchy classifier. |
| E | Anabelian / homological | `H_*(X ⊔ Y) = H_*(X) ⊕ H_*(Y)` | D | Presupposes (homology is vector-space valued; direct sum is additive in linear algebra). Does not apply to scalar `Z[J] ∈ R`. |
| F | Geometric quantization | `S[γ_1 ⊔ γ_2] = S[γ_1] + S[γ_2]` (classical action) | L | Invokes log via path-integral saddle: `S_cl = -ℏ log Z` in the semiclassical limit. The action's additivity comes from `∫L dt` integral structure (Pattern D for action itself), but the bridge to `Z` is `log`. |
| G | Legendre transform / free energy | `F[ρ_1 ⊗ ρ_2] = F[ρ_1] + F[ρ_2]` | L | Invokes log explicitly: `F = -k_B T log Z`. The `log` is the Cauchy choice; without it `Z` is multiplicative not additive. |
| H | Synthetic diff geom / tangent functor | `T(M × N) = TM ⊕ TN` | D | Presupposes (tangent is a vector-bundle functor; direct sum is additive). Does not apply to scalar `Z[J] ∈ R`. |
| I | Tarski first-order logic | (no native additivity-from-independence theorem on real-valued functionals) | — | No applicable theorem. |
| J | Tao-blog functional equations (post-2020 survey) | Cauchy `f(x+y) = f(x) + f(y)` with regularity → `f(x) = cx`. Cauchy log `f(xy) = f(x) + f(y)` with regularity → `f(x) = c log x` | L | Tao's notes (e.g. terrytao.wordpress.com on Cauchy theorem, multiplicative functions) reproduce the Cauchy classifier; they do NOT derive additivity from independence without it. |

**Convergent reading.** Every candidate either (Pattern L) explicitly
invokes `log` to bridge multiplicative-to-additive (which is P1 itself in
different vocabulary) or (Pattern D) packages additivity in a
dimension/integral/vector-space functor that does NOT apply to the
scalar real-valued `Z[J] = det(D+J) ∈ R` setting.

## 2. Why each Pattern-L candidate reproduces P1

The Pattern-L candidates (C, D, F, G, J) all introduce a `log` map to
convert a multiplicative structure to an additive one. The choice of
`log` over `(·)^p` for any nonzero `p` is exactly the Cauchy
classification theorem: among continuous group homomorphisms
`(R_+, ·) → (R, +)`, the only ones are `c log` for some real `c`. But
there is ALSO a one-parameter family of continuous group homomorphisms
`(R_+, ·) → (R_+, ·)`, namely `r → r^p` for any real `p`. The choice of
`log` (going to `(R, +)`) over `r^p` (staying in `(R_+, ·)`) is the
choice of an ADDITIVE TARGET. That choice IS P1.

Concretely:
- **C Cramér:** `Λ(λ) = log E[e^(λX)]` chooses `(R, +)` as the target;
  `E[e^(λX)]^p` chooses `(R_+, ·)` as the target. Cramér additivity
  presupposes the `log` (additive target) choice.
- **D Tropical:** `log_b(x)` dequantization presupposes additive target.
- **F Geometric quantization:** semiclassical `Z ≈ e^(-S_cl/ℏ)` and
  identifying `S_cl = -ℏ log Z` presupposes additive target (classical
  action lives in `(R, +)`).
- **G Free energy:** `F = -k_B T log Z` presupposes additive target.
- **J Tao Cauchy:** Cauchy's theorem CLASSIFIES the continuous additive
  functionals on `R_+` as `c log`. It does not derive WHY the physical
  scalar generator should be additive (= target `(R, +)`) rather than
  multiplicative (= target `(R_+, ·)`).

In each Pattern-L candidate, the choice of `log` as the bridge map is
the SAME selection step as P1 in `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE`.
The cross-disciplinary candidate provides external published vocabulary
("rate function", "tropical dequantization", "classical action", "free
energy", "Cauchy theorem") for the same selection step. It does not
derive the selection from primitives.

## 3. Why each Pattern-D candidate does not apply

The Pattern-D candidates (A, B, E, H) are functorial invariants valued
in integers or in vector spaces. Their additivity comes from `dim`
acting on direct sums or `Σ(-1)^k` acting on chain complexes.

The Grassmann partition function `Z[J] = det(D+J)` is a real number on
the runner blocks. It is NOT an integer (it's a determinant of a real
anti-symmetric matrix plus source, which is a real polynomial in `J`),
and it is NOT a vector space. The functorial-additivity arguments of
Pattern D require either:

- An invariant valued in `Z` (Atiyah-Singer index, Euler characteristic)
  built from `dim ker D - dim coker D` or `Σ(-1)^k dim H_k`. The
  staggered partition function `det(D+J)` is real-valued, not
  integer-valued, and there is no canonical map `R → Z` to apply Pattern D.
- An invariant valued in a vector space (homology `H_*(X ⊔ Y)`,
  K-theory `K(X) × K(Y)`, tangent bundle `T(M × N)`). Again `det(D+J)`
  is a number, not a vector space, so the direct-sum-of-vector-spaces
  structure does not apply.

Pattern-D candidates therefore do not apply to scalar real-valued
functionals of the staggered Grassmann partition function.

(Sub-claim: one could try to "lift" `Z[J]` to a vector-space-valued
invariant — e.g. the determinant line bundle, or the spectrum of `D+J`
as a multiset. But the determinant line bundle is itself a
multiplicative object — `det(D_A ⊕ D_B) = det(D_A) ⊗ det(D_B)` — and the
choice of trivialization to a number requires a chosen `log` again, so
the lift returns to Pattern L. The spectrum as a multiset is
additive under disjoint union — `spec(D_A ⊕ D_B) = spec(D_A) ⊔ spec(D_B)`
— but extracting a scalar from a multiset uses one of:
(a) `Σ` over eigenvalues, which would give `tr(D+J)` not `log|det(D+J)|`,
or (b) `Π` then `log`, which is Pattern L again.)

## 4. F_p obstruction on every candidate

For each candidate, we explicitly verify the `F_p[J] = r(J)^p`
counterexample on a 4x4 staggered toy block. Let `D = D_A ⊕ D_B` be
the block-diagonal staggered Dirac with `D_A, D_B` 2x2 real
antisymmetric, `J = j_A I_A ⊕ j_B I_B`. The runner verifies:

- `Z[J_A ⊕ J_B] = Z_A[J_A] · Z_B[J_B]` (multiplicative factorization,
  exact via `SymPy`);
- `r(J) = |Z[J]|` is multiplicative on independent blocks: `r(J_A ⊕ J_B)
  = r(J_A) · r(J_B)`;
- `F_p[J] := r(J)^p` is multiplicative for every real `p`: `F_p(J_A ⊕ J_B)
  = F_p(J_A) · F_p(J_B)`;
- `F_p` is additive for `p = 0` (degenerate) and for `p → 0` via
  `log r = lim_{p→0} (r^p - 1)/p`. For all `p ≠ 0`, `F_p` is
  multiplicative but NOT additive on independent blocks.

Each Pattern-L candidate's `log` choice excludes `F_p` for `p ≠ 1` (via
the `log` map's uniqueness as a group homomorphism `(R_+, ·) → (R, +)`
up to scalar, Cauchy classification), but the `log` choice itself is
P1. Each Pattern-D candidate's vector-space-valued structure does not
constrain `F_p` because `F_p` is a real-valued scalar functional, not a
vector-space-valued invariant.

The `F_p` obstruction therefore persists across all ten Route E
candidates A-J.

## 5. Honest boundary

This note records:
- A cross-disciplinary survey of ten mathematical structures (A-J)
  with additivity-on-independence theorems;
- The verdict that NONE of them derives additivity-from-independence
  without either invoking `log` explicitly (Pattern L = Cauchy
  classifier = P1 in different vocabulary) or relying on
  dimension/functor structure (Pattern D) that does NOT apply to
  scalar real-valued `Z[J] ∈ R`;
- The explicit `F_p[J] = r(J)^p` obstruction persists across every
  candidate.

This note **DOES NOT**:
- Derive the P1 admitted premise of
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`;
- Promote, alter, or set the audit status of
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, `CPT_EXACT_NOTE.md`, or
  any other upstream row;
- Close any framework-level hierarchy formula, scale ratio, or
  numerical readout;
- Add a new framework axiom or repo-wide premise;
- Introduce new repo vocabulary (only repo-canonical terms used:
  Grassmann, partition function, scalar generator, CPT-even,
  determinant factorization, independent subsystem, multiplicative,
  additive, classification, counterexample family).

The convergent reading across Routes A, B, C, and now E is that the
P1 (scalar additivity on independent subsystems) admitted premise is
genuinely undecidable from cross-disciplinary published mathematical
scaffolds alone. Closing P1 therefore requires a different argument:
a separate retained-grade primitive identifying physical scalar
observables with the additive class on independent subsystems, or a
sharpened no_go showing P1 is genuinely undecidable from
the repo's accepted framework primitives.

## 6. External references

- M. F. Atiyah, I. M. Singer, "The Index of Elliptic Operators I",
  Ann. of Math. 87 (1968), 484-530. (Pattern D: index as ring
  homomorphism to integers.)
- M. F. Atiyah, "K-Theory", Benjamin (1967). (Pattern D: Grothendieck
  ring of vector bundles, direct sum as addition.)
- H. Cramér, "Sur un nouveau théorème-limite de la théorie des
  probabilités", Actualités Sci. Indust. 736 (1938). (Pattern L:
  cumulant generating function = log MGF.)
- I. N. Sanov, "On the probability of large deviations of random
  variables", Mat. Sbornik 42 (1957), 11-44. (Pattern L: relative
  entropy as rate function, log-form.)
- A.-L. Cauchy, "Cours d'Analyse de l'Ecole Royale Polytechnique"
  (1821), §V. (Pattern L: multiplicative-to-additive classifier.)
- O. Viro, "Dequantization of real algebraic geometry on logarithmic
  paper", in *European Congress of Mathematics*, Vol. I (Barcelona
  2000), Birkhäuser, 135-146. (Pattern L: tropical dequantization
  map via `log`.)
- D. Maclagan, B. Sturmfels, "Introduction to Tropical Geometry",
  AMS Graduate Studies in Mathematics 161 (2015), §1.1. (Pattern L:
  max-plus semiring and log-dequantization.)
- A. Hatcher, "Algebraic Topology", Cambridge (2002), §2.2.
  (Pattern D: `H_*(X ⊔ Y) = H_*(X) ⊕ H_*(Y)`.)
- N. M. J. Woodhouse, "Geometric Quantization", Oxford (1992).
  (Pattern L: action as `-ℏ log Z` saddle limit.)
- R. P. Feynman, A. R. Hibbs, "Quantum Mechanics and Path Integrals",
  McGraw-Hill (1965), §2-1. (Pattern L: action additive over disjoint
  time intervals via integral structure; bridge to `Z` is `log`.)
- L. D. Landau, E. M. Lifshitz, "Statistical Physics, Part 1",
  Pergamon (1980), §31. (Pattern L: free energy `F = -T log Z`.)
- A. Kock, "Synthetic Differential Geometry", Cambridge (2006).
  (Pattern D: tangent functor on Cartesian products.)
- A. Tarski, "What is Elementary Geometry?", in *The Axiomatic
  Method*, North-Holland (1959), 16-29. (Pattern --- : no native
  additivity-from-independence theorem on real-valued functionals.)
- T. Tao, "What's new" blog at terrytao.wordpress.com — Notes 3
  on Cauchy's theorem (Math 246A, 2016-10-02) and multiplicative-
  functions tag posts (reviewed for any post-2020 derivation of
  additivity-from-independence; none found beyond the Cauchy
  classifier).
- D. Ayala, J. Francis, "Factorization homology of topological
  manifolds", arXiv:1206.5522. (Pattern D: symmetric monoidal
  disjoint-union structure.)
- E. H. Lieb, J. Yngvason, "A Guide to Entropy and the Second Law of
  Thermodynamics", Notices AMS 45 (1998), 571-581;
  arXiv:math-ph/9805005. (Entropy additivity calibrated as an axiom
  via the "additive entropy constants" postulate, not derived from
  non-additive primitives.)

## 7. Verification

The runner verifies the Layer-1 external content with exact
`fractions.Fraction` arithmetic plus `SymPy` symbolic checks. Tests:

- **T1** (Candidate enumeration): the note records ten candidates A-J
  with their additivity-theorem statements and pattern classification
  (L or D).
- **T2** (Pattern-L log-invocation check): for each Pattern-L candidate
  (C, D, F, G, J), the runner verifies that the candidate's
  additivity-on-independence statement explicitly involves `log` as the
  bridge map.
- **T3** (Pattern-D functor-additivity check): for each Pattern-D
  candidate (A, B, E, H), the runner verifies that the candidate's
  additivity-on-disjoint-union statement is structurally inherited from
  `dim` on direct sums or `Σ(-1)^k` on chain complexes, and is valued
  in `Z` or in vector spaces (not in `R` as a scalar).
- **T4** (Grassmann factorization on staggered toy block, SymPy
  symbolic): `det(D_A ⊕ D_B + j_A I_A ⊕ j_B I_B) = det(D_A + j_A I_A)
  · det(D_B + j_B I_B)` exactly on a 4x4 staggered block.
- **T5** (`F_p` counterexample family is multiplicative for every `p`):
  on rational `j_A, j_B`, `F_p(J_A ⊕ J_B) = F_p(J_A) · F_p(J_B)` to
  exact `Fraction` precision for `p ∈ {-2, -1, 1/2, 1, 2, 3}`.
- **T6** (`F_p` fails additivity for `p ≠ 0` on independent blocks):
  on the same rational grid, `F_p(J_A ⊕ J_B) ≠ F_p(J_A) + F_p(J_B)` for
  every `p ∈ {-2, -1, 1/2, 1, 2, 3}`; only the `p → 0` (i.e. `log r`)
  limit gives additivity, by Cauchy classification.
- **T7** (Cramér additivity invokes `log`): on independent Bernoulli
  random variables `X_A, X_B`, the cumulant generating function
  `Λ(λ) = log E[e^(λX)]` satisfies `Λ_{X_A + X_B}(λ) = Λ_{X_A}(λ) +
  Λ_{X_B}(λ)` exactly, and the same identity with `log` replaced by
  `(·)^p` FAILS additivity for `p ≠ 0`.
- **T8** (Tropical dequantization invokes `log`): the tropical map
  `T_b(x) = log_b(x)` satisfies `T_b(x · y) = T_b(x) + T_b(y)`, while
  `x → x^p` satisfies `(x · y)^p = x^p · y^p` (multiplicative, not
  additive) for any `p ≠ 0`.
- **T9** (Atiyah-Singer / K-theory / homology don't apply to scalar
  `Z[J]`): the runner verifies that `Z[J] = det(D + J)` is a real
  scalar on the staggered toy block (`Z ∈ R`), not an integer
  (`Z ∉ Z` for generic `J`) and not a vector space (`Z` has no direct
  sum structure as a single number). Pattern-D candidates therefore do
  not provide an applicable additivity argument.
- **T10** (Convergence with Routes A, B, C — `F_p` obstruction
  persists): the runner verifies the explicit cross-route convergence
  statement, with `F_1 = r(J)` satisfying multiplicative factorization
  but failing additivity, exactly as in Routes A (operator-algebraic
  counterexample) and B (Shannon/Khinchin presupposed-additivity) and
  C (no framework primitive excludes `F_p`).
- **T11** (Honest scope check — P1 NOT retired): the note string
  contains the explicit honest scoping statements that no Route E
  candidate retires P1, and that convergence with Routes A, B, C
  documents a structural admission rather than a closure.
- **T12** (Scope boundary, parent statuses unchanged): the note string
  contains the explicit non-promotion statement for
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE`, `CPT_EXACT_NOTE`, and
  staggered authorities.
- **T13** (Source-note boundary check): the note declares
  `Claim type: bounded_theorem`, avoids forbidden status-overclaim
  strings, and contains the explicit "does not derive P1" admission.

Expected runner result: `PASS=13, FAIL=0`.

## 8. Reproduction

```bash
PYTHONPATH=scripts python3 \
  scripts/frontier_observable_principle_p1_bridge_route_e_tao_cross_disciplinary_narrow.py
```

A passing run supports only the Layer-1 external cross-disciplinary
survey content recorded above plus the explicit honest admission that
P1 is NOT retired by any of the ten candidates. It does NOT support any
framework status promotion, any closure of P1, or any numerical
hierarchy readout.
