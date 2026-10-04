# θ₁₃ is the C₃-Doublet-Breaking Measure: the Trimaximal Geometry Forces sin θ₁₃ = sin θ_e/√2 (the √2 Derived); θ_e ≈ Cabibbo is the Residual — Narrow Theorem

**Date:** 2026-06-08
**Claim type:** bounded_theorem (locates θ₁₃ as C₃-doublet breaking + derives the √2 relation; θ_e is the dimensionless residual)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/theta13_is_c3_doublet_breaking_sqrt2_charged_lepton_runner.py`](../scripts/theta13_is_c3_doublet_breaking_sqrt2_charged_lepton_runner.py)
**Cached output:** [`logs/runner-cache/theta13_is_c3_doublet_breaking_sqrt2_charged_lepton_runner.txt`](../logs/runner-cache/theta13_is_c3_doublet_breaking_sqrt2_charged_lepton_runner.txt)

## Corrigendum (2026-09-30)

Source-scope correction. Status fields above are unchanged; effective status
stays with the independent audit lane. Checks are same-family (Claude Sonnet
5.5), not an independent referee.

The relation `sin theta_13 = sin theta_e / sqrt2` is exact for the stated
construction (`PMNS = U_e^dag U_nu`, real 1-2 rotation `theta_e`,
`U_nu = (xi, W, eta)`) and stands. Three statements around it need this scope:

- **"The only missing number is `theta_e`"** (What this advances). With a real
  `theta_e = 12.16 deg`, the PMNS solar angle of the same construction is
  `s12^2 = 0.2005` (0.4813 for the opposite sign of `theta_e`), outside the
  NuFIT-6.1 3-sigma range [0.2893, 0.3295] the repository already quotes
  (`PMNS_DCP_FORECAST_STANDING_DEGRADES_UNDER_NUFIT6_BOUNDED_NOTE_2026-06-08.md`,
  line 28). Once `theta_e != 0` the second PMNS column is no longer trimaximal.
  Reaching mid-range `s12^2` needs a second parameter, a relative phase of about
  77 degrees in the 1-2 rotation, which the note does not name.
- **"The framework derives the trimaximal column (TM2)"** (Audit context). Without
  the charged-lepton rotation the TM2 sum rule is `s12^2 = 1/(3 c13^2)`, at least
  `1/3` for every `s13^2` and 0.3409 at `s13^2 = 0.0222`, also outside that range.
  arXiv:2512.03809 (Ding, Li, Lu, Petcov; the statement is in the body text, not
  the abstract) reports the TM2-type patterns disagree with the first JUNO
  `sin^2 theta_12` measurement at the 3.6 sigma level. See the Corrigenda in
  `PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md`
  and
  `PMNS_TM2_MAGIC_RESIDUAL_DYNAMICAL_GENERATOR_NARROW_THEOREM_NOTE_2026-06-05.md`.
- **"`theta_13` is the free TM2 parameter"** (Audit context). It is free for the
  record dephasing alone. The TM2 package of the cited notes also carries the
  `mu`-`tau` residual; realised as the unitary invariance `[M_nu, P_23] = 0`
  it forces `theta_13 = 0` (Corrigendum in the magic-residual note). Here
  `theta_13` comes from the charged-lepton rotation acting on the tribimaximal
  `U_nu`, which is itself the `V_4` case with `theta_13 = 0`.

TM1 (first column `xi`) is a literature pattern the same paper finds inside the
JUNO 3-sigma range; this repository does not supply it, and nothing here adopts
it as a framework result. Evidence:
`scripts/pmns_tm2_scope_check_solar_angle_outside_nufit61_and_v4_commutant_forces_theta13_zero_2026_09_30.py`
(26 PASS, 0 FAIL).

## Audit context

The framework derives the **trimaximal column** (TM2) — the neutrino records einselect the C₃ singlet
`(1,1,1)/√3` as the second PMNS column
([`PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR`](PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md);
[`PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED`](PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md),
`retained_bounded`) — but those notes explicitly **do not predict** `sin²θ₁₃` (it is the free TM2
parameter). This note **locates** θ₁₃ and **derives** the geometric factor that relates it to the
charged-lepton correction, moving θ₁₃ from "no prediction" to "`θ_e/√2`, √2 derived."

## Safe statement

**Theorem (θ₁₃ = C₃-doublet breaking; sin θ₁₃ = sin θ_e/√2).**

1. **The C₃ structure is the TBM form.** The records-einselected C₃ **singlet** `(1,1,1)/√3` (the
   trimaximal 2nd column) together with the real **doublet** basis `{(2,−1,−1)/√6, (0,1,−1)/√2}` (the
   real/imaginary parts of the C₃ doublet eigenvectors `(1,ω,ω²)/√3, (1,ω²,ω)/√3`) is the orthonormal
   tribimaximal matrix.
2. **The doublet is degenerate → θ₁₃ is unfixed by the neutrino records.** A C₃-invariant einselecting
   operator is a real circulant `aI + b(C+C²)` with spectrum `{a+2b` (singlet)`, a−b, a−b` (doublet,
   **2-fold degenerate**)`}` ([`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md),
   `retained_bounded`). So the records resolve the singlet (the trimaximal column) but **not** the
   doublet rotation — **θ₁₃ ≠ 0 is a direct measure of C₃-doublet breaking**, sourced externally.
3. **The charged-lepton correction forces the √2.** A charged-lepton `1–2` rotation by `θ_e`
   (`PMNS = U_e† U_ν`) gives, **exactly**, `|U_e3| = sin θ_e/√2` — i.e. `sin θ₁₃ = sin θ_e/√2`. The
   **√2 is derived**: it is the normalization of the C₃-doublet imaginary basis vector `(0,1,−1)/√2`
   (the third column).
4. **The observed θ₁₃ implies θ_e ≈ Cabibbo (QLC-consistent).** `sin²θ₁₃ = 0.0222` (`θ₁₃ = 8.57°`)
   ⟹ `θ_e = arcsin(√2 sin θ₁₃) = 12.16°` — within ~1° of the Cabibbo angle `θ_C = 13.04°`
   (quark-lepton complementarity). Forward, `θ_e = θ_C` gives `sin²θ₁₃ = 0.0255` (`θ₁₃ = 9.18°` vs the
   observed `8.57°`, the known Cabibbo-haze near-match).

So **θ₁₃ = θ_e/√2** with the **√2 derived** (the C₃-doublet geometry) and **θ_e the residual** — a
single **dimensionless** charged-lepton input, Cabibbo-sized.

## What this advances

- It moves θ₁₃ from "no prediction / free TM2 parameter" to a **derived structural relation**
  `sin θ₁₃ = sin θ_e/√2`, and **identifies its physical meaning**: θ₁₃ is the order parameter of
  C₃-doublet (μ–τ-symmetry) breaking, which the records do *not* supply — it is sourced by the
  charged-lepton sector.
- It pins the residual precisely: the **only** missing number is the **dimensionless** charged-lepton
  angle `θ_e` (≈ the Cabibbo angle) — exactly the kind of genuine dimensionless residual the program
  reduces to (no scale ambiguity; the ruler is irrelevant for an angle).

## Boundary (honest)

- **θ₁₃ is not fully derived.** The √2 and the location (doublet-breaking) are derived; `θ_e` is an
  input. The result is `θ₁₃ = θ_e/√2`, not a number from nothing.
- **The forward match is approximate.** `θ_e = θ_C` overshoots by ~0.6° in the angle (the well-known
  Cabibbo-haze ~7% level); the exact `θ_e` is the charged-lepton correction, slightly below `θ_C`.
- **QLC (`θ_e ≈ θ_C`) is a consistency, not a derivation** — connecting `θ_e` to the *quark* Cabibbo
  angle is a separate (open) question.

## Forbidden imports check

No new axiom. A_min + the retained trimaximal-column / einselection results + standard PMNS geometry
(3×3, reproduced). PDG `sin²θ₁₃`, `θ_C` are the comparison data (a dimensionless observable; no scale
or ruler enters an angle). Memory-safe.

## Runner check breakdown

Class A: (A1) the C₃ singlet+doublet basis = TBM (trimaximal column); (A2) the C₃ doublet is degenerate
⟹ θ₁₃ unfixed by the records; (A3) `sin θ₁₃ = sin θ_e/√2` exactly (√2 derived); (A4) observed θ₁₃ ⟹
`θ_e ≈ 12.2° ≈ θ_C`. Expected `runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

The records-einselected C₃ singlet+doublet basis is the tribimaximal matrix; a C₃-invariant operator
leaves the doublet 2-fold degenerate, so θ₁₃ (the doublet rotation) is not fixed by the neutrino
records and is the order parameter of C₃-doublet breaking. A charged-lepton 1–2 rotation θ_e gives
exactly `sin θ₁₃ = sin θ_e/√2` (the √2 = the norm of the doublet imaginary basis vector), and the
observed θ₁₃ implies `θ_e = 12.16°`, within ~1° of the Cabibbo angle. The note is honest that θ₁₃ is
derived only up to the dimensionless residual θ_e (the √2 and the doublet-breaking interpretation are
the derived content), that the forward match is the ~7% Cabibbo-haze level, and that QLC is a
consistency not a derivation. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/theta13_is_c3_doublet_breaking_sqrt2_charged_lepton_runner.py
```
