# Observable-Principle P1 Bridge — Shannon/Khinchin External Narrow Bounded Note

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Scope:** Layer-1 external mathematical scaffold recording the
Shannon-Khinchin-Aczel-Daroczy classification theorems for continuous
additive scalar functionals (and the special case of Cauchy's logarithm
functional equation), with an explicit honest admission that applying
these classification theorems to the staggered Grassmann setting does
**not** derive the P1 (scalar additivity on independent subsystems)
admitted premise of `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`.
The Shannon-type uniqueness theorems CLASSIFY the additive-functional
class; they presuppose additivity as a hypothesis. P1 itself remains an admitted physical-principle selection premise of the parent note; this note does NOT close that premise.
**Status authority:** source-note proposal only; independent audit lane
sets any audit result and pipeline-derived effective status.
**Runner:**
[`scripts/frontier_observable_principle_p1_bridge_shannon_khinchin_external_narrow.py`](../scripts/frontier_observable_principle_p1_bridge_shannon_khinchin_external_narrow.py)

## 0. Honest framing up front

This note records the Shannon/Khinchin external-scaffold attempt to
close the P1 admitted premise in
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`. That attempt proposed that
the Shannon-Khinchin-Aczel uniqueness theorems
applied to the staggered Grassmann partition function `Z[J] = det(D+J)`
would force additivity on independent subsystems without admitting a new
"physical scalar bosonic observable generator" classification axiom.

The Shannon/Khinchin attempt **fails to close P1 positively**. The structural
reason: every published Shannon-Khinchin-Aczel-Daroczy uniqueness theorem
**takes additivity (or the equivalent chain rule) as a hypothesis** and
classifies the unique additive functional satisfying further regularity
conditions as `H(p) = -k sum p_i log p_i`. None of these theorems
**derive** additivity from independence; they assume it and characterize
its consequences. Applying them to `|Z[J]|` on independent Grassmann
blocks therefore reproduces the existing parent-note conclusion
`W = c log|Z|` **given exact P1 additivity admitted**, without retiring P1
itself.

The honest landing is therefore a **bounded_theorem** that records
Shannon-Khinchin-Aczel-Daroczy as a citable Layer-1 external
classification theorem, with the explicit admission that the
identification "physical scalar bosonic observable generator =
continuous additive scalar functional of |Z|" is the SAME admitted
classification choice as P1, just relabeled. P1 retirement requires a
**different** argument (operator-algebraic, structural, or a separate
retained-grade primitive identifying physical scalar observables with
the additive class on independent subsystems).

This note explicitly DOES NOT promote or alter the status of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, `CPT_EXACT_NOTE.md`, or any
upstream row.

## 1. External classification theorems

### 1.1 Cauchy's logarithm functional equation (classical)

Let `f: R_+ -> R` be a function on the positive reals with `f(xy) =
f(x) + f(y)` for all `x, y > 0`, and suppose `f` is continuous at some
point. Then there exists a real constant `c` such that

```text
f(x) = c log(x)        for all x > 0.
```

This is the classical multiplicative-to-additive functional equation,
proved by Cauchy (1821) and recorded in Aczel "Lectures on Functional
Equations and Their Applications" (1966), Theorem 1 §2.1.

### 1.2 Shannon entropy (1948)

Shannon's 1948 paper defines the entropy of a discrete probability
distribution `p = (p_1, ..., p_n)` as

```text
H(p) = - sum_{i=1}^{n} p_i log p_i,
```

and observes that for two **independent** distributions `p` and `q`
with joint `(p_i q_j)_{ij}`,

```text
H(p (x) q) = H(p) + H(q).
```

Shannon's "Mathematical Theory of Communication", Bell Syst. Tech. J.
27 (1948), 379-423 and 623-656.

### 1.3 Khinchin uniqueness theorem (1957)

Khinchin (1957, "Mathematical Foundations of Information Theory",
Dover, Theorem 1) proves: any functional `H_n(p_1, ..., p_n)` on
discrete probability distributions satisfying

(K1) **Continuity** in the `p_i`;

(K2) **Maximum at uniform**: `H_n(1/n, ..., 1/n)` is monotone
non-decreasing in `n`;

(K3) **Additivity on conditional sub-experiments** (chain rule):
`H(AB) = H(A) + H(B|A)` for joint experiments;

(K4) **Consistency**: `H_n(p_1, ..., p_n, 0) = H_n(p_1, ..., p_n)`
(adding zero-probability events does not change `H`);

is uniquely of the form

```text
H(p) = -k sum_i p_i log p_i
```

for some constant `k > 0`.

**Critical note on hypotheses.** (K3) is an **additivity hypothesis**:
it states that the entropy of a joint experiment equals the sum of
marginal and conditional entropies. The theorem **classifies** the
functionals satisfying (K1)-(K4); it does **not** derive additivity
from non-additive primitives.

### 1.4 Aczel-Daroczy strengthening (1975)

Aczel and Daroczy ("On Measures of Information and Their
Characterizations", Academic Press 1975) replace Khinchin's maximum
hypothesis (K2) with weaker symmetry / expansibility properties, and
classify a broader family including Renyi entropies. In every variant
the additivity (or generalized additivity / pseudo-additivity)
hypothesis remains explicit; the theorems are CLASSIFICATION theorems
on the additive class.

### 1.5 What these theorems collectively give

Given a continuous real-valued functional `W` on positive reals
satisfying the multiplicative-to-additive equation `W(r_1 r_2) = W(r_1)
+ W(r_2)`, Cauchy/Aczel's logarithm theorem forces `W(r) = c log r`.
Given a continuous functional `H` on probability simplices satisfying
Khinchin axioms, `H = -k sum p_i log p_i`.

**Both directions assume additivity as a premise.**

## 2. Application to the staggered Grassmann setting (bounded)

### 2.1 Setup (from existing retained / runner-local content)

By the retained finite-Grassmann content
([`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md),
status `retained_bounded`), the staggered partition function with
source `J` is

```text
Z[J] = det(D + J).
```

For two independent subsystems `D = D_A (+) D_B`, `J = J_A (+) J_B`,
block-diagonal determinant factorization gives

```text
Z[J_A (+) J_B] = det(D_A + J_A) det(D_B + J_B) = Z_A[J_A] Z_B[J_B].
```

This is the existing cluster-decomposition statement recorded in
`OBSERVABLE_GENERATOR_ADDITIVITY_FROM_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-05-10.md`;
that note is a context pointer here, not a load-bearing status import.

### 2.2 Conditional application of Cauchy / Khinchin / Aczel

**Conditional statement (bounded).** If one adopts the parent note's
admitted classification of "physical scalar bosonic observable
generator" as a continuous, additive, CPT-even, real-valued functional
on `|Z[J]|`, then:

- The continuous additive functional equation `W(r_1 r_2) = W(r_1) +
  W(r_2)` on `R_+` (with `r_i = |Z_i|`) has unique solution `W =
  c log r` by Cauchy's theorem (§1.1) — equivalently, by the
  Aczel-Daroczy classification (§1.4) specialized to scalar functionals
  on `R_+`. An additive offset `b` would give `W(r_1 r_2) -
  W(r_1) - W(r_2) = -b`, so exact additivity forces `b = 0`; this note
  does not invoke a shifted or gauge-normalized composition law;
- The Shannon-Khinchin theorem (§1.3) applied to the multinomial
  probability distribution `p_i = |Z_i|^2 / sum_j |Z_j|^2`
  reproduces `H(p) = -k sum_i p_i log p_i` — but this is the
  **Shannon entropy of a constructed probability distribution**, not
  the Grassmann observable generator.

The conditional conclusion `W = c log|Z|` matches the parent note's
exact-additive conclusion. The Shannon-Khinchin scaffold therefore
provides a **published external uniqueness theorem cite** for the same
content; it does not provide new closure.

### 2.3 Why P1 is NOT retired by this scaffold

P1 (parent note `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` §"What
remains admitted"): the requirement that the physical scalar bosonic
observable generator be **additive** on independent subsystems.

The Shannon-Khinchin-Aczel-Daroczy theorems all **assume** additivity
as a hypothesis (chain rule, factorization, or direct additivity). They
classify the consequence; they do not derive additivity from a more
primitive structure.

Applying any of these theorems to `|Z|` on independent Grassmann
blocks therefore requires assuming **additivity** as input, then
classifying the unique functional as `c log` as output. This is
exactly the parent note's existing conditional structure: assume
additivity (P1), conclude `W = log|det|`.

**Conclusion.** The Shannon route relabels P1 ("additivity is the
defining property of the physical scalar observable generator") in
information-theoretic vocabulary ("additivity is the Khinchin chain
rule for the physical scalar generator"). It does not derive P1.

## 3. Honest boundary

This note records published external mathematical content:

- Cauchy's logarithm functional equation;
- Shannon (1948) entropy and its independence-additivity property;
- Khinchin (1957) uniqueness classification of the entropy functional;
- Aczel-Daroczy (1975) generalization classifying broader entropy
  families.

The note **DOES NOT**:

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
  determinant factorization, independent subsystem).

The Shannon-Khinchin-Aczel-Daroczy classification theorems are
**conditional uniqueness theorems** on the additive functional class.
They do not produce additivity from non-additive primitives. Closing
P1 therefore requires a **different** argument: an operator-algebraic
forcing argument, an explicit retained-grade theorem identifying
physical scalar observables with the additive class, or a sharpened
no-go showing P1 is genuinely undecidable from the repo's accepted
framework primitives.

## 4. External references

- A.-L. Cauchy, "Cours d'Analyse de l'Ecole Royale Polytechnique"
  (1821), §V on functional equations.
- J. Aczel, "Lectures on Functional Equations and Their
  Applications", Academic Press (1966), §2.1 Theorem 1
  (multiplicative-to-additive uniqueness theorem).
- C. E. Shannon, "A Mathematical Theory of Communication", Bell
  System Technical Journal 27 (1948), 379-423 and 623-656.
- A. I. Khinchin, "Mathematical Foundations of Information Theory",
  Dover (1957), Theorem 1 (uniqueness of Shannon entropy from
  continuity, monotonicity at uniform, chain-rule additivity, and
  consistency).
- J. Aczel and Z. Daroczy, "On Measures of Information and Their
  Characterizations", Academic Press (1975).
- I. Csiszar, "Axiomatic Characterizations of Information Measures",
  Entropy 10 (2008), 261-273 (review of additivity-assuming
  classification theorems for f-divergences).

## 5. Verification

The runner verifies the Layer-1 external content with exact
`fractions.Fraction` arithmetic plus SymPy symbolic checks. Tests:

- **T1** (Cauchy log functional equation, symbolic):
  `log(x*y) - log(x) - log(y) = 0` symbolically for arbitrary
  positive `x, y`.
- **T2** (Cauchy log equation, numerical): on a dense grid of
  positive rationals, `c * (log(x*y) - log(x) - log(y))` evaluates
  to `0` to floating-point precision.
- **T3** (Shannon entropy additivity on independent distributions,
  exact Fraction): for `p = (1/2, 1/2)`, `q = (1/3, 2/3)`, `H(p) +
  H(q) = H(p (x) q)` to symbolic identity (rational p, q give exact
  rational equality after `log` expansion).
- **T4** (Khinchin axiom enumeration): a discrete-distribution test
  bank checks that the Shannon functional satisfies sample instances of
  continuity + max-at-uniform + chain-rule additivity + consistency,
  and that a non-additive alternative violates the chain rule. The
  uniqueness theorem itself is cited from Khinchin/Aczel-Daroczy, not
  reproved by the runner.
- **T5** (Grassmann determinant factorization, finite SymPy block):
  on a 4x4 staggered toy block `D` with `D = D_A (+) D_B`,
  `det(D + j_A I_A (+) j_B I_B) = det(D_A + j_A I_A) det(D_B + j_B
  I_B)` exactly via SymPy block-diagonal determinant.
- **T6** (Conditional additivity on `log|Z|` on the toy block):
  given factorization in T5, `log|det(D_A+J_A) det(D_B+J_B)| =
  log|det(D_A+J_A)| + log|det(D_B+J_B)|` numerically to floating-
  point precision.
- **T7** (Honest scope check — P1 NOT retired): the note string
  contains the explicit honest scoping statement that Shannon-
  Khinchin-Aczel-Daroczy classification theorems assume additivity
  as a hypothesis and do not derive P1.
- **T8** (Sensitivity / structural check): the non-additive
  functional `r -> r` (identity) satisfies `f(r1 r2) = r1 r2 !=
  f(r1) + f(r2) = r1 + r2` in general, demonstrating that
  multiplicative-to-additive forcing requires the logarithm form.
  This confirms that within the exact-additive continuous class
  Cauchy's theorem classifies the logarithm form, while without
  admitting additivity the scaffold does not select P1.
- **T9** (Scope boundary, parent statuses unchanged): the note
  string contains the explicit non-promotion statement for
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE`, `CPT_EXACT_NOTE`, and
  staggered authorities.
- **T10** (Source-note boundary check): the note declares
  `Claim type: bounded_theorem`, avoids forbidden status-overclaim
  strings, and contains the explicit "does not derive P1" admission.

Expected runner result: `PASS=20, FAIL=0`.

## 6. Reproduction

```bash
PYTHONPATH=scripts python3 \
  scripts/frontier_observable_principle_p1_bridge_shannon_khinchin_external_narrow.py
```

A passing run supports only the Layer-1 external classification
theorem content recorded above plus the explicit honest admission that
P1 is NOT retired by this scaffold. It does **NOT** support any
framework status promotion, any closure of P1, or any numerical
hierarchy readout.
