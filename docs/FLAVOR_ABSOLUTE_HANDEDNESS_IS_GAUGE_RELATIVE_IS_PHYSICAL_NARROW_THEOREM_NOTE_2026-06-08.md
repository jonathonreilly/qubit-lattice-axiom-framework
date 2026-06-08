# The Absolute Flavor Handedness Is Gauge — Only the Magnitude and Inter-Sector Relative Orientations Are Physical

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a gauge classification / residual resolution)
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived after
independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_flavor_absolute_handedness_is_gauge.py`](../scripts/frontier_flavor_absolute_handedness_is_gauge.py)
**Cached log:**
[`logs/runner-cache/frontier_flavor_absolute_handedness_is_gauge.txt`](../logs/runner-cache/frontier_flavor_absolute_handedness_is_gauge.txt)
(TOTAL: PASS=13 FAIL=0)

## 0. The residual, and its resolution

A chain of companion results located the deepest charged-lepton flavor input as a single
global **handedness Z₂** — `sign(Δ)`, `Δ(p)=(p_0−p_1)(p_1−p_2)(p_2−p_0)` — that governs the
`S_3 → C_3` orientation and the sign of the Brannen phase `δ`, and is **odd under** the
spatial axis-swap reflection `R` while the time-arrow (breaking only `T`) cannot fix it
(companion `RK`-even result, branch `science/flavor-handedness-rk-even-...`, plain text). The
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
derivation. The physical, `S_3`-invariant flavor data is the **magnitude** `|Δ|` (a function
of `|δ| = 2/9 = L_3(1,2)`, derived) and the **inter-sector relative orientation**
`sign(Δ_1)·sign(Δ_2)` (`R`-invariant — the mixing / CP phase). This answers the standing open
question of the
[`POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23.md)
("does the framework force a global handedness?") in the **negative**: it does not, and need
not — the handedness is gauge.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| staggered `η`-axis-ordering is `Z_2` gauge; physical axis-symmetry on the `hw=1` triplet is the full unbroken `S_3` | [`STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23`](STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | **load-bearing**: `R` is unbroken |
| the orientation `S_3` sign-rep = `Cl(3)` pseudoscalar; `+1` level set `= A_3 = C_3` | [`POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23.md), [`POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_ORIENTATION_SELECTS_C3_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | the orientation object resolved here |
| the magnitude `2/9 = L_3(1,2)` (C₃ fixed-point density) | [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) | `retained_bounded` | the physical magnitude |
| the generation count (number 3 = triplet dimension) | [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) | `retained` (corollary) | separate physical fact, untouched |

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

**(P) The physical content is `S_3`-invariant.** What survives:
- the **magnitude** `|Δ|` — a function of `|δ|`, with `|δ| = 2/9 = L_3(1,2)` the
  retained-bounded `C_3` fixed-point density (the physical, derived flavor number);
- the **inter-sector relative orientation** `sign(Δ_1)·sign(Δ_2)` — `R`-invariant, since `R`
  acts on the **shared** spatial axes of both sectors and flips both signs together (runner
  `P_relative_orientation_R_invariant`). This is where the physical **mixing / CP phase**
  lives.

So the absolute CP/handedness of a single sector is gauge; the relative (CKM/PMNS-type)
orientation is physical — **consistent with CP violation being a relative, not an absolute,
phenomenon.**

## 3. Scope — what this resolves and what it leaves

**Resolves:**
- The handedness residual (companion `RK`-even result): the `R`-breaking it sought is **not
  needed** — `R` is unbroken (retained `S_3`), so the absolute handedness is gauge.
- The POSITIVITY open question ("does the framework force a global handedness?"): **no**, and
  it need not — the orientation is a gauge labeling.

**Leaves (separate, untouched):**
- The **magnitude** `|δ| = 2/9 = L_3(1,2)` (the physical flavor number; derived, retained-bounded).
- The **number of generations** (3 = triplet dimension): a separate physical/derived fact,
  **not** the gauge orientation — this note does not touch the count of generations.
- The **inter-sector relative orientations** (mixing / CP phases): the physical, `S_3`-invariant
  flavor data not addressed here — the genuine open flavor target now that the absolute
  handedness is resolved as gauge.
- The **`r = 1/2` cone** (`Q = 2/3`): firewalled, held fixed for all `δ`.

## 4. Honest verdict

Going after the `R`-breaking that would supply the flavor handedness resolved the residual
the other way: the staggered axis-ordering is **gauge** (retained `S_3` unbroken), so `R` is an
unbroken physical symmetry, and `sign(Δ)` — odd under `R` with the two orientations carrying
identical masses — is **not a physical observable**. The "single deepest input" the companion
arc had located is therefore **not a missing derivation at all**: the absolute flavor
handedness is a gauge convention. The physical flavor content reduces cleanly to (i) the
firewalled cone `r = 1/2`, (ii) the derived magnitude `|δ| = 2/9 = L_3(1,2)`, (iii) the
generation number 3, and (iv) the inter-sector relative orientations (mixing / CP) — the last
being the genuine remaining open target, and exactly the data CP violation is built from.

## 5. No-Go Discipline Gate

**Status:** PASS for this bounded gauge classification. It says the **absolute** handedness is
gauge; it does **not** claim the relative orientations (mixing/CP) are gauge, that `|δ|` is
unphysical, or that the number 3 is gauge.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| staggered `η` axis-ordering as `R`-breaker | RULED OUT | pure `Z_2` gauge; `S_3` unbroken (retained) |
| time-arrow as `R`-breaker | RULED OUT (companion) | breaks only `T`; handedness `RK`-even |
| absolute `sign(Δ)` as a physical observable | RULED OUT | odd under unbroken `R` ⇒ gauge |
| magnitude `|Δ|` / `|δ| = 2/9` | PHYSICAL | `S_3`-invariant; `L_3(1,2)` (separate) |
| inter-sector relative orientation | PHYSICAL / OPEN | `R`-invariant; the mixing/CP phase |

**N2 — Wall-independence.** Absolute orientation (gauge, this note), magnitude `2/9`, the
number 3, the relative orientations, and the `r=1/2` cone are independent objects; this note
resolves only the first.

**N3 — Hidden-wall scan.** The classification uses only the retained `S_3`-unbrokenness, the
`R`-relabeling of equal masses, and the `S_3` sign rep — no hidden chirality premise.

**N4 — Residual matching.** The object resolved is exactly the absolute handedness `sign(Δ)`;
the named open residual moves to the **relative** orientations (mixing/CP).

**N5 — Rhetoric audit.** The claim is gauge-ness of the **absolute** orientation, proven by
odd-under-unbroken-`R`; it is not a claim about relative orientations or the magnitude.

**N6 — Partial-closure path scan.** The genuine next target is the inter-sector relative
orientations (mixing/CP phases), now isolated as the physical flavor data. No new axiom
requested.

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

Expected: `TOTAL: PASS=13 FAIL=0`. numpy + stdlib, deterministic, 3-vectors throughout
(memory-safe). The runner verifies the equal-mass `R`-relabeling, the `S_3` sign-rep character
of `sign(Δ)`, the gauge verdict (odd under unbroken `R`), the `S_3`-invariant magnitude and
`R`-invariant inter-sector relative orientation, the separate `L_3(1,2)` magnitude, the
separate number 3, and the phase-blind `Q = 2/3` cone.
