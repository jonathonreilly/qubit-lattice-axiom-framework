# On-Site Weyl-Boost Generator Algebra From Single-Site Bivectors

**Date:** 2026-06-01
**Claim type:** bounded_theorem
**Claim boundary:** bounded construction. This note verifies the single-site
`so(3,1)` generator algebra from Pauli/Clifford bivectors under a Lorentzian
sign and records the remaining selections: faithful-over-scalar, chirality, and
signature. It does not force the matter representation, derive the `(3,1)`
signature, close spin-statistics, or set an audit verdict.
**Primary runner:**
`scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
with cache
`logs/runner-cache/frontier_koide_onsite_weyl_boost_from_bivectors.txt`
(13/13 checks).

## The boost-embedding gap

The carrier-frame consolidation isolates the spin-statistics route to a fermionic
matter frame, with two located gaps. **Boost embedding:** the qubit's
*spatial* spin-½ (the `su(2)` rotations) is derived
([`PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md`](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md),
retained), but making the qubit a **full Lorentz spinor** — the **boosts** (the
non-compact `so(3,1)` part) — was posited via a *multi-site Grassmann staggered
field that already assumes the fermionic frame*, a boost/statistics circularity (one
assumes fermions to obtain the spinor index needed to force fermions).

## Result: the boosts come off the single-site ℂ², Grassmann-free

The emergent `so(3,1)` boosts are carried on the **single-site** Pauli ℂ² by a
**derived** object — the Cl(3,0) **bivector**
`B_i = (½)γ_jγ_k = i σ_i/2`
([`INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md),
cited bounded authority; built from Clifford **operator**-anticommutation
`{γ_i,γ_j}=2δ_ij`, with **no** field-anticommutation, Berezin, or staggered `χ`).
Verified (runner):

1. **`so(3,1)` closes exactly** on ℂ² with `J_i = σ_i/2` (rotations) and
   `K_i = B_i = iσ_i/2` (boosts): `[J,J]=iεJ`, `[J,K]=iεK`, and the load-bearing
   **non-compact sign** `[K,K] = −iεJ` (§B).
2. **Anti-Hermiticity is forced** by the Lorentzian `(3,1)` sign: a *Hermitian*
   boost `K=σ/2` gives `[K,K]=+iεJ = so(4)` (compact), not `so(3,1)` (§C). So
   once boosts act, `K` *must* be the anti-Hermitian bivector `iσ/2`.
3. **Rep-uniqueness:** `so(3,1)` is simple and perfect, so any **faithful** 2-dim
   rep is `sl(2,ℂ)` = the **Weyl** spinor; `{J,B}` is genuinely 6-real-dimensional
   (real rank 6), traceless, faithful. The only non-faithful 2-dim alternative is
   the **trivial scalar** `J=K=0`. So once faithful, the boosts are forced — up to
   the chirality binary `(½,0)` vs `(0,½)` (§D).

**This lifts the boost operators off the Grassmann crutch** (a strict improvement
in kind), and it is **non-circular w.r.t. spin-statistics**: the construction
assumes *no* statistics, so a spin-statistics argument can force CAR downstream
on a *given* faithful spinor -- breaking the boost/statistics circularity.

## What stays posited (honest residual)

The boost-embedding gap is **partially lifted, not closed**. The boost
*operators* are forced and
Grassmann-free, but three selections remain admitted:

- **Faithfulness selection (primary).** Emergent-spacetime *admits* the
  faithful (boost-acting) Weyl rep and *uniquely* identifies it once faithful, but
  does **not** force faithful-over-trivial: matter could equally sit in the scalar
  rep `J=K=0`. **The dynamics lever provably fails to force it** — the native
  single-component staggered `D` gives `H=iD` **spin-blind**
  (`[H⊗I_2, I⊗B_i]=0`, §E), so it generates only the spin-blind *orbital* boost;
  and **no** single 2×2 `G` anticommutes with all three Paulis (no on-site `γ⁰`,
  hence no on-site boost-*spin* part `S^{0i}`;
  [`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md),
  cited no-go authority). So the faithful-vs-scalar bit is the genuine residual posit.
- **(G2) Chirality** `(½,0)` vs `(0,½)`: a free binary (Schur-inequivalent on the
  irreducible ℂ²), **shared with the generation-ID chirality gate**.
- **(G3) The `(3,1)` signature** itself reduces (via
  [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md),
  retained) to the single binary `ε=e_4²=−1`, **delegated to
  `anomaly_forces_time` — which is unaudited on the live ledger (invalid as
  load-bearing)** — so even the signature is currently posited.

## What this buys

The gap is **sharpened** from "construct a multi-site spinor index" to a **single
binary selection** (faithful vs trivial) plus two attached binaries (chirality,
signature). And the circularity is **broken in kind**: the Grassmann crutch posits
the *fermionic frame* (the very thing spin-statistics must force), whereas the bivector
soldering posits no statistics. The native real anti-Hermitian
`D = iH`
([`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
cited bounded authority) supplies the time/space-mixing dynamics, but spin-blindly
(§E) — so it does not yet select the faithful rep.

## Non-circularity and scope

No `Q=2/3`, no `r=1/2`, no fermionic frame is assumed (the construction is pure
Clifford operator algebra on ℂ²). This note **does not** claim the boost-embedding gap is fully lifted;
it lands the on-site boost *construction* and states the residual selections
explicitly.

## Boundary (the next path)

Two concrete forcing levers for the residual, neither routing through the
unaudited `anomaly_forces_time`: **(1)** couple the faithful-vs-scalar selection to
**microcausality / spin-statistics** — exclude the scalar by the same engine
that excludes the bosonic frame, so the boost-acting rep is selected by the same
forcing that gives CAR; **(2)** derive `ε=−1` (the timelike sign) from
**reflection-positivity / KMS** on the records-emergent time, discharging the
signature posit. Test whether `[H, K_i]` can be made to reproduce the `iso(3,1)`
boost-Hamiltonian bracket `[H,K_i]=iP_i` (currently `=0` identically on-site,
which is *why* the selection is not yet forced).

## Load-bearing authorities

[INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md),
[PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md),
[CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md),
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
and
[NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md).

Non-load-bearing open signature context remains plain text:
`anomaly_forces_time`.
