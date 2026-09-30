# Emergent Gravity Reduces to One Admission: G_Newton Is Induced (~a²); the Residual Wall Is the Metric-DOF / Conformal-Class Posit

**Date:** 2026-06-17
**Type:** positive_theorem — narrow_theorem (Sakharov induced-G structure) + frontier resolution map
**Claim type:** positive_theorem — narrow_theorem

**Claim scope (narrow):** A structural result on the emergent Newton constant and a precise
location of the residual gravity wall. **(1)** Via the Sakharov route (gravity induced by the
fermion determinant `W = log|det D|`), the induced Einstein–Hilbert term is the Dirac
heat-kernel coefficient `a₁ = −R/3` (Gilkey/Lichnerowicz, computed), with cutoff magnitude
`~Λ²`, so `1/(16πG) ~ Λ² N_f` and **`G ~ a²/N_f`** — the emergent Newton constant is the
lattice/Planck scale set by the cutoff and the fermion species count, **not an admitted free
parameter**. **(2)** The residual obstruction to full closure is **not** G_Newton's magnitude
(induced) nor the graviton's existence (healthy spin-2): it is the overall EH-sign / source
coupling for `G>0`, which reduces to the **unaudited metric-DOF / conformal-class posit** (the
emergent metric's conformal factor / record-time axis). This note proposes **no** status change
and edits no other note. **Status authority: independent audit lane only.**

## Corrigendum (2026-09-30)

**In plain words.** This note printed the wrong number in front of its estimate for Newton's
constant. The formula written just above the number, once solved for `G`, gives a coefficient
`3π`, not `48π³`. The printed number was too large by `(4π)² ≈ 157.9`. Only that number was wrong;
the argument (the heat-kernel coefficient, the scaling `G ~ a²/N_f`, and the residual wall in §2) is
unchanged.

**What was wrong.** §1 (and the runner's printed output) gave
`G ~ 48π³ / (N_f Λ²)` as the consequence of `1/(16πG) ~ (4π)⁻² (1/3) Λ² N_f`. Solving that line for
`G`: `16πG = 3 (4π)² / (Λ² N_f) = 48π² / (Λ² N_f)`, so `G = 3π / (N_f Λ²)`. The printed
`48π³ = 3π · (4π)²` is what a loop prefactor `(4π)⁻⁴` (instead of the `(4π)⁻²` used in the same
section) would give, so it looks like the factor `(4π)²` was carried through once too often; the
original hand calculation is not preserved, so this is a reading, not a record. The runner carried
the same typed number.

**Corrected statement.** `G ~ 3π / (N_f Λ²) ~ a²/N_f` with `Λ ~ 1/a`, i.e. `G/a² = 3π/N_f ≈ 9.42/N_f`
for the coefficient of the matching line. With the illustrative `N_f = 8` and `Λ = 1/a`, the implied
`l_P/a = √(G/a²)` is `1.085`; the printed coefficient would have given `13.64` (a factor `4π` larger).
This is a correction to an order-one number inside an order-of-magnitude estimate.

**Nothing else in the note's normalisation rescues `48π³`.** The `(4π)⁻²` is the flat `d = 4`
heat-kernel prefactor (`∫ d⁴p/(2π)⁴ e^{-sp²} = (4πs)⁻²`); the proper-time cutoff integral gives
`Λ²/(4π)²`; `a₁ = −R/3` is computed in the runner. Rational scheme factors (the `1/2` in
`det D = (det D²)^{1/2}`, species or spinor counts, `8πG` versus `16πG`) multiply `3π` by a rational
number, and reaching `48π³` needs `16π²`, which is irrational. Only a different loop prefactor
would supply it, and none applies to a one-loop `d = 4` determinant.

**What still stands.** `a₁ = −R/3`; the induced Einstein–Hilbert term of order `Λ²`; the scaling
`G ~ a²/N_f`; and §2, the residual wall (the `G > 0` sign, tied to the unaudited metric-DOF posit).
The note never claimed `a = l_P`; it claimed the scaling only.

**What is not established here.** The order-one factor is only the coefficient of the matching
line. The `1/2` in `det D = (det D²)^{1/2}`, the fermion sign of the induced term (which is the §2
sign question), and the cutoff scheme (for example `Λ = π/a` in place of `Λ = 1/a` moves `l_P/a`
by a factor `π`) are not evaluated in this note. So this note does not derive a value of `l_P/a`.

**Evidence and checks.** The corrected runner
[`scripts/frontier_universal_gr_sakharov_gnewton_induced_scale_2026_06_17.py`](../scripts/frontier_universal_gr_sakharov_gnewton_induced_scale_2026_06_17.py)
now solves the matching line symbolically and adds nine PASS/FAIL checks (`C1`–`C9`, `TOTAL: PASS=9 FAIL=0`).
The error was found in the 2026-09-29 wall-campaign check of the gravity lane (entry L14-W11). All
checks here are by the same model family (Claude) and are not an independent-family review. No audit
status field is changed by this correction.

## 1. G_Newton is induced (~a²), not a free parameter

The Sakharov mechanism induces gravity from the matter determinant. The leading metric
effective-action terms are the Dirac operator's Seeley–DeWitt coefficients (Gilkey;
`P = −(∇² + E)`, Dirac `E = −R/4` by Lichnerowicz, spinor dim 4 in d=4):

- `a₀ ~ (4π)⁻² · 4` → induced **cosmological constant**, magnitude `~Λ⁴` (the dominant divergence).
- `a₁ = (4π)⁻²·(1/6)·tr(6E + R·I) = −(4π)⁻² R/3` → induced **Einstein–Hilbert** term, magnitude `~Λ²`.

Matching `S_ind ⊃ (4π)⁻²·(1/3)·Λ² ∫R√g` to `S_EH = (1/16πG) ∫R√g`:

> `1/(16πG) ~ (4π)⁻² (1/3) Λ² N_f`  ⟹  **`G ~ 48π³ / (N_f Λ²) ~ a²/N_f`**  (`Λ ~ 1/a`).

> **[Corrigendum 2026-09-30: the coefficient `48π³` printed above is wrong. The matching line gives `G ~ 3π / (N_f Λ²) ~ a²/N_f`; see the Corrigendum section at the top. The original text is kept as printed.]**

So the emergent Newton constant is the **lattice/Planck scale** — a finite quantity fixed by
the cutoff and the species count, *not* an input. (Computed runner block.)

## 2. What is healthy vs the residual wall

**Healthy / established** (the emergent graviton's kinetic + polarization structure):
- positive isotropic TT spin-2 stiffness `C_TT > 0` (the program's induced-determinant runs);
- canonical, frame-independent, SO(3)-irreducible spin-2 graviton channel with linearized-Einstein
  channel signs and the exact TT ½ coefficient
  ([`UNIVERSAL_GR_CANONICAL_CHANNEL_SECTION_AND_EINSTEIN_SIGNS`](UNIVERSAL_GR_CANONICAL_CHANNEL_SECTION_AND_EINSTEIN_SIGNS_NARROW_THEOREM_NOTE_2026-06-17.md));
- diffeomorphism-Ward identities to quintic order;
- `G_Newton` induced `~a²` (§1).

**Residual wall (NOT closed):** the overall EH-sign / source coupling for **`G > 0`** (attractive).
In induced gravity the sign of `1/(16πG)` is famously content/convention-sensitive (the Sakharov
sign problem). In this framework it is conditional on the `λ=1` / conformal-class structure of the
emergent metric, which ties to the **unaudited metric-DOF posit** (the emergent metric's conformal
factor / record-time axis). The conformal (trace) channel is exactly the wrong-sign mode
(`μ_conf < 0`, prior note), so **fixing `G > 0` = fixing the conformal-class admission.**

## 3. Resolution

Emergent gravity is cracked down to **one named structural admission** — the metric-DOF /
conformal-class posit (the record-time axis). Above it, the structure is in hand and computed:
a healthy spin-2 graviton, linearized-Einstein channel signs, an induced Newton constant at the
lattice scale `~a²`, and diffeomorphism-Ward identities to quintic order, all emergent from
`{qubit, Z³, Record}` via the fermion determinant. The wall is *not* the graviton's existence,
its polarization section, the Einstein-sign structure, or G_Newton's magnitude — it is the
**conformal-sector sign**, an instance of the metric-DOF admission.

This mirrors the framework's other frontier resolutions: color reduces to one composition-algebra
admission; one time dimension reduces to the single-generator dynamics gate; emergent gravity
reduces to the metric-DOF / conformal-class admission. In each case the frontier is advanced to a
single named, non-vacuous structural admission, with everything above it derived or precisely
characterized.

**Runner:** [`scripts/frontier_universal_gr_sakharov_gnewton_induced_scale_2026_06_17.py`](../scripts/frontier_universal_gr_sakharov_gnewton_induced_scale_2026_06_17.py)
(`a₁ = −1/3`, `G ~ a²/N_f`; deterministic, symbolic, memory-safe). No fitted parameters, no
observed values, no axiom-file edits, no `docs/audit/data/*` edits. Sets no audit status. The
continuum heat-kernel gives the universal *structure* (`G ~ Λ²`, `a₁ = −R/3`); the framework's
specific lattice realization confirms the healthy spin-2 sign; the conformal-sector sign is the
lattice-specific conditional piece that ties to the metric-DOF posit.
