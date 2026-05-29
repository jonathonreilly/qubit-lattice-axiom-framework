# Koide last mile — the chirality bridge is a no-go (chirality is an import)

> **d=3+1 CONFIRMATION + escape retraction (2026-05-28) — runner
> `koide_chirality_d3plus1_correction_2026_05_28.py`.** A floated escape (a
> spin-taste `γ₅⊗ξ₅` chirality with `ξ₅` acting on a 4-dim taste sector) was
> a **d=4 Euclidean artifact**. The framework is **d=3+1** (Z³ space +
> emergent time): only 8 spatial corners, NO 16-corner / 4-dim taste. In the
> correct structure the no-go is ROBUST: native chirality `C=(−1)^{x+y+z}` is
> a function of Hamming weight, hence **S₃-invariant → uniform on the hw=1
> generation orbit**, so it cannot anticommute with `Γ_χ` (which needs
> S₃/C₃-breaking); and the 3+1 Dirac Hamiltonian is gapped (`H²=|k|²+m²` →
> index 0, wall W1). The escape dissolves; chirality remains an import.

**Date:** 2026-05-28
**Claim type:** bounded_theorem / no-go (the spacetime→generation chirality
bridge). Imports nothing; promotes nothing; sets no retained status.
Local-branch working note (campaign last-mile, next step).
**Runner:** `scripts/koide_chirality_bridge_nogo_2026_05_28.py`;
cache `logs/runner-cache/koide_chirality_bridge_nogo_2026_05_28.txt`.
**Resolves the next step from** `KOIDE_Q23_DERIVED_MODULO_CHIRALITY_LAST_MILE_NOTE_2026-05-28.md`
and **corrects its GW framing.** Cross-confirmed by the sister
generation-identification lane (escape-hunt `w04q06x5l`, three-wall no-go;
wall 3 = retained R3-S1 "functorial anomalies can't split the C₃ orbit").

## The question
Can the framework's existing chirality machinery (`anomaly_forces_time` →
spacetime γ₅) be *transported* to supply the generation-sector chiral
operator that forces Koide Q=2/3 — i.e. a Hermitian operator on the
generation R³ anticommuting with the grading `Γ_χ=(2/3)J−I`, carrying the
√mass vector as a nonzero eigenvector? **Build it or refute it.**

## Verdict: NO-GO. Generation-sector chirality is an independent import.
1. **The Koide chiral operator must break C₃-equivariance.** Retained
   no-go `koide_z3_equivariant_anticommuting`: `comm(S) ∩ anticomm(Γ_χ) =
   {0}`. So a nonzero chiral H (`{H,Γ_χ}=0`) necessarily has `[H,S]≠0`.
2. **Spacetime γ₅ acts C₃-trivially → cannot supply it.** `anomaly_forces_time`
   gives γ₅ on the *spacetime* factor; on the generation index it acts as
   `γ₅ ⊗ G`. Anticommuting with `I ⊗ Γ_χ` requires `{G,Γ_χ}=0` on the
   generation factor. But every spacetime-supplied or C₃-equivariant `G`
   (`I_gen`, `S`, the Cl(3) bivector `S−Sᵀ`, …) **commutes** with `Γ_χ`
   (verified: `{G,Γ_χ}≠0`, `[G,S]=0`). The C₃-orbit-splitting
   (non-equivariant) operator chirality needs is **not** produced by any
   functorial/spacetime structure.
3. Therefore the spacetime-γ₅ → generation-`Γ_χ` **bridge does not exist**;
   the generation-sector chiral grading is an **independent primitive** that
   A1+A2+retained do not supply.

## Correction to the prior "no Ginsparg-Wilson" framing
The last-mile note attributed the gap partly to "staggered Z³ has no
Ginsparg-Wilson relation." That is **not the operative reason** — GW is
*sufficient, not necessary*. The sharp obstruction is C₃-equivariance: any
chiral grading anticommuting with `Γ_χ` must split the C₃ generation orbit,
and no functorial/spacetime operator does. (Same correction the sister
generation-ID lane recommends; their three walls are: (1) internal ε-grading
self-gaps `H(m)²=K²+m²` ⇒ spectral-flow=0; (2) the only available anomaly =
Euler characteristic χ=0 on the flat torus; (3) R3-S1 retained, functorial
anomalies can't split the C₃ orbit. Wall 3 is the Koide-side obstruction
verified here.)

## Consolidated status of charged-lepton Koide Q=2/3
**`derived-modulo-chirality`, with the chirality now a *confirmed* no-go to
derive from A1+A2+retained:**
- **Forward (retained, non-circular):** a chiral mass operator (anticommuting
  with `Γ_χ`) ⟹ Q=2/3 exactly. Q=2/3 is the *signature of chiral (Dirac)
  mass generation*; the non-chiral default (Z₃-equivariant circulant) gives
  Q=1.
- **The gate (now pinned):** that chirality is an **independent import** — a
  generation-sector chiral grading that breaks C₃-equivariance, *not*
  transportable from spacetime γ₅ (this note) and *not* present in
  A1+A2+retained (retained no-go).

So "why Q=2/3" is fully reduced to a single, sharp, *confirmed* import: an
independent chiral grading on the generation factor. The framework does not
supply it; positing it is a user-approval-required new primitive. With it,
charged-lepton Koide closes to `derived`; without it, the framework's
honest default is Q=1.

## Significance
Koide-2/3 and generation-identification chirality are now provably **one and
the same gate** (both require the C₃-orbit-splitting chiral grading;
spacetime chirality cannot transport over). Two of the framework's hardest
open problems collapse to a single import. This is the clean endpoint of the
charged-lepton Koide derivation program on the current axiom set: **derived
modulo one named, confirmed-irreducible chirality import.**

## Status
No-go on the bridge (chirality not transportable / not native). Koide
Q=2/3 = `derived-modulo-chirality`; the chirality is a single confirmed
import shared with the generation-identification gate. No closure without
that import; no false closure claimed.
