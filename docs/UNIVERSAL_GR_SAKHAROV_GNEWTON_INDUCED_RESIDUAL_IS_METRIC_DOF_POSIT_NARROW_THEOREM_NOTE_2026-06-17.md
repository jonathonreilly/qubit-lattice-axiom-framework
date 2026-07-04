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

## 1. G_Newton is induced (~a²), not a free parameter

The Sakharov mechanism induces gravity from the matter determinant. The leading metric
effective-action terms are the Dirac operator's Seeley–DeWitt coefficients (Gilkey;
`P = −(∇² + E)`, Dirac `E = −R/4` by Lichnerowicz, spinor dim 4 in d=4):

- `a₀ ~ (4π)⁻² · 4` → induced **cosmological constant**, magnitude `~Λ⁴` (the dominant divergence).
- `a₁ = (4π)⁻²·(1/6)·tr(6E + R·I) = −(4π)⁻² R/3` → induced **Einstein–Hilbert** term, magnitude `~Λ²`.

Matching `S_ind ⊃ (4π)⁻²·(1/3)·Λ² ∫R√g` to `S_EH = (1/16πG) ∫R√g`:

> `1/(16πG) ~ (4π)⁻² (1/3) Λ² N_f`  ⟹  **`G ~ 48π³ / (N_f Λ²) ~ a²/N_f`**  (`Λ ~ 1/a`).

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
