---
claim_id: microcausality_directional_tilt_axis_cone_refinement_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional refinement of the sibling bond-class walk bound on the same supplied surface (axioms supply no dynamics; same class, algebra, Heisenberg convention, and declared ODE context as the sibling; the refinement changes only the walk-COUNTING step), for observables separated along a coordinate axis: (D1) the exact height-change tables of the bond-adjacency graph under the height phi(b) = sum of the two axis-coordinates — parallel start {−2:1, −1:4, +1:4, +2:1}, transverse start {−1:2, 0:6, +1:2} — natively enumerated, box-stable, both transverse orientations; (D2) the tilt polynomials S_par(y) = y^2 + 4y + 4/y + 1/y^2 and S_perp(y) = 2y + 6 + 2/y with S_par(1) = S_perp(1) = 10 and the exact domination factorization S_par − S_perp = (y−1)^2(y^2+4y+1)/y^2 ≥ 0; (D3) the walk-tilt counting lemma, REBUILT: for y ≥ 1 the tilted walk sum factorizes stepwise below S_par(y)^{k−1}, and the indicator bound 1{gain ≥ m} ≤ y^{gain−m} gives #{k-bond walks with height gain ≥ m} ≤ n_X · S_par(y)^{k−1} · y^{−m}; (D4) the exact offset — bonds touching a hyperplane {x_1 = a} have phi in {2a−1, 2a, 2a+1}, so axis separation m forces gain ≥ 2m − 2; (D5) the theorem: for every rational y > 1, ||[τ_t(A), B]|| ≤ 2||A||||B|| n_X (y^2/S_par(y)) y^{−2m} (e^{2J S_par(y)|t|} − 1) — at y = 5/2 the decay factor is manifestly (4/25)^m per axis-site, all t, volume-uniform, with NO logarithm anywhere in the display; (D6) the velocity readout v_axis(y) = J·S_par(y)/ln y with the y = 5/2 instance (1801/100)J/ln(5/2), CERTIFIED below the parent readout 20eJ by exact rational brackets (e > 1957/720 from the factorial series; ln(5/2) > 2(3/7 + 9/343) from the atanh series, both displayed as rebuilt proofs and additionally gated by exact evalf comparisons), and certified best only WITHIN the six-point rational scan (pairwise gates against ALL FIVE other scan points; optimality over all y is NOT claimed), with the sibling k-term reconstructed symbolically and summed to the display (assembly gate), the e-bracket's finite sum gated exactly (sum_{n<=6} 1/n! = 1957/720), and the final rational margin gated as exactly 3234971/102900 > 0. Scope is per-axis: for diagonal separations the sibling isotropic bound can dominate and both bounds hold simultaneously; the anisotropic three-axis product tilt is named open; nothing physical is selected."
upstream_dependencies:
  - minimal_axioms
  - microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py
---

# Microcausality: Directional-Tilt Axis-Cone Refinement

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; same supplied bond class, algebra, and
conventions as the sibling walk-expansion note; only the walk-counting
step is refined; per-axis statement.
**Audit-status authority:** independent audit lane only. This note sets
no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py`](../scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.txt`](../logs/runner-cache/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.txt)

## Purpose

The sibling
[`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
proved the all-time volume-uniform bound with activity scale `20J` and
velocity-type readout `20eJ`, stating both non-sharp. This note takes
the sharp-rate item **partially**: it refines the walk-counting step —
and only that step — by tilting the count along a coordinate axis. The
sibling counts every walk equally (`10` per step); the tilt weights
each step by `y^{Δφ}` for a height function `φ` along the axis and a
rational `y > 1`, so walks that must climb toward a distant `Y` pay
`y^{−2m}` while the per-step cost only grows to `S_par(y) < 10·y^2`.
At `y = 5/2` this certifies an axis-cone velocity readout of
`(1801/100)J/ln(5/2)` — about `2.77×` below the sibling's `20eJ` —
with three honest boundaries stated up front: the statement is
**per-axis** (for diagonal separations the sibling's isotropic bound
can dominate; both hold simultaneously), the scan point is best only
**within the six-point rational scan** (no optimality over `y` is
claimed), and the true sharp rate remains **open**.

## Hypotheses (all supplied, none derived)

Exactly the sibling's supplied surface: finite `Λ ⊂ Z^3` with its
nearest-neighbor bond set, supplied Hermitian bond terms `h_b` with
`J = max ||h_b||`, the Heisenberg convention, the declared
finite-matrix ODE context, directed time with the `H → −H` extension,
and the standing scoping hypothesis `X ∩ Y = ∅`. The refinement
concerns only the counting of the walks that the sibling's Duhamel
expansion already produces; no algebraic step is touched. Axis setup:
fix a coordinate axis `e` (by cubic symmetry, `e = e_1`); let
`a = max_{x∈X} x_1` and suppose `Y ⊆ {x : x_1 ≥ a + m}` for an integer
`m ≥ 1` (the **axis separation**; the graph distance obeys `d ≥ m`).
The axioms supply no dynamics (needled); everything is
bridge-conditional. No literature statement is load-bearing; tilted /
generating-function walk counting is standard combinatorics whose
load-bearing steps are rebuilt and gated here.

## Results

**Height-change tables (exact, native, box-stable).** For a bond
`b = {p, q}` define `φ(b) = p_1 + q_1`. A bond parallel to `e_1` at
base `x` has `φ = 2x + 1`; a transverse bond at level `x` has
`φ = 2x`. The `10` neighbors of a bond change `φ` by:

- parallel start: `Δ ∈ {−2 (×1), −1 (×4), +1 (×4), +2 (×1)}`;
- transverse start (both transverse orientations, enumerated
  separately): `Δ ∈ {−1 (×2), 0 (×6), +1 (×2)}`.

**Tilt polynomials and domination.** For a formal `y > 0`,

> `S_par(y) = y^2 + 4y + 4/y + 1/y^2`,  `S_perp(y) = 2y + 6 + 2/y`,

built term-by-term from the tables (gated), with the untilted sanity
`S_par(1) = S_perp(1) = 10` and the exact factorization

> `S_par(y) − S_perp(y) = (y − 1)^2 (y^2 + 4y + 1) / y^2 ≥ 0`,

so `S_par` dominates both step types for every `y > 0` (gated
symbolically; each factor is nonnegative for `y > 0`).

**Walk-tilt counting lemma (rebuilt).** Fix `y ≥ 1`. For any bond of
`Z^3`, the sum of `y^{Δφ}` over its `10` neighbors is at most
`S_par(y)` (the row bound — by the tables and domination; in a finite
`Λ` a boundary bond's row is a sub-sum of positive terms, so the bound
only improves). Hence, by backward
induction on the remaining steps, the tilted sum over all `k`-bond
walks from a start set of size `n_X` obeys

> `Σ_walks y^{φ(b_k) − φ(b_1)} ≤ n_X · S_par(y)^{k−1}`,

and since `1_{gain ≥ m'} ≤ y^{gain − m'}` for `y ≥ 1` (if the gain
reaches `m'` the right side is at least `1`; otherwise the left side
is `0` and the right side is positive),

> `#{k-bond walks with height gain ≥ m'} ≤ n_X · S_par(y)^{k−1} ·
> y^{−m'}`.

Both steps are gated: the row bound symbolically in `y`, the
indicator bound at exact instances with the sign argument in text.

**Exact offset.** Bonds touching the hyperplane `{x_1 = r}` have
`φ ∈ {2r − 1, 2r, 2r + 1}` (enumerated at instances). With the axis
setup above, start bonds have `φ(b_1) ≤ 2a + 1` and end bonds
(touching `Y`) have `φ(b_k) ≥ 2(a + m) − 1`, so every contributing
walk has height gain at least `2m − 2` (gated arithmetic).

**Theorem (axis-cone refinement).** Feeding the tilted count into the
sibling's unrolled expansion (whose base terms, prefactors, and
iterated integrals are unchanged), for every rational `y > 1`:

> `||[τ_t(A), B]|| ≤ 2||A|| ||B|| n_X · (y^2/S_par(y)) · y^{−2m} ·
> (e^{2J S_par(y) |t|} − 1)`,

for all `t` and every finite `Λ` (assembly identity gated:
`Σ_{k≥1} (2JS|t|)^k/k! = e^{2JS|t|} − 1` and the `y^2` bookkeeping
from the offset). At `y = 5/2` the display contains **no logarithm**:
the decay factor is exactly `(4/25)^m` per axis-site (gated identity),
manifest exponential decay in the axis separation at every fixed `t`,
volume-uniformly. Both this bound and the sibling's isotropic bound
hold simultaneously; neither supersedes the other (for diagonal
separations `m ≪ d` the sibling's can be stronger — stated, not
hidden).

**Velocity readout and certified comparison.** The bound decays once
`2m ln y > 2J S_par(y) |t|`, i.e. an axis velocity
`v_axis(y) = J · S_par(y)/ln y`. At `y = 5/2`:
`S_par(5/2) = 1801/100` exactly (gated), so

> `v_axis(5/2) = (1801/100) · J / ln(5/2)`  (advisory `≈ 19.66 J`).

Certified below the sibling readout `20eJ` (advisory `≈ 54.37 J`) by
exact rational brackets, displayed as rebuilt proofs and additionally
gated by exact comparisons: `e > 1957/720` (a partial sum of the
everywhere-positive factorial series `Σ 1/n!`), and
`ln(5/2) = 2·atanh(3/7)` (since `(1 + 3/7)/(1 − 3/7) = 5/2`, gated)
`> 2(3/7 + (3/7)^3/3) = 2·(156/343) = 312/343` — the first two
terms of the everywhere-positive odd series — so

> `20 · e · ln(5/2) > 20 · (1957/720) · (312/343) > 1801/100`,

a pure rational comparison with wide margin (gated exactly, alongside
direct exact-evalf gates). Within the six-point rational scan
`y ∈ {5/4, 3/2, 2, 5/2, 3, 4}`, `y = 5/2` is certified best against
**all five** other scan points by the pairwise gates
`S_par(y')·ln(5/2) > (1801/100)·ln(y')` for every
`y' ∈ {5/4, 3/2, 2, 3, 4}` (with `S_par` values `4161/400`, `409/36`,
`57/4`, `202/9`, `529/16`) — and **only** scan-best is
claimed; optimality over all real `y > 1` is open, as is the true
sharp rate.

## No-Go Discipline Gate

- **N1 route inventory (residuals first).** Not attempted, not
  smuggled: (i) the true sharp rate — the tilt is a counting
  refinement; no optimization over walk correlations, non-backtracking
  structure, or exact generating functions is performed; (ii) the
  anisotropic three-axis product tilt (simultaneous decay in all
  coordinate separations) — named open; (iii) the transfer
  identification and `U`-integrated items — untouched, as in the
  siblings. Positive routes weighed: (1) tilt the accumulated-support
  coefficient count of the second sibling — ATTEMPTED as a design and
  REJECTED: coefficient-level sequences are not walks (that sibling
  proves the count is accumulated-support), so the tilt has no
  factorizing step there; (2) tilt with irrational optimal `y = y*` —
  ATTEMPTED as a design and REJECTED for the exact bar: the rational
  scan keeps every gate exact, at the cost of claiming only scan-best;
  (3) per-step type-resolved products (tracking parallel/transverse
  sequences exactly) — ATTEMPTED and simplified away: the domination
  factorization makes the uniform `S_par` bound exact-provable and
  costs little at the scan points.
- **N2 hypothesis independence (pairwise) — ATTEMPTED.** The tilt parameter `y`
  (counting only), the offset `2m − 2` (geometry only), the axis
  choice (cubic symmetry, both transverse orientations enumerated),
  and the sibling chain (algebra, untouched) enter at disjoint steps
  (the session mutation battery recorded in the loop pack flips each
  runner gate separately; the runner itself performs no mutations).
  No new physical hypothesis enters.
- **N3 hidden-wall scan — ATTEMPTED.** The only analysis objects beyond the
  sibling chain are `ln` and `e` **in the readout only** — the
  theorem display is logarithm-free at rational `y`. The readout
  comparisons are gated twice: by the rebuilt rational brackets
  (positivity of the displayed series' partial sums) and by direct
  exact comparisons of the same class the family already uses for
  `sin`/`exp` instances.
- **N4 dependency roles, per citation — ATTEMPTED.**
  - [`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    supplies the entire Duhamel chain and the walk set this note
    recounts; its non-sharpness sentence is the item taken here
    (needled). Residual: none — the counting step is the only change.
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only.
  - Tilted-count combinatorics literature: comparator class only; the
    lemma is rebuilt above.
  - Loop-pack worker analysis (`worker_b06_*`): scaffolding,
    disclosed; graded against supervisor derivations computed
    independently first; not executed or cited by the runner.
- **N5 rhetoric audit — ATTEMPTED.** "Refinement" is scoped to the counting step;
  "certified" refers to the exact gates named; "best" is always
  "scan-best"; the per-axis boundary and the simultaneous validity of
  the sibling bound are stated in the theorem paragraph itself.
- **N6 partial-closure scan — ATTEMPTED.** Closed here: a certified axis-cone
  improvement of the family's velocity readout (`≈ 2.77×` at the scan
  point). Still open, named: the true sharp rate, the anisotropic
  product tilt, the transfer identification, the `U`-integrated item.
- **N7 steelman (strongest counterarguments, answered) — ATTEMPTED.** (a) "The
  per-axis statement is weaker than the isotropic bound for diagonal
  pairs." Correct and stated where the theorem is stated; both bounds
  hold; the refinement targets axis-aligned geometry. (b) "The
  readout involves transcendental constants, breaking the exact bar."
  The theorem display is logarithm-free; the readout comparisons are
  doubly gated (rebuilt rational brackets + exact evalf), and the
  brackets' series are displayed. (c) "Scan-best might mislead toward
  optimality." The claim is scan-best only, gated pairwise, with
  optimality explicitly open. (d) "The row bound uses S_par even for
  transverse steps — is that lossy?" Yes, deliberately: domination is
  exact and gated; type-resolved refinement is named as a rejected
  route with its trade-off.
- **N8 prior-wall echo — ATTEMPTED.** The sibling's non-sharpness
  sentences are the wall this note moves **openly** (its readout
  stays an upper bound; nothing sharp is claimed). A grep across all
  246 `NO_GO` notes for walk-counting/tilted-count/Lieb-Robinson
  content found five mentions, all comparator/reference uses; the
  closest (`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`,
  backticked: dispositioned, not load-bearing) forbids deriving a
  time-axis selection from record durability — orthogonal to this
  note, whose spatial axis is a hypothesis of the geometry, not a
  derived selection. The family's exhibit-pair discipline is repeated
  (the offset and tables gated at exact instances; the non-optimality
  boundary stated).

**Status: PASS** (all eight items answered; the three honest
boundaries — per-axis, scan-best, non-sharp — are in the theorem and
readout paragraphs, not appendices).

## Non-Claims

- Does **not** claim the sharp rate, optimality of `y = 5/2` beyond
  the six-point scan, or any anisotropic multi-axis statement.
- Does **not** supersede the sibling's isotropic bound (both hold;
  for diagonal separations the sibling's can be stronger).
- Does **not** modify any algebraic step of the sibling chain, its
  class, or its constants on its own statement.
- Does **not** apply to the plaquette class (bond class only; the
  face-inclusive tilt is not attempted).
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py`](../scripts/microcausality_directional_tilt_axis_cone_refinement_2026_07_18.py)
— exact throughout. Gate kinds, honestly distinguished: **exhaustive
finite gates** (the height-change tables for the parallel start and
both transverse orientations, at two box radii), **symbolic identity
gates** (the tilt polynomials built term-by-term from the enumerated
tables; the domination factorization with per-factor nonnegativity;
the row bound; the assembly identity; the `(4/25)^m` display
identity), **exact instance gates** (the indicator inequality
instances; the hyperplane `φ`-ranges; the offset arithmetic;
`S_par(5/2) = 1801/100`), **reconstruction gates** (the sibling
`k`-term rebuilt symbolically — count times prefactors times iterated
integral — and summed to the theorem display), and **certified
comparison gates** (the rational-bracket chain with its finite sum
gated exactly — `Σ_{n≤6} 1/n! = 1957/720`, `ln(5/2) > 312/343` with
the two-term atanh partial gated as `312/343` exactly, the
pure-rational final comparison with margin exactly `3234971/102900` —
plus supplemental sign-determination comparisons via sympy, which
fail closed on an undecided `None`, and the pairwise scan gates
against all five other scan points). The
`N`-group gates are presence needles, not correctness oracles. The
gate sequence is enforced against an ordered label manifest. The
runner prints one `PASS`/`FAIL` line per gate and a final total; the
cached transcript is committed at the path in the header at landing
time.
