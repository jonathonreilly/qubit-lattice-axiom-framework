# Charged-lepton masses from the pinned shape (r=1/2, theta=2/9) plus one scale

**Date:** 2026-06-05
**Claim type:** theorem (dimensionless ratio reproduction is exact-modulo-imports)
**Primary runner:** [`scripts/cl3_lepton_masses_from_pinned_shape_2026_06_05.py`](../scripts/cl3_lepton_masses_from_pinned_shape_2026_06_05.py)
**Cache:** [`logs/runner-cache/cl3_lepton_masses_from_pinned_shape_2026_06_05.txt`](../logs/runner-cache/cl3_lepton_masses_from_pinned_shape_2026_06_05.txt)

## Purpose

Forward-derivation question: do the three charged-lepton masses
`m_e, m_mu, m_tau` fall out of the framework's *doubly pinned* generation
shape (`r = 1/2`, `theta = 2/9`) plus a *single* overall scale `a`? And is
that one scale pinnable, or free?

The generation mass operator is the `C_3` circulant with sqrt-mass
eigenvalues

```text
lambda_k = a * [ 1 + 2 sqrt(r) cos(theta + 2 pi k / 3) ],   k = 0, 1, 2,
m_k      = lambda_k^2.
```

The framework pins the **shape** twice:

- `r = 1/2` (swap-symmetric / Koide `Q = 2/3`), so `2 sqrt(r) = sqrt(2)`;
- `theta = 2/9` rad (the Brannen phase `= (N-1)/N^2` at `N=3`).

Hence the *dimensionless* spectrum `m_e : m_mu : m_tau` is **fixed with no
free parameter**, and the absolute masses are that fixed shape times the
single scale `a` (equivalently `a^2` in mass units).

This note records exactly what follows. It is a forward, honest accounting,
not a new derivation of the two shape pins: those remain the established
`AC_phi_lambda` Tier-A import on origin/main, and the scale remains the
units-only `scale_reference_primitive`. Nothing is promoted, no PDG value is
load-bearing for the shape, and no axiom is added.

## T1 — Dimensionless spectrum from the pinned shape (no fitting)

With `r = 1/2`, `theta = 2/9` *exactly*, the three sqrt-masses (unsorted) are

```text
lambda = { 2.379438172, 0.040349908, 0.580211920 }  (in units of a),
```

all positive, so sorting the masses is the increasing-order chamber
presentation of the same three outputs. The dimensionless mass ratios,
normalized to the electron slot, are

```text
m_e : m_mu : m_tau  =  1 : 206.770316 : 3477.472837   (model, r=1/2, theta=2/9)
                    =  1 : 206.768285 : 3477.228307   (PDG 2024, labelled).
```

**Labelled comparison (PDG 2024: `m_e=0.5109989461`, `m_mu=105.6583755`,
`m_tau=1776.86` MeV).** Per-slot relative deviation of the mass ratios:

| slot | model / PDG ratio | relative deviation |
|---|---|---|
| `mu / e`  | 206.770316 vs 206.768285 | **9.8e-6** |
| `tau / e` | 3477.472837 vs 3477.228307 | **7.0e-5** |

So `(r=1/2, theta=2/9)` reproduces the observed charged-lepton mass ratios to
**better than `7e-5` (max per-slot, in the `tau` slot; `~1e-5` in the `mu`
slot)**. This is the classic Brannen result, verified here from the pinned
shape. The Koide identity holds exactly for the model, `Q = 2/3`, independent
of the phase (retained guardrail).

## T1b — Honest `theta = 2/9` residual

`theta = 2/9` is **not exactly** the best-fit Brannen phase. The best-fit
phase extracted from PDG (in the Brannen chamber containing `2/9`) is

```text
theta_fit  =  0.22222963 rad,
theta_fit - 2/9  =  +7.4e-6 rad   ( 3.3e-5 relative ).
```

So the framework value `2/9 = 0.22222222...` sits within `~8e-6 rad` of the
empirical best fit, but the residual is nonzero. The empirical Koide value is
likewise `Q_PDG = 0.6666605`, with `Q_PDG - 2/3 = -6.2e-6` (tiny but nonzero).
The reproduction is **exact-modulo-imports** (the shape ratios are an exact
function of `r=1/2, theta=2/9`), not exact-to-PDG: the `~7e-5` ratio residual
and the `~7e-6 rad` phase residual are real and reported honestly. We do not
claim `2/9` is the measured value to machine precision.

## T2 — The scale: exactly one residual DOF, and it is free

**One DOF.** The dimensionless shape fixes *both* independent mass ratios
(`mu/e` and `tau/e`), so the only quantity not fixed is the overall `a`.
Rescaling `a -> a'` multiplies every mass by `(a'/a)^2` and leaves all ratios
invariant (verified). Counting: `3` masses minus `2` ratio constraints fixed
by `(r=1/2, theta=2/9)` `= 1` free real number. Setting it to PDG via
`a = (sqrt(m_e)+sqrt(m_mu)+sqrt(m_tau))/3` gives `a^2 = 313.84 MeV`.

**Is it pinnable? Currently NO.** On origin/main the single dimensionful scale
`a^{-1}` is registered as the framework's `scale_reference_primitive` —
"units conversion only, not a Tier-A admitted derivation target and not a
status-bounding dependency" — with the Planck-scale no-go portfolio
(`planck_finite_response_no_go`, `planck_parent_source_hidden_character_no_go`,
`planck_boundary_orientation_incidence_no_go`) recording why no finite
construction supplies it. Concretely for the three sub-questions posed:

- **(a) b-tau unification → m_tau ← m_b?** No `b-tau` (bottom-tau) unification
  source note exists on this tree; the runner confirms the absence. Even a
  GUT-style `m_b = m_tau` relation would only trade the lepton scale for the
  `m_b` scale, which is itself not pinned in-framework — it relocates the
  residual, it does not remove it.
- **(b) lepton scale ↔ derived top scale?** No retained framework relation on
  origin/main locks the charged-lepton scale to the top (or any other) scale.
  The two-gate companion note explicitly lists the absolute charged-lepton
  scale as a *separate residual* it does not close.
- **(c) Q=2/3 + theta=2/9 fix the shape but not the scale.** Confirmed: both
  selectors are dimensionless; neither carries a dimensionful magnitude. The
  scale is exactly one residual real number, orthogonal to the shape.

**Conclusion T2:** the overall scale is exactly **one free residual DOF** and
is **not pinnable** by any present framework relation; it is the units-only
primitive `a^{-1}`.

## T3 — Honest input count for the full 3-mass charged-lepton spectrum

| ingredient | count | status on origin/main |
|---|---|---|
| free real numbers | **1** | overall scale `a` (units-only `scale_reference_primitive`) |
| named imports | **2** | `I1` chirality → `r = 1/2`; `I2` radian-bridge → `theta = 2/9` |

Both imports are the established `AC_phi_lambda` Tier-A admitted mass-pattern
input (the `C_3`-breaking phase plus the amplitude-equipartition `sqrt(2)`),
each with its own retained no-go portfolio (chirality:
`koide_z3_equivariant_anticommuting_no_go`; radian bridge:
`koide_a1_radian_bridge_irreducibility_audit`,
`koide_delta_lattice_wilson_selected_eigenline_no_go`,
`koide_delta_marked_relative_cobordism_no_go`).

**Bottom line:** the full charged-lepton spectrum is

```text
3 charged-lepton masses  =  1 free number (scale)  +  2 named imports (chirality, radian bridge),
```

reproducing the PDG ratios to `< 7e-5` per slot, with `Q = 2/3` exact. The
two imports are dimensionless shape selectors; the one free number is the
overall scale. No additional free parameters enter.

## No-Go Discipline Gate

- **N1 alternative routes.** The shape ratios can be presented via the Brannen
  cosine form, the `C_3`-circulant eigenvalues, or the Koide cone; all give the
  same `1 : 206.77 : 3477.47`. None of these *derive* the two shape pins — they
  are the `AC_phi_lambda` import with retained no-go portfolios cited above.
- **N2 wall independence.** Gate-1 selection (`r=1/2`), Gate-2 phase
  (`theta=2/9`), and the absolute scale are three independent residuals. This
  note touches the dimensionless ratios (fixed by the two imports) and the
  scale count (one free number). It closes none of the three.
- **N3 hidden-wall scan.** The `sqrt(2)` amplitude, the `2/9` phase, and the
  scale `a` are explicit dependencies/residuals, not hidden premises. PDG is a
  labelled comparator, never an input to the shape (verified: `H1`).
- **N4 residual matching.** The chirality and radian-bridge no-gos are cited as
  the boundaries on the two imports, not as positive derivations.
- **N5 rhetoric audit.** "Exact-modulo-imports" means the dimensionless ratios
  are an exact closed-form function of `(r=1/2, theta=2/9)`; it does **not**
  mean PDG is reproduced exactly (the `~7e-5` ratio residual and `~7e-6 rad`
  phase residual are reported).
- **N6 partial-closure scan.** If a future retained derivation supplies `r=1/2`
  or `theta=2/9` (or pins the scale), this accounting can be revisited; this
  note performs no such derivation and no promotion.
- **N7 steelman.** A reviewer could object that `theta=2/9` is a fit, not a
  derivation. Correct: this note does not derive it; it imports it
  (`AC_phi_lambda`) and reports the residual against PDG. The dimensionless
  ratio reproduction *given* the two pins is the exact theorem content.
- **N8 cross-cycle echo.** This complements the Brannen-BAE delta bounded note
  (sorted ratios, `Q=2/3` guardrail, PDG sidecar) and the two-gate companion
  (gate structure); it adds the explicit forward scale-DOF count. Neither is
  treated as an audit verdict.

## What this does NOT claim

- Does **not** derive `r = 1/2`, `theta = 2/9`, or the `sqrt(2)` amplitude from
  the retained inventory alone (these are the `AC_phi_lambda` import).
- Does **not** claim `theta = 2/9` is exactly the measured Brannen phase; the
  residual `theta_fit - 2/9 = +7.4e-6 rad` is reported.
- Does **not** derive or pin the overall scale `a`; it is one free residual,
  the units-only primitive.
- Does **not** consume PDG values to fix the shape; PDG is a labelled
  comparator (and supplies the empirical best-fit phase / scale in T1b/T2 only).
- Does **not** make any neutrino-sector claim.
- Does **not** modify, promote, or weaken any registry entry or retained no-go,
  and does **not** add an axiom or new theory language.

## Authorities

| Authority | Standing on origin/main | Role |
|---|---|---|
| [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) | axiom premise | one-qubit local algebra + `Z^3` substrate; the circulant lives here |
| [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) | retained positive_theorem | `Q=2/3` for the `sqrt(2)` ansatz, any phase (T1 guardrail) |
| [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) | retained positive_theorem | cone/circulant equivalence (T1) |
| [`CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md`](CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md) | bounded_theorem | sorted ratios + PDG sidecar companion |
| [`CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md`](CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md) | bounded_theorem | two-gate structure; absolute scale = separate residual |
| [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md) | meta (audit-decided) | `AC_phi_lambda` import authority; scale-reference primitive |
| [`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json) | machine registry | `AC_phi_lambda` + `scale_reference_primitive` checked by the runner |
| Particle Data Group 2024 (`m_e, m_mu, m_tau`) | external observation | labelled comparator (T1) + empirical best-fit phase/scale (T1b/T2) only |

## Verification

```bash
python3 scripts/cl3_lepton_masses_from_pinned_shape_2026_06_05.py
```

Expected: `PASS=24 FAIL=0`. The runner checks the exact spectrum and ratios
from `(r=1/2, theta=2/9)`, the labelled PDG comparison (`< 7e-5` per slot), the
exact `Q=2/3`, the honest `theta` residual (`+7.4e-6 rad`, nonzero), the
single-DOF scale invariance, the registry's units-only scale primitive and the
absence of any `b-tau`/lepton-top pinning relation, the `1 free + 2 imports`
count, and hostile-audit guards (no PDG load-bearing in the shape, residual
nonzero, no promotion, scale not silently pinned).

## Sidecar references

Koide (1981); Brannen (2005); Particle Data Group (2024); Buckingham (1914).
Context only; no external value is load-bearing for the shape.
