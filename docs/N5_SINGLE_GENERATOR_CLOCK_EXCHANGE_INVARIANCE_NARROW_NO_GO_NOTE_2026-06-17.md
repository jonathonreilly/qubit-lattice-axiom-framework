# Clock-Exchange Invariance Gives No Site-Preferred Clock Selector

**Date:** 2026-06-17
**Type:** narrow_no_go (clock-exchange site-preference obstruction)
**Claim type:** no_go

**Claim scope (narrow, scoped — not an absolute impossibility):** On the
finite two-clock witness `H = C^2 tensor C^2`, the two independent
commuting clocks `G₁ = σ_z⊗I`, `G₂ = I⊗σ_z` are exchanged by a unitary
`S` (site swap) that preserves the Lattice placement and Quantum one-site
algebras. **Every `S`-invariant linear selector assigns `G₁` and `G₂` equal
status, so it cannot prefer one named site-clock over the other. Selecting
`G₁` rather than its `S`-conjugate `G₂` requires an `S`-breaking readout or
preferred-site ingredient.** This is a site-preference obstruction only. It
does **not** prove all `S`-invariant one-clock reductions impossible, and it
does **not** close a diagonal or quotient-style reduction that removes the
antisymmetric clock sector by an additional theorem. This note proposes **no**
status change, edits no other note, and makes **no** absolute-impossibility
claim. **Status authority: independent audit lane only.**

## 1. Context

`d_t = 1` factors as `[d_t ∈ {odd}]` (framework-internal lower bound) ∩
`[d_t ≤ 1]` (declared premise B-AXIS.3 / N5: "no independent commuting
transfer factor as a second clock"). The finite witness used here shows that a
two-clock commuting algebra is kinematically realizable, so N5 is non-vacuous.
The standing single-clock no-gos (record-durability 2026-06-11; KMS/APBC
2026-06-16; the S₄ axis-datum note 2026-06-17) each addressed only the
**axis-LABEL** clause (N4) and explicitly left **N5 untouched**. This note
does not close N5. It isolates the part that the finite witness actually
proves: no `S`-invariant site/readout selector can prefer one exchanged clock.

## 2. The clock-exchange symmetry (runner `[CLOCK-EXCHANGE SYMMETRY S]`)

For the two realizable clocks `G₁ = σ_z⊗I`, `G₂ = I⊗σ_z`, the swap `S` (exchange of the two
equivalent qubit sites, preserving the lattice placement and one-site algebra) satisfies
(computed, residual 0):

- `S` unitary, `S² = I`;
- `S G₁ S† = G₂`, `S G₂ S† = G₁` — `S` **exchanges the two independent clocks**;
- `S (G₁+G₂) S† = G₁+G₂` (symmetric direction fixed), `S (G₁−G₂) S† = −(G₁−G₂)` (antisymmetric
  direction flipped) — confirming a genuine exchange.

## 3. The obstruction (runner `[S-INVARIANT SELECTORS]`)

**Lemma.** Any `S`-invariant linear functional `Φ` (`Φ(S X S†) = Φ(X)`)
satisfies `Φ(G₂) = Φ(S G₁ S†) = Φ(G₁)`. So an `S`-invariant selector assigns
`G₁` and `G₂` **equal status** and cannot prefer one named site-clock over the
other.

Computed witnesses: `Tr(X)`, `Tr(X²)`, `Tr(X·(G₁+G₂))` (all `S`-invariant, Record-style:
additive / spectral / symmetric) give `Φ(G₁) = Φ(G₂)`. By contrast an `S`-**breaking**
functional `Tr(X·P_A)` (read site A only) gives `Φ(G₁) ≠ Φ(G₂)` and
`[P_A, S] ≠ 0` — i.e. **site-preferred clock selection requires an
`S`-breaking observable.**

**Why baseline selectors do not break `S`.** The Record axiom supplies durable realized-outcome
registration and finite additivity over supplied disjoint records; it does not supply a
site-preferred readout context. The Lattice and Quantum axioms supply the site set and the
one-site algebra, and the two clock sites are exchanged by `S`. Therefore any selector built
from the Lattice, Quantum, and Record baseline that honors this kinematic exchange is
`S`-invariant, hence (by the Lemma) cannot prefer one site-clock. A selector
that reads one named site is a further `S`-breaking readout input, not a
consequence of the baseline.

## 4. Sum-clock boundary diagnostic (runner `[SUM-CLOCK BOUNDARY]`)

If `G₁` is still admitted as a physical evolution, then replacing it by the
`S`-fixed sum-clock `H_sum = G₁+G₂` does not reproduce that evolution:
`exp(−iG₁)` is not on the sum-clock orbit `exp(−ir(G₁+G₂))` (runner min gap
`1.356 > 0.05`). This is only a boundary diagnostic. It shows that
"keep both physical generators but model one with the sum clock" fails in this
finite witness.

The diagnostic does **not** rule out a separate `S`-invariant diagonal
projection, quotient, or physical-state-selection theorem that removes the
antisymmetric sector rather than selecting `G₁` over `G₂`. Such a theorem is
outside this row and remains the live N5 repair target.

## 5. Result and the ingredient any future forcing must add

**Clock-exchange-invariant site/readout selectors cannot prefer one exchanged
clock over the other.** A route that selects `G₁` rather than `G₂`, or a named
site-A clock rather than its exchanged site-B partner, must add an
`S`-breaking readout, preferred-site, boundary, environment, or
record-production ingredient. This is the retained candidate from this row.

The broader N5 claim is left open: a future framework-native diagonal quotient
or dynamical superselection theorem could reduce the effective clock count
without preferring one named site-clock. This note neither supplies nor rules
out that theorem.

This is **distinct** from the arrow admission (which breaks time-**reversal** to fix a
direction of *one* time); N5 concerns the **number** of commuting time-generators
(dimensionality). The two are independent symmetry-breakings.

**Scope honesty:** like the framework's `W`-transportable axis-label no-gos,
this is a no-go relative to a symmetry class and a selector type. It blocks
site-preferred clock selection by `S`-invariant linear selectors on the
realizable two-clock witness. It is not an absolute single-clock
impossibility theorem.

## 6. No-Go Discipline Gate

This gate is source-side scope control, not an audit verdict.

**N1 -- Alternative routes.** Five attacks were checked. (1) Use an
`S`-invariant scalar readout to distinguish the clocks: the lemma forces equal
values on `G₁` and `G₂`. (2) Use spectral or trace-like symmetric readouts:
the runner checks representative cases and they again assign equal status. (3)
Keep both physical generators but model one with the sum-clock `G₁+G₂`: the
runner checks that `exp(-iG₁)` is not on the sum-clock orbit. (4) Read one
named site: this distinguishes the clocks, but the runner also checks that it
breaks `S`, so it is an extra input. (5) Add a diagonal quotient,
superselection, or preferred-clock rule: this is the live escape route and is
outside this row.

**N2 -- Wall independence.** There is one collapsed wall: an `S`-breaking
readout or preferred-site ingredient is needed to prefer one named clock over
its exchanged partner. No independent wall count is asserted.

**N3 -- Hidden-wall scan.** The earlier tempting standalone-axiom and
selector-derivation wording is narrowed here. The load-bearing premise is only
that the finite witness and any baseline-respecting site/readout selector
preserve the swap `S`; Record supplies no site-preferred readout context.

**N4 -- Residual matching.** This row does not close N5, i.e. exclusion of an
independent second commuting time-generator. It is distinct from N4 axis-label
transport and from the odd-`d_t` chirality lower bound; those surfaces are
context, not witnesses for this no-go.

**N5 -- Rhetoric audit.** "Cannot prefer one clock" means cannot distinguish
or select one named site-clock by an `S`-invariant linear selector on this
finite two-clock witness. It does not mean `d_t=1` is impossible, that dynamics
cannot later select one clock, that an `S`-invariant diagonal quotient is
closed, or that every future non-symmetric readout route is closed.

**N6 -- Partial-closure path scan.** The legitimate closure paths are explicit:
derive a framework-native diagonal quotient/superselection theorem, or add or
derive an `S`-breaking preferred-clock/readout ingredient. Approved primitives
and the four-axiom surface do not supply a site-preferred readout by
themselves, and this note does not propose a new axiom or primitive.

**N7 -- Steelman.** A future dynamics, environment, boundary condition, or record-production
mechanism could make one clock stable and the other nonphysical. A future
diagonal quotient could also remove the antisymmetric sector without preferring
one named site-clock. Those would be real routes against N5 pressure, but they
do not defeat this narrow `S`-invariant site-preference no-go.

**N8 -- Cross-cycle echo.** The closest precedent is the family of `W`-transportable
axis-label no-gos: symmetry transport prevents label selection until a
symmetry-breaking labeling or readout input is supplied. This note copies that
scope discipline for the clock-selector subproblem rather than claiming an
absolute single-clock impossibility.

**Runner:** [`scripts/n5_single_generator_clock_exchange_no_go_2026_06_17.py`](../scripts/n5_single_generator_clock_exchange_no_go_2026_06_17.py)
(`TOTAL: PASS=12 FAIL=0`, deterministic, no RNG, < 1s). No fitted parameters, no observed
values, no new axioms, no axiom-file edits, no `docs/audit/data/*` edits. Sets no audit status.
