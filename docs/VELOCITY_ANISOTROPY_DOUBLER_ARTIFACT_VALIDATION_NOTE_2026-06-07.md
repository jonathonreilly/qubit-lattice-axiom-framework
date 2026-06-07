# Velocity-Anisotropy Computation: the δv ≈ 0.31 Signal Was a Doubler Artifact (Validation / False-Alarm Retraction)

**Date:** 2026-06-07
**Claim type:** bounded_theorem (validation: a prototype signal is shown to be a numerical artifact)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_velocity_anisotropy_doubler_artifact_validation_2026_06_07.py`](../scripts/frontier_velocity_anisotropy_doubler_artifact_validation_2026_06_07.py)
**Cached runner output:**
[`logs/runner-cache/frontier_velocity_anisotropy_doubler_artifact_validation_2026_06_07.txt`](../logs/runner-cache/frontier_velocity_anisotropy_doubler_artifact_validation_2026_06_07.txt)

---

## Role

While pursuing the genuine open task of the Lorentz arc — *computing* the
radiative marginal velocity anisotropy `δv` (the route-1 task named by
`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06` (#3123) and the
framing-correction `LORENTZ_NATURALNESS_IS_A_COMPUTATION_NOT_A_TUNING_NOTE`
(#3134)) — a **prototype** one-loop self-energy on the spatial-lattice +
continuous-time surface produced an alarming preliminary signal:
`δv/v = B − A ≈ +0.31` per `g²C₂` (`A` = temporal kinetic renorm, `B` = spatial),
apparently stable as the external scale → 0. At `g²=1` (β=6) that is `~O(g²) ~ 0.3`,
which — vastly exceeding the LV bounds `~10⁻²⁰` — would **falsify** the framework.

The prototype was **never shipped as a claim**. It was put through validation +
an adversarial review (independently reproducing the numbers). **The `0.31` is a
numerical artifact.** This note documents the validation and retracts the alarm.
Runner: **10 PASS / 0 FAIL**.

## The four compounding errors (dominated by fermion doublers)

1. **Doublers (the dominant error).** The naive lattice fermion
   `G = −i(ν γ⁰ + Σ_j sin(k_j) γ^j)/(ν² + Σ sin²k_j)` has `2³ = 8` spatial doublers
   (poles at `k_j ∈ {0, π}`, alternating chirality / opposite group velocity). They
   contaminate the loop: **`A` does not converge** — it grows with the BZ grid
   (`A = −0.295 → −0.322 → −0.332` at `N = 16, 24, 32`; log-divergent), so the
   "`−0.31`" is just the divergent `A` at one arbitrary resolution.
2. **`B ≡ 0` is a parity artifact**, not a Ward identity: the spatial-channel
   integrand is odd over the symmetric BZ → exactly zero. So `B − A` compared a
   divergent `A` against a spurious `0`.
3. **`A, B` are gauge-dependent off-shell wavefunction renorms.** The physical
   observable is the **gauge-invariant pole velocity** `v² = (∂Σ/∂k²)/(∂Σ/∂ν²)` on
   shell — not the off-shell `B − A`.
4. **Normalization was *not* the issue** (a checked non-error): in lattice
   perturbation theory the loop `∫d⁴ℓ/(2π)⁴` already carries the `1/16π²`, and the
   one-loop `Z`-coefficients are genuinely `O(0.01–0.1)·C_F` (Capitani,
   hep-lat/0211036). The `0.31` was large only as a divergent log at the cutoff.

## The resolution (runner)

- **(A) Naive:** `A` log-divergent (grows with grid), `B ≡ 0` (parity). The `0.31`
  is spurious.
- **(B) Wilson (doubler-free, `r=1`):** removing the doublers **collapses the
  anisotropy ~5× to a finite, convergent `B − A ≈ 0.058`** per `g²C₂`
  (`0.0602 → 0.0585 → 0.0574` across the grid), with `B = −0.025 ≠ 0`.
- **(C) Isotropic control (4d-symmetric regulator):** `B − A ≈ −0.004 ≈ 0` — the
  velocity renorm vanishes (Lorentz preserved), confirming the method is sound and
  the residual anisotropy is genuinely the spatial-lattice/continuous-time source,
  not a coding bug.

## Verdict and corrected status

- The `δv ≈ 0.31` is an **artifact** (doublers + parity-zeroed `B` + a divergent
  cutoff log + an off-shell gauge-dependent extraction). **The framework is NOT
  falsified** at the `O(g²)` level; the alarm is retracted.
- The doubler-free off-shell value `~0.058` per `g²C₂` is `~O(α_s/π)` — the standard
  lattice magnitude (Capitani) — and **generically nonzero**, not zero
  (Groote–Shigemitsu, hep-lat/0001021, who compute exactly this speed-of-light
  renormalization on an anisotropic lattice). So there is **no** "shared-kernel
  kills it" theorem either: the velocity anisotropy is neither `0.3` nor `0`.
- **The status REVERTS to `LORENTZ_NATURALNESS_GAP` (#3123):** `δv ~ O(α_s/4π … α_s/π)`,
  loop- but not Planck-suppressed, **uncomputed at the physical (gauge-invariant
  pole) level**. The high-stakes uncomputed prediction is unchanged; only the
  spurious `0.3` alarm is removed.

## The genuine remaining computation (route 1, now de-bugged)

The corrected target: the framework's actual **staggered** fermion (4 tastes,
doubler-reduced — matching the tree-level free-staggered SO(4) result already on
repo), with **(i)** the **gauge-invariant pole-velocity** condition
`v² = (∂Σ/∂k²)/(∂Σ/∂ν²)` on shell (not the off-shell `A, B`), **(ii)** the species
`C₂`-difference (the observable), and **(iii)** the `(μ/M_Pl)^γ` IR flow over the
Planck-to-lab hierarchy. That yields the actual `δv` to compare against the bounds
— the definite pass/falsify that #3134 named as the real task.

## Methodological note (the owner's instinct, vindicated)

The owner's reasoning — *"too much of the framework works for it to be wrong; we're
missing something"* — was correct: the missing pieces were the **fermion doublers**
and the **pole-velocity condition**. The lesson generalizes: a preliminary lattice
signal must survive (i) a doubler-free action, (ii) a grid-convergence check, and
(iii) a gauge-invariant on-shell extraction before it can be trusted — and an
alarming "falsification" especially demands all three before it is even drafted as
a claim. The prototype correctly stayed a prototype; this note records the
validated retraction. The adversarial (Codex-style) review that independently
reproduced and diagnosed the artifact is the model for checking high-stakes
numerics.

## What this note does NOT claim

- It does **not** claim `δv` is small/zero (it is generically nonzero, `~O(α_s/π)`
  off-shell), nor that the framework passes the Lorentz bounds — that requires the
  de-bugged computation above.
- It does **not** change the #3123/#3134 status; it removes a spurious alarm and
  re-specifies the route-1 computation.
- **No** new axiom, primitive, repo vocabulary, or class tag; literature
  (Groote–Shigemitsu; Capitani) is comparator only. It sets **no** audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner, independently of the prototype): the naive-fermion
  `A` log-divergence (grid growth) and the `B ≡ 0` parity artifact; the Wilson
  doubler-free convergence of `B − A` to `~0.058`; the isotropic-control vanishing.
- **Cited** (comparator only): Groote–Shigemitsu, *PRD* 62 (2000) 014508
  (hep-lat/0001021, speed-of-light renormalization on an anisotropic lattice,
  generically nonzero `O(α_s)`); Capitani, *Phys. Rept.* 382 (2003) 113
  (hep-lat/0211036, lattice one-loop `Z`-coefficients `O(0.01–0.1)·C_F`); the
  framework's own #3123 / #3134 and the free-staggered SO(4) two-point result.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It
does not promote this note or change any audited claim scope.

- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- `LORENTZ_NATURALNESS_IS_A_COMPUTATION_NOT_A_TUNING_NOTE_2026-06-06.md` (the route-1 framing parent, #3134; not yet on main — backticked)

### Source-note boundary

**Hypothesis set:** (1) the spatial-lattice + continuous-time one-loop self-energy
setup (Euclidean Clifford verified); (2) naive vs Wilson (`r=1`, doubler-free) vs
isotropic (4d-symmetric) fermion regulators; (3) Feynman-gauge gluon with the
shared lattice kernel. The result is a numerical validation: the prototype `0.31`
is an artifact; the doubler-free off-shell value is finite `~0.058` per `g²C₂`.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class
tag; only standard terms (fermion doubling, Wilson term, wavefunction
renormalization, pole velocity, BZ grid convergence). No fitted/PDG/`g_bare` value
consumed; the literature is comparator only.

**No-promotion statement:** this note does **not** promote, demote, or set the
audit status of #3123, #3134, or any upstream row. The audit lane is the only
status authority.
