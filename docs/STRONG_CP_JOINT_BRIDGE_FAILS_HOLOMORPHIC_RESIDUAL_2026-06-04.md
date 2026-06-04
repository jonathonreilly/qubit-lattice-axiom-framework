# Strong-CP — the joint-basis bridge fails: θ̄ is not forced to zero (the emergent-time antiunitary is reflection-composed and anomaly-blind), and the single residual is a holomorphic generation coupling — the same unbuilt brick as Koide Q=2/3 and generation-ID

**Date:** 2026-06-04
**Claim type:** a no-go / load-bearing-blocker evaluation (the strong-CP joint-basis bridge fails; θ̄ survives) + a triple-convergence identification (the residual is one shared brick). Not a strong-CP solution.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade. It does not edit, re-cite, or promote any existing row.
**Runner:** `scripts/strong_cp_joint_bridge_holomorphic_residual_2026_06_04.py` (SCORECARD 6/6).

## The bridge and why it fails
The mass half of strong-CP needed a **joint-basis bridge**: that the gauge-OS reflection `Θ_OS` (which reals
the Wilson measure / constrains `θ_QCD`) is the *same* global emergent-time antiunitary as the generation
conjugation-parity `P` (which Hermitianizes `M` / constrains `arg det M`), so a single K-real basis would pin
the physical, anomaly-invariant `θ̄ = θ_QCD + arg det M`. **It does not close.**

- **Sector-disjoint, not one operator.** `Θ_OS` acts on the gauge links and restricts to the *identity* on the
  generation index; `P` acts on the generation index and restricts to the *identity* on gauge links. A global
  `Θ = Θ_OS ⊗ P` can be *written* (so a joint Θ-real basis trivially exists), but it is an **admitted splice**
  of two logically independent operations, not forced by any retained primitive.
- **Reflection-composed → `θ̄` survives.** The decisive parity rule is `Θ(iQ)Θ⁻¹ = −i(RQR)`: the CP-odd density
  is Θ-**odd** (forced 0) only under a **pure-K** antiunitary (`R=I`, no geometric reflection). But pure-K is
  **unavailable** — `conj(M) ≠ M` for complex `b` (the retained Koide radius `|b|²/a²=1/2` lives *off* the real
  axis), so only the reflection-composed `P` (`P M(b) P = M(b̄)`) is a symmetry, and under it the density
  `G=i(C−C²)` is **even** (`P conj(G) P = +G`, verified) while pure-K would make it odd (`conj(G)=−G`, verified).
  Reflection-composed ⊗ reflection-composed = reflection-composed, never pure-K. So `θ̄` is Θ-**even** and
  survives.
- **Anomaly-blind.** `θ̄` is the anomaly-invariant (an axial rotation `M→e^{iα}M` shifts `arg det M` by `+nα`
  and, via the Fujikawa Jacobian, `θ_QCD` by `−nα`, leaving `θ̄` fixed — verified). The rotation acts on
  *fermions*, not gauge links, so the Wilson measure stays real (α-invariant); the two reality conditions do
  **not** co-move. The gauge-side footprint (the topological Jacobian) is `Θ_OS`-odd and *cancels* in the
  reflected expectation — the very mechanism that would let `Θ_OS` detect the rotation makes it invisible. So
  joint Θ-reality does not see the anomaly; the loophole stays open.

The most the joint K-real + real-Wilson basis delivers is `arg det M ∈ {0,π}` — a discrete `sign(det M)` datum
set by mass magnitudes, *not* pinned to the CP-conserving 0, and chiral-removable in any case.

## The single residual — and the triple convergence
What `θ̄=0` requires is a **global pure-K** antiunitary: entrywise/anti-holomorphic conjugation with **no**
compensating geometric reflection, that is (a) a genuine emergent-time symmetry, (b) one Θ across gauge+matter,
and (c) anomaly-*covariant* (odd on the axial rotation, i.e. on the invariant `θ̄` itself). Concretely this needs
a **genuinely complex/holomorphic generation coupling** that breaks `coeff(C²)=conj(coeff(C))`, so that
`conj(M)=M` becomes available *without* the transpose-similarity `P`.

This is **exactly** the holomorphic polarization the retained `koide_emergent_time_eta_conjugation_parity` note
flags as open future work (it states its `P` is a transpose-similarity, *not* an independent holomorphic
polarization). And it is the **same chiral-grading gate** as:
- **Koide Q=2/3** (the value reduces to the holomorphic-vs-real reading of the doublet coupling), and
- **generation identification** (a chiral grading on the generation R³ factor that spacetime γ₅ cannot
  transport over).

So **three of the framework's hardest gates — strong-CP `θ̄=0`, Koide Q=2/3, and generation-ID — reduce to one
unbuilt brick: a chiral/holomorphic grading on the generation R³ factor.** That is the high-leverage structural
finding: the residual is shared, not three separate imports.

## Honest standing
The framework does **not** force `θ̄=0` (strong-CP remains a genuine admission, shared with the SM). The
joint-basis bridge is conclusively evaluated as reflection-composed + anomaly-blind on the full gauge+matter
carrier, with `θ̄` surviving — robust regardless of whether one splices the sector antiunitaries. The value is
the precise localization of the residual to one shared chiral/holomorphic generation brick.

## The next paths this opens (not closing)
- **The shared brick:** attempt to derive (or admit) a genuinely complex/holomorphic generation coupling /
  chiral grading on R³ — a single import that would serve strong-CP, Koide Q=2/3, and generation-ID at once
  (high leverage). Spacetime γ₅ provably does not transport onto the generation factor (retained no-go).
- **Quark transport:** re-derive the matter sector on `M_u, M_d` (where `θ̄=arg det(M_u M_d)` physically lives);
  the lepton-circulant `P` likely has no clean analog there, reinforcing non-closure.

## Provenance (verified 2026-06-04)
- `θ̄` anomaly-invariance (`d(arg det)=nα`, `θ̄` fixed under the Fujikawa shift); `conj(G)=−G` (pure-K odd) vs
  `P conj(G) P=+G` (reflection-composed even); `conj(M)≠M` for complex `b` with `P M P = M(b̄)`; sector-disjoint
  `Θ_OS`/`P`: verified directly (runner 6/6). Repo anchors on origin/main: `strong_cp_rp_half_cannot_forbid_cp_odd`
  (retained_no_go), `koide_emergent_time_eta_conjugation_parity` (retained_bounded),
  `strong_cp_operator_basis_and_mass_orientation` (audited_conditional),
  `strong_cp_epsilon_pseudotensor_oh_sign_bridge` (retained_bounded).
- This note sets no audit status; it evaluates the joint-basis bridge (fails) and localizes the residual to the
  shared chiral/holomorphic generation brick.
