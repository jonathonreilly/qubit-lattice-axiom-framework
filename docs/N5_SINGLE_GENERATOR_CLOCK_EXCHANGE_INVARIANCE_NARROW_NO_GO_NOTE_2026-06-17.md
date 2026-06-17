# N5 (Single Time-Generator) Is Not Derivable From Clock-Exchange-Invariant Structures

**Date:** 2026-06-17
**Type:** narrow_no_go (clock-exchange-invariance obstruction to deriving N5)
**Claim type:** no_go

**Claim scope (narrow, scoped — not an absolute impossibility):** On the
kinematically-realizable two-clock structure (the `d_t=2` witness of
[`ONE_TIME_DIMENSION_DT1_REDUCES_TO_EMERGENT_DYNAMICS_GATE…`](ONE_TIME_DIMENSION_DT1_REDUCES_TO_EMERGENT_DYNAMICS_GATE_NARROW_NO_GO_NOTE_2026-06-17.md)),
the two independent commuting clocks `G₁ = σ_z⊗I`, `G₂ = I⊗σ_z` are exchanged by a unitary
`S` (site-swap) that is a **Locality symmetry**. **Every structure invariant under `S`
assigns `G₁` and `G₂` equal status, so it cannot exclude one independent clock; and every
structure derivable from {Quantum, Locality, Record} that respects the kinematic exchange is
`S`-invariant. Therefore N5 (single generator / `d_t ≤ 1`) is NOT derivable from
clock-exchange-invariant structures on the current surface — it requires a clock-exchange-
symmetry-BREAKING ingredient.** This note proposes **no** status change, edits no other note,
and makes **no** absolute-impossibility claim (it is scoped to `S`-invariant structures, the
analogue of the framework's `W`-transportable axis-label no-gos). **Status authority:
independent audit lane only.**

## 1. Context

`d_t = 1` factors as `[d_t ∈ {odd}]` (framework-internal lower bound) ∩ `[d_t ≤ 1]`
(declared premise B-AXIS.3 / N5: "no independent commuting transfer factor as a second
clock"). The companion note proves the lower bound is internal-conditional and that
**multi-time is kinematically realizable** on `H = ⊗_{x} C²` (so N5 is non-vacuous), reducing
`d_t = 1` to the emergent-dynamics gate. The standing single-clock no-gos
(record-durability 2026-06-11; KMS/APBC 2026-06-16; the S₄ axis-datum note 2026-06-17) each
addressed only the **axis-LABEL** clause (N4) and explicitly left **N5 untouched**. This note
targets N5 directly.

## 2. The clock-exchange symmetry (runner `[CLOCK-EXCHANGE SYMMETRY S]`)

For the two realizable clocks `G₁ = σ_z⊗I`, `G₂ = I⊗σ_z`, the swap `S` (exchange of the two
equivalent qubit sites — a **Locality** symmetry) satisfies (computed, residual 0):

- `S` unitary, `S² = I`;
- `S G₁ S† = G₂`, `S G₂ S† = G₁` — `S` **exchanges the two independent clocks**;
- `S (G₁+G₂) S† = G₁+G₂` (symmetric direction fixed), `S (G₁−G₂) S† = −(G₁−G₂)` (antisymmetric
  direction flipped) — confirming a genuine exchange.

## 3. The obstruction (runner `[RECORD-INVARIANT SELECTORS]`)

**Lemma.** Any `S`-invariant linear functional `Φ` (`Φ(S X S†) = Φ(X)`) satisfies
`Φ(G₂) = Φ(S G₁ S†) = Φ(G₁)`. So an `S`-invariant selector assigns `G₁` and `G₂` **equal
status** and cannot pick one as "the physical clock."

Computed witnesses: `Tr(X)`, `Tr(X²)`, `Tr(X·(G₁+G₂))` (all `S`-invariant, Record-style:
additive / spectral / symmetric) give `Φ(G₁) = Φ(G₂)`. By contrast an `S`-**breaking**
functional `Tr(X·P_A)` (read site A only) gives `Φ(G₁) ≠ Φ(G₂)` and `[P_A, S] ≠ 0` — i.e.
**selecting a single clock requires an `S`-breaking observable.**

**Why Record-derivable selectors are `S`-invariant.** The Record axiom is a finitely-additive
scalar readout over **unordered** finite pairwise-disjoint collections of records — permutation/
exchange-symmetric by construction; and the two clock-sites are exchanged by `S`, a Locality
site-exchange that both qubit factors (Quantum) and the lattice (Locality) respect. So every
selector derivable from {Quantum, Locality, Record} that honors the kinematic exchange is
`S`-invariant, hence (by the Lemma) cannot exclude an independent clock.

## 4. The sum-clock loophole is closed (runner `[NO-REDUCTION]`)

Keeping only the `S`-fixed sum-clock `H_sum = G₁+G₂` does **not** reduce the count: the
off-diagonal evolution `exp(−iG₁)` is **not** on the sum-clock orbit `exp(−ir(G₁+G₂))`
(min gap `1.356 > 0.05`). So `G₁` remains an **independent physical evolution** not generated
by `H_sum`; genuine `d_t = 1` requires **excluding** `G₁` as a physical generator. Since
`G₁` and `G₂` are `S`-conjugate, excluding `G₁`-but-not-`G₂` **breaks `S`**.

## 5. Result and the ingredient any future forcing must add

**N5 (single generator / `d_t ≤ 1`) is not derivable from clock-exchange-invariant structures
on the current surface.** Reducing the time-generator count requires a clock-exchange-symmetry-
**breaking** input — equivalently, a **preferred-clock / registration-direction** ingredient
that singles out one generator of the commuting clock-algebra without presupposing it. No
structure built from {Quantum, Locality, Record} (all `S`-invariant) supplies this; so any
future derivation of `d_t = 1` must **add** such an ingredient. This upgrades the prior status
of N5 from "no note attempts it / undeclared-derivable" to **"provably not derivable from
clock-exchange-invariant structures."**

This is **distinct** from the arrow admission (which breaks time-**reversal** to fix a
direction of *one* time); N5 concerns the **number** of commuting time-generators
(dimensionality). The two are independent symmetry-breakings.

**Scope honesty:** like the framework's `W`-transportable axis-label no-gos, this is a no-go
*relative to a symmetry class* (`S`-invariant structures on the realizable two-clock witness),
not an absolute impossibility theorem. It names precisely the symmetry a forcing must break.

**Runner:** [`scripts/n5_single_generator_clock_exchange_no_go_2026_06_17.py`](../scripts/n5_single_generator_clock_exchange_no_go_2026_06_17.py)
(`TOTAL: PASS=9 FAIL=0`, deterministic, no RNG, < 1s). No fitted parameters, no observed
values, no new axioms, no axiom-file edits, no `docs/audit/data/*` edits. Sets no audit status.
