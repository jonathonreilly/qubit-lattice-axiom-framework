# How Much Of Born Is Unconditional From {Quantum + Record}

**Date:** 2026-06-05
**Claim type:** conditional / support (with a sharpened residual)
**Status authority:** independent audit lane only. This source note does not set,
predict, or assert an audit verdict and does not claim "retained" or "promoted"
standing.
**Primary runner:**
[`scripts/frontier_born_quantum_record_unconditional_2026_06_05.py`](../scripts/frontier_born_quantum_record_unconditional_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_born_quantum_record_unconditional_2026_06_05.txt`](../logs/runner-cache/frontier_born_quantum_record_unconditional_2026_06_05.txt)
(PASS=29, FAIL=0; peak RSS ~85 MB).

---

## Scope and honesty (read first)

This note sharpens the prior conditional result
[`BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL_PROBABILITY_NOTE_2026-06-05.md`](BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL_PROBABILITY_NOTE_2026-06-05.md)
("#2702"), which pinned the single residual admission to `A3` = "a probability
measure **exists and is a function of the state**." The sharpening tests whether
part of `A3` is already **inside** {Quantum, Record} once one reads the *algebra*
rather than the axiom memo's prose, and then attacks the genuinely residual piece
via the record-frequency structure.

The honest result is still **conditional**, but the residual is now much smaller
and precisely named:

- The Born **form** `omega = Tr(rho .)` and the Born **value** `|a_k|^2` for pure
  states are unconditional from {Quantum, Record} **as a formal probability
  functional** (modulo a small normalization input).
- The **only** genuinely residual piece is the **operational identification**
  that this functional equals the **empirical relative frequencies you record**.
  The frequency-operator route does **not** discharge it non-circularly: the
  convergence step re-imports the Born norm (Hartle's known critique).

**We do not claim "Born unconditional."** Born is unconditional as a *formal
probability functional*; its identification *as a frequency* is
**conditional on typicality**.

---

## 1. The sharpening: the algebraic-state fact for `M_2(C)`

The Quantum axiom is the one-site C*-algebra `A_x = M_2(C)`. A C*-algebra always
has **states** `omega` (positive, normalized, **linear** functionals). The
finite-dimensional structure theorem forces

```text
omega(A) = Tr(rho A)
```

for a unique density matrix `rho` (positive, `Tr rho = 1`). For a projector `P`,
`omega(P) = Tr(rho P) in [0,1]`, **additive** over orthogonal projectors by
linearity, and for a **pure** state `rho = |psi><psi|` with
`|psi> = sum_k a_k |k>`:

```text
omega(P_k) = <psi|P_k|psi> = |a_k|^2.       (exact; sympy-verified, Task 1b)
```

So "a consistent additive `[0,1]` state-functional with `omega(P_k) = |a_k|^2` for
pure states **exists**" is a **theorem of the algebra**, i.e. inside Quantum — *as
a property of the states of `M_2(C)`*. The runner verifies the form, positivity,
normalization, orthogonal-additivity, and the exact pure-state value.

### `A3` decomposes into two claims

| Sub-claim of `A3` | In {Quantum, Record}? |
|---|---|
| (a) a consistent additive `[0,1]` state-functional **exists**, with pure value `|a_k|^2` | **YES** — Quantum (C*-state) / Record (additivity); see Task 2 |
| (b) the **operational identification** `omega` = empirical relative frequency | **NO** — the genuine residual |

The C*-algebra never says the number `Tr(rho P)` is a *frequency*. Sub-claim (b)
is the irreducible physics; it is the only part of `A3` that is genuinely
residual.

---

## 2. Record discharges the Gleason additivity input

Gleason's frame function `f` satisfies `sum_i f(e_i) = 1` on **every** orthonormal
basis — non-contextual additivity over orthogonal projectors. The
[`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
and
[`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md)
chain treats this additivity (their "(M3)") as an **input** — "standard
probability axiom, universal background." That chain **predates** the Record
axiom ([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)).

The Record axiom says the scalar readout `I` is **finitely additive over
pairwise-disjoint records** with `I(empty) = 0`. Disjoint realized outcomes are
orthogonal projectors (commuting, summing to `<= I`). Therefore:

> **Record additivity == Gleason/Busch non-contextual frame-function additivity.**

This **discharges** the 2026-05-20 chain's "additivity is an input" residual: the
additivity is no longer an imported universal-background axiom but the content of
the Record axiom.

### {Quantum + Record} -> Busch (dim 2) -> `Tr(rho .)` -> `|a_k|^2`

- **dim >= 3** (multi-site, `dim = 2^|Lambda| >= 4`): Gleason applies.
- **dim 2** (single qubit): Busch's POVM extension applies. The runner verifies
  the heart of the dim-2 step on the qubit effect algebra: a `[0,1]` functional
  additive over POVM resolutions of the identity is affine on the Pauli
  parameterization, so the density matrix is **uniquely recovered** from the
  additive effect-values (`Tr(rho .)` is the unique such functional), and on a
  pure state it returns `|a_k|^2` (`f(P0) = 2/3`, `f(P1) = 1/3` for
  `|psi> = sqrt(2/3)|0> + sqrt(1/3)|1>`).

Crucially, Gleason/Busch is doing real work: it **upgrades** the *weaker* premise
"additive over orthogonal/POVM decompositions" (what Record supplies) to the
*stronger* conclusion "globally linear, i.e. `Tr(rho .)`." So the Born **form**
does not require separately assuming the functional is a C*-state; Record's
additivity earns it.

### The normalization gap (honest)

Record's additivity is a map into `(R, +)` with `I(empty) = 0`. Gleason/Busch need
a frame function valued in `[0,1]` with `sum_i f(e_i) = 1`. The extra content is:

- **`[0,1]` bound** — positivity of a count (plausibly Record-flavored, but
  Record-as-written asserts only additivity and `I(empty) = 0`);
- **sum-to-1** — "a complete measurement records exactly one outcome," a
  unit/normalization convention.

The runner exhibits the gap: `I(P) = 5 * Tr(rho P)` is additive with `I(empty)=0`
but `I(total) = 5 != 1`. So **normalization is a small separate input** — far
weaker than `A3`, but not literally inside Record's "(R,+) additive, `I(empty)=0`"
wording. Recorded here as a normalization gap.

---

## 3. The genuine residual: operational identification via record-frequency

On `N` copies of the prepared state, the **frequency operator** is

```text
f_hat_P = (1/N) sum_{i=1}^N P^(i).
```

The quantum law of large numbers (Finkelstein 1965; Hartle 1968; Farhi–Goldstone–
Gutmann 1989) says `psi^{otimes N}` approaches an eigenstate of `f_hat_P` with
eigenvalue `Tr(rho P)` as `N -> oo`. The runner tests this on `N = 1..8` (exact):

- **Mean** `<f_hat_P> = Tr(rho P)` for **every** `N` (verified `N=1..8`).
  This is **non-circular** — it is just linearity of the expectation — but it
  merely **re-expresses** the algebraic-state number; it proves nothing new.
- **Variance** `= (p - p^2)/N -> 0` (closed form verified `N=1..8`).

### The circularity verdict: CIRCULAR for the value, conditional on typicality

The step "variance `-> 0` => the recorded frequency **is** `Tr(rho P) = |a_k|^2`"
uses `<psi^N| (f_hat_P - <f>)^2 |psi^N>`. **That expectation is the Born inner
product weighting the deviation subspace.** The runner makes this literal
(Task 3c): decomposing `psi^{otimes N}` in the `f_hat_P` eigenbasis, the weight on
frequency `k/N` is

```text
C(N,k) (|a_0|^2)^k (|a_1|^2)^(N-k)  =  binomial with success prob = |a_0|^2.
```

The measure used to declare deviations "small" **is** the Born measure with the
very success probability `p = |a_0|^2` being derived. Replacing it with the
**uniform counting measure** over the `2^N` strings would concentrate the
frequency at `1/2`, **not** `|a_0|^2` (runner: counting-measure frequency mean
`= 0.5 != 2/3`). So the convergence to `|a_k|^2` is delivered by the Born norm,
not by bare counting.

The **record count** itself (an integer tally across `N` separate trials) is
non-circular and supplies the operational *frequency object*. But the claim that
this frequency *converges to* `|a_k|^2` (the typicality / measure-1 statement)
re-imports the Born measure. This is exactly Hartle's known critique (and Squires
1990; Caves–Schack 2005): the frequency-operator argument cannot derive the
measure it presupposes.

Finite-`N` honesty (Task 3d): at `N = 8`, `P(|freq - p_born| > 1/N) = 0.4537`.
Finite records do **not** pin `|a_k|^2`; only the `N -> oo` measure-1 statement
does, and that *is* the typicality assumption. **Record supplies the count, not
the limit measure.**

---

## 4. No-go intact and distinct from the frequency route

The narrow additivity no-go
([`OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md`](OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md))
bars only deriving the **branch** measure from the continuous homomorphism
`(R_+, x) -> (R, +)` (the map `c log p`, additive over independent branches
`p_AB = p_A p_B`). The frequency route uses **neither**:

- It tallies **integer occurrences** across `N` **separate** trials and forms
  `frequency = count/N`. That is additivity over **disjoint trials** (the Record
  axiom over disjoint records of separate copies), an existence/identification
  claim — **not** a map from a single branch's probability `p` to a scalar via a
  logarithm.
- It is also distinct from the no-go's **free-monoid caveat**, which concerns
  encoding **one** branch's probability `p` into a **word length** (`-log_b p`, or
  a different integer observable; the runner confirms `2^n = 3` has no integer
  solution). The frequency count is a different object: a tally of *which*
  outcome occurred, not a coding of a single branch's `p`.

So the no-go stands intact and is distinct from the frequency route. **(y)**

---

## 5. Honest verdict and reconciliation with #2702

### Circularity / typicality ledger

| Claim | In {Quantum, Record}? | Circular? |
|---|---|---|
| Existence of a `[0,1]` state-functional `omega` | YES (Quantum: C*-state) | no |
| `omega` has the `Tr(rho .)` **form** | YES (Quantum + Record; Gleason/Busch upgrades frame-additivity) | no |
| `omega(P_k) = |a_k|^2` for pure states (the **value**) | YES (follows from the form) | no |
| Non-contextual additivity (Gleason "(M3)" input) | YES (Record) | no |
| `[0,1]` bound + sum-to-1 **normalization** | PARTIAL (normalization gap) | no |
| **Mean** recorded frequency `= Tr(rho P)` | YES (linearity) | no (but only restates `omega`) |
| Recorded frequency **converges** to `|a_k|^2` (typicality) | **NO** | **YES** (Born norm) |
| Operational identification `omega` = empirical frequency | **NO (the residual)** | n/a |

### Verdict

**Unconditional from {Quantum + Record}:**

- the Born **form** `omega = Tr(rho .)` (Record discharges the Gleason additivity
  input; Gleason/Busch supplies the upgrade), modulo a small **normalization**
  input;
- the Born **value** `|a_k|^2` for pure states **as the algebraic-state number**;
- the **mean** recorded frequency equals that number (but this is a restatement,
  not new content).

**Still residual (not unconditional):**

- the **operational identification** that this number is the **empirical relative
  frequency**. The frequency-operator route discharges it only **conditional on
  typicality**, which it smuggles via the Born norm (circular for the value).

### Reconciliation with #2702's `A3`

`A3` does **not vanish**, but it **shrinks**: from "a state-functional
probability *exists*" (a bundle) down to **just the operational identification**
(equivalently, the **typicality** assumption that makes recorded frequency
converge to `omega`). The existence/form/value parts of `A3` are absorbed into
{Quantum, Record} by Tasks 1–2. The residual is one named premise: **typicality /
the frequency identification**, which the frequency route cannot supply
non-circularly.

This is consistent with #2702 (which correctly called the *whole package*
conditional) and with the broader smuggle ledger (typicality / measure selection
is a universal-floor admission, not a framework-specific one).

---

## What this note establishes / does not establish

**Establishes.**

- The C*-algebraic-state fact for `M_2(C)`: states exist, have the `Tr(rho .)`
  form, are orthogonal-additive, and give `|a_k|^2` on pure states (exact).
- Record additivity **is** Gleason/Busch non-contextual additivity, discharging
  the 2026-05-20 chain's "additivity is an input" residual.
- The frequency-operator mean is non-circular (`= Tr(rho P)`), but the
  convergence to `|a_k|^2` is **circular** (re-imports the Born norm).
- The frequency route sits **outside** the additivity no-go and is distinct from
  its free-monoid caveat.

**Does not establish.**

- An **unconditional** Born `= |amplitude|^2` *as an empirical frequency* from
  {Quantum, Record} alone. The operational identification is conditional on
  typicality.
- That the normalization (`[0,1]` + sum-to-1) is literally inside Record's bare
  additivity wording — it is recorded as a small separate input.
- Any enlargement of the Record axiom; any numerical-prediction change; any audit
  verdict (owned by the independent lane).

## Forbidden-imports check

- No PDG values, literature numerical comparators, or fitted selectors consumed.
- Gleason 1957 and Busch 2003 are cited as named standard mathematical-physics
  content; the framework-scoped applications already exist in the cited 2026-05-20
  narrow-theorem notes and are not re-proved here. The frequency-operator law of
  large numbers (Finkelstein 1965; Hartle 1968; Farhi–Goldstone–Gutmann 1989) and
  its circularity critique (Squires 1990; Caves–Schack 2005) are cited as named
  context, not as derivation inputs; the runner reproves the mean/variance/weight
  facts from the framework's qubit primitives.

## Validation

The runner `scripts/frontier_born_quantum_record_unconditional_2026_06_05.py`
checks (PASS=29, FAIL=0):

- the algebraic-state form, positivity, normalization, orthogonal-additivity, and
  the exact pure-state value `omega(P_k) = |a_k|^2` (sympy);
- frame-function additivity on every qubit orthonormal basis; the dim-2 Busch
  uniqueness (density matrix recovered from additive effect-values);
- `{Quantum + Record} -> Tr(rho .) -> |a_k|^2` on a pure qubit;
- the normalization gap (an additive scalar need not normalize);
- the frequency-operator mean (`= Tr(rho P)`, `N=1..8`) and variance
  (`(p-p^2)/N`, `N=1..8`);
- the explicit identification of the deviation weight with the binomial Born
  measure at `p = |a_0|^2`, and the contrast that the uniform counting measure
  gives `1/2`;
- finite-`N` non-pinning (`P(|freq - p_born| > 1/N) = 0.4537` at `N=8`);
- the no-go's barred homomorphism `c log p`, the trial-count additivity, the
  free-monoid caveat (`2^n = 3` unsolvable), and the distinctness of the
  frequency route from both.
