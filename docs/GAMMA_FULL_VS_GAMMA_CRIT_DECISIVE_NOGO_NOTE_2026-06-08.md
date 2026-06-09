# The Velocity Anomalous Dimension `γ_full = (4/3 + N_f/2)α_s` Is Decisively Below `γ_crit` for the Tight Lorentz-Violation Bounds — the Continuous-Time Obstruction Horn's Flow-Suppression Escape Is Closed (the Asymptotic-Freedom Trap) — No-Go Note

**Date:** 2026-06-08
**Claim type:** no_go (a computed quantitative no-go on the flow-suppression escape of the `ξ → ∞` obstruction horn)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.py`](../scripts/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.txt`](../logs/runner-cache/frontier_gamma_full_vs_gamma_crit_decisive_nogo_2026_06_08.txt)

---

## Role

On the continuous-time (`ξ = a_s/a_τ → ∞`) horn the marginal velocity anisotropy
`δv = c_t/c_s − 1` is regenerated at `O(α_s/4π)` and is loop- but **not**
Planck-suppressed (the Collins-Perez-Sudarsky-Urrutia-Vučetič naturalness problem).
The computed one-loop coefficient is `|δv| ≈ 0.2 α_s` (the velocity-RG coefficient note,
PR #3277), nonzero for every action tried and not internally (taste / U(1) / Cl(3))
protected. The **only** way to push the residual species anisotropy below the tight SME
bounds is the interacting velocity-RG **attractor**: the coupled flow suppresses the
species velocity difference as a power of the hierarchy,

  `|δv|_IR ~ |δv|_UV · (μ / M_Pl)^γ`,

with `γ` the anomalous dimension of the velocity-difference operator. Closing the
**unbounded** question (`δv = 0` retained *unconditionally*) requires `γ` to reach the
critical exponent `γ_crit` set by the bound and the Planck-to-IR hierarchy. This note
computes `γ_full` with the full SU(3) colour structure and tests it against `γ_crit`.

## The computation

**The difference-mode eigenvalue (runner Part A).** The coupled one-loop velocity RG on
`(v_F, v_b)` (fermion, gauge boson) has the difference `D = v_F − v_b` obeying
`dD/dl = −(C_F + T_F N_f) α_s D`, so

  `γ_full = c_γ α_s,  c_γ = C_F + T_F N_f = 4/3 + N_f/2.`

The adjoint Casimir `C_A = 3` **drops from the difference channel**: the pure-glue
(3-gluon + ghost) self-energy renormalizes the single gluon velocity toward itself (one
octet, one velocity) — a common-mode / wavefunction renormalization that cancels in the
difference and lives instead in the coupling β-function's `−11/3 C_A`. At `β = 6`
(`g² = 2N/β = 1`, `α_s = 1/4π`), `γ_full ≈ 0.15–0.34` for `N_f = 1…6`.

**Maximal-leak stress (runner Part B).** Even if the **full** adjoint `C_A` were forced
into the difference channel (physically wrong — it is a common-mode pull) **and** `N_f = 6`,

  `c_γ ≤ C_F + T_F·6 + C_A = 7.33,  γ_max ≈ 0.58.`

This over-states `γ` in two independent ways and **still** lands below every tight `γ_crit`.

**`γ_crit` and the decisive gap (runner Parts C–D).** With `δv_UV ~ 10⁻²` and the
`M_Pl → 1 GeV` hierarchy, `γ_crit` ≈ 0.96 (photon), 1.06 (electron), 1.32 (nucleon),
0.54 (weakest, quark/gluon). `γ_full ≤ 0.58` is below **all tight bounds** in every
amplified corner; the residual species `δv(1 GeV) ~ 10⁻⁷…10⁻⁴` exceeds the tight bounds by
**13–23 orders**. The IR strong-QCD regime (`α_s ~ 1`) acts over only ~1 e-fold near
`Λ_QCD` → extra suppression `~ e⁻¹`, nowhere near the `~10⁻¹⁴` needed.

## The one honest boundary (runner Part F)

The no-go is **conditional on the gauge sector being asymptotically free** — which the
framework's SU(3) is. The RG-integrated suppression exponent `S = ∫ γ dl` from 1 GeV to
`M_Pl` is `~7`, a factor 6–8 below the `S ~ 42–58` the tight bounds need, because `γ` is
tethered to the **weak UV** `α_s` exactly at the scale where the anisotropy regenerates.
A hypothetical **walking / near-conformal** plateau `α* ~ 0.3` sustained over the full
~44 e-folds *would* give `S ~ 37` and close the gap — but a sustained strong `γ` is
**mutually exclusive** with asymptotic freedom (a Banks-Zaks IR fixed point needs
`N_f ~ 16.5`, which destroys QCD). So asymptotic freedom is precisely the structural
property that both makes `γ` weak at `M_Pl` *and* forecloses the only escape — the
"asymptotic-freedom trap."

**False-escape guard.** The lattice bare `α ≈ 0.08` at `M_Pl` (β = 6) is **not** the
MS-bar continuum value (real `α_s(M_Pl) ~ 0.019`, even smaller); naively running the bare
coupling to a fake `~10¹⁵ GeV` Landau pole to inflate `S` is unphysical. The conservative
(bare) choice already over-states `γ` — the continuum value makes the no-go **stronger**.

## Verdict

**The continuous-time (`ξ → ∞`) obstruction horn's flow-suppression escape is closed.**
`γ_full < γ_crit` for the tight bounds robustly — to factor-2 in the `O(1)` coefficient
`c_v` (`d(γ_crit)/d log₁₀ δv_UV ≈ 0.05/decade`, so a 100× error moves `γ_crit` by ±0.10),
to the maximal colour leak, to large `N_f`, to a generous 2-loop coefficient, and to the
IR strong-coupling regime. Unconditional (unbounded) emergent Lorentz invariance is **not**
retainable via the continuous-time attractor flow. This computes and sharpens the
naturalness gap (the #3123 lane) with the full SU(3) colour structure and explicit
robustness in both directions.

## Honest scope (this is a no-go on the *escape*, not a closure of the lever)

- It is a no-go on the **flow-suppression escape** of the `ξ → ∞` horn **only**. On the
  `ξ = 1` discrete surface the B₄ hypercubic point group gives `δv = 0` **exactly**
  (rep-blind, all orders) — there is no residual and no `γ` is needed. So **both horns of
  `δv(ξ)` remain live**; this note does **not** close the `ξ` ambiguity.
- The `ξ = 1` protection is real B₄ but rests on a **supplied** `Z⁴` surface (the B₄
  boundary note); this note does **not** make `δv = 0` retained or unconditional.
- It does **not** resolve the open lever — the `record-tick = physical-time` bridge
  (live-ledger `audited_renaming`) stays **open**. The no-go sharpens the lever to one
  named bridge; it does not climb over it.
- It is **not** a solution, **not** a custodial mechanism, and **not** a proof of framework
  inconsistency. The framework is self-consistent; the `ξ → ∞` horn simply cannot reach the
  tight LV bounds by flow suppression.

## Reprove-and-cite ledger

- **Reproven here** (runner, from primitives): the SU(3) Casimirs `C_F = 4/3`,
  `T_F = 1/2`, `C_A = 3`; the difference-mode eigenvalue `c_γ = C_F + T_F N_f` (with `C_A`
  cancelling in the difference); `γ_full ≈ 0.15–0.34` and the maximal-leak over-estimate
  `γ_max ≈ 0.58`; `γ_crit` per sector and the 13–23-order residual gap; the
  asymptotic-freedom exponent `S ~ 7` vs the needed `S ~ 42–58`; the walking-conformal
  boundary and the bare-vs-MS-bar false-escape guard.
- **Cited** (comparator / scope only, never a derivation input): the SME tight LV bounds
  (photon / electron / nucleon / quark-gluon) as comparators; the
  Collins-Perez-Sudarsky-Urrutia-Vučetič naturalness problem as the named obstruction;
  Banks-Zaks as the scope marker for why a sustained strong fixed point is excluded for an
  AF gauge sector. No literature series or value is a derivation input.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. The cited
ledger statuses are recorded verbatim as of 2026-06-08.

- [LORENTZ_VELOCITY_RG_COEFFICIENT_COMPUTED_NOTE_2026-06-08.md](LORENTZ_VELOCITY_RG_COEFFICIENT_COMPUTED_NOTE_2026-06-08.md) (the computed `δv ≈ 0.2 α_s` coefficient; PR #3277)
- [EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md) (`retained_bounded`; the attractor whose contraction this bounds)
- [EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md) (the `ξ = 1` B₄ surface where `δv = 0`)
- [SINGLE_CLOCK_CONTINUOUS_TIME_IS_AN_UNAUDITED_INTERPOLATION_BOUNDED_NOTE_2026-06-08.md](SINGLE_CLOCK_CONTINUOUS_TIME_IS_AN_UNAUDITED_INTERPOLATION_BOUNDED_NOTE_2026-06-08.md) (the obstruction horn's demotion; Route 1)
- [TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md](TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md) (both horns live; the lever)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the computed one-loop
coefficient `|δv| ≈ 0.2 α_s` (PR #3277); (3) the coupled one-loop velocity RG with the
SU(3) colour factors; (4) the gauge sector is asymptotically free (the framework's SU(3)).
The result is a computed quantitative no-go: `γ_full < γ_crit` for the tight bounds
robustly, so the `ξ → ∞` horn's flow-suppression escape is closed.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag; the
SME bounds and the Collins / Banks-Zaks references are comparators / scope markers only,
never derivation inputs; the colour factors and `γ` are reproven from primitives in the
runner.

**No-promotion statement:** this note does **not** promote, demote, or set the audit status
of the velocity-RG notes, the attractor note, the B₄ boundary note, or any upstream row.
The independent audit lane is the only status authority. The no-go is on the flow-suppression
escape of the `ξ → ∞` horn only; both horns of `δv(ξ)` remain live and the
`record-tick = physical-time` lever stays open.
