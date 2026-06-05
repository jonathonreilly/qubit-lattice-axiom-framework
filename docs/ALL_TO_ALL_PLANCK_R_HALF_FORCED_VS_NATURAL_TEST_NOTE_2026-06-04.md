---
claim_id: all_to_all_planck_r_half_forced_vs_natural_test_note_2026-06-04
claim_type_author_hint: meta
---

# All-to-All Qulink + Planck-Minimum — Does It FORCE the Equal-Power Measure (r = 1/2)? Forced-vs-Natural Adjudication

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the canonical
> source-of-truth doc.

**Date:** 2026-06-04
**Type:** adjudication / measure-realization analysis (companion to the
√2-centered diagonal-connection build on the sister branch)
**Claim type:** meta. This note does **not** find the all-to-all sum forced; it
finds the value `r = 1/2` reproduced only by a **tuned weighting law** (the
inverse-first-power law at a unit cutoff), with the **parameter-free** all-to-all
coupling (the lattice propagator) giving `r ≈ 0.41`, missing both idealized
measures and landing nearest the Born side. It therefore stays meta, not
bounded_theorem. It sets no audit status and changes no axiom.
**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/all_to_all_planck_r_half_forced_vs_natural_test.py`](../scripts/all_to_all_planck_r_half_forced_vs_natural_test.py)
(SUMMARY: PASS=40 FAIL=0).
**Cached log:**
[`logs/runner-cache/all_to_all_planck_r_half_forced_vs_natural_test.txt`](../logs/runner-cache/all_to_all_planck_r_half_forced_vs_natural_test.txt)

---

## §0 Why

The charged-lepton Brannen modulus `r = |b|^2/a^2 = 1/2` (equivalently Koide
`Q = 2/3` via the retained biconditional
[`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md))
is currently the single Tier-A admitted input `AC_φλ` on the charged-lepton
value chain
([`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)).
That chain's §"structure/value split" records the precise residual: the
**equal-power-per-block** (det_C / block-counting) measure selects `r = 1/2`
within the 2-block structure, whereas the **Born/dimension** (det_R) measure
selects `r = 1`. The open question is whether anything in the framework's
geometry **forces** the equal-power measure rather than just **coinciding** with
its value.

Three workers explored the idea that **extended (non-nearest-neighbor)
adjacency closes this gate**:

- Two **diagonal** workers (single face-diagonal length `√2`, and a 6-phase
  sweep) concluded geometry supplies the `(1,2)`/Born/**dimension** measure
  → `r = 1`, **not** the equal-power/block-counting measure → `r = 1/2`. Their
  decisive computation: the actual `Z^3` lattice Green function between
  face-diagonal sites is **0.641**, not `1/√2 = 0.707`; and `r = 1/2` is already
  reachable by **pure discrete sector counting** `|Z_3| − 1 = 2` (numerically
  coincident with `(√2)^2 = 2` but structurally distinct). See the sister-branch
  `DIAGONAL_SQRT2_SYNTHESIS_VERDICT_NOTE_2026-06-04` and
  `DIAGONAL_SQRT2_FORCING_R_HALF_DEEP_DIVE_NOTE_2026-06-04` (verdict: NATURAL,
  **not** FORCED).
- A **third** worker explored a *different* model: every site connects to every
  other via a qulink, distance-weighted with a minimum length = Planck =
  lattice spacing. That worker claimed `r = 1/2` is **forced** in this
  all-to-all model.

**This note adjudicates the third worker's "forced" claim** against the same
hostile forced-vs-natural standard the diagonal workers applied. The verdict is
**TUNED-LAW**: the all-to-all "forced" claim is the same natural-vs-forced
conflation, now at the all-to-all level.

## §1 The model and the C_3 projection convention

The three generations are the `hw = 1` BZ-corner orbit
`{e1=(1,0,0), e2=(0,1,0), e3=(0,0,1)}`
([`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)),
mutually face-diagonal (pairwise squared distance 2). The Brannen circulant
`Y = a I + b C + b̄ C^2` (`C` = forward 3-cycle) lives on this `C^3` generation
factor, with `r = |b|^2/a^2` and the retained closure `r = 1/2 ⟺ Q = 2/3`
([`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)).

**The all-to-all coupling.** Every ordered lattice pair `(x, y)` carries a
connection weighted by `w(|x − y|)`, with a short-distance cutoff: the minimum
distance is the lattice spacing `a_Planck = 1` (this regularizes the `d → 0`
divergence of inverse-power laws).

**The C_3 generation action on Z^3** (stated precisely, the natural one, **not**
hand-picked): the generation 3-cycle `e1 → e2 → e3 → e1` is realized on `Z^3` by
the cyclic coordinate permutation `ρ(x1,x2,x3) = (x3,x1,x2)`, an order-3 lattice
**isometry** fixing the `(t,t,t)` axis. (Runner Part F-a verifies `ρ^3 = id`,
`ρ` preserves Euclidean length, and `ρ` cycles the three corners.)

**The projection (honest, no phase hack).** Give each generation slot `s` a
lattice wavefunction `ψ_s` with the C_3 covariance `ψ_{s+1} = ρ · ψ_s` (so the
three slots are a genuine `ρ`-orbit). The generation `3×3` coupling matrix is the
overlap through the all-to-all kernel,

```text
M[s,t] = Σ_{x,y} conj(ψ_s(x)) · w(|x − y|_floored) · ψ_t(y),
```

which is **automatically circulant** because `W` is translation-invariant and
`ρ` is a lattice isometry (runner Part F-b verifies exact circulancy for both
slot choices). We read off

```text
a = M[0,0]   (stay  = the C_3-invariant diagonal amplitude),
b = M[0,1]   (hop   = the C_3 forward-shift amplitude, = "the sum of weights for
                      all connections effecting the C_3 forward shift").
```

Two natural slot-wavefunction choices, both tested:

- **W-delta:** `ψ_s = δ` at corner `e_{s+1}`. Then `M[s,t] = w(|e_s − e_t|)`
  exactly: diagonal `= w(cutoff)` (regularized self-term), off-diagonal
  `= w(√2)`. This is the **literal generation-triangle reading**, and it
  **coincides with the diagonal worker's F2 object** `b/a = w(√2)/w(cutoff)`.
- **W-spread:** `ψ_s` = the C_3-covariant symmetric Gaussian-of-the-corner
  spread over a neighborhood — the genuinely "every site participates"
  all-to-all reading the third worker intends.

The projection convention is stated and verified, not chosen to land 1/2.

## §2 Part A — the all-to-all sum and its convergence

**W-delta, reference law `w = 1/d`, cutoff = 1:** `a = w(1) = 1`,
`b = w(√2) = 0.7071`, so `b/a = 1/√2` and `r = 0.5000` exactly. This is the
diagonal-F2 `p = 1` value: the bare-orbit all-to-all reading **is** the diagonal
inverse-first-power object.

**W-spread, `1/d`, cutoff = 1, varying the smear width:**

| smear `σ` | a | b | b/a | r |
|---:|---:|---:|---:|---:|
| 0.4 | 1.600 | 1.123 | 0.702 | 0.493 |
| 0.7 | 10.150 | 8.109 | 0.799 | 0.638 |
| 1.0 | 22.645 | 19.708 | 0.870 | 0.757 |
| 1.5 | 39.018 | 35.632 | 0.913 | 0.834 |
| 2.0 | 44.851 | 41.467 | 0.925 | 0.855 |

The all-to-all sum **converges** for each fixed convention (the lattice box sum
stabilizes; the `1/d` slot overlaps are finite once the cutoff regularizes the
`d → 0` term). But **smearing the slots moves `r` continuously from ≈0.49 up to
≈0.86** — the all-to-all structure does **not** pin `r` at any fixed value
independent of the smear convention. The hop `b` stays nonzero throughout
(runner F-c), so smearing does not annihilate the hop; it simply **retunes** it.

## §3 Part B — THE DECISIVE QUESTION: which measure does the sum realize?

`r = 1/2` can come from two structurally different sources: the **equal-power /
block-counting measure** (det_C, `3a^2 = 6|b|^2` → `r = 1/2`) or a **tuned
weighting law** that happens to hit 1/2 on the **dimension/Born measure** (det_R,
`r = 1` generically). The decisive discriminator: **the equal-power measure is
LAW-INVARIANT** (it weights the singlet and doublet isotypes equally regardless
of any distance law), whereas a tuned-law route is **LAW-DEPENDENT**.

**The singlet/doublet power ratio the all-to-all sum distributes, across laws**
(W-delta; equal-power would hold this at 1.0 for **all** laws):

| law | doublet/singlet power | r |
|---|---:|---:|
| `1/d` | 1.000 | 0.500 |
| `1/d^2` | 0.500 | 0.250 |
| `exp(−d)` | 0.873 | 0.437 |
| Gaussian `σ=1` | 0.736 | 0.368 |
| Yukawa `m=0.5` | 0.661 | 0.330 |

The ratio **varies by 0.50 across five laws** (equal-power would give spread 0).
**The all-to-all sum does NOT realize the law-invariant equal-power measure; it
distributes whatever isotype power the chosen law dictates.** At `1/d` the
singlet and doublet powers happen to come out equal — but that equality is a
**consequence** of `b/a = 1/√2` (it is the *definition* of `r = 1/2`), not a
*cause*: the sum did not weight the two isotypes equally by structure, it just
landed on the equal point for that one tuned law. The smeared (W-spread) version
gives doublet/singlet `= 1.51` at `1/d` (runner B3) — also not pinned to 1.

**Structural statement (Part F-d).** The det_C measure is the **block-count**
(weights `(1,1)` on the two minimal central idempotents of `R[Z_3] = R ⊕ C`) →
`r = 1/2`; the det_R measure is the **dimension count** (weights `(1,2)`) →
`r = 1`. A distance-weighted sum is **neither** block-count nor dimension-count;
it is a third object whose value is set by the law, coinciding with one of them
only at a tuned parameter. The parameter-free all-to-all `r ≈ 0.41` (§5) matches
**neither** 0.5 nor 1.0.

**Part-B finding: BORN-NOT-EQUAL-POWER at the structural level.** The sum does
not realize the equal-power measure; its isotype-power split is law-set, and its
parameter-free value sits on the Born side of 1/2, not at the equal-power point.

## §4 Part C — universality sweep (forced vs tuned)

`r` as a function of the weighting law (W-delta, cutoff = 1):

```text
power laws 1/d^p :  p=0.5 -> 0.707 ; p=1.0 -> 0.500* ; p=1.5 -> 0.354 ;
                    p=2.0 -> 0.250 ; p=3.0 -> 0.125
exponential exp(-d/λ): λ=0.5 -> 0.191 ; λ=1 -> 0.437 ; λ=2 -> 0.661 ; λ=5 -> 0.847
Gaussian exp(-d^2/2σ^2): σ=0.5 -> 0.018 ; σ=1 -> 0.368 ; σ=1.2 -> 0.499* ; σ=2 -> 0.779
Yukawa exp(-m d)/d: m=0 -> 0.500* ; m=0.5 -> 0.330 ; m=1 -> 0.218 ; m=2 -> 0.095
```

`r` ranges over **[0.018, 0.847]** across the sweep; **exactly 3 of 17 law-points
hit `r = 1/2`** (`1/d`, a tuned Gaussian `σ≈1.2`, massless Yukawa = `1/d`). This
is **NOT a plateau** — it is a set of **isolated single crossings**. The smeared
(W-spread) sweep likewise varies (`r ∈ [0.52, 0.76]` across laws, runner C). 

**Part-C result: SINGLE CROSSING (tuned), not a plateau.** `r = 1/2` appears only
at the inverse-first-power law (and its few coincidental law-equivalents), not
across a wide class. By the diagonal workers' standard this is the same status as
their F2: NATURAL/tuned, not forced.

## §5 Part D — the Planck-minimum role

Varying the cutoff (Planck-min, in lattice units) for `w = 1/d`, W-delta:

| cutoff | a = w(cutoff) | b = w(√2) | r |
|---:|---:|---:|---:|
| 0.25 | 4.000 | 0.707 | 0.031 |
| 0.50 | 2.000 | 0.707 | 0.125 |
| **1.00** | **1.000** | **0.707** | **0.500** |
| 1.50 | 0.667 | 0.667 | 1.000 |
| 2.00 | 0.500 | 0.500 | 1.000 |

`r` **depends on the cutoff** (`r = (cutoff/√2)^2` while `cutoff ≤ √2`; once
`cutoff ≥ √2` the hop floors to the stay value and `r → 1`, the no-hierarchy
Born endpoint). So the Planck cutoff is **not a passive regulator** — it
co-determines `r` together with the law.

**The one genuinely notable alignment, stated honestly.** `r = 1/2` occurs at
`cutoff = 1 = lattice spacing` **for the `1/d` law specifically**. This is an
appealing structural coincidence (the Coulomb/Newton `1/r` law + a Planck-minimum
equal to the lattice spacing land exactly on the equipartition point). But it is
a **double tuning, not a forcing**: at `cutoff = 1` a different law (`1/d^2`)
gives `r = 0.25`, not 1/2 (runner D), so the cutoff alone supplies no forcing —
**both** the `1/d` law **and** the unit cutoff must be chosen. The Planck cutoff
supplies a regulator and an evocative numerical alignment, **not** independent
measure data.

## §6 Part E — the category-mismatch hostile check (reused CM-1/CM-2/CM-3)

- **CM-1 (the law is the free input).** The lattice hands a discrete length
  *set* `{0, 1, √2, √3, …}`, **not** a weighting function. Forming
  `b/a = w(√2)/w(1)` still requires choosing `w`, and **infinitely many distinct
  lattice-native `w` give `r = 1/2`** — `1/d`, a tuned Gaussian, and a tuned
  exponential all do (runner E/CM-1). The all-to-all sum does **not** pick the
  law; the law is the free continuous input one level up. Mismatch **not
  defeated**.
- **CM-2 (already discrete).** `r = 1/2` is **already** reachable by pure
  discrete sector counting `r = 1/(|Z_3| − 1) = 1/2` with **zero** continuous
  input (no length, no law). The all-to-all 1/2 (when it appears, at the tuned
  law) is **numerically the same sector-count value** — a *second* coincidence
  with the discrete value, not a new continuous bridge to the equal-power
  measure.
- **CM-3 (the parameter-free anchor — DECISIVE).** The **unique parameter-free**
  all-to-all coupling is the lattice Green function itself (no decay law chosen).
  Re-running the diagonal workers' validated `Z^3` Green-function routine
  (`G(0,0,0) = 0.2527311`, matching the exact Watson value to `4×10^{-8}`):

  ```text
  facediag/NN propagator ratio = 0.6413   (target 1/√2 = 0.7071)
  implied r = (0.6413)^2 = 0.4112         (target 1/2 = 0.5)
  ```

  The parameter-free all-to-all coupling gives **0.641, not 1/√2** → implied
  **`r ≈ 0.41`, not 1/2**, exactly the diagonal F3 verdict. The all-to-all sum
  **does not force `r = 1/2`** parameter-free, and its parameter-free value sits
  **below** 1/2 (the Born side, `r < 1/2 < 1`), nearer Born than equal-power.

## §7 Honest verdict — TUNED-LAW (Born-leaning parameter-free anchor)

**The all-to-all "forced" claim is the same natural-vs-forced conflation the
diagonal workers flagged, now at the all-to-all level.** Of the three honest
outcomes:

- **NOT** FORCED-EQUAL-POWER: `r = 1/2` is **not** universal across laws (spread
  0.83, three isolated crossings), and the sum's isotype-power split is
  **law-dependent** (Part B), so it does **not** structurally realize the
  equal-power (det_C) measure.
- **TUNED-LAW (the verdict):** `r = 1/2` is reproduced **only** for the tuned
  inverse-first-power law at a unit (= lattice-spacing) cutoff — the same single
  tuned coincidence as the diagonal F2, with the cutoff a co-tuned second knob.
- **BORN-leaning anchor:** the **parameter-free** all-to-all coupling (the
  lattice propagator) gives `r ≈ 0.41`, missing **both** idealized measures and
  landing on the **Born side** of 1/2 — directly corroborating the diagonal
  workers' "geometry gives the wrong measure" finding.

**Net effect on `GATE-R-HALF`:** the all-to-all picture does **not** discharge
the `AC_φλ` admission. Like the diagonal picture it offers an evocative
*motivation* (here: the Coulomb `1/d` law with a Planck-minimum equal to the
lattice spacing lands on the equipartition point), but the motivation rests on a
**double-tuned convention** (the law **and** the cutoff), and the unique
parameter-free object misses 1/2. The residual is unchanged and sharply located:
**why the inverse-first-power weighting** (and why the cutoff at exactly the
lattice spacing) — a dynamical/variational selection of the law, which the
substrate geometry does not supply. All three workers (two diagonal + this
all-to-all adjudication) **converge**.

## §8 What this note does NOT do

- It does **not** find the all-to-all sum forced and does **not** claim
  `r = 1/2` is derived. The verdict is TUNED-LAW; `r = 1/2` remains the Tier-A
  admitted input `AC_φλ`.
- It does **not** modify any axiom. `MINIMAL_AXIOMS_2026-06-04.md` (Lattice /
  Quantum / Record) is untouched; the all-to-all coupling and the Planck-minimum
  are a thought-experiment surface, **not** adopted as a primitive.
- It does **not** set audit status, promote any row, or weaken any retained
  no-go. The isotype-split no-go
  ([`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md),
  retained_no_go — the singlet:doublet ratio is free) and the chirality no-go
  ([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md))
  remain correct on their scope; this note's TUNED-LAW verdict is **consistent**
  with the isotype-split no-go (the "free singlet:doublet ratio" is precisely the
  free weighting-law/cutoff found here).
- It does **not** import external comparators or PDG values. `√2` and `r = 1/2`
  are lattice/structural data; the runner uses **no** measured mass. The
  geometric face-diagonal/NN propagator ratio is computed from the bare `Z^3`
  Laplacian.
- It does **not** claim the all-to-all picture is useless: the `1/d` + unit-cutoff
  alignment is a genuine evocative motivation and sharpens the residual. It
  simply does not rise to a forcing/closure.
- It does **not** re-derive the diagonal workers' settled results; it reuses their
  validated Green-function routine for an apples-to-apples parameter-free
  comparison and confirms the same anchor (0.641, not 0.707).

## §9 Audit-lane handoff

- **Claim type:** meta. The all-to-all weighting is **tuned-not-forced**; there
  is a named residual (the choice of weighting law **and** the cutoff scale), so
  this is not a bounded_theorem with a discharged value. The honest
  classification is meta, matching the sister-branch diagonal deep-dive.
- **No status to set.** This note proposes no promotion. `r = 1/2` remains
  Tier-A `AC_φλ`. If the audit lane wishes to record the *better-motivation*
  (the `1/d` + Planck-minimum = lattice-spacing alignment) as a support-tier
  annotation on the `AC_φλ` registry row, that is an audit-lane decision per the
  convention-adoption precedent
  ([`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv`](RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md));
  it is **not** asserted here.
- **Runner:**
  [`scripts/all_to_all_planck_r_half_forced_vs_natural_test.py`](../scripts/all_to_all_planck_r_half_forced_vs_natural_test.py)
  (PASS=40, FAIL=0), with the F3/CM-3 lattice Green function validated against the
  exact Watson `G(0)` value and the `G(0) − 1/6` origin recurrence (same
  cross-checks as the diagonal deep-dive runner).
- **Dependency posture:** depends only on the framework baseline (Brannen
  circulant structure, the `hw = 1` orbit geometry, the `Z^3` Laplacian) and on
  retained rows cited above as *context*. It load-bears on none of them and
  weakens none of them. It does not load-bear on
  `closure_c_staggered_dirac_gate` or any open-gate output.

## Cross-references

- Sister branch `codex/diagonal-sqrt2-r-half-2026-06-04`:
  `DIAGONAL_SQRT2_SYNTHESIS_VERDICT_NOTE_2026-06-04.md` and
  `DIAGONAL_SQRT2_FORCING_R_HALF_DEEP_DIVE_NOTE_2026-06-04.md` — the diagonal-level
  NATURAL-not-FORCED finding (lattice Green function 0.641 ≠ 0.707; CM-1/CM-2)
  whose hostile standard this note applies, and whose F3 routine this note reuses.
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  — the `AC_φλ` chain, the equal-power-vs-dimension measure fork (the
  structure/value split), and the `r = 1/2` admission this note does not
  discharge.
- [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
  — the `r = 1/2 ⟺ Q = 2/3` biconditional and the `κ = a²/|b|²` structure.
- [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  — retained_no_go: the singlet:doublet (equal-power vs Born) ratio is free,
  consistent with the weighting-law/cutoff freedom found here.
- [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  — the `hw = 1` generation orbit `{e1, e2, e3}` the C_3 projection acts on.
- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) — the Lattice /
  Quantum / Record axiom baseline (untouched).
- [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the endpoint biconditional `Q = 2/3 ⟺ r = 1/2`.
