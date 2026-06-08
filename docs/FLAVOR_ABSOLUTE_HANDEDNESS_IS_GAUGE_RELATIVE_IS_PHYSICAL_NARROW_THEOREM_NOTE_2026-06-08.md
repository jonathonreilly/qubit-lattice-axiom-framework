# Absolute Flavor Handedness Is Gauge; Magnitude and Relative-Orientation Readouts Remain Open

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a gauge classification / residual resolution)
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived after
independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_flavor_absolute_handedness_is_gauge.py`](../scripts/frontier_flavor_absolute_handedness_is_gauge.py)
**Cached log:**
[`logs/runner-cache/frontier_flavor_absolute_handedness_is_gauge.txt`](../logs/runner-cache/frontier_flavor_absolute_handedness_is_gauge.txt)
(TOTAL: PASS=17 FAIL=0)

## 0. The residual, and its resolution

A chain of companion results located the deepest charged-lepton flavor input as a single
global **handedness Z₂** — `sign(Δ)`, `Δ(p)=(p_0−p_1)(p_1−p_2)(p_2−p_0)` — that governs the
`S_3 → C_3` orientation and the sign of the Brannen phase `δ`, and is **odd under** the
spatial axis-swap reflection `R` while the time-arrow (breaking only `T`) cannot fix it
(companion `RK`-even result; context only, not a load-bearing link here). The
natural next move was to find the `R`-breaking that supplies the handedness — the staggered
axis-ordering being the candidate.

**The candidate dissolves the residual rather than supplying it.** The retained-bounded
[`STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23`](STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md)
proves the staggered `η`-ordering asymmetry is **pure `Z_2` gauge**: the physical
axis-symmetry on the `hw=1` triplet is the **full, unbroken `S_3`** (all six orderings
gauge-equivalent). So `R` (an orientation-reversing transposition in `S_3`) is an **unbroken
physical symmetry**. Two consequences pin the result:

1. The two orientations `+δ_*` and `−δ_*` are the **same masses, `R`-relabeled**:
   `√m_k(−δ) = √m_{−k}(+δ)`, identical sorted multiset (runner `M_*`).
2. `sign(Δ)` is **odd under** `R` (it carries the `S_3` sign rep).

An observable odd under an **unbroken** physical symmetry is **not gauge-invariant**.
Therefore **the absolute flavor handedness is gauge** — a labeling convention, not a missing
derivation. This note closes only that gauge classification. It also records two
`S_3`-invariant survivors that remain available for later physics bridges:
the magnitude `|Δ|` (with the operator-side identity `|δ| = 2/9 = L_3(1,2)`) and the
inter-sector relative sign `sign(Δ_1)·sign(Δ_2)`. This packet does **not** derive a physical
single-summand readout for `2/9` and does **not** identify the relative sign with a CKM/PMNS
CP or mixing observable. This answers the standing open
question of the
[`POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23.md)
("does the framework force a global handedness?") in the **negative**: it does not, and need
not — the handedness is gauge.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| staggered `η`-axis-ordering is `Z_2` gauge; physical axis-symmetry on the `hw=1` triplet is the full unbroken `S_3` | [`STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23`](STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | **load-bearing**: `R` is unbroken |
| the orientation `S_3` sign-rep = `Cl(3)` pseudoscalar; `+1` level set `= A_3 = C_3` | [`POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23.md), [`POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | the orientation object resolved here |
| the operator-side identity `2/9 = L_3(1,2)` (C₃ fixed-point density) | [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) | `retained_bounded` | invariant magnitude context; not a closed physical single-summand readout here |
| the generation count (number 3 = triplet dimension) | [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) | `retained` (corollary) | separate context, untouched |

No PDG value is load-bearing; PDG enters only the Section 4 comparator. No new axiom, import,
or vocabulary.

## 2. The gauge classification

On the firewalled cone (`Q = 2/3`, `r = 1/2`, held fixed), the Born record is `p_k(δ)`, and
the handedness is `sign(Δ(p))`.

**(M) The two orientations are the same physical masses.** `√m_k(−δ) = √m_{−k}(+δ)`, so the
sorted mass multiset at `+δ_*` and `−δ_*` is identical (runner `M_*`). `+δ_*` and `−δ_*`
differ only in the assignment of the three masses to the `C_3[111]` axis positions.

**(S) `R` is an unbroken physical symmetry.** The axis-swap transposition `R` lies in the
`S_3` axis-permutation group, which is **unbroken** on the staggered `hw=1` triplet: the
`η`-ordering asymmetry is pure `Z_2` gauge (all six orderings share the plaquette field
strength `−1` and trivial Polyakov holonomies, hence are gauge-equivalent — retained
`STAGGERED_AXIS_SYMMETRY_IS_S3`). `R` is orientation-reversing (`sgn(R) = −1`, a reflection;
the `A_3 = C_3` rotations have `sgn = +1`) (runner `S_*`).

**(G) Hence the absolute handedness is gauge.** `sign(Δ)` carries the `S_3` sign rep — odd
under every transposition (including `R`), even under `A_3` (runner `G_*`). Because `R` maps
the realized record to an equal-mass relabeling and `R` is an **unbroken** symmetry, the two
orientations are physically equivalent: `sign(Δ)` is **not** a gauge-invariant observable.
The absolute handedness is a **labeling convention**, not a derivable physical quantity.

**(P) The closed survivors are invariant candidates, not readout theorems.** What the
runner checks after the gauge classification:
- the **magnitude** `|Δ|` is invariant under `δ -> -δ`, and the separate operator-side
  identity `|δ| = 2/9 = L_3(1,2)` remains available as context;
- the **inter-sector relative orientation** `sign(Δ_1)·sign(Δ_2)` is `R`-invariant if a
  later multi-sector bridge supplies shared axes and a physical readout.

Those two facts are useful because they isolate the possible gauge-invariant data left after
absolute handedness is removed. They are not, in this note, a derivation that `2/9` is a
physical charged-lepton magnitude or that the relative sign is a CKM/PMNS CP or mixing
observable.

## 3. Scope — what this resolves and what it leaves

**Resolves:**
- The handedness residual (companion `RK`-even result): the `R`-breaking it sought is **not
  needed** — `R` is unbroken (retained `S_3`), so the absolute handedness is gauge.
- The POSITIVITY open question ("does the framework force a global handedness?"): **no**, and
  it need not — the orientation is a gauge labeling.

**Leaves (separate, untouched):**
- The physical single-summand readout of **magnitude** `|δ| = 2/9 = L_3(1,2)`. The
  operator-side identity is retained-bounded context; this note does not close the physical
  readout bridge.
- The **number of generations** (3 = triplet dimension): a separate physical/derived fact,
  **not** the gauge orientation — this note does not touch the count of generations.
- The **inter-sector relative orientations**: `R`-invariant candidates. Their identification
  with physical mixing / CP phases remains a multi-sector shared-axis/readout bridge target.
- The **`r = 1/2` cone** (`Q = 2/3`): firewalled, held fixed for all `δ`.

## 4. Honest verdict

Going after the `R`-breaking that would supply the flavor handedness resolved the residual
the other way: the staggered axis-ordering is **gauge** (retained `S_3` unbroken), so `R` is an
unbroken physical symmetry, and `sign(Δ)` — odd under `R` with the two orientations carrying
identical masses — is **not a gauge-invariant observable**. The "single deepest input" the
companion arc had located is therefore **not a missing derivation at all**: the absolute
flavor handedness is a gauge convention. The remaining work is not to choose an absolute
handedness, but to supply separate readout bridges for the invariant magnitude and for any
multi-sector relative orientation that is to become a physical CP/mixing observable.

## 5. No-Go Discipline Gate

**Status:** PASS for this bounded gauge classification. It says the **absolute** handedness is
gauge; it does **not** close the relative orientations as mixing/CP observables, does **not**
close `|δ| = 2/9` as a physical single-summand readout, and does **not** say the number 3 is
gauge.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| staggered `η` axis-ordering as `R`-breaker | RULED OUT | pure `Z_2` gauge; `S_3` unbroken (retained) |
| time-arrow as `R`-breaker | RULED OUT (companion) | breaks only `T`; handedness `RK`-even |
| absolute `sign(Δ)` as a physical observable | RULED OUT | odd under unbroken `R` ⇒ gauge |
| magnitude `|Δ|` / `|δ| = 2/9` | OPEN READOUT | `S_3`-invariant / operator-side context; physical single-summand bridge not closed here |
| inter-sector relative orientation | OPEN BRIDGE | `R`-invariant candidate; physical mixing/CP identification not closed here |

**N2 — Wall-independence.** Absolute orientation (gauge, this note), operator-side magnitude
`2/9`, the number 3, the relative orientations, and the `r=1/2` cone are independent objects;
this note resolves only the first.

**N3 — Hidden-wall scan.** The classification uses only the retained `S_3`-unbrokenness, the
`R`-relabeling of equal masses, and the `S_3` sign rep — no hidden chirality premise.

**N4 — Residual matching.** The object resolved is exactly the absolute handedness `sign(Δ)`.
The named open residual moves to readout bridges for invariant magnitudes and relative
orientations.

**N5 — Rhetoric audit.** The claim is gauge-ness of the **absolute** orientation, proven by
odd-under-unbroken-`R`; it is not a claim about relative orientations or the magnitude.

**N6 — Partial-closure path scan.** The genuine next targets are the physical
single-summand readout for the `2/9` magnitude and the multi-sector bridge that could
identify a relative orientation with a CP/mixing observable. No new axiom requested.

**N7 — Steelman.** A reviewer may argue some *other* framework structure (beyond the staggered
kinematics) breaks `R` and makes the absolute handedness physical. The candidate pseudoscalar
`ω = σ_1σ_2σ_3` is `R`-odd, but its **sign is itself the complex-structure convention** (gauge),
so it supplies no physical `R`-breaking; and the companion result rules out the arrow. If a
genuinely `R`-breaking (chiral) structure is later identified, the absolute handedness would
become physical — this note is explicit that the gauge verdict rests on the retained
`S_3`-unbrokenness.

**N8 — Cross-cycle echo.** Consistent with retained `STAGGERED_AXIS_SYMMETRY_IS_S3` (unbroken
`S_3`), the POSITIVITY notes (orientation sign-rep, open bridge — here resolved), and the
companion `RK`-even result (no arrow `R`-breaking) — connecting them without overruling any by
prose.

## 6. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained/retained-bounded rows
  plus the Brannen algebra.
- **No PDG/fitted load-bearing input** (PDG only in Section 4 comparator); **no forcing of
  `r = 1/2`**; **no new transcendental constant.**
- The companion `RK`-even note is named as context, not a citation-graph dependency.

## 7. Command

```bash
python3 scripts/frontier_flavor_absolute_handedness_is_gauge.py
```

Expected: `TOTAL: PASS=17 FAIL=0`. numpy + stdlib, deterministic, 3-vectors throughout
(memory-safe). The runner verifies the equal-mass `R`-relabeling, the `S_3` sign-rep character
of `sign(Δ)`, the gauge verdict (odd under unbroken `R`), the invariant-candidate status of
`|Δ|` and `sign(Δ_1)sign(Δ_2)`, the separate `L_3(1,2)` identity, the separate number 3, the
phase-blind `Q = 2/3` cone, and source-boundary text that leaves the physical readout bridges
open.
