# The One-Component Staggered Measure Delivers a First-Order Generation Determinant; Count-Twice Enters Exactly and Only Through the K-Reality Restriction (Bounded Theorem)

**Date:** 2026-06-11
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. This source note
does not set or predict an audit outcome, does not adopt any premise, and
does not edit the audit-lane-owned Tier-A registry or any audit data file.
**Primary runner:**
[`scripts/frontier_koide_staggered_first_order_generation_determinant_2026_06_11.py`](../scripts/frontier_koide_staggered_first_order_generation_determinant_2026_06_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_staggered_first_order_generation_determinant_2026_06_11.txt`](../logs/runner-cache/frontier_koide_staggered_first_order_generation_determinant_2026_06_11.txt)
(SCORECARD: PASS=19, FAIL=0)

> **Not claimed:** a derivation of `r = 1/2`, a derivation of the
> generation Yukawa coupling form, adoption of the orbit-occupancy premise
> candidate, retirement of any admission, or any audit status. **Claimed
> (bounded):** on the staggered-Dirac realization surface, with the
> `C_3[111]` rotation channel as a declared probe coupling, the matter
> measure's generation determinant is **first-order** (a single power,
> computed by explicit Grassmann expansion); the taste-conjugate triplet
> squares the generation factor **channel-uniformly** (r-neutral); and the
> count-twice `|b|^2` dependence that forces `r = 1` in the landed
> modulus-route no-gos enters **exactly and only** through the K-reality
> restriction `c = conj(b)` of the coupling parameters — not through the
> measure, the corner structure, or the taste doubling.

## Role — the named open question this answers

The meta-note
[`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
localized the Koide `r`-gate to one dynamics question: *does the
framework's staggered-Dirac realization deliver the first-order
(count-once) or second-order (count-twice) generation determinant?* The
static-readout no-go
([`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md))
named this as the only non-circular opening and recorded that "its
first-order construction is not yet done." The Kähler-Dirac realization
no-go
([`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md))
closed the index route on the hand-built Hermitian-corner doubling
`D = [[0,M],[M†,0]]`, whose determinant is `|det M|²` **by construction**.
This note does the construction that was not yet done: it starts from the
**actual matter measure** of the realization gate
([`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
— one Grassmann pair per site, forced) and computes what that measure
delivers, with no Hermitian doubling put in by hand.

## The four computed facts (runner, 19/19)

Surface: the one-component staggered operator `D` with Kawamoto-Smit
phases on the periodic `4³` torus (real antisymmetric, `dim ker D = 8`,
spectral gap 1.0, Hamming grading `1+3+3+1`), the exact corner plane-wave
null basis, and the lattice `C_3[111]` rotation `U_R` — all reconstructed
from scratch and verified against the gate note (checks 1–5).

**Fact 1 — the measure is first-order.** The Berezin integral of the
single-pair-per-site Grassmann measure is computed by explicit
exterior-algebra expansion and nested single-generator Berezin
integrals — no determinant identity is assumed at any point. For a generic
symbolic 3×3 coupling, and for an antisymmetric-kinetic-plus-coupling toy
of the staggered shape, the partition function is `det(D + A)` to the
**first power** (checks 6–7). The measure does not produce `|det|²`; the
Hermitian L/R doubling of the Kähler-Dirac note is an additional
construction step, not a consequence of the matter-statistics clause.

**Fact 2 — exact corner factorization; the taste square is r-neutral.**
For the probe coupling `A(a,b,c) = a·I + b·U_R + c·U_R^T` (the rotation
channel), `U_R|_ker` is an exact integer permutation, block-diagonal in
the Hamming grading, whose hw=1 and hw=2 blocks are 3-cycles in the
**same** orientation class (checks 8–10). The corner determinant
factorizes exactly (sympy):

```text
det(A|_ker) = (a+b+c)² · det₃(a,b,c)²,   det₃ = a³ + b³ + c³ − 3abc.
```

The taste-conjugate hw=2 triplet **squares** the generation circulant
factor — a *holomorphic* square, not a modulus (check 11). The square is
channel-uniform, so it cancels in any doublet:singlet weight ratio (the
landed pruning lemma, reproven; check 12). The small-`t` leading behaviour
of `det(D + tA)` on the full 64-dimensional surface matches the corner
factorization (ratio test, mismatch < 6×10⁻⁶; check 13).

**Fact 3 — the holomorphy fork is exact and localized.** The Berezin
corner output is a degree-8 **polynomial** in `(a,b,c)`: the first-order
measure introduces no conjugate dependence whatsoever (check 14). With `c`
independent the channel factor is **harmonic** in `(Re b, Im b)`
(Laplacian = 0, the exact holomorphy criterion); on the K-real line
`c = b̄` the Wirtinger derivative `∂² det₃ / ∂b ∂b̄ = −3a`
(Laplacian `−12a`) — the count-twice `|b|²` term of the rank-2 modulus
wall appears exactly there (check 15). The K-real line is exactly the
Hermitian-channel restriction of the probe coupling (check 16). So on this
surface the second-order (count-twice) structure is not supplied by the
measure, the corner sector, or the taste doubling — it is supplied by the
**parameter restriction** `c = b̄`, which is the K-reality selector already
named as an operative admitted input in
[`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md).

**Fact 4 — the doublet channels are one K-orbit.** Complex conjugation
swaps the `ω`/`ω̄` generation-channel projectors and fixes the trivial
channel; on the K-real line the channel spectrum
`λ_k = a + 2|b| cos(δ + 2πk/3)` is K-paired by `δ → −δ`: the trivial
channel is K-fixed and the two generically distinct doublet eigenvalues
swap (checks 17–18). With the landed ρ-map orientation (cells cited from
[`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md),
arithmetic reproven), Hermitian-channel (count-twice) slotting gives
`r = 1` and holomorphic-channel (one slot per K-orbit) slotting gives
`r = 1/2` (check 19).

## What this changes — the fork relocated, not resolved

The gate question "first-order or second-order?" has, on this surface, a
computed answer: **the measure side is first-order.** What remains is not
a measure-order question at all. The binary that decides `r` is:

> read the generation determinant on the **K-real section** of the
> coupling space (Hermitian channel; `|b|²` dependence; sector slots;
> `r = 1`), or read the **holomorphic first-order output** with outcomes
> grained by K-orbits (one slot per `ω/ω̄` pair; `r = 1/2`).

This is the same binary as the occupancy atom of
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md),
now realized dynamically on the actual matter surface rather than at the
bookkeeping level: the sector-vs-orbit slot choice appears as the
K-real-section-vs-K-orbit-quotient reading of one and the same first-order
determinant. In particular, on this surface the custody note's two named
selectors are not independent knobs: imposing K-reality on the coupling
**is** what creates the rank-2 `|b|²` (count-twice) structure that the
modulus-route no-gos then read out as `r = 1`. Neither horn is derived
here; the runner prints both as declared-open residuals.

## What this note does NOT claim

- **Not** a derivation of `r = 1/2` or `r = 1`: which horn is physical is
  not decided by this surface, and no occupancy/weighting rule is adopted.
- **Not** a derivation of the generation Yukawa form: the rotation-channel
  probe `A = aI + bU_R + cU_R^T` is a **declared probe coupling**
  (residual printed at the point of use). Conclusions are about what this
  channel delivers on the realization; other `C_3`-equivariant couplings
  are not enumerated here.
- **Not** a contradiction of the landed `r = 1` no-gos: on the K-real
  (Hermitian) section this note reproduces exactly the rank-2 `|b|²`
  structure those notes read out. The new content is *where* that
  structure enters.
- **Not** a Tier-A registry change, premise adoption, or audit verdict;
  the `AC_φλ` admission and its sub-residuals stand unchanged.
- **No** PDG value, fitted selector, or empirical comparator is consumed
  anywhere; `r = 1/2` and `r = 1` are named only as the landed fork cells.

## Honesty gate (localization-claim discipline)

The negative-flavored sub-claim here is narrow: "count-twice does not
enter through the measure/corner/taste structure *of this probe coupling
on this surface*." Routes outside that scope, named: (i) other
`C_3`-equivariant coupling channels (multi-link, translation-built taste
operators) — OPEN, not tested; (ii) gauge-sector or measure-normalization
contributions beyond the matter Grassmann measure — OPEN; (iii)
interacting/beyond-quadratic actions — OPEN; (iv) the Hermitian-corner
Dirac construction — not a counter-route but a different object,
reproduced on the K-real section (the prior no-gos' scope); (v)
off-circulant constructions — outside the `C_3` carrier, OPEN. The claim
is an exact computed identity on the stated scope, not a universal
negative.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  (consumed at its declared bounded grade; its §5 residuals — kinetic-class
  premise, spin-statistics support tier, boundary-holonomy convention,
  `AC_φλ` labeling convention — are inherited and printed by the runner)
- [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
- [`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`](KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md)
- [`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md)
- [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  (the landed cells and ρ-map orientation)
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  (the K-reality selector this note localizes the count-twice term onto)
- [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
  (the occupancy atom this note realizes dynamically)

## Reprove-and-cite ledger

- **Reproven here (runner):** the staggered surface (D, kernel, gap,
  grading, `U_R`) from scratch; the Berezin first-power identity by
  explicit Grassmann expansion (no determinant identity assumed); the
  corner permutation structure and both 3-cycle orientations; the exact
  `(a+b+c)²·det₃²` factorization; the uniform-power cancellation lemma;
  the full-surface small-`t` ratio test; the polynomial/holomorphy fact;
  the Wirtinger localization of the `|b|²` term; the Hermitian-section
  identification; the K-orbit channel pairing; the ρ-map cell arithmetic.
- **Cited at declared grade:** the gate-note synthesis and residuals; the
  landed fork cells and orientation; the K-reality selector naming; the
  occupancy-atom independence result.

## Verification

```bash
python3 scripts/frontier_koide_staggered_first_order_generation_determinant_2026_06_11.py
```

Expected: 19 `[PASS]` lines, four `RESIDUAL (declared-open)` lines, then
`TOTAL: PASS=19 FAIL=0` and the verdict paragraph. Exit code 0 iff
FAIL=0.

**Independent audit required.** This note asserts no effective-status
change.
