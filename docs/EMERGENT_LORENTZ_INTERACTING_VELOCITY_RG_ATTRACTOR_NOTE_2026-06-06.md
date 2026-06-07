# Interacting Emergent Lorentz: the Velocity Anisotropy is an Attractive IR Fixed Point, and the Naturalness Gate Reduces to One Number

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The `bounded_theorem` label is a source-side
claim-boundary declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.py`](../scripts/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.txt`](../logs/runner-cache/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.txt)

---

## Role

This note attacks the **deepest** residual of the emergent-Lorentz program: the
**interacting radiative-naturalness problem**, named as "honest residual #2" of the
tree-level result `EMERGENT_LORENTZ_CONTINUOUS_TIME_MARGINAL_GATE_DISSOLUTION_NOTE_2026-06-06`
(continuation of a `/exercise` pass; packet at `.claude/science/exercises/emergent-lorentz/`).
Collins–Perez–Sudarsky–Urrutia–Vucetich (*PRL* **93** (2004) 191301) argue that
radiative corrections on a Lorentz-violating (lattice/Planck) cutoff regenerate the
marginal `c_t ≠ c_s` anisotropy at a level not suppressed by `1/M_Pl`, unless a
custodial symmetry protects it. This note is **free + structural** (standard one-loop
coefficients); it adds **no axiom**, and it is explicit about what it does and does
not establish. Runner: **12 PASS / 0 FAIL**.

**Net result.** The deepest residual is **reclassified** from "the marginal anisotropy
is an O(1), two-parameter, unprotected wall" to "a **single, IR-attractive,
hierarchy-suppressed number**":
1. the interacting gauge dynamics makes `c_t = c_s` an **attractive IR fixed point**;
2. the framework's **canonical continuous time fixes `c_t`** and **`O_h` keeps the
   spatial split a single scalar**, reducing Collins' two-parameter gate to **one
   number `c_s`**;
3. the residual — the power-divergent UV regeneration of that one number — is
   IR-suppressed by the attractive flow over the `a⁻¹ = M_Pl` hierarchy, but not by a
   custodial symmetry: the genuine, sharpened, open problem.

## (A) The velocity anisotropy is an attractive IR fixed point — verified

For a Dirac fermion (speed `v_F`) coupled to a gauge/Yukawa boson (speed `v_b`), the
one-loop coupled velocity RG is

```text
    dv_F/dl = C_F α (v_b − v_F),    dv_b/dl = C_B α N_f (v_F − v_b),
```

so the difference obeys `d(v_F − v_b)/dl = −(C_F + C_B N_f) α (v_F − v_b)`. Hence
`η = v_F/v_b` flows to **1 from any initial ratio**, with linear-stability eigenvalue
`−(C_F + C_B N_f) α < 0` (runner Part A: convergence from `η₀ ∈ {0.3,0.6,1.8,3.0}`;
the common-speed direction is marginal — the overall `c` is set by the scale
primitive, not by the flow). The marginal **speed-difference operator is
IR-irrelevant**: Lorentz invariance emerges dynamically. This is the standard
mechanism — Chadha–Nielsen (*Nucl. Phys.* B217 (1983) 125), Nielsen–Ninomiya, the
rigorous graphene result of Giuliani–Mastropietro–Porta (*Ann. Phys.* 327 (2012) 461),
and Roy–Juričić–Herbut (*JHEP* 04 (2016) 018) — here applied to the framework's
asymptotically-free gauge sector.

## (B) `O_h` keeps the spatial split a single scalar — verified

The spatial self-energy renormalization is an `O_h`-invariant symmetric `3×3` tensor.
The space of such tensors is **one-dimensional** (multiples of `δ_{ij}`; runner Part B,
Reynolds projection rank 1), so the regenerated spatial Lorentz violation is a **single
scalar `c_s`**, not a tensor — the three spatial speeds stay equal (`O_h`-protected,
consistent with the dim-6 `ℓ=4` structure of the retained emergent-Lorentz note).

## (C) Canonical continuous time fixes `c_t` — the gate reduces to one number

On the framework's native surface, time is continuous and the equal-time
`{ψ_x, ψ†_y} = δ_{xy}` CAR is preserved by unitary Stone evolution `U(t) = e^{−iHt}`
(runner Part C1: `U U† = I` to `7×10⁻¹⁶`). The time-kinetic coefficient is therefore
renormalized **only** by wavefunction rescaling `Z_ψ` — it is not an independent
velocity, so `c_t ≡ 1` by canonical normalization (Part C2: CAR-norm and `c_t` rescale
by the same `Z`). Consequently **all** of the velocity renormalization lives in `c_s`:
Collins' two-parameter `(c_t, c_s)` gate **reduces to one number** `c_s` (relative to
the canonical `c_t = 1`), and by (A) that number flows to 1 (Part C3). Canonical time
closes half the gate kinematically; `O_h` makes the other half a single scalar; the
interacting flow drives that scalar to the Lorentz-invariant value.

## (D) The honest residual — power-divergent UV regeneration (scoped, NOT solved)

The β-function (A) controls the **logarithmic** running. The genuine Collins problem is
the **power-divergent** UV piece: the lattice's own dimension-6 anisotropy (coefficient
`~ a²/3`, the retained emergent-Lorentz result) feeds the marginal `c_s` through a
spatial power-divergent loop, giving `δc_s ~ O(α/4π)` — **loop-suppressed but not
Planck-suppressed** (runner Part D1). By Reisz lattice power-counting (continuous time,
spatial BZ cutoff) this power divergence is **spatial-only**, so it shifts `c_s` but not
the canonical `c_t` — confirming the one-number reduction — and it is **not forbidden**
by CPT (the split is CPT-even), `O_h` (permits it), or any gauge Ward identity (which
does not tie `c_t` to `c_s`).

The attractive flow (A) gives an **additional power-law IR suppression**
`|η − 1|_IR ~ |η − 1|_UV · (μ/M_Pl)^γ` with `γ = (C_F + C_B N_f) α > 0` (runner Part D2;
Bednik–Pujolàs–Sibiryakov *JHEP* 1311 (2013) 064). Whether this — together with the
framework's exact `a⁻¹ = M_Pl` EFT/LV scale separation (Belenchia–Gambassi–Liberati,
*JHEP* 06 (2016) 049) — suffices against the experimental LV bounds **without** a
custodial symmetry is the **genuine open problem** (Part D3). The cheapest candidate
closer is that Planck-scale separation, which the framework **already has** (not a new
symmetry); SUSY (Nibbelink–Pospelov, hep-ph/0502106) would also work but is
overkill/absent (Part D4).

## What this note establishes vs leaves open

- **Establishes** (verified): (A) the velocity anisotropy is an attractive IR fixed
  point (marginal operator IR-irrelevant); (B) the spatial split is a single `O_h`
  scalar; (C) canonical time fixes `c_t`, reducing the gate to one number that flows to
  the Lorentz value. Net: the two-parameter O(1) wall is reclassified to one
  IR-attractive, hierarchy-suppressed number.
- **Leaves open** (named, not solved): (D) the exact power-divergent coefficient and the
  anomalous dimension `γ` at the physical fixed point, hence whether the
  flow + Planck-hierarchy suppression beats the LV bounds with no custodial symmetry.
  This is the field-wide UV naturalness problem; this note sharpens it, it does not
  close it.

## What this note does NOT claim

- **No** solution to the Lorentz naturalness problem (residual D stands).
- **No** unconditional emergent-Lorentz theorem; the dynamics is still admitted (the
  interaction is supplied), and the result is one-loop + structural.
- **No** contradiction of the no-go (`spatial_cubic_time_anisotropy_gate_no_go`, the
  Euclidean route) or of `dm_continuum_limit_velocity_note` (an unrelated
  wave-deflection observable).
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG / fitted /
  `β=6` / `g_bare` input. Literature is comparator/scope only.
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): the attractive coupled velocity RG flow (`η → 1` from all
  initial ratios; negative difference-mode eigenvalue; marginal common-speed direction);
  the `O_h`-invariant-tensor dimension `= 1` (Reynolds projection → `∝ δ_{ij}`); the CAR
  preservation under Stone evolution and the `c_t`-fixing/one-number reduction; the
  loop-vs-Planck suppression scaling and the `(μ/M_Pl)^γ` IR factor.
- **Cited** (comparator/scope only, never a derivation input): Collins et al *PRL* 93
  (2004) 191301; Chadha–Nielsen *Nucl. Phys.* B217 (1983) 125; Nielsen–Ninomiya;
  Giuliani–Mastropietro–Porta *Ann. Phys.* 327 (2012) 461 (arXiv:1107.4741);
  Roy–Juričić–Herbut *JHEP* 04 (2016) 018 (arXiv:1510.07650); Bednik–Pujolàs–Sibiryakov
  *JHEP* 1311 (2013) 064; Belenchia–Gambassi–Liberati *JHEP* 06 (2016) 049
  (arXiv:1601.06700); Nibbelink–Pospelov hep-ph/0502106; Reisz (lattice power-counting,
  *CMP* 1988).

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It does
not promote this note or change any audited claim scope.

- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- `EMERGENT_LORENTZ_CONTINUOUS_TIME_MARGINAL_GATE_DISSOLUTION_NOTE_2026-06-06.md` (the tree-level parent; not yet on main — backticked to avoid a broken citation-graph edge)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the native surface
(spatial `Z³` + continuous time) of the tree-level parent; (3) supplied interacting
dynamics — a gauge/Yukawa coupling `α` (the pre-existing dynamics gate); (4) standard
one-loop velocity-RG structure (the cited literature analogs). The result is one-loop +
structural; the power-divergent coefficient and the fixed-point anomalous dimension are
out of scope (residual D).

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (RG flow, β-function, IR fixed point, anomalous dimension, Reynolds
projector, equal-time CAR, Reisz power-counting). No fitted / PDG / lattice-MC / `β=6` /
`g_bare` value consumed; the literature is comparator/scope.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of the no-go, the emergent-Lorentz notes, the tree-level parent, or any upstream
row. The audit lane is the only status authority.
