# Interacting Emergent Lorentz Conditional Algebra: Supplied One-Loop Velocity Attractor and One-Scalar Gate Boundary

**Date:** 2026-06-06
**Claim type:** open_gate / conditional-support packet
**Type:** conditional-support
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label above is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.py`](../scripts/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.txt`](../logs/runner-cache/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.txt)

---

## 2026-06-12 audit firewall: no bounded-theorem promotion

The audited blocker is real: this note does not derive the interacting
one-loop velocity RG, the spatial-only power-divergent mixing theorem, the
physical fixed-point anomalous dimension, or the coefficient needed to compare
against Lorentz-violation bounds from retained framework primitives. Those
inputs remain supplied model/literature-context inputs in this packet.

Therefore the actual source status is **conditional-support / open gate**, not
`bounded_theorem` or retained-grade interacting Lorentz closure. The useful
content retained here is the runner-checked algebraic consequence: once the
specified one-loop packet is supplied, the speed-difference mode is
IR-attractive, the `O_h` spatial split is one scalar, and canonical time
reduces the Collins gate to one conditional scalar. No new axiom, primitive,
Tier-A admission, or audit status change is introduced.

## 2026-06-18 partial source-side support: spatial-BZ channel only

[`EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md`](EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md)
proves one narrow structural part of residual D directly on the
continuous-time / spatial-`Z^3` surface: the central-difference spatial
artifact begins as `sum_i k_i^4`; its quadratic projection has zero time
component; and the `O_h` orbit average leaves one spatial scalar channel.

This reduces the supplied "spatial-only power-divergent mixing" phrase to an
exact source-side channel theorem plus a still-open coefficient. It does not
derive the interacting one-loop velocity RG, the physical coefficient
multiplying the spatial channel, the fixed-point anomalous dimension, or
sufficiency against Lorentz-violation bounds. The parent row therefore remains
conditional until those remaining bridges are supplied and independently
audited.

## 2026-06-09 surface-scope update

Residual D below (the power-divergent UV regeneration of the marginal anisotropy)
belongs to the **non-isotropic** surface. The approved
`kinetic_isotropy_primitive`
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md))
supplies the OS0 kinetic-form premise `c_t = c_s`; the separate B4 note
([`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md))
handles the marginal anisotropy on that OS0 surface. The conditional one-loop
algebra below remains valid on its own supplied continuous-time/non-isotropic
surface; this pointer only records that its residual is outside the approved OS0
kinetic-form premise. No audit verdict is changed by this pointer.

## 2026-06-07 conditional-algebra scope repair

The current auditable claim is narrower than a retained interacting-Lorentz
naturalness theorem. It is a **conditional one-loop/structural algebra packet**
over supplied inputs:

- supplied one-loop velocity-RG dynamics;
- supplied spatial-only power-divergent mixing/power-counting context;
- supplied Planck-to-IR hierarchy scale used in the illustrative suppression
  estimate.

The runner verifies algebraic consequences of those supplied inputs: attractive
difference-mode flow, `O_h` scalar reduction, canonical-time one-number
reduction, and the form of an illustrative `(mu/M_Pl)^gamma` damping factor.
This note does **not** provide retained one-hop bridges for the one-loop
dynamics, the spatial-only power-divergent mixing theorem, the physical
fixed-point anomalous dimension, or the hierarchy-suppression sufficiency
claim. The hierarchy line is non-load-bearing interpretation unless those
bridges are supplied and independently audited.

## Role

This note is a standalone conditional-algebra packet for the emergent-Lorentz
lane's **interacting radiative-naturalness problem**. It treats spatial `Z^3`,
continuous time, and supplied gauge/Yukawa dynamics as the context under test;
it does not rely on any unlanded tree-level packet as a load-bearing dependency.
Collins–Perez–Sudarsky–Urrutia–Vucetich (*PRL* **93** (2004) 191301) argue that
radiative corrections on a Lorentz-violating (lattice/Planck) cutoff regenerate the
marginal `c_t ≠ c_s` anisotropy at a level not suppressed by `1/M_Pl`, unless a
custodial symmetry protects it. This note is **free + structural** (standard one-loop
coefficients); it adds **no axiom**, and it is explicit about what it does and does
not establish. Runner: **12 PASS / 0 FAIL**.

**Net result inside the supplied one-loop packet.** The residual is **organized**
from "the marginal anisotropy is an O(1), two-parameter, unprotected wall" to "a
single IR-attractive scalar in the conditional model":
1. the interacting gauge dynamics makes `c_t = c_s` an **attractive IR fixed point**;
2. the framework's **canonical continuous time fixes `c_t`** and **`O_h` keeps the
   spatial split a single scalar**, reducing Collins' two-parameter gate to **one
   number `c_s`**;
3. the residual — the power-divergent UV regeneration of that one number —
   admits an illustrative IR-damping factor in the supplied model, but whether
   that factor is the physical fixed-point anomalous dimension and whether it
   beats bounds remains the genuine open problem.

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

- **Establishes** (verified inside the supplied one-loop/structural packet):
  (A) the velocity anisotropy is an attractive IR fixed point for the supplied
  coupled RG form; (B) the spatial split is a single `O_h` scalar; (C)
  canonical time fixes `c_t`, reducing the gate to one number in the model.
  Net: the two-parameter wall is reorganized to one conditional IR-attractive
  scalar.
- **Leaves open** (named, not solved): (D) the exact power-divergent coefficient and the
  anomalous dimension `γ` at the physical fixed point, hence whether the
  flow + Planck-hierarchy suppression beats the LV bounds with no custodial symmetry.
  This is the field-wide UV naturalness problem; this note sharpens it, it does not
  close it.

## What this note does NOT claim

- **No** solution to the Lorentz naturalness problem (residual D stands).
- **No** unconditional emergent-Lorentz theorem; the dynamics is still admitted (the
  interaction is supplied), and the result is one-loop + structural.
- **No** retained hierarchy-suppression conclusion; the `(mu/M_Pl)^gamma`
  factor is an illustrative consequence of the supplied model until the
  physical fixed-point anomalous dimension and power-divergent coefficient are
  derived or otherwise retained.
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
### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the native surface
(spatial `Z³` + continuous time) as supplied context; (3) supplied interacting
dynamics — a gauge/Yukawa coupling `α` (the pre-existing dynamics gate); (4) standard
one-loop velocity-RG structure (the cited literature analogs). The result is one-loop +
structural; the power-divergent coefficient and the fixed-point anomalous dimension are
out of scope (residual D).

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (RG flow, β-function, IR fixed point, anomalous dimension, Reynolds
projector, equal-time CAR, Reisz power-counting). No fitted / PDG / lattice-MC / `β=6` /
`g_bare` value consumed; the literature is comparator/scope.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of the no-go, the emergent-Lorentz notes, or any upstream row. The audit lane
is the only status authority.

## 2026-06-15 audit-unlock residual certificate

This re-audit packet preserves the useful model algebra but refuses the
stronger interacting-Lorentz closure. The runner checks the supplied RG
matrix, the `O_h` one-scalar reduction, and canonical-time bookkeeping.

The unresolved bridge is the source of those supplied continuum inputs in
this framework: an audit-clean one-loop velocity RG authority, a
spatial-only power-divergent mixing theorem, and the physical anomalous
dimension/sufficiency bound. Without those, this row remains conditional
support only. This repair introduces no custodial symmetry, observed bound,
new axiom, or status promotion.

## 2026-06-18 velocity-RG exchange-matrix support

[`EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md`](EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md)
supplies an exact exchange-matrix theorem for the algebraic one-loop
velocity-flow form: given positive mutual-drag coefficients `a,b`, the
common-speed line is fixed, `b v_F + a v_B` is invariant, and the
speed-difference mode has eigenvalue `-(a+b)`.

This retires the algebraic exchange-matrix step in the supplied RG packet. It
does not derive the physical one-loop coefficients from framework
interactions, the spatial-only power-divergent coefficient, the physical
anomalous dimension, or LV-bound sufficiency. No audit status changes here;
the row remains conditional support / open gate until those physical bridges
are supplied and independently audited.
