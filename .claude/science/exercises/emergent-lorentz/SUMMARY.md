# /exercise — Emergent Lorentz Invariance (SUMMARY)

**Date:** 2026-06-06 · **Slug:** emergent-lorentz · **Subagents:** 5 (max-reasoning) · **Literature:** yes

## Wall (neutral)
Emergent Lorentz is the sole remaining residual of the FS/boost-spinor chain (Link C),
after the two functional-analysis blockers beneath it were repaired (#3011 RP Wilson
temporal-gauge sign; #3015 free-Dirac Poincaré self-adjointness). Can the continuum
Lorentz/Dirac structure — especially the **boost-spinor** and the **emergent speed of
light** — be derived from {Lattice=Z³, Quantum, Record}+Planck (+supplied dynamics)
with no new principle, or is it an irreducible admission?

## The decisive structural finding (all 5 agents converged)
Emergent Lorentz factors into THREE pieces with very different status:
1. **Spatial isotropy** — already retained_bounded: dim-6 LV, CPT+P protected, ℓ=4 cubic harmonic.
2. **Boost-spinor / Poincaré self-adjointness** — repaired (#3015); generators close from Cl(3,0)→Cl(3,1) bivectors.
3. **The marginal (dimension-2) time/space normalization `c_t = c_s`** (the emergent speed of light) — today's no-go (`spatial_cubic_time_anisotropy_gate_no_go`) shows spatial O_h does NOT fix it; only SO(4)/4D-hypercubic does.

**Piece 3 is the genuine residual — BUT it is an artifact of putting a lattice on TIME.**
The Lattice axiom is `Z³` (space only). A temporal lattice `Z_τ` (the spacing `a_τ` that
manufactures the second coefficient `c_t`) is NOT axiomatic. On the framework's **native
surface** (spatial Z³ + continuous time from a self-adjoint Hamiltonian — the surface the
retained `lorentz_boost_covariance_2d/3plus1d` theorems already use), the quadratic kinetic
invariant space is ONE-dimensional (one speed `c`), so the marginal gate never arises.

## What was built
- **Runner** `scripts/frontier_emergent_lorentz_continuous_time_marginal_gate_dissolution_2026_06_06.py` (16/16 PASS):
  invariant counting (spatial O_h → dim 1; O_h×time-parity → dim 2; B_4 → dim 1); continuous-time
  dispersion (one speed, isotropic, first anisotropy dim-6 c₄=−1/3); Euclidean contrast + a_τ→0 collapse;
  so(3,1) boost closure; honest controls.
- **Note** `docs/EMERGENT_LORENTZ_CONTINUOUS_TIME_MARGINAL_GATE_DISSOLUTION_NOTE_2026-06-06.md` (bounded_theorem).

## Honest residuals (named, NOT solved)
1. **Dynamics admission** — continuous-time Hamiltonian is supplied (pre-existing record-production gate); cheaper than the no-go's 4D-hypercubic salvage, not new.
2. **Interacting radiative naturalness** (Collins et al, PRL 93 (2004) 191301) — loops on a Planck-cutoff lattice regenerate marginal LV at O(1) without a custodial symmetry. The free/tree result does NOT address this; it is the deeper field-wide open question. Candidate route: interacting IR fixed point (Bednik–Pujolàs–Sibiryakov 2013; Gross–Neveu–Yukawa).
3. **P2 Euclidean magnitude debt** — the Euclidean branch carries the α_LM magnitude; the native route owes a separate derivation (Record K/CPT temporal 2-fold candidate).

## Ranked route portfolio
| Rank | Route | Status if successful | First artifact | Stop condition |
|---|---|---|---|---|
| 1 | **Continuous-time dissolution** (BUILT) | bounded_theorem: marginal gate dissolved on native surface | the runner above (DONE, 16/16) | landed; residual = dynamics gate + interacting naturalness |
| 2 | Anisotropy RG β-function (interacting) | retained if β<0 attractor on framework's β=6 vertex | block-spin dξ/d log b on free + plaquette vertex | β=0 marginal line ⇒ no-go fundamental; β<0 ⇒ escapable |
| 3 | Modular/Bisognano-Wichmann | NO-GO (circular): geometric modular action ⇔ relativistic normalization | modular-flow geometric test on lattice wedge | confirms BW presupposes c_t=c_s |
| 4 | Record K/CPT temporal 2-fold | pays the P2 magnitude debt natively | K/CPT-orbit factor-2 vs α_LM | reproduces v-match or not |
| 5 | Boost-spinor partner-chirality delivery | closes the massive-Dirac boost rep | R-reconstruction (massive partner) | orthogonal to c_t=c_s |

## Verdict
A genuine **positive bounded theorem** (route 1, built): the marginal `c_t/c_s` gate is dissolved
on the framework's native continuous-time surface with **no new principle** beyond the pre-existing
dynamics gate. The free emergent-Lorentz residual reduces to the already-retained dim-6 spatial LV +
the boost-spinor (#3015). The honest frontier is now (2) the interacting radiative-naturalness problem
— a field-wide hard question, the right next target if pushing further.

## Do NOT
- Claim emergent Lorentz "solved" — residuals 1–3 stand, especially (2).
- Contradict the no-go — it correctly scopes the Euclidean route; route 1 selects the native one.
- Cite modular/BW as forcing c_t=c_s — it is circular for this purpose (route 3).
