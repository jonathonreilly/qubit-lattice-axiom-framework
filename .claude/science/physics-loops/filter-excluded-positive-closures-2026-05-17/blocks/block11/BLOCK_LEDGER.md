# Block 11 Ledger: u_0 = <P>^{1/4} Plaquette-Quartic-Exponent Derivation

**Date:** 2026-05-17
**Branch:** `physics-loop/u0-plaquette-quartic-derivation-block11-2026-05-17`
**Lane:** yt tadpole improvement chain (continues blocks 08, 10)
**Status:** POSITIVE CLOSURE (bounded under named external admission `(P2)`)

## Target

Derive the **1/4 exponent** in `u_0 = <P>^{1/4}` (the Lepage-Mackenzie
tadpole-improvement constant definition) from a structural identity,
specifically: the four-link plaquette geometry plus the tree-level
mean-field unit-normalization principle. Previously, this exponent was
carried throughout the repo only as the defining convention of the
Lüscher-Mackenzie tadpole formula (cf.
`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10`
(T6) which treats `u_0 = P^(1/4)` as a parameterized substitution with
abstract positive `P`, and
`U0_SU2_BIVECTOR_IRREP_ANALYTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17`
which admits the fourth-root convention as named external `(X3)`).

## What is closed

The narrow theorem `(Q1)` establishes that, given:

- **(P1)** the elementary plaquette is the ordered product of exactly
  four gauge-link variables (`U_p = U_1 U_2 U_3 U_4`, geometric cubic
  incidence), and
- **(P2)** the tree-level mean-field unit-normalization principle
  defining `u_0` (named external admission, Lepage-Mackenzie 1993),

then the exponent **`1/4`** in `u_0 = <P>^{1/4}` is **forced** — not
chosen by convention — by the cubic loop length `L = 4` in `(P1)`
combined with the unit-mean condition `(P2b)`. The proof is two
algebraic steps:

```text
(S2)  U_p_dressed = U_p / u_0^4               (scalar factorization across L=4 links)
(S3)  <P_dressed> = <P> / u_0^4                (expectation, c-number factor out)
(S4)  <P_dressed> = 1     →     u_0^4 = <P>    (unit-mean principle (P2b))
(S5)  u_0 = <P>^{1/4}                          (unique positive fourth root)
```

## V1-V5 grounding

**V1 — Distinct from blocks 08, 10:**
- Block 08 (`YT_VERTEX_POWER_DERIVATION`) derived **`n_link = 2`** — the
  exponent of `u_0` in the coupling rescaling `alpha_s(v) = alpha_bare/u_0^2`.
- Block 10 (`ALPHA_S_TADPOLE_COUPLING_RESCALING_MAP_*_2026-05-17`)
  derived the coupling-rescaling **map** `M: alpha_bare → alpha_bare/u_0^2`.
- Block 11 (this) derives the **`1/4` exponent** in `u_0 = <P>^{1/4}` —
  the exponent in the *plaquette-to-u_0* map, not the *coupling-to-alpha_s*
  map. Three different exponents/maps in the same chain.

**V2 — A_min only:** uses only (i) elementary cubic-lattice incidence
(`(P1)`) and (ii) the named external admission of the Lepage-Mackenzie
mean-field principle (`(P2)`). No additional axioms.

**V3 — No PDG / no fitted u_0:** the derivation is purely algebraic.
`<P>` and `u_0` are abstract positives throughout the proof and runner.
Numerical scan in Part 9 uses 10 abstract test points (including 0.5934
as a test value, explicitly marked non-load-bearing).

**V4 — Not a relabeling of an existing landed cycle:** the exponent
`1/4` was previously carried only as part of the defining convention of
`u_0` (e.g., `(T6)` of the vertex-power note treats it as a
parametrized substitution; `(X3)` of the SU(2) bivector note admits it
as external). No prior repo note derives the `1/4` itself.

**V5 — Honest bounded scope:** the principle `(P2)` itself remains
external (a textbook lattice QCD convention), and the numerical `<P>`
evaluation remains in its own bounded chain. The note carries
`bounded_theorem` author tier and the source-note honesty preamble
flags status authority to the independent audit lane.

## Deliverables

1. **Source theorem note:**
   `docs/U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md`
   (≈ 290 lines)
2. **Runner:**
   `scripts/frontier_u0_plaquette_quartic_derivation.py`
   (≈ 380 lines, 36 checks, all pass; Pattern A class)
3. **Cached output:**
   `logs/runner-cache/frontier_u0_plaquette_quartic_derivation.txt`
4. **Block artifacts:** this directory.

## Runner scorecard

```
Block:                u0-plaquette-quartic-derivation-block11
Date:                 2026-05-17
Audit-lane class:     A (Pattern A narrow algebraic)
Theorem type:         bounded_theorem (positive closure)

Total checks:         36
Passed:               36
Failed:               0

STATUS:               ALL CHECKS PASS
Honest closure:       1/4 exponent in u_0 = <P>^{1/4}
                      DERIVED from L=4 (cubic plaquette) + (P2).
External admission:   (P2) tree-level mean-field unit-norm principle.
Open downstream:      numerical <P> evaluation (separate chain).
```

## Coverage map

| Part | Checks | Content |
|------|--------|---------|
| 1 | 8 | `(S1)–(S5)`, `(Q1)`: algebraic chain + exponent-forced |
| 2 | 2 | `(Q-C1)`: loop-length scaling generalization |
| 3 | 5 | `(Q-C2)`, `(Q-C3)`: counterfactual L=3, 5, 6 |
| 4 | 2 | `(Q-C4)`: free-action boundary |
| 5 | 1 | `(Q-C5)`: forward chain into vertex-power `(T6)` |
| 6 | 1 | `(Q-C6)`: inverse algebra (dressed = 1) |
| 7 | 3 | `(Q-C7)`: monotone calibration + 2 concrete tests |
| 8 | 2 | Roundtrip dressed-identity ↔ closed-form |
| 9 | 4 | Numerical parametric scan + counterfactual numeric |
| 10 | 8 | Forbidden-imports check |
| **Total** | **36** | **all pass** |

## Three-note synthesis (companion structure)

Block 11's closure completes a three-note clustering on the structural
contents of the Lepage-Mackenzie tadpole-improvement chain:

| Note | Derives | Admits |
|------|---------|--------|
| `ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10` | algebraic identities `(T1)–(T6)` on `(alpha_bare, u_0)` | the `1/u_0` per-link convention |
| `U0_SU2_BIVECTOR_IRREP_ANALYTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17` | `N_SU(2) = 2` from Cl(3) bivector irrep | the `1/4` exponent (as `(X3)` external) |
| `U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17` (this) | the `1/4` exponent from cubic loop + unit-mean principle | the unit-mean principle `(P2)` itself |

Each note isolates a distinct structural step. None derives the
principle `(P2)` itself (which would be a separate row), and none
derives a numerical `<P>` value (separate bounded chain).

## Forbidden-imports compliance

- ✅ No PDG observed `u_0`.
- ✅ No PDG observed `<P>`.
- ✅ No lattice Monte Carlo value load-bearing.
- ✅ No fitted u_0.
- ✅ No specific gauge group (works for any N ≥ 1 abstract).
- ✅ No dependency on Block 08 (n_link = 2) or Block 10 (M map).
- ✅ No dependency on SU(2) bivector irrep sister note.
- ✅ A_min only.

## Time budget actuals

| Phase | Budget | Actual |
|-------|--------|--------|
| Ground | ~15 min | ~15 min |
| V1-V5  | ~10 min | ~10 min |
| Build  | ~50 min | ~45 min |
| Total  | ~75 min | ~70 min |
