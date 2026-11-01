# Mass-gap crossover reduction (conditional; closes no MG row)

Author checkpoint, 1 November 2026. **The four-dimensional continuum
existence and physical mass-gap target remains open.** This unit states a
conditional theorem (Theorem H) that reduces MG1 and MG3 of
[MASS_GAP_TARGET.md](MASS_GAP_TARGET.md) to one named estimate, the
crossover-window clustering bound (CW), plus MG2 and literature inputs. It
proves no new inequality on the Wilson measure. It also records three scope
controls on what any CW producer must use. No MG row changes status.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: conditional-support
independent_review: pending
MG_rows_closed: []
```

The long-form derivation, with the repo-note audit and the hybrid routes
considered, is [MASS_GAP_RECORD_RG_HYBRID_SKETCH.md](MASS_GAP_RECORD_RG_HYBRID_SKETCH.md).
Pinned inputs: this branch at `f76f6c649cff`; main-repo notes as cited
below, all `audit_status: unaudited` in `docs/audit/data/ledger/**`.

## 1. Setting

SU(N), N ≥ 2, Wilson action on Λ = (Z/LZ)^4, spacing a,

    dμ_{β,Λ}(U) = Z^{-1} exp{ (β/N) Σ_p Re Tr U_p } Π_e dU_e,   β = 2N/g_0^2,

with g_0(a) → 0 along the asymptotic-freedom trajectory at fixed lattice
Λ-parameter Λ_L. Observables 𝔄_+ are gauge-invariant local functions at
positive time; Θ is a link- or site-plane time reflection. The fourth
direction, the action and the trajectory are supplied; none is derived from
the framework axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md` lists them as open
gates).

## 2. Hypotheses and their status

| Tag | Hypothesis | Status |
|---|---|---|
| H1 | μ_{β,Λ} is reflection positive (link and site planes, periodic Λ, β ≥ 0) | Proved, literature: Osterwalder–Seiler 1978. Main-repo pieces (unaudited): two-slice temporal-gauge Gram PSD; one-link kernel c_λ(β) ≥ 0 |
| H2 | Transfer operator T = P_G M^{1/2} K M^{1/2} P_G is bounded, positive, compact on the gauge-invariant space, with simple top eigenvalue | Proved, literature: Lüscher 1977. Assembly from the two repo pieces: step A1 |
| H3 | Uniform reflected decay on a dense family ⇔ lattice gap | ⇐ is [MASS_GAP_TARGET.md](MASS_GAP_TARGET.md) §2; ⇒ is standard |
| H4 | Strong-coupling clustering, volume-uniform, β ≤ β_sc | Proved, literature (Osterwalder–Seiler cluster expansion). SU(2), 0 < β ≤ 1/32: [MASS_GAP_LOCAL_BLOCK_ASTRA.md](MASS_GAP_LOCAL_BLOCK_ASTRA.md), review pending |
| H5 | Balaban block-spin UV stability while g_k ≤ ḡ: effective actions (1/g_k^2)·Wilson + polymers, small-field analyticity, large-field suppression, asymptotic-freedom flow | Proved, literature, **finite volume, partition-function/effective-action bounds only** (Balaban, CMP 95–122). Not: infinite volume, general correlators, a gap |
| H6 | The flow reaches ḡ at a fixed physical scale ℓ_1 = c_1/Λ_L | Plausible bookkeeping from H5; not written |
| MG2 | Source transport of the original observables through the RG | Open; [MASS_GAP_CONSTRUCTION_ASTRA.md](MASS_GAP_CONSTRUCTION_ASTRA.md) covers its stated sectors only |
| **CW** | See §3 | **Open. The single irreducible estimate.** |

## 3. The open estimate CW

**CW (crossover-window clustering).** There exist ḡ ≤ g_* (the H5 range),
a fixed number n_* of further block steps (or a direct estimate), and
μ_* > 0 such that the effective measure at the physical scale
ℓ_* = L_b^{n_*} ℓ_1 has truncated gauge-invariant correlations bounded by
C e^{-μ_* d/ℓ_*}, uniformly in volume and in a, and such that the bound
transports to the original observables (MG2) with F-dependent prefactor and
onset only.

CW is the "quantitative crossover theorem" of MASS_GAP_TARGET §3 written as
one estimate. In words: no bulk transition between Balaban's ḡ and a
provable cluster regime, with a finite correlation length made quantitative.
For SU(2) the proved cluster regime starts at β ≤ 1/32, i.e. g^2 ≥ 128; no
theorem covers the window. The fixed positive handoff interval of Kirk v4
is a candidate CW supplier; [CROSSOVER_LITERATURE_BRIDGE_ASTRA.md](CROSSOVER_LITERATURE_BRIDGE_ASTRA.md)
and [its review](REVIEW_CROSSOVER_LITERATURE_BRIDGE_ASTRA.md) find that
its Lemma 3.26 operator-norm hypothesis does not give the displayed
core-size-independent determinant bound. A size-aware repair remains
possible, but no checked import supplies CW at this checkpoint.

## 4. Theorem H (conditional)

> Assume H1–H6, MG2 and CW. Then for every small enough a and every volume,
> the lattice Hamiltonian H_a = −a^{-1} log(T/‖T‖) satisfies
>
>     spec(H_a) ⊂ {0} ∪ [m_*, ∞),   ker H_a = span{Ω_a},
>     m_* = μ_*/ℓ_* = c·Λ_L,   c = μ_*/(c_1 L_b^{n_*}),
>
> with c independent of a and volume. With MG0 the bound passes to the
> continuum H by the fixed-t-first rule of MASS_GAP_TARGET §3. MG4
> (a non-empty Ω-perp) is a separate input. Without CW the statement is
> empty as a → 0: H1–H4 give only the fixed-spacing strong-coupling gap
> already in MASS_GAP_LOCAL_BLOCK_ASTRA.

### Steps

- **A1 (RP ⇒ positive compact transfer).** Temporal gauge; weight
  Π_t M^{1/2} K M^{1/2} with K = ⊗_e k_β(U_e V_e^†). c_λ(β) ≥ 0 makes
  convolution by k_β positive; k_β ∈ L^2 makes it Hilbert–Schmidt. Tensor
  products, sandwiching by M^{1/2} and the commuting Gauss projector keep
  positivity and compactness; k_β > 0 gives a simple top eigenvalue
  (Jentzsch). Standard (Lüscher 1977); the repo pieces are exactly its inputs.
- **A2 (decay ⇔ gap).** C_F(n) = ⟨v_F, T̂^n v_F⟩ = ∫ λ^n dν_F. A uniform
  rate m with F-dependent A_F, n_F confines ν_F to [0, e^{-ma}]; density
  gives H_a ≥ m on Ω-perp. This is MASS_GAP_TARGET §2 at fixed a.
- **A3 (volume).** Volume-uniform fixed-n bounds and RP survive weak limits;
  reconstruct and reapply A2. Uniqueness of the limit is known at β ≤ β_sc
  only; in the window CW must supply it.
- **A4 (strong coupling).** H4 gives A2's hypothesis at β ≤ β_sc. Proved,
  and the wrong end of the trajectory.
- **B0 (inductive hypothesis).** IH(k): (i) small-field analyticity with
  polymer bounds |E_k(X)| ≤ g_k^{κ_0} e^{-κ|X|}; (ii) large-field
  suppression; (iii) coupling flow. **Not** (iv) block-unit clustering at
  every scale (flag C1).
- **B1 (one step preserves IH).** Gauge-covariant blocking, shrinking
  analyticity domains, summable polymer bounds, large-field suppression,
  marginal coupling renormalization only. This is H5. RP of S_k is not
  needed: A1–A2 use RP of the original Wilson measure only.
- **B2 (flow to ḡ).** H6: k_1(a) → ∞ steps, fixed physical ℓ_1.
- **B3 (crossover).** CW. Routes: continue RG past ḡ to a cluster regime;
  a Dobrushin/Doob contraction (as in MASS_GAP_LOCAL_BLOCK_ASTRA) for the
  effective one-block kernel at ℓ_1; or an external import (none checked).
- **B4 (transport back).** MG2: write C_F(n) as an effective expectation of
  a source-dependent block functional; F-dependent A_F, t_F are allowed.
- **B5 (conclude).** A2 gives H_a ≥ m_* on Ω-perp uniformly in a and
  volume; MG0 carries it to the continuum.

## 5. What this adds to the ledger

1. MG1 + MG3 ⇐ CW + MG2 (+ H5 finite volume, H6). CW is stated as one estimate.
2. RP of the effective RG actions is not required.
3. Inductive RG hypotheses must not include block-unit clustering at every
   scale: at weak coupling the effective correlation length in block units
   is ~ 1/(Λ a_k) and diverges, so such a hypothesis is false or is MG1.
4. Scope control on CW producers: an argument that uses neither the
   non-abelian group nor d = 4 would equally give a gap for compact U(1)
   Wilson theory in d = 4, which has a proved massless phase (Guth 1980;
   Fröhlich–Spencer 1982). A d = 5 analogue is heuristic only (numerics).
   This is a test a candidate must pass, not a route-exhaustion claim.
5. Framework note: a permanent record readout R satisfies τ_n R = R, so
   ⟨R; τ_n R⟩ = Var(R) for all n. Records are superselection labels, cannot
   be the dense MG1 family, and the Record axiom
   (`docs/MINIMAL_AXIOMS_2026-06-29.md`) contains no decay clause.

## 6. Circularity flags

- **C1.** Block-unit decay at every RG scale: false at weak coupling, or MG1.
- **C2.** "Record clustering uniformly in a" in physical units is MG1 + MG3;
  adopting it would adopt the gap as an axiom.
- **C3.** A gap at β ≤ β_sc is at the wrong end of the trajectory.
- **C4.** Main-repo `SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  assumes no bulk critical point on 0 < β ≤ 6. CW contains that premise,
  uniformly along the trajectory. It is not evidence for CW.
- **C5.** The ASTRA mass-gap units cited here have pending or same-family
  review; they are used as supported, not verified.

## 7. Relation to PR #10132

`.claude/science/physics-loops/ym4d-hard-route-20261030/` (branch
`claude/ym4d-hard-route`, read at `5ad46ff72b19`) targets SU(2) existence
and non-triviality (NT1, NT2) and lists the mass gap as a later target. On a
common trajectory and observable family: a gap with non-empty Ω-perp gives
NT1; its NT1/NT2 witnesses give MG4 non-emptiness. Interface note on that
branch: `library/mass-gap-interface.md`. Trajectories and blocking differ
(hard-constraint vs soft kernel); the interface holds only on a common
hierarchy.

## 8. Not claimed

No MG row is closed. The fixed-spacing endpoint of
MASS_GAP_LOCAL_BLOCK_ASTRA is unchanged. H5 is used at its finite-volume
literature scope. CW is open and is the Clay-level step.

## 9. Update: Proposition S and Theorem H′

Details, scripts and outputs: [MASS_GAP_CW_CROSSOVER_ATTACK.md](MASS_GAP_CW_CROSSOVER_ATTACK.md), [checks/cw/](checks/cw/README.md).
**CW remains open; no MG row changes status.**

- **Prop. S (SU(2), d = 4; author-side, needs independent review).** For 0 < β < 1/9 the Wilson specification satisfies single-link
  Dobrushin uniqueness, with influence sum q(β) ≤ 9β. The ingredients are: 18 neighbours per link; Pinsker; KL ≤ ½λ_max(Cov)|δ|² for the
  tilted S³ family; and λ_max ≤ 1/4. The bound λ_max ≤ 1/4 is arb-certified on 29,602 cells. With RP and A2 this gives a volume-uniform
  m_lat ≥ −log(9β). Relative to MASS_GAP_LOCAL_BLOCK_ASTRA (Doob, β ≤ 1/32; 18β row bound, β < 1/18), this extends the H4 range for SU(2)
  to g² > 36 once reviewed. Validated numerics, not certified, give β < 0.117, and the conjectured sharp value is 3π/72 ≈ 0.131. The mass
  bound is weaker than the Doob bound at very small β.
- **KP negative.** A simple Kotecký–Preiss character expansion (a_j = I_{2j+1}/I_1, normalization checked to 2e-31) converges only for
  β ≲ 0.0078 (self-contained counting) or β ≲ 0.0109 (eΔ animal count). It does not beat 1/32.
- **MDTN finding.** The MDTN/ASQR truncation (arXiv:2502.14175; j_max = ½) is uncontrolled in the crossover: the certified tail
  τ_½(β) = Σ_{j>½} d_j² a_j exceeds 1 for β ≳ 1.5. Reaching τ < 1e-2 at β ≈ 2–3 needs j_max ≥ 3, i.e. 140 or more states per link. MDTN
  is not a CW tool. Local MDTN notes are not committed.
- **Theorem H′.** Theorem H holds with CW replaced by **CW′**: there is a finite link block V (diameter ℓ) and a reference specification
  γ_0 with Dobrushin–Shlosman-type block coefficient α_V(γ_0) ≤ 1 − 2η. In addition, after k_1(a) + n_* RG steps, the effective
  gauge-invariant specification is δ(η, V)-close to γ_0, uniformly in a and the volume, and MG2 transports the decay back. The block
  condition is a strict inequality, so it is open under perturbation. The DS continuous-spin form still has to be checked against the 1985
  original. New flags:
  - **C6.** The criterion must hold for the effective Bałaban action, which is not a finite-range link specification.
  - **C7.** The landing bound must not use the clustering it is meant to produce.
  - **C8.** Landing near strong-coupling Wilson means carrying the coupling from ḡ to g² ≈ 36. That is the entire non-perturbative problem.
  - **C9.** Martinelli–Olivieri finite-size criteria are for finite spin spaces only.
- **Evidence only (C4 applies).** SU(2) 4⁴/6⁴/8⁴ Monte Carlo runs show a smooth plaquette and hot/cold agreement. The dP/dβ peak near
  β ≈ 2.1–2.3 does not grow with L, and leading-order strong coupling fails beyond β ≈ 1.
- **Status delta.** H4: SU(2) β_sc from 1/32 to 1/9 *pending review of Prop. S*. CW is unchanged (open) and restated as CW′.
  MG1/MG3 are unchanged (conditional). MG_rows_closed: [].

## References

- K. Osterwalder, E. Seiler, Ann. Phys. 110 (1978) 440.
- M. Lüscher, Commun. Math. Phys. 54 (1977) 283.
- T. Bałaban, Commun. Math. Phys. 95, 96, 98, 99, 102, 109, 116, 119, 122 (1984–1989).
- A. Guth, Phys. Rev. D 21 (1980) 2291.
- J. Fröhlich, T. Spencer, Commun. Math. Phys. 83 (1982) 411.
- K. Osterwalder, R. Schrader, Commun. Math. Phys. 31 (1973) 83; 42 (1975) 281.
- R. L. Dobrushin, S. B. Shlosman, constructive criterion for uniqueness of Gibbs fields (1985).
- R. Kotecký, D. Preiss, Commun. Math. Phys. 103 (1986) 491.
- F. Martinelli, E. Olivieri, finite-volume mixing conditions (1994).
- S. Chandrasekharan, H. Siew, T. Bhattacharya, arXiv:2502.14175, Phys. Rev. D 111, 114502 (2025).
- H. D. Kirk, v4 (2 Aug 2026), Zenodo 21765806, as examined in CROSSOVER_LITERATURE_BRIDGE_ASTRA.
