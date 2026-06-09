# The Fixed-Point Velocity Anomalous Dimension `γ = (4/3 + N_f/2)α_s` Is Below the Critical Exponent `γ_crit` for the Tight Lorentz-Violation Bounds — Filling the Open Input Named by the Interacting Velocity-RG Attractor (#3121, Part D) — No-Go Note

**Date:** 2026-06-08
**Claim type:** no_go (a computed bound on the flow-suppression sufficiency of the `ξ → ∞` horn; fills a named open input of a landed note)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome, and does not change the status of any other note.
**Primary runner:**
[`scripts/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.py`](../scripts/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.txt`](../logs/runner-cache/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.txt)

---

## What this fills

[`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)
(the #3121 attractor, on main) organizes the velocity-anisotropy residual but leaves open,
**named**: *"the anomalous dimension `γ` at the physical fixed point, hence whether the
hierarchy suppression beats bounds."* On the continuous-time (`ξ = a_s/a_τ → ∞`) horn the
species velocity anisotropy is suppressed by the attractor as

  `|δv|_IR ~ |δv|_UV · (μ / M_Pl)^γ`,

so beating a Lorentz-violation bound `B` requires `γ ≥ γ_crit(B)`, with
`γ_crit(B) = log₁₀(δv_UV / B) / log₁₀(M_Pl / μ)`. This note computes `γ` with the full
SU(3) colour structure and compares it to `γ_crit`. **Result: `γ < γ_crit` for the tight
bounds, robustly — the hierarchy suppression does not beat them; #3121's residual stands.**

## The computation (exact scope of the runner)

**The difference-mode eigenvalue (runner Part A — diagonalized).** The coupled one-loop
velocity RG on `(v_F, v_b)` (fundamental fermion, gauge boson),
`dv_F/dl = C_F α_s (v_b − v_F)`, `dv_b/dl = T_F N_f α_s (v_F − v_b)`, is a 2×2 system whose
eigenvalues, computed by diagonalization, are `0` (the common / overall-velocity mode) and

  `−γ,  γ = (C_F + T_F N_f) α_s = (4/3 + N_f/2) α_s.`

The adjoint Casimir `C_A = 3` does **not** appear in the coupled matrix: the pure-glue
self-energy renormalizes the single gluon velocity toward itself (a common-mode /
wavefunction pull) and lives in the coupling β-function's `−11/3 C_A`, not the velocity
**difference**. At `β = 6` (`g² = 2N/β = 1`, `α_s = 1/4π`), `γ ≈ 0.15–0.34` for `N_f = 1…6`.

**Inflated over-estimate (runner Part B).** Forcing the **full** adjoint `C_A` into the
difference channel **and** `N_f = 6` gives `c_γ ≤ 7.33`, `γ_max ≈ 0.58` — an over-estimate in
two independent ways.

**`γ_crit` and the margin (runner Parts C–D).** With the one-loop estimate `δv_UV ~ 0.2 α_s`
and the `M_Pl → 1 GeV` hierarchy (≈19.1 decades), `γ_crit ≈ 0.95` (photon), 1.06 (electron),
1.32 (nucleon), 0.53 (weakest, quark/gluon). The inflated `γ_max = 0.58` is below **all
tight bounds**. The IR strong-QCD regime (`α_s ~ 1`) acts over only ~1 e-fold near `Λ_QCD`,
giving an extra factor `~e⁻¹`, nowhere near the `~10⁻¹⁴` needed.

**Robust to the (also-open) coefficient.** #3121 also leaves the *exact* `δv_UV` coefficient
open. The no-go does not need it: `d γ_crit / d log₁₀ δv_UV ≈ 0.05/decade`, and the one-loop
estimate `δv_UV ~ 1.6×10⁻²` sits **7 orders** (inflated `γ`) to **14 orders** (physical `γ`)
above the threshold `δv_UV ~ 10⁻⁹…10⁻¹⁶` where even the inflated `γ_max` would begin to beat
the photon bound. So the no-go survives the open coefficient being wrong by many orders.
*(Honest boundary: it does not survive an unbounded downward revision of `δv_UV` below
`~10⁻⁹`; the one-loop estimate is `~10⁻²`, so this is not a live concern.)*

## The one honest boundary (runner Part F)

The no-go holds **because the gauge sector is asymptotically free** — which the framework's
SU(3) is. The RG-integrated exponent `S = ∫ γ dl` from 1 GeV to `M_Pl` is `~7`, a factor
6–8 below the `S ~ 42–58` the tight bounds need, because `γ` is tethered to the **weak UV**
`α_s` exactly where the anisotropy regenerates. A hypothetical **walking / near-conformal**
plateau `α* ~ 0.3` sustained over the full hierarchy *would* give `S ~ 37` and could close the
gap — but a sustained strong `γ` is **mutually exclusive** with asymptotic freedom (a
Banks-Zaks fixed point needs `N_f ~ 16.5`, which destroys QCD). Asymptotic freedom is exactly
what both makes `γ` weak at `M_Pl` and forecloses the only escape.

**False-escape guard.** The lattice bare `α ≈ 0.08` at `M_Pl` (β = 6) is **not** the MS-bar
continuum value (`α_s(M_Pl) ~ 0.019`, smaller); running the bare coupling to a fake
`~10¹⁵ GeV` Landau pole to inflate `S` is unphysical, and the continuum value makes the
no-go **stronger**.

## Honest scope (a no-go on the *escape*, not a closure)

- It bounds the **flow-suppression sufficiency** of the `ξ → ∞` horn **only**. On the
  `ξ = 1` discrete surface the cited
  [B₄ boundary note](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  gives `δv = 0` by the hypercubic point group (on a supplied `Z⁴` surface). So **both horns
  of `δv(ξ)` remain live**; this note does **not** close the `ξ` ambiguity and does **not**
  establish `δv = 0`.
- `δv ~ 0.2 α_s` is a one-loop **estimate** (its exact value is #3121's other open input), not
  a fully computed coefficient; the no-go is robust to it (margin above).
- It is **not** a solution to the Lorentz naturalness problem, **not** a custodial mechanism,
  and **not** a proof of framework inconsistency. It is a computed bound that the named
  attractor exponent does not reach `γ_crit` for an asymptotically-free gauge sector.

## Reprove-and-cite ledger

- **Reproven here** (runner, from primitives; every check an independent numeric test): the
  SU(3) Casimirs from `N = 3`; the difference-mode eigenvalue `γ = (C_F + T_F N_f) α_s` by
  diagonalizing the coupled 2×2 RG (with the zero common-mode and `C_A` structurally absent);
  the inflated `γ_max ≈ 0.58`; `γ_crit(B)` per sector; the `γ_max < γ_crit` tight-bound
  comparison; the open-coefficient margin (fail-threshold vs the one-loop estimate); the
  asymptotic-freedom exponent `S ~ 7` vs the needed `~42`; the walking-conformal boundary;
  the bare-vs-MS-bar guard; the two-normalization reconciliation.
- **Cited** (comparator / scope only, never a derivation input): the SME tight LV bounds as
  comparators; the Collins-Perez-Sudarsky-Urrutia-Vučetič naturalness problem as the named
  obstruction; Banks-Zaks as the scope marker for why a sustained strong fixed point is
  excluded for an AF gauge sector.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. The cited
ledger statuses are recorded verbatim as of 2026-06-08 (all authorities below are on main).

- [EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md) (`retained_bounded`; the note whose Part-D open input — the fixed-point `γ` — this fills)
- [EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md) (the `ξ = 1` B₄ surface where `δv = 0`)
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md) (`retained_bounded`; the dim-6 IR dispersion isotropy)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the coupled one-loop velocity
RG of #3121 with the SU(3) colour factors; (3) the one-loop estimate `δv_UV ~ 0.2 α_s` (used
only through a margin — the no-go is robust to it); (4) the gauge sector is asymptotically
free (the framework's SU(3)). The result is a computed bound: the fixed-point anomalous
dimension `γ < γ_crit` for the tight bounds, robustly, so the `ξ → ∞` horn's flow-suppression
escape does not beat them.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag; the SME
bounds and the Collins / Banks-Zaks references are comparators / scope markers only, never
derivation inputs; the colour factors, `γ`, and `γ_crit` are reproven from primitives in the
runner.

**No-promotion statement:** this note does **not** promote, demote, or set the audit status of
the attractor note, the B₄ boundary note, or any other row; it adds a computed bound that fills
a named open input. The independent audit lane is the only status authority. The bound is on the
flow-suppression escape of the `ξ → ∞` horn only; both horns of `δv(ξ)` remain live and the
question of which surface is physical is not addressed here.
