# Observable-Principle P1 Bridge — Extensivity Primitive Narrow Note

**Date:** 2026-05-21
**Status authority:** independent audit lane only.
**Claim type:** no_go
**Claim scope:** narrow sharpened no-go on the extensivity primitive as a
candidate derivation of the P1 admitted premise (scalar additivity on
independent subsystems) of
[`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md).
Records that the extensivity premise

> *the framework's physical scalar observable generator `W` is extensive
> — under bulk replication `Λ → Λ^N` of a finite region into N disjoint
> copies with identical sources, `W[J^{(N)}] = N · W[J]`* (E)

routed through the bulk replication multiplicative factorization
`|Z[J^{(N)}]| = |Z[J]|^N` (an elementary consequence of the
block-diagonal determinant identity / trace-tensor factorization)
**uniquely selects the natural log form `W = c · log|Z| + const`**, but
that the selection mechanism reduces — via the substitution
`g(x) := f(e^x)` on `f(r) := W[J]|_{|Z[J]| = r}` — to the **integer-N
restriction of the Cauchy multiplicative-to-additive functional
equation** `g(Nx) = N g(x)` (`N ∈ ℕ`), which together with
continuity in `r` forces `g` linear and hence `f = c log`. This is the
same Cauchy classifier (Pattern L) that consolidated Route D
[(no_go PR #1408)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1408)
identified as the universal obstruction across Routes A/B/C/E.
Extensivity is therefore a **FIFTH equivalent vocabulary** for the same
selection step (alongside Cauchy, Shannon-Khinchin K3, Tempesta
composability + additive-formal-group selection, and free-energy
`F = -k_B T log Z` Pattern-L invocations). It does not bypass the
Route D D5 Pattern L circularity; it routes through it. Independently,
the bulk-replication thermodynamic-limit existence of `W/|Λ|`
(Ruelle 1969; Israel 1979) requires translation-invariance (A2,
retained baseline) **and** finite-range interactions, where the
finite-range structure on the staggered-Dirac realization is currently
the `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03` `open_gate`
on the live ledger. So extensivity carries the same A3 dependency as
the prior pre-record tracial route (PR #1618). Either branch is fatal
to a positive_theorem closure on the current ledger.

**Runner:**
[`scripts/frontier_observable_principle_p1_bridge_extensivity_primitive.py`](../scripts/frontier_observable_principle_p1_bridge_extensivity_primitive.py)

This is a source-note proposal; the independent audit lane sets any
audit verdict and pipeline-derived effective status. This note does
**not** promote or alter the status of
[`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
or any cited upstream row.

## 0. Honest framing up front

The originating hypothesis for this route was that the **extensivity
primitive** (E) — interpreted as a *physical scaling premise* tied to
the thermodynamic limit rather than as a functional-analytic
classification — would FORCE the log form `W = c · log|Z|` via the
elementary multiplicative-to-additive computation:

```text
|Z[J^{(N)}]|  =  |Z[J]|^N            (bulk replication, det block-diag)
W[J^{(N)}]    =  N · W[J]            (E, extensivity premise)
⇒  W            =  c · log|Z| + const  (only solution under continuity in |Z|).
```

The hope was that this bypasses the [Route D
(PR #1408)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1408)
D5 Pattern L circularity because the selection happens through a
**concrete quantitative scaling defect** (the candidate `F_p[J] = r^p`
on `Λ^N` gives `|Z|^{Np}`, which fails `N · |Z|^p` for generic `|Z|`
and `p ≠ 0`), not through an abstract functional-equation
classification.

Honest stress test outcome: **the bypass does not work.** The
quantitative scaling defect IS the integer-N restriction of the Cauchy
multiplicative-to-additive functional equation, applied to `g(x) :=
W[J]|_{log|Z[J]| = x}`. With continuity in `|Z|`, `g(Nx) = N g(x)` for
all `N ∈ ℕ` forces `g` linear (see §3.2 and the runner T3 / T4 exact
SymPy verifications). The forcing mechanism is identical to Cauchy
classification; the vocabulary "extensivity under bulk replication" is
the FIFTH equivalent surface for the same selection step.

A separate, independent obstruction: the thermodynamic-limit existence
of the intensive density `w_∞[j] := lim_{|Λ|→∞} W[J]/|Λ|` (which is the
genuine physical content of "extensivity" in lattice statistical
mechanics; Ruelle 1969; Israel 1979; Bratteli-Robinson Vol II 1981)
requires translation invariance (A2, retained baseline) **plus**
finite-range / decay-controlled interactions. The finite-range structure
on the framework's staggered-Dirac realization is currently the
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03` `open_gate` on the
live ledger (effective_status `open_gate` per
`docs/audit/data/audit_ledger.json`). So even if one were to wave off
the Pattern-L circularity above, the substantive thermodynamic-limit
argument carries the same A3 open-gate dependency as the prior
[Route B (PR #1618) pre-record tracial route](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1618).

Two independently-fatal findings for a positive_theorem closure on the
current ledger. The honest landing is therefore a narrow **no_go**
documenting (i) extensivity as a fifth Pattern-L vocabulary for the
same Cauchy selection, and (ii) the A3-open-gate dependency of the
substantive thermodynamic-limit route.

This note explicitly DOES NOT claim:
- P1 is false. `W = log|Z|` is still the natural choice; extensivity is
  consistent with it.
- That extensivity is the wrong physical premise. It is a perfectly
  reasonable physical scaling premise; the finding is that it is
  *equivalent in selection content* to P1 under bulk replication.
- That `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` should be demoted. Its
  audit verdict `audited_conditional` already admits P1 as a bridge
  premise; this no_go provides additional structural backing.
- That `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03` should be
  demoted or promoted. The gate's `open_gate` effective_status is
  unchanged; this note only documents its load-bearing role in any
  substantive thermodynamic-limit extensivity argument.

## 1. Mandatory four exercises (concrete output)

### 1.1 Assumption audit

Listed premises for the (E)-routed P1 closure attempt, with explicit
status classification:

| Premise | Class | Status / source |
|---|---|---|
| A1 — qubit at every site (`M_2(ℂ)` per `x ∈ Z³`) | (a) framework axiom | [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) |
| A2 — `Z³` lattice with translation symmetry | (a) framework axiom | [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) |
| A3 — staggered-Dirac realization (finite-range / locality) | (a) open gate | [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md), live status `open_gate` |
| Block-diagonal det factorization `det(D_A ⊕ D_B) = det(D_A) · det(D_B)` | (b) elementary linear algebra | retained as standard linear algebra; runner T2 verifies on SymPy 4×4 sample |
| Bulk replication `Λ → Λ^N` is a well-defined operation on lattice region | (a/d) admitted under A2 translation invariance | direct from `Z³` translation structure |
| Continuity in `|Z|` for the scalar generator `W` | (d) admitted regularity (also P3 of the parent note) | parent note `audited_conditional` premises P1-P4 |
| Extensivity primitive (E): `W[J^{(N)}] = N · W[J]` | (d) admitted as candidate premise | THIS NOTE — the candidate primitive under audit |
| Thermodynamic-limit existence of `w_∞[j] = lim W/\|Λ\|` | (c) external lit import | Ruelle 1969; Israel 1979; Bratteli-Robinson Vol II 1981 — REQUIRES A3 finite-range |

Critical specific audits per the prompt:

- **"Bulk replication of region Λ → N disjoint copies":** trivially
  defined under A2 (`Z³` translation symmetry); not load-bearing
  separately.
- **"Thermodynamic-limit existence of `W/|Λ|`":** NOT a retained narrow
  theorem in the live audit ledger. Standard treatments (Ruelle 1969;
  Israel 1979) require finite-range / Kirkwood-Salsburg-decaying
  interactions, which is the A3 = `staggered_dirac_realization_gate_note_2026-05-03`
  `open_gate` content on the live ledger.
- **"Does the extensivity primitive depend on A3 closure?":** YES for
  the substantive thermodynamic-limit interpretation (the
  Ruelle/Israel theorems require finite-range to even define the
  bulk free-energy density). NO for the *pure*
  algebraic-bulk-replication interpretation (the determinant block
  identity `det(D_{Λ^N}) = det(D_Λ)^N` is elementary linear algebra,
  needing no A3 closure). But the pure algebraic version reduces to
  the Cauchy classifier (§3) and is P1 in different vocabulary, not
  an independent derivation.

So one branch (substantive lit-imported extensivity) depends on A3
closure; the other branch (pure algebraic bulk replication) reduces to
the Cauchy classifier. **Both branches are fatal to positive_theorem
closure on the current ledger.**

### 1.2 Elon Musk first-principles

**Strip to first principles.** Why does extensivity force the log form?

The bare logical chain:

1. **Multiplicative factorization of `|Z|` under bulk replication.**
   By the block-diagonal determinant identity `det(D_{Λ^N}) =
   det(D_Λ)^N`, on N disjoint copies of `Λ` with identical sources `J`,
   the partition function magnitude factorizes as
   ```
   |Z[J^{(N)}]|  =  |Z[J]|^N.                                      (M)
   ```
   This step is elementary linear algebra; it uses no extensivity
   premise and no A3 finite-range content. (Runner T2 verifies on a
   SymPy 4×4 real anti-Hermitian sample.)

2. **Extensivity premise (E):** `W[J^{(N)}] = N · W[J]` for all
   `N ∈ ℕ` and all source configurations `J`.

3. **Combine M + E:** define `f: ℝ_+ → ℝ` by
   `f(|Z[J]|) := W[J]` (well-defined because P3 = continuity says `W`
   depends only on `|Z|` on the CPT-even sector; abuse of notation
   for the dependence structure under bulk replication). Then
   ```
   f(|Z|^N)  =  W[J^{(N)}]  =  N · W[J]  =  N · f(|Z|),            (Cm-N)
   ```
   i.e., `f(r^N) = N · f(r)` for all `N ∈ ℕ` and `r > 0`.

4. **Forcing.** Substitute `g(x) := f(e^x)` (well-defined for `r > 0`
   via `r = e^x`). Equation (Cm-N) becomes
   ```
   g(Nx)  =  N · g(x),       N ∈ ℕ, x ∈ ℝ.                         (Cg-N)
   ```
   With continuity in `r` (equivalently in `x`), define
   `h(x) := g(x)/x` for `x ≠ 0`. Equation (Cg-N) gives
   `h(Nx) = g(Nx)/(Nx) = N g(x)/(Nx) = g(x)/x = h(x)`, so `h` is
   invariant under multiplication by every positive integer.
   By continuity and density of `{Nx : N ∈ ℕ, x ∈ (0,1)}` in `ℝ_+`,
   `h` is constant. Hence `g(x) = c · x`, i.e., `f(r) = c · log r`,
   i.e., `W[J] = c · log|Z[J]| + const`. The "+ const" absorbs the
   `g(0)` ambiguity; setting `W[J=0] = 0` (P4 normalization in the
   parent note) fixes const.

So **extensivity (E) + multiplicative factorization (M) + continuity in
|Z| ⟹ W = c log|Z|**. The derivation is honest, the algebra is
elementary.

**Now ask: is extensivity an axiom-level demand, or does it follow from
more fundamental structure?**

Two readings:

(a) **Pure algebraic-bulk-replication reading.** Extensivity (E) is
posited as an *independent admitted premise* on the candidate physical
scalar observable generator. The bulk replication operation is forced
by A2 translation invariance + elementary determinant block identity.
Under this reading, **(E) IS the selection premise**: it is a
classification step on candidate scalar generators selecting the
additive class over the `F_p = |Z|^p` (`p ≠ 0`) multiplicative-only
class. The selection is then forced by (Cg-N), which is the
integer-N restriction of the Cauchy multiplicative-to-additive
functional equation. **This is P1 in different vocabulary**, by
exactly the same logic as Tempesta composability (PR #1404) reduces
to P1 under "additive-formal-group selection" and Shannon-Khinchin K3
(PR #1368) reduces to P1 under "chain-rule selection." Pattern-L
circularity D5 applies.

(b) **Substantive thermodynamic-limit reading.** Extensivity is not
posited as an axiom but DERIVED as the existence of the bulk free
energy density `w_∞[j] := lim_{|Λ|→∞} W[J]/|Λ|` under
Kirkwood-Salsburg-controlled interactions (Ruelle 1969 Chapter 2;
Israel 1979 Chapter II; Bratteli-Robinson Vol II 1981 §6.2). This
substantive reading is genuine *physical* extensivity, not a
classification fiat. But the Ruelle/Israel/Bratteli-Robinson theorems
require finite-range or exponentially-decaying interactions on the
lattice; in the framework, this is the staggered-Dirac realization
finite-range structure, which is currently the `open_gate` on the
live ledger.

Articulate the structural distinction:

- (a) is honest about P1 selection-equivalence and yields no_go via
  Pattern L.
- (b) would yield bounded_theorem (P1 closed, modulo A3 open gate), but
  the A3 dependency is the same as the prior pre-record tracial route
  (PR #1618 Route B), which also landed bounded_theorem with explicit
  A3 dependency.

**Either way, no positive_theorem closure on the current ledger.**
The honest outcome under (a) is no_go (fifth Pattern-L vocabulary);
under (b) is bounded_theorem (with A3 dependency). This note documents
(a) as the dominant outcome because it is the route that does not
depend on A3 closure — i.e., the most generous interpretation of
"extensivity as a primitive" still doesn't bypass Pattern L.

### 1.3 Literature search

External authorities directly relevant to the extensivity premise:

1. **Ruelle 1969** — D. Ruelle, *Statistical Mechanics: Rigorous
   Results*, W. A. Benjamin (1969); reprinted World Scientific (1999).
   Chapter 2 ("The Thermodynamic Limit") establishes existence of the
   thermodynamic-limit free-energy density for classical lattice
   systems with translation-invariant interactions of finite range or
   appropriately decaying long range. This is the standard external
   citation for "extensivity is a derived property" in the lattice
   statistical mechanics literature. **Requires finite-range** —
   matches the A3 open gate on the live ledger.

2. **Israel 1979** — R. B. Israel, *Convexity in the Theory of Lattice
   Gases*, Princeton University Press (1979). Chapter II ("Pressure
   and equilibrium states") extends Ruelle's results to quantum
   lattice systems via the C*-algebraic framework, establishing
   `lim_{|Λ| → ∞} (1/|Λ|) log Tr_Λ(e^{-β H_Λ})` exists for
   translation-invariant interactions of finite range. Same A3
   dependency.

3. **Bratteli-Robinson Vol II 1981** — O. Bratteli & D. W. Robinson,
   *Operator Algebras and Quantum Statistical Mechanics, Vol. II*,
   Springer (1981, 2nd ed. 1997). §6.2 ("The Thermodynamic Limit")
   gives the operator-algebraic treatment of the bulk free-energy
   density on UHF C*-algebras (matching the qubit-trace setting of
   `OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20`).
   Theorem 6.2.4 states existence of
   `p(Φ) := lim_{Λ ↑ ∞} |Λ|^{-1} log Tr_Λ(e^{-β H_Λ(Φ)})` for
   translation-invariant Banach-space interactions `Φ ∈ B`.
   The interaction-norm finiteness condition is the modern formulation
   of the A3 finite-range / decay structure.

4. **Tempesta 2014/2015/2018/2024** — already cited in the prior
   [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_TEMPESTA_COMPOSABILITY_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_TEMPESTA_COMPOSABILITY_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md).
   The Tempesta route already identifies extensivity as one of the
   additional principles needed to select the additive formal-group
   subclass after composability is imposed: "*selecting one over the
   others requires an additional principle (extensivity,
   thermodynamic limit, or a specific identification of the physical
   scalar generator with the additive subclass)*" (Tempesta route §1.2).
   This is the **published precedent** that "extensivity" is exactly
   the additive-subclass selection step on the formal-group classification —
   i.e., a vocabulary for P1.

5. **Sokal 1981** — A. D. Sokal, J. Stat. Phys. 25 (1981), 51-92,
   "Existence of compatible families of proper regular conditional
   probabilities," and related work on uniqueness of equilibrium
   states under DLR conditions. Sokal's results require
   finite-range interactions to even define the consistent
   family of conditional distributions; same A3 dependency.

6. **Borgs-Imbrie 1992** — C. Borgs & J. Imbrie, Comm. Math. Phys.
   145 (1992), 235-280, "A unified approach to phase diagrams in field
   theory and statistical mechanics," gives extensivity of effective
   actions in low-temperature expansions of lattice field theories.
   Their setup explicitly assumes finite-range Hamiltonian; A3
   dependency.

7. **Wilson-Kogut 1974** — K. G. Wilson & J. Kogut, Phys. Rep. 12
   (1974), 75-199, "The renormalization group and the epsilon
   expansion." Extensivity of the effective action under block-spin
   coarse-graining is taken as a foundational physical premise of the
   Wilson renormalization-group framework. Pattern-L circularity D5
   applies if interpreted as a classification fiat; A3 dependency
   if interpreted as substantive bulk-limit content.

8. **Symanzik 1983** — K. Symanzik, Nucl. Phys. B 226 (1983), 187-204,
   "Continuum limit and improved action in lattice theories." Bulk
   extensivity of the lattice effective action under continuum limit;
   requires finite-range improvement program. Same A3 dependency.

9. **Susskind 1977 / Kogut-Susskind 1975** — L. Susskind, Phys. Rev. D
   16 (1977), 3031-3039; J. Kogut & L. Susskind, Phys. Rev. D 11
   (1975), 395-408. The staggered-fermion construction itself; provides
   the finite-range structure on which bulk free-energy density
   arguments would apply *if* the framework's A3 staggered-Dirac gate
   were closed. Currently A3 = `open_gate`.

10. **Lieb-Yngvason 1998** — E. H. Lieb & J. Yngvason, *Physics
    Reports* 310 (1999), 1-96, "The physics and mathematics of the
    second law of thermodynamics" (also arXiv:cond-mat/9708200).
    Axiomatic derivation of entropy and extensivity from
    adiabatic-accessibility primitives; explicitly identifies
    extensivity as a non-trivial structural primitive of
    thermodynamics rather than a derived consequence of other axioms.
    Their "(S5) Scaling" axiom is essentially (E) repackaged as a
    thermodynamic admissibility primitive. **Independent
    confirmation** that extensivity is a primitive in the same
    classification-step sense as P1.

No published derivation of `W = c log|Z|` on a real-valued scalar
functional of a multiplicatively factorizing partition function via
extensivity that bypasses the Cauchy classification (Pattern L) or the
finite-range A3 dependency.

### 1.4 Math search (Tao-style)

**Bare math problem.** Let `D_Λ` be a self-adjoint operator on a finite-
dimensional Hilbert space `H_Λ` with
`D_{Λ^N} := D_Λ ⊕ D_Λ ⊕ ... ⊕ D_Λ` (`N` disjoint copies) on
`H_Λ^{⊗N}` (block-direct-sum, not tensor product). Define a
continuous, non-trivial real-valued functional
`W : M_{sa}(H_Λ) → ℝ` (self-adjoint matrices to reals). Suppose

```
W(D_{Λ^N})  =  N · W(D_Λ)        for all N ∈ ℕ                       (E')
```

(an abstract version of bulk-replication extensivity (E)). What is the
classification of `W`?

**Math answer.** Setting `r := |det(D_Λ)|` and `f(r) := W(D_Λ)|_{r =
|det D|}` (well-defined on the CPT-even / phase-blind sector), we have

```
|det(D_{Λ^N})|  =  |det(D_Λ)|^N            (block-direct-sum det identity)
W(D_{Λ^N})       =  f(|det(D_Λ)|^N)         (definition)
                  =  N · f(|det(D_Λ)|)      (by (E'))
```

so `f(r^N) = N · f(r)` for all `N ∈ ℕ` and `r > 0`.

Set `g(x) := f(e^x)` for `x ∈ ℝ`. Then

```
g(Nx)  =  f(e^{Nx})  =  f((e^x)^N)  =  N · f(e^x)  =  N · g(x).     (Cg-N)
```

**Lemma (Cauchy integer-scaling classifier).** If `g: ℝ → ℝ` is
continuous and `g(Nx) = N · g(x)` for all `N ∈ ℕ` and `x ∈ ℝ`, then
`g(x) = c · x` for some `c ∈ ℝ`.

*Proof sketch (also exercised in runner T4).* For `x ≠ 0`, define
`h(x) := g(x)/x`. Then `h(Nx) = g(Nx)/(Nx) = N g(x)/(Nx) = g(x)/x =
h(x)`, so `h` is invariant under multiplication by every positive
integer. For any two positive reals `x_1, x_2`, by Dirichlet's theorem
on density of `{N_1 / N_2 : N_1, N_2 ∈ ℕ}` in `ℝ_+`, there exists a
sequence `N_k / M_k → x_2 / x_1`, giving `M_k x_2 → N_k x_1` (up to
subsequence), so by continuity `h(x_2) = h(x_1)`. Hence `h` is
constant on `ℝ_{>0}`, say `h ≡ c`; similarly on `ℝ_{<0}`, say `h ≡ c'`.
At `x = 0`, (Cg-N) gives `g(0) = N g(0)` for `N = 2`, so `g(0) = 0`,
matching `g(x) = c · x` at `x = 0^+` and `g(x) = c' · x` at `x = 0^-`.
Symmetry of (Cg-N) under `x → -x` gives `c = c'`, so `g(x) = c · x`
globally.

Hence `f(r) = c · log r`, i.e., `W(D) = c · log|det D| + const`. QED.

**Honest math danger** (per prompt): the above lemma IS the Cauchy
multiplicative-to-additive classification step, just restricted to
integer-N scaling instead of arbitrary multiplicative pairs. The
forcing mechanism is identical:

```
classical Cauchy (Routes A/B/D):   f(r_A · r_B) = f(r_A) + f(r_B)
                                                       + continuity ⇒ c log
extensivity (this route):          f(r^N) = N · f(r) for N ∈ ℕ
                                                       + continuity ⇒ c log
```

Both reduce to "continuous group homomorphism `(ℝ_+, ·) → (ℝ, +)`,
unique up to base." The extensivity route is genuinely weaker as a
*premise* (integer-N scaling is weaker than arbitrary product
decomposition), but the *forcing conclusion* under continuity is
identical: `W = c log|Z|`. Therefore extensivity routed through bulk
replication **IS** Pattern-L circularity D5 in a fifth equivalent
vocabulary.

**The math finding is genuinely orthogonal-to-G3 only on its premise
side, not on its forcing side.** The forcing reduces to Cauchy via
(Cg-N). This is the make-or-break honest finding of the route.

## 2. Premise statement (extensivity primitive + derivation chain)

### 2.1 Premise (E): bulk-replication extensivity

**Premise (E).** *The framework's physical scalar observable generator
`W : M_{sa}(H_Λ) → ℝ` is extensive under bulk replication: for the
lattice region `Λ → Λ^N := Λ_1 ⊔ Λ_2 ⊔ ... ⊔ Λ_N` consisting of `N`
disjoint copies of the same finite region, with identical source
configurations `J^{(N)} := J ⊕ J ⊕ ... ⊕ J`,*

```
W[J^{(N)}]  =  N · W[J]            for all N ∈ ℕ and all admissible J.    (E)
```

Equivalent intensive-density form: `lim_{|Λ| → ∞} W[J] / |Λ| =
w_∞[J/|Λ|]` is a well-defined intensive functional (the bulk free-
energy density of Ruelle 1969 / Israel 1979).

### 2.2 Bulk-replication factorization (M)

By the block-diagonal determinant identity, on the staggered-Dirac
representation (A3 conditional) or equivalently on the qubit-trace
representation
[(`OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20.md`)](OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20.md):

```
det(D_{Λ^N})  =  det(D_Λ ⊕ D_Λ ⊕ ... ⊕ D_Λ)  =  det(D_Λ)^N            (M-det)
Tr_{A_{Λ^N}}(e^{-(H_{Λ^N} + J^{(N)})})  =  Tr_{A_Λ}(e^{-(H_Λ + J)})^N  (M-tr)
```

so

```
|Z[J^{(N)}]|  =  |Z[J]|^N.                                              (M)
```

Both (M-det) and (M-tr) are elementary block-diagonal / tensor-product
identities; runner T2 verifies (M-det) on a SymPy 4×4 real
anti-Hermitian sample.

### 2.3 Derivation chain (E) + (M) + continuity ⟹ `W = c log|Z| + const`

Substituting (M) into (E):

```
W[J^{(N)}]  =  N · W[J]                                                (E)
|Z[J^{(N)}]|  =  |Z[J]|^N                                              (M)
                ⇒  f(|Z[J]|^N)  =  N · f(|Z[J]|),                      (Cm-N)
```

where `f(r) := W[J]` written as a function of `r = |Z[J]|` via P3
continuity (`W` depends on `J` only through `|Z[J]|` on the CPT-even
sector).

By the Cauchy integer-scaling lemma of §1.4: under continuity in `r`,
(Cm-N) forces `f(r) = c · log r + const`, hence

```
W[J]  =  c · log|Z[J]| + const.                                       (W-form)
```

Setting `const = -c · log|Z[J=0]|` recovers the standard normalization
`W[0] = 0` (P4 of the parent note).

### 2.4 P1 (block-additivity on arbitrary partitions) follows trivially

Once `W = c log|Z|` is fixed, for any arbitrary block-diagonal
partition `D = D_A ⊕ D_B` (not just bulk-replicated N-copies),

```
W[J_A ⊕ J_B]  =  c · log|det(D_A + J_A) · det(D_B + J_B)|
              =  c · log|Z_A| + c · log|Z_B|
              =  W[J_A] + W[J_B].                                     (P1)
```

So if extensivity (E) were a retained primitive independent of P1,
this chain would close P1 cleanly. The crux is therefore: **is
extensivity (E) retainable independent of P1?**

## 3. Load-bearing step (class A)

### 3.1 Class A statement

The load-bearing class A step is the **honest classification finding**:

> **Class A (load-bearing).** The selection of the log subclass `W =
> c · log|Z|` from the candidate functional family `{f(|Z|) :
> f continuous}` via the extensivity premise (E) and the bulk-
> replication factorization (M) reduces — by substitution `g(x) :=
> f(e^x)` — to the integer-N restriction of the Cauchy multiplicative-
> to-additive functional equation `g(Nx) = N g(x)` (Cg-N). Continuity
> in `|Z|` then forces `g` linear, hence `f = c log`. This integer-N
> Cauchy classification is the same forcing mechanism as the standard
> Cauchy multiplicative-to-additive functional equation (Routes A/B/D
> D5 Pattern L), just on the weaker integer-N scaling premise instead
> of arbitrary product decomposition. **Extensivity (E) is therefore a
> fifth equivalent vocabulary for the same Cauchy selection step** —
> joining Cauchy classification (Aczel 1966), Shannon-Khinchin K3
> (Khinchin 1957), Tempesta composability + additive-formal-group
> selection (Tempesta 2014/2015), and free-energy `F = -k_B T log Z`
> (Landau-Lifshitz 1980). The selection is forced; the *selection step
> itself* is a classification fiat equivalent to P1.

This is honest. It is consistent with the Tempesta route's published
observation (Tempesta arXiv:1507.07436, 2015) that "extensivity" is
exactly the additional principle needed to select the additive
formal-group subclass after composability is imposed — which is itself
the classification-step equivalent of P1.

### 3.2 Class A verification

The runner verifies at exact SymPy / Fraction precision:

- **T1** Note structure check: contains all required section markers
  (§0-§7), the (E) premise statement, the (M) factorization statement,
  the (W-form) conclusion, the Class A statement, and the §5 audit-
  lane disposition YAML.
- **T2** Block-diagonal det factorization on SymPy 4×4 real
  anti-Hermitian sample: `det(D_A ⊕ D_B + J_A ⊕ J_B) = det(D_A + J_A)
  · det(D_B + J_B)` symbolically; bulk replication `det(D_Λ^N) =
  det(D_Λ)^N` for N ∈ {2, 3, 4} on a 2×2 sample.
- **T3** Counterexample family `F_p[J] = r^p` (`p ≠ 0`) is
  block-multiplicative but NOT bulk-extensive. Symbolic:
  `(r^N)^p ≠ N · r^p` for `p ≠ 0` and generic `r > 1`; rational grid
  check at `p ∈ {-2, -1, 1/2, 2, 3}` and `r ∈ {3/2, 2, 11/7}`,
  `N ∈ {2, 3, 5}`.
- **T4** Cauchy integer-scaling forcing: the unique continuous solution
  of `g(Nx) = N g(x)` for `g: ℝ → ℝ`, `N ∈ ℕ`, `x ∈ ℝ` is `g(x) = c x`
  for some `c ∈ ℝ`. Exercised by exact verification on a rational test
  grid: `g(x) = c x` satisfies (Cg-N) symbolically; `g(x) = x^2` and
  `g(x) = e^x - 1` and `g(x) = sin(x)` each FAIL (Cg-N) at some
  `(N, x)`. Combined with the elementary derivation in §1.4 lemma,
  this confirms the forcing.
- **T5** Pattern L equivalence: the four prior Pattern-L vocabularies
  (Cauchy, Shannon-Khinchin K3, Tempesta composability + additive
  selection, free-energy `-k_B T log Z`) ALL reduce to the same
  `f(r) = c log r` conclusion. Symbolic verification on the conclusion;
  ledger status check that all four corresponding bridge notes landed
  as `bounded_theorem` or no_go with explicit Pattern L admission.
- **T6** A3 open-gate dependency for the substantive thermodynamic-
  limit reading: read `docs/audit/data/audit_ledger.json` for
  `staggered_dirac_realization_gate_note_2026-05-03`, verify
  `effective_status == "open_gate"`.
- **T7** Honest scope check: parses note for explicit no_go
  statement, explicit non-promotion language, explicit absence of
  status-promotion strings.
- **T8** Source-note boundary check: `Claim type: no_go`,
  `Status authority: independent audit lane only`, no forbidden
  retained / promoted language.

Expected runner result: `PASS=N, FAIL=0`.

## 4. What this closes / what remains admitted

### 4.1 What this no_go closes (positive content)

- **Documents extensivity as a fifth Pattern-L vocabulary for the same
  Cauchy selection step.** Future agents do not need to re-attempt
  extensivity routes for P1 closure expecting a bypass of Pattern L;
  this no_go records the explicit (Cg-N) reduction.
- **Identifies two independent obstructions to a positive-theorem
  closure** of P1 via extensivity:
  (i) the (Cg-N) integer-N Cauchy reduction (Pattern L);
  (ii) the A3 open-gate dependency for the substantive
  thermodynamic-limit (Ruelle/Israel/Bratteli-Robinson) reading.
- **Confirms** the prior Tempesta-route observation (PR #1404) that
  extensivity is exactly the additional principle needed to select the
  additive subclass after composability — by independently identifying
  the same equivalence from the bulk-replication-factorization
  direction.
- **Aligns with Lieb-Yngvason 1998** axiomatic-thermodynamics finding
  that extensivity ("(S5) Scaling") is a primitive at the
  classification-step level, not a derived consequence of more
  fundamental axioms.

### 4.2 What remains admitted

- P1 (scalar additivity on independent subsystems) remains admitted as
  a physical-principle selection premise of
  [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md);
  its audit verdict `audited_conditional` is unaffected by this no_go.
- The bounded-theorem alternative (extensivity from substantive
  thermodynamic-limit arguments conditional on A3 closure) remains
  available as a future bounded route, but inherits the A3 open-gate
  dependency of the prior pre-record tracial route (PR #1618).
- The forward paths from Route D §5 remain unchanged:
  (a) a new retained-grade primitive that excludes `F_p` without
  invoking `log` (research-grade open);
  (b) accept P1 as a permanent classification premise (current state
  of the parent note).

## 5. Audit-lane disposition (proposed YAML)

The following YAML stub is for the audit lane's convenience; the audit
lane sets the actual ledger row, not this source note.

```yaml
claim_id: observable_principle_p1_bridge_extensivity_primitive_narrow_note_2026-05-21
claim_type: no_go
proposed_status: source_note_only
effective_status: (set by audit pipeline)
scope: |
  Narrow sharpened no-go on the extensivity primitive as a candidate
  derivation of the P1 admitted premise of OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.
  Documents that extensivity routed through bulk replication reduces to the
  integer-N Cauchy multiplicative-to-additive classifier (Pattern L D5),
  and that the substantive thermodynamic-limit reading carries an A3
  open-gate dependency.
load_bearing_authorities:
  - observable_principle_from_axiom_note  # parent (audited_conditional)
  - staggered_dirac_realization_gate_note_2026-05-03  # A3 open_gate dependency
  - observable_principle_p1_bridge_route_d_sharpened_no_go_note_2026-05-17  # D5 Pattern L
external_citations:
  - "Ruelle 1969 (Statistical Mechanics: Rigorous Results, Ch. 2)"
  - "Israel 1979 (Convexity in the Theory of Lattice Gases, Ch. II)"
  - "Bratteli-Robinson 1981 (Operator Algebras and QSM Vol. II, §6.2)"
  - "Tempesta 2014/2015 (arXiv:1407.3807, 1507.07436)"
  - "Lieb-Yngvason 1998 (Phys. Rep. 310, 1-96)"
  - "Aczel 1966 (Lectures on Functional Equations, §2.1)"
proposal_allowed: false  # source-note only; no proposed promotion
admitted_context_inputs:
  - "Bulk replication operation on Z^3 lattice (A2 translation invariance)"
  - "Continuity in |Z| (P3 of parent note)"
  - "Block-diagonal det / trace-tensor factorization (elementary)"
forbidden_imports_check: pass
no_promotion_check: pass  # explicit non-promotion language in §0 and §9
```

## 6. Comparison with route portfolio

| Route | Vocabulary | Forcing mechanism | Outcome |
|---|---|---|---|
| A — operator-algebraic external (PR #1373) | Hilbert tensor product, type II_1 trace-state, Reeh-Schlieder | Cauchy on multiplicative pairs `f(r_A · r_B) = f(r_A) + f(r_B)` | bounded_theorem (D1+D5) |
| B — Shannon-Khinchin external (PR #1368) | Shannon-Khinchin K3 chain rule, Aczel-Daroczy | Cauchy on chain-rule additivity hypothesis | bounded_theorem (D2+D5) |
| C — framework-internal (PR #1402) | Retained primitive enumeration | No retained primitive independently excludes `F_p` | bounded_theorem (D3) |
| D — sharpened no_go (PR #1408) | Cross-route consolidation | All four routes reduce to Pattern L or Pattern D | no_go (D1-D5) |
| E — Tao cross-disciplinary (PR #1406) | Atiyah-Singer, K-theory, Cramer, tropical, ... | Pattern L (Cauchy in disguise) or Pattern D (inapplicable) | bounded_theorem (D4+D5) |
| Tempesta composability (PR #1404) | Formal group laws (Lazard) | Composability admits infinite formal-group family; additive selection = P1 | bounded_theorem (D5 in Lazard vocabulary) |
| Pre-record tracial (PR #1618) | C* tracial state factorization | F_p obstruction + A3 inter-algebra gap | bounded_theorem (open A3 gate) |
| Qubit-trace (PR ?, 2026-05-20) | UHF C* tracial factorization | P1 trivially holds for `W_qubit = log Tr e^{-(H+J)}`; transfer to `log|det(D+J)|` is gate-conditional | bounded_theorem candidate |
| Gleason-Busch (PR #1620) | Born-rule reconstruction | Born rule selects probability functor; selection step IS P1 | no_go |
| Free cumulant (PR #1616) | Voiculescu free probability | Wrong tool (free cumulants are for free independence, not classical/tensor independence) | bounded_theorem |
| Operator-algebraic qubit re-attempt (PR #1619) | C* operator-algebraic | Universal-quantifier bug repair, F_p obstruction | bounded_theorem |
| **This note — extensivity primitive** | **Bulk-replication scaling under N → ∞** | **Integer-N Cauchy `g(Nx) = N g(x)` (a fifth Pattern-L vocabulary)** | **no_go (D5 in extensivity vocabulary)** |

This note adds the **fifth equivalent vocabulary for Pattern L** to the
catalog. The structural finding strengthens Route D's consolidated
no_go by demonstrating that even a physical-scaling premise (rather
than a functional-analytic classification) reduces to the same Cauchy
forcing mechanism under continuity.

## 7. Cross-references

- Parent (P1 admitted premise lives here):
  [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
- Audit packet:
  [`OBSERVABLE_PRINCIPLE_AUDIT_NOTE_2026-05-02.md`](OBSERVABLE_PRINCIPLE_AUDIT_NOTE_2026-05-02.md)
- Consolidated Route D no_go (the Pattern-L D5 obstruction this note
  routes through):
  [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17.md)
- Tempesta composability route (independent identification of
  extensivity as additive-subclass selection):
  [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_TEMPESTA_COMPOSABILITY_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_TEMPESTA_COMPOSABILITY_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)
- Route A operator-algebraic external:
  [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_OPERATOR_ALGEBRAIC_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_OPERATOR_ALGEBRAIC_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)
- Route B Shannon-Khinchin external:
  [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)
- Route C framework-internal:
  [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_FRAMEWORK_INTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_FRAMEWORK_INTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)
- Route E Tao cross-disciplinary:
  [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_E_TAO_CROSS_DISCIPLINARY_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_E_TAO_CROSS_DISCIPLINARY_NARROW_BOUNDED_NOTE_2026-05-17.md)
- Qubit-trace P1+P2 attempt (UHF C* tracial; closest prior closure
  attempt with explicit qubit-substrate framing):
  [`OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20.md`](OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20.md)
- A3 open-gate dependency:
  [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- CPT upstream (P2 phase blindness):
  [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)
- Minimal axiom baseline:
  [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)

## 8. Repo vocabulary discipline

This note uses only repo-canonical vocabulary:

- "extensivity primitive" — descriptive label for the (E) premise; not
  a new repo tag.
- "bulk replication" — repo-canonical (standard lattice-physics term).
- "block-diagonal determinant identity", "trace-tensor factorization"
  — repo-canonical elementary linear algebra.
- "Pattern L" / "Pattern D" — Route E / Route D vocabulary, used here
  as descriptive labels for the structural patterns; not a new repo
  tag.
- "counterexample family `F_p[J] = r^p`" — Route A/C/E/D vocabulary,
  used here as the standard non-extensive multiplicative scalar
  functional.
- "Cauchy integer-scaling classifier" — descriptive label for the
  forcing lemma of §1.4; not a new repo tag.

No new repo-wide tags, no new framework classifications, no
status-promotion language.

## 9. Status authority and source-note boundary

This is a source-note proposal only. The independent audit lane sets
audit results and pipeline-derived effective status. This note does
not predict or claim an audit verdict.

- **Claim type:** no_go.
- **Status authority:** independent audit lane only.
- **Effective status on creation:** to be set by the audit pipeline,
  not authored.

This note does not promote, alter, or set the audit status of:

- [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  (stays `audited_conditional`);
- [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17.md)
  (stays at current ledger status);
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  (stays `open_gate`);
- [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md) (stays
  `audited_conditional`);
- Any other cited row.
