# N5 (Single Time-Generator) Is Not Derivable From Clock-Exchange-Invariant Structures

**Date:** 2026-06-17
**Type:** narrow_no_go (clock-exchange-invariance obstruction to deriving N5)
**Claim type:** no_go

**Claim scope (narrow, scoped — not an absolute impossibility):** On the
finite two-clock witness `H = C^2 tensor C^2`, the two independent
commuting clocks `G₁ = σ_z⊗I`, `G₂ = I⊗σ_z` are exchanged by a unitary
`S` (site swap) that preserves the Lattice placement and Quantum one-site
algebras. **Every structure invariant under `S`
assigns `G₁` and `G₂` equal status, so it cannot exclude one independent clock; and every
structure built from the Lattice, Quantum, and Record baseline without an extra
`S`-breaking readout context and respecting the kinematic exchange is
`S`-invariant. Therefore N5 (single generator / `d_t ≤ 1`) is NOT derivable from
clock-exchange-invariant structures on the current surface — it requires a clock-exchange-
symmetry-BREAKING ingredient.** This note proposes **no** status change, edits no other note,
and makes **no** absolute-impossibility claim (it is scoped to `S`-invariant structures, the
analogue of the framework's `W`-transportable axis-label no-gos). **Status authority:
independent audit lane only.**

## 1. Context

`d_t = 1` factors as `[d_t ∈ {odd}]` (framework-internal lower bound) ∩ `[d_t ≤ 1]`
(declared premise B-AXIS.3 / N5: "no independent commuting transfer factor as a second
clock"). The finite witness used here shows that a two-clock commuting algebra is
kinematically realizable, so N5 is non-vacuous. The standing single-clock no-gos
(record-durability 2026-06-11; KMS/APBC 2026-06-16; the S₄ axis-datum note 2026-06-17) each
addressed only the **axis-LABEL** clause (N4) and explicitly left **N5 untouched**. This note
targets N5 directly.

## 2. The clock-exchange symmetry (runner `[CLOCK-EXCHANGE SYMMETRY S]`)

For the two realizable clocks `G₁ = σ_z⊗I`, `G₂ = I⊗σ_z`, the swap `S` (exchange of the two
equivalent qubit sites, preserving the lattice placement and one-site algebra) satisfies
(computed, residual 0):

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

**Why baseline selectors do not break `S`.** The Record axiom supplies durable realized-outcome
registration and finite additivity over supplied disjoint records; it does not supply a
site-preferred readout context. The Lattice and Quantum axioms supply the site set and the
one-site algebra, and the two clock sites are exchanged by `S`. Therefore any selector built
from the Lattice, Quantum, and Record baseline that honors this kinematic exchange is
`S`-invariant, hence (by the Lemma) cannot exclude an independent clock. A selector that reads
one named site is a further `S`-breaking readout input, not a consequence of the baseline.

## 4. The sum-clock loophole is closed (runner `[NO-REDUCTION]`)

Keeping only the `S`-fixed sum-clock `H_sum = G₁+G₂` does **not** reduce the count: the
off-diagonal evolution `exp(−iG₁)` is **not** on the sum-clock orbit `exp(−ir(G₁+G₂))`
(min gap `1.356 > 0.05`). So `G₁` remains an **independent physical evolution** not generated
by `H_sum`; genuine `d_t = 1` requires **excluding** `G₁` as a physical generator. Since
`G₁` and `G₂` are `S`-conjugate, excluding `G₁`-but-not-`G₂` **breaks `S`**.

## 5. Result and the ingredient any future forcing must add

**N5 (single generator / `d_t ≤ 1`) is not derivable from clock-exchange-invariant structures
on the current surface.** Reducing the time-generator count requires a clock-exchange-symmetry-
**breaking** input — equivalently, a separate preferred-clock or registration-direction
ingredient that singles out one generator of the commuting clock-algebra without presupposing
it. No structure built from the Lattice, Quantum, and Record baseline while respecting `S`
supplies this. This upgrades the prior status of N5 from "no note attempts it /
undeclared-derivable" to **"provably not derivable from
clock-exchange-invariant structures."**

This is **distinct** from the arrow admission (which breaks time-**reversal** to fix a
direction of *one* time); N5 concerns the **number** of commuting time-generators
(dimensionality). The two are independent symmetry-breakings.

**Scope honesty:** like the framework's `W`-transportable axis-label no-gos, this is a no-go
*relative to a symmetry class* (`S`-invariant structures on the realizable two-clock witness),
not an absolute impossibility theorem. It names precisely the symmetry a forcing must break.

## 6. No-Go Discipline Gate

This gate is source-side scope control, not an audit verdict.

**N1 -- Alternative routes.** Five attacks were checked. (1) Use an `S`-invariant scalar
readout to distinguish the clocks: the lemma forces equal values on `G₁` and `G₂`. (2) Use
spectral or trace-like symmetric readouts: the runner checks representative cases and they
again assign equal status. (3) Keep only the sum-clock `G₁+G₂`: the runner checks that
`exp(-iG₁)` is not on the sum-clock orbit. (4) Read one named site: this distinguishes the
clocks, but the runner also checks that it breaks `S`, so it is an extra input. (5) Import a
preferred-clock or registration-direction rule: that is exactly the live escape route and is
outside the clock-exchange-invariant class.

**N2 -- Wall independence.** There is one collapsed wall: an `S`-breaking readout or
preferred-clock ingredient is needed to reduce the two-clock witness to one physical
generator. No independent wall count is asserted.

**N3 -- Hidden-wall scan.** The earlier tempting standalone-axiom and
selector-derivation wording is narrowed here. The load-bearing premise is only that the
finite witness and any baseline-respecting selector preserve the swap `S`; Record supplies no
site-preferred readout context.

**N4 -- Residual matching.** This residual is N5, exclusion of an independent second commuting
time-generator. It is distinct from N4 axis-label transport and from the odd-`d_t` chirality
lower bound; those surfaces are context, not witnesses for this no-go.

**N5 -- Rhetoric audit.** "Not derivable" means not derivable from the `S`-invariant symmetry
class on this finite two-clock witness. It does not mean `d_t=1` is impossible, that dynamics
cannot later select one clock, or that every future non-symmetric readout route is closed.

**N6 -- Partial-closure path scan.** The legitimate closure path is explicit: add or derive a
framework-native `S`-breaking preferred-clock/readout ingredient. Approved primitives and the
three axioms do not supply that ingredient by themselves, and this note does not propose a new
axiom or primitive.

**N7 -- Steelman.** A future dynamics, environment, boundary condition, or record-production
mechanism could make one clock stable and the other nonphysical. That would be a real route
against global N5 obstruction, but it would add the `S`-breaking ingredient this note says is
missing; it does not defeat the narrow `S`-invariant no-go.

**N8 -- Cross-cycle echo.** The closest precedent is the family of `W`-transportable
axis-label no-gos: symmetry transport prevents label selection until a symmetry-breaking
labeling or readout input is supplied. This note copies that scope discipline for N5 rather
than claiming an absolute single-clock impossibility.

**Runner:** [`scripts/n5_single_generator_clock_exchange_no_go_2026_06_17.py`](../scripts/n5_single_generator_clock_exchange_no_go_2026_06_17.py)
(`TOTAL: PASS=9 FAIL=0`, deterministic, no RNG, < 1s). No fitted parameters, no observed
values, no new axioms, no axiom-file edits, no `docs/audit/data/*` edits. Sets no audit status.
