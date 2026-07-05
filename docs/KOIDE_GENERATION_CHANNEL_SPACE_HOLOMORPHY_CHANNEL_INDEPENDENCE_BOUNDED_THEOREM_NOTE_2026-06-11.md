# The Complete C₃-Equivariant Generation Channel Space Is M₄⊕M₂⊕M₂, Fully Lattice-Realizable; First-Order Holomorphy Is Channel-Independent and Count-Twice Arises Exactly on Antiunitary-Tied Parameter Sections (Bounded Theorem)

**Date:** 2026-06-11
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. This source note
does not set or predict an audit outcome, does not adopt any premise, and
does not edit the audit-lane-owned Tier-A registry or any audit data file.
**Primary runner:**
[`scripts/frontier_koide_equivariant_channel_space_holomorphy_2026_06_11.py`](../scripts/frontier_koide_equivariant_channel_space_holomorphy_2026_06_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_equivariant_channel_space_holomorphy_2026_06_11.txt`](../logs/runner-cache/frontier_koide_equivariant_channel_space_holomorphy_2026_06_11.txt)
(SCORECARD: PASS=17, FAIL=0)

> **Not claimed:** a derivation of `r = 1/2` or `r = 1`, adoption of any
> occupancy/weighting rule, or any audit status. **Claimed (bounded):** the
> channel-generality residual declared by
> [`KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md)
> (block01) is closed at the bilinear level: the **complete**
> C₃-equivariant coupling space on the corner sector is classified
> (`M₄(C) ⊕ M₂(C) ⊕ M₂(C)`, 24-dimensional, fully lattice-realizable,
> including native hw=1↔hw=2 mixing channels), first-order holomorphy of
> the Berezin corner output holds for **every** channel, and
> count-twice/modulus structure arises **exactly on the antiunitary-tied
> parameter sections** — never from the measure, for any channel.

## Role

Block01 proved, for the single rotation-channel probe, that the
one-component staggered measure delivers a first-order generation
determinant with count-twice entering only through the K-reality
restriction `c = b̄`, and declared the coupling form a residual: other
channels might behave differently. This note closes that residual for the
whole bilinear equivariant channel space and, in doing so, **refines**
block01's headline: the general statement has *two* antiunitary tying
classes, and block01's `c = b̄` line is the circulant locus where they
coincide.

## The five computed results (runner, 17/17)

**Result 1 — classification.** On the reconstructed gate-note surface
(`D` real antisymmetric, `dim ker D = 8`, exact corner basis, Hamming
grading 1+3+3+1, rotation permutation `P8` with `P8³ = I`), the realized
C₃ action has isotype multiplicities `(trivial, ω, ω̄) = (4, 2, 2)` (exact
projector traces), so the equivariant coupling space — the commutant — is
`M₄(C) ⊕ M₂(C) ⊕ M₂(C)`, complex dimension 24. Computed twice: nullity of
the commutator map, and an explicit basis of 24 **integer** orbit-sum
matrices (checks 3–5).

**Result 2 — lattice realizability, including hw-mixing.** The staggered
phase `ε(x) = (−1)^{x₁+x₂+x₃}` restricts on the corner sector to the exact
corner-label **complement** `hw_k ↔ hw_{3−k}` — a native hw=1↔hw=2 mixing
channel — and the `ε_μ(x) = (−1)^{x_μ}` phases to the bit-μ toggles.
Translation/`ε_μ` monomials span all of `M₈` on the corner sector
(rank 64), and their C₃ averages span the full 24-dimensional channel
space (checks 6–7). Every equivariant channel is realizable by
lattice-built operators; the hw-mixing channel class named OPEN by the
dynamical pruning no-go is inside the classification, not outside it.

**Result 3 — block structure and factorization, every channel.** In the
exact isotype basis `V` (ω̄ columns defined as conjugates of ω columns),
every channel basis element is block-diagonal `(A₄, β, γ)`; the corner
determinant factorizes as `det(A₄)·det(β)·det(γ)` (verified by full 8×8
exact determinants at exact rational/complex parameter points); and
complex conjugation maps every channel's blocks
`(A₄, β, γ) → (Ā₄, γ̄, β̄)` — the ω/ω̄ doublet blocks are **one K-orbit
for every channel** (checks 8–11).

**Result 4 — channel-independent holomorphy.** The channel space is the
C-span of integer matrices, so for every channel the first-order corner
output is a **polynomial** in the channel parameters; `det β` and `det γ`
computed symbolically over all 24 parameters contain no conjugate
(check 12). The first-order measure never supplies count-twice, for any
bilinear equivariant channel.

**Result 5 — the two antiunitary tying classes.** Count-twice/modulus
structure arises exactly on parameter sections tied by an antiunitary:

- **K-real section** (real channel parameters — lattice-real couplings):
  `γ = β̄` exactly for every channel, and the doublet factor becomes
  `det β · conj(det β) = |det β|²` — the modulus, channel-independently
  (check 13).
- **Hermitian section** (`A† = A`; transpose permutes the integer basis,
  so Hermiticity ties `θ_i = conj θ_{τ(i)}`): blocks become individually
  Hermitian, and a Hermitian-restricted doublet block `[[p,z],[z̄,q]]`
  carries the in-block count-twice term (Wirtinger `∂²det/∂z∂z̄ = −1`),
  while the unrestricted block determinant is conjugate-free (check 14).

Both landed objects are recovered as instances: block01's rotation channel
is the scalar (circulant) case `β = λ_ω I`, `γ = λ_ω̄ I` with the landed
`(a+b+c)²·det₃²` identity reproduced exactly, and its `c = b̄` line is the
channel-space K-real section (check 15); the 2026-06-08 Hermitian-corner
`|det M|²` object is the **Hermitian point of the native ε-mixing channel
family**, whose unrestricted form is holomorphic (`det β = −μμ′`,
conjugate-free) and whose Hermitian point ties `μ′ = μ̄`, giving
`det β = −|μ|²` (check 16). A full-surface ratio test confirms the corner
factorization governs `det(D + tA)` with the ε-mixing channel included
(mismatch < 6×10⁻⁶, check 17).

## Consequence — the occupancy binary is channel-independent

On this surface, the standing occupancy/polarization atom takes one
channel-independent form:

> read the generation determinant on an **antiunitary-tied parameter
> section** (sector slots; modulus/count-twice; the landed `r = 1`
> readouts), or read the **unrestricted holomorphic first-order output**
> with outcomes grained by K-orbits (the ω/ω̄ block pair is one orbit for
> every channel; count-once; `r = 1/2`).

The custody note's K-reality selector (`b = c̄`) is the circulant instance
of the tied section; the Kähler-Dirac `|det M|²` is the Hermitian point of
the ε-mixing family. So the occupancy atom and the K-reality selector are
**one binary, not two independent knobs**, on the realization surface —
with the refinement that "tied" splits into the reality class
(cross-block, `γ = β̄`) and the Hermiticity class (in-block, `z z̄`),
which coincide on the circulant channel. Which reading is physical
remains the named owner-decision premise surface; nothing here selects it.

## What this note does NOT claim

- **Not** a derivation of `r = 1/2` or `r = 1`; no occupancy, weighting,
  or reading-section rule is adopted or derived.
- **Not** a claim beyond bilinear (free/quadratic) matter actions;
  interacting or beyond-bilinear couplings are outside the classification
  (declared residual).
- **Not** a claim about couplings that break the C₃ carrier (excluded by
  the gate-note species surface, not by this runner).
- **Not** a Tier-A registry change or audit verdict. The `AC_φλ`
  admission and its sub-residuals stand unchanged.
- **No** PDG value, fitted selector, or empirical comparator is consumed.

## Honesty gate (negative-flavored sub-claim discipline)

The negative-flavored sub-claim — "the measure never supplies count-twice,
for any channel" — is scoped: (i) bilinear couplings on the corner sector
of this surface; (ii) channels commuting with the realized C₃; (iii) the
classification is complete *within* that scope (commutant computed two
independent ways; realizability exhibited), so the universal quantifier is
over a computed finite-dimensional space, not an open-ended family.
Outside scope and OPEN: interacting actions, gauge-sector/measure-
normalization contributions, non-equivariant couplings, off-circulant
carriers, and the physical selection of the reading section. The prior
no-gos' `r = 1` results are reproduced on the tied sections, not
contradicted.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  (surface and inherited §5 residuals, consumed at declared grade)
- [`KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  (block01; the channel-generality residual closed here)
- [`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md)
  (the Hermitian-corner object recovered as the ε-family Hermitian point)
- [`KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_DYNAMICAL_DETERMINANT_ROUTE_PRUNING_NO_GO_NOTE_2026-06-08.md)
  (whose open non-tested channel classes are located inside the
  classification)
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  (the K-reality selector, located as the circulant tied section)
- [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
  (the occupancy atom whose channel-independent dynamical form is stated
  here)

## Reprove-and-cite ledger

- **Reproven here (runner):** the surface; the isotype multiplicities;
  the commutant dimension (two routes); the integer orbit-sum basis; the
  ε/ε_μ corner restrictions; the M₈ span and equivariant-average span;
  the exact isotype basis and P8 block-diagonalization; the block
  structure of all 24 basis elements; the K block-swap; the 8×8-vs-block
  determinant factorization at exact points; the symbolic
  conjugate-freedom of `det β`, `det γ`; the K-real `γ = β̄` tying and
  `|det β|²`; the transpose involution and Hermitian Wirtinger `−1`; the
  rotation-channel embedding identity; the ε-family blocks, holomorphy,
  and Hermitian-point modulus; the full-surface ratio test.
- **Cited at declared grade:** block01's results; the gate-note premises;
  the landed fork/no-go scopes; the custody selector naming; the
  occupancy-atom independence result.

## Verification

```bash
python3 scripts/frontier_koide_equivariant_channel_space_holomorphy_2026_06_11.py
```

Expected: 17 `[PASS]` lines, four `RESIDUAL (declared-open)` lines, then
`TOTAL: PASS=17 FAIL=0` and the verdict paragraph. Exit code 0 iff FAIL=0.

**Independent audit required.** This note asserts no effective-status
change.
