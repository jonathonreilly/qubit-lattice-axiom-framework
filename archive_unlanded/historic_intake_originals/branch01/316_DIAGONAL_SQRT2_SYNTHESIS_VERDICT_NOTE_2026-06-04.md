# Diagonal-Connection Thought Experiment — √2-Centered Synthesis & Verdict

**Date:** 2026-06-04
**Type:** synthesis / verdict
**Claim type:** meta
**Status authority:** independent audit lane only. This note sets no audit
status and changes no axiom. It synthesizes the five phases of the
√2-centered diagonal-connection exploration and records the honest verdict.

## One-paragraph verdict

Extending `Z^3` adjacency to face-diagonals is a **beautiful unifying
picture** — one structural change touches all three open gates — but on
rigorous examination it **closes no gate**. It cleanly **relocates** each:
color from "no `su(3)` on the triplet" to "`su(3)` on generation space,
color identification still open"; chirality from "no grading on NN" to
"grading available on the wider class, selection still open"; and `r = 1/2`
from "admitted modulus" to "`√2`-weighted convention whose weighting rule is
not forced." The decisive negative is geometric: the **actual `Z^3` lattice
Green function** between face-diagonal sites is `0.641`, **not** `1/√2 = 0.707`
— so the one parameter-free candidate that could have *forced* `√2` does not.
The exploration is valuable precisely because it is a clean negative: it
rules out the diagonal-geometric route to `r = 1/2` and sharpens where each
gate actually lives.

## Phase scorecard (all runner-verified, 157 PASS / 0 FAIL total)

| Phase | Question | Runner | Verdict |
|---|---|---:|---|
| 1 Foundation | Do the four scout facts hold? | 16/0 | YES — all four are finite linear-algebra facts |
| 2 (L1) | Does diagonal-as-Wilson-composite add new DOF? | 27/0 | **NO** — zero new DOF; `W1·W2† = U_plaquette` exactly. Gate content requires L2/L3, not free L1. |
| 3 (√2-forcing) | Is the `√2` weighting FORCED, giving derived `r=1/2`? | 34/0 | **NOT FORCED** (0 of 6 candidates force it; lattice Green fn = 0.641 ≠ 0.707) |
| 4 (color) | Does face-diagonal supply color `SU(3)`? | 35/0 | **PARTIAL** — genuine `su(3)`, but on generation space, not color (mismatched `Z_3` characters) |
| 5 (chirality) | Does face-diagonal supply the chiral grading `Γ_χ`? | 45/0 | **AVAILABLE-NOT-FORCED** — wider class, but selection of the `Γ_χ`-anticommuting operator stays open |

## Phase 2 (L1) — frame-clearing negative

A diagonal connection defined as the ordered product of NN connections along
a path carries **no new degree of freedom**: the face-diagonal two-path
holonomy difference equals the NN plaquette field strength `U_p` exactly
(machine precision), and body-diagonal six-path differences are transported
face plaquettes. Consequence: the gate-relevant content lives only at **L2**
(independent connections) or **L3** (distance-weighted), never at the free
L1 reading. This is essential framing — it means any gate-closing claim
*requires* the convention/physics commitment, and cannot be had for free.

## Phase 3 (√2-forcing) — the centerpiece negative

The load-bearing question of the whole build: is `|b|/a = 1/√2` (hence
`r = 1/2`) **forced** by the face-diagonal connection structure?

Six forcing candidates, computed explicitly:

| | Mechanism | Gives `1/√2`? | Verdict |
|---|---|---|---|
| F1 | Gaussian overlap `exp(-d²/2σ²)` | yes, with tuned `σ` | NATURAL |
| F2 | inverse-distance `1/d^p` | yes at `p=1`, `p` is a choice | NATURAL |
| **F3** | **`Z^3` lattice Green function (parameter-free)** | **NO — 0.641 ≠ 0.707** | **NO-√2** |
| F4 | geometric multiplicity | yes, with amplitude convention | NATURAL |
| F5 | spectral norm of the shift `C` | no — gives `r=1` (Born default) | NO-√2 |
| F6 | Clifford/`u(2)` γ-norm | re-encodes the metric, wrong sign (`r=2`) | NO-√2 |

**Forced count: 0 of 6.** The decisive computation: the actual nearest-neighbor
`Z^3` lattice Green function (momentum-space integral, validated to `4×10⁻⁸`
against the Watson value `G(0)=0.252731…` and the exact recurrence
`G(1,0,0)=G(0)−1/6`) gives a face-diagonal/NN propagator ratio of **0.641**,
not `1/√2 = 0.707`. The one parameter-free candidate — the one that could have
forced `√2` — contradicts it.

**The category mismatch is NOT defeated** (two independent runner-verified
reasons):
- **(CM-1)** The lattice supplies the discrete *length set* `{0, 1, √2, √3}`
  but not the *weighting function* `f`. Infinitely many lattice-native `f`
  hit `r = 1/2`; choosing inverse-first-power is itself a continuous input one
  level up.
- **(CM-2)** `r = 1/2` is *already* reachable by **pure discrete sector
  counting** — the equipartition factor is `|Z_3| − 1 = 2` non-trivial Fourier
  sectors, with no length at all. The length-squared `(√2)² = 2` and the
  sector-count `2` coincide *numerically* but are *structurally distinct*. So
  `√2` is a **second** length-based coincidence with the same value, not the
  unique continuous bridge the build hoped for.

Honest progress: `r = 1/2` becomes a **better-motivated convention** (the
generation orbit is a face-diagonal equilateral triangle of equal hops — an
appealing picture) but **not a closure**. It remains the Tier-A admitted input
`AC_φλ`. The open question is sharply relocated: *why this weighting rule* —
specifically why inverse-first-power, which the actual lattice propagator
contradicts.

## Phase 4 (color) — PARTIAL relocation

- The NN obstruction is **real and quantified**: the three hw=1 generation
  sites are mutually face-diagonal, so NN adjacency connects **zero** of the
  three pairs; the NN-connection algebra on the triplet is the abelian
  `u(1)³` (dim 3), strictly smaller than `u(3)` (dim 9). This *is* the
  qubit-link note's color obstruction.
- Face-diagonal adjacency makes all three pairs adjacent; pairwise `u(2)`
  closes to a **certified** `su(3) ⊕ u(1)` (real/antisymmetric structure
  constants, negative-definite Killing form, rank 2).
- **But the `su(3)` acts on the generation carrier, not the color carrier.**
  The framework's retained color `SU(3)` (`cl3_color_automorphism_theorem`)
  lives on the symmetric-base carrier; the two 3-dim spaces intersect in
  dimension 1 and carry **different `Z_3` characters** (generation regular
  `(3,0,0)` vs color-center `(3, 3ω, 3ω²)`). This is exactly the already-open
  `Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE` — the bridge is
  unbuilt.
- Body-diagonals add nothing (they connect hw=1↔hw=2, creating no 4th
  generation, leaving the hw=1 `u(3)` unchanged).

Verdict: face-diagonal **relocates** the color obstruction from "no `su(3)`
at all" to "`su(3)` on generation space, color identification still required"
— the same open color/generation gate. Not discharged.

## Phase 5 (chirality) — AVAILABLE-NOT-FORCED

- Operator-class map: `Sym(3,R)` (6-dim) = circulant-symmetric (2-dim, the
  no-go's domain) + non-circulant (4-dim, where chirality can live). The
  `{H, Γ_χ}=0` family is exactly 2-dim and **entirely non-circulant** — so
  the no-go and the `anticommuting ⇒ Q=2/3` result are two faces of one fact.
- **A readout subtlety the bare scout statement hid**: the `Z_2` grading
  available on a single face-diagonal coupling is `diag(1,−1,1)`, which is
  **NOT** the canonical `Γ_χ = (2/3)J − I`. Against it the eigenvector gives
  Koide **`Q = 1/2`, not `2/3`**. No pure off-diagonal face-diagonal coupling
  can anticommute with `Γ_χ` (that requires diagonal content `H_ii = 2h_i/3`).
- **Two incompatible `Q = 2/3` operators**: the Brannen `r = 1/2` route
  (Phase 3) gives `Q = 2/3` via a **circulant** operator that **commutes**
  with `Γ_χ` and carries **no chirality**; the `Γ_χ`-anticommuting route gives
  `Q = 2/3` via a **non-circulant** operator. The `√2` length supplies the
  former — which is *not* the chirality-admitting operator. So the chirality
  (S3) and `r=1/2` (S4) findings are reached by **mutually exclusive**
  operator classes.
- **No native principle forces the non-circulant selection**: cubic `O_h`
  permutes the 12 face-diagonals transitively (no preferred direction);
  `C_3`-symmetry selects circulant (back inside the no-go, `Q=1`); and the
  weak-parity grading `ε = (−1)^(x+y+z)` is uniform `−1` on the hw=1 orbit,
  so restricted to the generation triplet it is `−I` and cannot grade it.

Verdict: face-diagonal makes the chirality grading **available** (wider class,
no-go genuinely doesn't apply there) but the **selection** of the
`Γ_χ`-anticommuting operator remains the same `C_3`-orbit-splitting gate,
precisely relocated onto the face-diagonal class.

## Net assessment

The diagonal-connection thought experiment is a genuine and unusually
*coherent* idea — one geometric change (face-diagonal adjacency) is the right
*kind* of move, and it touches all three gates from a single structural
source. The honest finding is that it **relocates** all three rather than
closing any:

- **Color**: → the open color/generation `Z_3`-character bridge.
- **Chirality**: → the open `C_3`-orbit-splitting selection within the
  face-diagonal class.
- **`r = 1/2`**: → the open "why inverse-first-power weighting" question,
  with the parameter-free lattice-propagator candidate ruled out.

This is real progress of the *negative* kind the framework culture values:
it **rules out the diagonal-geometric route to `r = 1/2`** (the actual lattice
Green function settles it), and it sharpens each gate's true location. It does
**not** justify adopting an extended-adjacency convention (L2) or a
distance-weighted primitive (L3): neither closes a gate, and L3's weighting
function is exactly the unforced input.

## Recommendation

- **Do not** adopt the L2/L3 extended-adjacency convention on this evidence —
  no gate closes, and the `√2` weighting is not forced.
- **Do** record the negative as a frontier-narrowing result: future `r = 1/2`
  attacks should *not* pursue the diagonal-geometric length route (F3
  forecloses it); the live residual is the discrete sector-count reading
  (`|Z_3| − 1 = 2`) and the `det_C`/`det_R` measure-selection, which the
  prior panels already isolated and which the `√2` coincidence does **not**
  illuminate.
- **Keep** the appealing geometric picture (generation orbit = face-diagonal
  equilateral triangle) as expository context for `r = 1/2`, clearly labeled
  convention-not-derivation.

## What this build does NOT do

- It does **not** modify any axiom; `MINIMAL_AXIOMS_2026-06-04.md` is
  untouched.
- It does **not** claim any gate closed; all three verdicts are
  PARTIAL/relocation or NOT-FORCED.
- It does **not** weaken any retained no-go; the chirality no-go is correct on
  its circulant scope, and the build explicitly confirms it (Phase 5).
- It does **not** set audit status or import external comparators; `√2` and
  `r = 1/2` are compared structurally only.

## Cross-references (build artifacts on this branch)

- `DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md` (+ enumerator) — the four scout facts.
- `DIAGONAL_L1_WILSON_COMPOSITE_NEGATIVE_NOTE_2026-06-04.md` — L1 zero-DOF.
- `DIAGONAL_SQRT2_FORCING_R_HALF_DEEP_DIVE_NOTE_2026-06-04.md` — the √2-forcing centerpiece (NOT FORCED).
- `DIAGONAL_GATE_COLOR_L2_FACE_ALGEBRA_DEEP_DIVE_NOTE_2026-06-04.md` — color PARTIAL.
- `DIAGONAL_GATE_CHIRALITY_SELECTION_DEEP_DIVE_NOTE_2026-06-04.md` — chirality AVAILABLE-NOT-FORCED.
