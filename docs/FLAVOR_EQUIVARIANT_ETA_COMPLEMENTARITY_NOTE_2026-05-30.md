# Flavor — the equivariant-η / spectral-asymmetry route reduces to the chirality gate via an exact complementarity (and 2/9 is not an η)

**Date:** 2026-05-30
**Claim type:** bounded result (η-retrapped, provisional) + a structural complementarity + the 2/9 disambiguation.
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_equivariant_eta_complementarity_2026_05_30.py` (SCORECARD PASS=5).
**Source:** 11-agent build `wf_f105c938` (map → 3 operator constructions → adversarial scrutinize → lit) — all three builds independently land η-retrapped; all three verdicts refute; lit confirms no literature mechanism supplies the breaking.

## Question
Can the equivariant APS-η / Z_N spectral-asymmetry route, realized as a **native** framework
Dirac operator, *force* the C₃-equivariance-breaking orbit-splitting chiral grading on the
hw=1 generation triplet (→ Koide Q=2/3), landing the `L₃(1,2)=2/9` weight — escaping the
circulant wall of `koide_z3_equivariant_anticommuting_no_go` (retained_bounded)?

## Answer — η-retrapped: the route reduces to the chirality gate, via an exact complementarity
The decisive new structural fact:
- **On the single generation R³, η is alive but the operator is forced circulant** (breaking
  impossible). R is multiplicity-free (eigs `1,ω,ω²`), so its commutant is exactly the 3-dim
  circulant algebra; `comm(R) ∩ anticomm(Γ_χ) = {0}` because `Γ_χ=(2/3)J−I` is itself circulant.
  An η-driven zero crossing of a commuting family genuinely jumps (e.g. `η_R: 0→−2` at the k=0
  crossing), but the operator stays circulant on both sides — η lives precisely where breaking is impossible.
- **On the C²-tensored factor, breaking becomes possible but η is identically zero.** The only
  dodge of the bare-R³ no-go is the tensor-coin extension `D=I₃⊗σ_x`, `g=R⊗I`, grading `Γ_χ⊗σ_z`,
  which satisfies `[D,g]=0` **and** `{D,grading}=0` simultaneously — but its spectrum is `±`-symmetric
  (`{−1,−1,−1,+1,+1,+1}`), so `η_R=η_grading=0` for all parameters. The index forces nothing, and
  the σ_z coin grading is itself the unsupplied C₃-orbit-splitting chiral import (the no-go's Escape Hatch II).

> **η is loud exactly where breaking is impossible; η is silent exactly where breaking is possible.**

The Γ_χ-graded equivariant index of R is nonzero (`tr(R|₊)−tr(R|₋) = 1−(−1) = 2`) but is the
**wrong obstruction**: `[R,P₊]=[R,P₋]=0`, so both eigenspaces are R-invariant and the index is
saturated by the C₃-**symmetric** vacuum — it mandates no breaking. (Lit-confirmed: every relevant
theorem — Donnelly equivariant APS, APS-III ρ, lattice-index = spectral-flow arXiv:2407.17708,
anomaly inflow / Callias — *counts* a symmetry-**preserving** operator and takes the sign-changing /
Wilson mass as a **separate input**. Positing "η forces the chiral grading" would import a mechanism
absent from the math — a wrong-escape-via-citation and a no-imports violation.)

## The 2/9 disambiguation (answers "no coincidences" precisely)
| object | value | category |
|---|---|---|
| `L₃(1,2)` (Lefschetz fixed-point weight of R's two nontrivial chars) | 2/9 | dimensionless rational; natively forced by R |
| `(N−1)/N²` at N=3 (Koide variance / CKM-Bernoulli family) | 2/9 | **same rational function** — a genuine structural family in dimensionless-rational space |
| `η_g(T)` | ∈ **Z[ζ₃]** (algebraic integers) | 2/9 has minpoly `9x−2` (non-monic) → **2/9 ∉ Z[ζ₃]**; η can *never* equal 2/9 |
| `δ_Brannen` | 2/9 **rad** | a radian phase; separated from dimensionless 2/9 by retained_no_go `koide_a1_radian_bridge_irreducibility` (transcendence of π) |
| `Q` | 2/3 | requires the separate `r=1/2` pin **and** the signed readout; `2/9 ≠ 2/3`, logically independent |

So: the two 2/9's **are** structurally the same object *within* dimensionless-rational space (the
`(N−1)/N²` family — not a coincidence). But 2/9 is a geometric *weight/density*, **not** an η value,
and **not** Q=2/3; and the crossing to the radian phase `δ_Brannen=2/9 rad` is the **pun**, blocked
by the retained radian-bridge no-go (π transcendental).

## Stale-citation flags (verified vs origin/main ledger)
- Load-bearing & retained_bounded: `axiom_first_z_n_equivariant_spectral_asymmetry`,
  `new_parity_is_circulant_phase`, `koide_z3_equivariant_anticommuting_no_go`;
  `koide_a1_radian_bridge_irreducibility` = retained_no_go.
- The downstream phenomenology routes `koide_phase_aps_eta_parity_route` and
  `koide_emergent_time_eta_conjugation_parity` are **unaudited — not load-bearing.**

## Sharpest next path (off the index/η axis — not a closing framing)
The complementarity names exactly what is needed: a **non-index, native invariant that is nonzero
on the tensor-coin sector where η vanishes** — one living on the qubit `M₂(C)` factor (already
native), sensitive to the σ_z grading without requiring `±`-spectral symmetry. The candidate is a
**qubit-factor Berry / holonomy phase**: a Berry phase is nonzero precisely on a degenerate-block
adiabatic loop where η is blind, and it is **natively radian-valued** — the one object class that
could simultaneously source the missing odd term on the auxiliary factor **and** collapse the
dimensionless-weight → radian-phase wall that blocks `2/9-weight → 2/9-rad`. Concrete probe (not yet
run): compute the qubit-factor Berry holonomy of the adiabatic loop `δ: 0→2π` of the mass-embedded
circulant `H(a,|b|e^{iδ})` on `R³⊗C²`, and test (a) whether it equals `2/9` (in radians) and
(b) whether its value is `r=1/2`-selective. That single quantitative check has not been run and does
not presuppose a closeable search space.
