---
claim_id: diagonal_sqrt2_forcing_r_half_deep_dive_note_2026-06-04
claim_type_author_hint: meta
---

# Diagonal-Connection √2 Forcing Deep Dive — Is r = 1/2 Derived From Substrate Geometry? (Phase 3)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** deep-dive analysis / thought-experiment surface (centerpiece of the
√2-centered diagonal-connection build)
**Claim type:** meta. This note does **not** find the √2 weighting forced; it
finds it *natural-but-not-forced*, with a named residual (the choice of
length-weighting rule). It therefore stays meta, not bounded_theorem. It sets
no audit status and changes no axiom.
**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/diagonal_sqrt2_forcing_r_half_deep_dive.py`](../scripts/diagonal_sqrt2_forcing_r_half_deep_dive.py)
(SUMMARY: PASS=34 FAIL=0).
**Cached log:**
[`logs/runner-cache/diagonal_sqrt2_forcing_r_half_deep_dive.txt`](../logs/runner-cache/diagonal_sqrt2_forcing_r_half_deep_dive.txt)
**Foundation:**
[`DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md`](DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md)
(scout fact **S4**: face-diagonal length √2 → |b|/a = 1/√2 → r = 1/2).

---

## §0 Why

The charged-lepton Brannen modulus `r = |b|^2/a^2 = 1/2` (equivalently Koide
`Q = 2/3` via the retained biconditional
[`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md))
is currently the single Tier-A admitted input `AC_φλ` on the charged-lepton
value chain
([`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)).
Every prior attack on `r = 1/2` converged on the same wall: **the framework
reaches discrete data but never the continuous modulus `r`** (a category
mismatch; 24-physicist panel, (α,β)-cone panel, K₀-real panel).

The foundation scout fact **S4** noticed that the discrete `Z^3` lattice
*does* supply one continuous datum that lands `r = 1/2` exactly: the
**face-diagonal Euclidean length √2**. The three hw=1 generation-orbit sites
`{(1,0,0),(0,1,0),(0,0,1)}` are mutually face-diagonal (squared distance 2;
scout **S1**), and a circulant hop weight `|b|/a = 1/√2` gives `r = 1/2`.

This note attacks the **load-bearing question** head-on: **is √2 forced**, so
that `r = 1/2` becomes *derived* from substrate geometry, or is it only
*natural*?

## §1 The question, stated precisely

On the hw=1 generation factor `C^3`, the charged-lepton Yukawa reduces (after
phase reduction) to the Brannen circulant

```text
Y = a I + b C + bbar C^2,   a in R, b in C,   C = forward 3-cycle,
```

with `r = |b|^2 / a^2` and the retained closure `r = 1/2 <=> Q = 2/3`
([`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)).

The "stay" weight `a` multiplies `I`; the "hop" weight `b` multiplies the
generation shift `C`, which is **one face-diagonal hop** on the hw=1 orbit.
The question:

> Does the qubit-link connection structure on a face-diagonal edge **force**
> the hop amplitude `|b|/a = 1/√2` (no free parameter), or is `1/√2` reached
> only by a *chosen* weighting rule (natural but tunable)?

We test six forcing candidates F1–F6. For each we ask: is the value `1/√2`
**fixed by the structure** (FORCED), reached only **with a tuned parameter or
convention** (NATURAL), or **not produced at all** (NO-√2)?

## §2 The six forcing candidates (explicit computation)

All numbers below are reproduced by the runner.

### F1 — Gaussian overlap (tight-binding orbital overlap)

A Gaussian-localized orbital of width `σ` gives hop/stay
`b/a = exp(-d_b^2/2σ^2) / exp(-d_a^2/2σ^2)`.

- Reference `a` = on-site (`d_a = 0`): `b/a = exp(-1/σ^2)`. This equals `1/√2`
  iff `σ^2 = 2/ln2 ≈ 2.885`.
- Reference `a` = NN (`d_a = 1`): `b/a = exp(-1/2σ^2)`, equal to `1/√2` iff
  `σ^2 = 1/ln2 ≈ 1.443`.

Neither required `σ` is a distinguished value, and `b/a` sweeps continuously
through `1/√2` as `σ` varies — `1/√2` is not singled out. **Verdict: NATURAL**
(a width exists, but `σ` is a free parameter tuned to the target).

### F2 — Inverse-distance power law `b ~ 1/d^p`

On-site reference (`d = 0`) diverges for any `p > 0`, so the natural reference
is NN (`d = 1`). Then `b/a = (√2)^{-p}/1^{-p} = 2^{-p/2}`:

| `p` | `b/a = 2^{-p/2}` | `r` |
|----|----|----|
| **1** | **0.707107** | **0.500000** |
| 2 | 0.500000 | 0.250000 |
| 3 | 0.353553 | 0.125000 |
| 4 | 0.250000 | 0.062500 |

Exactly `p = 1` (the `1/r` Coulomb/Newton law) gives `b/a = 1/√2 → r = 1/2`.
But `p` is a **choice** — the lattice does not select which power law weights
the hop. **Verdict: NATURAL** (inverse-first-power hits it; the power is an
input).

### F3 — The actual `Z^3` nearest-neighbor lattice Green function (PARAMETER-FREE)

This is the **load-bearing candidate**, because the lattice propagator is the
*unique parameter-free object* among the six: it is fixed once the NN `Z^3`
Laplacian is fixed, with no convention to choose. If the propagator ratio
between face-diagonal and NN sites were `1/√2`, that would be a genuine
forcing.

We compute the massless lattice Green function

```text
G(R) = (1/(2π)^3) ∫_{[-π,π]^3} cos(k·R) / (2 Σ_j (1 - cos k_j)) d^3k
```

numerically by a momentum-space midpoint grid that **avoids `k = 0`** (so the
integrable `1/k^2` singularity never lands on a node), with a two-point
Richardson extrapolation in the grid size `N ∈ {80,120,160,200}`.

**Method validation** (two independent exact cross-checks, both PASS):
- `G(0,0,0) → 0.2527311`, matching the exact Watson value `0.25273100986` to
  `4 × 10^{-8}`;
- `G(1,0,0) → 0.0860644`, matching the exact origin recurrence
  `6 G(0) − 6 G(1,0,0) = 1`, i.e. `G(1,0,0) = G(0) − 1/6 = 0.0860643`.

**Result:**

| pair | `G` | ratio to NN | target `1/√2` |
|----|----|----|----|
| on-site `G(0,0,0)` | 0.2527311 | — | — |
| NN `G(1,0,0)` | 0.0860644 | 1 | — |
| face-diag `G(1,1,0)` | 0.0551915 | **0.6413** | 0.7071 |
| body-diag `G(1,1,1)` | 0.0435784 | 0.5063 | (`1/√3` = 0.5774) |

The face-diagonal / NN propagator ratio is **0.6413, not `1/√2 = 0.7071`**
(off by ~9%); the implied `r = (0.6413)^2 = 0.411`, not `0.5`. The
body-diagonal / NN ratio is `0.5063`, not `1/√3` — the propagator obeys **no
clean inverse-length law**. **Verdict: NO-√2.** The one parameter-free
candidate that *could* have forced √2 does not.

### F4 — Geometric multiplicity (area/volume measure)

In the infinite cubic lattice an NN edge is shared by **4** unit cubes; a
face-diagonal (lying in one shared face) is shared by the **2** cubes meeting
at that face. The intensity ratio is `2/4 = 1/2` (→ `r = 1/4`); the
**amplitude** ratio under `amplitude = √intensity` is `√(2/4) = 1/√2`
(→ `r = 1/2`). So `1/√2` appears **only** under the amplitude-equals-square-
root-of-intensity convention; the square-root step is the (conventional)
choice. **Verdict: NATURAL.**

### F5 — Spectral / shift-operator norm

The shift `C` and identity `I` have **equal** Frobenius norm
(`‖C‖_F = ‖I‖_F = √3`) and equal operator norm (`1`, since `C` is unitary).
Equal-norm weighting gives `b/a = 1 → r = 1` — the **maximal-hierarchy /
det_R-Born default lane**, not `1/√2`. **Verdict: NO-√2** (the bare spectral
norm gives `r = 1`, the opposite endpoint).

### F6 — The qubit-link `u(2)` / Clifford connection structure

In `Cl(3,0) = M_2(C)` a displacement vector `v` maps to `γ(v) = Σ_i v_i σ_i`
with the Clifford relation `γ(v)^2 = |v|^2 I`. The face-diagonal displacement
`(1,1,0)` gives `γ(1,1,0)^2 = 2 I`, **recovering the squared length `2 =
(√2)^2`** exactly — but this is just the `Cl(3,0)` metric *being* the Euclidean
metric, i.e. √2 re-encoded, not new information. Worse, the **direction is
wrong**: the face-diagonal `γ`-vector is **larger** (`‖γ(1,1,0)‖_F = 2 =
√2·‖γ(1,0,0)‖_F`), so a connection amplitude tracking the `γ`-norm gives
`b/a = √2 → r = 2`, the inverse of what is needed. To get `b/a = 1/√2` the
length must enter **inversely** (a *decay* with distance) — which is precisely
F1/F2 with a chosen decay law. **Verdict: NO-√2** as a forcing (√2 appears
only by re-encoding the metric, and with the wrong sign).

### Verdict table

| candidate | mechanism | gives `1/√2`? | free parameter? | verdict |
|----|----|----|----|----|
| F1 | Gaussian overlap | yes | yes (width `σ`) | **NATURAL** |
| F2 | inverse-distance `1/d^p` | yes (`p=1`) | yes (power `p`) | **NATURAL** |
| F3 | **lattice Green function** | **no (0.641)** | **none** | **NO-√2** |
| F4 | geometric multiplicity | yes | yes (amp=√intensity) | **NATURAL** |
| F5 | spectral norm of `C` vs `I` | no (gives `r=1`) | none | **NO-√2** |
| F6 | Clifford `γ`-norm | only by re-encoding, wrong sign | none | **NO-√2** |

**Totals: FORCED = 0, NATURAL = 3, NO-√2 = 3.**

## §3 The category-mismatch defeat analysis (the crux)

The prior panels said: discrete axioms cannot pin a continuous modulus `r`.
The foundation's hope was that the **continuous** face-diagonal length
`√2 = |(1,1,0)|`, genuinely supplied by the discrete lattice, *defeats* this
wall. **It does not.** The mismatch reappears one level up, for two independent
reasons (both runner-verified):

**(CM-1) The lattice supplies lengths, not a weighting rule.** The lattice
hands us the discrete length *set* `{0, 1, √2, √3}`. It does **not** hand us
the function `f` that converts a length into an amplitude. Forming the
dimensionless `b/a = f(√2)/f(1)` requires choosing `f`, and **infinitely many
lattice-native `f` give `r = 1/2`**:

- `f(d) = d^{-1}` (inverse length) → `b/a = 1/√2`;
- `f(d) = exp(-(ln2/2) d^2)` (a Gaussian) → `b/a = 1/√2`;
- `f(d) = exp(-c d)` with `c = ln2/(2(√2−1))` (an exponential) → `b/a = 1/√2`.

All three use only `√2` and `1` — all equally "lattice-native". Selecting the
inverse-**first**-power (so that `r = 1/2` rather than `r = 1/4`, `1/8`, …) is
a **continuous input supplied by hand**, not by the substrate. The continuous
freedom the panels named has simply moved from "the value `r`" to "the
weighting rule `f` (and its power)".

**(CM-2) `r = 1/2` is already reachable with *zero* continuous input.** The
established L9 reading
([`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md);
the 2-orbit factorization
[`KOIDE_KAPPA_TWO_ORBIT_DIMENSION_FACTORIZATION_NOTE_2026-04-19`](KOIDE_KAPPA_TWO_ORBIT_DIMENSION_FACTORIZATION_NOTE_2026-04-19.md)
is *unaudited* on the current ledger, so it is cited only as a parallel
arithmetic picture, not as a load-bearing tier; the equipartition arithmetic
below is re-derived here directly and stands on its own)
is HS 2-sector equipartition `‖aI‖^2 = ‖bC + bbar C^2‖^2`. Computing the
norms: `‖aI‖^2 = 3a^2` and `‖bC + bbar C^2‖^2 = 6|b|^2 = 2·(3|b|^2)`, where the
factor **2** is the number of **non-trivial `Z_3` Fourier sectors**
(`C` and `C^2`), i.e. `|Z_3| − 1 = 2`. Equipartition then forces
`3a^2 = 2·3|b|^2 → r = 1/(|Z_3|−1) = 1/2`. This is **pure discrete sector
counting** — no length, no `√2`, no weighting rule. The framework *already*
reaches `r = 1/2` combinatorially.

**(CM-3) The two "2"s coincide numerically but not structurally.** The
length-squared `(√2)^2 = 2` and the sector count `|Z_3| − 1 = 2` are the same
number, which is *why* both routes land `r = 1/2`. But they are **structurally
distinct origins**: one is a continuous Euclidean datum, the other a discrete
counting fact. The √2-length story is therefore a **second, length-based
coincidence with the same value**, not the *unique continuous bridge* the wall
demanded. (Per the repo's own "no coincidences in frontier physics" reasoning,
this coincidence is suggestive of a real structural fact — but the structural
fact it points to is the **discrete** sector count `|Z_3| − 1 = 2`, which was
already known and already discrete, *not* a continuous derivation of `r`.)

**Conclusion of §3: the category mismatch is NOT defeated.** The continuous
datum √2 is real, but it does not close the gap: (a) the choice of
length-weighting `f` is itself the continuous input, and (b) `r = 1/2` is
already reachable by discrete counting, so √2 is not load-bearing for the
value.

## §4 Honest verdict

**MIXED, leaning NATURAL — NOT FORCED.**

- **No candidate FORCES √2** parameter-free in the right direction
  (FORCED = 0 of 6).
- The **one parameter-free candidate** — the actual `Z^3` lattice Green
  function (F3) — gives face-diagonal/NN = **0.641, not `1/√2`**. The lattice
  propagator does **not** select the √2 weight.
- The three candidates that **do** reproduce `1/√2` (F1 Gaussian, F2
  inverse-distance, F4 multiplicity) each require a **tuned parameter or a
  convention choice** (the width `σ`, the power `p`, or amplitude = √intensity).
- The remaining parameter-free structures (F5 spectral norm, F6 Clifford
  `γ`-norm) give `r = 1` or `r = 2` respectively — the **opposite** lanes — and
  F6's apparent √2 is only the Euclidean metric re-encoded.
- The **category mismatch is not defeated**: it reappears as the choice of
  weighting rule, and `r = 1/2` is independently reachable by pure discrete
  sector counting (`|Z_3| − 1 = 2`).

**Net effect on `GATE-R-HALF`:** the face-diagonal picture makes `r = 1/2` a
**better-motivated convention** — it supplies an appealing geometric *picture*
(the generation orbit is a face-diagonal triangle; equal-length hops; the
length √2 numerically coincides with the sector count) — but it is **not a
closure**. `r = 1/2` remains the Tier-A admitted input `AC_φλ`; this analysis
strengthens the *motivation* without discharging the *admission*.

This is progress of the honest kind: it **converts the open question into a
sharply located residual** — the weighting rule `f` (specifically, why the hop
amplitude should scale as the inverse-first-power of length, vs. the actual
lattice propagator which does not). Future attacks on `GATE-R-HALF` via the
diagonal surface should target *that* residual (a dynamical/variational
selection of `f`), not the bare length √2, which is now shown insufficient on
its own.

## §5 What this note does NOT do

- It does **not** find √2 forced and does **not** claim `r = 1/2` is derived.
  The verdict is natural-not-forced; `r = 1/2` stays the admitted `AC_φλ`.
- It does **not** modify any axiom. `MINIMAL_AXIOMS_2026-06-04.md` is untouched;
  the diagonal extension remains a thought-experiment surface, not adopted.
- It does **not** set audit status, promote any row, or weaken any retained
  no-go. The chirality no-go
  ([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md))
  and the isotype-split no-go
  ([`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md))
  remain correct on their scope; this note's NATURAL verdict is *consistent*
  with them (the isotype-split no-go says the singlet:doublet ratio is free,
  which is exactly the freedom in the weighting rule `f` found here).
- It does **not** import external comparators or PDG values. `√2` is a lattice
  geometric datum and `r = 1/2` is compared only structurally; the runner uses
  no measured mass.
- It does **not** claim the face-diagonal picture is *useless*: it is a genuine
  better-motivation (a geometric picture for `r = 1/2`), and it sharpens the
  residual. It simply does not rise to a forcing/closure.

## §6 Audit-lane handoff

- **Claim type:** meta. The √2 weighting is **natural-not-forced**; there is a
  named residual (the choice of length-weighting rule `f`), so this is not a
  bounded_theorem with a discharged value. The honest classification is meta,
  matching the foundation scoping note.
- **No status to set.** This note proposes no promotion. `r = 1/2` remains
  Tier-A `AC_φλ`. If the audit lane wishes to record the *better-motivation*
  (the geometric picture + the sector-count coincidence) as a support-tier
  annotation on the `AC_φλ` registry row, that is an audit-lane decision per
  the convention-adoption precedent
  ([`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv`](RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md));
  it is **not** asserted here.
- **Runner:** `scripts/diagonal_sqrt2_forcing_r_half_deep_dive.py`
  (PASS=34, FAIL=0), with two independent exact cross-checks validating the F3
  lattice Green function numerics (Watson `G(0)` and the `G(0)−1/6` recurrence).
- **Dependency posture:** depends only on the framework baseline (Brannen
  circulant structure, the hw=1 orbit geometry, the `Z^3` NN Laplacian) and on
  retained rows cited above as *context*. It load-bears on none of them and
  weakens none of them.

## Cross-references

- [`DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md`](DIAGONAL_SQRT2_FOUNDATION_SCOPING_NOTE_2026-06-04.md)
  — the scoping note and scout fact **S4** this note deepens.
- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) — the
  three-axiom baseline (untouched).
- [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
  — the qubit-link `u(2)` connection (F6 context).
- [`CHARGED_LEPTON_TWO_HIGGS_CANONICAL_REDUCTION_NOTE.md`](CHARGED_LEPTON_TWO_HIGGS_CANONICAL_REDUCTION_NOTE.md)
  — `Y_e = A_e + B_e·C` circulant reduction.
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  — the `AC_φλ` chain, the L9 equipartition reading (CM-2), and the `r = 1/2`
  admission this note does not discharge.
- [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
  — `r = 1/2 ⟺ Q = 2/3` biconditional.
- [`KOIDE_KAPPA_TWO_ORBIT_DIMENSION_FACTORIZATION_NOTE_2026-04-19.md`](KOIDE_KAPPA_TWO_ORBIT_DIMENSION_FACTORIZATION_NOTE_2026-04-19.md)
  — a parallel 2-sector dimension-factorization picture for CM-2 (currently
  *unaudited* on the ledger; cited only as picture, the CM-2 arithmetic is
  re-derived in this note and its runner).
- [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  — the singlet:doublet ratio is free (retained_no_go), consistent with the
  weighting-rule freedom found here.
