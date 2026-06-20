# Koide MRU Formal Demotion Note

**Date:** 2026-04-20
**Lane:** Charged-lepton Koide / kappa = 2
**Status:** support - structural/meta repair note. This note demotes
the `SO(2)`-quotient MRU closure route to supplementary /
alternative-framing support and keeps the spectrum-operator bridge as
the only graph-visible retained authority for the operator-side
bridge corollary
`spectrum-side Q = 2/3 => operator-side kappa = 2`.
It does not claim an independent block-total closure route.
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome.
**Primary runner:**
`scripts/frontier_koide_mru_demotion_bridge_corollary_2026_06_18.py`
**Graph-visible retained authority:**
`docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`
(runner PASS=9, symbolic zero residual).
**Bounded context, not a closure route here:**
`docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`
(runner PASS=16, retained-bounded algebraic support with the canonical
scalar-measure bridge still open).
**Demoted route:**
`docs/KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md` +
`docs/KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`.

---

## Graph-visible source authority (one hop)

This note's load-bearing one-hop citation registered to the audit-graph
builder:

- [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
  — retained spectrum-operator bridge identity that carries operator-side
  `kappa = 2` as a corollary of spectrum-side `Q = 2/3` with symbolic zero
  residue. This is the retained authority used by the present demotion note.

Non-load-bearing context pointers, intentionally left as backticked plain
text rather than graph-visible dependency edges:

- `KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`
  is bounded algebraic support for the block-total Frobenius branch. Its
  own source boundary leaves the canonical physical scalar-measure bridge
  open, so this demotion note does not use it as an independent retained
  closure route.
- `KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md` is the
  demoted MRU theorem note.
- `KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`
  — the companion MRU obstruction note co-demoted by this reclassification.

## 2026-06-18 source-boundary repair

This repair also corrects the cubic trace diagnostic below. For
`H = a I + b C + bbar C^2`,

```text
tr(H^3) = 3 a^3 + 18 a |b|^2 + 3 (b^3 + bbar^3).
```

Thus the non-`SO(2)`-invariant phase term is proportional to
`b^3 + bbar^3 = 2 |b|^3 cos(3 arg b)`, not to
`a (b^3 + bbar^3)`.

No new axiom, Tier-A admission, audit verdict, or physical scalar-measure
bridge is introduced here.

The clean claim is bounded demotion / bridge-corollary support. The primary
exact bridge-corollary route is the graph-visible spectrum-operator bridge.
The block-total Frobenius result remains independent bounded support in its
own source note, but it is not a standalone full physical scalar-measure
closure theorem here.

## 2026-06-20 scope-boundary repair

The Path A failure below is deliberately route-local. It shows that the
displayed spectral-observable route from the retained observable principle
does not derive the scalar-lane `SO(2)` quotient. It does not claim to exhaust
every alternative attack route against that quotient; other routes remain
open, not closed. No derived value, audit verdict, ledger status, publication
status, or repo-wide authority surface is changed by this source repair.

---

## 0. Why this note exists

A strict-reviewer audit of the scalar-selector cycle 1 stack found one
structural open import behind the MRU closure route for Koide kappa:

> The MRU + weight-class obstruction route relies on a postulate that
> "the scalar charged-lepton lane does not retain the Cartesian basis of
> the real doublet; it retains only the Frobenius radius
> `rho_perp^2 = E_perp`". This is an internal `SO(2)`-quotient of the
> doublet frame. The two MRU notes renamed the postulate as a
> derivation, but the underlying SO(2)-invariance check in the runner
> verifies only the trivial rotation identity
>
>     r_1'^2 + r_2'^2 = r_1^2 + r_2^2 under R(theta),
>
> not the physical claim that the lane observables **factor through**
> that radius.

That is a correct audit finding. This note accepts it, attempts the displayed
framework derivation (Path A), documents why that route does not close, and
formally repositions the stack so the operator-side `kappa = 2` statement is
carried only as the spectrum-operator bridge corollary of spectrum-side
`Q = 2/3`. The block-total Frobenius branch remains bounded algebraic context
until a retained canonical scalar-measure bridge exists.

---

## 1. Path A attempt: can the SO(2)-quotient be derived from the retained observable principle?

### 1.1 The candidate route

Path A would attempt to derive the SO(2)-quotient from the retained
observable principle:

- `docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` — scalar bosonic
  observables are source derivatives of `W[J] = log|det(D + J)|`.
- `docs/THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md` — on the retained
  `hw=1` triplet, the retained operator algebra is all of `M_3(C)`.
- `docs/CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md` — on
  the sqrt-mass vector Fourier decomposition, Koide `Q = 2/3` is
  equivalent to `a_0^2 = 2 |z|^2`.
- `docs/KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md` —
  `C_3[111]`-invariant Hermitian operators are circulants
  `H = a I + b C + bbar C^2`.

The naive Path A argument would go:

1. Scalar observables are determined by the spectrum (log|det| and its
   derivatives are symmetric functions of the eigenvalues).
2. Under the internal SO(2) frame rotation of the doublet
   `span_R{B_1, B_2} = span_R{C + C^2, i(C - C^2)}`, the parameter `b`
   transforms as `b -> e^{i theta} b`.
3. If this were a unitary conjugation, the spectrum would be invariant,
   and therefore all scalar observables would factor through the
   rotation-invariant data `(a, |b|)`.

### 1.2 Why Path A fails

Step 3 is false. Under `b -> e^{i theta} b`, the eigenvalues of
`H = a I + b C + bbar C^2` transform as

```text
lambda_k(theta) = a + 2 |b| cos(arg(b) + theta + 2 pi k / 3),   k = 0, 1, 2.
```

For a generic continuous `theta`, this is **not** a permutation of the
eigenvalue multi-set `{lambda_0, lambda_1, lambda_2}`. The multiset is
invariant only under the discrete subgroup `theta in {0, 2 pi / 3,
4 pi / 3}` (which cycles the index `k`). So the SO(2) continuous
rotation is not a spectral symmetry, hence not a unitary conjugation of
`H`, and spectral scalar observables are **not** SO(2)-invariant in
general.

Explicit check:

- `tr(H^2) = 3 a^2 + 6 |b|^2` is SO(2)-invariant (depends only on `|b|^2`).
- `tr(H^3) = 3 a^3 + 18 a |b|^2 + 3 (b^3 + bbar^3)`, so its phase term
  `3 (b^3 + bbar^3) = 6 |b|^3 cos(3 arg b)` is **not** invariant under
  `b -> e^{i theta} b` for generic `theta`.
- `det(H) = a^3 + b^3 + bbar^3 - 3 a |b|^2` carries the same
  `cos(3 arg b)` dependence, so `log|det|` is **not** SO(2)-invariant.

Therefore the retained observable principle does **not** force the
SO(2)-quotient on its own. The generic scalar observable on
`Herm_circ(3)` depends on both `|b|` and `arg(b)` (through
`cos(3 arg b)`). The SO(2)-quotient is a genuinely additional
postulate, strictly stronger than "scalar observables are
spectrum-native".

### 1.3 What a broken Path A would look like

A putative Path A derivation could still try to restrict attention to
scalar observables that happen to be `arg(b)`-independent (such as
`tr(H^2)`, `|b|^2`, `E_perp`). But that selection is a non-trivial
choice — it is exactly the same SO(2) postulate written in a different
coordinate system ("use only `arg(b)`-independent invariants"). That is
the circular restatement the reviewer audit flagged.

**Verdict.** Path A cannot close at the Nature bar: the `SO(2)` quotient is
not a corollary of the retained observable principle along the displayed
spectral-observable route. This note checks Path A only; it does not survey or
exhaust every alternative attack route against the quotient. Other attack
routes, such as a future result that decouples the `cos(3 arg b)` channel,
remain open, not closed.

---

## 2. Path B: formal demotion of MRU, bridge-corollary replacement

Path B observes that the MRU route is **not needed** for the
operator-side bridge corollary. The retained spectrum-operator bridge
shows that, on `Herm_circ(3)`, the operator-side equation
`a^2 = 2 |b|^2` is exactly the spectrum-side equation
`a_0^2 = 2 |z|^2` written in cyclic-compression coordinates. This
does not derive spectrum-side `Q = 2/3`; it transfers that condition to
operator-side `kappa = 2` with zero symbolic residue.

### 2.1 Primary route — spectrum-operator bridge

Source: `docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`.

Content. On `Herm_circ(3)`, the cyclic-compression Fourier dictionary
delivers the **exact** polynomial identity

```text
a_0^2 - 2 |z|^2  =  3 (a^2 - 2 |b|^2)
```

where `(a_0, z)` are the Fourier scalars of the sqrt-mass eigenvalue
triple under the retained P1 identification `lambda_k = sqrt(m_k)`, and
`(a, b)` are the circulant parameters. The identity is symbolic with
zero residual. Consequently

```text
[spectrum-side]  a_0^2 = 2 |z|^2   (Koide Q = 2/3)
           <=>  [operator-side] a^2 = 2 |b|^2   (kappa = 2),
```

with **zero residue**, for any `Herm_circ(3)`. The operator-side
`kappa = 2` is a direct corollary of the spectrum-side Koide condition;
no SO(2)-quotient is used, because the identity is a genuine Fourier
bijection on `Herm_circ(3)` rather than an extremal-law argument on a
reduced carrier.

Runner: `scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py`,
`PASS = 9, FAIL = 0`.

### 2.2 Bounded context — block-total Frobenius measure is not a second closure route here

Source: `docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`.

Content. The block-total Frobenius-squared functional

```text
E_I(H) := || pi_I(H) ||_F^2
```

assigns one scalar slot per real isotype. At `d = 3` it gives the
`(1, 1)` multiplicity count from Frobenius reciprocity (one trivial
real isotype + one real doublet, each with multiplicity one), and the
equal-weight log-law

```text
S_MRU(H) = log E_+ + log E_perp
```

has its equal-weight extremum at `E_+ = E_perp`, equivalently
`kappa = 2`. The `(1, 1)` weights come from real-isotype multiplicity,
not from a frame rotation of the doublet. `d = 3` is the unique
dimension for which the multiplicity pattern is exactly
`(1 trivial + 1 doublet)` (runner enumerates d = 2..6).

Runner: `scripts/frontier_koide_kappa_block_total_frobenius_measure_theorem.py`,
`PASS = 16, FAIL = 0`.

Boundary. This branch is not used by the present demotion note as an
independent retained closure route. Its own source note says the
canonical physical scalar-lane measure / `SO(2)`-quotient bridge is
still open. It is retained-bounded algebraic support for a possible
future scalar-measure theorem, not an unbounded closure of operator-side
`kappa = 2` by itself.

### 2.3 What this note carries

This note carries three restricted statements:

1. The MRU/SO(2)-quotient route is demoted because the quotient is not
   derived from retained observable-principle inputs.
2. The spectrum-operator bridge gives a retained algebraic corollary:
   if spectrum-side `Q = 2/3` holds, then operator-side `kappa = 2`
   holds on the cyclic-compression carrier.
3. The block-total Frobenius route remains bounded context and is not
   advertised as an independent retained closure route here.

---

## 3. Formal demotion statement

Effective from this note:

1. **MRU is no longer a primary closure route for operator-side
   kappa = 2.** The two MRU notes on the branch
   (`KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md` and
   `KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`) are
   reclassified as **supplementary / alternative-framing support**
   rather than load-bearing theorems.

2. **The MRU closure argument assumes a postulate that Path A does not
   derive.** Specifically, along the displayed spectral-observable route, the
   scalar-lane `SO(2)` quotient of the doublet frame is not a consequence of
   the retained observable principle (spectrum-native scalar observables are
   **not** `SO(2)`-invariant on `Herm_circ(3)` in general). This is the Path-A
   finding; it does not assert that no other attack route could derive the
   quotient.

3. **The spectrum-operator bridge theorem is the primary graph-visible
   retained authority** for the operator-side bridge corollary. It
   carries `spectrum-side Q = 2/3 => operator-side kappa = 2` with
   symbolic zero residual and no new operator-side axiom.

4. **The block-total Frobenius measure theorem is not an independent
   retained closure route in this note.** It produces the `(1, 1)`
   weight pattern from Frobenius reciprocity multiplicity, but its own
   boundary leaves the canonical scalar-lane measure bridge open.

5. **The MRU notes retain their role as alternative pedagogical
   framings.** They correctly capture the content that, *if one
   imposes* the SO(2)-quotient by hand, the block log-volume extremum
   gives `kappa = 2`. That remains a valid conditional statement and
   is useful exposition. It is not a retained closure path.

---

## 4. Scientific consequence for the scalar-selector cycle 1 stack

The strict-reviewer audit's structural open import (I6) is handled by
demotion rather than promotion: the postulate is **not** promoted to a
theorem, and the MRU route it sat under is demoted out of the closure
stack.

Operator-side `kappa = 2` is not supplied here by an independent
operator-side scalar-measure postulate. It is inherited from
spectrum-side `Q = 2/3` through the exact spectrum-operator bridge,
without any SO(2)-quotient postulate.

The remaining load-bearing input for the full charged-lepton Koide
closure is the **spectrum-side** `Q = 2/3` route itself. This note does
not audit, alter, or strengthen that spectrum-side route; it only says
the operator-side equation is the same condition transported through
the retained bridge.

---

## 5. Effect on cross-references

The following source notes currently reference the MRU route as if
it were a primary closure path and should be read with this demotion
in mind:

- `docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`
  is bounded algebraic support. Any wording that makes it sound like
  an unbounded independent closure route should be read through its own
  measure-choice boundary: the canonical physical scalar-lane measure
  bridge remains open.
- `docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`
  already states correctly (section 3) that the operator-side framing
  is a **corollary** of the spectrum-side closure via the bridge
  identity. No change of content is needed there; this note confirms
  the bridge's primary status.
- `docs/KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md` and
  `docs/KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`
  are downgraded to supplementary status but remain useful exposition
  of the conditional MRU argument. Their runners
  (`frontier_koide_moment_ratio_uniformity_theorem.py` and
  `frontier_koide_mru_weight_class_obstruction_theorem.py`) continue
  to verify what they actually verify (the reduced-carrier
  log-volume extremum **given** the SO(2)-quotient); they do not
  claim to derive that quotient.

---

## 6. What is not claimed here

1. This note does not claim that the SO(2)-quotient is **false**. It
   may still be physically correct — e.g. if a future retained result
   establishes that the charged-lepton scalar lane decouples the
   `cos(3 arg b)` channel. What is claimed is only that the displayed
   Path A route does not deliver it; alternative attack routes remain open.
2. This note does not invalidate the two MRU notes as technical
   documents. Their calculations remain correct within the conditional
   "assume SO(2)-quotient, then...". What changes is only their status
   in the closure stack.
3. This note does not change the spectrum-side Koide closure. Berry +
   Brannen remain the load-bearing spectrum-side input.

---

## 7. Reproduction

The source-side demotion checks are:

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_mru_demotion_bridge_corollary_2026_06_18.py
PYTHONPATH=scripts python3 scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py
```

Both must continue to PASS cleanly on this branch. The block-total and
MRU runners continue to verify their own internal bounded or
conditional statements, but they are no longer load-bearing for this
note's operator-side bridge corollary.

---

## 8. Summary

| Route | Status | Requires SO(2)-quotient? |
|---|---|---|
| Spectrum-operator bridge (PASS=9, zero symbolic residue) | **Graph-visible retained authority for the bridge corollary** | No |
| Block-total Frobenius measure (PASS=16) | **Bounded algebraic context; not a closure route here** | No for its bounded algebra, but yes for physical scalar-measure closure |
| MRU + weight-class obstruction | **Supplementary / alternative framing** | Yes (not derivable from retained theorems) |

The operator-side `kappa = 2` statement is carried here only as the
retained spectrum-operator bridge corollary of spectrum-side `Q = 2/3`.
The MRU route is kept as supplementary support but is not load-bearing.
